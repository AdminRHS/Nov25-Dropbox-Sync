# PowerShell script to convert Candidates_Last_1000_old_crm.md to JSON format clusters
# Each cluster file contains 1,000 candidates
# Script is in scripts/ folder, so reference parent directory

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$parentDir = Split-Path -Parent $scriptDir
$inputFile = Join-Path $parentDir "Candidates_Last_1000_old_crm.md"
$outputDir = Join-Path $parentDir "Candidates_JSON_Clusters"
$candidatesPerFile = 1000

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
            # Try to find data array in a wrapper object
            if ($content -match '"data"\s*:\s*\{') {
                $startIdx = $content.IndexOf('{', $content.IndexOf('"data"'))
            }
            else {
                throw "Could not find JSON array start"
            }
        }
        
        # Find matching closing bracket
        $bracketCount = 0
        $endIdx = $startIdx
        for ($i = $startIdx; $i -lt $content.Length; $i++) {
            if ($content[$i] -eq '{') {
                $bracketCount++
            }
            elseif ($content[$i] -eq '}') {
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
    # The file structure is: {"message": "success", "data": {"data": [...candidates...], "pagination": {...}}}
    if ($data -is [PSCustomObject]) {
        # If it's an object, look for nested data property
        if ($data.PSObject.Properties.Name -contains 'data') {
            $nestedData = $data.data
            if ($nestedData -is [PSCustomObject] -and $nestedData.PSObject.Properties.Name -contains 'data') {
                $candidates = $nestedData.data
            }
            elseif ($nestedData -is [Array]) {
                $candidates = $nestedData
            }
            else {
                # Get first property value
                $prop = $nestedData.PSObject.Properties | Select-Object -First 1
                $candidates = $prop.Value
            }
        }
        elseif ($data.PSObject.Properties.Name -contains 'candidates') {
            $candidates = $data.candidates
        }
        else {
            # Get first property value
            $prop = $data.PSObject.Properties | Select-Object -First 1
            $candidates = $prop.Value
        }
    }
    elseif ($data -is [Array]) {
        $candidates = $data
    }
    else {
        throw "Unexpected data structure"
    }
    
    Write-Host "Found $($candidates.Count) candidates"
    
    # Create output directory
    if (-not (Test-Path $outputDir)) {
        New-Item -ItemType Directory -Path $outputDir | Out-Null
    }
    
    # Split candidates into clusters
    $numFiles = [Math]::Ceiling($candidates.Count / $candidatesPerFile)
    
    for ($i = 0; $i -lt $numFiles; $i++) {
        $startIdx = $i * $candidatesPerFile
        $endIdx = [Math]::Min($startIdx + $candidatesPerFile, $candidates.Count)
        $cluster = $candidates[$startIdx..($endIdx - 1)]
        
        # Create output filename
        $fileNum = ($i + 1).ToString('0000')
        $outputFile = Join-Path $outputDir "Candidates_cluster_$fileNum.json"
        
        # Convert to JSON and write
        $cluster | ConvertTo-Json -Depth 100 | Set-Content -Path $outputFile -Encoding UTF8
        
        Write-Host "Created $outputFile with $($cluster.Count) candidates (candidates $($startIdx+1)-$endIdx)"
    }
    
    Write-Host "`nConversion complete! Created $numFiles JSON files in $outputDir"
}
catch {
    Write-Host "Error: $_" -ForegroundColor Red
    Write-Host $_.Exception.Message
    exit 1
}

