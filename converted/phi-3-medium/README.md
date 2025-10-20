# Phi 3 Medium Conversational - NVIDIA Brev Launchable

Fine-tune Phi 3 Medium Conversational with Unsloth on NVIDIA GPUs using Brev.

🔗 **Original Notebook:** [Unsloth Colab Notebook](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Phi_3_Medium-Conversational.ipynb)

## 🚀 Quick Start (Brev Console)

1. **Launch on Brev:**
   ```bash
   brev launch phi-3-medium
   ```

2. **Open Jupyter Lab:**
   - Navigate to the provided URL (port 8888)
   - Open the notebook and start training

## 📊 Requirements

| Requirement | Value |
|------------|-------|
| **Recommended GPU** | L4 |
| **Minimum VRAM** | 16 GB |
| **Batch Size** | 2 |
| **Difficulty** | intermediate |
| **Categories** | fine-tuning |

## 🛠️ Local Setup (Optional)

If you want to run this locally with Docker:

```bash
# Clone the repository
git clone <repo-url>
cd phi-3-medium

# Start with Docker Compose
docker-compose up

# Access Jupyter Lab at http://localhost:8888
```

### Prerequisites

- Docker with NVIDIA GPU support
- NVIDIA drivers installed
- CUDA 12.1+

## 📝 What's Included

- Original notebook file (`.ipynb`) - Main training notebook (converted from Colab)
- `requirements.txt` - Python dependencies
- `setup.sh` - Environment setup script
- `docker-compose.yml` - Docker configuration
- `.brevconfig.json` - Brev metadata

## 🔧 Key Adaptations

This notebook has been adapted from the original Unsloth Colab version with the following changes:

- ✅ Replaced Colab-specific installation with conda variant
- ✅ Converted magic commands to subprocess calls
- ✅ Removed Google Drive dependencies
- ✅ Updated paths from `/content/` to `/workspace/`
- ✅ Added `device_map="auto"` for multi-GPU support
- ✅ Optimized batch sizes for NVIDIA GPUs

## 📚 Links

- [Unsloth Documentation](https://docs.unsloth.ai/)
- [Brev Documentation](https://docs.nvidia.com/brev)
- [Original Notebook](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Phi_3_Medium-Conversational.ipynb)
- [Report Issues](https://github.com/brevdev/unsloth-notebook-adaptor/issues)

## 📄 License

This adaptation maintains the original license from Unsloth. See the upstream repository for details.

---

**Powered by [Unsloth](https://unsloth.ai/) 🦥 + [Brev](https://developer.nvidia.com/brev) ⚡**
