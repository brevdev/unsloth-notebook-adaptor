# README Table Update Summary

**Date:** October 20, 2025  
**Status:** ✅ Complete

## 🎨 Changes Made

Updated the README launchables table to match the clean, professional style of the [Unsloth notebooks README](https://github.com/unslothai/notebooks/blob/main/README.md).

## 📊 Before vs After

### ❌ Before (Old Format)

```markdown
| Model | Description | GPU | VRAM | Categories | Deploy |
|-------|-------------|-----|------|------------|--------|
| Gemma3 (4B) | Fine-tune Gemma3 (4B) with Unsloth on NVIDIA GPUs | L4 | 16GB | General |  |
| Llama3 | Fine-tune Llama3 with Unsloth on NVIDIA GPUs | L4 | 16GB | General |  |
```

**Issues:**
- 6 columns (too wide)
- Plain model names (not bold)
- Generic descriptions
- Empty deploy column
- Single flat table (129 rows, hard to browse)
- No categorization

### ✅ After (New Format - Unsloth-style)

```markdown
### Main Notebooks

| Model | Type | GPU Requirements | Notebook Link |
|-------|------|------------------|---------------|
| **Gemma3 (4B)** | Fine-tuning | L4 (16GB) | [View Notebook](converted/gemma3-4b/Gemma3_(4B).ipynb) |
| **Llama3** | Conversational | L4 (16GB) | [View Notebook](converted/llama3/Llama3.3_(70B)_A100-Conversational.ipynb) |

### Vision (Multimodal) Notebooks

| Model | Type | GPU Requirements | Notebook Link |
|-------|------|------------------|---------------|
| **Gemma3 (4B) Vision Grpo** | Vision | L4 (16GB) | [View Notebook](converted/gemma3-4b-vision-grpo/Gemma3_(4B)-Vision.ipynb) |

### Text-to-Speech (TTS) Notebooks

| Model | Type | GPU Requirements | Notebook Link |
|-------|------|------------------|---------------|
| **Sesame-CSM (1B)** | TTS | T4 (12GB) | [View Notebook](converted/sesame-csm-1b/Sesame_CSM_(1B)-TTS.ipynb) |
```

**Improvements:**
- ✅ 4 columns (clean and readable)
- ✅ **Bold model names** for emphasis
- ✅ Concise types (Alpaca, Vision, TTS, GRPO, etc.)
- ✅ Combined GPU requirements (tier + VRAM)
- ✅ Direct links to notebooks
- ✅ **Categorized by type** (6 categories)
- ✅ Easy to browse and find specific models

## 📂 Categories

The 129 launchables are now organized into 6 logical categories:

1. **Main Notebooks** (~62 entries)
   - Popular models: Llama, Gemma, Qwen, Phi, Mistral
   - General fine-tuning and conversational models
   
2. **Vision (Multimodal) Notebooks** (~12 entries)
   - Gemma3 Vision, Llama3.2 Vision, Qwen2.5 VL, Pixtral
   
3. **Text-to-Speech (TTS) Notebooks** (~7 entries)
   - Sesame-CSM, Orpheus, Spark-TTS, Oute-TTS, Llasa TTS
   
4. **Speech-to-Text (STT) Notebooks** (~2 entries)
   - Whisper models
   
5. **GRPO Notebooks** (~27 entries)
   - Reinforcement learning / reasoning models
   - HuggingFace Course variants
   
6. **Other Notebooks** (~19 entries)
   - Specialized models (BERT, GPT-OSS, etc.)
   - Inference-only, synthetic data, etc.

## 🔧 Implementation Details

### Updated Scripts

**File:** `scripts/generate_readme_table.py`

**New Functions:**
1. `get_model_type(launchable)` - Intelligently determines model type from tags and filename
   - Returns: "Vision", "TTS", "STT", "GRPO", "Alpaca", "Conversational", etc.
   
2. `categorize_launchables(launchables)` - Groups models by category
   - Returns: Dict mapping category names to lists of launchables
   
3. `generate_table(launchables)` - Updated to create categorized tables
   - Generates multiple tables (one per category)
   - Formats with bold names and direct links

### Type Detection Logic

```python
# Checks tags first, then notebook filename
if 'vision' in tags:
    return 'Vision'
elif 'tts' in tags:
    return 'TTS'
elif 'grpo' in notebook_name:
    return 'GRPO'
elif 'alpaca' in notebook_name:
    return 'Alpaca'
# ... and more
```

### Categorization Logic

```python
# Groups by primary purpose
if model_type == 'Vision':
    categories['Vision (Multimodal) Notebooks'].append(launchable)
elif model_type == 'TTS':
    categories['Text-to-Speech (TTS) Notebooks'].append(launchable)
# ... etc
```

## 📝 Updated README Sections

### Section 1: Intro (New)

```markdown
## 📒 Available Launchables

Below are **181 Unsloth notebooks** organized into **129 launchables** for NVIDIA Brev, 
categorized by model type. Each notebook is fully adapted for Brev environments with 
GPU-optimized configurations, companion files, and ready-to-run setups.

**Quick Start:** Browse the notebooks below, clone this repo, and deploy on Brev Console 
or run locally with Docker. View the original Unsloth notebooks here.
```

**Style notes:**
- Similar to Unsloth's intro paragraph
- Provides context and quick navigation
- Links to both Brev Console and upstream repo

### Section 2: Tables (Updated)

- 6 categorized tables instead of 1 flat table
- Bold model names
- Concise types
- Direct notebook links

### Section 3: Manual Deploy (Kept)

- Instructions for deploying on Brev Console
- List of included files per launchable

## 🎯 Comparison with Unsloth README

### What We Adopted

✅ **Clean 3-4 column layout** (Model | Type | Link)  
✅ **Bold model names** with sizes  
✅ **Categorized sections** (Main, Vision, TTS, etc.)  
✅ **Concise type labels** (Alpaca, Vision, GRPO)  
✅ **Direct links** to notebooks  
✅ **Intro paragraph** with context and navigation

### What We Customized for Brev

🔧 **Added GPU Requirements column** - Shows recommended tier and VRAM  
🔧 **Links to our repo** - Instead of Colab badges, direct GitHub links  
🔧 **Brev-specific context** - References Brev Console and deployment  
🔧 **129 launchables** - Grouped notebooks vs individual files  

## 📈 Statistics

| Metric | Count |
|--------|-------|
| Total Notebooks | 181 |
| Unique Launchables | 129 |
| Categories | 6 |
| Main Notebooks | ~62 |
| Vision Notebooks | ~12 |
| TTS Notebooks | ~7 |
| STT Notebooks | ~2 |
| GRPO Notebooks | ~27 |
| Other Notebooks | ~19 |

## ✅ Benefits

### For Users
- **Easier browsing** - Find models by category
- **Quick identification** - Bold names and clear types
- **Direct access** - Click links to view notebooks
- **GPU clarity** - See requirements at a glance

### For Maintainers
- **Automated** - Script generates table from metadata
- **Consistent** - Same format across all entries
- **Scalable** - Easy to add new categories
- **Flexible** - Type detection adapts to new models

## 🚀 How to Regenerate

```bash
cd unsloth-notebook-adaptor
source venv/bin/activate
python3 scripts/generate_readme_table.py \
  --metadata-path metadata/launchables.json \
  --readme-path README.md
```

The script will:
1. Load metadata from `launchables.json`
2. Categorize all 129 launchables
3. Generate formatted tables
4. Update README between `<!-- LAUNCHABLES_TABLE_START -->` and `<!-- LAUNCHABLES_TABLE_END -->` markers

## 📁 Related Files

- **Script:** `scripts/generate_readme_table.py` (updated)
- **Metadata:** `metadata/launchables.json` (source of truth)
- **README:** `README.md` (updated table section)

## 🎉 Result

The README now has a **professional, easy-to-navigate table** that:
- Matches the Unsloth style and quality
- Makes it simple to find specific models
- Provides all necessary information at a glance
- Works seamlessly with automated updates

Perfect for showcasing the 181 converted notebooks! 🚀

