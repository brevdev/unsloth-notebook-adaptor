# gpt-oss-20b-GRPO - NVIDIA Brev Launchable

Fine-tune gpt-oss-20b-GRPO with Unsloth on NVIDIA GPUs using Brev.

🔗 **Original Notebook:** [View on GitHub](https://github.com/unslothai/notebooks/blob/main/nb/gpt-oss-20b-grpo.ipynb)

## 🤙 Quick Start with NVIDIA Brev

NVIDIA Brev provides streamlined access to NVIDIA GPU instances, automatic environment setup, and flexible deployment options.

### Provision
Brev provisions a GPU for you - no need to set up cloud accounts. We have solid GPU supply.

### Configure
Brev configures your GPU with the right drivers and libraries. Advanced options available for Docker containers.

### Connect
```bash
# Open in your preferred editor
brev open gpt-oss-20b-grpo-rl

# Or SSH directly
ssh gpt-oss-20b-grpo-rl
```

**Deploy this notebook:** [Click here to deploy on Brev Console](https://brev.nvidia.com)

## 📊 Requirements

| Requirement | Value |
|------------|-------|
| **Recommended GPU** | A100-80GB |
| **Minimum VRAM** | 40 GB |
| **Batch Size** | 1 |
| **Difficulty** | advanced |
| **Categories** | reasoning, reinforcement-learning, grpo |

## 🛠️ Local Setup (Optional)

If you want to run this locally with Docker:

```bash
# Clone the repository
git clone <repo-url>
cd gpt-oss-20b-grpo-rl

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
- [Original Notebook](https://github.com/unslothai/notebooks/blob/main/nb/gpt-oss-20b-grpo.ipynb)
- [Report Issues](https://github.com/brevdev/unsloth-notebook-adaptor/issues)

## 📄 License

This adaptation maintains the original license from Unsloth. See the upstream repository for details.

---

**Powered by [Unsloth](https://unsloth.ai/) 🦥 + [Brev](https://developer.nvidia.com/brev) ⚡**
