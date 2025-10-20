"""
Tests for notebook conversion functions.
"""

import pytest
from pathlib import Path

from adapters import ColabToBrevAdapter


@pytest.fixture
def templates_dir():
    """Get templates directory."""
    return Path(__file__).parent.parent / 'templates'


@pytest.fixture
def adapter(templates_dir):
    """Create adapter instance."""
    return ColabToBrevAdapter(templates_dir)


@pytest.fixture
def test_config():
    """Test configuration."""
    return {
        'model_name': 'Test Model',
        'launchable_name': 'test-model',
        'recommended_gpu': 'L4',
        'min_vram_gb': 16,
        'recommended_batch_size': 4,
        'categories': ['text-generation', 'fine-tuning'],
        'difficulty': 'beginner',
        'upstream_notebook_url': 'https://example.com/notebook.ipynb',
        'multi_gpu': False
    }


def test_convert_installation(adapter, test_config):
    """Test installation conversion."""
    # Colab installation pattern
    code = '''!pip install "unsloth[colab-new] @ git+https://github.com/unslothai/unsloth.git"'''
    
    result = adapter.convert_installation(code, test_config)
    
    # Check that colab-specific code is removed
    assert 'colab-new' not in result
    assert '!pip' not in result
    
    # Check that conda variant is added
    assert 'conda' in result
    assert 'subprocess.check_call' in result
    assert 'sys.executable' in result


def test_convert_installation_no_change(adapter, test_config):
    """Test installation conversion when no Colab pattern present."""
    code = '''import torch
print("Hello world")'''
    
    result = adapter.convert_installation(code, test_config)
    
    # Should remain unchanged
    assert result == code


def test_convert_magic_commands_pip(adapter, test_config):
    """Test magic command conversion for pip."""
    code = '''!pip install numpy
%pip install pandas'''
    
    result = adapter.convert_magic_commands(code, test_config)
    
    # Check removal of magic commands
    assert '!pip' not in result
    assert '%pip' not in result
    
    # Check subprocess added
    assert 'subprocess.check_call' in result
    assert 'sys.executable' in result


def test_convert_magic_commands_nvidia_smi(adapter, test_config):
    """Test magic command conversion for nvidia-smi."""
    code = '''!nvidia-smi'''
    
    result = adapter.convert_magic_commands(code, test_config)
    
    # Check removal of magic command
    assert '!nvidia-smi' not in result
    
    # Check subprocess added (non-critical)
    assert 'subprocess.run' in result
    assert 'check=False' in result


def test_convert_storage_drive_mount(adapter, test_config):
    """Test removal of Google Drive mounting."""
    code = '''from google.colab import drive
drive.mount('/content/drive')
model_path = '/content/drive/MyDrive/models/llama'
output_path = '/content/outputs'
'''
    
    result = adapter.convert_storage(code, test_config)
    
    # Check Google Drive code removed
    assert 'google.colab' not in result
    assert 'drive.mount' not in result
    
    # Check paths updated
    assert '/workspace' in result
    assert '/content/drive/MyDrive' not in result
    assert '/content/' not in result or '/workspace/' in result


def test_convert_storage_paths(adapter, test_config):
    """Test path conversions."""
    code = '''path1 = "/content/models"
path2 = "/content/drive/MyDrive/data"
'''
    
    result = adapter.convert_storage(code, test_config)
    
    # Check paths converted
    assert '/workspace' in result
    assert '/content/' not in result


def test_adapt_model_config_device_map(adapter, test_config):
    """Test adding device_map to model loading."""
    code = '''model = FastLanguageModel.from_pretrained(
    "unsloth/llama-3-8b",
    max_seq_length=2048,
    load_in_4bit=True
)'''
    
    result = adapter.adapt_model_config(code, test_config)
    
    # Check device_map added
    assert 'device_map="auto"' in result


def test_adapt_model_config_existing_device_map(adapter, test_config):
    """Test that existing device_map is not duplicated."""
    code = '''model = FastLanguageModel.from_pretrained(
    "unsloth/llama-3-8b",
    device_map="cuda:0"
)'''
    
    result = adapter.adapt_model_config(code, test_config)
    
    # Should not add another device_map
    assert result.count('device_map') == 1


def test_adapt_model_config_output_dir(adapter, test_config):
    """Test output directory update."""
    code = '''output_dir = "/content/outputs"'''
    
    result = adapter.adapt_model_config(code, test_config)
    
    # Check output_dir updated
    assert '/workspace/outputs' in result


def test_adapt_model_config_batch_size(adapter, test_config):
    """Test batch size adjustment."""
    code = '''per_device_train_batch_size=2'''
    
    result = adapter.adapt_model_config(code, test_config)
    
    # Should use recommended batch size from config
    expected_batch_size = test_config['recommended_batch_size']
    assert f'per_device_train_batch_size={expected_batch_size}' in result


def test_generate_companion_files(adapter, test_config):
    """Test companion files generation."""
    notebook_path = Path('/fake/path/test.ipynb')
    
    companion_files = adapter.generate_companion_files(notebook_path, test_config)
    
    # Check all required files present
    assert 'requirements.txt' in companion_files
    assert 'setup.sh' in companion_files
    assert 'docker-compose.yml' in companion_files
    assert 'README.md' in companion_files
    assert '.brevconfig.json' in companion_files
    
    # Check files are not empty
    for filename, content in companion_files.items():
        assert len(content) > 0, f"{filename} is empty"


def test_generate_requirements(adapter, test_config):
    """Test requirements.txt generation."""
    requirements = adapter._generate_requirements(test_config)
    
    # Check essential packages present
    assert 'torch' in requirements
    assert 'transformers' in requirements
    assert 'accelerate' in requirements
    assert 'peft' in requirements
    assert 'jupyterlab' in requirements


def test_generate_requirements_vision(adapter, test_config):
    """Test requirements.txt with vision dependencies."""
    test_config['categories'] = ['vision', 'fine-tuning']
    
    requirements = adapter._generate_requirements(test_config)
    
    # Check vision packages present
    assert 'pillow' in requirements.lower()
    assert 'torchvision' in requirements.lower()


def test_generate_requirements_audio(adapter, test_config):
    """Test requirements.txt with audio dependencies."""
    test_config['categories'] = ['audio', 'fine-tuning']
    
    requirements = adapter._generate_requirements(test_config)
    
    # Check audio packages present
    assert 'librosa' in requirements.lower()
    assert 'soundfile' in requirements.lower()


def test_generate_setup_script(adapter, test_config):
    """Test setup.sh generation."""
    setup_script = adapter._generate_setup_script(test_config)
    
    # Check script structure
    assert '#!/bin/bash' in setup_script
    assert 'set -e' in setup_script
    assert 'pip install' in setup_script
    assert 'unsloth[conda]' in setup_script
    assert 'mkdir -p /workspace' in setup_script


def test_generate_docker_compose(adapter, test_config):
    """Test docker-compose.yml generation."""
    docker_compose = adapter._generate_docker_compose(test_config)
    
    # Check Docker Compose structure
    assert 'version:' in docker_compose
    assert 'services:' in docker_compose
    assert 'nvidia/cuda' in docker_compose
    assert 'runtime: nvidia' in docker_compose
    assert '8888:8888' in docker_compose


def test_generate_readme(adapter, test_config):
    """Test README.md generation."""
    readme = adapter._generate_readme(test_config)
    
    # Check README structure
    assert '# Test Model' in readme
    assert 'Quick Start' in readme
    assert 'Requirements' in readme
    assert test_config['recommended_gpu'] in readme
    assert str(test_config['min_vram_gb']) in readme


def test_generate_brev_config(adapter, test_config):
    """Test .brevconfig.json generation."""
    import json
    
    brev_config_str = adapter._generate_brev_config(test_config)
    brev_config = json.loads(brev_config_str)
    
    # Check structure
    assert 'name' in brev_config
    assert 'gpu' in brev_config
    assert 'ports' in brev_config
    assert 'tags' in brev_config
    assert 'upstream' in brev_config
    
    # Check values
    assert brev_config['name'] == test_config['model_name']
    assert brev_config['gpu']['tier'] == test_config['recommended_gpu']
    assert 8888 in brev_config['ports']
    assert 'unsloth' in brev_config['tags']

