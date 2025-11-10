# PowerShell script to convert Job_Account_prod.md to JSON format
# This script calls the Python conversion script

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$baseDir = Split-Path -Parent $scriptDir
$pythonScript = Join-Path $scriptDir "convert_job_account_to_json.py"

Write-Host "Converting Job_Account_prod.md to JSON format..." -ForegroundColor Cyan
Write-Host "Base directory: $baseDir" -ForegroundColor Gray

# Check if Python is available
try {
    $pythonVersion = python --version 2>&1
    Write-Host "Using Python: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "Error: Python is not installed or not in PATH" -ForegroundColor Red
    exit 1
}

# Run the Python script
python $pythonScript

if ($LASTEXITCODE -eq 0) {
    Write-Host "`nConversion completed successfully!" -ForegroundColor Green
} else {
    Write-Host "`nConversion failed with exit code: $LASTEXITCODE" -ForegroundColor Red
    exit $LASTEXITCODE
}

