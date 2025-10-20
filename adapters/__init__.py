"""
Unsloth to Brev Notebook Adapter Package

This package provides adapters for converting Unsloth Colab notebooks
to NVIDIA Brev-compatible launchables.
"""

from .base_adapter import NotebookAdapter
from .colab_to_brev import ColabToBrevAdapter
from .model_configs import MODEL_CONFIGS, get_config_for_notebook

__all__ = [
    'NotebookAdapter',
    'ColabToBrevAdapter',
    'MODEL_CONFIGS',
    'get_config_for_notebook',
]

__version__ = '1.0.0'

