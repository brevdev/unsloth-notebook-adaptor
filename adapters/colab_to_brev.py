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
        self.register_conversion('colab_conditionals', self.clean_colab_conditionals)
        self.register_conversion('colab_links', self.clean_colab_links)
        self.register_conversion('magic_commands', self.convert_magic_commands)
        self.register_conversion('gpu_check', self.convert_gpu_check)
        self.register_conversion('storage', self.convert_storage)
        self.register_conversion('model_config', self.adapt_model_config)
        self.register_conversion('generation_cache', self.setup_generation_cache)

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

    def clean_colab_conditionals(self, code: str, config: Dict[str, Any]) -> str:
        """
        Remove Colab-specific conditional installation logic.

        Args:
            code: Source code
            config: Configuration dictionary

        Returns:
            Cleaned code
        """
        # Check if this is a Colab conditional installation cell
        # (Has %%capture and COLAB_ environment check)
        if '%%capture' in code and 'COLAB_' in code:
            logger.debug("Removing Colab conditional installation block")
            # Replace with environment check + installation using uv
            return '''# Environment Check for Brev
import sys
import os
import shutil

print(f"Python executable: {sys.executable}")
print(f"Python version: {sys.version}")

# Configure PyTorch cache directories to avoid permission errors
# MUST be set before any torch imports
# Prefer /ephemeral for Brev instances (larger scratch space)

# Test if /ephemeral exists and is actually writable (not just readable)
use_ephemeral = False
if os.path.exists("/ephemeral"):
    try:
        test_file = "/ephemeral/.write_test"
        with open(test_file, "w") as f:
            f.write("test")
        os.remove(test_file)
        use_ephemeral = True
    except (PermissionError, OSError):
        pass

if use_ephemeral:
    cache_base = "/ephemeral/torch_cache"
    triton_cache = "/ephemeral/triton_cache"
    print("Using /ephemeral for cache (Brev scratch space)")
else:
    cache_base = os.path.expanduser("~/.cache/torch/inductor")
    triton_cache = os.path.expanduser("~/.cache/triton")
    print("Using home directory for cache")

os.environ["TORCHINDUCTOR_CACHE_DIR"] = cache_base
os.environ["TORCH_COMPILE_DIR"] = cache_base
os.environ["TRITON_CACHE_DIR"] = triton_cache
os.environ["XDG_CACHE_HOME"] = os.path.expanduser("~/.cache")

# Create cache directories with proper permissions
for cache_dir in [cache_base, triton_cache, os.environ["XDG_CACHE_HOME"]]:
    os.makedirs(cache_dir, mode=0o755, exist_ok=True)

# Clean up any old compiled caches that point to /tmp
old_cache = os.path.join(os.getcwd(), "unsloth_compiled_cache")
if os.path.exists(old_cache):
    print(f"⚠️  Removing old compiled cache: {old_cache}")
    shutil.rmtree(old_cache, ignore_errors=True)

print(f"✅ PyTorch cache: {cache_base}")

try:
    from unsloth import FastLanguageModel
    print("\\n✅ Unsloth already available")
    print(f"   Location: {FastLanguageModel.__module__}")
except ImportError:
    print("\\n⚠️  Unsloth not found - will install")

# Install unsloth using uv (the package manager for this environment)
import subprocess

print(f"\\nInstalling packages into: {sys.executable}")
print("Using uv package manager...\\n")

try:
    # Use uv to install packages into the current environment
    subprocess.check_call(["uv", "pip", "install", "unsloth"])
    subprocess.check_call(["uv", "pip", "install", "transformers==4.56.2"])
    subprocess.check_call(["uv", "pip", "install", "--no-deps", "trl==0.22.2"])
    print("\\n✅ Installation complete")
except FileNotFoundError:
    print("❌ 'uv' command not found. Trying alternative method...")
    # Fallback: install pip into venv first, then use it
    subprocess.check_call([sys.executable, "-m", "ensurepip", "--upgrade"])
    subprocess.check_call([sys.executable, "-m", "pip", "install", "unsloth"])
    subprocess.check_call([sys.executable, "-m", "pip", "install", "transformers==4.56.2"])
    subprocess.check_call([sys.executable, "-m", "pip", "install", "--no-deps", "trl==0.22.2"])
    print("\\n✅ Installation complete")

# Verify installation
try:
    from unsloth import FastLanguageModel
    print("✅ Unsloth is now available")
except ImportError as e:
    print(f"❌ Installation failed: {e}")
    print("⚠️  Please restart kernel and try again")
    raise'''
        
        # Remove standalone %%capture magic commands (won't work outside IPython)
        if '%%capture' in code:
            logger.debug("Removing standalone %%capture magic command")
            code = re.sub(r'%%capture\s*\n', '', code)
        
        return code

    def clean_colab_links(self, code: str, config: Dict[str, Any]) -> str:
        """
        Remove or update 'Some other links' sections and inline Colab links.

        Args:
            code: Source code
            config: Configuration dictionary

        Returns:
            Cleaned code
        """
        # 1. Replace inline Colab/GitHub links with direct GitHub links
        # Pattern: https://colab.research.google.com/github/... -> https://github.com/...
        code = re.sub(
            r'https://colab\.research\.google\.com/github/([^\s\)]+)',
            r'https://github.com/\1',
            code
        )
        
        # 2. Remove Google Drive Colab links (can't be converted)
        # Pattern: https://colab.research.google.com/drive/... -> generic message
        code = re.sub(
            r'\[([^\]]+)\]\(https://colab\.research\.google\.com/drive/[^\)]+\)',
            r'(additional notebook - see Unsloth documentation)',
            code
        )
        
        # 3. Remove Colab badge images (markdown format)
        code = re.sub(
            r'!\[Open In Colab\]\(https://colab\.research\.google\.com/assets/colab-badge\.svg\)',
            '',
            code,
            flags=re.IGNORECASE
        )
        code = re.sub(
            r'\[!\[.*?\]\(https://colab\.research\.google\.com/assets/colab-badge\.svg\)\]\([^\)]+\)',
            '',
            code
        )
        
        # 4. Remove Colab badge images (HTML format)
        code = re.sub(
            r'<a\s+href="[^"]*"\s+target="_parent"><img\s+src="https://colab\.research\.google\.com/assets/colab-badge\.svg"[^>]*></a>',
            '',
            code,
            flags=re.IGNORECASE
        )
        
        # 2. Pattern for "Some other links" section with Colab references
        links_pattern = r'Some other links:.*?(?:Free Colab|Free notebook).*?(?=\n\n[A-Z]|\Z)'
        
        if re.search(links_pattern, code, re.DOTALL | re.IGNORECASE):
            logger.debug("Removing Colab links section")
            # Replace with Brev-specific links
            replacement = '''**Additional Resources:**

- 📚 [Unsloth Documentation](https://docs.unsloth.ai) - Complete guides and examples
- 💬 [Unsloth Discord](https://discord.gg/unsloth) - Community support
- 📖 [More Notebooks](https://github.com/unslothai/notebooks) - Full collection on GitHub
- 🚀 [Brev Documentation](https://docs.nvidia.com/brev) - Deploy and scale on NVIDIA GPUs'''
            
            code = re.sub(links_pattern, replacement, code, flags=re.DOTALL | re.IGNORECASE)
        
        return code

    def convert_magic_commands(self, code: str, config: Dict[str, Any]) -> str:
        """
        Convert Jupyter magic commands to subprocess calls.
        Handles multiline commands with backslash continuation.

        Args:
            code: Source code
            config: Configuration dictionary

        Returns:
            Converted code
        """
        lines = code.split('\n')
        converted_lines = []
        needs_imports = False
        i = 0
        
        while i < len(lines):
            line = lines[i]
            stripped = line.lstrip()
            
            # Handle !command patterns (including multiline)
            if stripped.startswith('!'):
                needs_imports = True
                indent = line[:len(line) - len(stripped)]
                command = stripped[1:].strip()
                
                # Check for multiline command (ends with \)
                if command.endswith('\\'):
                    # Accumulate continuation lines
                    full_command_parts = [command[:-1].strip()]  # Remove trailing \
                    i += 1
                    
                    # Collect continuation lines
                    while i < len(lines):
                        cont_line = lines[i].strip()
                        if cont_line.endswith('\\'):
                            full_command_parts.append(cont_line[:-1].strip())
                            i += 1
                        else:
                            # Last line of the command
                            full_command_parts.append(cont_line)
                            break
                    
                    # Join with spaces
                    command = ' '.join(full_command_parts)
                
                # Special handling for pip
                if command.startswith('pip install'):
                    packages = command.replace('pip install', '').strip()
                    # Use sys.executable -m pip to install to kernel's Python
                    converted = f'{indent}subprocess.check_call([sys.executable, "-m", "pip", "install", {repr(packages)}])'
                # Special handling for nvidia-smi (non-critical)
                elif 'nvidia-smi' in command:
                    converted = f'{indent}subprocess.run([{repr(command)}], check=False, shell=True)'
                else:
                    # Generic command - use shell=True for complex commands
                    converted = f'{indent}subprocess.run([{repr(command)}], check=True, shell=True)'
                
                converted_lines.append(converted)
                    
            # Handle %pip patterns
            elif stripped.startswith('%pip'):
                needs_imports = True
                indent = line[:len(line) - len(stripped)]
                packages = stripped.replace('%pip install', '').strip()
                # Use sys.executable -m pip to install to kernel's Python
                converted = f'{indent}subprocess.check_call([sys.executable, "-m", "pip", "install", {repr(packages)}])'
                converted_lines.append(converted)
            else:
                converted_lines.append(line)
            
            i += 1
        
        result = '\n'.join(converted_lines)
        
        # Add imports at the beginning if needed and not already present
        if needs_imports:
            imports_needed = []
            if 'import subprocess' not in result:
                imports_needed.append('import subprocess')
            if 'import sys' not in result:
                imports_needed.append('import sys')
            
            if imports_needed:
                result = '\n'.join(imports_needed) + '\n\n' + result
        
        return result

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
                # Strip any trailing whitespace and commas before adding device_map
                call = call.rstrip()
                if call.endswith(','):
                    call = call.rstrip(',').rstrip()
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

    def setup_generation_cache(self, code: str, config: Dict[str, Any]) -> str:
        """
        Add cache directory setup before model.generate() calls to avoid /tmp permission errors.

        Args:
            code: Source code
            config: Configuration dictionary

        Returns:
            Converted code with cache setup
        """
        # Check if this cell has model.generate() or similar generation calls
        if not re.search(r'(model\.generate|FastLanguageModel\.generate|trainer\.generate)', code):
            return code
        
        # Check if cache setup is already present
        if 'TORCHINDUCTOR_CACHE_DIR' in code or 'torch_cache' in code:
            return code
        
        logger.debug("Adding torch cache setup before generation call")
        
        # Add cache setup at the beginning of the cell
        cache_setup = '''# Fix torch compilation cache permissions
import os
import shutil

# Test if /ephemeral is writable (not just readable)
use_ephemeral = False
if os.path.exists("/ephemeral"):
    try:
        test_file = "/ephemeral/.write_test"
        with open(test_file, "w") as f:
            f.write("test")
        os.remove(test_file)
        use_ephemeral = True
    except (PermissionError, OSError):
        pass

if use_ephemeral:
    cache_dir = "/ephemeral/torch_cache"
else:
    cache_dir = os.path.expanduser("~/.cache/torch/inductor")

os.makedirs(cache_dir, exist_ok=True)

# Set PyTorch to use this directory
os.environ["TORCHINDUCTOR_CACHE_DIR"] = cache_dir
os.environ["TORCH_COMPILE_DIR"] = cache_dir

# Clean up any old compiled caches
old_cache = os.path.join(os.getcwd(), "unsloth_compiled_cache")
if os.path.exists(old_cache):
    shutil.rmtree(old_cache, ignore_errors=True)

print(f"✅ Torch cache: {cache_dir}")

'''
        
        return cache_setup + code

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

