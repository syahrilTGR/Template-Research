# setup_docx_infra.ps1
# Automate docx library installation and NODE_PATH configuration for Global NPM usage.

Write-Host "--- DOCX Infrastructure Setup ---" -ForegroundColor Cyan

# 1. Check for Global docx
Write-Host "[1/2] Checking global 'docx' library..."
$npmRoot = npm root -g
$docxPath = Join-Path $npmRoot "docx"

if (-not (Test-Path $docxPath)) {
    Write-Host "-> 'docx' not found globally. Installing..." -ForegroundColor Yellow
    npm install -g docx
} else {
    Write-Host "-> 'docx' is already installed globally at $docxPath" -ForegroundColor Green
}

# 2. Check and Set NODE_PATH
Write-Host "[2/2] Checking NODE_PATH environment variable..."
$currentNodePath = [System.Environment]::GetEnvironmentVariable("NODE_PATH", "User")

if ($currentNodePath -notlike "*$npmRoot*") {
    Write-Host "-> NODE_PATH is missing or incorrect. Setting it to: $npmRoot" -ForegroundColor Yellow
    # Append if something else exists, or just set if empty
    if ($null -eq $currentNodePath -or $currentNodePath -eq "") {
        [System.Environment]::SetEnvironmentVariable("NODE_PATH", $npmRoot, "User")
    } else {
        $newNodePath = "$currentNodePath;$npmRoot"
        [System.Environment]::SetEnvironmentVariable("NODE_PATH", $newNodePath, "User")
    }
    Write-Host "-> NODE_PATH updated globally via setx (Environment Variable)." -ForegroundColor Green
    Write-Host "-> IMPORTANT: You may need to restart your terminal/IDE for changes to reflect in standard shells." -ForegroundColor Green
} else {
    Write-Host "-> NODE_PATH is already correctly configured." -ForegroundColor Green
}

Write-Host "--- Setup Complete ---" -ForegroundColor Cyan
