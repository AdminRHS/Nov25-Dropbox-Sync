"""
Script to convert all markdown files in Libs folder to proper JSON files.
Each .md file will be converted to .json and saved in a Libs_JSON folder.
"""
import json
import os
from pathlib import Path


def convert_libs_to_json(libs_dir, output_dir):
    """
    Convert all markdown files in Libs directory to JSON files.

    Args:
        libs_dir (str): Path to Libs directory
        output_dir (str): Directory to save output JSON files
    """
    libs_path = Path(libs_dir)
    output_path = Path(output_dir)

    # Create output directory if it doesn't exist
    output_path.mkdir(parents=True, exist_ok=True)

    # Get all .md files in the Libs directory
    md_files = list(libs_path.glob('*.md'))

    if not md_files:
        print(f"No .md files found in {libs_dir}")
        return

    print(f"Found {len(md_files)} markdown files to convert")

    converted_count = 0
    error_count = 0

    for md_file in md_files:
        try:
            print(f"\nProcessing: {md_file.name}")

            # Read the markdown file
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()

            # Parse the JSON content
            data = json.loads(content.strip())

            # Create output filename (replace .md with .json)
            json_filename = md_file.stem + '.json'
            output_file = output_path / json_filename

            # Write JSON file with proper formatting
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)

            print(f"  [OK] Created: {json_filename}")
            converted_count += 1

        except json.JSONDecodeError as e:
            print(f"  [ERROR] Error parsing JSON in {md_file.name}: {e}")
            error_count += 1
        except Exception as e:
            print(f"  [ERROR] Error processing {md_file.name}: {e}")
            error_count += 1

    print(f"\n{'='*60}")
    print(f"Conversion complete!")
    print(f"  Successfully converted: {converted_count} files")
    print(f"  Errors: {error_count} files")
    print(f"  Output directory: {output_dir}")
    print(f"{'='*60}")


if __name__ == "__main__":
    # Set paths - scripts are in scripts/ folder, so go up one level
    base_dir = Path(__file__).parent.parent
    libs_dir = base_dir / "Libs"
    output_dir = base_dir / "Libs_JSON"

    print(f"Converting files from: {libs_dir}")
    print(f"Output directory: {output_dir}")

    convert_libs_to_json(str(libs_dir), str(output_dir))
