# SmartCart AI - Notebook Quick Start Script
# This script helps you set up the environment for training models

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  SmartCart AI - Notebook Setup" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Check Python installation
Write-Host "Checking Python installation..." -ForegroundColor Yellow
try {
    $pythonVersion = python --version 2>&1
    Write-Host "✓ Found: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "✗ Python not found! Please install Python 3.8+ first." -ForegroundColor Red
    exit 1
}

Write-Host ""

# Create virtual environment
Write-Host "Creating virtual environment..." -ForegroundColor Yellow
if (Test-Path "venv") {
    Write-Host "✓ Virtual environment already exists" -ForegroundColor Green
} else {
    python -m venv venv
    Write-Host "✓ Virtual environment created" -ForegroundColor Green
}

Write-Host ""

# Activate virtual environment
Write-Host "Activating virtual environment..." -ForegroundColor Yellow
& .\venv\Scripts\Activate.ps1
Write-Host "✓ Virtual environment activated" -ForegroundColor Green

Write-Host ""

# Install dependencies
Write-Host "Installing dependencies..." -ForegroundColor Yellow
Write-Host "This may take several minutes..." -ForegroundColor Gray
pip install -r requirements.txt --upgrade --quiet

if ($LASTEXITCODE -eq 0) {
    Write-Host "✓ Dependencies installed successfully" -ForegroundColor Green
} else {
    Write-Host "✗ Error installing dependencies" -ForegroundColor Red
    exit 1
}

Write-Host ""

# Check for CUDA (GPU support)
Write-Host "Checking for GPU support..." -ForegroundColor Yellow
try {
    $cudaCheck = python -c "import torch; print(torch.cuda.is_available())" 2>&1
    if ($cudaCheck -eq "True") {
        Write-Host "✓ GPU support available (CUDA)" -ForegroundColor Green
        $gpuName = python -c "import torch; print(torch.cuda.get_device_name(0))" 2>&1
        Write-Host "  GPU: $gpuName" -ForegroundColor Cyan
    } else {
        Write-Host "ℹ GPU not available - will use CPU (slower)" -ForegroundColor Yellow
        Write-Host "  Tip: Install CUDA-enabled PyTorch for faster training" -ForegroundColor Gray
    }
} catch {
    Write-Host "ℹ Could not check GPU status" -ForegroundColor Yellow
}

Write-Host ""

# Create necessary directories
Write-Host "Creating directories..." -ForegroundColor Yellow
$dirs = @("outputs", "checkpoints")
foreach ($dir in $dirs) {
    if (!(Test-Path $dir)) {
        New-Item -ItemType Directory -Path $dir | Out-Null
        Write-Host "✓ Created $dir/" -ForegroundColor Green
    } else {
        Write-Host "✓ $dir/ already exists" -ForegroundColor Green
    }
}

Write-Host ""

# Check for API keys
Write-Host "Checking configuration..." -ForegroundColor Yellow
$envFile = "..\\.env"
if (Test-Path $envFile) {
    Write-Host "✓ Found .env file" -ForegroundColor Green
    
    # Check for specific keys
    $envContent = Get-Content $envFile -Raw
    
    if ($envContent -match "PINECONE_API_KEY") {
        Write-Host "  ✓ PINECONE_API_KEY found" -ForegroundColor Green
    } else {
        Write-Host "  ℹ PINECONE_API_KEY not found (optional)" -ForegroundColor Yellow
    }
    
    if ($envContent -match "OPENAI_API_KEY") {
        Write-Host "  ✓ OPENAI_API_KEY found" -ForegroundColor Green
    } else {
        Write-Host "  ℹ OPENAI_API_KEY not found (optional)" -ForegroundColor Yellow
    }
} else {
    Write-Host "ℹ No .env file found" -ForegroundColor Yellow
    Write-Host "  Tip: Create ../.env for API keys (optional)" -ForegroundColor Gray
}

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  Setup Complete! 🎉" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Next steps:" -ForegroundColor Yellow
Write-Host "  1. Ensure your dataset is at: ../intern_data_ikarus.csv" -ForegroundColor White
Write-Host "  2. Start Jupyter: jupyter notebook" -ForegroundColor White
Write-Host "  3. Open: model_training.ipynb" -ForegroundColor White
Write-Host "  4. Run all cells sequentially" -ForegroundColor White
Write-Host ""
Write-Host "For help, see: README.md" -ForegroundColor Gray
Write-Host ""
