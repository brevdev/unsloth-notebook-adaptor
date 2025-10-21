#!/usr/bin/env python3
"""
Convert Unsloth Colab notebooks to Brev-compatible format.

Usage:
    python convert_notebook.py --source <path> --output <path>
    python convert_notebook.py --changed-file changes.txt --source <path> --output <path>
"""

import argparse
import json
import logging
import sys
from pathlib import Path

import nbformat

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from adapters import ColabToBrevAdapter, get_config_for_notebook

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def convert_single_notebook(
    notebook_path: Path,
    output_dir: Path,
    templates_dir: Path
) -> bool:
    """
    Convert a single notebook.

    Args:
        notebook_path: Path to source notebook
        output_dir: Base output directory
        templates_dir: Path to Jinja2 templates

    Returns:
        True if successful, False otherwise
    """
    try:
        logger.info(f"Converting: {notebook_path}")
        
        # Get configuration
        config = get_config_for_notebook(notebook_path.stem)
        logger.info(f"Using config: {config['launchable_name']}")
        
        # Create adapter
        adapter = ColabToBrevAdapter(templates_dir)
        
        # Adapt notebook
        adapted_notebook, companion_files = adapter.adapt(notebook_path, config)
        
        # Create output directory for this launchable
        launchable_dir = output_dir / config['launchable_name']
        launchable_dir.mkdir(parents=True, exist_ok=True)
        
        # Save adapted notebook with original filename
        notebook_output = launchable_dir / notebook_path.name
        with open(notebook_output, 'w', encoding='utf-8') as f:
            nbformat.write(adapted_notebook, f)
        logger.info(f"Saved notebook to: {notebook_output}")
        
        # Save companion files
        for filename, content in companion_files.items():
            file_path = launchable_dir / filename
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            logger.info(f"Saved companion file: {file_path}")
        
        logger.info(f"✓ Successfully converted: {notebook_path.name}")
        return True
        
    except Exception as e:
        logger.error(f"✗ Failed to convert {notebook_path}: {e}", exc_info=True)
        return False


def main():
    """Main conversion script."""
    parser = argparse.ArgumentParser(
        description='Convert Unsloth Colab notebooks to Brev format'
    )
    parser.add_argument(
        '--source',
        type=Path,
        required=True,
        help='Source directory containing Unsloth notebooks'
    )
    parser.add_argument(
        '--output',
        type=Path,
        required=True,
        help='Output directory for converted notebooks'
    )
    parser.add_argument(
        '--config',
        type=Path,
        help='Optional path to custom config JSON'
    )
    parser.add_argument(
        '--changed-file',
        type=Path,
        help='File containing list of changed notebooks (one per line)'
    )
    parser.add_argument(
        '--notebooks',
        nargs='+',
        help='Specific notebooks to convert (filenames)'
    )
    
    args = parser.parse_args()
    
    # Validate paths
    if not args.source.exists():
        logger.error(f"Source directory not found: {args.source}")
        sys.exit(1)
    
    # Get templates directory
    templates_dir = Path(__file__).parent.parent / 'templates'
    if not templates_dir.exists():
        logger.error(f"Templates directory not found: {templates_dir}")
        sys.exit(1)
    
    # Create output directory
    args.output.mkdir(parents=True, exist_ok=True)
    
    # Determine which notebooks to convert
    notebooks_to_convert = []
    
    if args.changed_file and args.changed_file.exists():
        # Read from changed file
        logger.info(f"Reading changed notebooks from: {args.changed_file}")
        with open(args.changed_file, 'r') as f:
            for line in f:
                notebook_path = args.source / line.strip()
                if notebook_path.exists() and notebook_path.suffix == '.ipynb':
                    notebooks_to_convert.append(notebook_path)
    
    elif args.notebooks:
        # Convert specific notebooks
        for notebook_name in args.notebooks:
            notebook_path = args.source / notebook_name
            if notebook_path.exists():
                notebooks_to_convert.append(notebook_path)
            else:
                logger.warning(f"Notebook not found: {notebook_path}")
    
    else:
        # Convert all notebooks in source directory
        logger.info(f"Converting all notebooks in: {args.source}")
        notebooks_to_convert = list(args.source.glob('**/*.ipynb'))
    
    if not notebooks_to_convert:
        logger.warning("No notebooks to convert")
        sys.exit(0)
    
    # Filter out Kaggle notebooks (they're redundant duplicates of the main notebooks)
    original_count = len(notebooks_to_convert)
    notebooks_to_convert = [
        nb for nb in notebooks_to_convert 
        if 'kaggle' not in nb.stem.lower() and 'kaggle' not in nb.name.lower()
    ]
    
    if original_count != len(notebooks_to_convert):
        kaggle_filtered = original_count - len(notebooks_to_convert)
        logger.info(f"Filtered out {kaggle_filtered} Kaggle notebook(s) (redundant for Brev)")
    
    if not notebooks_to_convert:
        logger.warning("No notebooks to convert after filtering Kaggle variants")
        sys.exit(0)
    
    logger.info(f"Converting {len(notebooks_to_convert)} notebook(s)")
    
    # Convert notebooks
    successful = 0
    failed = 0
    skipped = 0
    
    for notebook_path in notebooks_to_convert:
        if convert_single_notebook(notebook_path, args.output, templates_dir):
            successful += 1
        else:
            failed += 1
    
    # Print summary
    logger.info("=" * 60)
    logger.info("CONVERSION SUMMARY")
    logger.info("=" * 60)
    logger.info(f"Total notebooks: {len(notebooks_to_convert)}")
    logger.info(f"Successful: {successful}")
    logger.info(f"Failed: {failed}")
    logger.info("=" * 60)
    
    sys.exit(0 if failed == 0 else 1)


if __name__ == '__main__':
    main()

