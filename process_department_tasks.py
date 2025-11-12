#!/usr/bin/env python3
"""
Generic script to process any department's task.md files from folders 04-11.
Usage: python3 process_department_tasks.py <department_name>
Example: python3 process_department_tasks.py AI
"""

import os
import re
import json
import sys
from pathlib import Path
from collections import defaultdict
from difflib import SequenceMatcher

def parse_task_file(filepath, employee_name, date_folder):
    """Parse a task.md file and extract task information."""
    tasks = []
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Skip template files
        if '[Task Name from plans.md]' in content or 'Task Breakdown - [Date]' in content:
            return tasks
        
        # Extract date from file
        date_match = re.search(r'Task Breakdown - (.+)', content)
        date = date_match.group(1) if date_match else date_folder
        
        # Split by task markers
        task_sections = re.split(r'## Task \d+:', content)
        
        for i, section in enumerate(task_sections[1:], 1):
            # Extract task title
            title_match = re.match(r'^([^\n]+)', section.strip())
            if not title_match:
                continue
            
            title = title_match.group(1).strip()
            
            # Skip template tasks
            if 'Task Name from plans.md' in title or not title or len(title) < 5:
                continue
            
            # Extract status
            status_match = re.search(r'### Status:\s*(.+?)(?:\n|$)', section, re.IGNORECASE)
            status = status_match.group(1).strip() if status_match else "Not Started"
            
            # Normalize status
            status_lower = status.lower()
            if 'completed' in status_lower or 'done' in status_lower or '✅' in title:
                status = "Completed"
            elif 'in progress' in status_lower or 'progress' in status_lower or '🔄' in title:
                status = "In Progress"
            elif 'planned' in status_lower or 'planning' in status_lower or '⏳' in title:
                status = "Planned"
            elif 'pending' in status_lower:
                status = "Pending"
            else:
                status = "Not Started"
            
            # Extract steps
            steps_match = re.search(r'### Steps:\s*(.*?)(?=### |$)', section, re.DOTALL)
            steps = []
            if steps_match:
                steps_text = steps_match.group(1)
                step_lines = re.findall(r'^\d+\.\s*(.+)$', steps_text, re.MULTILINE)
                steps = [s.strip() for s in step_lines if s.strip()]
            
            # Extract resources
            resources_match = re.search(r'### Resources and Links:\s*(.*?)(?=### |$)', section, re.DOTALL)
            resources = []
            if resources_match:
                resources_text = resources_match.group(1)
                resource_lines = re.findall(r'^-\s*(.+)$', resources_text, re.MULTILINE)
                resources = [r.strip() for r in resource_lines if r.strip()]
            
            # Extract instructions
            instructions_match = re.search(r'### Instructions:\s*(.*?)(?=---|$)', section, re.DOTALL)
            instructions = instructions_match.group(1).strip() if instructions_match else ""
            
            # Extract outcomes
            outcomes_match = re.search(r'### Outcomes:\s*(.*?)(?=### |$)', section, re.DOTALL)
            outcomes = []
            if outcomes_match:
                outcomes_text = outcomes_match.group(1)
                outcome_lines = re.findall(r'^-\s*(.+)$', outcomes_text, re.MULTILINE)
                outcomes = [o.strip() for o in outcome_lines if o.strip()]
            
            # Determine priority (default to MEDIUM)
            priority = "MEDIUM"
            if any(word in title.lower() for word in ['critical', 'urgent', 'blocking', 'blocked']):
                priority = "CRITICAL"
            elif any(word in title.lower() for word in ['high', 'important', 'priority']):
                priority = "HIGH"
            elif any(word in title.lower() for word in ['low', 'nice to have', 'optional']):
                priority = "LOW"
            
            # Build full content
            full_content = f"**Steps:**\n"
            if steps:
                for step in steps:
                    full_content += f"{step}\n"
            if resources:
                full_content += f"\n**Resources:**\n"
                for res in resources:
                    full_content += f"- {res}\n"
            if instructions:
                full_content += f"\n**Instructions:**\n{instructions}\n"
            if outcomes:
                full_content += f"\n**Outcomes:**\n"
                for outcome in outcomes:
                    full_content += f"- {outcome}\n"
            
            task = {
                'title': title,
                'priority': priority,
                'status': status,
                'assignee': employee_name,
                'date': date_folder,
                'source_file': str(filepath),
                'steps': steps,
                'resources': resources,
                'instructions': instructions,
                'outcomes': outcomes,
                'content': full_content
            }
            
            tasks.append(task)
    
    except Exception as e:
        print(f"Error parsing {filepath}: {e}")
    
    return tasks

def collect_and_parse_all_tasks(base_dir, dates, include_left=False):
    """Collect and parse all task.md/tasks.md files from specified date folders."""
    all_tasks = []
    
    base_path = Path(base_dir)
    
    for date_folder in dates:
        # Find all employee folders
        for employee_folder in base_path.iterdir():
            if not employee_folder.is_dir() or employee_folder.name.startswith('.'):
                continue
            
            # Handle Left folder separately
            if employee_folder.name.lower() == 'left':
                if include_left:
                    # Iterate through employee folders inside Left
                    left_path = employee_folder
                    for left_employee_folder in left_path.iterdir():
                        if not left_employee_folder.is_dir() or left_employee_folder.name.startswith('.'):
                            continue
                        
                        # Try both task.md and tasks.md
                        task_file = left_employee_folder / date_folder / 'task.md'
                        tasks_file = left_employee_folder / date_folder / 'tasks.md'
                        
                        file_to_parse = None
                        if task_file.exists():
                            file_to_parse = task_file
                        elif tasks_file.exists():
                            file_to_parse = tasks_file
                        
                        if file_to_parse:
                            employee_name = left_employee_folder.name
                            tasks = parse_task_file(file_to_parse, employee_name, date_folder)
                            all_tasks.extend(tasks)
                            if tasks:
                                print(f"Found {len(tasks)} tasks in Left/{employee_name}/{date_folder}/{file_to_parse.name}")
                continue
            
            # Try both task.md and tasks.md
            task_file = employee_folder / date_folder / 'task.md'
            tasks_file = employee_folder / date_folder / 'tasks.md'
            
            file_to_parse = None
            if task_file.exists():
                file_to_parse = task_file
            elif tasks_file.exists():
                file_to_parse = tasks_file
            
            if file_to_parse:
                employee_name = employee_folder.name
                tasks = parse_task_file(file_to_parse, employee_name, date_folder)
                all_tasks.extend(tasks)
                if tasks:
                    print(f"Found {len(tasks)} tasks in {employee_name}/{date_folder}/{file_to_parse.name}")
    
    return all_tasks

def normalize_title(title):
    """Normalize task title for comparison."""
    # Remove common prefixes and normalize
    title = re.sub(r'^(Task \d+:\s*)', '', title, flags=re.IGNORECASE)
    title = re.sub(r'[✅🔄⏳]', '', title)  # Remove emoji markers
    title = re.sub(r'\s+', ' ', title)
    title = title.strip()
    return title.lower()

def group_and_merge_tasks(all_tasks):
    """Group similar tasks and merge duplicates."""
    # Filter out completed tasks for consolidation (but keep them for reference)
    active_tasks = [t for t in all_tasks if t['status'] != 'Completed']
    completed_tasks = [t for t in all_tasks if t['status'] == 'Completed']
    
    # Group by normalized title similarity
    groups = []
    used_indices = set()
    
    for i, task in enumerate(active_tasks):
        if i in used_indices:
            continue
        
        group = [task]
        used_indices.add(i)
        
        # Find similar tasks
        for j, other_task in enumerate(active_tasks[i+1:], start=i+1):
            if j in used_indices:
                continue
            
            similarity = SequenceMatcher(
                None,
                normalize_title(task['title']),
                normalize_title(other_task['title'])
            ).ratio() * 100
            
            # If very similar (85%+), group them
            if similarity >= 85:
                group.append(other_task)
                used_indices.add(j)
        
        groups.append(group)
    
    # Merge groups
    merged_tasks = []
    for group in groups:
        if len(group) == 1:
            merged_tasks.append(group[0])
        else:
            # Merge multiple tasks
            main_task = group[0].copy()
            
            # Combine assignees
            assignees = list(set([t['assignee'] for t in group]))
            main_task['assignee'] = ', '.join(assignees) if len(assignees) > 1 else assignees[0]
            
            # Use most recent status (prioritize In Progress > Not Started > Planned)
            status_priority = {'In Progress': 3, 'Not Started': 2, 'Planned': 1, 'Pending': 1}
            main_task['status'] = max(group, key=lambda t: status_priority.get(t['status'], 0))['status']
            
            # Combine all dates
            dates = list(set([t['date'] for t in group]))
            main_task['date'] = ', '.join(sorted(dates))
            
            # Combine source files
            sources = [t['source_file'] for t in group]
            main_task['source_files'] = sources
            
            # Combine steps (unique)
            all_steps = []
            for t in group:
                all_steps.extend(t.get('steps', []))
            main_task['steps'] = list(dict.fromkeys(all_steps))  # Remove duplicates
            
            merged_tasks.append(main_task)
    
    return merged_tasks, completed_tasks

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 process_department_tasks.py <department_name> [--include-left]")
        print("Example: python3 process_department_tasks.py AI")
        print("Example: python3 process_department_tasks.py Video --include-left")
        sys.exit(1)
    
    department = sys.argv[1]
    include_left = '--include-left' in sys.argv
    
    base_dir = f'/Users/nikolay/Library/CloudStorage/Dropbox/Nov25/{department}'
    dates = ['04', '05', '06', '07', '08', '09', '10', '11']
    
    if not os.path.exists(base_dir):
        print(f"Error: Department directory not found: {base_dir}")
        sys.exit(1)
    
    print(f"Collecting and parsing {department} department tasks...")
    if include_left:
        print("Including Left folder...")
    all_tasks = collect_and_parse_all_tasks(base_dir, dates, include_left=include_left)
    
    print(f"\nTotal tasks found: {len(all_tasks)}")
    
    print("\nGrouping and merging similar tasks...")
    merged_tasks, completed_tasks = group_and_merge_tasks(all_tasks)
    
    print(f"Unique active tasks after merging: {len(merged_tasks)}")
    print(f"Completed tasks: {len(completed_tasks)}")
    
    # Save to JSON
    output_file = os.path.join(base_dir, f'extracted_{department.lower()}_tasks.json')
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump({
            'active_tasks': merged_tasks,
            'completed_tasks': completed_tasks,
            'total_active': len(merged_tasks),
            'total_completed': len(completed_tasks)
        }, f, indent=2, ensure_ascii=False)
    
    print(f"\nSaved {len(merged_tasks)} active tasks and {len(completed_tasks)} completed tasks to {output_file}")
    
    # Print summary
    by_priority = defaultdict(int)
    by_status = defaultdict(int)
    by_employee = defaultdict(int)
    
    for task in merged_tasks:
        by_priority[task['priority']] += 1
        by_status[task['status']] += 1
        by_employee[task['assignee']] += 1
    
    print("\n=== Summary ===")
    print(f"\nBy Priority:")
    for priority in ['CRITICAL', 'HIGH', 'MEDIUM', 'LOW']:
        print(f"  {priority}: {by_priority[priority]}")
    
    print(f"\nBy Status:")
    for status in sorted(by_status.keys()):
        print(f"  {status}: {by_status[status]}")
    
    print(f"\nBy Employee:")
    for employee in sorted(by_employee.keys()):
        print(f"  {employee}: {by_employee[employee]}")

if __name__ == '__main__':
    main()

