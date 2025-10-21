"""
Base Notebook Adapter Class

Provides the foundation for converting notebooks between different platforms.
"""

import json
import logging
from abc import ABC, abstractmethod
from datetime import datetime
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional, Tuple

import nbformat
from nbformat.v4 import new_markdown_cell

logger = logging.getLogger(__name__)


class NotebookAdapter(ABC):
    """Base class for notebook adapters."""

    def __init__(self):
        """Initialize the adapter with a registry of conversion functions."""
        self.conversions: Dict[str, Callable] = {}
        self._register_default_conversions()

    def _register_default_conversions(self):
        """Register default conversion functions. Override in subclasses."""
        pass

    def register_conversion(self, name: str, func: Callable) -> None:
        """
        Register a conversion function.

        Args:
            name: Name of the conversion (e.g., 'installation', 'magic_commands')
            func: Callable that takes (code: str, config: dict) and returns str
        """
        self.conversions[name] = func
        logger.debug(f"Registered conversion: {name}")

    def adapt(
        self,
        notebook_path: Path,
        config: Dict[str, Any]
    ) -> Tuple[nbformat.NotebookNode, Dict[str, str]]:
        """
        Adapt a notebook to the target platform.

        Args:
            notebook_path: Path to the source notebook
            config: Configuration dictionary for the model

        Returns:
            Tuple of (adapted_notebook, companion_files_dict)
        """
        logger.info(f"Adapting notebook: {notebook_path}")

        # Load the notebook
        with open(notebook_path, 'r', encoding='utf-8') as f:
            notebook = nbformat.read(f, as_version=4)

        # Add header cell
        header_cell = self.create_header_cell(notebook_path, config)
        notebook.cells.insert(0, header_cell)

        # Process each code and markdown cell
        for cell in notebook.cells:
            if cell.cell_type == 'code':
                original_source = cell.source
                adapted_source = self._apply_conversions(original_source, config)
                cell.source = adapted_source
                # Clear outputs and execution state
                cell.outputs = []
                cell.execution_count = None
            elif cell.cell_type == 'markdown':
                # Apply conversions to markdown cells too (for cleaning links, etc.)
                original_source = cell.source
                adapted_source = self._apply_conversions(original_source, config)
                cell.source = adapted_source

        # Clean notebook-level metadata (remove widget state from Colab)
        if 'widgets' in notebook.metadata:
            del notebook.metadata['widgets']
            logger.debug("Removed widget state metadata from notebook")

        # Generate companion files
        companion_files = self.generate_companion_files(notebook_path, config)

        logger.info(f"Adaptation complete for {notebook_path}")
        return notebook, companion_files

    def _apply_conversions(self, code: str, config: Dict[str, Any]) -> str:
        """
        Apply all registered conversions to code.

        Args:
            code: Source code to convert
            config: Configuration dictionary

        Returns:
            Converted code
        """
        result = code
        for name, func in self.conversions.items():
            try:
                result = func(result, config)
            except Exception as e:
                logger.warning(f"Conversion '{name}' failed: {e}")
        return result

    def create_header_cell(
        self,
        notebook_path: Path,
        config: Dict[str, Any]
    ) -> nbformat.NotebookNode:
        """
        Create a header cell with Brev information.

        Args:
            notebook_path: Path to the source notebook
            config: Configuration dictionary

        Returns:
            Markdown cell with styled header
        """
        model_name = config.get('model_name', 'Unknown Model')
        upstream_url = config.get('upstream_notebook_url', '#')
        gpu = config.get('recommended_gpu', 'N/A')
        vram = config.get('min_vram_gb', 'N/A')
        batch_size = config.get('recommended_batch_size', 'N/A')
        categories = ', '.join(config.get('categories', []))

        # Convert Colab URL to GitHub URL
        if 'colab.research.google.com' in upstream_url:
            # Extract notebook path from Colab URL
            # Format: https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Notebook.ipynb
            parts = upstream_url.split('/github/')
            if len(parts) > 1:
                github_url = f"https://github.com/{parts[1]}"
            else:
                github_url = upstream_url
        else:
            github_url = upstream_url
        
        header_markdown = f"""# 🤙 {model_name} on NVIDIA Brev

<div style="background: linear-gradient(90deg, #00ff87 0%, #60efff 100%); padding: 1px; border-radius: 8px; margin: 20px 0;">
    <div style="background: #0a0a0a; padding: 20px; border-radius: 7px;">
        <p style="color: #60efff; margin: 0;"><strong>⚡ Powered by Brev</strong> | Converted from <a href="{github_url}" style="color: #00ff87;">Unsloth Notebook</a></p>
    </div>
</div>

## 📋 Configuration

<table style="width: auto; margin-left: 0; border-collapse: collapse; border: 2px solid #808080;">
    <thead>
        <tr style="border-bottom: 2px solid #808080;">
            <th style="text-align: left; padding: 8px 12px; border-right: 2px solid #808080; font-weight: bold;">Parameter</th>
            <th style="text-align: left; padding: 8px 12px; font-weight: bold;">Value</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="text-align: left; padding: 8px 12px; border-right: 1px solid #808080;"><strong>Model</strong></td>
            <td style="text-align: left; padding: 8px 12px;">{model_name}</td>
        </tr>
        <tr>
            <td style="text-align: left; padding: 8px 12px; border-right: 1px solid #808080;"><strong>Recommended GPU</strong></td>
            <td style="text-align: left; padding: 8px 12px;">{gpu}</td>
        </tr>
        <tr>
            <td style="text-align: left; padding: 8px 12px; border-right: 1px solid #808080;"><strong>Min VRAM</strong></td>
            <td style="text-align: left; padding: 8px 12px;">{vram} GB</td>
        </tr>
        <tr>
            <td style="text-align: left; padding: 8px 12px; border-right: 1px solid #808080;"><strong>Batch Size</strong></td>
            <td style="text-align: left; padding: 8px 12px;">{batch_size}</td>
        </tr>
        <tr>
            <td style="text-align: left; padding: 8px 12px; border-right: 1px solid #808080;"><strong>Categories</strong></td>
            <td style="text-align: left; padding: 8px 12px;">{categories}</td>
        </tr>
    </tbody>
</table>

## 🔧 Key Adaptations for Brev

- ✅ Replaced Colab-specific installation with conda-based Unsloth
- ✅ Converted magic commands to subprocess calls
- ✅ Removed Google Drive dependencies
- ✅ Updated paths from `/content/` to `/workspace/`
- ✅ Added `device_map="auto"` for multi-GPU support
- ✅ Optimized batch sizes for NVIDIA GPUs

## 📚 Resources

- [Unsloth Documentation](https://docs.unsloth.ai/)
- [Brev Documentation](https://docs.nvidia.com/brev)
- [Original Notebook]({upstream_url})
"""
        return new_markdown_cell(header_markdown)

    @abstractmethod
    def generate_companion_files(
        self,
        notebook_path: Path,
        config: Dict[str, Any]
    ) -> Dict[str, str]:
        """
        Generate companion files (setup scripts, configs, etc.).

        Args:
            notebook_path: Path to the source notebook
            config: Configuration dictionary

        Returns:
            Dictionary mapping filenames to their content
        """
        pass

