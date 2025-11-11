#!/usr/bin/env python3
"""
Process CRM Employee Export File
Matches employees from Employees.json with Finance Public data
Filters for employees with "Available" status
Creates mini-file for Talent service import
"""

import json
import os
from datetime import datetime

# Paths
EMPLOYEES_JSON_PATH = "/Users/nikolay/Library/CloudStorage/Dropbox/Nov25/AI/Niko AI/ExportCRMS/Employees.json"
FINANCE_AVAILABLE_PATH = "/Users/nikolay/Library/CloudStorage/Dropbox/Finance Public/Nov 25 - Employees_Available.md"
OUTPUT_DIR = "/Users/nikolay/Library/CloudStorage/Dropbox/Nov25/AI/Artemchuk Nikolay/11"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "employees_filtered_for_talent.json")
REPORT_FILE = os.path.join(OUTPUT_DIR, "processing_report.md")

def extract_available_employee_ids(finance_file):
    """Extract employee IDs from Finance Public Available file"""
    available_ids = []
    try:
        with open(finance_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for line in lines:
                # Look for table rows with employee IDs
                if '|' in line and line.strip().startswith('|'):
                    parts = [p.strip() for p in line.split('|')]
                    if len(parts) >= 2 and parts[1].isdigit():
                        employee_id = int(parts[1])
                        # Check if status is "Available"
                        if len(parts) >= 4 and 'Available' in parts[3]:
                            available_ids.append(employee_id)
    except Exception as e:
        print(f"Error reading finance file: {e}")
    return available_ids

def find_employee_by_id(employees_data, target_id):
    """Find employee in JSON by matching employee_id (as string)"""
    target_id_str = str(target_id)
    for emp in employees_data:
        # Match by employee_id field (stored as string in JSON)
        if emp.get('employee_id') == target_id_str:
            return emp
        # Also check in employee_detail
        if emp.get('employee_detail') and emp['employee_detail'].get('employee_id') == target_id_str:
            return emp
    return None

def has_institution_date(employee):
    """Check if employee has institution date field (joining_date or similar)"""
    # Check for joining_date
    if employee.get('joining_date'):
        return True
    # Check in employee_detail
    if employee.get('employee_detail') and employee['employee_detail'].get('joining_date'):
        return True
    # Check for any date field that might indicate institution
    date_fields = ['joining_date', 'start_date', 'institution_date', 'institutionDate']
    for field in date_fields:
        if employee.get(field):
            return True
        if employee.get('employee_detail') and employee['employee_detail'].get(field):
            return True
    return False

def process_employees():
    """Main processing function"""
    print("Starting employee processing...")
    
    # Step 1: Extract available employee IDs from Finance Public
    print(f"Reading Finance Public file: {FINANCE_AVAILABLE_PATH}")
    available_ids = extract_available_employee_ids(FINANCE_AVAILABLE_PATH)
    print(f"Found {len(available_ids)} employees with 'Available' status")
    print(f"Available IDs: {available_ids}")
    
    # Step 2: Load Employees.json
    print(f"\nLoading Employees.json: {EMPLOYEES_JSON_PATH}")
    try:
        with open(EMPLOYEES_JSON_PATH, 'r', encoding='utf-8') as f:
            data = json.load(f)
            employees = data.get('data', {}).get('employees', [])
        print(f"Loaded {len(employees)} employees from JSON")
    except Exception as e:
        print(f"Error loading JSON: {e}")
        return
    
    # Step 3: Match and filter employees
    print("\nMatching employees...")
    matched_employees = []
    matched_with_date = []
    not_found_ids = []
    
    for emp_id in available_ids:
        employee = find_employee_by_id(employees, emp_id)
        if employee:
            matched_employees.append(employee)
            if has_institution_date(employee):
                matched_with_date.append(employee)
        else:
            not_found_ids.append(emp_id)
    
    print(f"Matched {len(matched_employees)} employees")
    print(f"Matched with institution date: {len(matched_with_date)}")
    print(f"Not found in JSON: {not_found_ids}")
    
    # Step 4: Create filtered mini-file
    print(f"\nCreating filtered file: {OUTPUT_FILE}")
    filtered_data = {
        "message": "Filtered Employees for Talent Service Import",
        "filter_date": datetime.now().isoformat(),
        "filter_criteria": {
            "status": "Available",
            "has_institution_date": True,
            "source": "Finance Public - Nov 25 - Employees_Available.md"
        },
        "summary": {
            "total_available": len(available_ids),
            "matched": len(matched_employees),
            "matched_with_date": len(matched_with_date),
            "not_found": len(not_found_ids)
        },
        "data": {
            "employees": matched_with_date
        }
    }
    
    try:
        with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
            json.dump(filtered_data, f, indent=2, ensure_ascii=False)
        print(f"✓ Created filtered file with {len(matched_with_date)} employees")
    except Exception as e:
        print(f"Error writing output file: {e}")
        return
    
    # Step 5: Generate processing report
    print(f"\nGenerating processing report: {REPORT_FILE}")
    report = f"""# Employee Export Processing Report

**Date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**Task:** Task_02_Process_CRM_Employee_Export.md

## Summary

- **Total employees with 'Available' status:** {len(available_ids)}
- **Matched in Employees.json:** {len(matched_employees)}
- **Matched with institution date:** {len(matched_with_date)}
- **Not found in JSON:** {len(not_found_ids)}

## Available Employee IDs

{', '.join(map(str, available_ids))}

## Matched Employees (with institution date)

"""
    
    for emp in matched_with_date:
        emp_id = emp.get('user', {}).get('id') or emp.get('id')
        name = emp.get('name_eng') or emp.get('name_ua') or 'Unknown'
        joining_date = emp.get('joining_date') or emp.get('employee_detail', {}).get('joining_date') or 'N/A'
        report += f"- **ID {emp_id}:** {name} (Joining Date: {joining_date})\n"
    
    if not_found_ids:
        report += f"\n## Not Found in JSON\n\n"
        report += f"The following employee IDs from Finance Public were not found in Employees.json:\n"
        report += f"{', '.join(map(str, not_found_ids))}\n"
    
    report += f"""
## Output Files

- **Filtered JSON:** `employees_filtered_for_talent.json`
- **Report:** `processing_report.md`

## Next Steps

1. Review filtered employees
2. Validate data structure for Talent service import
3. Archive original Employees.json file
4. Import filtered data into Talent service

---
**Generated by:** process_employee_export.py
**Source:** {EMPLOYEES_JSON_PATH}
"""
    
    try:
        with open(REPORT_FILE, 'w', encoding='utf-8') as f:
            f.write(report)
        print("✓ Created processing report")
    except Exception as e:
        print(f"Error writing report: {e}")
    
    print("\n✓ Processing complete!")

if __name__ == "__main__":
    process_employees()

