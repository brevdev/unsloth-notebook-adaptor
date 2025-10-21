#!/usr/bin/env python3
"""
Generate Launchables table for README.md from metadata.

Usage:
    python generate_readme_table.py --metadata-path <path> --readme-path <path>
"""

import argparse
import json
import logging
import sys
from collections import OrderedDict
from pathlib import Path
from typing import List, Dict
from urllib.parse import quote

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Markers for table insertion
START_MARKER = "<!-- LAUNCHABLES_TABLE_START -->"
END_MARKER = "<!-- LAUNCHABLES_TABLE_END -->"


def load_metadata(metadata_path: Path) -> Dict:
    """
    Load launchables metadata from JSON file.

    Args:
        metadata_path: Path to launchables.json

    Returns:
        Metadata dictionary
    """
    logger.info(f"Loading metadata from: {metadata_path}")
    with open(metadata_path, 'r') as f:
        return json.load(f)


def generate_description(launchable: Dict) -> str:
    """
    Generate a concise description for a launchable.

    Args:
        launchable: Launchable metadata dictionary

    Returns:
        Description string
    """
    name = launchable.get('name', '')
    tags = launchable.get('tags', [])
    
    # Use existing description if available
    if 'description' in launchable and launchable['description']:
        return launchable['description']
    
    # Generate based on tags
    if 'vision' in tags or 'multimodal' in tags:
        return f"{name} - Multimodal fine-tuning"
    elif 'audio' in tags:
        if 'speech-to-text' in tags:
            return f"{name} - Speech-to-Text fine-tuning"
        elif 'text-to-speech' in tags:
            return f"{name} - Text-to-Speech fine-tuning"
        else:
            return f"{name} - Audio model fine-tuning"
    elif 'reinforcement-learning' in tags or 'grpo' in tags:
        return f"{name} - Reasoning with GRPO"
    elif 'text-generation' in tags or 'fine-tuning' in tags:
        return f"{name} - Fine-tuning"
    else:
        return f"{name} - Unsloth fine-tuning"


def get_model_type(launchable: Dict) -> str:
    """
    Determine the model type/use case from tags and notebook name.
    Matches Unsloth's categorization approach.

    Args:
        launchable: Launchable metadata dictionary

    Returns:
        Model type string (e.g., "Conversational", "Vision", "TTS", etc.)
    """
    tags = launchable.get('tags', [])
    name = launchable.get('name', '').lower()
    notebook = launchable.get('notebook', '').lower()
    
    # Check tags and filename for clues
    combined = f"{name} {notebook}".lower()
    
    # Check for specific types in order of specificity
    if 'vision' in combined or 'multimodal' in tags:
        return 'Vision'
    elif 'tts' in combined or 'text-to-speech' in tags:
        return 'TTS'
    elif 'whisper' in combined or 'speech-to-text' in tags or 'stt' in tags:
        return 'STT'
    elif 'grpo' in combined or 'reinforcement-learning' in tags:
        return 'GRPO'
    elif 'conversational' in combined or 'chat' in combined:
        return 'Conversational'
    elif 'alpaca' in combined:
        return 'Alpaca'
    elif 'inference' in combined:
        return 'Inference'
    elif 'reasoning' in combined:
        return 'Reasoning'
    elif 'orpo' in combined:
        return 'ORPO'
    elif 'dpo' in combined:
        return 'DPO'
    elif 'thinking' in combined:
        return 'Thinking'
    elif 'ollama' in combined:
        return 'Ollama'
    elif 'raft' in combined:
        return 'RAFT'
    elif 'synthetic' in combined:
        return 'Synthetic Data'
    elif 'instruct' in combined:
        return 'Instruct'
    elif 'cpt' in combined:
        return 'CPT'
    elif 'tool' in combined and 'calling' in combined:
        return 'Tool Calling'
    elif 'classification' in combined:
        return 'Classification'
    elif 'studio' in combined:
        return 'Studio'
    
    # Default
    return 'Fine-tuning'


def categorize_launchables(launchables: List[Dict]) -> Dict[str, List[Dict]]:
    """
    Categorize launchables to match Unsloth's exact structure.

    Args:
        launchables: List of launchable metadata dictionaries

    Returns:
        Dictionary mapping category names to lists of launchables (ordered)
    """
    # Use OrderedDict to maintain category order
    categories = OrderedDict([
        ('Main Notebooks', []),
        ('Vision Notebooks', []),
        ('Kaggle Notebooks', []),
        ('Spark Notebooks', []),
        ('Whisper Notebooks', []),
        ('Other Notebooks', [])
    ])
    
    for launchable in launchables:
        model_type = get_model_type(launchable)
        name = launchable.get('name', '').lower()
        notebook = launchable.get('notebook', '').lower()
        
        # Categorize based on Unsloth's structure
        if 'kaggle' in notebook or 'kaggle' in name:
            # Kaggle variants
            categories['Kaggle Notebooks'].append(launchable)
        elif 'spark' in name and 'tts' in name:
            # Spark TTS models
            categories['Spark Notebooks'].append(launchable)
        elif 'whisper' in name:
            # Whisper STT models
            categories['Whisper Notebooks'].append(launchable)
        elif model_type == 'Vision' or 'vision' in name or 'multimodal' in name:
            # Vision/Multimodal models
            categories['Vision Notebooks'].append(launchable)
        elif any(main in name for main in ['gemma3n', 'qwen3', 'qwen2', 'gemma3', 'gemma2', 'llama3', 'phi', 'mistral']):
            # Main featured models (Gemma, Qwen, Llama, Phi, Mistral families)
            categories['Main Notebooks'].append(launchable)
        else:
            # Everything else
            categories['Other Notebooks'].append(launchable)
    
    # Remove empty categories
    return OrderedDict((k, v) for k, v in categories.items() if v)


def generate_table(launchables: List[Dict]) -> str:
    """
    Generate markdown table matching Unsloth's format with GPU requirements added.

    Args:
        launchables: List of launchable metadata dictionaries

    Returns:
        Markdown table as string
    """
    logger.info(f"Generating table for {len(launchables)} launchables")
    
    # Categorize launchables
    categorized = categorize_launchables(launchables)
    
    # Build tables by category
    lines = []
    
    for category_name, category_launchables in categorized.items():
        # Sort alphabetically by name within each category
        category_launchables.sort(key=lambda x: x.get('name', ''))
        
        # Add category header
        lines.append(f"\n### {category_name}\n")
        lines.append("| Model | Type | GPU Requirements | Notebook Link |")
        lines.append("|-------|------|------------------|---------------|")
        
        for launchable in category_launchables:
            name = launchable.get('name', 'Unknown')
            model_type = get_model_type(launchable)
            
            # Format name - match Unsloth's bold style
            formatted_name = f"**{name}**"
            
            # GPU requirements (our additional column)
            gpu_info = launchable.get('gpu', {})
            gpu_tier = gpu_info.get('tier', 'L4')
            min_vram = gpu_info.get('min_vram_gb', 16)
            gpu_req = f"{gpu_tier}<br/>({min_vram}GB VRAM)"
            
            # Get launchable path
            launchable_path = launchable.get('path', launchable.get('id', name.lower().replace(' ', '-')))
            notebook_name = launchable.get('notebook', 'notebook.ipynb')
            
            # URL-encode for GitHub links
            encoded_path = quote(launchable_path)
            encoded_notebook = quote(notebook_name)
            github_path = f"converted/{encoded_path}/{encoded_notebook}"
            
            # Create link - match Unsloth's style
            notebook_link = f"[Open in Brev]({github_path})"
            
            # Add row with proper alignment
            lines.append(f"| {formatted_name} | {model_type} | {gpu_req} | {notebook_link} |")
    
    return '\n'.join(lines)


def update_readme(readme_path: Path, table_content: str) -> bool:
    """
    Update README.md with generated table.

    Args:
        readme_path: Path to README.md
        table_content: Generated table markdown

    Returns:
        True if updated successfully, False otherwise
    """
    logger.info(f"Updating README at: {readme_path}")
    
    # Read current README
    with open(readme_path, 'r', encoding='utf-8') as f:
        readme_content = f.read()
    
    # Check for markers
    if START_MARKER not in readme_content or END_MARKER not in readme_content:
        logger.error(f"Markers not found in README. Expected {START_MARKER} and {END_MARKER}")
        return False
    
    # Find marker positions
    start_pos = readme_content.find(START_MARKER)
    end_pos = readme_content.find(END_MARKER)
    
    if start_pos >= end_pos:
        logger.error("Invalid marker positions in README")
        return False
    
    # Build new content
    before_table = readme_content[:start_pos + len(START_MARKER)]
    after_table = readme_content[end_pos:]
    
    new_content = f"{before_table}\n{table_content}\n{after_table}"
    
    # Write updated README
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    logger.info("README updated successfully")
    return True


def main():
    """Main script execution."""
    parser = argparse.ArgumentParser(
        description='Generate Launchables table for README.md'
    )
    parser.add_argument(
        '--metadata-path',
        type=Path,
        required=True,
        help='Path to launchables.json metadata file'
    )
    parser.add_argument(
        '--readme-path',
        type=Path,
        required=True,
        help='Path to README.md file to update'
    )
    
    args = parser.parse_args()
    
    # Validate inputs
    if not args.metadata_path.exists():
        logger.error(f"Metadata file not found: {args.metadata_path}")
        sys.exit(1)
    
    if not args.readme_path.exists():
        logger.error(f"README file not found: {args.readme_path}")
        sys.exit(1)
    
    try:
        # Load metadata
        metadata = load_metadata(args.metadata_path)
        launchables = metadata.get('launchables', [])
        
        if not launchables:
            logger.warning("No launchables found in metadata")
            sys.exit(0)
        
        # Generate table
        table_content = generate_table(launchables)
        
        # Update README
        if update_readme(args.readme_path, table_content):
            logger.info(f"✓ Successfully updated README with {len(launchables)} launchables")
        else:
            logger.error("Failed to update README")
            sys.exit(1)
        
    except Exception as e:
        logger.error(f"Error generating table: {e}", exc_info=True)
        sys.exit(1)


if __name__ == '__main__':
    main()

