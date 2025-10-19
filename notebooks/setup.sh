#!/bin/bash

# SmartCart AI - Notebook Quick Start Script
# This script helps you set up the environment for training models

echo "========================================"
echo "  SmartCart AI - Notebook Setup"
echo "========================================"
echo ""

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
GRAY='\033[0;37m'
NC='\033[0m' # No Color

# Check Python installation
echo -e "${YELLOW}Checking Python installation...${NC}"
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version)
    echo -e "${GREEN}✓ Found: $PYTHON_VERSION${NC}"
    PYTHON_CMD=python3
elif command -v python &> /dev/null; then
    PYTHON_VERSION=$(python --version)
    echo -e "${GREEN}✓ Found: $PYTHON_VERSION${NC}"
    PYTHON_CMD=python
else
    echo -e "${RED}✗ Python not found! Please install Python 3.8+ first.${NC}"
    exit 1
fi

echo ""

# Create virtual environment
echo -e "${YELLOW}Creating virtual environment...${NC}"
if [ -d "venv" ]; then
    echo -e "${GREEN}✓ Virtual environment already exists${NC}"
else
    $PYTHON_CMD -m venv venv
    echo -e "${GREEN}✓ Virtual environment created${NC}"
fi

echo ""

# Activate virtual environment
echo -e "${YELLOW}Activating virtual environment...${NC}"
source venv/bin/activate
echo -e "${GREEN}✓ Virtual environment activated${NC}"

echo ""

# Install dependencies
echo -e "${YELLOW}Installing dependencies...${NC}"
echo -e "${GRAY}This may take several minutes...${NC}"
pip install -r requirements.txt --upgrade --quiet

if [ $? -eq 0 ]; then
    echo -e "${GREEN}✓ Dependencies installed successfully${NC}"
else
    echo -e "${RED}✗ Error installing dependencies${NC}"
    exit 1
fi

echo ""

# Check for CUDA (GPU support)
echo -e "${YELLOW}Checking for GPU support...${NC}"
CUDA_CHECK=$($PYTHON_CMD -c "import torch; print(torch.cuda.is_available())" 2>&1)
if [ "$CUDA_CHECK" = "True" ]; then
    echo -e "${GREEN}✓ GPU support available (CUDA)${NC}"
    GPU_NAME=$($PYTHON_CMD -c "import torch; print(torch.cuda.get_device_name(0))" 2>&1)
    echo -e "${CYAN}  GPU: $GPU_NAME${NC}"
else
    echo -e "${YELLOW}ℹ GPU not available - will use CPU (slower)${NC}"
    echo -e "${GRAY}  Tip: Install CUDA-enabled PyTorch for faster training${NC}"
fi

echo ""

# Create necessary directories
echo -e "${YELLOW}Creating directories...${NC}"
for dir in outputs checkpoints; do
    if [ ! -d "$dir" ]; then
        mkdir -p "$dir"
        echo -e "${GREEN}✓ Created $dir/${NC}"
    else
        echo -e "${GREEN}✓ $dir/ already exists${NC}"
    fi
done

echo ""

# Check for API keys
echo -e "${YELLOW}Checking configuration...${NC}"
ENV_FILE="../.env"
if [ -f "$ENV_FILE" ]; then
    echo -e "${GREEN}✓ Found .env file${NC}"
    
    # Check for specific keys
    if grep -q "PINECONE_API_KEY" "$ENV_FILE"; then
        echo -e "${GREEN}  ✓ PINECONE_API_KEY found${NC}"
    else
        echo -e "${YELLOW}  ℹ PINECONE_API_KEY not found (optional)${NC}"
    fi
    
    if grep -q "OPENAI_API_KEY" "$ENV_FILE"; then
        echo -e "${GREEN}  ✓ OPENAI_API_KEY found${NC}"
    else
        echo -e "${YELLOW}  ℹ OPENAI_API_KEY not found (optional)${NC}"
    fi
else
    echo -e "${YELLOW}ℹ No .env file found${NC}"
    echo -e "${GRAY}  Tip: Create ../.env for API keys (optional)${NC}"
fi

echo ""
echo -e "${CYAN}========================================${NC}"
echo -e "${GREEN}  Setup Complete! 🎉${NC}"
echo -e "${CYAN}========================================${NC}"
echo ""
echo -e "${YELLOW}Next steps:${NC}"
echo -e "${NC}  1. Ensure your dataset is at: ../intern_data_ikarus.csv${NC}"
echo -e "${NC}  2. Start Jupyter: jupyter notebook${NC}"
echo -e "${NC}  3. Open: model_training.ipynb${NC}"
echo -e "${NC}  4. Run all cells sequentially${NC}"
echo ""
echo -e "${GRAY}For help, see: README.md${NC}"
echo ""
