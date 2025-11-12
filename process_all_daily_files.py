#!/usr/bin/env python3
"""
Comprehensive script to process all daily files (daily.md, plans.md, task.md) 
from folders 05-11 for all employees and extract tasks.
Usage: python3 process_all_daily_files.py <department_name>
Example: python3 process_all_daily_files.py AI
"""

import os
import re
import json
import sys
from pathlib import Path
from collections import defaultdict
from difflib import SequenceMatcher
from datetime import datetime

def extract_tasks_from_daily(daily_content, employee_name, date_folder, source_file):
    """Extract tasks from daily.md file content."""
    tasks = []
    
    # Skip template files
    if '[Date]' in daily_content and '## Instructions' in daily_content and len(daily_content) < 500:
        return tasks
    
    # Extract activities and outcomes
    activity_pattern = r'###\s*(\d{1,2}:\d{2}|\[Time\])\s*-\s*(.+?)(?=###|$)'
    activities = re.findall(activity_pattern, daily_content, re.DOTALL)
    
    for time, activity_content in activities:
        # Extract "What I worked on" section
        what_worked = re.search(r'\*\*What I worked on:\*\*\s*(.*?)(?=\*\*|$)', activity_content, re.DOTALL)
        if what_worked:
            work_items = what_worked.group(1).strip()
            if work_items and work_items != '-' and len(work_items) > 10:
                # Split by lines and extract tasks
                for line in work_items.split('\n'):
                    line = line.strip()
                    if line and line.startswith('-') and len(line) > 10:
                        task_title = line.lstrip('- ').strip()
                        if len(task_title) > 5:
                            tasks.append({
                                'title': task_title,
                                'priority': 'MEDIUM',
                                'status': 'Not Started',
                                'assignee': employee_name,
                                'date': date_folder,
                                'source_file': source_file,
                                'source_type': 'daily.md',
                                'context': f"From daily activity at {time}",
                                'content': f"**Context:** {activity_content[:200]}..."
                            })
        
        # Extract outcomes
        outcomes = re.search(r'\*\*Outcomes:\*\*\s*(.*?)(?=\*\*|$)', activity_content, re.DOTALL)
        if outcomes:
            outcome_text = outcomes.group(1).strip()
            if outcome_text and outcome_text != '-' and len(outcome_text) > 10:
                for line in outcome_text.split('\n'):
                    line = line.strip()
                    if line and line.startswith('-') and len(line) > 10:
                        task_title = f"Complete: {line.lstrip('- ').strip()}"
                        tasks.append({
                            'title': task_title,
                            'priority': 'MEDIUM',
                            'status': 'Not Started',
                            'assignee': employee_name,
                            'date': date_folder,
                            'source_file': source_file,
                            'source_type': 'daily.md',
                            'context': f"Outcome from activity at {time}",
                            'content': f"**Outcome:** {outcome_text[:200]}..."
                        })
    
    return tasks

def extract_tasks_from_plans(plans_content, employee_name, date_folder, source_file):
    """Extract tasks from plans.md file content."""
    tasks = []
    
    # Skip template files
    if '[Date]' in plans_content and '## Instructions' in plans_content and len(plans_content) < 300:
        return tasks
    
    # Extract prioritized action items
    priority_sections = re.findall(r'###\s*(High|Medium|Low)\s+Priority\s*(.*?)(?=###|$)', plans_content, re.DOTALL | re.IGNORECASE)
    
    priority_map = {'high': 'HIGH', 'medium': 'MEDIUM', 'low': 'LOW'}
    
    for priority_level, section_content in priority_sections:
        priority = priority_map.get(priority_level.lower(), 'MEDIUM')
        
        # Extract task items (numbered or bulleted)
        task_items = re.findall(r'^\d+\.\s*\*\*?([^\n]+?)\*\*?\s*$', section_content, re.MULTILINE)
        if not task_items:
            task_items = re.findall(r'^\d+\.\s*([^\n]+?)(?:\n|$)', section_content, re.MULTILINE)
        
        for task_title in task_items:
            task_title = task_title.strip()
            if task_title and len(task_title) > 5 and '[Task Name]' not in task_title:
                # Extract goal, outcome, deadline if present
                task_section = re.search(rf'{re.escape(task_title)}.*?(?=^\d+\.|$)', section_content, re.DOTALL | re.MULTILINE)
                content = ""
                if task_section:
                    content = task_section.group(0)[:500]
                
                tasks.append({
                    'title': task_title,
                    'priority': priority,
                    'status': 'Not Started',
                    'assignee': employee_name,
                    'date': date_folder,
                    'source_file': source_file,
                    'source_type': 'plans.md',
                    'content': content
                })
    
    return tasks

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
            if 'completed' in status_lower or 'done' in status_lower or '✅' in title or 'COMPLETED' in status:
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
            
            task = {
                'title': title,
                'priority': priority,
                'status': status,
                'assignee': employee_name,
                'date': date_folder,
                'source_file': str(filepath),
                'source_type': 'task.md',
                'steps': steps,
                'resources': resources,
                'instructions': instructions,
                'content': full_content
            }
            
            tasks.append(task)
    
    except Exception as e:
        print(f"Error parsing {filepath}: {e}")
    
    return tasks

def collect_all_files(base_dir, dates, include_left=False):
    """Collect and parse all daily.md, plans.md, and task.md files."""
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
                    left_path = employee_folder
                    for left_employee_folder in left_path.iterdir():
                        if not left_employee_folder.is_dir() or left_employee_folder.name.startswith('.'):
                            continue
                        
                        # Process all three file types
                        for file_type in ['daily.md', 'plans.md', 'task.md', 'tasks.md']:
                            file_path = left_employee_folder / date_folder / file_type
                            if file_path.exists():
                                employee_name = left_employee_folder.name
                                try:
                                    with open(file_path, 'r', encoding='utf-8') as f:
                                        content = f.read()
                                    
                                    if file_type in ['daily.md']:
                                        tasks = extract_tasks_from_daily(content, employee_name, date_folder, str(file_path))
                                    elif file_type in ['plans.md']:
                                        tasks = extract_tasks_from_plans(content, employee_name, date_folder, str(file_path))
                                    else:  # task.md or tasks.md
                                        tasks = parse_task_file(file_path, employee_name, date_folder)
                                    
                                    all_tasks.extend(tasks)
                                    if tasks:
                                        print(f"Found {len(tasks)} tasks in Left/{employee_name}/{date_folder}/{file_type}")
                                except Exception as e:
                                    print(f"Error reading {file_path}: {e}")
                continue
            
            # Process all three file types
            for file_type in ['daily.md', 'plans.md', 'task.md', 'tasks.md']:
                file_path = employee_folder / date_folder / file_type
                if file_path.exists():
                    employee_name = employee_folder.name
                    try:
                        with open(file_path, 'r', encoding='utf-8') as f:
                            content = f.read()
                        
                        if file_type in ['daily.md']:
                            tasks = extract_tasks_from_daily(content, employee_name, date_folder, str(file_path))
                        elif file_type in ['plans.md']:
                            tasks = extract_tasks_from_plans(content, employee_name, date_folder, str(file_path))
                        else:  # task.md or tasks.md
                            tasks = parse_task_file(file_path, employee_name, date_folder)
                        
                        all_tasks.extend(tasks)
                        if tasks:
                            print(f"Found {len(tasks)} tasks in {employee_name}/{date_folder}/{file_type}")
                    except Exception as e:
                        print(f"Error reading {file_path}: {e}")
    
    return all_tasks

def normalize_title(title):
    """Normalize task title for comparison."""
    title = re.sub(r'^(Task \d+:\s*|Complete:\s*)', '', title, flags=re.IGNORECASE)
    title = re.sub(r'[✅🔄⏳]', '', title)
    title = re.sub(r'\s+', ' ', title)
    title = title.strip()
    return title.lower()

def group_and_merge_tasks(all_tasks):
    """Group similar tasks and merge duplicates."""
    active_tasks = [t for t in all_tasks if t['status'] != 'Completed']
    completed_tasks = [t for t in all_tasks if t['status'] == 'Completed']
    
    groups = []
    used_indices = set()
    
    for i, task in enumerate(active_tasks):
        if i in used_indices:
            continue
        
        group = [task]
        used_indices.add(i)
        
        for j, other_task in enumerate(active_tasks[i+1:], start=i+1):
            if j in used_indices:
                continue
            
            similarity = SequenceMatcher(
                None,
                normalize_title(task['title']),
                normalize_title(other_task['title'])
            ).ratio() * 100
            
            if similarity >= 85:
                group.append(other_task)
                used_indices.add(j)
        
        groups.append(group)
    
    merged_tasks = []
    for group in groups:
        if len(group) == 1:
            merged_tasks.append(group[0])
        else:
            main_task = group[0].copy()
            assignees = list(set([t['assignee'] for t in group]))
            main_task['assignee'] = ', '.join(assignees) if len(assignees) > 1 else assignees[0]
            
            status_priority = {'In Progress': 3, 'Not Started': 2, 'Planned': 1, 'Pending': 1}
            main_task['status'] = max(group, key=lambda t: status_priority.get(t['status'], 0))['status']
            
            dates = list(set([t['date'] for t in group]))
            main_task['date'] = ', '.join(sorted(dates))
            
            sources = [t['source_file'] for t in group]
            main_task['source_files'] = sources
            
            all_steps = []
            for t in group:
                all_steps.extend(t.get('steps', []))
            main_task['steps'] = list(dict.fromkeys(all_steps))
            
            merged_tasks.append(main_task)
    
    return merged_tasks, completed_tasks

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 process_all_daily_files.py <department_name> [--include-left]")
        print("Example: python3 process_all_daily_files.py AI")
        print("Example: python3 process_all_daily_files.py Video --include-left")
        sys.exit(1)
    
    department = sys.argv[1]
    include_left = '--include-left' in sys.argv
    
    base_dir = f'/Users/nikolay/Library/CloudStorage/Dropbox/Nov25/{department}'
    dates = ['05', '06', '07', '08', '09', '10', '11']
    
    if not os.path.exists(base_dir):
        print(f"Error: Department directory not found: {base_dir}")
        sys.exit(1)
    
    print(f"Collecting and parsing {department} department files (daily.md, plans.md, task.md)...")
    if include_left:
        print("Including Left folder...")
    
    all_tasks = collect_all_files(base_dir, dates, include_left=include_left)
    
    print(f"\nTotal tasks found: {len(all_tasks)}")
    
    print("\nGrouping and merging similar tasks...")
    merged_tasks, completed_tasks = group_and_merge_tasks(all_tasks)
    
    print(f"Unique active tasks after merging: {len(merged_tasks)}")
    print(f"Completed tasks: {len(completed_tasks)}")
    
    # Save to JSON
    output_file = os.path.join(base_dir, f'extracted_{department.lower()}_all_tasks.json')
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump({
            'active_tasks': merged_tasks,
            'completed_tasks': completed_tasks,
            'total_active': len(merged_tasks),
            'total_completed': len(completed_tasks),
            'source_files_processed': len(set([t.get('source_file', '') for t in all_tasks]))
        }, f, indent=2, ensure_ascii=False)
    
    print(f"\nSaved {len(merged_tasks)} active tasks and {len(completed_tasks)} completed tasks to {output_file}")
    
    # Print summary
    by_priority = defaultdict(int)
    by_status = defaultdict(int)
    by_employee = defaultdict(int)
    by_source_type = defaultdict(int)
    
    for task in merged_tasks:
        by_priority[task['priority']] += 1
        by_status[task['status']] += 1
        by_employee[task['assignee']] += 1
        by_source_type[task.get('source_type', 'unknown')] += 1
    
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
    
    print(f"\nBy Source Type:")
    for source_type in sorted(by_source_type.keys()):
        print(f"  {source_type}: {by_source_type[source_type]}")

if __name__ == '__main__':
    main()

