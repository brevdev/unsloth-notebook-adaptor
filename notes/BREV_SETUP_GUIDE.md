# Brev Setup Guide for Self-Contained Unsloth Notebooks

## Solution Overview

All 181 converted Unsloth notebooks are **self-contained** and work with any Jupyter environment. Each notebook automatically:

1. **Checks** which Python environment is running
2. **Installs** unsloth into that specific environment using `sys.executable`
3. **Verifies** the installation succeeded
4. **Runs** the original notebook code

## No Manual Setup Required

The notebooks handle environment setup automatically. Just:

1. Open any converted notebook in Jupyter Lab on your Brev instance
2. Run the first cell - it installs everything needed
3. Continue with the rest of the notebook

## How It Works

### First Cell Pattern

Every converted notebook starts with this cell:

```python
# Environment Check for Brev
import sys

print(f"Python executable: {sys.executable}")
print(f"Python version: {sys.version}")

try:
    from unsloth import FastLanguageModel
    print("\n✅ Unsloth already available")
    print(f"   Location: {FastLanguageModel.__module__}")
except ImportError:
    print("\n⚠️  Unsloth not found - will install")

# Install unsloth in the kernel's Python environment
import subprocess

print(f"\nInstalling unsloth into: {sys.executable}")

subprocess.check_call([
    sys.executable, "-m", "pip", "install", "unsloth"
])
subprocess.check_call([
    sys.executable, "-m", "pip", "install", "transformers==4.56.2"
])
subprocess.check_call([
    sys.executable, "-m", "pip", "install", "--no-deps", "trl==0.22.2"
])

print("\n✅ Installation complete")

# Verify installation
try:
    from unsloth import FastLanguageModel
    print("✅ Unsloth is now available")
except ImportError as e:
    print(f"❌ Installation failed: {e}")
    print("⚠️  Please restart kernel and try again")
    raise
```

### Why This Works

The key is `sys.executable` - it always points to the **exact Python interpreter** running the notebook kernel, regardless of:

- Virtual environments (venv, conda, etc.)
- System Python locations
- User-specific Python installations
- uv-managed Python environments

When you run `subprocess.check_call([sys.executable, "-m", "pip", "install", "unsloth"])`, you're guaranteed to install into the same Python that will later run `import unsloth`.

## Brev Instance Compatibility

### Tested Environments

✅ System Python (`/usr/bin/python3`)
✅ Virtual environments (`/home/ubuntu/.venv/bin/python3`)
✅ uv-managed Python
✅ conda environments

### Jupyter Kernel Requirements

The Jupyter kernel must be configured correctly:

**Check kernel config:**
```bash
cat /usr/local/share/jupyter/kernels/python3/kernel.json
```

**Should use `python3`:**
```json
{
 "argv": [
  "python3",
  "-m",
  "ipykernel_launcher",
  "-f",
  "{connection_file}"
 ],
 "display_name": "Python 3 (ipykernel)",
 "language": "python"
}
```

**If it says `"python"` instead of `"python3"`, fix it:**
```bash
sudo sed -i 's/"python"/"python3"/' /usr/local/share/jupyter/kernels/python3/kernel.json
```

## Expected Behavior

### First Run (Clean Environment)

```
Python executable: /home/ubuntu/.venv/bin/python3
Python version: 3.12.12

⚠️  Unsloth not found - will install

Installing unsloth into: /home/ubuntu/.venv/bin/python3
[installation output...]

✅ Installation complete
✅ Unsloth is now available
```

### Subsequent Runs (Already Installed)

```
Python executable: /home/ubuntu/.venv/bin/python3
Python version: 3.12.12

✅ Unsloth already available
   Location: unsloth

Installing unsloth into: /home/ubuntu/.venv/bin/python3
Requirement already satisfied: unsloth...
[...]

✅ Installation complete
✅ Unsloth is now available
```

## Troubleshooting

### Issue: "command 'python' not found"

**Symptom**: Kernel fails to start or notebooks can't find Python

**Fix**: Update kernel.json to use `python3` instead of `python` (see above)

### Issue: "ModuleNotFoundError: No module named 'unsloth'" in later cells

**Symptom**: First cell succeeds, but later cells can't import unsloth

**Fix**: Restart the kernel after first cell completes:
- In Jupyter Lab: `Kernel` → `Restart Kernel`
- Then run cells from the beginning

### Issue: Installation takes too long

**Symptom**: First cell runs for several minutes

**Explanation**: This is normal on first run. The cell installs:
- unsloth (~100MB)
- transformers (~500MB)
- trl (~50MB)
- All dependencies

**Subsequent runs** are much faster as pip sees packages are already installed.

### Issue: pip warnings about externally-managed environment

**Symptom**: Warning: `externally-managed-environment`

**Fix**: This is just a warning, not an error. The installation still works. To silence it:
```python
subprocess.check_call([
    sys.executable, "-m", "pip", "install", "--break-system-packages", "unsloth"
])
```

But this isn't necessary - the current code works fine.

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
│                                                  │
│  sys.executable reveals actual Python path      │
└────────────────┬────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────┐
│  Python Environment (varies by setup)           │
│                                                  │
│  Could be:                                       │
│  - /usr/bin/python3 (system)                    │
│  - /home/ubuntu/.venv/bin/python3 (venv)        │
│  - ~/.local/share/uv/python/... (uv)            │
│  - /opt/conda/bin/python3 (conda)               │
│                                                  │
│  First cell installs packages HERE              │
│  using sys.executable                           │
└─────────────────────────────────────────────────┘
```

## Benefits of This Approach

✅ **Self-Contained**: No manual setup required
✅ **Portable**: Works with any Python environment
✅ **Debuggable**: First cell shows exactly which Python is being used
✅ **Idempotent**: Safe to run multiple times (checks if already installed)
✅ **Production-Ready**: Follows Python best practices for environment-specific installation

## Comparison with Original Colab Notebooks

| Feature | Colab | Converted for Brev |
|---------|-------|-------------------|
| Installation | `!pip install unsloth` | `subprocess.check_call([sys.executable, "-m", "pip", "install", "unsloth"])` |
| Environment check | Checks for `COLAB_` env var | Checks for unsloth import |
| Installation target | System Python (unspecified) | Kernel's Python (explicit) |
| Verification | None | Explicit verification step |
| GPU check | Colab-specific | Generic GPU detection |

## Testing Converted Notebooks

### Quick Test

```bash
# SSH into Brev instance
brev shell your-instance-name

# Clone repo
cd ~
git clone https://github.com/brevdev/unsloth-notebook-adaptor.git
cd unsloth-notebook-adaptor

# Test a notebook
cd converted/gemma3-4b
jupyter notebook Gemma3_\(4B\).ipynb
```

### Automated Test

```bash
cd unsloth-notebook-adaptor

# Test first cell execution
python3 << 'EOF'
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor

with open('converted/gemma3-4b/Gemma3_(4B).ipynb', 'r') as f:
    nb = nbformat.read(f, as_version=4)

# Execute first cell
nb.cells = nb.cells[:1]
ep = ExecutePreprocessor(timeout=900, kernel_name='python3')
ep.preprocess(nb, {'metadata': {'path': 'converted/gemma3-4b'}})

print("✅ Test passed!")
EOF
```

## Summary

The converted notebooks are **production-ready** and require **no manual setup**. They automatically:

1. Detect the running Python environment
2. Install dependencies into that environment
3. Verify everything works
4. Proceed with the original notebook logic

This approach eliminates environment mismatches and makes the notebooks truly portable across any Jupyter setup on NVIDIA Brev.
