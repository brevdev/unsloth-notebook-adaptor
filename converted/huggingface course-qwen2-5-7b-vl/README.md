# Huggingface Course Qwen2 5 7B Vl Grpo - NVIDIA Brev Launchable

Fine-tune Huggingface Course Qwen2 5 7B Vl Grpo with Unsloth on NVIDIA GPUs using Brev.

🔗 **Original Notebook:** [Unsloth Colab Notebook](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/HuggingFace Course-Qwen2_5_7B_VL_GRPO.ipynb)

## 🚀 Quick Start (Brev Console)

1. **Launch on Brev:**
   ```bash
   brev launch huggingface course-qwen2-5-7b-vl
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
cd huggingface course-qwen2-5-7b-vl

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
- [Original Notebook](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/HuggingFace Course-Qwen2_5_7B_VL_GRPO.ipynb)
- [Report Issues](https://github.com/brevdev/unsloth-notebook-adaptor/issues)

## 📄 License

This adaptation maintains the original license from Unsloth. See the upstream repository for details.

---

**Powered by [Unsloth](https://unsloth.ai/) 🦥 + [Brev](https://developer.nvidia.com/brev) ⚡**
