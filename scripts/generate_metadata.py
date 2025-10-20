#!/usr/bin/env python3
"""
Generate metadata registry for all converted launchables.

Usage:
    python generate_metadata.py --notebooks-dir <path> --output <path>
"""

import argparse
import json
import logging
import sys
from datetime import datetime, timezone
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def scan_launchables(notebooks_dir: Path) -> list:
    """
    Scan converted directory for launchables.

    Args:
        notebooks_dir: Directory containing converted notebooks

    Returns:
        List of launchable metadata dictionaries
    """
    launchables = []
    
    for launchable_dir in notebooks_dir.iterdir():
        if not launchable_dir.is_dir():
            continue
        
        # Look for .brevconfig.json
        config_file = launchable_dir / '.brevconfig.json'
        if not config_file.exists():
            logger.warning(f"No .brevconfig.json found in {launchable_dir}")
            continue
        
        try:
            # Read Brev config
            with open(config_file, 'r') as f:
                brev_config = json.load(f)
            
            # Find notebook file (look for any .ipynb file)
            notebook_files = list(launchable_dir.glob('*.ipynb'))
            if not notebook_files:
                logger.warning(f"No notebook found in {launchable_dir}")
                continue
            
            # Use first notebook found (should only be one)
            notebook_file = notebook_files[0]
            
            # List companion files
            companion_files = []
            for file_path in launchable_dir.iterdir():
                if file_path.is_file():
                    companion_files.append(file_path.name)
            
            # Build launchable metadata
            launchable = {
                'id': launchable_dir.name,
                'name': brev_config.get('name', launchable_dir.name),
                'description': brev_config.get('description', ''),
                'notebook': notebook_file.name,
                'path': str(launchable_dir.relative_to(notebooks_dir)),
                'gpu': brev_config.get('gpu', {}),
                'tags': brev_config.get('tags', []),
                'upstream': brev_config.get('upstream', {}),
                'files': companion_files
            }
            
            launchables.append(launchable)
            logger.info(f"Found launchable: {launchable['name']}")
            
        except Exception as e:
            logger.error(f"Error processing {launchable_dir}: {e}")
            continue
    
    return launchables


def main():
    """Main metadata generation script."""
    parser = argparse.ArgumentParser(
        description='Generate metadata registry for converted launchables'
    )
    parser.add_argument(
        '--notebooks-dir',
        type=Path,
        required=True,
        help='Directory containing converted notebooks'
    )
    parser.add_argument(
        '--output',
        type=Path,
        required=True,
        help='Output path for launchables.json'
    )
    
    args = parser.parse_args()
    
    # Validate input
    if not args.notebooks_dir.exists():
        logger.error(f"Notebooks directory not found: {args.notebooks_dir}")
        sys.exit(1)
    
    # Scan for launchables
    logger.info(f"Scanning: {args.notebooks_dir}")
    launchables = scan_launchables(args.notebooks_dir)
    
    # Build registry
    registry = {
        'version': '1.0.0',
        'generated_at': datetime.now(timezone.utc).isoformat(),
        'total_launchables': len(launchables),
        'launchables': sorted(launchables, key=lambda x: x['name'])
    }
    
    # Write to output
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with open(args.output, 'w') as f:
        json.dump(registry, f, indent=2)
    
    logger.info(f"Generated registry with {len(launchables)} launchable(s)")
    logger.info(f"Saved to: {args.output}")


if __name__ == '__main__':
    main()

