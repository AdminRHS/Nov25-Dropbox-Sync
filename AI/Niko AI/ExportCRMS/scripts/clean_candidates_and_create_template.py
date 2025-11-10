"""
Script to clean candidates JSON by removing empty/null placeholders
and create a JSON lookup template of all possible candidate fields.
"""
import json
from pathlib import Path
from collections import OrderedDict


def is_empty_value(value):
    """
    Check if a value is considered empty (null, empty string, empty array, empty dict).
    
    Args:
        value: Value to check
        
    Returns:
        bool: True if value is empty, False otherwise
    """
    if value is None:
        return True
    if isinstance(value, str) and value.strip() == "":
        return True
    if isinstance(value, (list, dict)) and len(value) == 0:
        return True
    return False


def clean_object(obj):
    """
    Recursively remove empty/null values from an object.
    
    Args:
        obj: Object to clean (dict, list, or primitive)
        
    Returns:
        Cleaned object
    """
    if isinstance(obj, dict):
        cleaned = {}
        for key, value in obj.items():
            cleaned_value = clean_object(value)
            if not is_empty_value(cleaned_value):
                cleaned[key] = cleaned_value
        return cleaned
    elif isinstance(obj, list):
        cleaned = []
        for item in obj:
            cleaned_item = clean_object(item)
            if not is_empty_value(cleaned_item):
                cleaned.append(cleaned_item)
        return cleaned
    else:
        return obj


def extract_field_template(obj, template=None, path=""):
    """
    Extract all possible fields from candidate objects to create a template.
    
    Args:
        obj: Candidate object to analyze
        template: Current template dictionary (for recursion)
        path: Current path in the object (for nested fields)
        
    Returns:
        Template dictionary with all possible fields
    """
    if template is None:
        template = OrderedDict()
    
    if isinstance(obj, dict):
        for key, value in obj.items():
            field_path = f"{path}.{key}" if path else key
            
            if isinstance(value, dict):
                # Nested object
                if field_path not in template:
                    template[field_path] = {
                        "type": "object",
                        "fields": OrderedDict(),
                        "description": f"Nested object: {key}"
                    }
                elif "fields" not in template[field_path]:
                    # Update existing entry to be an object type
                    template[field_path] = {
                        "type": "object",
                        "fields": OrderedDict(),
                        "description": f"Nested object: {key}"
                    }
                extract_field_template(value, template[field_path]["fields"], field_path)
            elif isinstance(value, list):
                # Array
                if field_path not in template:
                    template[field_path] = {
                        "type": "array",
                        "item_type": "unknown",
                        "description": f"Array of: {key}"
                    }
                # Check first item to determine array item type
                if value and len(value) > 0:
                    if isinstance(value[0], dict):
                        template[field_path]["item_type"] = "object"
                        template[field_path]["item_fields"] = OrderedDict()
                        extract_field_template(value[0], template[field_path]["item_fields"], f"{field_path}[]")
                    else:
                        template[field_path]["item_type"] = type(value[0]).__name__
            else:
                # Primitive value
                if field_path not in template:
                    template[field_path] = {
                        "type": type(value).__name__,
                        "description": f"Field: {key}",
                        "example": value if not isinstance(value, (dict, list)) else None
                    }
    
    return template


def process_candidates_file(input_file, output_file, template_file):
    """
    Process candidates JSON file: clean empty values and create template.
    
    Args:
        input_file (str): Path to input JSON file
        output_file (str): Path to output cleaned JSON file
        template_file (str): Path to output template JSON file
    """
    print(f"Reading file: {input_file}")
    
    # Read file with utf-8-sig to handle BOM
    with open(input_file, 'r', encoding='utf-8-sig') as f:
        candidates = json.load(f)
    
    print(f"Found {len(candidates)} candidates")
    
    # Create template from first candidate
    if candidates:
        print("Extracting field template from candidates...")
        template = OrderedDict()
        for candidate in candidates[:5]:  # Analyze first 5 to catch all variations
            extract_field_template(candidate, template)
        
        # Save template
        print(f"Creating template file: {template_file}")
        template_output = {
            "candidate_fields_template": template,
            "total_fields": len(template),
            "description": "JSON lookup template showing all possible candidate fields with types and descriptions"
        }
        
        with open(template_file, 'w', encoding='utf-8') as f:
            json.dump(template_output, f, indent=2, ensure_ascii=False)
        
        print(f"Template created with {len(template)} fields")
    
    # Clean candidates
    print("Cleaning candidates (removing empty/null values)...")
    cleaned_candidates = []
    for i, candidate in enumerate(candidates):
        cleaned = clean_object(candidate)
        cleaned_candidates.append(cleaned)
        if (i + 1) % 100 == 0:
            print(f"Processed {i + 1}/{len(candidates)} candidates")
    
    # Save cleaned candidates
    print(f"Saving cleaned candidates to: {output_file}")
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(cleaned_candidates, f, indent=2, ensure_ascii=False)
    
    print(f"\nProcessing complete!")
    print(f"  - Cleaned {len(cleaned_candidates)} candidates")
    print(f"  - Template saved to: {template_file}")


if __name__ == "__main__":
    # Set paths - scripts are in scripts/ folder, so go up one level
    base_dir = Path(__file__).parent.parent
    
    # Process the cluster file
    input_file = base_dir / "Candidates_JSON_Clusters" / "Candidates_cluster_0001.json"
    output_file = base_dir / "Candidates_JSON_Clusters" / "Candidates_cluster_0001_cleaned.json"
    template_file = base_dir / "Candidates_JSON_Clusters" / "candidate_fields_template.json"
    
    process_candidates_file(str(input_file), str(output_file), str(template_file))

