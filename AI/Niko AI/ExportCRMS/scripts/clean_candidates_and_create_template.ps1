# PowerShell script to clean candidates JSON by removing empty/null placeholders
# and create a JSON lookup template of all possible candidate fields
# Script is in scripts/ folder, so reference parent directory

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$parentDir = Split-Path -Parent $scriptDir
$inputFile = Join-Path $parentDir "Candidates_JSON_Clusters\Candidates_cluster_0001.json"
$outputFile = Join-Path $parentDir "Candidates_JSON_Clusters\Candidates_cluster_0001_cleaned.json"
$templateFile = Join-Path $parentDir "Candidates_JSON_Clusters\candidate_fields_template.json"

Write-Host "Reading file: $inputFile"

try {
    # Read and parse JSON
    $content = Get-Content -Path $inputFile -Raw -Encoding UTF8
    $candidates = $content | ConvertFrom-Json
    
    Write-Host "Found $($candidates.Count) candidates"
    
    # Function to check if value is empty
    function Is-EmptyValue {
        param($value)
        if ($null -eq $value) { return $true }
        if ($value -is [string] -and $value.Trim() -eq "") { return $true }
        if ($value -is [System.Collections.IList] -and $value.Count -eq 0) { return $true }
        if ($value -is [System.Collections.IDictionary] -and $value.Count -eq 0) { return $true }
        return $false
    }
    
    # Function to clean object recursively
    function Clean-Object {
        param($obj)
        
        if ($obj -is [PSCustomObject]) {
            $cleaned = @{}
            foreach ($prop in $obj.PSObject.Properties) {
                $cleanedValue = Clean-Object -obj $prop.Value
                if (-not (Is-EmptyValue -value $cleanedValue)) {
                    $cleaned[$prop.Name] = $cleanedValue
                }
            }
            return $cleaned
        }
        elseif ($obj -is [System.Collections.IList]) {
            $cleaned = @()
            foreach ($item in $obj) {
                $cleanedItem = Clean-Object -obj $item
                if (-not (Is-EmptyValue -value $cleanedItem)) {
                    $cleaned += $cleanedItem
                }
            }
            return $cleaned
        }
        else {
            return $obj
        }
    }
    
    # Extract template from first few candidates
    Write-Host "Extracting field template from candidates..."
    $template = @{}
    $sampleSize = [Math]::Min(5, $candidates.Count)
    
    for ($i = 0; $i -lt $sampleSize; $i++) {
        $candidate = $candidates[$i]
        $candidateObj = $candidate | ConvertTo-Json -Depth 100 | ConvertFrom-Json
        
        # Extract all fields
        foreach ($prop in $candidateObj.PSObject.Properties) {
            $fieldName = $prop.Name
            if (-not $template.ContainsKey($fieldName)) {
                $fieldInfo = @{
                    type = $prop.TypeNameOfValue
                    description = "Field: $fieldName"
                }
                
                # Determine if it's an object, array, or primitive
                if ($prop.Value -is [PSCustomObject]) {
                    $fieldInfo.type = "object"
                    $fieldInfo.fields = @{}
                }
                elseif ($prop.Value -is [System.Collections.IList]) {
                    $fieldInfo.type = "array"
                    if ($prop.Value.Count -gt 0) {
                        $fieldInfo.item_type = $prop.Value[0].GetType().Name
                    }
                }
                else {
                    $fieldInfo.example = $prop.Value
                }
                
                $template[$fieldName] = $fieldInfo
            }
        }
    }
    
    # Create template output
    $templateOutput = @{
        candidate_fields_template = $template
        total_fields = $template.Count
        description = "JSON lookup template showing all possible candidate fields with types and descriptions"
    } | ConvertTo-Json -Depth 10
    
    Write-Host "Creating template file: $templateFile"
    $templateOutput | Set-Content -Path $templateFile -Encoding UTF8
    Write-Host "Template created with $($template.Count) fields"
    
    # Clean candidates
    Write-Host "Cleaning candidates (removing empty/null values)..."
    $cleanedCandidates = @()
    
    for ($i = 0; $i -lt $candidates.Count; $i++) {
        $candidate = $candidates[$i]
        $cleaned = Clean-Object -obj $candidate
        $cleanedCandidates += $cleaned
        
        if (($i + 1) % 100 -eq 0) {
            Write-Host "Processed $($i + 1)/$($candidates.Count) candidates"
        }
    }
    
    # Save cleaned candidates
    Write-Host "Saving cleaned candidates to: $outputFile"
    $cleanedCandidates | ConvertTo-Json -Depth 100 | Set-Content -Path $outputFile -Encoding UTF8
    
    Write-Host "`nProcessing complete!"
    Write-Host "  - Cleaned $($cleanedCandidates.Count) candidates"
    Write-Host "  - Template saved to: $templateFile"
}
catch {
    Write-Host "Error: $_" -ForegroundColor Red
    Write-Host $_.Exception.Message
    exit 1
}

