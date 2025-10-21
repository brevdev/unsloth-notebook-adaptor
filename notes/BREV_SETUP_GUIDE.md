# Brev Instance Setup Guide for Unsloth Notebooks

## Problem Summary

The converted Unsloth notebooks were failing with `ModuleNotFoundError: No module named 'unsloth'` when run in Jupyter Lab on Brev instances, even though `unsloth` was installed on the system.

**Root Cause**: Jupyter kernel misconfiguration - the kernel was configured to use `python` (which doesn't exist), while the system only has `python3`.

## Solution

### 1. Fix Jupyter Kernel Configuration

The default Jupyter kernel on Brev instances uses `"python"` in its configuration, but only `python3` exists on the system.

**Fix the kernel on your Brev instance:**

```bash
# SSH into your Brev instance
brev shell your-instance-name

# Backup the original kernel config
sudo cp /usr/local/share/jupyter/kernels/python3/kernel.json \
     /usr/local/share/jupyter/kernels/python3/kernel.json.backup

# Update kernel.json to use python3
sudo tee /usr/local/share/jupyter/kernels/python3/kernel.json > /dev/null << 'JSON'
{
 "argv": [
  "python3",
  "-m",
  "ipykernel_launcher",
  "-f",
  "{connection_file}"
 ],
 "display_name": "Python 3 (ipykernel)",
 "language": "python",
 "metadata": {
  "debugger": true
 }
}
JSON
```

### 2. Verify Installation

After fixing the kernel, verify the setup:

```bash
# Check that python3 is available
which python3
# Should output: /usr/bin/python3

# Verify unsloth is installed
python3 -c "from unsloth import FastLanguageModel; print('✅ Unsloth available')"

# Check Jupyter kernel
cat /usr/local/share/jupyter/kernels/python3/kernel.json
# Should show "python3" not "python"
```

### 3. Restart Jupyter Lab

After fixing the kernel configuration:

1. Stop Jupyter Lab if it's running
2. Start Jupyter Lab again
3. Any new notebook kernels will now use the correct Python

**Note**: You may need to restart existing notebook kernels:
- In Jupyter Lab: `Kernel` → `Restart Kernel`

## Converted Notebook Behavior

### Environment Check Cell

All converted notebooks now start with an environment diagnostic cell:

```python
# Environment Check for Brev
import sys

print(f"Python executable: {sys.executable}")
print(f"Python version: {sys.version}")

try:
    from unsloth import FastLanguageModel
    print("\n✅ Unsloth loaded successfully")
    print(f"   Location: {FastLanguageModel.__module__}")
except ImportError as e:
    print(f"\n❌ Unsloth not available in this kernel")
    print(f"   Error: {e}")
    print(f"\n⚠️  Please ensure you're using the 'Python 3 (ipykernel)' kernel")
    print(f"   and that unsloth is installed in the system Python.")
    raise
```

**Expected Output**:
```
Python executable: /usr/bin/python3
Python version: 3.10.12 ...

✅ Unsloth loaded successfully
   Location: unsloth
```

### No Installation from Notebooks

The converted notebooks **do not install packages from within cells**. This is intentional:

- ❌ **Old approach**: Install via `subprocess.check_call([sys.executable, "-m", "pip", "install", "unsloth"])`
- ✅ **New approach**: Pre-install dependencies in the system Python, use diagnostic cells to verify

**Why this is better**:
- Avoids Python environment mismatches
- Faster notebook startup (no repeated installations)
- More predictable and production-ready
- Follows Jupyter best practices

## Prerequisites for Brev Instances

### System Requirements

1. **Python 3.10+** installed as `python3`
2. **Unsloth and dependencies** pre-installed in system Python
3. **Jupyter Lab** with correct kernel configuration

### Installation Script

For new Brev instances, use the setup script:

```bash
# On your Brev instance
cd unsloth-notebook-adaptor
bash setup-scripts/unsloth/setup.sh

# This installs:
# - PyTorch with CUDA
# - Unsloth
# - transformers, datasets, accelerate, peft, trl, bitsandbytes
# - Jupyter Lab
# - Vision and audio dependencies (optional)
```

## Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'unsloth'"

**Check 1**: Verify kernel configuration
```bash
cat /usr/local/share/jupyter/kernels/python3/kernel.json | grep python
```
- Should show `"python3"`, not `"python"`

**Check 2**: Verify unsloth is installed
```bash
python3 -c "import unsloth; print(unsloth.__file__)"
```
- Should print a path like `/usr/local/lib/python3.10/dist-packages/unsloth/__init__.py`

**Check 3**: Restart Jupyter kernel
- In Jupyter Lab: `Kernel` → `Restart Kernel`

### Issue: Different Python path in notebook

If the diagnostic cell shows a different Python than `/usr/bin/python3`:

1. Check which Python the kernel is using:
   ```bash
   jupyter kernelspec list
   cat /usr/local/share/jupyter/kernels/python3/kernel.json
   ```

2. Ensure the kernel config points to the correct Python

3. Restart Jupyter Lab

### Issue: Kernel not found

If Jupyter can't find the Python 3 kernel:

```bash
# Re-register the kernel
python3 -m ipykernel install --user --name python3 --display-name "Python 3 (ipykernel)"
```

## Architecture

```
┌─────────────────────────────────────────────────┐
│  Jupyter Lab (Web Interface)                    │
└────────────────┬────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────┐
│  Jupyter Kernel (ipykernel)                     │
│  Uses: python3 -m ipykernel_launcher            │
└────────────────┬────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────┐
│  Python 3 (/usr/bin/python3)                    │
│  Packages installed in:                         │
│  /usr/local/lib/python3.10/dist-packages/       │
│    ├── unsloth/                                 │
│    ├── torch/                                   │
│    ├── transformers/                            │
│    └── ...                                      │
└─────────────────────────────────────────────────┘
```

## Testing

After setup, test with a sample notebook:

```bash
cd unsloth-notebook-adaptor/converted/gemma3-4b
jupyter notebook Gemma3_\(4B\).ipynb
```

1. Run the first cell (environment check)
2. Should see: `✅ Unsloth loaded successfully`
3. Run the second cell (model loading)
4. Should load without errors

## Summary

- ✅ Jupyter kernel now points to `python3` (not `python`)
- ✅ Unsloth is pre-installed in system Python
- ✅ Notebooks use diagnostic cells, not installation cells
- ✅ All 181 converted notebooks ready to use
- ✅ Production-ready approach following Jupyter best practices

This approach eliminates environment mismatches and provides a clean, maintainable setup for running Unsloth notebooks on NVIDIA Brev.

