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

## 📒 Available Launchables

Below are **181 Unsloth notebooks** organized into **129 launchables** for NVIDIA Brev, categorized by model type. Each notebook is fully adapted for Brev environments with GPU-optimized configurations, companion files, and ready-to-run setups.

**Quick Start:** Browse the notebooks below, clone this repo, and deploy on [Brev Console](https://brev.nvidia.com) or run locally with Docker. View the [original Unsloth notebooks here](https://github.com/unslothai/notebooks).

<!-- LAUNCHABLES_TABLE_START -->

### Main Notebooks

| Model | Type | GPU Requirements | Notebook Link |
|-------|------|------------------|---------------|
| **Codegemma (7B) Conversational** | Conversational | L4 (16GB) | [View Notebook](converted/codegemma-7b/CodeGemma_(7B)-Conversational.ipynb) |
| **Gemma2 (2B) Alpaca** | Alpaca | L4 (16GB) | [View Notebook](converted/gemma2-2b/Gemma2_(2B)-Alpaca.ipynb) |
| **Gemma2 (9B) Alpaca** | Alpaca | L4 (16GB) | [View Notebook](converted/gemma2-9b/Gemma2_(9B)-Alpaca.ipynb) |
| **Gemma3 (270M)** | Fine-tuning | L4 (16GB) | [View Notebook](converted/gemma3-270m/Gemma3_(270M).ipynb) |
| **Gemma3 (27B) A100 Conversational** | Conversational | L4 (16GB) | [View Notebook](converted/gemma3-27b/Gemma3_(27B)_A100-Conversational.ipynb) |
| **Gemma3 (4B)** | Fine-tuning | L4 (16GB) | [View Notebook](converted/gemma3-4b/Gemma3_(4B).ipynb) |
| **Gemma3N (2B) Inference** | Inference | L4 (16GB) | [View Notebook](converted/gemma3n-2b/Gemma3N_(2B)-Inference.ipynb) |
| **Gemma3N (4B) Audio** | Fine-tuning | L4 (16GB) | [View Notebook](converted/gemma3n-4b-audio/Gemma3N_(4B)-Audio.ipynb) |
| **Gemma3N (4B) Conversational** | Conversational | L4 (16GB) | [View Notebook](converted/gemma3n-4b/Gemma3N_(4B)-Conversational.ipynb) |
| **Kaggle Codegemma (7B) Conversational** | Conversational | L4 (16GB) | [View Notebook](converted/kaggle-codegemma-7b/Kaggle-CodeGemma_(7B)-Conversational.ipynb) |
| **Kaggle Gemma2 (2B) Alpaca** | Alpaca | L4 (16GB) | [View Notebook](converted/kaggle-gemma2-2b/Kaggle-Gemma2_(2B)-Alpaca.ipynb) |
| **Kaggle Gemma2 (9B) Alpaca** | Alpaca | L4 (16GB) | [View Notebook](converted/kaggle-gemma2-9b/Kaggle-Gemma2_(9B)-Alpaca.ipynb) |
| **Kaggle Gemma3 (270M)** | Fine-tuning | L4 (16GB) | [View Notebook](converted/kaggle-gemma3-270m/Kaggle-Gemma3_(270M).ipynb) |
| **Kaggle Gemma3 (27B) A100 Conversational** | Conversational | L4 (16GB) | [View Notebook](converted/kaggle-gemma3-27b/Kaggle-Gemma3_(27B)_A100-Conversational.ipynb) |
| **Kaggle Gemma3 (4B)** | Fine-tuning | L4 (16GB) | [View Notebook](converted/kaggle-gemma3-4b/Kaggle-Gemma3_(4B).ipynb) |
| **Kaggle Gemma3N (2B) Inference** | Inference | L4 (16GB) | [View Notebook](converted/kaggle-gemma3n-2b/Kaggle-Gemma3N_(2B)-Inference.ipynb) |
| **Kaggle Gemma3N (4B) Audio** | Fine-tuning | L4 (16GB) | [View Notebook](converted/kaggle-gemma3n-4b-audio/Kaggle-Gemma3N_(4B)-Audio.ipynb) |
| **Kaggle Gemma3N (4B) Conversational** | Conversational | L4 (16GB) | [View Notebook](converted/kaggle-gemma3n-4b/Kaggle-Gemma3N_(4B)-Conversational.ipynb) |
| **Kaggle Llama3** | Conversational | L4 (16GB) | [View Notebook](converted/kaggle-llama3/Kaggle-Llama3.2_(1B_and_3B)-Conversational.ipynb) |
| **Kaggle Llama3 (8B) Conversational** | Alpaca | L4 (16GB) | [View Notebook](converted/kaggle-llama3-8b/Kaggle-Llama3_(8B)-Alpaca.ipynb) |
| **Kaggle Llama3 (8B) Ollama** | Fine-tuning | L4 (16GB) | [View Notebook](converted/kaggle-llama3-8b-ollama/Kaggle-Llama3_(8B)-Ollama.ipynb) |
| **Kaggle Llama3 (8B) Orpo** | ORPO | L4 (16GB) | [View Notebook](converted/kaggle-llama3-8b-orpo/Kaggle-Llama3_(8B)-ORPO.ipynb) |
| **Kaggle Meta Synthetic Data Llama3** | Synthetic Data | L4 (16GB) | [View Notebook](converted/kaggle-meta-synthetic-data-llama3/Kaggle-Meta-Synthetic-Data-Llama3.1_(8B).ipynb) |
| **Kaggle Meta Synthetic Data Llama3 2 (3B)** | Synthetic Data | L4 (16GB) | [View Notebook](converted/kaggle-meta-synthetic-data-llama3-2-3b/Kaggle-Meta_Synthetic_Data_Llama3_2_(3B).ipynb) |
| **Kaggle Mistral (7B) Text Completion** | Fine-tuning | L4 (16GB) | [View Notebook](converted/kaggle-mistral-7b-text-completion/Kaggle-Mistral_(7B)-Text_Completion.ipynb) |
| **Kaggle Mistral Nemo (12B) Alpaca** | Alpaca | L4 (16GB) | [View Notebook](converted/kaggle-mistral-nemo-12b/Kaggle-Mistral_Nemo_(12B)-Alpaca.ipynb) |
| **Kaggle Mistral Small (22B) Alpaca** | Alpaca | L4 (16GB) | [View Notebook](converted/kaggle-mistral-small-22b/Kaggle-Mistral_Small_(22B)-Alpaca.ipynb) |
| **Kaggle Mistral V0** | Alpaca | L4 (16GB) | [View Notebook](converted/kaggle-mistral-v0/Kaggle-Mistral_v0.3_(7B)-Alpaca.ipynb) |
| **Kaggle Phi 3** | Conversational | L4 (16GB) | [View Notebook](converted/kaggle-phi-3/Kaggle-Phi_3.5_Mini-Conversational.ipynb) |
| **Kaggle Phi 3 Medium Conversational** | Conversational | L4 (16GB) | [View Notebook](converted/kaggle-phi-3-medium/Kaggle-Phi_3_Medium-Conversational.ipynb) |
| **Kaggle Phi 4 Conversational** | Conversational | L4 (16GB) | [View Notebook](converted/kaggle-phi-4/Kaggle-Phi_4-Conversational.ipynb) |
| **Kaggle Qwen2** | Conversational | L4 (16GB) | [View Notebook](converted/kaggle-qwen2/Kaggle-Qwen2.5_Coder_(14B)-Conversational.ipynb) |
| **Kaggle Qwen2 (7B) Alpaca** | Alpaca | L4 (16GB) | [View Notebook](converted/kaggle-qwen2-7b/Kaggle-Qwen2_(7B)-Alpaca.ipynb) |
| **Kaggle Qwen2.5 Coder (1** | Fine-tuning | L4 (16GB) | [View Notebook](converted/kaggle-qwen2.5-coder-1/Kaggle-Qwen2.5_Coder_(1.5B)-Tool_Calling.ipynb) |
| **Kaggle Qwen3 (32B) A100 Reasoning Conversational** | Conversational | L4 (16GB) | [View Notebook](converted/kaggle-qwen3-32b-a100-reasoning/Kaggle-Qwen3_(32B)_A100-Reasoning-Conversational.ipynb) |
| **Kaggle Qwen3 (4B) Instruct** | Instruct | L4 (16GB) | [View Notebook](converted/kaggle-qwen3-4b-instruct/Kaggle-Qwen3_(4B)-Instruct.ipynb) |
| **Kaggle Qwen3 (4B) Thinking** | Thinking | L4 (16GB) | [View Notebook](converted/kaggle-qwen3-4b-thinking/Kaggle-Qwen3_(4B)-Thinking.ipynb) |
| **Kaggle Tinyllama (1** | Alpaca | L4 (16GB) | [View Notebook](converted/kaggle-tinyllama-1/Kaggle-TinyLlama_(1.1B)-Alpaca.ipynb) |
| **Llama3 (8B) Alpaca** | Conversational | L4 (16GB) | [View Notebook](converted/llama3-8b/Llama3_(8B)-Conversational.ipynb) |
| **Llama3 (8B) Ollama** | Fine-tuning | L4 (16GB) | [View Notebook](converted/llama3-8b-ollama/Llama3_(8B)-Ollama.ipynb) |
| **Llama3 (8B) Orpo** | ORPO | L4 (16GB) | [View Notebook](converted/llama3-8b-orpo/Llama3_(8B)-ORPO.ipynb) |
| **Meta Synthetic Data Llama3** | Synthetic Data | L4 (16GB) | [View Notebook](converted/meta-synthetic-data-llama3/Meta-Synthetic-Data-Llama3.1_(8B).ipynb) |
| **Meta Synthetic Data Llama3 2 (3B)** | Synthetic Data | L4 (16GB) | [View Notebook](converted/meta-synthetic-data-llama3-2-3b/Meta_Synthetic_Data_Llama3_2_(3B).ipynb) |
| **Mistral (7B) Text Completion** | Fine-tuning | L4 (16GB) | [View Notebook](converted/mistral-7b-text-completion/Mistral_(7B)-Text_Completion.ipynb) |
| **Mistral Nemo (12B) Alpaca** | Alpaca | L4 (16GB) | [View Notebook](converted/mistral-nemo-12b/Mistral_Nemo_(12B)-Alpaca.ipynb) |
| **Mistral Small (22B) Alpaca** | Alpaca | L4 (16GB) | [View Notebook](converted/mistral-small-22b/Mistral_Small_(22B)-Alpaca.ipynb) |
| **Mistral V0** | Conversational | L4 (16GB) | [View Notebook](converted/mistral-v0/Mistral_v0.3_(7B)-Conversational.ipynb) |
| **Phi 3** | Conversational | L4 (16GB) | [View Notebook](converted/phi-3/Phi_3.5_Mini-Conversational.ipynb) |
| **Phi 3 Medium Conversational** | Conversational | L4 (16GB) | [View Notebook](converted/phi-3-medium/Phi_3_Medium-Conversational.ipynb) |
| **Phi-4 (14B)** | Conversational | A100-40GB (24GB) | [View Notebook](converted/phi-4-14b-fine-tuning/Phi_4-Conversational.ipynb) |
| **Qwen2 (7B) Alpaca** | Alpaca | L4 (16GB) | [View Notebook](converted/qwen2-7b/Qwen2_(7B)-Alpaca.ipynb) |
| **Qwen2.5 Coder (1** | Fine-tuning | L4 (16GB) | [View Notebook](converted/qwen2.5-coder-1/Qwen2.5_Coder_(1.5B)-Tool_Calling.ipynb) |
| **Qwen3 (14B)** | Fine-tuning | A100-40GB (24GB) | [View Notebook](converted/qwen3-14b-fine-tuning/Qwen3_(14B).ipynb) |
| **Qwen3 (32B) A100 Reasoning Conversational** | Conversational | L4 (16GB) | [View Notebook](converted/qwen3-32b-a100-reasoning/Qwen3_(32B)_A100-Reasoning-Conversational.ipynb) |
| **Qwen3 (4B) Instruct** | Instruct | L4 (16GB) | [View Notebook](converted/qwen3-4b-instruct/Qwen3_(4B)-Instruct.ipynb) |
| **Qwen3 (4B) Thinking** | Thinking | L4 (16GB) | [View Notebook](converted/qwen3-4b-thinking/Qwen3_(4B)-Thinking.ipynb) |
| **Tinyllama (1** | Alpaca | L4 (16GB) | [View Notebook](converted/tinyllama-1/TinyLlama_(1.1B)-Alpaca.ipynb) |

### Vision (Multimodal) Notebooks

| Model | Type | GPU Requirements | Notebook Link |
|-------|------|------------------|---------------|
| **Gemma3 (4B) Vision Grpo** | Vision | L4 (16GB) | [View Notebook](converted/gemma3-4b-vision/Gemma3_(4B)-Vision.ipynb) |
| **Gemma3N (4B) Vision** | Vision | L4 (16GB) | [View Notebook](converted/gemma3n-4b-vision/Gemma3N_(4B)-Vision.ipynb) |
| **Huggingface Course Gemma3 (4B) Vision Grpo** | Vision | L4 (16GB) | [View Notebook](converted/huggingface course-gemma3-4b-vision/HuggingFace Course-Gemma3_(4B)-Vision-GRPO.ipynb) |
| **Kaggle Gemma3 (4B) Vision Grpo** | Vision | L4 (16GB) | [View Notebook](converted/kaggle-gemma3-4b-vision/Kaggle-Gemma3_(4B)-Vision.ipynb) |
| **Kaggle Gemma3N (4B) Vision** | Vision | L4 (16GB) | [View Notebook](converted/kaggle-gemma3n-4b-vision/Kaggle-Gemma3N_(4B)-Vision.ipynb) |
| **Kaggle Pixtral (12B) Vision** | Vision | L4 (16GB) | [View Notebook](converted/kaggle-pixtral-12b-vision/Kaggle-Pixtral_(12B)-Vision.ipynb) |
| **Kaggle Qwen2 Vl (7B) Vision** | Vision | L4 (16GB) | [View Notebook](converted/kaggle-qwen2-vl-7b-vision/Kaggle-Qwen2_VL_(7B)-Vision.ipynb) |
| **Llama3** | Vision | L4 (16GB) | [View Notebook](converted/llama3/Llama3.2_(11B)-Vision.ipynb) |
| **Pixtral (12B) Vision** | Vision | L4 (16GB) | [View Notebook](converted/pixtral-12b-vision/Pixtral_(12B)-Vision.ipynb) |
| **Qwen2** | Vision | L4 (16GB) | [View Notebook](converted/qwen2/Qwen2.5_VL_(7B)-Vision.ipynb) |
| **Qwen2 Vl (7B) Vision** | Vision | L4 (16GB) | [View Notebook](converted/qwen2-vl-7b-vision/Qwen2_VL_(7B)-Vision.ipynb) |
| **Qwen3-VL (8B)** | Vision | A100-40GB (24GB) | [View Notebook](converted/qwen3-vl-8b-vision/Kaggle-Qwen3_VL_(8B)-Vision.ipynb) |

### Text-to-Speech (TTS) Notebooks

| Model | Type | GPU Requirements | Notebook Link |
|-------|------|------------------|---------------|
| **Sesame-CSM (1B)** | TTS | T4 (12GB) | [View Notebook](converted/sesame-csm-1b-tts/Kaggle-Sesame_CSM_(1B)-TTS.ipynb) |

### Speech-to-Text (STT) Notebooks

| Model | Type | GPU Requirements | Notebook Link |
|-------|------|------------------|---------------|
| **Kaggle Whisper** | STT | L4 (16GB) | [View Notebook](converted/kaggle-whisper/Kaggle-Whisper.ipynb) |
| **Whisper Large V3** | STT | L4 (16GB) | [View Notebook](converted/whisper-large-v3-stt/Whisper.ipynb) |

### GRPO Notebooks

| Model | Type | GPU Requirements | Notebook Link |
|-------|------|------------------|---------------|
| **Advanced Llama3 1 (3B) Grpo Lora** | GRPO | L4 (16GB) | [View Notebook](converted/advanced-llama3-1-3b-grpo-lora/Advanced_Llama3_1_(3B)_GRPO_LoRA.ipynb) |
| **Advanced Llama3 2 (3B) Grpo Lora** | GRPO | L4 (16GB) | [View Notebook](converted/advanced-llama3-2-3b-grpo-lora/Advanced_Llama3_2_(3B)_GRPO_LoRA.ipynb) |
| **Deepseek R1 0528 Qwen3 (8B) Grpo** | GRPO | L4 (16GB) | [View Notebook](converted/deepseek-r1-0528-qwen3-8b/DeepSeek_R1_0528_Qwen3_(8B)_GRPO.ipynb) |
| **Gemma3 (1B) Grpo** | GRPO | L4 (16GB) | [View Notebook](converted/gemma3-1b/Gemma3_(1B)-GRPO.ipynb) |
| **Huggingface Course Advanced Llama3 1 (3B) Grpo Lora** | GRPO | L4 (16GB) | [View Notebook](converted/huggingface course-advanced-llama3-1-3b-grpo-lora/HuggingFace Course-Advanced_Llama3_1_(3B)_GRPO_LoRA.ipynb) |
| **Huggingface Course Advanced Llama3 2 (3B) Grpo Lora** | GRPO | L4 (16GB) | [View Notebook](converted/huggingface course-advanced-llama3-2-3b-grpo-lora/HuggingFace Course-Advanced_Llama3_2_(3B)_GRPO_LoRA.ipynb) |
| **Huggingface Course Deepseek R1 0528 Qwen3 (8B) Grpo** | GRPO | L4 (16GB) | [View Notebook](converted/huggingface course-deepseek-r1-0528-qwen3-8b/HuggingFace Course-DeepSeek_R1_0528_Qwen3_(8B)_GRPO.ipynb) |
| **Huggingface Course Gemma3 (1B) Grpo** | GRPO | L4 (16GB) | [View Notebook](converted/huggingface course-gemma3-1b/HuggingFace Course-Gemma3_(1B)-GRPO.ipynb) |
| **Huggingface Course Llama3** | GRPO | L4 (16GB) | [View Notebook](converted/huggingface course-llama3/HuggingFace Course-Llama3.1_(8B)-GRPO.ipynb) |
| **Huggingface Course Mistral V0** | GRPO | L4 (16GB) | [View Notebook](converted/huggingface course-mistral-v0/HuggingFace Course-Mistral_v0.3_(7B)-GRPO.ipynb) |
| **Huggingface Course Qwen2** | GRPO | L4 (16GB) | [View Notebook](converted/huggingface course-qwen2/HuggingFace Course-Qwen2.5_(3B)-GRPO.ipynb) |
| **Huggingface Course Qwen2 5 7B Vl Grpo** | GRPO | L4 (16GB) | [View Notebook](converted/huggingface course-qwen2-5-7b-vl/HuggingFace Course-Qwen2_5_7B_VL_GRPO.ipynb) |
| **Huggingface Course Qwen3 (4B) Grpo** | GRPO | L4 (16GB) | [View Notebook](converted/huggingface course-qwen3-4b/HuggingFace Course-Qwen3_(4B)-GRPO.ipynb) |
| **Kaggle Advanced Llama3 1 (3B) Grpo Lora** | GRPO | L4 (16GB) | [View Notebook](converted/kaggle-advanced-llama3-1-3b-grpo-lora/Kaggle-Advanced_Llama3_1_(3B)_GRPO_LoRA.ipynb) |
| **Kaggle Advanced Llama3 2 (3B) Grpo Lora** | GRPO | L4 (16GB) | [View Notebook](converted/kaggle-advanced-llama3-2-3b-grpo-lora/Kaggle-Advanced_Llama3_2_(3B)_GRPO_LoRA.ipynb) |
| **Kaggle Deepseek R1 0528 Qwen3 (8B) Grpo** | GRPO | L4 (16GB) | [View Notebook](converted/kaggle-deepseek-r1-0528-qwen3-8b/Kaggle-DeepSeek_R1_0528_Qwen3_(8B)_GRPO.ipynb) |
| **Kaggle Gemma3 (1B) Grpo** | GRPO | L4 (16GB) | [View Notebook](converted/kaggle-gemma3-1b/Kaggle-Gemma3_(1B)-GRPO.ipynb) |
| **Kaggle Qwen2 5 7B Vl Grpo** | GRPO | L4 (16GB) | [View Notebook](converted/kaggle-qwen2-5-7b-vl/Kaggle-Qwen2_5_7B_VL_GRPO.ipynb) |
| **Kaggle Qwen3 (4B) Grpo** | GRPO | L4 (16GB) | [View Notebook](converted/kaggle-qwen3-4b/Kaggle-Qwen3_(4B)-GRPO.ipynb) |
| **Qwen2 5 7B Vl Grpo** | GRPO | L4 (16GB) | [View Notebook](converted/qwen2-5-7b-vl/Qwen2_5_7B_VL_GRPO.ipynb) |
| **Qwen3 (4B) GRPO** | GRPO | L4 (16GB) | [View Notebook](converted/qwen3-4b-grpo-rl/Qwen3_(4B)-GRPO.ipynb) |
| **gpt-oss-20b-GRPO** | GRPO | A100-80GB (40GB) | [View Notebook](converted/gpt-oss-20b-grpo-rl/gpt_oss_(20B)_GRPO_BF16.ipynb) |

### Other Notebooks

| Model | Type | GPU Requirements | Notebook Link |
|-------|------|------------------|---------------|
| **Bert Classification** | Classification | L4 (16GB) | [View Notebook](converted/bert-classification/bert_classification.ipynb) |
| **Codeforces Cot Finetune For Reasoning On Codeforces** | Reasoning | L4 (16GB) | [View Notebook](converted/codeforces-cot-finetune-for-reasoning-on-codeforces/CodeForces-cot-Finetune_for_Reasoning_on_CodeForces.ipynb) |
| **Falcon H1 (0** | Alpaca | L4 (16GB) | [View Notebook](converted/falcon-h1-0/Falcon_H1_(0.5B)-Alpaca.ipynb) |
| **Falcon H1 Alpaca** | Alpaca | L4 (16GB) | [View Notebook](converted/falcon-h1/Falcon_H1-Alpaca.ipynb) |
| **Gpt Oss Bnb (20B) Inference** | Inference | L4 (16GB) | [View Notebook](converted/gpt-oss-bnb-20b/GPT_OSS_BNB_(20B)-Inference.ipynb) |
| **Gpt Oss Mxfp4 (20B) Inference** | Inference | L4 (16GB) | [View Notebook](converted/gpt-oss-mxfp4-20b/GPT_OSS_MXFP4_(20B)-Inference.ipynb) |
| **Granite4** | Fine-tuning | L4 (16GB) | [View Notebook](converted/granite4/Granite4.0.ipynb) |
| **Kaggle Bert Classification** | Classification | L4 (16GB) | [View Notebook](converted/kaggle-bert-classification/Kaggle-bert_classification.ipynb) |
| **Kaggle Codeforces Cot Finetune For Reasoning On Codeforces** | Reasoning | L4 (16GB) | [View Notebook](converted/kaggle-codeforces-cot-finetune-for-reasoning-on-codeforces/Kaggle-CodeForces-cot-Finetune_for_Reasoning_on_CodeForces.ipynb) |
| **Kaggle Falcon H1 (0** | Alpaca | L4 (16GB) | [View Notebook](converted/kaggle-falcon-h1-0/Kaggle-Falcon_H1_(0.5B)-Alpaca.ipynb) |
| **Kaggle Gpt Oss Bnb (20B) Inference** | Inference | L4 (16GB) | [View Notebook](converted/kaggle-gpt-oss-bnb-20b/Kaggle-GPT_OSS_BNB_(20B)-Inference.ipynb) |
| **Kaggle Gpt Oss Mxfp4 (20B) Inference** | Inference | L4 (16GB) | [View Notebook](converted/kaggle-gpt-oss-mxfp4-20b/Kaggle-GPT_OSS_MXFP4_(20B)-Inference.ipynb) |
| **Kaggle Granite4** | Fine-tuning | L4 (16GB) | [View Notebook](converted/kaggle-granite4/Kaggle-Granite4.0.ipynb) |
| **Kaggle Liquid Lfm2 (1** | Conversational | L4 (16GB) | [View Notebook](converted/kaggle-liquid-lfm2-1/Kaggle-Liquid_LFM2_(1.2B)-Conversational.ipynb) |
| **Kaggle Llasa Tts (1B)** | TTS | L4 (16GB) | [View Notebook](converted/kaggle-llasa-tts-1b/Kaggle-Llasa_TTS_(1B).ipynb) |
| **Kaggle Llasa Tts (3B)** | TTS | L4 (16GB) | [View Notebook](converted/kaggle-llasa-tts-3b/Kaggle-Llasa_TTS_(3B).ipynb) |
| **Kaggle Magistral (24B) Reasoning Conversational** | Conversational | L4 (16GB) | [View Notebook](converted/kaggle-magistral-24b-reasoning/Kaggle-Magistral_(24B)-Reasoning-Conversational.ipynb) |
| **Kaggle Orpheus (3B) Tts** | TTS | L4 (16GB) | [View Notebook](converted/kaggle-orpheus-3b-tts/Kaggle-Orpheus_(3B)-TTS.ipynb) |
| **Kaggle Oute Tts (1B)** | TTS | L4 (16GB) | [View Notebook](converted/kaggle-oute-tts-1b/Kaggle-Oute_TTS_(1B).ipynb) |
| **Kaggle Spark Tts (0 5B)** | TTS | L4 (16GB) | [View Notebook](converted/kaggle-spark-tts-0-5b/Kaggle-Spark_TTS_(0_5B).ipynb) |
| **Kaggle Unsloth Studio** | Fine-tuning | L4 (16GB) | [View Notebook](converted/kaggle-unsloth-studio/Kaggle-Unsloth_Studio.ipynb) |
| **Kaggle Zephyr (7B) Dpo** | DPO | L4 (16GB) | [View Notebook](converted/kaggle-zephyr-7b-dpo/Kaggle-Zephyr_(7B)-DPO.ipynb) |
| **Liquid Lfm2 (1** | Conversational | L4 (16GB) | [View Notebook](converted/liquid-lfm2-1/Liquid_LFM2_(1.2B)-Conversational.ipynb) |
| **Liquid Lfm2 Conversational** | Conversational | L4 (16GB) | [View Notebook](converted/liquid-lfm2/Liquid_LFM2-Conversational.ipynb) |
| **Llasa Tts (1B)** | TTS | L4 (16GB) | [View Notebook](converted/llasa-tts-1b/Llasa_TTS_(1B).ipynb) |
| **Llasa Tts (3B)** | TTS | L4 (16GB) | [View Notebook](converted/llasa-tts-3b/Llasa_TTS_(3B).ipynb) |
| **Magistral (24B) Reasoning Conversational** | Conversational | L4 (16GB) | [View Notebook](converted/magistral-24b-reasoning/Magistral_(24B)-Reasoning-Conversational.ipynb) |
| **Orpheus (3B) Tts** | TTS | L4 (16GB) | [View Notebook](converted/orpheus-3b-tts/Orpheus_(3B)-TTS.ipynb) |
| **Oute Tts (1B)** | TTS | L4 (16GB) | [View Notebook](converted/oute-tts-1b/Oute_TTS_(1B).ipynb) |
| **Spark Tts (0 5B)** | TTS | L4 (16GB) | [View Notebook](converted/spark-tts-0-5b/Spark_TTS_(0_5B).ipynb) |
| **Synthetic Data Hackathon** | Synthetic Data | L4 (16GB) | [View Notebook](converted/synthetic-data-hackathon/Synthetic_Data_Hackathon.ipynb) |
| **Unsloth Studio** | Fine-tuning | L4 (16GB) | [View Notebook](converted/unsloth-studio/Unsloth_Studio.ipynb) |
| **Zephyr (7B) Dpo** | DPO | L4 (16GB) | [View Notebook](converted/zephyr-7b-dpo/Zephyr_(7B)-DPO.ipynb) |
| **gpt-oss-120b** | Fine-tuning | A100-80GB (80GB) | [View Notebook](converted/gpt-oss-120b-fine-tuning/Kaggle-gpt-oss-(120B)_A100-Fine-tuning.ipynb) |
| **gpt-oss-20b** | Fine-tuning | A100-40GB (24GB) | [View Notebook](converted/gpt-oss-20b-fine-tuning/Kaggle-gpt-oss-(20B)-Fine-tuning.ipynb) |
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

