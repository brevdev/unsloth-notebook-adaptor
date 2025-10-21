# 🚀 Unsloth to NVIDIA Brev Adapter

[![Sync Notebooks](https://github.com/brevdev/unsloth-notebook-adaptor/workflows/Sync%20and%20Convert%20Notebooks/badge.svg)](https://github.com/brevdev/unsloth-notebook-adaptor/actions/workflows/sync-and-convert.yml)
[![Test Conversions](https://github.com/brevdev/unsloth-notebook-adaptor/workflows/Test%20Conversions/badge.svg)](https://github.com/brevdev/unsloth-notebook-adaptor/actions/workflows/test-conversions.yml)
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

## 📒 Available Launchables

Below are **181 Unsloth notebooks** organized into **129 launchables** for NVIDIA Brev, categorized by model type. Each notebook is fully adapted for Brev environments with GPU-optimized configurations, companion files, and ready-to-run setups.

**Quick Start:** Browse the notebooks below, clone this repo, and deploy on [Brev Console](https://brev.nvidia.com) or run locally with Docker. View the [original Unsloth notebooks here](https://github.com/unslothai/notebooks).

<!-- LAUNCHABLES_TABLE_START -->

### Main Notebooks

| Model | Type | GPU Requirements | Notebook Link |
|-------|------|------------------|---------------|
| **Liquid_LFM2-Conversational** | Conversational | L4<br/>(16GB VRAM) | [Open in Brev](converted/liquid-lfm2/Liquid_LFM2-Conversational.ipynb) |
| **Liquid_LFM2_(1.2B)-Conversational** | Conversational | L4<br/>(16GB VRAM) | [Open in Brev](converted/liquid-lfm2-1/Liquid_LFM2_%281.2B%29-Conversational.ipynb) |
| **Magistral_(24B)-Reasoning-Conversational** | Conversational | L4<br/>(16GB VRAM) | [Open in Brev](converted/magistral-24b-reasoning/Magistral_%2824B%29-Reasoning-Conversational.ipynb) |

### GPT-OSS Notebooks

| Model | Type | GPU Requirements | Notebook Link |
|-------|------|------------------|---------------|
| **GPT_OSS_BNB_(20B)-Inference** | Inference | L4<br/>(16GB VRAM) | [Open in Brev](converted/gpt-oss-bnb-20b/GPT_OSS_BNB_%2820B%29-Inference.ipynb) |
| **GPT_OSS_MXFP4_(20B)-Inference** | Inference | L4<br/>(16GB VRAM) | [Open in Brev](converted/gpt-oss-mxfp4-20b/GPT_OSS_MXFP4_%2820B%29-Inference.ipynb) |
| **gpt-oss-(120B)_A100-Fine-tuning** | Fine-tuning | A100-80GB<br/>(80GB VRAM) | [Open in Brev](converted/gpt-oss-120b-fine-tuning/gpt-oss-%28120B%29_A100-Fine-tuning.ipynb) |
| **gpt-oss-(20B)-Fine-tuning** | Fine-tuning | A100-40GB<br/>(24GB VRAM) | [Open in Brev](converted/gpt-oss-20b-fine-tuning/gpt-oss-%2820B%29-Fine-tuning.ipynb) |
| **gpt-oss-(20B)-GRPO** | GRPO | A100-40GB<br/>(24GB VRAM) | [Open in Brev](converted/gpt-oss-20b-fine-tuning/HuggingFace%20Course-gpt-oss-%2820B%29-GRPO.ipynb) |
| **gpt-oss-(20B)-GRPO** | GRPO | A100-40GB<br/>(24GB VRAM) | [Open in Brev](converted/gpt-oss-20b-fine-tuning/gpt-oss-%2820B%29-GRPO.ipynb) |
| **gpt-oss-(20B)_A100-GRPO** | GRPO | A100-40GB<br/>(24GB VRAM) | [Open in Brev](converted/gpt-oss-20b-fine-tuning/HuggingFace%20Course-gpt-oss-%2820B%29_A100-GRPO.ipynb) |
| **gpt-oss-(20B)_A100-GRPO** | GRPO | A100-40GB<br/>(24GB VRAM) | [Open in Brev](converted/gpt-oss-20b-fine-tuning/gpt-oss-%2820B%29_A100-GRPO.ipynb) |
| **gpt_oss_(20B)_GRPO_BF16** | GRPO | A100-80GB<br/>(40GB VRAM) | [Open in Brev](converted/gpt-oss-20b-grpo-rl/gpt_oss_%2820B%29_GRPO_BF16.ipynb) |
| **gpt_oss_(20B)_Reinforcement_Learning_2048_Game** | Fine-tuning | A100-40GB<br/>(24GB VRAM) | [Open in Brev](converted/gpt-oss-20b-fine-tuning/gpt_oss_%2820B%29_Reinforcement_Learning_2048_Game.ipynb) |
| **gpt_oss_(20B)_Reinforcement_Learning_2048_Game_BF16** | Fine-tuning | A100-40GB<br/>(24GB VRAM) | [Open in Brev](converted/gpt-oss-20b-fine-tuning/gpt_oss_%2820B%29_Reinforcement_Learning_2048_Game_BF16.ipynb) |
| **gpt_oss_(20B)_Reinforcement_Learning_2048_Game_DGX_Spark** | Fine-tuning | A100-40GB<br/>(24GB VRAM) | [Open in Brev](converted/gpt-oss-20b-fine-tuning/gpt_oss_%2820B%29_Reinforcement_Learning_2048_Game_DGX_Spark.ipynb) |

### Llama Notebooks

| Model | Type | GPU Requirements | Notebook Link |
|-------|------|------------------|---------------|
| **Advanced_Llama3_1_(3B)_GRPO_LoRA** | GRPO | L4<br/>(16GB VRAM) | [Open in Brev](converted/huggingface%20course-advanced-llama3-1-3b-grpo-lora/HuggingFace%20Course-Advanced_Llama3_1_%283B%29_GRPO_LoRA.ipynb) |
| **Advanced_Llama3_1_(3B)_GRPO_LoRA** | GRPO | L4<br/>(16GB VRAM) | [Open in Brev](converted/advanced-llama3-1-3b-grpo-lora/Advanced_Llama3_1_%283B%29_GRPO_LoRA.ipynb) |
| **Advanced_Llama3_2_(3B)_GRPO_LoRA** | GRPO | L4<br/>(16GB VRAM) | [Open in Brev](converted/advanced-llama3-2-3b-grpo-lora/Advanced_Llama3_2_%283B%29_GRPO_LoRA.ipynb) |
| **Advanced_Llama3_2_(3B)_GRPO_LoRA** | GRPO | L4<br/>(16GB VRAM) | [Open in Brev](converted/huggingface%20course-advanced-llama3-2-3b-grpo-lora/HuggingFace%20Course-Advanced_Llama3_2_%283B%29_GRPO_LoRA.ipynb) |
| **Llama3.1_(8B)-Alpaca** | Alpaca | L4<br/>(16GB VRAM) | [Open in Brev](converted/llama3/Llama3.1_%288B%29-Alpaca.ipynb) |
| **Llama3.1_(8B)-GRPO** | GRPO | L4<br/>(16GB VRAM) | [Open in Brev](converted/llama3/Llama3.1_%288B%29-GRPO.ipynb) |
| **Llama3.1_(8B)-GRPO** | GRPO | L4<br/>(16GB VRAM) | [Open in Brev](converted/huggingface%20course-llama3/HuggingFace%20Course-Llama3.1_%288B%29-GRPO.ipynb) |
| **Llama3.1_(8B)-Inference** | Inference | L4<br/>(16GB VRAM) | [Open in Brev](converted/llama3/Llama3.1_%288B%29-Inference.ipynb) |
| **Llama3.2_(1B)-RAFT** | RAFT | L4<br/>(16GB VRAM) | [Open in Brev](converted/llama3/Llama3.2_%281B%29-RAFT.ipynb) |
| **Llama3.2_(1B_and_3B)-Conversational** | Conversational | L4<br/>(16GB VRAM) | [Open in Brev](converted/llama3/Llama3.2_%281B_and_3B%29-Conversational.ipynb) |
| **Llama3.3_(70B)_A100-Conversational** | Conversational | L4<br/>(16GB VRAM) | [Open in Brev](converted/llama3/Llama3.3_%2870B%29_A100-Conversational.ipynb) |
| **Llama3_(8B)-Alpaca** | Alpaca | L4<br/>(16GB VRAM) | [Open in Brev](converted/llama3-8b/Llama3_%288B%29-Alpaca.ipynb) |
| **Llama3_(8B)-Conversational** | Conversational | L4<br/>(16GB VRAM) | [Open in Brev](converted/llama3-8b/Llama3_%288B%29-Conversational.ipynb) |
| **Llama3_(8B)-ORPO** | ORPO | L4<br/>(16GB VRAM) | [Open in Brev](converted/llama3-8b-orpo/Llama3_%288B%29-ORPO.ipynb) |
| **Llama3_(8B)-Ollama** | Ollama | L4<br/>(16GB VRAM) | [Open in Brev](converted/llama3-8b-ollama/Llama3_%288B%29-Ollama.ipynb) |
| **Meta-Synthetic-Data-Llama3.1_(8B)** | Synthetic Data | L4<br/>(16GB VRAM) | [Open in Brev](converted/meta-synthetic-data-llama3/Meta-Synthetic-Data-Llama3.1_%288B%29.ipynb) |
| **Meta_Synthetic_Data_Llama3_2_(3B)** | Synthetic Data | L4<br/>(16GB VRAM) | [Open in Brev](converted/meta-synthetic-data-llama3-2-3b/Meta_Synthetic_Data_Llama3_2_%283B%29.ipynb) |
| **TinyLlama_(1.1B)-Alpaca** | Alpaca | L4<br/>(16GB VRAM) | [Open in Brev](converted/tinyllama-1/TinyLlama_%281.1B%29-Alpaca.ipynb) |

### Gemma Notebooks

| Model | Type | GPU Requirements | Notebook Link |
|-------|------|------------------|---------------|
| **CodeGemma_(7B)-Conversational** | Conversational | L4<br/>(16GB VRAM) | [Open in Brev](converted/codegemma-7b/CodeGemma_%287B%29-Conversational.ipynb) |
| **Gemma2_(2B)-Alpaca** | Alpaca | L4<br/>(16GB VRAM) | [Open in Brev](converted/gemma2-2b/Gemma2_%282B%29-Alpaca.ipynb) |
| **Gemma2_(9B)-Alpaca** | Alpaca | L4<br/>(16GB VRAM) | [Open in Brev](converted/gemma2-9b/Gemma2_%289B%29-Alpaca.ipynb) |
| **Gemma3N_(2B)-Inference** | Inference | L4<br/>(16GB VRAM) | [Open in Brev](converted/gemma3n-2b/Gemma3N_%282B%29-Inference.ipynb) |
| **Gemma3N_(4B)-Conversational** | Conversational | L4<br/>(16GB VRAM) | [Open in Brev](converted/gemma3n-4b/Gemma3N_%284B%29-Conversational.ipynb) |
| **Gemma3_(1B)-GRPO** | GRPO | L4<br/>(16GB VRAM) | [Open in Brev](converted/gemma3-1b/Gemma3_%281B%29-GRPO.ipynb) |
| **Gemma3_(1B)-GRPO** | GRPO | L4<br/>(16GB VRAM) | [Open in Brev](converted/huggingface%20course-gemma3-1b/HuggingFace%20Course-Gemma3_%281B%29-GRPO.ipynb) |
| **Gemma3_(270M)** | Fine-tuning | L4<br/>(16GB VRAM) | [Open in Brev](converted/gemma3-270m/Gemma3_%28270M%29.ipynb) |
| **Gemma3_(27B)_A100-Conversational** | Conversational | L4<br/>(16GB VRAM) | [Open in Brev](converted/gemma3-27b/Gemma3_%2827B%29_A100-Conversational.ipynb) |
| **Gemma3_(4B)** | Fine-tuning | L4<br/>(16GB VRAM) | [Open in Brev](converted/gemma3-4b/Gemma3_%284B%29.ipynb) |

### Qwen Notebooks

| Model | Type | GPU Requirements | Notebook Link |
|-------|------|------------------|---------------|
| **DeepSeek_R1_0528_Qwen3_(8B)_GRPO** | GRPO | L4<br/>(16GB VRAM) | [Open in Brev](converted/deepseek-r1-0528-qwen3-8b/DeepSeek_R1_0528_Qwen3_%288B%29_GRPO.ipynb) |
| **DeepSeek_R1_0528_Qwen3_(8B)_GRPO** | GRPO | L4<br/>(16GB VRAM) | [Open in Brev](converted/huggingface%20course-deepseek-r1-0528-qwen3-8b/HuggingFace%20Course-DeepSeek_R1_0528_Qwen3_%288B%29_GRPO.ipynb) |
| **Qwen2.5_(3B)-GRPO** | GRPO | L4<br/>(16GB VRAM) | [Open in Brev](converted/qwen2/Qwen2.5_%283B%29-GRPO.ipynb) |
| **Qwen2.5_(3B)-GRPO** | GRPO | L4<br/>(16GB VRAM) | [Open in Brev](converted/huggingface%20course-qwen2/HuggingFace%20Course-Qwen2.5_%283B%29-GRPO.ipynb) |
| **Qwen2.5_(7B)-Alpaca** | Alpaca | L4<br/>(16GB VRAM) | [Open in Brev](converted/qwen2/Qwen2.5_%287B%29-Alpaca.ipynb) |
| **Qwen2.5_Coder_(1.5B)-Tool_Calling** | Tool Calling | L4<br/>(16GB VRAM) | [Open in Brev](converted/qwen2.5-coder-1/Qwen2.5_Coder_%281.5B%29-Tool_Calling.ipynb) |
| **Qwen2.5_Coder_(14B)-Conversational** | Conversational | L4<br/>(16GB VRAM) | [Open in Brev](converted/qwen2/Qwen2.5_Coder_%2814B%29-Conversational.ipynb) |
| **Qwen2_(7B)-Alpaca** | Alpaca | L4<br/>(16GB VRAM) | [Open in Brev](converted/qwen2-7b/Qwen2_%287B%29-Alpaca.ipynb) |
| **Qwen3_(14B)** | Fine-tuning | A100-40GB<br/>(24GB VRAM) | [Open in Brev](converted/qwen3-14b-fine-tuning/Qwen3_%2814B%29.ipynb) |
| **Qwen3_(14B)-Alpaca** | Alpaca | A100-40GB<br/>(24GB VRAM) | [Open in Brev](converted/qwen3-14b-fine-tuning/Qwen3_%2814B%29-Alpaca.ipynb) |
| **Qwen3_(14B)-Reasoning-Conversational** | Conversational | A100-40GB<br/>(24GB VRAM) | [Open in Brev](converted/qwen3-14b-fine-tuning/Qwen3_%2814B%29-Reasoning-Conversational.ipynb) |
| **Qwen3_(32B)_A100-Reasoning-Conversational** | Conversational | L4<br/>(16GB VRAM) | [Open in Brev](converted/qwen3-32b-a100-reasoning/Qwen3_%2832B%29_A100-Reasoning-Conversational.ipynb) |
| **Qwen3_(4B)-GRPO** | GRPO | L4<br/>(16GB VRAM) | [Open in Brev](converted/huggingface%20course-qwen3-4b/HuggingFace%20Course-Qwen3_%284B%29-GRPO.ipynb) |
| **Qwen3_(4B)-GRPO** | GRPO | L4<br/>(16GB VRAM) | [Open in Brev](converted/qwen3-4b-grpo-rl/Qwen3_%284B%29-GRPO.ipynb) |
| **Qwen3_(4B)-Instruct** | Instruct | L4<br/>(16GB VRAM) | [Open in Brev](converted/qwen3-4b-instruct/Qwen3_%284B%29-Instruct.ipynb) |
| **Qwen3_(4B)-Thinking** | Thinking | L4<br/>(16GB VRAM) | [Open in Brev](converted/qwen3-4b-thinking/Qwen3_%284B%29-Thinking.ipynb) |

### Phi Notebooks

| Model | Type | GPU Requirements | Notebook Link |
|-------|------|------------------|---------------|
| **Phi_3.5_Mini-Conversational** | Conversational | L4<br/>(16GB VRAM) | [Open in Brev](converted/phi-3/Phi_3.5_Mini-Conversational.ipynb) |
| **Phi_3_Medium-Conversational** | Conversational | L4<br/>(16GB VRAM) | [Open in Brev](converted/phi-3-medium/Phi_3_Medium-Conversational.ipynb) |
| **Phi_4-Conversational** | Conversational | A100-40GB<br/>(24GB VRAM) | [Open in Brev](converted/phi-4-14b-fine-tuning/Phi_4-Conversational.ipynb) |
| **Phi_4_(14B)-GRPO** | GRPO | A100-40GB<br/>(24GB VRAM) | [Open in Brev](converted/phi-4-14b-fine-tuning/HuggingFace%20Course-Phi_4_%2814B%29-GRPO.ipynb) |
| **Phi_4_(14B)-GRPO** | GRPO | A100-40GB<br/>(24GB VRAM) | [Open in Brev](converted/phi-4-14b-fine-tuning/Phi_4_%2814B%29-GRPO.ipynb) |

### Mistral Notebooks

| Model | Type | GPU Requirements | Notebook Link |
|-------|------|------------------|---------------|
| **Mistral_(7B)-Text_Completion** | Fine-tuning | L4<br/>(16GB VRAM) | [Open in Brev](converted/mistral-7b-text-completion/Mistral_%287B%29-Text_Completion.ipynb) |
| **Mistral_Nemo_(12B)-Alpaca** | Alpaca | L4<br/>(16GB VRAM) | [Open in Brev](converted/mistral-nemo-12b/Mistral_Nemo_%2812B%29-Alpaca.ipynb) |
| **Mistral_Small_(22B)-Alpaca** | Alpaca | L4<br/>(16GB VRAM) | [Open in Brev](converted/mistral-small-22b/Mistral_Small_%2822B%29-Alpaca.ipynb) |
| **Mistral_v0.3_(7B)-Alpaca** | Alpaca | L4<br/>(16GB VRAM) | [Open in Brev](converted/mistral-v0/Mistral_v0.3_%287B%29-Alpaca.ipynb) |
| **Mistral_v0.3_(7B)-CPT** | CPT | L4<br/>(16GB VRAM) | [Open in Brev](converted/mistral-v0/Mistral_v0.3_%287B%29-CPT.ipynb) |
| **Mistral_v0.3_(7B)-Conversational** | Conversational | L4<br/>(16GB VRAM) | [Open in Brev](converted/mistral-v0/Mistral_v0.3_%287B%29-Conversational.ipynb) |
| **Mistral_v0.3_(7B)-GRPO** | GRPO | L4<br/>(16GB VRAM) | [Open in Brev](converted/huggingface%20course-mistral-v0/HuggingFace%20Course-Mistral_v0.3_%287B%29-GRPO.ipynb) |
| **Mistral_v0.3_(7B)-GRPO** | GRPO | L4<br/>(16GB VRAM) | [Open in Brev](converted/mistral-v0/Mistral_v0.3_%287B%29-GRPO.ipynb) |

### Vision Notebooks

| Model | Type | GPU Requirements | Notebook Link |
|-------|------|------------------|---------------|
| **Gemma3N_(4B)-Vision** | Vision | L4<br/>(16GB VRAM) | [Open in Brev](converted/gemma3n-4b-vision/Gemma3N_%284B%29-Vision.ipynb) |
| **Gemma3_(4B)-Vision** | Vision | L4<br/>(16GB VRAM) | [Open in Brev](converted/gemma3-4b-vision/Gemma3_%284B%29-Vision.ipynb) |
| **Gemma3_(4B)-Vision-GRPO** | Vision | L4<br/>(16GB VRAM) | [Open in Brev](converted/gemma3-4b-vision/Gemma3_%284B%29-Vision-GRPO.ipynb) |
| **Gemma3_(4B)-Vision-GRPO** | Vision | L4<br/>(16GB VRAM) | [Open in Brev](converted/huggingface%20course-gemma3-4b-vision/HuggingFace%20Course-Gemma3_%284B%29-Vision-GRPO.ipynb) |
| **Llama3.2_(11B)-Vision** | Vision | L4<br/>(16GB VRAM) | [Open in Brev](converted/llama3/Llama3.2_%2811B%29-Vision.ipynb) |
| **Pixtral_(12B)-Vision** | Vision | L4<br/>(16GB VRAM) | [Open in Brev](converted/pixtral-12b-vision/Pixtral_%2812B%29-Vision.ipynb) |
| **Qwen2.5_VL_(7B)-Vision** | Vision | L4<br/>(16GB VRAM) | [Open in Brev](converted/qwen2/Qwen2.5_VL_%287B%29-Vision.ipynb) |
| **Qwen2_5_7B_VL_GRPO** | GRPO | L4<br/>(16GB VRAM) | [Open in Brev](converted/qwen2-5-7b-vl/Qwen2_5_7B_VL_GRPO.ipynb) |
| **Qwen2_5_7B_VL_GRPO** | GRPO | L4<br/>(16GB VRAM) | [Open in Brev](converted/huggingface%20course-qwen2-5-7b-vl/HuggingFace%20Course-Qwen2_5_7B_VL_GRPO.ipynb) |
| **Qwen2_VL_(7B)-Vision** | Vision | L4<br/>(16GB VRAM) | [Open in Brev](converted/qwen2-vl-7b-vision/Qwen2_VL_%287B%29-Vision.ipynb) |
| **Qwen3_VL_(8B)-Vision** | Vision | A100-40GB<br/>(24GB VRAM) | [Open in Brev](converted/qwen3-vl-8b-vision/Qwen3_VL_%288B%29-Vision.ipynb) |
| **Qwen3_VL_(8B)-Vision-GRPO** | Vision | A100-40GB<br/>(24GB VRAM) | [Open in Brev](converted/qwen3-vl-8b-vision/HuggingFace%20Course-Qwen3_VL_%288B%29-Vision-GRPO.ipynb) |
| **Qwen3_VL_(8B)-Vision-GRPO** | Vision | A100-40GB<br/>(24GB VRAM) | [Open in Brev](converted/qwen3-vl-8b-vision/Qwen3_VL_%288B%29-Vision-GRPO.ipynb) |

### Audio Notebooks

| Model | Type | GPU Requirements | Notebook Link |
|-------|------|------------------|---------------|
| **Gemma3N_(4B)-Audio** | Fine-tuning | L4<br/>(16GB VRAM) | [Open in Brev](converted/gemma3n-4b-audio/Gemma3N_%284B%29-Audio.ipynb) |
| **Llasa_TTS_(1B)** | TTS | L4<br/>(16GB VRAM) | [Open in Brev](converted/llasa-tts-1b/Llasa_TTS_%281B%29.ipynb) |
| **Llasa_TTS_(3B)** | TTS | L4<br/>(16GB VRAM) | [Open in Brev](converted/llasa-tts-3b/Llasa_TTS_%283B%29.ipynb) |
| **Orpheus_(3B)-TTS** | TTS | L4<br/>(16GB VRAM) | [Open in Brev](converted/orpheus-3b-tts/Orpheus_%283B%29-TTS.ipynb) |
| **Oute_TTS_(1B)** | TTS | L4<br/>(16GB VRAM) | [Open in Brev](converted/oute-tts-1b/Oute_TTS_%281B%29.ipynb) |
| **Sesame_CSM_(1B)-TTS** | TTS | T4<br/>(12GB VRAM) | [Open in Brev](converted/sesame-csm-1b-tts/Sesame_CSM_%281B%29-TTS.ipynb) |
| **Spark_TTS_(0_5B)** | TTS | L4<br/>(16GB VRAM) | [Open in Brev](converted/spark-tts-0-5b/Spark_TTS_%280_5B%29.ipynb) |
| **Whisper** | STT | L4<br/>(16GB VRAM) | [Open in Brev](converted/whisper-large-v3-stt/Whisper.ipynb) |

### Kaggle Notebooks

| Model | Type | GPU Requirements | Notebook Link |
|-------|------|------------------|---------------|
| **Advanced_Llama3_1_(3B)_GRPO_LoRA** | GRPO | L4<br/>(16GB VRAM) | [Open in Brev](converted/kaggle-advanced-llama3-1-3b-grpo-lora/Kaggle-Advanced_Llama3_1_%283B%29_GRPO_LoRA.ipynb) |
| **Advanced_Llama3_2_(3B)_GRPO_LoRA** | GRPO | L4<br/>(16GB VRAM) | [Open in Brev](converted/kaggle-advanced-llama3-2-3b-grpo-lora/Kaggle-Advanced_Llama3_2_%283B%29_GRPO_LoRA.ipynb) |
| **CodeForces-cot-Finetune_for_Reasoning_on_CodeForces** | Reasoning | L4<br/>(16GB VRAM) | [Open in Brev](converted/kaggle-codeforces-cot-finetune-for-reasoning-on-codeforces/Kaggle-CodeForces-cot-Finetune_for_Reasoning_on_CodeForces.ipynb) |
| **CodeGemma_(7B)-Conversational** | Conversational | L4<br/>(16GB VRAM) | [Open in Brev](converted/kaggle-codegemma-7b/Kaggle-CodeGemma_%287B%29-Conversational.ipynb) |
| **DeepSeek_R1_0528_Qwen3_(8B)_GRPO** | GRPO | L4<br/>(16GB VRAM) | [Open in Brev](converted/kaggle-deepseek-r1-0528-qwen3-8b/Kaggle-DeepSeek_R1_0528_Qwen3_%288B%29_GRPO.ipynb) |
| **Falcon_H1_(0.5B)-Alpaca** | Alpaca | L4<br/>(16GB VRAM) | [Open in Brev](converted/kaggle-falcon-h1-0/Kaggle-Falcon_H1_%280.5B%29-Alpaca.ipynb) |
| **GPT_OSS_BNB_(20B)-Inference** | Inference | L4<br/>(16GB VRAM) | [Open in Brev](converted/kaggle-gpt-oss-bnb-20b/Kaggle-GPT_OSS_BNB_%2820B%29-Inference.ipynb) |
| **GPT_OSS_MXFP4_(20B)-Inference** | Inference | L4<br/>(16GB VRAM) | [Open in Brev](converted/kaggle-gpt-oss-mxfp4-20b/Kaggle-GPT_OSS_MXFP4_%2820B%29-Inference.ipynb) |
| **Gemma2_(2B)-Alpaca** | Alpaca | L4<br/>(16GB VRAM) | [Open in Brev](converted/kaggle-gemma2-2b/Kaggle-Gemma2_%282B%29-Alpaca.ipynb) |
| **Gemma2_(9B)-Alpaca** | Alpaca | L4<br/>(16GB VRAM) | [Open in Brev](converted/kaggle-gemma2-9b/Kaggle-Gemma2_%289B%29-Alpaca.ipynb) |
| **Gemma3N_(2B)-Inference** | Inference | L4<br/>(16GB VRAM) | [Open in Brev](converted/kaggle-gemma3n-2b/Kaggle-Gemma3N_%282B%29-Inference.ipynb) |
| **Gemma3N_(4B)-Audio** | Fine-tuning | L4<br/>(16GB VRAM) | [Open in Brev](converted/kaggle-gemma3n-4b-audio/Kaggle-Gemma3N_%284B%29-Audio.ipynb) |
| **Gemma3N_(4B)-Conversational** | Conversational | L4<br/>(16GB VRAM) | [Open in Brev](converted/kaggle-gemma3n-4b/Kaggle-Gemma3N_%284B%29-Conversational.ipynb) |
| **Gemma3N_(4B)-Vision** | Vision | L4<br/>(16GB VRAM) | [Open in Brev](converted/kaggle-gemma3n-4b-vision/Kaggle-Gemma3N_%284B%29-Vision.ipynb) |
| **Gemma3_(1B)-GRPO** | GRPO | L4<br/>(16GB VRAM) | [Open in Brev](converted/kaggle-gemma3-1b/Kaggle-Gemma3_%281B%29-GRPO.ipynb) |
| **Gemma3_(270M)** | Fine-tuning | L4<br/>(16GB VRAM) | [Open in Brev](converted/kaggle-gemma3-270m/Kaggle-Gemma3_%28270M%29.ipynb) |
| **Gemma3_(27B)_A100-Conversational** | Conversational | L4<br/>(16GB VRAM) | [Open in Brev](converted/kaggle-gemma3-27b/Kaggle-Gemma3_%2827B%29_A100-Conversational.ipynb) |
| **Gemma3_(4B)** | Fine-tuning | L4<br/>(16GB VRAM) | [Open in Brev](converted/kaggle-gemma3-4b/Kaggle-Gemma3_%284B%29.ipynb) |
| **Gemma3_(4B)-Vision** | Vision | L4<br/>(16GB VRAM) | [Open in Brev](converted/kaggle-gemma3-4b-vision/Kaggle-Gemma3_%284B%29-Vision.ipynb) |
| **Gemma3_(4B)-Vision-GRPO** | Vision | L4<br/>(16GB VRAM) | [Open in Brev](converted/kaggle-gemma3-4b-vision/Kaggle-Gemma3_%284B%29-Vision-GRPO.ipynb) |
| **Granite4.0** | Fine-tuning | L4<br/>(16GB VRAM) | [Open in Brev](converted/kaggle-granite4/Kaggle-Granite4.0.ipynb) |
| **Liquid_LFM2_(1.2B)-Conversational** | Conversational | L4<br/>(16GB VRAM) | [Open in Brev](converted/kaggle-liquid-lfm2-1/Kaggle-Liquid_LFM2_%281.2B%29-Conversational.ipynb) |
| **Llama3.1_(8B)-Alpaca** | Alpaca | L4<br/>(16GB VRAM) | [Open in Brev](converted/kaggle-llama3/Kaggle-Llama3.1_%288B%29-Alpaca.ipynb) |
| **Llama3.1_(8B)-GRPO** | GRPO | L4<br/>(16GB VRAM) | [Open in Brev](converted/kaggle-llama3/Kaggle-Llama3.1_%288B%29-GRPO.ipynb) |
| **Llama3.1_(8B)-Inference** | Inference | L4<br/>(16GB VRAM) | [Open in Brev](converted/kaggle-llama3/Kaggle-Llama3.1_%288B%29-Inference.ipynb) |
| **Llama3.2_(11B)-Vision** | Vision | L4<br/>(16GB VRAM) | [Open in Brev](converted/kaggle-llama3/Kaggle-Llama3.2_%2811B%29-Vision.ipynb) |
| **Llama3.2_(1B)-RAFT** | RAFT | L4<br/>(16GB VRAM) | [Open in Brev](converted/kaggle-llama3/Kaggle-Llama3.2_%281B%29-RAFT.ipynb) |
| **Llama3.2_(1B_and_3B)-Conversational** | Conversational | L4<br/>(16GB VRAM) | [Open in Brev](converted/kaggle-llama3/Kaggle-Llama3.2_%281B_and_3B%29-Conversational.ipynb) |
| **Llama3.3_(70B)_A100-Conversational** | Conversational | L4<br/>(16GB VRAM) | [Open in Brev](converted/kaggle-llama3/Kaggle-Llama3.3_%2870B%29_A100-Conversational.ipynb) |
| **Llama3_(8B)-Alpaca** | Alpaca | L4<br/>(16GB VRAM) | [Open in Brev](converted/kaggle-llama3-8b/Kaggle-Llama3_%288B%29-Alpaca.ipynb) |
| **Llama3_(8B)-Conversational** | Conversational | L4<br/>(16GB VRAM) | [Open in Brev](converted/kaggle-llama3-8b/Kaggle-Llama3_%288B%29-Conversational.ipynb) |
| **Llama3_(8B)-ORPO** | ORPO | L4<br/>(16GB VRAM) | [Open in Brev](converted/kaggle-llama3-8b-orpo/Kaggle-Llama3_%288B%29-ORPO.ipynb) |
| **Llama3_(8B)-Ollama** | Ollama | L4<br/>(16GB VRAM) | [Open in Brev](converted/kaggle-llama3-8b-ollama/Kaggle-Llama3_%288B%29-Ollama.ipynb) |
| **Llasa_TTS_(1B)** | TTS | L4<br/>(16GB VRAM) | [Open in Brev](converted/kaggle-llasa-tts-1b/Kaggle-Llasa_TTS_%281B%29.ipynb) |
| **Llasa_TTS_(3B)** | TTS | L4<br/>(16GB VRAM) | [Open in Brev](converted/kaggle-llasa-tts-3b/Kaggle-Llasa_TTS_%283B%29.ipynb) |
| **Magistral_(24B)-Reasoning-Conversational** | Conversational | L4<br/>(16GB VRAM) | [Open in Brev](converted/kaggle-magistral-24b-reasoning/Kaggle-Magistral_%2824B%29-Reasoning-Conversational.ipynb) |
| **Meta-Synthetic-Data-Llama3.1_(8B)** | Synthetic Data | L4<br/>(16GB VRAM) | [Open in Brev](converted/kaggle-meta-synthetic-data-llama3/Kaggle-Meta-Synthetic-Data-Llama3.1_%288B%29.ipynb) |
| **Meta_Synthetic_Data_Llama3_2_(3B)** | Synthetic Data | L4<br/>(16GB VRAM) | [Open in Brev](converted/kaggle-meta-synthetic-data-llama3-2-3b/Kaggle-Meta_Synthetic_Data_Llama3_2_%283B%29.ipynb) |
| **Mistral_(7B)-Text_Completion** | Fine-tuning | L4<br/>(16GB VRAM) | [Open in Brev](converted/kaggle-mistral-7b-text-completion/Kaggle-Mistral_%287B%29-Text_Completion.ipynb) |
| **Mistral_Nemo_(12B)-Alpaca** | Alpaca | L4<br/>(16GB VRAM) | [Open in Brev](converted/kaggle-mistral-nemo-12b/Kaggle-Mistral_Nemo_%2812B%29-Alpaca.ipynb) |
| **Mistral_Small_(22B)-Alpaca** | Alpaca | L4<br/>(16GB VRAM) | [Open in Brev](converted/kaggle-mistral-small-22b/Kaggle-Mistral_Small_%2822B%29-Alpaca.ipynb) |
| **Mistral_v0.3_(7B)-Alpaca** | Alpaca | L4<br/>(16GB VRAM) | [Open in Brev](converted/kaggle-mistral-v0/Kaggle-Mistral_v0.3_%287B%29-Alpaca.ipynb) |
| **Mistral_v0.3_(7B)-CPT** | CPT | L4<br/>(16GB VRAM) | [Open in Brev](converted/kaggle-mistral-v0/Kaggle-Mistral_v0.3_%287B%29-CPT.ipynb) |
| **Mistral_v0.3_(7B)-Conversational** | Conversational | L4<br/>(16GB VRAM) | [Open in Brev](converted/kaggle-mistral-v0/Kaggle-Mistral_v0.3_%287B%29-Conversational.ipynb) |
| **Mistral_v0.3_(7B)-GRPO** | GRPO | L4<br/>(16GB VRAM) | [Open in Brev](converted/kaggle-mistral-v0/Kaggle-Mistral_v0.3_%287B%29-GRPO.ipynb) |
| **Orpheus_(3B)-TTS** | TTS | L4<br/>(16GB VRAM) | [Open in Brev](converted/kaggle-orpheus-3b-tts/Kaggle-Orpheus_%283B%29-TTS.ipynb) |
| **Oute_TTS_(1B)** | TTS | L4<br/>(16GB VRAM) | [Open in Brev](converted/kaggle-oute-tts-1b/Kaggle-Oute_TTS_%281B%29.ipynb) |
| **Phi_3.5_Mini-Conversational** | Conversational | L4<br/>(16GB VRAM) | [Open in Brev](converted/kaggle-phi-3/Kaggle-Phi_3.5_Mini-Conversational.ipynb) |
| **Phi_3_Medium-Conversational** | Conversational | L4<br/>(16GB VRAM) | [Open in Brev](converted/kaggle-phi-3-medium/Kaggle-Phi_3_Medium-Conversational.ipynb) |
| **Phi_4-Conversational** | Conversational | L4<br/>(16GB VRAM) | [Open in Brev](converted/kaggle-phi-4/Kaggle-Phi_4-Conversational.ipynb) |
| **Phi_4_(14B)-GRPO** | GRPO | A100-40GB<br/>(24GB VRAM) | [Open in Brev](converted/phi-4-14b-fine-tuning/Kaggle-Phi_4_%2814B%29-GRPO.ipynb) |
| **Pixtral_(12B)-Vision** | Vision | L4<br/>(16GB VRAM) | [Open in Brev](converted/kaggle-pixtral-12b-vision/Kaggle-Pixtral_%2812B%29-Vision.ipynb) |
| **Qwen2.5_(3B)-GRPO** | GRPO | L4<br/>(16GB VRAM) | [Open in Brev](converted/kaggle-qwen2/Kaggle-Qwen2.5_%283B%29-GRPO.ipynb) |
| **Qwen2.5_(7B)-Alpaca** | Alpaca | L4<br/>(16GB VRAM) | [Open in Brev](converted/kaggle-qwen2/Kaggle-Qwen2.5_%287B%29-Alpaca.ipynb) |
| **Qwen2.5_Coder_(1.5B)-Tool_Calling** | Tool Calling | L4<br/>(16GB VRAM) | [Open in Brev](converted/kaggle-qwen2.5-coder-1/Kaggle-Qwen2.5_Coder_%281.5B%29-Tool_Calling.ipynb) |
| **Qwen2.5_Coder_(14B)-Conversational** | Conversational | L4<br/>(16GB VRAM) | [Open in Brev](converted/kaggle-qwen2/Kaggle-Qwen2.5_Coder_%2814B%29-Conversational.ipynb) |
| **Qwen2.5_VL_(7B)-Vision** | Vision | L4<br/>(16GB VRAM) | [Open in Brev](converted/kaggle-qwen2/Kaggle-Qwen2.5_VL_%287B%29-Vision.ipynb) |
| **Qwen2_(7B)-Alpaca** | Alpaca | L4<br/>(16GB VRAM) | [Open in Brev](converted/kaggle-qwen2-7b/Kaggle-Qwen2_%287B%29-Alpaca.ipynb) |
| **Qwen2_5_7B_VL_GRPO** | GRPO | L4<br/>(16GB VRAM) | [Open in Brev](converted/kaggle-qwen2-5-7b-vl/Kaggle-Qwen2_5_7B_VL_GRPO.ipynb) |
| **Qwen2_VL_(7B)-Vision** | Vision | L4<br/>(16GB VRAM) | [Open in Brev](converted/kaggle-qwen2-vl-7b-vision/Kaggle-Qwen2_VL_%287B%29-Vision.ipynb) |
| **Qwen3_(14B)** | Fine-tuning | A100-40GB<br/>(24GB VRAM) | [Open in Brev](converted/qwen3-14b-fine-tuning/Kaggle-Qwen3_%2814B%29.ipynb) |
| **Qwen3_(14B)-Alpaca** | Alpaca | A100-40GB<br/>(24GB VRAM) | [Open in Brev](converted/qwen3-14b-fine-tuning/Kaggle-Qwen3_%2814B%29-Alpaca.ipynb) |
| **Qwen3_(14B)-Reasoning-Conversational** | Conversational | A100-40GB<br/>(24GB VRAM) | [Open in Brev](converted/qwen3-14b-fine-tuning/Kaggle-Qwen3_%2814B%29-Reasoning-Conversational.ipynb) |
| **Qwen3_(32B)_A100-Reasoning-Conversational** | Conversational | L4<br/>(16GB VRAM) | [Open in Brev](converted/kaggle-qwen3-32b-a100-reasoning/Kaggle-Qwen3_%2832B%29_A100-Reasoning-Conversational.ipynb) |
| **Qwen3_(4B)-GRPO** | GRPO | L4<br/>(16GB VRAM) | [Open in Brev](converted/kaggle-qwen3-4b/Kaggle-Qwen3_%284B%29-GRPO.ipynb) |
| **Qwen3_(4B)-Instruct** | Instruct | L4<br/>(16GB VRAM) | [Open in Brev](converted/kaggle-qwen3-4b-instruct/Kaggle-Qwen3_%284B%29-Instruct.ipynb) |
| **Qwen3_(4B)-Thinking** | Thinking | L4<br/>(16GB VRAM) | [Open in Brev](converted/kaggle-qwen3-4b-thinking/Kaggle-Qwen3_%284B%29-Thinking.ipynb) |
| **Qwen3_VL_(8B)-Vision** | Vision | A100-40GB<br/>(24GB VRAM) | [Open in Brev](converted/qwen3-vl-8b-vision/Kaggle-Qwen3_VL_%288B%29-Vision.ipynb) |
| **Qwen3_VL_(8B)-Vision-GRPO** | Vision | A100-40GB<br/>(24GB VRAM) | [Open in Brev](converted/qwen3-vl-8b-vision/Kaggle-Qwen3_VL_%288B%29-Vision-GRPO.ipynb) |
| **Sesame_CSM_(1B)-TTS** | TTS | T4<br/>(12GB VRAM) | [Open in Brev](converted/sesame-csm-1b-tts/Kaggle-Sesame_CSM_%281B%29-TTS.ipynb) |
| **Spark_TTS_(0_5B)** | TTS | L4<br/>(16GB VRAM) | [Open in Brev](converted/kaggle-spark-tts-0-5b/Kaggle-Spark_TTS_%280_5B%29.ipynb) |
| **TinyLlama_(1.1B)-Alpaca** | Alpaca | L4<br/>(16GB VRAM) | [Open in Brev](converted/kaggle-tinyllama-1/Kaggle-TinyLlama_%281.1B%29-Alpaca.ipynb) |
| **Unsloth_Studio** | Studio | L4<br/>(16GB VRAM) | [Open in Brev](converted/kaggle-unsloth-studio/Kaggle-Unsloth_Studio.ipynb) |
| **Whisper** | STT | L4<br/>(16GB VRAM) | [Open in Brev](converted/kaggle-whisper/Kaggle-Whisper.ipynb) |
| **Zephyr_(7B)-DPO** | DPO | L4<br/>(16GB VRAM) | [Open in Brev](converted/kaggle-zephyr-7b-dpo/Kaggle-Zephyr_%287B%29-DPO.ipynb) |
| **bert_classification** | Classification | L4<br/>(16GB VRAM) | [Open in Brev](converted/kaggle-bert-classification/Kaggle-bert_classification.ipynb) |
| **gpt-oss-(120B)_A100-Fine-tuning** | Fine-tuning | A100-80GB<br/>(80GB VRAM) | [Open in Brev](converted/gpt-oss-120b-fine-tuning/Kaggle-gpt-oss-%28120B%29_A100-Fine-tuning.ipynb) |
| **gpt-oss-(20B)-Fine-tuning** | Fine-tuning | A100-40GB<br/>(24GB VRAM) | [Open in Brev](converted/gpt-oss-20b-fine-tuning/Kaggle-gpt-oss-%2820B%29-Fine-tuning.ipynb) |
| **gpt-oss-(20B)-GRPO** | GRPO | A100-40GB<br/>(24GB VRAM) | [Open in Brev](converted/gpt-oss-20b-fine-tuning/Kaggle-gpt-oss-%2820B%29-GRPO.ipynb) |
| **gpt-oss-(20B)_A100-GRPO** | GRPO | A100-40GB<br/>(24GB VRAM) | [Open in Brev](converted/gpt-oss-20b-fine-tuning/Kaggle-gpt-oss-%2820B%29_A100-GRPO.ipynb) |

### Other Notebooks

| Model | Type | GPU Requirements | Notebook Link |
|-------|------|------------------|---------------|
| **CodeForces-cot-Finetune_for_Reasoning_on_CodeForces** | Reasoning | L4<br/>(16GB VRAM) | [Open in Brev](converted/codeforces-cot-finetune-for-reasoning-on-codeforces/CodeForces-cot-Finetune_for_Reasoning_on_CodeForces.ipynb) |
| **Falcon_H1-Alpaca** | Alpaca | L4<br/>(16GB VRAM) | [Open in Brev](converted/falcon-h1/Falcon_H1-Alpaca.ipynb) |
| **Falcon_H1_(0.5B)-Alpaca** | Alpaca | L4<br/>(16GB VRAM) | [Open in Brev](converted/falcon-h1-0/Falcon_H1_%280.5B%29-Alpaca.ipynb) |
| **Granite4.0** | Fine-tuning | L4<br/>(16GB VRAM) | [Open in Brev](converted/granite4/Granite4.0.ipynb) |
| **Synthetic_Data_Hackathon** | Synthetic Data | L4<br/>(16GB VRAM) | [Open in Brev](converted/synthetic-data-hackathon/Synthetic_Data_Hackathon.ipynb) |
| **Unsloth_Studio** | Studio | L4<br/>(16GB VRAM) | [Open in Brev](converted/unsloth-studio/Unsloth_Studio.ipynb) |
| **Zephyr_(7B)-DPO** | DPO | L4<br/>(16GB VRAM) | [Open in Brev](converted/zephyr-7b-dpo/Zephyr_%287B%29-DPO.ipynb) |
| **bert_classification** | Classification | L4<br/>(16GB VRAM) | [Open in Brev](converted/bert-classification/bert_classification.ipynb) |
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

