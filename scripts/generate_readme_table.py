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
    Categorize launchables by model family to match Unsloth's structure.
    Matches the exact ordering from Unsloth's README.

    Args:
        launchables: List of launchable metadata dictionaries

    Returns:
        Dictionary mapping category names to lists of launchables (ordered)
    """
    # Use OrderedDict to maintain category order - match Unsloth's exact structure
    categories = OrderedDict([
        ('GRPO Notebooks', []),
        ('GPT-OSS Notebooks', []),
        ('Gemma Notebooks', []),
        ('Linear Attention Notebooks', []),
        ('Llama Notebooks', []),
        ('Mistral Notebooks', []),
        ('Orpheus Notebooks', []),
        ('Oute Notebooks', []),
        ('Phi Notebooks', []),
        ('Qwen Notebooks', []),
        ('Spark Notebooks', []),
        ('Whisper Notebooks', []),
        ('Other Notebooks', []),
    ])
    
    # Separate list for Kaggle variants (in collapsible section)
    kaggle_categories = OrderedDict([
        ('GRPO Notebooks', []),
        ('GPT-OSS Notebooks', []),
        ('Gemma Notebooks', []),
        ('Linear Attention Notebooks', []),
        ('Llama Notebooks', []),
        ('Mistral Notebooks', []),
        ('Orpheus Notebooks', []),
        ('Oute Notebooks', []),
        ('Phi Notebooks', []),
        ('Qwen Notebooks', []),
        ('Spark Notebooks', []),
        ('Whisper Notebooks', []),
        ('Other Notebooks', []),
    ])
    
    for launchable in launchables:
        model_type = get_model_type(launchable)
        name = launchable.get('name', '').lower()
        notebook = launchable.get('notebook', '').lower()
        
        # Check if it's a Kaggle variant first
        is_kaggle = 'kaggle' in notebook or 'kaggle' in name
        
        # Determine which category to use
        target_categories = kaggle_categories if is_kaggle else categories
        
        # Categorize by family/type (matching Unsloth's exact logic)
        if 'grpo' in name or 'grpo' in notebook:
            target_categories['GRPO Notebooks'].append(launchable)
        elif 'gpt-oss' in name or 'gpt_oss' in name or 'gpt oss' in name:
            target_categories['GPT-OSS Notebooks'].append(launchable)
        elif 'gemma' in name:
            target_categories['Gemma Notebooks'].append(launchable)
        elif 'liquid' in name or 'falcon' in name:
            target_categories['Linear Attention Notebooks'].append(launchable)
        elif 'llama' in name or 'llasa' in name:
            target_categories['Llama Notebooks'].append(launchable)
        elif 'mistral' in name or 'zephyr' in name or 'pixtral' in name:
            target_categories['Mistral Notebooks'].append(launchable)
        elif 'orpheus' in name:
            target_categories['Orpheus Notebooks'].append(launchable)
        elif 'oute' in name:
            target_categories['Oute Notebooks'].append(launchable)
        elif 'phi' in name:
            target_categories['Phi Notebooks'].append(launchable)
        elif 'qwen' in name:
            target_categories['Qwen Notebooks'].append(launchable)
        elif 'spark' in name:
            target_categories['Spark Notebooks'].append(launchable)
        elif 'whisper' in name:
            target_categories['Whisper Notebooks'].append(launchable)
        else:
            target_categories['Other Notebooks'].append(launchable)
    
    # Remove empty categories
    categories = OrderedDict((k, v) for k, v in categories.items() if v)
    kaggle_categories = OrderedDict((k, v) for k, v in kaggle_categories.items() if v)
    
    return categories, kaggle_categories


def format_model_name(launchable: Dict) -> str:
    """
    Format model name to match Unsloth's style.
    Examples: **Gemma3N** **(4B)**, **(A100) Llama3.3** **(70B)**

    Args:
        launchable: Launchable metadata dictionary

    Returns:
        Formatted model name with bold and size in parentheses
    """
    name = launchable.get('name', 'Unknown')
    notebook = launchable.get('notebook', '')
    
    # Extract the base model name from notebook filename (more reliable than name field)
    # Remove .ipynb extension and clean up
    clean_name = notebook.replace('.ipynb', '').replace('Kaggle-', '').replace('HuggingFace Course-', '')
    
    # Check if it starts with (A100) or similar GPU prefix
    if clean_name.startswith('(A100)') or notebook.startswith('(A100)'):
        # Format: **(A100) Model** **(Size)**
        return f"**{clean_name}**"
    
    # Otherwise just format as **Model Name**
    return f"**{clean_name}**"


def generate_table(launchables: List[Dict]) -> str:
    """
    Generate markdown table matching Unsloth's exact format with GPU requirements added.
    Creates separate sections for regular notebooks and Kaggle notebooks (in collapsible).

    Args:
        launchables: List of launchable metadata dictionaries

    Returns:
        Markdown table as string with both regular and Kaggle sections
    """
    logger.info(f"Generating table for {len(launchables)} launchables")
    
    # Categorize launchables (returns both regular and kaggle categories)
    categories, kaggle_categories = categorize_launchables(launchables)
    
    # Build tables by category
    lines = []
    
    # Regular notebooks section (auto-generated, with clear markers)
    lines.append("<!-- 🛑 🚨 DO NOT EDIT MANUALLY THIS SECTION UNTIL `end of notebook links`!! 🛑 🚨 -->")
    lines.append("<!-- 🛑 🚨 THIS SECTION IS GENERATED BY `generate_readme_table.py` AUTOMATICALLY 🛑 🚨  -->")
    lines.append("")
    lines.append("<!-- START OF EDITING -->")
    
    for category_name, category_launchables in categories.items():
        # Sort alphabetically by name within each category
        category_launchables.sort(key=lambda x: x.get('notebook', ''))
        
        # Add category header
        lines.append(f"### {category_name}")
        lines.append("| Model | Type | GPU Requirements | Notebook Link |")
        lines.append("| --- | --- | --- | --- |")
        
        for launchable in category_launchables:
            formatted_name = format_model_name(launchable)
            model_type = get_model_type(launchable)
            
            # GPU requirements (our additional column)
            gpu_info = launchable.get('gpu', {})
            gpu_tier = gpu_info.get('tier', 'L4')
            min_vram = gpu_info.get('min_vram_gb', 16)
            gpu_req = f"{gpu_tier} ({min_vram}GB)"
            
            # Get launchable path
            launchable_path = launchable.get('path', launchable.get('id', ''))
            notebook_name = launchable.get('notebook', 'notebook.ipynb')
            
            # URL-encode for GitHub links
            encoded_path = quote(launchable_path)
            encoded_notebook = quote(notebook_name)
            github_path = f"https://github.com/brevdev/unsloth-notebook-adaptor/blob/main/converted/{encoded_path}/{encoded_notebook}"
            
            # Create link using HTML anchor tag (match Unsloth's style)
            notebook_link = f'<a href="{github_path}" target="_blank" rel="noopener noreferrer">View Notebook</a>'
            
            # If model type is empty, leave it blank (some Unsloth entries have no type)
            type_cell = model_type if model_type and model_type != 'Fine-tuning' else ''
            
            # Add row
            lines.append(f"| {formatted_name} | {type_cell} | {gpu_req} | {notebook_link} |")
    
    lines.append("")
    
    # Kaggle notebooks section (collapsible)
    if kaggle_categories:
        lines.append("# 📒 Kaggle Notebooks")
        lines.append("<details>")
        lines.append("  <summary>")
        lines.append("    Click for all our Kaggle notebooks categorized by model:")
        lines.append("  </summary>")
        lines.append("")
        
        for category_name, category_launchables in kaggle_categories.items():
            # Sort alphabetically by name within each category
            category_launchables.sort(key=lambda x: x.get('notebook', ''))
            
            # Add category header
            lines.append(f"### {category_name}")
            lines.append("| Model | Type | GPU Requirements | Notebook Link |")
            lines.append("| --- | --- | --- | --- |")
            
            for launchable in category_launchables:
                formatted_name = format_model_name(launchable)
                model_type = get_model_type(launchable)
                
                # GPU requirements
                gpu_info = launchable.get('gpu', {})
                gpu_tier = gpu_info.get('tier', 'L4')
                min_vram = gpu_info.get('min_vram_gb', 16)
                gpu_req = f"{gpu_tier} ({min_vram}GB)"
                
                # Get launchable path
                launchable_path = launchable.get('path', launchable.get('id', ''))
                notebook_name = launchable.get('notebook', 'notebook.ipynb')
                
                # URL-encode for GitHub links
                encoded_path = quote(launchable_path)
                encoded_notebook = quote(notebook_name)
                github_path = f"https://github.com/brevdev/unsloth-notebook-adaptor/blob/main/converted/{encoded_path}/{encoded_notebook}"
                
                # Create link using HTML anchor tag
                notebook_link = f'<a href="{github_path}" target="_blank" rel="noopener noreferrer">View Notebook</a>'
                
                # If model type is empty, leave it blank
                type_cell = model_type if model_type and model_type != 'Fine-tuning' else ''
                
                # Add row
                lines.append(f"| {formatted_name} | {type_cell} | {gpu_req} | {notebook_link} |")
        
        lines.append("</details>")
    
    lines.append("")
    lines.append("<!-- END OF EDITING -->")
    
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

