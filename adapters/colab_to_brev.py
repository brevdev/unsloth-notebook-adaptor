"""
Colab to Brev Adapter

Converts Google Colab notebooks with Unsloth to NVIDIA Brev-compatible notebooks.
"""

import json
import logging
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict

from jinja2 import Environment, FileSystemLoader

from .base_adapter import NotebookAdapter

logger = logging.getLogger(__name__)


class ColabToBrevAdapter(NotebookAdapter):
    """Adapter for converting Colab notebooks to Brev format."""

    def __init__(self, templates_dir: Path):
        """
        Initialize the adapter.

        Args:
            templates_dir: Path to Jinja2 templates directory
        """
        super().__init__()
        self.templates_dir = templates_dir
        self.jinja_env = Environment(
            loader=FileSystemLoader(str(templates_dir)),
            trim_blocks=True,
            lstrip_blocks=True
        )

    def _register_default_conversions(self):
        """Register all conversion functions."""
        self.register_conversion('installation', self.convert_installation)
        self.register_conversion('magic_commands', self.convert_magic_commands)
        self.register_conversion('gpu_check', self.convert_gpu_check)
        self.register_conversion('storage', self.convert_storage)
        self.register_conversion('model_config', self.adapt_model_config)

    def convert_installation(self, code: str, config: Dict[str, Any]) -> str:
        """
        Convert Colab installation commands to Brev-compatible ones.

        Args:
            code: Source code
            config: Configuration dictionary

        Returns:
            Converted code
        """
        # Pattern for Colab Unsloth installation
        colab_pattern = r'!pip install\s+"?unsloth\[colab-new\].*?"?'
        
        if re.search(colab_pattern, code, re.IGNORECASE):
            logger.debug("Converting Colab installation to Brev")
            
            replacement = '''import subprocess
import sys

# Install Unsloth with conda variant for Brev
subprocess.check_call([
    sys.executable, "-m", "pip", "install",
    "unsloth[conda] @ git+https://github.com/unslothai/unsloth.git"
])'''
            
            code = re.sub(colab_pattern, replacement, code, flags=re.IGNORECASE)
        
        return code

    def convert_magic_commands(self, code: str, config: Dict[str, Any]) -> str:
        """
        Convert Jupyter magic commands to subprocess calls.

        Args:
            code: Source code
            config: Configuration dictionary

        Returns:
            Converted code
        """
        lines = code.split('\n')
        converted_lines = []
        
        for line in lines:
            stripped = line.lstrip()
            
            # Handle !command patterns
            if stripped.startswith('!'):
                indent = line[:len(line) - len(stripped)]
                command = stripped[1:].strip()
                
                # Special handling for pip
                if command.startswith('pip install'):
                    packages = command.replace('pip install', '').strip()
                    converted = f'{indent}subprocess.check_call([sys.executable, "-m", "pip", "install", {repr(packages)}])'
                # Special handling for nvidia-smi (non-critical)
                elif 'nvidia-smi' in command:
                    converted = f'{indent}subprocess.run([{repr(command)}], check=False, shell=True)'
                else:
                    # Generic command
                    converted = f'{indent}subprocess.run([{repr(command)}], check=True, shell=True)'
                
                converted_lines.append(converted)
                
                # Add imports if not present
                if 'import subprocess' not in code:
                    code = 'import subprocess\nimport sys\n\n' + code
                    
            # Handle %pip patterns
            elif stripped.startswith('%pip'):
                indent = line[:len(line) - len(stripped)]
                packages = stripped.replace('%pip install', '').strip()
                converted = f'{indent}subprocess.check_call([sys.executable, "-m", "pip", "install", {repr(packages)}])'
                converted_lines.append(converted)
                
                if 'import subprocess' not in code:
                    code = 'import subprocess\nimport sys\n\n' + code
            else:
                converted_lines.append(line)
        
        return '\n'.join(converted_lines)

    def convert_gpu_check(self, code: str, config: Dict[str, Any]) -> str:
        """
        Enhance GPU checking code.

        Args:
            code: Source code
            config: Configuration dictionary

        Returns:
            Converted code
        """
        # Look for GPU check patterns
        if 'gpu_stats' in code.lower() or 'torch.cuda' in code:
            # Add comprehensive GPU info at the start
            gpu_check = '''import subprocess
import sys

# Enhanced GPU check for NVIDIA Brev
print("=" * 60)
print("GPU Information")
print("=" * 60)

# Run nvidia-smi
subprocess.run(['nvidia-smi'], check=False)

# PyTorch CUDA info
import torch
print(f"\\nPyTorch CUDA Available: {torch.cuda.is_available()}")
if torch.cuda.is_available():
    print(f"CUDA Version: {torch.version.cuda}")
    print(f"Number of GPUs: {torch.cuda.device_count()}")
    for i in range(torch.cuda.device_count()):
        print(f"  GPU {i}: {torch.cuda.get_device_name(i)}")
        props = torch.cuda.get_device_properties(i)
        print(f"    Memory: {props.total_memory / 1024**3:.2f} GB")
print("=" * 60)

'''
            # Only add if not already present
            if 'Enhanced GPU check' not in code:
                code = gpu_check + '\n' + code
        
        return code

    def convert_storage(self, code: str, config: Dict[str, Any]) -> str:
        """
        Remove Google Drive dependencies and update paths.

        Args:
            code: Source code
            config: Configuration dictionary

        Returns:
            Converted code
        """
        # Remove Google Drive imports
        code = re.sub(r'from google\.colab import drive.*?\n', '', code)
        code = re.sub(r'drive\.mount\(.*?\).*?\n', '', code)
        
        # Replace paths
        code = code.replace('/content/drive/MyDrive', '/workspace')
        code = code.replace('/content/drive', '/workspace')
        code = code.replace('/content/', '/workspace/')
        
        return code

    def adapt_model_config(self, code: str, config: Dict[str, Any]) -> str:
        """
        Add device_map and adjust model configurations.

        Args:
            code: Source code
            config: Configuration dictionary

        Returns:
            Converted code
        """
        # Look for from_pretrained calls
        pattern = r'(FastLanguageModel\.from_pretrained\s*\([^)]+)'
        
        def add_device_map(match):
            call = match.group(1)
            # Check if device_map already present
            if 'device_map' not in call:
                # Add device_map before the closing parenthesis
                return call + ',\n    device_map="auto"'
            return call
        
        code = re.sub(pattern, add_device_map, code)
        
        # Update output directories
        code = re.sub(r'output_dir\s*=\s*["\'][^"\']*["\']', 
                     'output_dir="/workspace/outputs"', code)
        
        # Adjust batch sizes if specified in config
        if 'recommended_batch_size' in config:
            batch_size = config['recommended_batch_size']
            code = re.sub(r'per_device_train_batch_size\s*=\s*\d+',
                         f'per_device_train_batch_size={batch_size}', code)
        
        return code

    def _generate_requirements(self, config: Dict[str, Any]) -> str:
        """Generate requirements.txt from template."""
        template = self.jinja_env.get_template('requirements.txt.jinja2')
        return template.render(
            model_name=config.get('model_name', 'Unknown'),
            timestamp=datetime.now(timezone.utc).isoformat(),
            categories=config.get('categories', []),
            has_vision='vision' in config.get('categories', []),
            has_audio='audio' in config.get('categories', [])
        )

    def _generate_setup_script(self, config: Dict[str, Any]) -> str:
        """Generate setup.sh from template."""
        template = self.jinja_env.get_template('setup.sh.jinja2')
        return template.render(
            model_name=config.get('model_name', 'Unknown'),
            has_vision='vision' in config.get('categories', []),
            has_audio='audio' in config.get('categories', [])
        )

    def _generate_docker_compose(self, config: Dict[str, Any]) -> str:
        """Generate docker-compose.yml from template."""
        template = self.jinja_env.get_template('docker-compose.yml.jinja2')
        return template.render(
            model_name=config.get('model_name', 'Unknown'),
            launchable_name=config.get('launchable_name', 'unknown')
        )

    def _generate_readme(self, config: Dict[str, Any]) -> str:
        """Generate README.md from template."""
        template = self.jinja_env.get_template('README.md.jinja2')
        return template.render(
            model_name=config.get('model_name', 'Unknown'),
            launchable_name=config.get('launchable_name', 'unknown'),
            recommended_gpu=config.get('recommended_gpu', 'L4'),
            min_vram_gb=config.get('min_vram_gb', 16),
            recommended_batch_size=config.get('recommended_batch_size', 2),
            categories=config.get('categories', []),
            difficulty=config.get('difficulty', 'intermediate'),
            upstream_url=config.get('upstream_notebook_url', '#')
        )

    def _generate_brev_config(self, config: Dict[str, Any]) -> str:
        """Generate .brevconfig.json."""
        brev_config = {
            "name": config.get('model_name', 'Unknown Model'),
            "description": f"Fine-tune {config.get('model_name')} with Unsloth on NVIDIA GPUs",
            "version": "1.0.0",
            "gpu": {
                "tier": config.get('recommended_gpu', 'L4'),
                "min_vram_gb": config.get('min_vram_gb', 16),
                "multi_gpu": config.get('multi_gpu', False)
            },
            "ports": [8888],
            "environment": {
                "JUPYTER_ENABLE_LAB": "yes"
            },
            "tags": ["unsloth", "fine-tuning"] + config.get('categories', []),
            "upstream": {
                "source": "unslothai/notebooks",
                "notebook_url": config.get('upstream_notebook_url', '#'),
                "last_synced": datetime.now(timezone.utc).isoformat()
            }
        }
        return json.dumps(brev_config, indent=2)

    def generate_companion_files(
        self,
        notebook_path: Path,
        config: Dict[str, Any]
    ) -> Dict[str, str]:
        """
        Generate all companion files for the notebook.

        Args:
            notebook_path: Path to the source notebook
            config: Configuration dictionary

        Returns:
            Dictionary mapping filenames to their content
        """
        return {
            'requirements.txt': self._generate_requirements(config),
            'setup.sh': self._generate_setup_script(config),
            'docker-compose.yml': self._generate_docker_compose(config),
            'README.md': self._generate_readme(config),
            '.brevconfig.json': self._generate_brev_config(config)
        }

