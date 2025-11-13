#!/usr/bin/env python3
"""
Archive Week 1 Employee Notes
Creates Week_1 folder in each employee directory and moves daily folders 03-07 into it.
"""

import os
import shutil
from pathlib import Path
from typing import List, Tuple

# Base directory (script is in Nov25 folder)
BASE_DIR = Path(__file__).parent

# System folders to exclude (not employee folders)
SYSTEM_FOLDERS = {
    "Left", "LEFT", "Reports", "Projects", "Tasks", "TEAMLEADS", 
    "prompt", "Microservices", "Video Guides Project", "Design Department",
    "Lead Generation Department", "salesnov25", "Dropbox guid"
}

# Week 1 daily folders to archive
WEEK_1_DAYS = ["03", "04", "05", "06", "07"]
WEEK_1_FOLDER_NAME = "Week_1"


def is_employee_folder(folder_name: str, department_path: Path) -> bool:
    """
    Determine if a folder is an employee folder.
    Employee folders are directories that are not system folders.
    """
    if folder_name in SYSTEM_FOLDERS:
        return False
    
    folder_path = department_path / folder_name
    if not folder_path.is_dir():
        return False
    
    # Check if it contains daily folders (03, 04, etc.) or other employee files
    # This helps distinguish employee folders from other directories
    contents = list(folder_path.iterdir())
    has_daily_folders = any(item.name in WEEK_1_DAYS and item.is_dir() for item in contents)
    has_profile = any(item.name.startswith("Profile") and item.name.endswith(".md") for item in contents)
    has_readme = (folder_path / "README.md").exists()
    
    return has_daily_folders or has_profile or has_readme


def find_employee_folders() -> List[Tuple[Path, str, str]]:
    """
    Scan Nov25 directory and find all employee folders.
    Returns list of tuples: (employee_path, employee_name, department_name)
    """
    employee_folders = []
    
    if not BASE_DIR.exists():
        print(f"Error: Base directory not found: {BASE_DIR}")
        return employee_folders
    
    # Scan all departments
    for dept_path in BASE_DIR.iterdir():
        if not dept_path.is_dir():
            continue
        
        dept_name = dept_path.name
        
        # Skip if it's not a department folder (like Reports, etc.)
        if dept_path.name in SYSTEM_FOLDERS:
            continue
        
        # Scan for employee folders in this department
        for item in dept_path.iterdir():
            if item.is_dir() and is_employee_folder(item.name, dept_path):
                employee_folders.append((item, item.name, dept_name))
    
    return employee_folders


def archive_week1_for_employee(employee_path: Path, employee_name: str, department_name: str) -> dict:
    """
    Create Week_1 folder and move daily folders 03-07 into it for a single employee.
    Returns dict with operation results.
    """
    results = {
        "employee": employee_name,
        "department": department_name,
        "week1_created": False,
        "folders_moved": [],
        "folders_skipped": [],
        "errors": []
    }
    
    try:
        # Create Week_1 folder if it doesn't exist
        week1_path = employee_path / WEEK_1_FOLDER_NAME
        if not week1_path.exists():
            week1_path.mkdir(parents=True, exist_ok=True)
            results["week1_created"] = True
        else:
            results["week1_created"] = False  # Already exists
        
        # Move daily folders 03-07 into Week_1
        for day in WEEK_1_DAYS:
            day_folder = employee_path / day
            
            if not day_folder.exists():
                results["folders_skipped"].append(day)
                continue
            
            # Check if already in Week_1
            target_path = week1_path / day
            if target_path.exists():
                results["folders_skipped"].append(f"{day} (already in Week_1)")
                continue
            
            # Move the folder
            try:
                shutil.move(str(day_folder), str(target_path))
                results["folders_moved"].append(day)
            except Exception as e:
                error_msg = f"Error moving {day}: {str(e)}"
                results["errors"].append(error_msg)
                print(f"  ⚠️  {error_msg}")
    
    except Exception as e:
        error_msg = f"Error processing {employee_name}: {str(e)}"
        results["errors"].append(error_msg)
        print(f"  ❌ {error_msg}")
    
    return results


def main():
    """
    Main function to archive Week 1 notes for all employees.
    """
    print("=" * 70)
    print("Archive Week 1 Employee Notes")
    print("=" * 70)
    print(f"Base directory: {BASE_DIR}")
    print(f"Week 1 days to archive: {', '.join(WEEK_1_DAYS)}")
    print()
    
    # Find all employee folders
    print("Scanning for employee folders...")
    employee_folders = find_employee_folders()
    
    if not employee_folders:
        print("❌ No employee folders found!")
        return
    
    print(f"✅ Found {len(employee_folders)} employee folders")
    print()
    
    # Process each employee
    total_moved = 0
    total_skipped = 0
    total_errors = 0
    
    for employee_path, employee_name, department_name in employee_folders:
        print(f"Processing: {department_name} / {employee_name}")
        results = archive_week1_for_employee(employee_path, employee_name, department_name)
        
        # Print results
        if results["week1_created"]:
            print(f"  ✅ Created Week_1 folder")
        else:
            print(f"  ℹ️  Week_1 folder already exists")
        
        if results["folders_moved"]:
            print(f"  ✅ Moved folders: {', '.join(results['folders_moved'])}")
            total_moved += len(results["folders_moved"])
        
        if results["folders_skipped"]:
            print(f"  ⏭️  Skipped: {', '.join(results['folders_skipped'])}")
            total_skipped += len(results["folders_skipped"])
        
        if results["errors"]:
            total_errors += len(results["errors"])
        
        print()
    
    # Summary
    print("=" * 70)
    print("Summary")
    print("=" * 70)
    print(f"Total employees processed: {len(employee_folders)}")
    print(f"Total folders moved: {total_moved}")
    print(f"Total folders skipped: {total_skipped}")
    print(f"Total errors: {total_errors}")
    print()
    
    if total_errors == 0:
        print("✅ Archive completed successfully!")
    else:
        print(f"⚠️  Archive completed with {total_errors} error(s)")


if __name__ == "__main__":
    main()

