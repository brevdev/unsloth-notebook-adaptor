#!/usr/bin/env python3
"""
Create GitHub Actions step summary.

Usage:
    python create_summary.py <launchables.json>
"""

import json
import sys
from collections import defaultdict
from pathlib import Path


def create_summary(launchables_file: Path) -> str:
    """
    Create GitHub-flavored markdown summary.

    Args:
        launchables_file: Path to launchables.json

    Returns:
        Markdown formatted summary
    """
    # Load launchables
    with open(launchables_file, 'r') as f:
        registry = json.load(f)
    
    launchables = registry.get('launchables', [])
    total = registry.get('total_launchables', 0)
    
    # Group by category
    by_category = defaultdict(list)
    for launchable in launchables:
        tags = launchable.get('tags', [])
        # Use first non-generic tag as category
        category = 'Other'
        for tag in tags:
            if tag not in ['unsloth', 'fine-tuning']:
                category = tag.title()
                break
        by_category[category].append(launchable)
    
    # Build markdown
    lines = [
        "# 🚀 Unsloth to Brev Conversion Summary",
        "",
        f"**Generated:** {registry.get('generated_at', 'Unknown')}",
        "",
        "## 📊 Statistics",
        "",
        "| Metric | Value |",
        "|--------|-------|",
        f"| **Total Launchables** | {total} |",
        f"| **Categories** | {len(by_category)} |",
        "",
        "## 📦 Launchables by Category",
        ""
    ]
    
    # Add launchables by category
    for category in sorted(by_category.keys()):
        launchables_list = by_category[category]
        lines.append(f"### {category} ({len(launchables_list)})")
        lines.append("")
        
        for launchable in sorted(launchables_list, key=lambda x: x['name']):
            name = launchable['name']
            gpu = launchable.get('gpu', {}).get('tier', 'N/A')
            vram = launchable.get('gpu', {}).get('min_vram_gb', 'N/A')
            
            lines.append(f"- **{name}**")
            lines.append(f"  - GPU: {gpu} ({vram} GB VRAM)")
            lines.append(f"  - Path: `{launchable['path']}`")
            
            upstream_url = launchable.get('upstream', {}).get('notebook_url', '')
            if upstream_url and upstream_url != '#':
                lines.append(f"  - [Original Notebook]({upstream_url})")
            
            lines.append("")
    
    # Add quick links
    lines.extend([
        "## 🔗 Quick Links",
        "",
        "- [Unsloth Documentation](https://docs.unsloth.ai/)",
        "- [Brev Documentation](https://docs.nvidia.com/brev)",
        "- [Repository](https://github.com/brevdev/unsloth-notebook-adaptor)",
        ""
    ])
    
    return '\n'.join(lines)


def main():
    """Main summary creation script."""
    if len(sys.argv) < 2:
        print("Usage: python create_summary.py <launchables.json>", file=sys.stderr)
        sys.exit(1)
    
    launchables_file = Path(sys.argv[1])
    
    if not launchables_file.exists():
        print(f"File not found: {launchables_file}", file=sys.stderr)
        sys.exit(1)
    
    # Create and print summary
    summary = create_summary(launchables_file)
    print(summary)


if __name__ == '__main__':
    main()

