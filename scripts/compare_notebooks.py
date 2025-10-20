#!/usr/bin/env python3
"""
Compare notebooks between commits to detect changes.

Usage:
    python compare_notebooks.py --source <path> --metadata <path> --output changes.txt
"""

import argparse
import logging
import subprocess
import sys
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def get_last_sync_commit(metadata_file: Path) -> str:
    """
    Read the last synced commit hash from metadata file.

    Args:
        metadata_file: Path to last_sync.txt

    Returns:
        Commit hash or empty string if not found
    """
    if not metadata_file.exists():
        logger.info("No previous sync found")
        return ""
    
    try:
        with open(metadata_file, 'r') as f:
            lines = f.readlines()
            if lines:
                # First line should be commit hash
                return lines[0].strip()
    except Exception as e:
        logger.warning(f"Could not read last sync commit: {e}")
    
    return ""


def get_changed_notebooks(
    source_dir: Path,
    last_commit: str
) -> list:
    """
    Get list of changed notebook files since last commit.

    Args:
        source_dir: Path to notebooks repository
        last_commit: Last synced commit hash

    Returns:
        List of changed notebook paths (relative to source_dir)
    """
    try:
        # Change to source directory
        original_dir = Path.cwd()
        
        # Check if source is a git repository
        git_dir = source_dir / '.git'
        if not git_dir.exists():
            logger.warning(f"Source directory is not a git repository: {source_dir}")
            logger.info("Returning all notebooks instead")
            all_notebooks = list(source_dir.glob('**/*.ipynb'))
            return [str(nb.relative_to(source_dir)) for nb in all_notebooks]
        
        # If no last commit, return all notebooks
        if not last_commit:
            logger.info("No last commit found, returning all notebooks")
            all_notebooks = list(source_dir.glob('**/*.ipynb'))
            return [str(nb.relative_to(source_dir)) for nb in all_notebooks]
        
        # Use git diff to find changed files
        cmd = [
            'git', '-C', str(source_dir),
            'diff', '--name-only', last_commit, 'HEAD'
        ]
        
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            check=True
        )
        
        # Filter for .ipynb files
        changed_files = []
        for line in result.stdout.split('\n'):
            line = line.strip()
            if line.endswith('.ipynb'):
                changed_files.append(line)
        
        logger.info(f"Found {len(changed_files)} changed notebook(s)")
        return changed_files
        
    except subprocess.CalledProcessError as e:
        logger.error(f"Git command failed: {e}")
        logger.info("Returning all notebooks as fallback")
        all_notebooks = list(source_dir.glob('**/*.ipynb'))
        return [str(nb.relative_to(source_dir)) for nb in all_notebooks]
    
    except Exception as e:
        logger.error(f"Error getting changed notebooks: {e}", exc_info=True)
        return []


def main():
    """Main comparison script."""
    parser = argparse.ArgumentParser(
        description='Compare notebooks to detect changes'
    )
    parser.add_argument(
        '--source',
        type=Path,
        required=True,
        help='Source directory of Unsloth notebooks repository'
    )
    parser.add_argument(
        '--metadata',
        type=Path,
        required=True,
        help='Path to last_sync.txt metadata file'
    )
    parser.add_argument(
        '--output',
        type=Path,
        required=True,
        help='Output file for list of changed notebooks'
    )
    
    args = parser.parse_args()
    
    # Validate source
    if not args.source.exists():
        logger.error(f"Source directory not found: {args.source}")
        sys.exit(1)
    
    # Get last commit
    last_commit = get_last_sync_commit(args.metadata)
    if last_commit:
        logger.info(f"Last sync commit: {last_commit}")
    
    # Get changed notebooks
    changed_notebooks = get_changed_notebooks(args.source, last_commit)
    
    # Write to output file
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with open(args.output, 'w') as f:
        for notebook in changed_notebooks:
            f.write(f"{notebook}\n")
    
    logger.info(f"Wrote {len(changed_notebooks)} changed notebook(s) to {args.output}")
    
    # Exit with code indicating if changes were found
    sys.exit(0 if changed_notebooks else 0)


if __name__ == '__main__':
    main()

