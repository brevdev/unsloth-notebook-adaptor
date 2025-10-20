#!/bin/bash
set -e

echo "=================================================="
echo "Unsloth to Brev Adapter - Quick Start"
echo "=================================================="
echo ""

# Check Python version
echo "[1/5] Checking Python version..."
python3 --version || { echo "Error: Python 3 not found"; exit 1; }
echo "✓ Python 3 found"
echo ""

# Install dependencies
echo "[2/5] Installing dependencies..."
pip install -r requirements.txt -q
echo "✓ Dependencies installed"
echo ""

# Run tests
echo "[3/5] Running tests..."
pytest tests/ -v --tb=short
echo "✓ All tests passed"
echo ""

# Clone Unsloth notebooks (if not present)
echo "[4/5] Checking for Unsloth notebooks..."
if [ ! -d "unsloth-notebooks" ]; then
    echo "Cloning Unsloth notebooks repository..."
    git clone https://github.com/unslothai/notebooks.git unsloth-notebooks
    echo "✓ Unsloth notebooks cloned"
else
    echo "✓ Unsloth notebooks already present"
fi
echo ""

# Convert a sample notebook
echo "[5/5] Converting sample notebook..."
if [ -f "unsloth-notebooks/nb/Llama_3.1_(8B).ipynb" ]; then
    python3 scripts/convert_notebook.py \
        --source unsloth-notebooks/nb \
        --output converted \
        --notebooks "Llama_3.1_(8B).ipynb"
    echo "✓ Sample notebook converted"
    echo ""
    echo "Check the output in: converted/llama-3.1-8b-fine-tuning/"
else
    echo "Sample notebook not found, skipping conversion test"
fi

echo ""
echo "=================================================="
echo "Setup Complete! 🚀"
echo "=================================================="
echo ""
echo "Next steps:"
echo "  1. View converted notebooks: ls converted/"
echo "  2. Run full conversion: python3 scripts/convert_notebook.py --source unsloth-notebooks/nb --output converted"
echo "  3. Generate metadata: python3 scripts/generate_metadata.py --notebooks-dir converted --output metadata/launchables.json"
echo ""
echo "For more information, see README.md"

