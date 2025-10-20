# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-10-20

### Added
- Initial release of Unsloth to Brev Adapter
- Automated daily sync with unslothai/notebooks repository
- Intelligent conversion of Colab notebooks to Brev format
- Support for 25+ models (LLMs, VLMs, Audio, GRPO)
- Comprehensive conversion features:
  - Installation conversion (colab-new → conda)
  - Magic commands → subprocess calls
  - Storage adaptation (Google Drive → /workspace)
  - GPU configuration (device_map="auto")
  - Batch size optimization
- Companion file generation:
  - requirements.txt
  - setup.sh
  - docker-compose.yml
  - README.md
  - .brevconfig.json
- GitHub Actions workflows:
  - Daily sync and convert (6 AM UTC)
  - Test suite on PR/push
- Auto-generated Launchables table in README
- Comprehensive test suite (23+ tests)
- Full documentation:
  - README.md
  - CONTRIBUTING.md
  - VERIFICATION.md
  - BUILD_SUMMARY.md
- CLI scripts:
  - convert_notebook.py
  - compare_notebooks.py
  - generate_metadata.py
  - generate_readme_table.py
  - create_summary.py

### Supported Models
- **LLMs**: gpt-oss (20B, 120B), Llama 3.1-3.2, Gemma 3, Qwen3, Phi-4
- **Vision Models**: Llama 3.2 Vision, Qwen3-VL, Gemma 3 Vision
- **Audio Models**: Whisper Large V3, Orpheus-TTS, Sesame-CSM
- **GRPO/RL**: All major models with reinforcement learning support

[1.0.0]: https://github.com/brevdev/unsloth-notebook-adaptor/releases/tag/v1.0.0

