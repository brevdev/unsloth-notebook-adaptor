#!/bin/bash
set -e

echo "=========================================="
echo "Test Conversion - Small Sample"
echo "=========================================="
echo ""

# Step 1: Clone Unsloth notebooks if not present
if [ ! -d "unsloth-notebooks" ]; then
    echo "[1/6] Cloning Unsloth notebooks repository..."
    git clone https://github.com/unslothai/notebooks.git unsloth-notebooks
    echo "✓ Cloned successfully"
else
    echo "[1/6] Unsloth notebooks already present"
    echo "✓ Ready to convert"
fi
echo ""

# Step 2: Create/activate virtual environment and install dependencies
echo "[2/6] Setting up virtual environment..."
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
    echo "✓ Virtual environment created"
fi

echo "Activating virtual environment..."
source venv/bin/activate

echo "Installing dependencies..."
pip install -q -r requirements.txt
echo "✓ Dependencies installed"
echo ""

# Step 3: Convert just 3 test notebooks (using venv Python)
echo "[3/6] Converting 3 test notebooks..."
echo ""
echo "Converting:"
echo "  1. Gemma 3 (4B) - Text generation"
echo "  2. Gemma 3 (4B) Vision - Multimodal"
echo "  3. Gemma 3N (4B) Audio - Text-to-speech"
echo ""

python3 scripts/convert_notebook.py \
    --source unsloth-notebooks/nb \
    --output converted \
    --notebooks \
        "Gemma3_(4B).ipynb" \
        "Gemma3_(4B)-Vision.ipynb" \
        "Gemma3N_(4B)-Audio.ipynb"

echo ""

# Step 4: Generate metadata
echo "[4/6] Generating metadata..."
python3 scripts/generate_metadata.py \
    --notebooks-dir converted \
    --output metadata/launchables.json

echo ""

# Step 5: Update README with table
echo "[5/6] Updating README with launchables table..."
python3 scripts/generate_readme_table.py \
    --metadata-path metadata/launchables.json \
    --readme-path README.md

echo ""

# Step 6: Show summary
echo "[6/6] Test conversion summary..."
python3 scripts/create_summary.py metadata/launchables.json

echo ""
echo "=========================================="
echo "Test Conversion Complete! 🎉"
echo "=========================================="
echo ""
echo "Converted notebooks:"
ls -1 converted/
echo ""
echo "To review:"
echo "  cd converted/llama-3.1-8b-fine-tuning"
echo "  cat README.md"
echo ""
echo "To convert all notebooks:"
echo "  source venv/bin/activate"
echo "  python3 scripts/convert_notebook.py --source unsloth-notebooks/nb --output converted"
echo ""
echo "Note: Virtual environment is in ./venv/"
echo ""

