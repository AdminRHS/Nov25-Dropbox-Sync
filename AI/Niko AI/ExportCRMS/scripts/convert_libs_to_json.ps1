# PowerShell script to convert Libs markdown files to JSON
# This script calls the Python conversion script

# Get the directory where this script is located
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$pythonScript = Join-Path $scriptDir "convert_libs_to_json.py"

# Check if Python is available
$pythonCmd = Get-Command python -ErrorAction SilentlyContinue
if (-not $pythonCmd) {
    Write-Host "Error: Python is not installed or not in PATH" -ForegroundColor Red
    exit 1
}

# Run the Python script
Write-Host "Running conversion script..." -ForegroundColor Cyan
python $pythonScript

# Check if the script ran successfully
if ($LASTEXITCODE -eq 0 -or $null -eq $LASTEXITCODE) {
    Write-Host "`nConversion completed successfully!" -ForegroundColor Green
} else {
    Write-Host "`nConversion failed with exit code: $LASTEXITCODE" -ForegroundColor Red
    exit $LASTEXITCODE
}
