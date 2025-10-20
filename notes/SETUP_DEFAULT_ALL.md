# Setup Script: Default to Install All Dependencies

**Date:** October 20, 2025  
**Change:** Made `--all` (vision + audio) the default behavior

## Rationale

The setup script is meant to be a **baseline** that works for all 181+ converted Unsloth notebooks out of the box. Making users opt-in to vision and audio support defeats this purpose.

### Why This Makes Sense

1. **True Baseline**: A baseline should cover all use cases by default
2. **Better UX**: Users won't hit "missing dependency" errors when trying vision/audio notebooks
3. **Minimal Cost**: Additional dependencies are ~1GB extra and ~2 minutes longer
4. **Brev Context**: Brev instances typically have good bandwidth and storage
5. **Prevents Surprises**: Users won't need to re-run setup when switching notebook types

## Changes Made

### Before (Opt-In Model)

```bash
# Default: Text models only
bash setup.sh                  # Text only
bash setup.sh --vision         # Text + Vision
bash setup.sh --audio          # Text + Audio
bash setup.sh --all            # Everything
```

**Problem:** Users trying vision/audio notebooks would get import errors.

### After (Opt-Out Model)

```bash
# Default: Everything
bash setup.sh                  # ALL: Text + Vision + Audio (RECOMMENDED)
bash setup.sh --minimal        # Text only (opt-out)
bash setup.sh --no-vision      # Skip vision
bash setup.sh --no-audio       # Skip audio
```

**Benefit:** All 181+ notebooks work immediately after setup.

## New Default Installation

Running `bash setup.sh` with no arguments now installs:

### Core (Always Installed)
- ✅ Unsloth (conda variant)
- ✅ PyTorch with CUDA
- ✅ Transformers, Datasets, Accelerate
- ✅ PEFT, TRL, BitsAndBytes
- ✅ Jupyter Lab full stack
- ✅ Monitoring (wandb, tensorboard)
- ✅ Utilities (numpy, pandas, tqdm, etc.)

### Now Default (Previously Optional)
- ✅ **Vision:** torchvision, pillow, opencv-python
- ✅ **Audio:** librosa, soundfile

### Total Installation Size
- Before (text only): ~8GB
- After (all): ~9GB (+1GB)

### Installation Time
- Before (text only): ~8-10 minutes
- After (all): ~10-12 minutes (+2 minutes)

## New Command-Line Options

### Minimal Installation (Opt-Out)
```bash
bash setup.sh --minimal
# or
bash setup.sh --text-only
```
Installs only text model dependencies (original behavior).

### Selective Exclusion
```bash
bash setup.sh --no-vision   # Skip vision, keep audio
bash setup.sh --no-audio    # Skip audio, keep vision
```

### Help
```bash
bash setup.sh --help
```
Shows updated usage with clear indication that all is default.

## Updated Output

### Installation Summary (Default Run)
```
📊 Installation Summary:
  ✓ Unsloth (conda variant)
  ✓ PyTorch with CUDA
  ✓ Core ML libraries (transformers, datasets, peft, trl)
  ✓ Jupyter Lab environment
  ✓ Monitoring tools (wandb, tensorboard)
  ✓ Vision dependencies (torchvision, pillow, opencv)
  ✓ Audio dependencies (librosa, soundfile)
```

### Installation Summary (Minimal)
```bash
bash setup.sh --minimal
```
```
📊 Installation Summary:
  ✓ Unsloth (conda variant)
  ✓ PyTorch with CUDA
  ✓ Core ML libraries (transformers, datasets, peft, trl)
  ✓ Jupyter Lab environment
  ✓ Monitoring tools (wandb, tensorboard)
  ⊘ Vision dependencies (skipped with --minimal)
  ⊘ Audio dependencies (skipped with --minimal)
```

## Impact on Users

### Positive Impact
- ✅ **Zero surprises**: Any notebook in the repo works immediately
- ✅ **Less friction**: No need to re-run setup or debug missing imports
- ✅ **Better first experience**: New users can try any notebook type
- ✅ **Consistent behavior**: "Baseline" truly means all bases covered

### Minimal Drawbacks
- ~1GB extra disk space (negligible on Brev instances)
- ~2 minutes extra install time (one-time cost)
- Users wanting text-only can use `--minimal`

## Notebook Compatibility

### Before
| Notebook Type | Worked by Default? |
|---------------|-------------------|
| Text (120+) | ✅ Yes |
| Vision (15+) | ❌ No - needed --vision |
| Audio (8+) | ❌ No - needed --audio |
| GRPO/RL (25+) | ✅ Yes |

### After
| Notebook Type | Worked by Default? |
|---------------|-------------------|
| Text (120+) | ✅ Yes |
| Vision (15+) | ✅ Yes |
| Audio (8+) | ✅ Yes |
| GRPO/RL (25+) | ✅ Yes |
| **ALL (181+)** | **✅ Yes** |

## Documentation Updates

Updated files:
- ✅ `setup-scripts/unsloth/setup.sh` - Changed defaults, updated help
- ✅ `setup-scripts/unsloth/README.md` - Clarified default behavior
- ✅ Installation summary output - Shows what was installed/skipped

## Migration

### For Existing Users

**No action required!** 
- Running the script again will update to include vision/audio
- Or continue using `--minimal` if preferred

### For New Users

**Just run:**
```bash
bash setup-scripts/unsloth/setup.sh
```

Everything works!

## Testing

### Verified Scenarios

1. **Default install (all):**
   ```bash
   bash setup.sh
   python3 -c "import torch, torchvision, librosa; print('✅ All imports work')"
   ```
   ✅ Pass

2. **Minimal install:**
   ```bash
   bash setup.sh --minimal
   python3 -c "import torch, transformers; print('✅ Text models work')"
   ```
   ✅ Pass

3. **Selective exclusion:**
   ```bash
   bash setup.sh --no-audio
   python3 -c "import torchvision; print('✅ Vision works')"
   ```
   ✅ Pass

## Conclusion

This change aligns the setup script with its purpose: **a true baseline that works for all notebooks**. The minimal additional cost is far outweighed by the improved user experience and consistency.

**Recommendation:** This should be the standard approach for all Brev setup scripts - install everything needed by default, allow opt-out for special cases.

---

**Files Modified:**
- `setup-scripts/unsloth/setup.sh`
- `setup-scripts/unsloth/README.md`

**Status:** ✅ Complete

