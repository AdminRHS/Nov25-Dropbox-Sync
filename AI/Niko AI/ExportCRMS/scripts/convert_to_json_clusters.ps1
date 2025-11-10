# PowerShell script to convert LeadAccount_old_crm.md to JSON format clusters
# Each cluster file contains 10 accounts
# Script is in scripts/ folder, so reference parent directory

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$parentDir = Split-Path -Parent $scriptDir
$inputFile = Join-Path $parentDir "LeadAccount_old_crm.md"
$outputDir = Join-Path $parentDir "LeadAccount_JSON_Clusters"
$accountsPerFile = 10

Write-Host "Reading file: $inputFile"

# Read the file content
$content = Get-Content -Path $inputFile -Raw -Encoding UTF8

# Try to parse as JSON
try {
    # Try to parse the entire content first
    try {
        $data = $content | ConvertFrom-Json
    }
    catch {
        # If that fails, try to find and extract JSON array
        Write-Host "Direct parse failed, trying to extract JSON array..."
        
        # Find the JSON array start
        $startIdx = $content.IndexOf('[')
        if ($startIdx -eq -1) {
            # Try to find accounts array in a wrapper object
            if ($content -match '"accounts"\s*:\s*\[') {
                $startIdx = $content.IndexOf('[', $content.IndexOf('"accounts"'))
            }
            else {
                throw "Could not find JSON array start"
            }
        }
        
        # Find matching closing bracket
        $bracketCount = 0
        $endIdx = $startIdx
        for ($i = $startIdx; $i -lt $content.Length; $i++) {
            if ($content[$i] -eq '[') {
                $bracketCount++
            }
            elseif ($content[$i] -eq ']') {
                $bracketCount--
                if ($bracketCount -eq 0) {
                    $endIdx = $i + 1
                    break
                }
            }
        }
        
        $jsonStr = $content.Substring($startIdx, $endIdx - $startIdx)
        $data = $jsonStr | ConvertFrom-Json
    }
    
    # Handle different data structures
    if ($data -is [PSCustomObject]) {
        # If it's an object, look for accounts property
        if ($data.PSObject.Properties.Name -contains 'accounts') {
            $accounts = $data.accounts
        }
        elseif ($data.PSObject.Properties.Name -contains 'data') {
            $accounts = $data.data
        }
        else {
            # Get first property value
            $prop = $data.PSObject.Properties | Select-Object -First 1
            $accounts = $prop.Value
        }
    }
    elseif ($data -is [Array]) {
        $accounts = $data
    }
    else {
        throw "Unexpected data structure"
    }
    
    Write-Host "Found $($accounts.Count) accounts"
    
    # Create output directory
    if (-not (Test-Path $outputDir)) {
        New-Item -ItemType Directory -Path $outputDir | Out-Null
    }
    
    # Split accounts into clusters
    $numFiles = [Math]::Ceiling($accounts.Count / $accountsPerFile)
    
    for ($i = 0; $i -lt $numFiles; $i++) {
        $startIdx = $i * $accountsPerFile
        $endIdx = [Math]::Min($startIdx + $accountsPerFile, $accounts.Count)
        $cluster = $accounts[$startIdx..($endIdx - 1)]
        
        # Create output filename
        $fileNum = ($i + 1).ToString('0000')
        $outputFile = Join-Path $outputDir "LeadAccount_cluster_$fileNum.json"
        
        # Convert to JSON and write
        $cluster | ConvertTo-Json -Depth 100 | Set-Content -Path $outputFile -Encoding UTF8
        
        Write-Host "Created $outputFile with $($cluster.Count) accounts (accounts $($startIdx+1)-$endIdx)"
    }
    
    Write-Host "`nConversion complete! Created $numFiles JSON files in $outputDir"
}
catch {
    Write-Host "Error: $_" -ForegroundColor Red
    Write-Host $_.Exception.Message
    exit 1
}

