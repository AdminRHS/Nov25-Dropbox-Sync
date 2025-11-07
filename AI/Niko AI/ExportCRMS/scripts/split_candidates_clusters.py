"""
Script to convert Candidates_Last_1000_old_crm.md to JSON format clusters.
Each cluster file contains 1,000 candidates.
"""
import json
import os
from pathlib import Path


def convert_candidates_to_json_clusters(input_file, output_dir, candidates_per_file=1000):
    """
    Convert markdown file containing JSON data to multiple JSON files.
    
    Args:
        input_file (str): Path to input markdown file
        output_dir (str): Directory to save output JSON files
        candidates_per_file (int): Number of candidates per JSON file (default: 1000)
    """
    # Read the markdown file
    print(f"Reading file: {input_file}")
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Try to parse as JSON - the file appears to contain JSON data
    # First, try to find the JSON array in the content
    try:
        # If the content starts with JSON, parse it directly
        if content.strip().startswith('[') or content.strip().startswith('{'):
            # Try to find the candidates array
            if '"data"' in content or 'data' in content:
                # Parse entire content as JSON
                data = json.loads(content)
            else:
                # Parse entire content
                data = json.loads(content)
        else:
            # Try to extract JSON from markdown
            # Look for JSON code blocks or inline JSON
            if '```json' in content:
                start = content.find('```json') + 7
                end = content.find('```', start)
                json_str = content[start:end].strip()
                data = json.loads(json_str)
            elif '```' in content:
                start = content.find('```') + 3
                end = content.find('```', start)
                json_str = content[start:end].strip()
                data = json.loads(json_str)
            else:
                # Try to find JSON array directly
                start_idx = content.find('[')
                if start_idx != -1:
                    bracket_count = 0
                    end_idx = start_idx
                    for i in range(start_idx, len(content)):
                        if content[i] == '[':
                            bracket_count += 1
                        elif content[i] == ']':
                            bracket_count -= 1
                            if bracket_count == 0:
                                end_idx = i + 1
                                break
                    json_str = content[start_idx:end_idx]
                    data = json.loads(json_str)
                else:
                    raise ValueError("Could not find JSON data in file")
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}")
        # Try alternative parsing - maybe it's a single line
        try:
            data = json.loads(content.strip())
        except:
            raise ValueError(f"Could not parse JSON from file: {e}")
    
    # Handle different data structures
    # The file structure is: {"message": "success", "data": {"data": [...candidates...], "pagination": {...}}}
    if isinstance(data, dict):
        # If it's a dict, look for nested 'data' key
        if 'data' in data and isinstance(data['data'], dict):
            if 'data' in data['data']:
                candidates = data['data']['data']
            else:
                # Assume the dict values contain the candidates
                candidates = list(data['data'].values())[0] if data['data'] else []
        elif 'data' in data:
            candidates = data['data']
        elif 'candidates' in data:
            candidates = data['candidates']
        else:
            # Assume the dict values contain the candidates
            candidates = list(data.values())[0] if data else []
    elif isinstance(data, list):
        candidates = data
    else:
        raise ValueError("Unexpected data structure")
    
    print(f"Found {len(candidates)} candidates")
    
    # Create output directory if it doesn't exist
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    # Split candidates into clusters
    num_files = (len(candidates) + candidates_per_file - 1) // candidates_per_file
    
    for i in range(num_files):
        start_idx = i * candidates_per_file
        end_idx = min(start_idx + candidates_per_file, len(candidates))
        cluster = candidates[start_idx:end_idx]
        
        # Create output filename
        output_file = output_path / f"Candidates_cluster_{i+1:04d}.json"
        
        # Write JSON file with proper formatting
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(cluster, f, indent=2, ensure_ascii=False)
        
        print(f"Created {output_file} with {len(cluster)} candidates (candidates {start_idx+1}-{end_idx})")
    
    print(f"\nConversion complete! Created {num_files} JSON files in {output_dir}")


if __name__ == "__main__":
    # Set paths - scripts are in scripts/ folder, so go up one level
    base_dir = Path(__file__).parent.parent
    input_file = base_dir / "Candidates_Last_1000_old_crm.md"
    output_dir = base_dir / "Candidates_JSON_Clusters"
    
    convert_candidates_to_json_clusters(str(input_file), str(output_dir), candidates_per_file=1000)

