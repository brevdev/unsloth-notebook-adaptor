"""
Integration tests for notebook conversion.
"""

import json
import pytest
import tempfile
from pathlib import Path

import nbformat
from nbformat.v4 import new_code_cell, new_notebook

from adapters import ColabToBrevAdapter, get_config_for_notebook


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
        'model_name': 'Llama 3.1 (8B)',
        'launchable_name': 'llama-3.1-8b',
        'recommended_gpu': 'L4',
        'min_vram_gb': 16,
        'recommended_batch_size': 4,
        'categories': ['text-generation', 'fine-tuning'],
        'difficulty': 'beginner',
        'upstream_notebook_url': 'https://example.com/notebook.ipynb',
        'multi_gpu': False
    }


@pytest.fixture
def sample_notebook():
    """Create a sample Colab notebook."""
    cells = [
        new_code_cell('!pip install "unsloth[colab-new] @ git+https://github.com/unslothai/unsloth.git"'),
        new_code_cell('!nvidia-smi'),
        new_code_cell('''from google.colab import drive
drive.mount('/content/drive')'''),
        new_code_cell('''from unsloth import FastLanguageModel

model = FastLanguageModel.from_pretrained(
    "unsloth/llama-3-8b",
    max_seq_length=2048,
    load_in_4bit=True
)'''),
        new_code_cell('''output_dir = "/content/outputs"''')
    ]
    
    notebook = new_notebook(cells=cells)
    return notebook


def test_notebook_adaptation(adapter, sample_notebook, test_config, tmp_path):
    """Test full notebook adaptation."""
    # Save sample notebook
    notebook_path = tmp_path / 'test_notebook.ipynb'
    with open(notebook_path, 'w') as f:
        nbformat.write(sample_notebook, f)
    
    # Adapt notebook
    adapted_notebook, companion_files = adapter.adapt(notebook_path, test_config)
    
    # Check that header cell was added
    assert len(adapted_notebook.cells) == len(sample_notebook.cells) + 1
    assert adapted_notebook.cells[0].cell_type == 'markdown'
    assert 'Powered by Brev' in adapted_notebook.cells[0].source
    
    # Check that conversions were applied to code cells
    all_code = '\n'.join(
        cell.source for cell in adapted_notebook.cells if cell.cell_type == 'code'
    )
    
    # Should not have Colab-specific code
    assert 'colab-new' not in all_code
    assert 'google.colab' not in all_code
    
    # Should have Brev-compatible code
    assert 'conda' in all_code
    assert 'device_map="auto"' in all_code
    assert '/workspace' in all_code
    
    # Check companion files
    assert len(companion_files) == 5


def test_companion_files_content(adapter, sample_notebook, test_config, tmp_path):
    """Test content of companion files."""
    notebook_path = tmp_path / 'test_notebook.ipynb'
    with open(notebook_path, 'w') as f:
        nbformat.write(sample_notebook, f)
    
    _, companion_files = adapter.adapt(notebook_path, test_config)
    
    # Test requirements.txt
    requirements = companion_files['requirements.txt']
    assert 'torch' in requirements
    assert 'unsloth' in requirements.lower()
    
    # Test setup.sh
    setup_sh = companion_files['setup.sh']
    assert '#!/bin/bash' in setup_sh
    assert 'pip install' in setup_sh
    
    # Test docker-compose.yml
    docker_compose = companion_files['docker-compose.yml']
    assert 'nvidia/cuda' in docker_compose
    assert '8888:8888' in docker_compose
    
    # Test README.md
    readme = companion_files['README.md']
    assert test_config['model_name'] in readme
    assert 'Quick Start' in readme
    
    # Test .brevconfig.json
    brev_config = json.loads(companion_files['.brevconfig.json'])
    assert brev_config['name'] == test_config['model_name']
    assert brev_config['gpu']['tier'] == test_config['recommended_gpu']


def test_get_config_for_notebook():
    """Test configuration lookup by notebook name."""
    # Test exact match
    config = get_config_for_notebook('llama-3.1-8b')
    assert config['model_name'] == 'Llama 3.1 (8B)'
    
    # Test with .ipynb extension
    config = get_config_for_notebook('llama-3.1-8b.ipynb')
    assert config['model_name'] == 'Llama 3.1 (8B)'
    
    # Test fuzzy match
    config = get_config_for_notebook('Llama_3.1_(8B).ipynb')
    assert 'llama' in config['model_name'].lower()
    
    # Test unknown model (should return default)
    config = get_config_for_notebook('unknown-model-xyz')
    assert config['model_name'] == 'Unknown Model'
    assert config['recommended_gpu'] == 'L4'


def test_multiple_conversions_idempotent(adapter, test_config):
    """Test that running conversions multiple times is idempotent."""
    code = '!pip install numpy'
    
    # First conversion
    result1 = adapter.convert_magic_commands(code, test_config)
    
    # Second conversion on result
    result2 = adapter.convert_magic_commands(result1, test_config)
    
    # Should not change further (except for import additions)
    assert 'subprocess' in result1
    assert 'subprocess' in result2
    assert '!pip' not in result1
    assert '!pip' not in result2

