# 🚀 Unsloth to NVIDIA Brev Adapter

[![Sync Notebooks](https://github.com/brevdev/unsloth-notebook-adaptor/actions/workflows/sync-and-convert.yml/badge.svg)](https://github.com/brevdev/unsloth-notebook-adaptor/actions/workflows/sync-and-convert.yml)
[![Test Conversions](https://github.com/brevdev/unsloth-notebook-adaptor/actions/workflows/test-conversions.yml/badge.svg)](https://github.com/brevdev/unsloth-notebook-adaptor/actions/workflows/test-conversions.yml)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: LGPL-3.0](https://img.shields.io/badge/License-LGPL%203.0-blue.svg)](https://www.gnu.org/licenses/lgpl-3.0)

Automatically sync and convert [Unsloth](https://unsloth.ai/) Colab notebooks to NVIDIA Brev-compatible launchables. This repository provides a production-ready pipeline that:

- ⚡ **Syncs daily** with the [unslothai/notebooks](https://github.com/unslothai/notebooks) repository
- 🔄 **Automatically converts** Colab-specific code to Brev-compatible format
- 🐳 **Generates companion files** (requirements.txt, setup.sh, docker-compose.yml, README)
- 🧪 **Tests all conversions** with comprehensive pytest suite
- 📦 **Creates launchables** ready to deploy on NVIDIA Brev

## 📋 What This Does

This adapter transforms Unsloth Colab notebooks for seamless use on NVIDIA Brev by:

1. **Installation Conversion** - Replaces `unsloth[colab-new]` with `unsloth[conda]`
2. **Magic Commands** - Converts `!` and `%` commands to `subprocess` calls
3. **Storage Adaptation** - Removes Google Drive mounting, updates paths to `/workspace/`
4. **GPU Configuration** - Adds `device_map="auto"` for multi-GPU support
5. **Batch Size Optimization** - Adjusts batch sizes for NVIDIA GPUs
6. **Companion Files** - Generates setup scripts, Docker configs, and documentation

## 🚀 Available Launchables

<!-- LAUNCHABLES_TABLE_START -->
*Launchables table will be auto-generated here after first sync*
<!-- LAUNCHABLES_TABLE_END -->

**Note:** Deploy buttons will be added by the Brev team as Launchables are created on the platform.

### Manual Deploy Instructions

To deploy any converted notebook to Brev:

1. **Go to Brev Console**: [brev.nvidia.com](https://brev.nvidia.com)
2. **Create New Launchable**: Navigate to Launchables → Create New
3. **Configure Settings**:
   - **Repository**: `https://github.com/brevdev/unsloth-notebook-adaptor`
   - **Path**: `converted/{model-name}` (see table above for exact model names)
   - **GPU Tier**: Use recommended tier from table above
   - **Port**: 8888 (for Jupyter Lab)
4. **Deploy**: Click Deploy and access Jupyter at the provided URL

All converted notebooks include:
- `notebook.ipynb` - Main training notebook
- `requirements.txt` - Python dependencies  
- `setup.sh` - Environment setup script
- `docker-compose.yml` - Local Docker configuration
- `README.md` - Model-specific documentation
- `.brevconfig.json` - Brev metadata

## 🎯 Quick Start for Users

### Deploy on Brev Console

```bash
# Browse available launchables
ls converted/

# Launch a specific model (example)
cd converted/llama-3.1-8b-fine-tuning
cat README.md  # View instructions

# Or use with Docker
docker-compose up
```

All converted notebooks are in the `converted/` directory, organized by model name.

## 🛠️ Quick Start for Contributors

### Local Setup

```bash
# Clone the repository
git clone git@github.com:brevdev/unsloth-notebook-adaptor.git
cd unsloth-notebook-adaptor

# Install dependencies
pip install -r requirements.txt

# Run tests
pytest tests/ -v
```

### Manual Conversion

```bash
# Clone Unsloth notebooks
git clone https://github.com/unslothai/notebooks.git unsloth-notebooks

# Convert all notebooks
python scripts/convert_notebook.py \
  --source unsloth-notebooks/nb \
  --output converted

# Or convert specific notebooks
python scripts/convert_notebook.py \
  --source unsloth-notebooks/nb \
  --output converted \
  --notebooks "Llama_3.1_(8B).ipynb" "Gemma_3_(4B).ipynb"
```

## 📁 Repository Structure

```
unsloth-notebook-adaptor/
├── .github/workflows/       # GitHub Actions automation
│   ├── sync-and-convert.yml      # Daily sync workflow
│   └── test-conversions.yml      # Test suite on PR
├── adapters/                # Conversion logic
│   ├── base_adapter.py           # Base adapter class
│   ├── colab_to_brev.py         # Colab→Brev conversions
│   └── model_configs.py         # Model-specific configs
├── templates/               # Jinja2 templates
│   ├── requirements.txt.jinja2
│   ├── setup.sh.jinja2
│   ├── docker-compose.yml.jinja2
│   └── README.md.jinja2
├── converted/               # Output: converted notebooks
│   └── [launchable-name]/
│       ├── notebook.ipynb
│       ├── requirements.txt
│       ├── setup.sh
│       ├── docker-compose.yml
│       ├── README.md
│       └── .brevconfig.json
├── metadata/                # Tracking and registry
│   ├── launchables.json         # Registry of all launchables
│   └── last_sync.txt            # Last synced commit hash
├── scripts/                 # CLI tools
│   ├── convert_notebook.py      # Main conversion script
│   ├── compare_notebooks.py     # Detect upstream changes
│   ├── generate_metadata.py     # Build registry
│   └── create_summary.py        # GitHub Actions summary
└── tests/                   # Test suite
    ├── test_conversions.py
    └── test_notebooks.py
```

## 🔧 How It Works

### 1. Daily Sync (Automated)

GitHub Actions runs daily at 6 AM UTC:
- Checks out the latest Unsloth notebooks
- Compares against last synced commit
- Converts any changed notebooks
- Generates metadata registry
- Commits and pushes changes

### 2. Conversion Pipeline

For each notebook:
1. Load source notebook and model configuration
2. Apply conversion functions (installation, magic commands, storage, etc.)
3. Add Brev header cell with model information
4. Generate companion files from Jinja2 templates
5. Save adapted notebook and files to `converted/[launchable-name]/`

### 3. Quality Assurance

- Comprehensive pytest suite tests all conversion functions
- Integration tests verify end-to-end notebook adaptation
- GitHub Actions runs tests on all PRs and commits

## 🎨 Key Conversions

### Before (Colab)

```python
# Installation
!pip install "unsloth[colab-new] @ git+https://github.com/unslothai/unsloth.git"

# GPU Check
!nvidia-smi

# Storage
from google.colab import drive
drive.mount('/content/drive')
model_path = '/content/drive/MyDrive/models'

# Model Loading
model = FastLanguageModel.from_pretrained(
    "unsloth/llama-3-8b",
    max_seq_length=2048,
    load_in_4bit=True
)
```

### After (Brev)

```python
# Installation
import subprocess
import sys

subprocess.check_call([
    sys.executable, "-m", "pip", "install",
    "unsloth[conda] @ git+https://github.com/unslothai/unsloth.git"
])

# GPU Check
subprocess.run(['nvidia-smi'], check=False)

# Storage
model_path = '/workspace/models'

# Model Loading
model = FastLanguageModel.from_pretrained(
    "unsloth/llama-3-8b",
    max_seq_length=2048,
    load_in_4bit=True,
    device_map="auto"  # Added for multi-GPU support
)
```

## 🦙 Supported Models

### Language Models (LLMs)
- **gpt-oss** (20B, 120B) - Reasoning models
- **Llama 3.1** (8B), **Llama 3.2** (1B, 3B) - Text generation
- **Gemma 3** (1B, 4B, 27B), **Gemma 3n** (E4B) - Multimodal
- **Qwen3** (4B, 14B, 32B) - Text generation
- **Phi-4** (14B) - Reasoning

### Vision Models (VLMs)
- **Llama 3.2 Vision** (11B)
- **Qwen3-VL** (8B)
- **Gemma 3 Vision** (4B)

### Audio Models
- **Whisper Large V3** - Speech-to-Text (STT)
- **Orpheus-TTS** (3B) - Text-to-Speech
- **Sesame-CSM** (1B) - Text-to-Speech

### Reinforcement Learning (GRPO)
- **gpt-oss-20b GRPO**
- **Qwen3-VL GRPO** - Vision RL
- **Gemma 3 GRPO**
- **Llama 3.2 GRPO**
- **Phi-4 GRPO**

See [`adapters/model_configs.py`](adapters/model_configs.py) for complete list with GPU requirements.

## 🧪 Testing

```bash
# Run all tests
pytest tests/ -v

# Run with coverage
pytest tests/ --cov=adapters --cov-report=term --cov-report=html

# Run specific test file
pytest tests/test_conversions.py -v

# Run specific test
pytest tests/test_conversions.py::test_convert_installation -v
```

## 🤝 Contributing

We welcome contributions! Here's how to help:

1. **Add New Models** - Update [`adapters/model_configs.py`](adapters/model_configs.py)
2. **Improve Conversions** - Enhance conversion functions in [`adapters/colab_to_brev.py`](adapters/colab_to_brev.py)
3. **Fix Bugs** - Submit PRs with test coverage
4. **Report Issues** - Use [GitHub Issues](https://github.com/brevdev/unsloth-notebook-adaptor/issues)

### Development Workflow

```bash
# Create a feature branch
git checkout -b feature/my-improvement

# Make changes and test
pytest tests/ -v

# Commit with conventional commits
git commit -m "feat: add support for new model"

# Push and create PR
git push origin feature/my-improvement
```

## 📊 Metadata Registry

The `metadata/launchables.json` file contains a complete registry of all converted launchables:

```json
{
  "version": "1.0.0",
  "generated_at": "2025-10-20T12:00:00Z",
  "total_launchables": 25,
  "launchables": [
    {
      "id": "llama-3.1-8b-fine-tuning",
      "name": "Llama 3.1 (8B)",
      "description": "Fine-tune Llama 3.1 (8B) with Unsloth on NVIDIA GPUs",
      "notebook": "notebook.ipynb",
      "path": "llama-3.1-8b-fine-tuning",
      "gpu": {
        "tier": "L4",
        "min_vram_gb": 16,
        "multi_gpu": false
      },
      "tags": ["unsloth", "fine-tuning", "text-generation"],
      "upstream": {
        "source": "unslothai/notebooks",
        "notebook_url": "https://colab.research.google.com/...",
        "last_synced": "2025-10-20T12:00:00Z"
      },
      "files": [...]
    }
  ]
}
```

## 🔗 Links

- **Unsloth** - [Website](https://unsloth.ai/) | [Docs](https://docs.unsloth.ai/) | [GitHub](https://github.com/unslothai/unsloth)
- **NVIDIA Brev** - [Website](https://developer.nvidia.com/brev) | [Docs](https://docs.nvidia.com/brev)
- **Original Notebooks** - [unslothai/notebooks](https://github.com/unslothai/notebooks)
- **Issues & Support** - [GitHub Issues](https://github.com/brevdev/unsloth-notebook-adaptor/issues)

## 📄 License

This project is licensed under the LGPL-3.0 License - see the [LICENSE](LICENSE) file for details.

The converted notebooks maintain their original licenses from the Unsloth project.

## 🙏 Acknowledgments

- **[Unsloth AI](https://unsloth.ai/)** for the amazing fine-tuning framework and notebooks
- **[NVIDIA Brev](https://developer.nvidia.com/brev)** for providing the GPU infrastructure platform
- All contributors to the Unsloth and Brev communities

---

**Built with ❤️ by the Brev team** | [Brev](https://developer.nvidia.com/brev) | [Unsloth](https://unsloth.ai/)

