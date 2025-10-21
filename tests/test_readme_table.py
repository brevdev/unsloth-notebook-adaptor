"""
Tests for README table generation.
"""

import json
import pytest
import tempfile
from pathlib import Path

# Add parent directory to path for imports
import sys
sys.path.insert(0, str(Path(__file__).parent.parent))

from scripts.generate_readme_table import (
    generate_description,
    generate_table,
    update_readme,
    START_MARKER,
    END_MARKER
)


@pytest.fixture
def sample_launchables():
    """Create sample launchables data."""
    return [
        {
            "id": "llama-3.1-8b",
            "name": "Llama 3.1 (8B)",
            "description": "Fine-tune Llama 3.1 (8B) with Unsloth",
            "path": "llama-3.1-8b",
            "notebook": "Llama3.1_(8B).ipynb",
            "gpu": {
                "tier": "L4",
                "min_vram_gb": 16
            },
            "tags": ["unsloth", "fine-tuning", "text-generation"]
        },
        {
            "id": "gemma-3-vision",
            "name": "Gemma 3 Vision",
            "description": "",  # Test auto-generation
            "path": "gemma-3-vision",
            "notebook": "Gemma3_Vision.ipynb",
            "gpu": {
                "tier": "L4",
                "min_vram_gb": 20
            },
            "tags": ["unsloth", "vision", "multimodal"]
        },
        {
            "id": "whisper-large-v3",
            "name": "Whisper Large V3",
            "description": "",
            "path": "whisper-large-v3",
            "notebook": "Whisper.ipynb",
            "gpu": {
                "tier": "A100-40GB",
                "min_vram_gb": 16
            },
            "tags": ["audio", "speech-to-text"]
        }
    ]


def test_generate_description_with_existing(sample_launchables):
    """Test description generation with existing description."""
    launchable = sample_launchables[0]
    description = generate_description(launchable)
    
    assert description == "Fine-tune Llama 3.1 (8B) with Unsloth"


def test_generate_description_vision(sample_launchables):
    """Test description generation for vision model."""
    launchable = sample_launchables[1]
    description = generate_description(launchable)
    
    assert "Multimodal" in description or "multimodal" in description.lower()


def test_generate_description_audio(sample_launchables):
    """Test description generation for audio model."""
    launchable = sample_launchables[2]
    description = generate_description(launchable)
    
    assert "Speech-to-Text" in description or "speech" in description.lower()


def test_generate_table(sample_launchables):
    """Test table generation."""
    table = generate_table(sample_launchables)
    
    # Check new Unsloth-style table structure
    assert "| Model | Type | GPU Requirements | Notebook Link |" in table
    assert "| --- | --- | --- | --- |" in table
    
    # Check family-based categories are present
    assert "### Llama Notebooks" in table
    assert "### Gemma Notebooks" in table
    assert "### Whisper Notebooks" in table
    
    # Check all models are in table (with bold formatting from notebook filenames)
    assert "**Llama3.1_(8B)**" in table
    assert "**Gemma3_Vision**" in table
    assert "**Whisper**" in table
    
    # Check GPU requirements (new format without <br/> or VRAM text)
    assert "L4 (16GB)" in table
    assert "A100-40GB (16GB)" in table
    assert "L4 (20GB)" in table
    
    # Check notebook links use HTML anchor tags with full GitHub URLs
    assert "<a href=" in table
    assert "https://github.com/brevdev/unsloth-notebook-adaptor/blob/main/converted/" in table
    assert 'target="_blank"' in table
    assert 'rel="noopener noreferrer"' in table
    assert "View Notebook</a>" in table
    
    # Check auto-generated markers
    assert "<!-- START OF EDITING -->" in table
    assert "<!-- END OF EDITING -->" in table


def test_generate_table_empty():
    """Test table generation with empty list."""
    table = generate_table([])
    
    # Empty list still includes markers but no category sections
    assert "<!-- START OF EDITING -->" in table
    assert "<!-- END OF EDITING -->" in table
    
    # Should not have any category headers
    assert "###" not in table


def test_update_readme_success(sample_launchables, tmp_path):
    """Test successful README update."""
    # Create test README with markers
    readme_content = f"""# Test README

Some content before.

{START_MARKER}
Old table content here
{END_MARKER}

Some content after.
"""
    
    readme_path = tmp_path / "README.md"
    with open(readme_path, 'w') as f:
        f.write(readme_content)
    
    # Generate table
    table = generate_table(sample_launchables)
    
    # Update README
    success = update_readme(readme_path, table)
    assert success
    
    # Read updated README
    with open(readme_path, 'r') as f:
        updated_content = f.read()
    
    # Check markers are preserved
    assert START_MARKER in updated_content
    assert END_MARKER in updated_content
    
    # Check old content is removed
    assert "Old table content here" not in updated_content
    
    # Check new content is present (uses notebook filename format)
    assert "**Llama3.1_(8B)**" in updated_content
    
    # Check surrounding content preserved
    assert "Some content before." in updated_content
    assert "Some content after." in updated_content


def test_update_readme_missing_markers(tmp_path):
    """Test README update with missing markers."""
    # Create README without markers
    readme_content = "# Test README\n\nNo markers here."
    
    readme_path = tmp_path / "README.md"
    with open(readme_path, 'w') as f:
        f.write(readme_content)
    
    # Try to update
    success = update_readme(readme_path, "test table")
    assert not success


def test_update_readme_invalid_markers(tmp_path):
    """Test README update with invalid marker order."""
    # Create README with markers in wrong order
    readme_content = f"""# Test README

{END_MARKER}
Some content
{START_MARKER}
"""
    
    readme_path = tmp_path / "README.md"
    with open(readme_path, 'w') as f:
        f.write(readme_content)
    
    # Try to update
    success = update_readme(readme_path, "test table")
    assert not success


def test_url_encoding_in_links():
    """Test that notebook links are properly URL-encoded."""
    # Create launchable with spaces in path and filename
    launchables = [
        {
            "id": "huggingface-course-llama",
            "name": "HuggingFace Course Llama3",
            "path": "huggingface course-llama3",  # Space in path
            "notebook": "HuggingFace Course-Llama3.1_(8B)-GRPO.ipynb",  # Spaces and special chars
            "gpu": {"tier": "L4", "min_vram_gb": 16},
            "tags": ["grpo", "reinforcement-learning"]
        }
    ]
    
    table = generate_table(launchables)
    
    # Check that spaces are encoded as %20 in the href
    assert "huggingface%20course-llama3" in table
    assert "HuggingFace%20Course-Llama3.1_%288B%29-GRPO.ipynb" in table
    
    # Check that parentheses are encoded in the href
    assert "%28" in table  # (
    assert "%29" in table  # )
    
    # Check HTML anchor tag format with full GitHub URL
    assert '<a href="https://github.com/brevdev/unsloth-notebook-adaptor/blob/main/converted/huggingface%20course-llama3/' in table
    assert 'target="_blank"' in table
    assert 'rel="noopener noreferrer"' in table

