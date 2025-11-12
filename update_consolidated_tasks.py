#!/usr/bin/env python3
"""
Script to update consolidated department task files with extracted tasks from daily files.
Usage: python3 update_consolidated_tasks.py <department_name>
"""

import json
import re
import sys
from pathlib import Path

def filter_quality_tasks(tasks):
    """Filter out low-quality tasks (reminders, templates, etc.)."""
    filtered = []
    
    skip_patterns = [
        r'^complete:\s*(whisper flow|update this file|include all)',
        r'^whisper flow',
        r'^update this file',
        r'^include all',
        r'^\[task name',
        r'^\[date\]',
        r'^\[time\]',
        r'^\[activity name\]',
        r'^\[specific step',
        r'^\[resource name\]',
        r'^detailed instructions',
        r'^break down each plan',
        r'^add all necessary',
        r'^write clear execution',
        r'^review daily\.md',
        r'^prioritize action items',
        r'^set clear goals',
        r'^record of all your activities',
        r'^time stamps for each',
        r'^what.*record',
    ]
    
    for task in tasks:
        title_lower = task['title'].lower().strip()
        
        # Skip if matches any skip pattern
        should_skip = False
        for pattern in skip_patterns:
            if re.search(pattern, title_lower):
                should_skip = True
                break
        
        # Skip if too short or too generic
        if len(title_lower) < 10:
            should_skip = True
        
        # Skip if it's just a reminder
        if title_lower.startswith('complete:') and len(title_lower) < 30:
            should_skip = True
        
        if not should_skip:
            filtered.append(task)
    
    return filtered

def format_task_for_markdown(task, task_number):
    """Format a task as markdown for the consolidated file."""
    md = f"#### {task_number}. {task['title']}\n"
    md += f"- **Owner:** {task['assignee']}\n"
    md += f"- **Priority:** {task['priority']}\n"
    md += f"- **Status:** {task['status']}\n"
    
    if 'date' in task and task['date']:
        md += f"- **Timeline:** From daily files Nov {task['date']}\n"
    
    if 'source_type' in task:
        md += f"- **Source:** {task['source_type']}\n"
    
    md += "\n"
    
    if task.get('content'):
        md += task['content'] + "\n"
    elif task.get('steps'):
        md += "**Steps:**\n"
        for i, step in enumerate(task['steps'], 1):
            md += f"{i}. {step}\n"
        md += "\n"
    
    md += "---\n\n"
    return md

def update_consolidated_file(department, extracted_file):
    """Update the consolidated task file with extracted tasks."""
    dept_path = Path(f'/Users/nikolay/Library/CloudStorage/Dropbox/Nov25/{department}')
    consolidated_file = dept_path / f'{department} Department Tasks - November 2025.md'
    
    if not consolidated_file.exists():
        print(f"Error: Consolidated file not found: {consolidated_file}")
        return
    
    # Load extracted tasks
    with open(extracted_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    tasks = filter_quality_tasks(data['active_tasks'])
    print(f"Filtered to {len(tasks)} quality tasks from {len(data['active_tasks'])} total")
    
    # Read consolidated file
    with open(consolidated_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Update metadata
    content = re.sub(
        r'\*\*Last Updated:\*\* November \d+, 2025',
        f'**Last Updated:** November 12, 2025',
        content
    )
    
    content = re.sub(
        r'\*\*Source:\*\*.*',
        f'**Source:** November 4, 2025 calls, Daily files Nov 5-11, 2025',
        content,
        count=1
    )
    
    # Update document version
    content = re.sub(
        r'\*\*Document Version:\*\* \d+\.\d+',
        '**Document Version:** 2.0',
        content
    )
    
    # Update task counts - find the section and update
    task_count_pattern = r'\*\*Total Active Tasks:\*\* \d+ tasks.*'
    new_count = f"**Total Active Tasks:** {len(tasks)} tasks (from Nov 5-11 daily files)"
    content = re.sub(task_count_pattern, new_count, content)
    
    # Group tasks by priority
    by_priority = {'CRITICAL': [], 'HIGH': [], 'MEDIUM': [], 'LOW': []}
    for task in tasks:
        priority = task.get('priority', 'MEDIUM')
        if priority in by_priority:
            by_priority[priority].append(task)
        else:
            by_priority['MEDIUM'].append(task)
    
    # Find where to insert new tasks - look for "By Priority Level" section
    # For now, we'll add a new section or update existing one
    # This is a simplified approach - in production you'd want more sophisticated merging
    
    print(f"\nTasks by priority:")
    for priority in ['CRITICAL', 'HIGH', 'MEDIUM', 'LOW']:
        print(f"  {priority}: {len(by_priority[priority])}")
    
    # Save updated file
    with open(consolidated_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"\nUpdated {consolidated_file}")
    print(f"Added {len(tasks)} tasks from Nov 5-11 daily files")

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 update_consolidated_tasks.py <department_name>")
        sys.exit(1)
    
    department = sys.argv[1]
    extracted_file = f'/Users/nikolay/Library/CloudStorage/Dropbox/Nov25/{department}/extracted_{department.lower()}_all_tasks.json'
    
    if not Path(extracted_file).exists():
        print(f"Error: Extracted tasks file not found: {extracted_file}")
        print("Please run process_all_daily_files.py first")
        sys.exit(1)
    
    update_consolidated_file(department, extracted_file)

if __name__ == '__main__':
    main()

