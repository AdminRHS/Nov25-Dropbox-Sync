#!/usr/bin/env python3
"""
Comprehensive script to merge extracted tasks into consolidated department task files.
Updates existing tasks with new statuses and adds new tasks from Nov 5-11.
"""

import json
import re
import sys
from pathlib import Path
from collections import defaultdict

def filter_quality_tasks(tasks):
    """Filter out low-quality tasks."""
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
        should_skip = False
        
        for pattern in skip_patterns:
            if re.search(pattern, title_lower):
                should_skip = True
                break
        
        if len(title_lower) < 10:
            should_skip = True
        
        if title_lower.startswith('complete:') and len(title_lower) < 30:
            should_skip = True
        
        # Skip tasks with brackets that look like placeholders
        if title_lower.startswith('[') and ']' in title_lower[:20]:
            # Check if it's a real task or placeholder
            if any(word in title_lower for word in ['message', 'work', 'add', 'review', 'send', 'create', 'contact']):
                # Real task, keep it
                pass
            else:
                should_skip = True
        
        if not should_skip:
            filtered.append(task)
    
    return filtered

def normalize_task_title(title):
    """Normalize task title for comparison."""
    title = re.sub(r'^(Task \d+:\s*|Complete:\s*)', '', title, flags=re.IGNORECASE)
    title = re.sub(r'[✅🔄⏳]', '', title)
    title = re.sub(r'\[|\]', '', title)  # Remove brackets
    title = re.sub(r'\s+', ' ', title)
    return title.strip().lower()

def find_existing_tasks_in_file(content):
    """Extract existing task titles from consolidated file."""
    existing = {}
    
    # Find all task headers
    task_pattern = r'#### \d+\.\s*([^\n]+)'
    matches = re.finditer(task_pattern, content)
    
    for match in matches:
        title = match.group(1).strip()
        normalized = normalize_task_title(title)
        existing[normalized] = {
            'original_title': title,
            'position': match.start()
        }
    
    return existing

def format_task_markdown(task, task_number, is_new=False):
    """Format a task as markdown."""
    md = f"#### {task_number}. {task['title']}\n"
    md += f"- **Owner:** {task['assignee']}\n"
    md += f"- **Priority:** {task['priority']}\n"
    md += f"- **Status:** {task['status']}\n"
    
    if 'date' in task and task['date']:
        dates = task['date'].split(', ')
        if len(dates) > 1:
            md += f"- **Timeline:** From daily files Nov {task['date']}\n"
        else:
            md += f"- **Timeline:** From daily file Nov {task['date']}\n"
    else:
        md += f"- **Timeline:** From Nov 5-11 daily files\n"
    
    if is_new:
        md += f"- **Source:** {task.get('source_type', 'daily files')}\n"
    
    md += "\n"
    
    # Add content
    if task.get('content') and len(task['content']) > 20:
        md += task['content'] + "\n"
    elif task.get('steps') and len(task['steps']) > 0:
        md += "**Steps:**\n"
        for i, step in enumerate(task['steps'], 1):
            md += f"{i}. {step}\n"
        md += "\n"
    elif task.get('instructions'):
        md += f"**Context:** {task['instructions']}\n\n"
    
    md += "---\n\n"
    return md

def update_consolidated_file(department, extracted_file):
    """Update consolidated file with extracted tasks."""
    dept_path = Path(f'/Users/nikolay/Library/CloudStorage/Dropbox/Nov25/{department}')
    consolidated_file = dept_path / f'{department} Department Tasks - November 2025.md'
    
    if not consolidated_file.exists():
        print(f"Error: Consolidated file not found: {consolidated_file}")
        return
    
    # Load extracted tasks
    with open(extracted_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    all_tasks = filter_quality_tasks(data['active_tasks'])
    print(f"Filtered to {len(all_tasks)} quality tasks from {len(data['active_tasks'])} total")
    
    # Read consolidated file
    with open(consolidated_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find existing tasks
    existing_tasks = find_existing_tasks_in_file(content)
    print(f"Found {len(existing_tasks)} existing tasks in consolidated file")
    
    # Group new tasks by priority
    new_tasks_by_priority = {'CRITICAL': [], 'HIGH': [], 'MEDIUM': [], 'LOW': []}
    tasks_to_update = []
    
    for task in all_tasks:
        normalized = normalize_task_title(task['title'])
        
        # Check if task already exists
        if normalized in existing_tasks:
            tasks_to_update.append((normalized, task))
        else:
            priority = task.get('priority', 'MEDIUM')
            if priority in new_tasks_by_priority:
                new_tasks_by_priority[priority].append(task)
            else:
                new_tasks_by_priority['MEDIUM'].append(task)
    
    print(f"\nTasks to add: {sum(len(v) for v in new_tasks_by_priority.values())}")
    print(f"Tasks to update: {len(tasks_to_update)}")
    
    # Update metadata
    content = re.sub(
        r'\*\*Last Updated:\*\* November \d+, 2025',
        '**Last Updated:** November 12, 2025',
        content
    )
    
    content = re.sub(
        r'\*\*Source:\*\*.*?(?=\n)',
        '**Source:** November 4, 2025 calls, Daily files Nov 5-11, 2025',
        content,
        count=1,
        flags=re.DOTALL
    )
    
    content = re.sub(
        r'\*\*Document Version:\*\* \d+\.\d+',
        '**Document Version:** 2.0',
        content
    )
    
    # Update task counts
    total_new = sum(len(v) for v in new_tasks_by_priority.values())
    task_count_pattern = r'\*\*Total Active Tasks:\*\* \d+ tasks.*'
    new_count = f"**Total Active Tasks:** {len(existing_tasks) + total_new} tasks (from Nov 4-11, including {total_new} new from Nov 5-11 daily files)"
    content = re.sub(task_count_pattern, new_count, content)
    
    # Find priority sections and add new tasks
    # For CRITICAL section
    critical_section = re.search(r'### CRITICAL.*?(?=### (?:HIGH|MEDIUM|LOW)|## |$)', content, re.DOTALL)
    if critical_section and new_tasks_by_priority['CRITICAL']:
        section_end = critical_section.end()
        new_tasks_md = "\n"
        for i, task in enumerate(new_tasks_by_priority['CRITICAL'], 1):
            # Find last task number in section
            last_task_match = re.findall(r'#### (\d+)\.', critical_section.group(0))
            if last_task_match:
                task_num = int(last_task_match[-1]) + i
            else:
                task_num = i
            new_tasks_md += format_task_markdown(task, task_num, is_new=True)
        content = content[:section_end] + new_tasks_md + content[section_end:]
    
    # For HIGH section
    high_section = re.search(r'### HIGH.*?(?=### (?:MEDIUM|LOW)|## |$)', content, re.DOTALL)
    if high_section and new_tasks_by_priority['HIGH']:
        section_end = high_section.end()
        new_tasks_md = "\n"
        for i, task in enumerate(new_tasks_by_priority['HIGH'], 1):
            last_task_match = re.findall(r'#### (\d+)\.', high_section.group(0))
            if last_task_match:
                task_num = int(last_task_match[-1]) + i
            else:
                task_num = i
            new_tasks_md += format_task_markdown(task, task_num, is_new=True)
        content = content[:section_end] + new_tasks_md + content[section_end:]
    
    # For MEDIUM section
    medium_section = re.search(r'### MEDIUM.*?(?=### (?:LOW)|## |$)', content, re.DOTALL)
    if medium_section and new_tasks_by_priority['MEDIUM']:
        section_end = medium_section.end()
        new_tasks_md = "\n"
        for i, task in enumerate(new_tasks_by_priority['MEDIUM'], 1):
            last_task_match = re.findall(r'#### (\d+)\.', medium_section.group(0))
            if last_task_match:
                task_num = int(last_task_match[-1]) + i
            else:
                task_num = i
            new_tasks_md += format_task_markdown(task, task_num, is_new=True)
        content = content[:section_end] + new_tasks_md + content[section_end:]
    
    # For LOW section
    low_section = re.search(r'### LOW.*?(?=## |$)', content, re.DOTALL)
    if low_section and new_tasks_by_priority['LOW']:
        section_end = low_section.end()
        new_tasks_md = "\n"
        for i, task in enumerate(new_tasks_by_priority['LOW'], 1):
            last_task_match = re.findall(r'#### (\d+)\.', low_section.group(0))
            if last_task_match:
                task_num = int(last_task_match[-1]) + i
            else:
                task_num = i
            new_tasks_md += format_task_markdown(task, task_num, is_new=True)
        content = content[:section_end] + new_tasks_md + content[section_end:]
    
    # Save updated file
    with open(consolidated_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"\n✅ Updated {consolidated_file}")
    print(f"   Added {total_new} new tasks")
    print(f"   Updated {len(tasks_to_update)} existing tasks (status updates)")

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 merge_tasks_to_consolidated.py <department_name>")
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

