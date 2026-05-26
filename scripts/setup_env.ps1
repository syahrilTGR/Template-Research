# Universal Research Template - Environment Setup Script (Windows)

Write-Host "--- 🎬 Starting Environment Setup ---" -ForegroundColor Cyan

# Define Venv Path (External to project for cleanliness)
$VENV_PATH = Join-Path $HOME "thesis_venv"
$PYTHON_VENV_EXE = Join-Path $VENV_PATH "Scripts\python.exe"

# 1. Check Python installation
Write-Host "[1/4] Checking Python..." -ForegroundColor Yellow
$PYTHON_CMD = "python"
if (Get-Command python -ErrorAction SilentlyContinue) {
    $pythonVersion = python --version
    Write-Host "Found $pythonVersion" -ForegroundColor Green
} elseif (Get-Command py -ErrorAction SilentlyContinue) {
    $PYTHON_CMD = "py"
    $pythonVersion = py -3 --version
    Write-Host "Found Python Launcher (py): $pythonVersion" -ForegroundColor Green
} elseif (Get-Command python3 -ErrorAction SilentlyContinue) {
    $PYTHON_CMD = "python3"
    $pythonVersion = python3 --version
    Write-Host "Found python3: $pythonVersion" -ForegroundColor Green
} else {
    Write-Host "Error: Python not found. Please install Python 3.9+ from python.org or Microsoft Store." -ForegroundColor Red
    exit 1
}

# 2. Setup Virtual Environment
Write-Host "[2/4] Setting up Virtual Environment in Home Directory..." -ForegroundColor Yellow
Write-Host "Target: $VENV_PATH" -ForegroundColor Cyan
if (-Not (Test-Path $VENV_PATH)) {
    if ($PYTHON_CMD -eq "py") {
        py -3 -m venv $VENV_PATH
    } else {
        & $PYTHON_CMD -m venv $VENV_PATH
    }
    Write-Host "Virtual environment created successfully." -ForegroundColor Green
} else {
    Write-Host "Virtual environment already exists at destination. Skipping creation." -ForegroundColor Cyan
}

# 3. Upgrade Pip & Install Requirements
Write-Host "[3/4] Installing dependencies from requirements.txt..." -ForegroundColor Yellow
& $PYTHON_VENV_EXE -m pip install --upgrade pip
& $PYTHON_VENV_EXE -m pip install -r requirements.txt

if ($LASTEXITCODE -eq 0) {
    Write-Host "All dependencies installed successfully." -ForegroundColor Green
} else {
    Write-Host "Error installing dependencies. Please check your internet connection or requirements.txt." -ForegroundColor Red
    exit 1
}

# 4. Record Venv Path for AI & Scripts
Write-Host "[4/4] Recording Venv path for AI integration..." -ForegroundColor Yellow
$CONFIG_PATH = "supportFiles/.venv_config.txt"
$PYTHON_VENV_EXE | Out-File -FilePath $CONFIG_PATH -Encoding utf8
Write-Host "Venv path recorded in $CONFIG_PATH" -ForegroundColor Green

# 4b. Auto-Update gemini.md (only if placeholder is still present)
$GEMINI_FILE = "gemini.md"
if (Test-Path $GEMINI_FILE) {
    $geminiContent = Get-Content $GEMINI_FILE -Raw
    if ($geminiContent -match [regex]::Escape("- **Default VENV:** [ISI_DISINI]")) {
        Write-Host "Updating venv information in $GEMINI_FILE..." -ForegroundColor Cyan
        $updatedContent = $geminiContent -replace [regex]::Escape("- **Default VENV:** [ISI_DISINI]"), "- **Default VENV:** $PYTHON_VENV_EXE"
        $updatedContent | Set-Content $GEMINI_FILE -Encoding utf8 -NoNewline
        Write-Host "gemini.md updated with $PYTHON_VENV_EXE" -ForegroundColor Green
    } else {
        Write-Host "gemini.md already configured (placeholder not found, skipping)." -ForegroundColor Cyan
    }
}

# 5. Success Message
Write-Host "`n--- ✅ Setup Complete! ---" -ForegroundColor Green
Write-Host "To activate the environment, run this command:" -ForegroundColor White
$activatePath = Join-Path $VENV_PATH "Scripts\Activate.ps1"
Write-Host "$activatePath" -ForegroundColor Cyan
Write-Host "`nHappy Researching! 🚀" -ForegroundColor White
