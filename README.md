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
| Model | Description | GPU | VRAM | Categories | Deploy |
|-------|-------------|-----|------|------------|--------|
| Sesame-CSM (1B) | Fine-tune Sesame-CSM (1B) with Unsloth on NVIDIA GPUs | T4 | 12GB | audio, text-to-speech |  |
| Whisper Large V3 | Fine-tune Whisper Large V3 with Unsloth on NVIDIA GPUs | L4 | 16GB | audio, speech-to-text |  |
| gpt-oss-120b | Fine-tune gpt-oss-120b with Unsloth on NVIDIA GPUs | A100-80GB | 80GB | reasoning, large-model |  |
| gpt-oss-20b | Fine-tune gpt-oss-20b with Unsloth on NVIDIA GPUs | A100-40GB | 24GB | reasoning, large-model |  |
| gpt-oss-20b-GRPO | Fine-tune gpt-oss-20b-GRPO with Unsloth on NVIDIA GPUs | A100-80GB | 40GB | reasoning, reinforcement-learning, grpo |  |
| Qwen3 (4B) GRPO | Fine-tune Qwen3 (4B) GRPO with Unsloth on NVIDIA GPUs | L4 | 16GB | reinforcement-learning, grpo, reasoning |  |
| Phi-4 (14B) | Fine-tune Phi-4 (14B) with Unsloth on NVIDIA GPUs | A100-40GB | 24GB | text-generation, reasoning |  |
| Qwen3 (14B) | Fine-tune Qwen3 (14B) with Unsloth on NVIDIA GPUs | A100-40GB | 24GB | text-generation |  |
| Qwen3-VL (8B) | Fine-tune Qwen3-VL (8B) with Unsloth on NVIDIA GPUs | A100-40GB | 24GB | vision, multimodal |  |
| Advanced Llama3 1 (3B) Grpo Lora | Fine-tune Advanced Llama3 1 (3B) Grpo Lora with Unsloth on NVIDIA GPUs | L4 | 16GB | General |  |
| Advanced Llama3 2 (3B) Grpo Lora | Fine-tune Advanced Llama3 2 (3B) Grpo Lora with Unsloth on NVIDIA GPUs | L4 | 16GB | General |  |
| Bert Classification | Fine-tune Bert Classification with Unsloth on NVIDIA GPUs | L4 | 16GB | General |  |
| Codeforces Cot Finetune For Reasoning On Codeforces | Fine-tune Codeforces Cot Finetune For Reasoning On Codeforces with Unsloth on NVIDIA GPUs | L4 | 16GB | General |  |
| Codegemma (7B) Conversational | Fine-tune Codegemma (7B) Conversational with Unsloth on NVIDIA GPUs | L4 | 16GB | General |  |
| Deepseek R1 0528 Qwen3 (8B) Grpo | Fine-tune Deepseek R1 0528 Qwen3 (8B) Grpo with Unsloth on NVIDIA GPUs | L4 | 16GB | General |  |
| Falcon H1 (0 | Fine-tune Falcon H1 (0 with Unsloth on NVIDIA GPUs | L4 | 16GB | General |  |
| Falcon H1 Alpaca | Fine-tune Falcon H1 Alpaca with Unsloth on NVIDIA GPUs | L4 | 16GB | General |  |
| Gemma2 (2B) Alpaca | Fine-tune Gemma2 (2B) Alpaca with Unsloth on NVIDIA GPUs | L4 | 16GB | General |  |
| Gemma2 (9B) Alpaca | Fine-tune Gemma2 (9B) Alpaca with Unsloth on NVIDIA GPUs | L4 | 16GB | General |  |
| Gemma3 (1B) Grpo | Fine-tune Gemma3 (1B) Grpo with Unsloth on NVIDIA GPUs | L4 | 16GB | General |  |
| Gemma3 (270M) | Fine-tune Gemma3 (270M) with Unsloth on NVIDIA GPUs | L4 | 16GB | General |  |
| Gemma3 (27B) A100 Conversational | Fine-tune Gemma3 (27B) A100 Conversational with Unsloth on NVIDIA GPUs | L4 | 16GB | General |  |
| Gemma3 (4B) | Fine-tune Gemma3 (4B) with Unsloth on NVIDIA GPUs | L4 | 16GB | General |  |
| Gemma3 (4B) Vision Grpo | Fine-tune Gemma3 (4B) Vision Grpo with Unsloth on NVIDIA GPUs | L4 | 16GB | General |  |
| Gemma3N (2B) Inference | Fine-tune Gemma3N (2B) Inference with Unsloth on NVIDIA GPUs | L4 | 16GB | General |  |
| Gemma3N (4B) Audio | Fine-tune Gemma3N (4B) Audio with Unsloth on NVIDIA GPUs | L4 | 16GB | General |  |
| Gemma3N (4B) Conversational | Fine-tune Gemma3N (4B) Conversational with Unsloth on NVIDIA GPUs | L4 | 16GB | General |  |
| Gemma3N (4B) Vision | Fine-tune Gemma3N (4B) Vision with Unsloth on NVIDIA GPUs | L4 | 16GB | General |  |
| Gpt Oss Bnb (20B) Inference | Fine-tune Gpt Oss Bnb (20B) Inference with Unsloth on NVIDIA GPUs | L4 | 16GB | General |  |
| Gpt Oss Mxfp4 (20B) Inference | Fine-tune Gpt Oss Mxfp4 (20B) Inference with Unsloth on NVIDIA GPUs | L4 | 16GB | General |  |
| Granite4 | Fine-tune Granite4 with Unsloth on NVIDIA GPUs | L4 | 16GB | General |  |
| Huggingface Course Advanced Llama3 1 (3B) Grpo Lora | Fine-tune Huggingface Course Advanced Llama3 1 (3B) Grpo Lora with Unsloth on NVIDIA GPUs | L4 | 16GB | General |  |
| Huggingface Course Advanced Llama3 2 (3B) Grpo Lora | Fine-tune Huggingface Course Advanced Llama3 2 (3B) Grpo Lora with Unsloth on NVIDIA GPUs | L4 | 16GB | General |  |
| Huggingface Course Deepseek R1 0528 Qwen3 (8B) Grpo | Fine-tune Huggingface Course Deepseek R1 0528 Qwen3 (8B) Grpo with Unsloth on NVIDIA GPUs | L4 | 16GB | General |  |
| Huggingface Course Gemma3 (1B) Grpo | Fine-tune Huggingface Course Gemma3 (1B) Grpo with Unsloth on NVIDIA GPUs | L4 | 16GB | General |  |
| Huggingface Course Gemma3 (4B) Vision Grpo | Fine-tune Huggingface Course Gemma3 (4B) Vision Grpo with Unsloth on NVIDIA GPUs | L4 | 16GB | General |  |
| Huggingface Course Llama3 | Fine-tune Huggingface Course Llama3 with Unsloth on NVIDIA GPUs | L4 | 16GB | General |  |
| Huggingface Course Mistral V0 | Fine-tune Huggingface Course Mistral V0 with Unsloth on NVIDIA GPUs | L4 | 16GB | General |  |
| Huggingface Course Qwen2 | Fine-tune Huggingface Course Qwen2 with Unsloth on NVIDIA GPUs | L4 | 16GB | General |  |
| Huggingface Course Qwen2 5 7B Vl Grpo | Fine-tune Huggingface Course Qwen2 5 7B Vl Grpo with Unsloth on NVIDIA GPUs | L4 | 16GB | General |  |
| Huggingface Course Qwen3 (4B) Grpo | Fine-tune Huggingface Course Qwen3 (4B) Grpo with Unsloth on NVIDIA GPUs | L4 | 16GB | General |  |
| Kaggle Advanced Llama3 1 (3B) Grpo Lora | Fine-tune Kaggle Advanced Llama3 1 (3B) Grpo Lora with Unsloth on NVIDIA GPUs | L4 | 16GB | General |  |
| Kaggle Advanced Llama3 2 (3B) Grpo Lora | Fine-tune Kaggle Advanced Llama3 2 (3B) Grpo Lora with Unsloth on NVIDIA GPUs | L4 | 16GB | General |  |
| Kaggle Bert Classification | Fine-tune Kaggle Bert Classification with Unsloth on NVIDIA GPUs | L4 | 16GB | General |  |
| Kaggle Codeforces Cot Finetune For Reasoning On Codeforces | Fine-tune Kaggle Codeforces Cot Finetune For Reasoning On Codeforces with Unsloth on NVIDIA GPUs | L4 | 16GB | General |  |
| Kaggle Codegemma (7B) Conversational | Fine-tune Kaggle Codegemma (7B) Conversational with Unsloth on NVIDIA GPUs | L4 | 16GB | General |  |
| Kaggle Deepseek R1 0528 Qwen3 (8B) Grpo | Fine-tune Kaggle Deepseek R1 0528 Qwen3 (8B) Grpo with Unsloth on NVIDIA GPUs | L4 | 16GB | General |  |
| Kaggle Falcon H1 (0 | Fine-tune Kaggle Falcon H1 (0 with Unsloth on NVIDIA GPUs | L4 | 16GB | General |  |
| Kaggle Gemma2 (2B) Alpaca | Fine-tune Kaggle Gemma2 (2B) Alpaca with Unsloth on NVIDIA GPUs | L4 | 16GB | General |  |
| Kaggle Gemma2 (9B) Alpaca | Fine-tune Kaggle Gemma2 (9B) Alpaca with Unsloth on NVIDIA GPUs | L4 | 16GB | General |  |
| Kaggle Gemma3 (1B) Grpo | Fine-tune Kaggle Gemma3 (1B) Grpo with Unsloth on NVIDIA GPUs | L4 | 16GB | General |  |
| Kaggle Gemma3 (270M) | Fine-tune Kaggle Gemma3 (270M) with Unsloth on NVIDIA GPUs | L4 | 16GB | General |  |
| Kaggle Gemma3 (27B) A100 Conversational | Fine-tune Kaggle Gemma3 (27B) A100 Conversational with Unsloth on NVIDIA GPUs | L4 | 16GB | General |  |
| Kaggle Gemma3 (4B) | Fine-tune Kaggle Gemma3 (4B) with Unsloth on NVIDIA GPUs | L4 | 16GB | General |  |
| Kaggle Gemma3 (4B) Vision Grpo | Fine-tune Kaggle Gemma3 (4B) Vision Grpo with Unsloth on NVIDIA GPUs | L4 | 16GB | General |  |
| Kaggle Gemma3N (2B) Inference | Fine-tune Kaggle Gemma3N (2B) Inference with Unsloth on NVIDIA GPUs | L4 | 16GB | General |  |
| Kaggle Gemma3N (4B) Audio | Fine-tune Kaggle Gemma3N (4B) Audio with Unsloth on NVIDIA GPUs | L4 | 16GB | General |  |
| Kaggle Gemma3N (4B) Conversational | Fine-tune Kaggle Gemma3N (4B) Conversational with Unsloth on NVIDIA GPUs | L4 | 16GB | General |  |
| Kaggle Gemma3N (4B) Vision | Fine-tune Kaggle Gemma3N (4B) Vision with Unsloth on NVIDIA GPUs | L4 | 16GB | General |  |
| Kaggle Gpt Oss Bnb (20B) Inference | Fine-tune Kaggle Gpt Oss Bnb (20B) Inference with Unsloth on NVIDIA GPUs | L4 | 16GB | General |  |
| Kaggle Gpt Oss Mxfp4 (20B) Inference | Fine-tune Kaggle Gpt Oss Mxfp4 (20B) Inference with Unsloth on NVIDIA GPUs | L4 | 16GB | General |  |
| Kaggle Granite4 | Fine-tune Kaggle Granite4 with Unsloth on NVIDIA GPUs | L4 | 16GB | General |  |
| Kaggle Liquid Lfm2 (1 | Fine-tune Kaggle Liquid Lfm2 (1 with Unsloth on NVIDIA GPUs | L4 | 16GB | General |  |
| Kaggle Llama3 | Fine-tune Kaggle Llama3 with Unsloth on NVIDIA GPUs | L4 | 16GB | General |  |
| Kaggle Llama3 (8B) Conversational | Fine-tune Kaggle Llama3 (8B) Conversational with Unsloth on NVIDIA GPUs | L4 | 16GB | General |  |
| Kaggle Llama3 (8B) Ollama | Fine-tune Kaggle Llama3 (8B) Ollama with Unsloth on NVIDIA GPUs | L4 | 16GB | General |  |
| Kaggle Llama3 (8B) Orpo | Fine-tune Kaggle Llama3 (8B) Orpo with Unsloth on NVIDIA GPUs | L4 | 16GB | General |  |
| Kaggle Llasa Tts (1B) | Fine-tune Kaggle Llasa Tts (1B) with Unsloth on NVIDIA GPUs | L4 | 16GB | General |  |
| Kaggle Llasa Tts (3B) | Fine-tune Kaggle Llasa Tts (3B) with Unsloth on NVIDIA GPUs | L4 | 16GB | General |  |
| Kaggle Magistral (24B) Reasoning Conversational | Fine-tune Kaggle Magistral (24B) Reasoning Conversational with Unsloth on NVIDIA GPUs | L4 | 16GB | General |  |
| Kaggle Meta Synthetic Data Llama3 | Fine-tune Kaggle Meta Synthetic Data Llama3 with Unsloth on NVIDIA GPUs | L4 | 16GB | General |  |
| Kaggle Meta Synthetic Data Llama3 2 (3B) | Fine-tune Kaggle Meta Synthetic Data Llama3 2 (3B) with Unsloth on NVIDIA GPUs | L4 | 16GB | General |  |
| Kaggle Mistral (7B) Text Completion | Fine-tune Kaggle Mistral (7B) Text Completion with Unsloth on NVIDIA GPUs | L4 | 16GB | General |  |
| Kaggle Mistral Nemo (12B) Alpaca | Fine-tune Kaggle Mistral Nemo (12B) Alpaca with Unsloth on NVIDIA GPUs | L4 | 16GB | General |  |
| Kaggle Mistral Small (22B) Alpaca | Fine-tune Kaggle Mistral Small (22B) Alpaca with Unsloth on NVIDIA GPUs | L4 | 16GB | General |  |
| Kaggle Mistral V0 | Fine-tune Kaggle Mistral V0 with Unsloth on NVIDIA GPUs | L4 | 16GB | General |  |
| Kaggle Orpheus (3B) Tts | Fine-tune Kaggle Orpheus (3B) Tts with Unsloth on NVIDIA GPUs | L4 | 16GB | General |  |
| Kaggle Oute Tts (1B) | Fine-tune Kaggle Oute Tts (1B) with Unsloth on NVIDIA GPUs | L4 | 16GB | General |  |
| Kaggle Phi 3 | Fine-tune Kaggle Phi 3 with Unsloth on NVIDIA GPUs | L4 | 16GB | General |  |
| Kaggle Phi 3 Medium Conversational | Fine-tune Kaggle Phi 3 Medium Conversational with Unsloth on NVIDIA GPUs | L4 | 16GB | General |  |
| Kaggle Phi 4 Conversational | Fine-tune Kaggle Phi 4 Conversational with Unsloth on NVIDIA GPUs | L4 | 16GB | General |  |
| Kaggle Pixtral (12B) Vision | Fine-tune Kaggle Pixtral (12B) Vision with Unsloth on NVIDIA GPUs | L4 | 16GB | General |  |
| Kaggle Qwen2 | Fine-tune Kaggle Qwen2 with Unsloth on NVIDIA GPUs | L4 | 16GB | General |  |
| Kaggle Qwen2 (7B) Alpaca | Fine-tune Kaggle Qwen2 (7B) Alpaca with Unsloth on NVIDIA GPUs | L4 | 16GB | General |  |
| Kaggle Qwen2 5 7B Vl Grpo | Fine-tune Kaggle Qwen2 5 7B Vl Grpo with Unsloth on NVIDIA GPUs | L4 | 16GB | General |  |
| Kaggle Qwen2 Vl (7B) Vision | Fine-tune Kaggle Qwen2 Vl (7B) Vision with Unsloth on NVIDIA GPUs | L4 | 16GB | General |  |
| Kaggle Qwen2.5 Coder (1 | Fine-tune Kaggle Qwen2.5 Coder (1 with Unsloth on NVIDIA GPUs | L4 | 16GB | General |  |
| Kaggle Qwen3 (32B) A100 Reasoning Conversational | Fine-tune Kaggle Qwen3 (32B) A100 Reasoning Conversational with Unsloth on NVIDIA GPUs | L4 | 16GB | General |  |
| Kaggle Qwen3 (4B) Grpo | Fine-tune Kaggle Qwen3 (4B) Grpo with Unsloth on NVIDIA GPUs | L4 | 16GB | General |  |
| Kaggle Qwen3 (4B) Instruct | Fine-tune Kaggle Qwen3 (4B) Instruct with Unsloth on NVIDIA GPUs | L4 | 16GB | General |  |
| Kaggle Qwen3 (4B) Thinking | Fine-tune Kaggle Qwen3 (4B) Thinking with Unsloth on NVIDIA GPUs | L4 | 16GB | General |  |
| Kaggle Spark Tts (0 5B) | Fine-tune Kaggle Spark Tts (0 5B) with Unsloth on NVIDIA GPUs | L4 | 16GB | General |  |
| Kaggle Tinyllama (1 | Fine-tune Kaggle Tinyllama (1 with Unsloth on NVIDIA GPUs | L4 | 16GB | General |  |
| Kaggle Unsloth Studio | Fine-tune Kaggle Unsloth Studio with Unsloth on NVIDIA GPUs | L4 | 16GB | General |  |
| Kaggle Whisper | Fine-tune Kaggle Whisper with Unsloth on NVIDIA GPUs | L4 | 16GB | General |  |
| Kaggle Zephyr (7B) Dpo | Fine-tune Kaggle Zephyr (7B) Dpo with Unsloth on NVIDIA GPUs | L4 | 16GB | General |  |
| Liquid Lfm2 (1 | Fine-tune Liquid Lfm2 (1 with Unsloth on NVIDIA GPUs | L4 | 16GB | General |  |
| Liquid Lfm2 Conversational | Fine-tune Liquid Lfm2 Conversational with Unsloth on NVIDIA GPUs | L4 | 16GB | General |  |
| Llama3 | Fine-tune Llama3 with Unsloth on NVIDIA GPUs | L4 | 16GB | General |  |
| Llama3 (8B) Conversational | Fine-tune Llama3 (8B) Conversational with Unsloth on NVIDIA GPUs | L4 | 16GB | General |  |
| Llama3 (8B) Ollama | Fine-tune Llama3 (8B) Ollama with Unsloth on NVIDIA GPUs | L4 | 16GB | General |  |
| Llama3 (8B) Orpo | Fine-tune Llama3 (8B) Orpo with Unsloth on NVIDIA GPUs | L4 | 16GB | General |  |
| Llasa Tts (1B) | Fine-tune Llasa Tts (1B) with Unsloth on NVIDIA GPUs | L4 | 16GB | General |  |
| Llasa Tts (3B) | Fine-tune Llasa Tts (3B) with Unsloth on NVIDIA GPUs | L4 | 16GB | General |  |
| Magistral (24B) Reasoning Conversational | Fine-tune Magistral (24B) Reasoning Conversational with Unsloth on NVIDIA GPUs | L4 | 16GB | General |  |
| Meta Synthetic Data Llama3 | Fine-tune Meta Synthetic Data Llama3 with Unsloth on NVIDIA GPUs | L4 | 16GB | General |  |
| Meta Synthetic Data Llama3 2 (3B) | Fine-tune Meta Synthetic Data Llama3 2 (3B) with Unsloth on NVIDIA GPUs | L4 | 16GB | General |  |
| Mistral (7B) Text Completion | Fine-tune Mistral (7B) Text Completion with Unsloth on NVIDIA GPUs | L4 | 16GB | General |  |
| Mistral Nemo (12B) Alpaca | Fine-tune Mistral Nemo (12B) Alpaca with Unsloth on NVIDIA GPUs | L4 | 16GB | General |  |
| Mistral Small (22B) Alpaca | Fine-tune Mistral Small (22B) Alpaca with Unsloth on NVIDIA GPUs | L4 | 16GB | General |  |
| Mistral V0 | Fine-tune Mistral V0 with Unsloth on NVIDIA GPUs | L4 | 16GB | General |  |
| Orpheus (3B) Tts | Fine-tune Orpheus (3B) Tts with Unsloth on NVIDIA GPUs | L4 | 16GB | General |  |
| Oute Tts (1B) | Fine-tune Oute Tts (1B) with Unsloth on NVIDIA GPUs | L4 | 16GB | General |  |
| Phi 3 | Fine-tune Phi 3 with Unsloth on NVIDIA GPUs | L4 | 16GB | General |  |
| Phi 3 Medium Conversational | Fine-tune Phi 3 Medium Conversational with Unsloth on NVIDIA GPUs | L4 | 16GB | General |  |
| Pixtral (12B) Vision | Fine-tune Pixtral (12B) Vision with Unsloth on NVIDIA GPUs | L4 | 16GB | General |  |
| Qwen2 | Fine-tune Qwen2 with Unsloth on NVIDIA GPUs | L4 | 16GB | General |  |
| Qwen2 (7B) Alpaca | Fine-tune Qwen2 (7B) Alpaca with Unsloth on NVIDIA GPUs | L4 | 16GB | General |  |
| Qwen2 5 7B Vl Grpo | Fine-tune Qwen2 5 7B Vl Grpo with Unsloth on NVIDIA GPUs | L4 | 16GB | General |  |
| Qwen2 Vl (7B) Vision | Fine-tune Qwen2 Vl (7B) Vision with Unsloth on NVIDIA GPUs | L4 | 16GB | General |  |
| Qwen2.5 Coder (1 | Fine-tune Qwen2.5 Coder (1 with Unsloth on NVIDIA GPUs | L4 | 16GB | General |  |
| Qwen3 (32B) A100 Reasoning Conversational | Fine-tune Qwen3 (32B) A100 Reasoning Conversational with Unsloth on NVIDIA GPUs | L4 | 16GB | General |  |
| Qwen3 (4B) Instruct | Fine-tune Qwen3 (4B) Instruct with Unsloth on NVIDIA GPUs | L4 | 16GB | General |  |
| Qwen3 (4B) Thinking | Fine-tune Qwen3 (4B) Thinking with Unsloth on NVIDIA GPUs | L4 | 16GB | General |  |
| Spark Tts (0 5B) | Fine-tune Spark Tts (0 5B) with Unsloth on NVIDIA GPUs | L4 | 16GB | General |  |
| Synthetic Data Hackathon | Fine-tune Synthetic Data Hackathon with Unsloth on NVIDIA GPUs | L4 | 16GB | General |  |
| Tinyllama (1 | Fine-tune Tinyllama (1 with Unsloth on NVIDIA GPUs | L4 | 16GB | General |  |
| Unsloth Studio | Fine-tune Unsloth Studio with Unsloth on NVIDIA GPUs | L4 | 16GB | General |  |
| Zephyr (7B) Dpo | Fine-tune Zephyr (7B) Dpo with Unsloth on NVIDIA GPUs | L4 | 16GB | General |  |
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
- Original notebook file (`.ipynb`) - Main training notebook
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

**Important**: Use a virtual environment to avoid system package conflicts (especially on macOS).

```bash
# Clone the repository
git clone git@github.com:brevdev/unsloth-notebook-adaptor.git
cd unsloth-notebook-adaptor

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

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

