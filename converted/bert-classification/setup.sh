#!/bin/bash
set -e

echo "=========================================="
echo "Setting up Bert Classification Environment"
echo "=========================================="

# Update system packages
echo "[1/5] Updating system packages..."
apt-get update -qq
apt-get install -y -qq git wget curl

# Install Python requirements
echo "[2/5] Installing Python requirements..."
pip install --upgrade pip -q
pip install -r requirements.txt -q

# Install Unsloth with conda variant
echo "[3/5] Installing Unsloth (conda variant)..."
pip install "unsloth[conda] @ git+https://github.com/unslothai/unsloth.git" -q

# Verify installations
echo "[4/5] Verifying installations..."
python -c "import torch; print(f'PyTorch: {torch.__version__}')"
python -c "import transformers; print(f'Transformers: {transformers.__version__}')"
python -c "from unsloth import FastLanguageModel; print('Unsloth: OK')"

# Create workspace directories
echo "[5/5] Creating workspace directories..."
mkdir -p /workspace/models
mkdir -p /workspace/outputs
mkdir -p /workspace/checkpoints
mkdir -p /workspace/datasets

echo "=========================================="
echo "Setup complete! 🚀"
echo "=========================================="
