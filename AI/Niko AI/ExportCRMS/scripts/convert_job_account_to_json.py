"""
Script to convert Job_Account_prod.md to proper JSON format.
The file contains JSON data but has a .md extension.
"""
import json
from pathlib import Path


def convert_job_account_to_json(input_file, output_file=None):
    """
    Convert Job_Account_prod.md file to JSON format.

    Args:
        input_file (str): Path to input markdown file containing JSON
        output_file (str): Optional path to output JSON file. 
                          If None, will use same name with .json extension
    """
    input_path = Path(input_file)
    
    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_file}")
    
    # Determine output file path
    if output_file is None:
        # Use same directory, change extension to .json
        output_path = input_path.parent / f"{input_path.stem}.json"
    else:
        output_path = Path(output_file)
    
    print(f"Reading file: {input_path}")
    
    # Read the markdown file
    with open(input_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Parse the JSON content
    try:
        data = json.loads(content.strip())
        print(f"Successfully parsed JSON data")
        
        # Check structure
        if isinstance(data, dict):
            if 'success' in data and 'data' in data:
                print(f"Found {len(data.get('data', []))} job accounts")
            else:
                print(f"JSON structure: {list(data.keys())}")
        elif isinstance(data, list):
            print(f"Found {len(data)} items in array")
        
    except json.JSONDecodeError as e:
        raise ValueError(f"Error parsing JSON: {e}")
    
    # Create output directory if it doesn't exist
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Write JSON file with proper formatting
    print(f"Writing JSON file: {output_path}")
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print(f"\n{'='*60}")
    print(f"Conversion complete!")
    print(f"  Input:  {input_path}")
    print(f"  Output: {output_path}")
    print(f"{'='*60}")


if __name__ == "__main__":
    # Set paths - scripts are in scripts/ folder, so go up one level
    base_dir = Path(__file__).parent.parent
    input_file = base_dir / "Job_Account_prod.md"
    output_file = base_dir / "Job_Account_prod.json"
    
    print(f"Converting Job_Account_prod.md to JSON format")
    print(f"Base directory: {base_dir}")
    
    convert_job_account_to_json(str(input_file), str(output_file))

