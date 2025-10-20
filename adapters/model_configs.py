"""
Model Configurations

Contains metadata and configuration for each supported model/notebook.
"""

import re
from pathlib import Path
from typing import Dict, Optional

# Model configurations registry
MODEL_CONFIGS: Dict[str, Dict] = {
    # gpt-oss models
    "gpt-oss-20b": {
        "model_name": "gpt-oss-20b",
        "launchable_name": "gpt-oss-20b-fine-tuning",
        "recommended_gpu": "A100-40GB",
        "min_vram_gb": 24,
        "recommended_batch_size": 2,
        "categories": ["reasoning", "fine-tuning", "large-model"],
        "difficulty": "advanced",
        "upstream_notebook_url": "https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/gpt-oss-20b.ipynb",
        "multi_gpu": True
    },
    "gpt-oss-20b-grpo": {
        "model_name": "gpt-oss-20b-GRPO",
        "launchable_name": "gpt-oss-20b-grpo-rl",
        "recommended_gpu": "A100-80GB",
        "min_vram_gb": 40,
        "recommended_batch_size": 1,
        "categories": ["reasoning", "reinforcement-learning", "grpo"],
        "difficulty": "advanced",
        "upstream_notebook_url": "https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/gpt-oss-20b-grpo.ipynb",
        "multi_gpu": True
    },
    "gpt-oss-120b": {
        "model_name": "gpt-oss-120b",
        "launchable_name": "gpt-oss-120b-fine-tuning",
        "recommended_gpu": "A100-80GB",
        "min_vram_gb": 80,
        "recommended_batch_size": 1,
        "categories": ["reasoning", "fine-tuning", "large-model"],
        "difficulty": "advanced",
        "upstream_notebook_url": "https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/gpt-oss-120b.ipynb",
        "multi_gpu": True
    },

    # Gemma models
    "gemma-3-4b": {
        "model_name": "Gemma 3 (4B)",
        "launchable_name": "gemma-3-4b-fine-tuning",
        "recommended_gpu": "L4",
        "min_vram_gb": 16,
        "recommended_batch_size": 4,
        "categories": ["text-generation", "fine-tuning"],
        "difficulty": "beginner",
        "upstream_notebook_url": "https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Gemma_3_(4B).ipynb",
        "multi_gpu": False
    },
    "gemma-3-4b-vision": {
        "model_name": "Gemma 3 (4B) Vision",
        "launchable_name": "gemma-3-4b-vision",
        "recommended_gpu": "L4",
        "min_vram_gb": 20,
        "recommended_batch_size": 2,
        "categories": ["vision", "multimodal", "fine-tuning"],
        "difficulty": "intermediate",
        "upstream_notebook_url": "https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Gemma_3_(4B)_vision.ipynb",
        "multi_gpu": False
    },
    "gemma-3-1b-grpo": {
        "model_name": "Gemma 3 (1B) GRPO",
        "launchable_name": "gemma-3-1b-grpo-rl",
        "recommended_gpu": "T4",
        "min_vram_gb": 12,
        "recommended_batch_size": 4,
        "categories": ["reinforcement-learning", "grpo", "reasoning"],
        "difficulty": "intermediate",
        "upstream_notebook_url": "https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Gemma_3_(1B)_grpo.ipynb",
        "multi_gpu": False
    },
    "gemma-3n-e4b": {
        "model_name": "Gemma 3n (E4B)",
        "launchable_name": "gemma-3n-e4b-multimodal",
        "recommended_gpu": "L4",
        "min_vram_gb": 16,
        "recommended_batch_size": 2,
        "categories": ["multimodal", "text", "vision", "audio"],
        "difficulty": "intermediate",
        "upstream_notebook_url": "https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Gemma_3n_(E4B).ipynb",
        "multi_gpu": False
    },

    # Llama models
    "llama-3.1-8b": {
        "model_name": "Llama 3.1 (8B)",
        "launchable_name": "llama-3.1-8b-fine-tuning",
        "recommended_gpu": "L4",
        "min_vram_gb": 16,
        "recommended_batch_size": 4,
        "categories": ["text-generation", "fine-tuning"],
        "difficulty": "beginner",
        "upstream_notebook_url": "https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Llama_3.1_(8B).ipynb",
        "multi_gpu": False
    },
    "llama-3.2-1b": {
        "model_name": "Llama 3.2 (1B)",
        "launchable_name": "llama-3.2-1b-fine-tuning",
        "recommended_gpu": "T4",
        "min_vram_gb": 8,
        "recommended_batch_size": 8,
        "categories": ["text-generation", "fine-tuning", "small-model"],
        "difficulty": "beginner",
        "upstream_notebook_url": "https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Llama_3.2_(1B).ipynb",
        "multi_gpu": False
    },
    "llama-3.2-3b": {
        "model_name": "Llama 3.2 (3B)",
        "launchable_name": "llama-3.2-3b-fine-tuning",
        "recommended_gpu": "T4",
        "min_vram_gb": 12,
        "recommended_batch_size": 4,
        "categories": ["text-generation", "fine-tuning"],
        "difficulty": "beginner",
        "upstream_notebook_url": "https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Llama_3.2_(3B).ipynb",
        "multi_gpu": False
    },
    "llama-3.2-3b-grpo": {
        "model_name": "Llama 3.2 (3B) GRPO",
        "launchable_name": "llama-3.2-3b-grpo-rl",
        "recommended_gpu": "L4",
        "min_vram_gb": 16,
        "recommended_batch_size": 2,
        "categories": ["reinforcement-learning", "grpo", "reasoning"],
        "difficulty": "intermediate",
        "upstream_notebook_url": "https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Llama_3.2_(3B)_grpo.ipynb",
        "multi_gpu": False
    },
    "llama-3.2-vision-11b": {
        "model_name": "Llama 3.2 Vision (11B)",
        "launchable_name": "llama-3.2-vision-11b",
        "recommended_gpu": "A100-40GB",
        "min_vram_gb": 24,
        "recommended_batch_size": 2,
        "categories": ["vision", "multimodal", "fine-tuning"],
        "difficulty": "intermediate",
        "upstream_notebook_url": "https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Llama_3.2_Vision_(11B).ipynb",
        "multi_gpu": False
    },

    # Qwen models
    "qwen3-14b": {
        "model_name": "Qwen3 (14B)",
        "launchable_name": "qwen3-14b-fine-tuning",
        "recommended_gpu": "A100-40GB",
        "min_vram_gb": 24,
        "recommended_batch_size": 2,
        "categories": ["text-generation", "fine-tuning"],
        "difficulty": "intermediate",
        "upstream_notebook_url": "https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Qwen3_(14B).ipynb",
        "multi_gpu": False
    },
    "qwen3-4b-grpo": {
        "model_name": "Qwen3 (4B) GRPO",
        "launchable_name": "qwen3-4b-grpo-rl",
        "recommended_gpu": "L4",
        "min_vram_gb": 16,
        "recommended_batch_size": 2,
        "categories": ["reinforcement-learning", "grpo", "reasoning"],
        "difficulty": "intermediate",
        "upstream_notebook_url": "https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Qwen3_(4B)_grpo.ipynb",
        "multi_gpu": False
    },
    "qwen3-vl-8b": {
        "model_name": "Qwen3-VL (8B)",
        "launchable_name": "qwen3-vl-8b-vision",
        "recommended_gpu": "A100-40GB",
        "min_vram_gb": 24,
        "recommended_batch_size": 2,
        "categories": ["vision", "multimodal", "fine-tuning"],
        "difficulty": "intermediate",
        "upstream_notebook_url": "https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Qwen3-VL_(8B).ipynb",
        "multi_gpu": False
    },
    "qwen3-vl-8b-grpo": {
        "model_name": "Qwen3-VL (8B) GRPO",
        "launchable_name": "qwen3-vl-8b-grpo-vision-rl",
        "recommended_gpu": "A100-40GB",
        "min_vram_gb": 32,
        "recommended_batch_size": 1,
        "categories": ["vision", "reinforcement-learning", "grpo"],
        "difficulty": "advanced",
        "upstream_notebook_url": "https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Qwen3-VL_(8B)_grpo.ipynb",
        "multi_gpu": False
    },

    # Phi models
    "phi-4-14b": {
        "model_name": "Phi-4 (14B)",
        "launchable_name": "phi-4-14b-fine-tuning",
        "recommended_gpu": "A100-40GB",
        "min_vram_gb": 24,
        "recommended_batch_size": 2,
        "categories": ["text-generation", "fine-tuning", "reasoning"],
        "difficulty": "intermediate",
        "upstream_notebook_url": "https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Phi-4_(14B).ipynb",
        "multi_gpu": False
    },
    "phi-4-14b-grpo": {
        "model_name": "Phi-4 (14B) GRPO",
        "launchable_name": "phi-4-14b-grpo-rl",
        "recommended_gpu": "A100-40GB",
        "min_vram_gb": 32,
        "recommended_batch_size": 1,
        "categories": ["reinforcement-learning", "grpo", "reasoning"],
        "difficulty": "advanced",
        "upstream_notebook_url": "https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Phi-4_(14B)_grpo.ipynb",
        "multi_gpu": False
    },

    # Audio models
    "whisper-large-v3": {
        "model_name": "Whisper Large V3",
        "launchable_name": "whisper-large-v3-stt",
        "recommended_gpu": "L4",
        "min_vram_gb": 16,
        "recommended_batch_size": 4,
        "categories": ["audio", "speech-to-text", "fine-tuning"],
        "difficulty": "intermediate",
        "upstream_notebook_url": "https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Whisper_Large_V3.ipynb",
        "multi_gpu": False
    },
    "sesame-csm-1b": {
        "model_name": "Sesame-CSM (1B)",
        "launchable_name": "sesame-csm-1b-tts",
        "recommended_gpu": "T4",
        "min_vram_gb": 12,
        "recommended_batch_size": 4,
        "categories": ["audio", "text-to-speech", "fine-tuning"],
        "difficulty": "intermediate",
        "upstream_notebook_url": "https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Sesame-CSM_(1B).ipynb",
        "multi_gpu": False
    },
    "orpheus-tts-3b": {
        "model_name": "Orpheus-TTS (3B)",
        "launchable_name": "orpheus-tts-3b",
        "recommended_gpu": "L4",
        "min_vram_gb": 16,
        "recommended_batch_size": 2,
        "categories": ["audio", "text-to-speech", "fine-tuning"],
        "difficulty": "intermediate",
        "upstream_notebook_url": "https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Orpheus-TTS_(3B).ipynb",
        "multi_gpu": False
    },
}

# Default configuration for unknown models
DEFAULT_CONFIG = {
    "model_name": "Unknown Model",
    "launchable_name": "unknown-model",
    "recommended_gpu": "L4",
    "min_vram_gb": 16,
    "recommended_batch_size": 2,
    "categories": ["fine-tuning"],
    "difficulty": "intermediate",
    "upstream_notebook_url": "#",
    "multi_gpu": False
}


def create_unique_default_config(notebook_name: str) -> Dict:
    """
    Create a unique default config based on filename.
    
    Args:
        notebook_name: Notebook filename
        
    Returns:
        Configuration dictionary
    """
    stem = Path(notebook_name).stem
    
    # Try to extract model name from patterns like "Gemma3_(4B)" or "Llama3_1_(8B)"
    match = re.search(r'([A-Za-z]+\d*(?:_\d+)?)\s*\((\d+[A-Z]*)\)', stem)
    if match:
        model_base = match.group(1).replace('_', ' ')
        model_size = match.group(2)
        model_name = f"{model_base} ({model_size})"
    else:
        # Fallback: clean up the filename
        model_name = stem.replace('_', ' ').replace('-', ' ').title()
    
    # Create slug from filename
    slug = re.sub(r'[()]', '', stem.lower())  # Remove parens
    slug = slug.replace('_', '-')              # Underscores to dashes
    slug = re.sub(r'-+', '-', slug)            # Multiple dashes to single
    
    # Remove common suffixes
    for suffix in ['-alpaca', '-conversational', '-inference', '-a100', '-grpo']:
        if slug.endswith(suffix):
            slug = slug[:-len(suffix)]
    
    return {
        "model_name": model_name,
        "launchable_name": slug,
        "recommended_gpu": "L4",
        "min_vram_gb": 16,
        "recommended_batch_size": 2,
        "categories": ["fine-tuning"],
        "difficulty": "intermediate",
        "upstream_notebook_url": f"https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/{stem}.ipynb",
        "multi_gpu": False
    }


def get_config_for_notebook(notebook_name: str) -> Dict:
    """
    Get configuration for a notebook by matching its name.
    
    Handles various naming patterns:
    - Gemma3_(4B).ipynb → gemma-3-4b
    - Llama3_1_(8B)-Alpaca.ipynb → llama-3.1-8b
    - Qwen2_5_(7B)-Alpaca.ipynb → qwen-2.5-7b

    Args:
        notebook_name: Name or path of the notebook

    Returns:
        Configuration dictionary
    """
    # Extract just the filename stem
    stem = Path(notebook_name).stem.lower()
    
    # Normalize: remove parentheses, replace underscores with dashes
    clean_name = re.sub(r'[()]', '', stem)     # Remove parens
    clean_name = clean_name.replace('_', '-')  # Underscores to dashes
    clean_name = re.sub(r'-+', '-', clean_name) # Multiple dashes to single
    
    # Remove common suffixes
    for suffix in ['-alpaca', '-conversational', '-inference', '-a100', '-grpo', '-vision']:
        if clean_name.endswith(suffix):
            clean_name = clean_name[:-len(suffix)]
            break
    
    # Try exact match first
    if clean_name in MODEL_CONFIGS:
        return MODEL_CONFIGS[clean_name].copy()
    
    # Try fuzzy matching with scoring
    best_match = None
    best_score = 0
    
    for config_key in MODEL_CONFIGS.keys():
        # Calculate similarity score
        if config_key in clean_name:
            # Config key is substring of cleaned name
            score = len(config_key)
            if score > best_score:
                best_score = score
                best_match = config_key
        elif clean_name in config_key:
            # Cleaned name is substring of config key
            score = len(clean_name)
            if score > best_score:
                best_score = score
                best_match = config_key
    
    # Only use match if it's reasonably good (at least 5 characters)
    if best_match and best_score >= 5:
        return MODEL_CONFIGS[best_match].copy()
    
    # No good match found - create unique config from filename
    return create_unique_default_config(notebook_name)

