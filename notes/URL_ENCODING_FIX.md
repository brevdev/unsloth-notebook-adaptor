# URL Encoding Fix for README Notebook Links

**Date:** October 20, 2025  
**Issue:** Broken "View Notebook" links in README for notebooks with spaces in filenames  
**Status:** ✅ Fixed

## Problem

Several notebook links in the generated README were broken, specifically for "HuggingFace Course" notebooks that have spaces and special characters in their filenames.

### Examples of Broken Links

Before the fix, these links were 404ing:

```markdown
[View Notebook](converted/huggingface course-advanced-llama3-1-3b-grpo-lora/HuggingFace Course-Advanced_Llama3_1_(3B)_GRPO_LoRA.ipynb)
```

**Problem:** Spaces and special characters in URLs break GitHub markdown links.

### Affected Notebooks

- All "HuggingFace Course" notebooks (~10 notebooks)
- Any notebook with spaces in the filename
- Notebooks with special characters like parentheses `()` in filenames

## Root Cause

The `generate_readme_table.py` script was constructing GitHub URLs without URL-encoding the path components:

```python
# Before (broken)
github_path = f"converted/{launchable_path}/{notebook_name}"
```

This resulted in raw spaces and special characters in the URLs, which GitHub cannot resolve.

## Solution

Added URL encoding using Python's `urllib.parse.quote()` to properly encode all path components:

```python
# After (fixed)
from urllib.parse import quote

encoded_path = quote(launchable_path)
encoded_notebook = quote(notebook_name)
github_path = f"converted/{encoded_path}/{encoded_notebook}"
```

### Encoding Examples

| Character | Encoded As |
|-----------|------------|
| Space (` `) | `%20` |
| `(` | `%28` |
| `)` | `%29` |
| Dash (`-`) | `-` (unchanged) |
| Underscore (`_`) | `_` (unchanged) |

## Before & After

### Before (Broken)
```markdown
[View Notebook](converted/huggingface course-llama3/HuggingFace Course-Llama3.1_(8B)-GRPO.ipynb)
```
❌ Results in 404 - spaces and parens break the link

### After (Fixed)
```markdown
[View Notebook](converted/huggingface%20course-llama3/HuggingFace%20Course-Llama3.1_%288B%29-GRPO.ipynb)
```
✅ Works correctly - all special characters are URL-encoded

## Changes Made

### 1. Updated `scripts/generate_readme_table.py`

**Added import:**
```python
from urllib.parse import quote
```

**Updated link generation:**
```python
# Get launchable path (use 'path' or 'id' which matches directory name)
launchable_path = launchable.get('path', launchable.get('id', name.lower().replace(' ', '-')))
notebook_name = launchable.get('notebook', 'notebook.ipynb')

# URL-encode path components for GitHub markdown links
# This handles spaces and special characters in filenames
encoded_path = quote(launchable_path)
encoded_notebook = quote(notebook_name)
github_path = f"converted/{encoded_path}/{encoded_notebook}"

# Create link to the notebook in the repo
notebook_link = f"[View Notebook]({github_path})"
```

### 2. Regenerated README.md

Ran the script to update all links:
```bash
python3 scripts/generate_readme_table.py \
  --metadata-path metadata/launchables.json \
  --readme-path README.md
```

### 3. Added Test Coverage

Added new test in `tests/test_readme_table.py`:

```python
def test_url_encoding_in_links():
    """Test that notebook links are properly URL-encoded."""
    launchables = [
        {
            "id": "huggingface-course-llama",
            "name": "HuggingFace Course Llama3",
            "path": "huggingface course-llama3",  # Space in path
            "notebook": "HuggingFace Course-Llama3.1_(8B)-GRPO.ipynb",
            "gpu": {"tier": "L4", "min_vram_gb": 16},
            "tags": ["grpo", "reinforcement-learning"]
        }
    ]
    
    table = generate_table(launchables)
    
    # Verify encoding
    assert "huggingface%20course-llama3" in table
    assert "HuggingFace%20Course-Llama3.1_%288B%29-GRPO.ipynb" in table
    assert "%28" in table  # (
    assert "%29" in table  # )
```

## Verification

### Test Results
```bash
pytest tests/test_readme_table.py -v
```
✅ All 9 tests pass, including the new URL encoding test

### Manual Verification

Checked affected links in README:
```bash
grep "Huggingface Course" README.md | grep "View Notebook"
```

Sample output:
```
| **Huggingface Course Llama3** | GRPO | L4 (16GB) | 
  [View Notebook](converted/huggingface%20course-llama3/HuggingFace%20Course-Llama3.1_%288B%29-GRPO.ipynb) |
```

All links now properly URL-encoded! ✅

## Impact

### Fixed Notebooks
- ✅ All 10 HuggingFace Course notebooks now have working links
- ✅ Any future notebooks with spaces will automatically be encoded
- ✅ Special characters (parentheses, etc.) are handled correctly

### No Regression
- ✅ Regular notebooks (without spaces) still work
- ✅ All existing tests continue to pass
- ✅ No changes to notebook files themselves

## Future-Proofing

This fix ensures that:
1. **Any filename** can be used, including those with spaces and special characters
2. **GitHub links** work correctly in markdown
3. **Automatic handling** - no manual encoding needed
4. **Test coverage** prevents regression

## Files Modified

| File | Change |
|------|--------|
| `scripts/generate_readme_table.py` | Added URL encoding for notebook links |
| `tests/test_readme_table.py` | Added URL encoding test |
| `README.md` | Regenerated with encoded links |

## Related Issues

This fix resolves the issue where users clicking "View Notebook" links for HuggingFace Course notebooks would get 404 errors.

## Testing Checklist

- [x] Unit tests pass
- [x] Manual verification of affected links
- [x] Checked both encoded and non-encoded paths work
- [x] Verified no regression in existing functionality
- [x] Test coverage added for URL encoding

---

**Status:** ✅ Complete  
**All notebook links now working correctly!**

