#!/usr/bin/env python3
"""
Extract all tasks from department consolidated task files and create individual task files
in TASK_MANAGERS structure.
"""

import re
import os
import sys
from pathlib import Path
from datetime import datetime

def extract_tasks_from_file(filepath):
    """Extract all tasks from a department task file."""
    tasks = []
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find department name from file path
    dept_match = re.search(r'/([A-Z][a-z]*)/.*Department Tasks', str(filepath))
    if dept_match:
        department = dept_match.group(1)
    else:
        # Try alternative pattern
        dept_match2 = re.search(r'/(AI|Design|Dev|LG|Video)/', str(filepath))
        department = dept_match2.group(1) if dept_match2 else "UNKNOWN"
    
    # Extract all task sections (#### number. Title)
    task_pattern = r'#### (\d+)\.\s*([^\n]+)\n(.*?)(?=#### \d+\.|## |$)'
    matches = re.finditer(task_pattern, content, re.DOTALL)
    
    for match in matches:
        task_num = match.group(1)
        title = match.group(2).strip()
        task_content = match.group(3)
        
        # Extract metadata
        owner_match = re.search(r'- \*\*Owner:\*\*\s*([^\n]+)', task_content)
        owner = owner_match.group(1).strip() if owner_match else "Unassigned"
        
        # Also check for Department field which might override
        dept_match = re.search(r'- \*\*Department:\*\*\s*([^\n]+)', task_content)
        if dept_match:
            dept_from_task = dept_match.group(1).strip()
            # Extract department name (might be "AI / LG" or "Design, Operations" or just "AI")
            if '/' in dept_from_task:
                department = dept_from_task.split('/')[0].strip()
            elif ',' in dept_from_task:
                # Take first department if comma-separated
                department = dept_from_task.split(',')[0].strip()
            else:
                department = dept_from_task
        
        priority_match = re.search(r'- \*\*Priority:\*\*\s*([^\n]+)', task_content)
        priority = priority_match.group(1).strip() if priority_match else "MEDIUM"
        
        status_match = re.search(r'- \*\*Status:\*\*\s*([^\n]+)', task_content)
        status = status_match.group(1).strip() if status_match else "Not Started"
        
        timeline_match = re.search(r'- \*\*Timeline:\*\*\s*([^\n]+)', task_content)
        timeline = timeline_match.group(1).strip() if timeline_match else ""
        
        # Extract profession
        profession_match = re.search(r'- \*\*Profession:\*\*\s*([^\n]+)', task_content)
        profession = profession_match.group(1).strip() if profession_match else ""
        
        # Extract steps
        steps_match = re.search(r'\*\*Steps:\*\*\s*(.*?)(?=\*\*|$)', task_content, re.DOTALL)
        steps = []
        if steps_match:
            steps_text = steps_match.group(1)
            step_lines = re.findall(r'^\d+\.\s*(.+)$', steps_text, re.MULTILINE)
            steps = [s.strip() for s in step_lines if s.strip()]
        
        # Extract context/description
        context_match = re.search(r'\*\*Context:\*\*\s*(.*?)(?=\*\*|$)', task_content, re.DOTALL)
        context = context_match.group(1).strip() if context_match else ""
        
        # Extract resources
        resources_match = re.search(r'\*\*Resources?:\*\*\s*(.*?)(?=\*\*|$)', task_content, re.DOTALL)
        resources = []
        if resources_match:
            resources_text = resources_match.group(1)
            resource_lines = re.findall(r'^-\s*(.+)$', resources_text, re.MULTILINE)
            resources = [r.strip() for r in resource_lines if r.strip()]
        
        # Extract instructions
        instructions_match = re.search(r'\*\*Instructions?:\*\*\s*(.*?)(?=\*\*|$)', task_content, re.DOTALL)
        instructions = instructions_match.group(1).strip() if instructions_match else ""
        
        # Determine action and object from title
        action, object_part = parse_action_object(title)
        
        task = {
            'number': task_num,
            'title': title,
            'department': department,
            'owner': owner,
            'priority': priority,
            'status': status,
            'timeline': timeline,
            'steps': steps,
            'context': context,
            'resources': resources,
            'instructions': instructions,
            'content': task_content,
            'profession': profession
        }
        
        tasks.append(task)
    
    return tasks

def parse_action_object(title):
    """Parse action and object from task title."""
    # Common action verbs (longer ones first to match correctly)
    actions = ['Schedule & Organize', 'Complete Technical Setup', 'Create Video Tutorial',
               'Create Standalone', 'Process Video Transcriptions', 'Update Video Transcription',
               'Review and Optimize', 'Review and Organize', 'Review and Test', 'Review and Respond',
               'Create or Update', 'Create New', 'Complete Remaining', 'Complete Secondary',
               'Create', 'Update', 'Complete', 'Review', 'Implement', 'Develop', 'Design', 
               'Process', 'Document', 'Schedule', 'Distribute', 'Test', 'Fix', 'Optimize',
               'Monitor', 'Research', 'Analyze', 'Build', 'Setup', 'Configure', 'Install',
               'Train', 'Organize', 'Separate', 'Upload', 'Export', 'Import', 'Verify',
               'Finalize', 'Troubleshoot', 'Resolve', 'Coordinate', 'Prepare', 'Send',
               'Add', 'Remove', 'Delete', 'Edit', 'Modify', 'Generate', 'Extract', 'Write',
               'Formulate', 'Identify', 'Port', 'Standardize', 'Address', 'Explore', 'Investigate']
    
    title_lower = title.lower()
    action = "Complete"
    object_part = title
    
    # Try to match longer action phrases first
    for act in sorted(actions, key=len, reverse=True):
        if title_lower.startswith(act.lower()):
            action = act
            object_part = title[len(act):].strip()
            # Remove common prefixes
            if object_part.startswith(':') or object_part.startswith(' -') or object_part.startswith(' - '):
                object_part = re.sub(r'^[:\s-]+', '', object_part)
            break
    
    return action, object_part

def normalize_priority(priority):
    """Normalize priority to standard format."""
    priority_lower = priority.lower()
    if 'critical' in priority_lower:
        return 'High'
    elif 'high' in priority_lower:
        return 'High'
    elif 'medium' in priority_lower:
        return 'Medium'
    elif 'low' in priority_lower:
        return 'Low'
    return 'Medium'

def normalize_status(status):
    """Normalize status to standard format."""
    status_lower = status.lower()
    if 'completed' in status_lower or 'done' in status_lower:
        return 'Done'
    elif 'in progress' in status_lower or 'progress' in status_lower:
        return 'In Progress'
    elif 'not started' in status_lower or 'pending' in status_lower:
        return 'Not Started'
    elif 'waiting' in status_lower or 'blocked' in status_lower:
        return 'In Progress'
    return 'Not Started'

def extract_employee_id(owner_text):
    """Extract employee ID from owner text if present."""
    id_match = re.search(r'\(ID:\s*(\d+)\)', owner_text)
    return id_match.group(1) if id_match else None

def create_task_file(task, dept_code, task_counter, output_dir):
    """Create individual task file in TASK_MANAGERS format."""
    # Generate task ID
    task_id = f"{dept_code}-{task_counter:03d}"
    filename = f"{task_id}_{task['title'].replace(' ', '_').replace('/', '_').replace(':', '')[:50]}.md"
    
    # Limit filename length
    if len(filename) > 100:
        filename = f"{task_id}_{task_counter:03d}.md"
    
    filepath = output_dir / filename
    
    # Extract employee ID
    employee_id = extract_employee_id(task['owner'])
    owner_name = task['owner'].split('(')[0].strip() if '(' in task['owner'] else task['owner']
    
    # Build markdown content
    md_content = f"# {task_id}: {task['title']}\n\n"
    md_content += f"**Department:** {task['department']}\n"
    md_content += f"**Status:** {normalize_status(task['status'])}\n"
    md_content += f"**Priority:** {normalize_priority(task['priority'])}\n"
    md_content += f"**Assignee:** {owner_name}"
    if employee_id:
        md_content += f" (ID: {employee_id})"
    md_content += "\n"
    md_content += f"**Date Created:** {datetime.now().strftime('%B %d, %Y')}\n"
    
    if task['timeline']:
        md_content += f"**Timeline:** {task['timeline']}\n"
    
    md_content += "\n---\n\n"
    
    # Quick Info
    action, object_part = parse_action_object(task['title'])
    md_content += "## Quick Info\n\n"
    md_content += f"- **Action:** {action}\n"
    md_content += f"- **Object:** {object_part}\n"
    
    # Extract tools from resources
    tools = []
    for res in task['resources']:
        if any(tool in res for tool in ['VS Code', 'Cursor', 'Git', 'Dropbox', 'Figma', 'Notion', 'CRM', 'Google', 'Discord', 'Email', 'Whisper', 'Perplexity', 'ChatGPT', 'Claude', 'Adobe', 'PowerPoint', 'Excel', 'ZOHO', 'TurboScribe']):
            tools.append(res)
    
    if tools:
        md_content += f"- **Tool:** {', '.join(tools[:3])}\n"
    else:
        md_content += "- **Tool:** TBD\n"
    
    # Related projects (extract from context/content)
    projects = []
    if 'CRM' in task['content']:
        projects.append('CRM')
    if 'RAC' in task['content'] or 'Remote AI Context' in task['content']:
        projects.append('RAC')
    if 'File System' in task['content']:
        projects.append('File System')
    if 'Lead Generation' in task['content'] or 'LG' in task['content']:
        projects.append('Lead Generation')
    if 'Game Academy' in task['content']:
        projects.append('Game Academy')
    if 'Data Mining' in task['content']:
        projects.append('Data Mining')
    if 'Hanni Stone' in task['content'] or 'Honeystone' in task['content']:
        projects.append('Hanni Stone')
    if 'Storyboard' in task['content']:
        projects.append('Storyboard')
    if 'MOSIK' in task['content']:
        projects.append('MOSIK')
    
    if projects:
        md_content += f"- **Related Projects:** {', '.join(projects)}\n"
    
    md_content += "\n---\n\n"
    
    # Description
    md_content += "## Description\n\n"
    if task['context']:
        md_content += task['context'] + "\n\n"
    elif task['instructions']:
        md_content += task['instructions'] + "\n\n"
    else:
        md_content += task['title'] + "\n\n"
    
    # Full Template (YAML)
    md_content += "## Full Template\n\n"
    md_content += "```yaml\n"
    md_content += f"task_id: {task_id}\n"
    md_content += f"task_name: {task['title']}\n"
    md_content += "metadata:\n"
    md_content += f"  status: {normalize_status(task['status'])}\n"
    md_content += f"  priority: {normalize_priority(task['priority'])}\n"
    md_content += f"  created_date: '{datetime.now().strftime('%Y-%m-%d')}'\n"
    md_content += f"  extraction_date: '{datetime.now().strftime('%Y-%m-%d')}'\n"
    md_content += "ownership:\n"
    md_content += f"  department: {task['department']}\n"
    md_content += f"  assigned_to: {owner_name}"
    if employee_id:
        md_content += f" (ID: {employee_id})"
    md_content += "\n"
    
    # Extract profession from task data or infer
    profession = task.get('profession', '')
    if not profession:
        if 'Project manager' in task['owner'] or 'PM' in task['owner']:
            profession = "Project manager"
        elif 'Designer' in task['owner'] or 'Design' in task['content']:
            profession = "Designer"
        elif 'Developer' in task['owner'] or 'Dev' in task['content']:
            profession = "Developer"
        elif 'Lead generator' in task['owner'] or 'LG' in task['content']:
            profession = "Lead generator"
        elif 'Video Editor' in task['owner'] or 'Video' in task['content']:
            profession = "Video Editor"
        else:
            profession = "Team member"
    
    md_content += f"  profession: {profession}\n"
    md_content += "taxonomy:\n"
    md_content += f"  action: {action}\n"
    md_content += f"  object: {object_part}\n"
    md_content += f"  object_type: Task\n"
    if tools:
        md_content += f"  tool: {', '.join(tools[:2])}\n"
    md_content += f"  context: {task['department']}-Department\n"
    md_content += "dependencies:\n"
    md_content += "  prerequisites: []\n"
    md_content += "  related_tasks: []\n"
    if projects:
        md_content += "  related_projects:\n"
        for proj in projects:
            md_content += f"  - {proj}\n"
    else:
        md_content += "  related_projects: []\n"
    md_content += "deliverables:\n"
    if task['steps']:
        md_content += f"- Complete: {task['title']}\n"
    else:
        md_content += f"- {task['title']}\n"
    md_content += "source_tracking:\n"
    md_content += f"  source_file: {task['department']} Department Tasks - November 2025.md\n"
    md_content += f"  extraction_date: '{datetime.now().strftime('%Y-%m-%d')}'\n"
    md_content += f"  source_section: Task {task['number']}\n"
    md_content += "```\n\n"
    md_content += "---\n\n"
    
    # Steps
    if task['steps']:
        md_content += "## Steps\n\n"
        for i, step in enumerate(task['steps'], 1):
            md_content += f"{i}. **{step}**\n"
            md_content += "   - Description: " + step + "\n"
            md_content += "   - Status: Not Started\n\n"
    else:
        md_content += "## Steps\n\n"
        md_content += "1. **Review task requirements**\n"
        md_content += "   - Description: Understand task scope and objectives\n"
        md_content += "   - Status: Not Started\n\n"
    
    # Tools Required
    md_content += "## Tools Required\n\n"
    if tools:
        for tool in tools[:5]:
            md_content += f"- {tool}\n"
    else:
        md_content += "- TBD\n"
    md_content += "\n"
    
    # Notes
    md_content += "## Notes\n\n"
    if task['instructions']:
        md_content += task['instructions'] + "\n\n"
    elif task['context']:
        md_content += task['context'] + "\n\n"
    else:
        md_content += f"Task extracted from {task['department']} Department Tasks file.\n\n"
    
    md_content += "---\n\n"
    md_content += f"**Source:** {task['department']} Department Tasks - November 2025.md\n"
    md_content += f"**Date:** {datetime.now().strftime('%Y-%m-%d')}\n"
    
    # Write file
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(md_content)
    
    return filepath

def main():
    departments = {
        'AI': 'AI',
        'Design': 'DESIGN',
        'Dev': 'DEV',
        'LG': 'LG',
        'Video': 'VIDEO'
    }
    
    base_dir = Path('/Users/nikolay/Library/CloudStorage/Dropbox/Nov25')
    output_dir = Path('/Users/nikolay/Library/CloudStorage/Dropbox/Taxonomy/Entities/TASK_MANAGERS/Tasks')
    
    # Create output directory if it doesn't exist
    output_dir.mkdir(parents=True, exist_ok=True)
    
    all_tasks = []
    
    # Process each department
    for dept_name, dept_code in departments.items():
        task_file = base_dir / dept_name / f'{dept_name} Department Tasks - November 2025.md'
        
        if not task_file.exists():
            print(f"Warning: {task_file} not found, skipping...")
            continue
        
        print(f"\nProcessing {dept_name} department...")
        tasks = extract_tasks_from_file(task_file)
        print(f"  Found {len(tasks)} tasks")
        
        # Create task files
        task_counter = 1
        for task in tasks:
            try:
                filepath = create_task_file(task, dept_code, task_counter, output_dir)
                all_tasks.append({
                    'id': f"{dept_code}-{task_counter:03d}",
                    'title': task['title'],
                    'file': filepath.name
                })
                task_counter += 1
            except Exception as e:
                print(f"  Error creating task file: {e}")
                continue
    
    print(f"\n✅ Created {len(all_tasks)} task files in {output_dir}")
    print(f"\nTask files created:")
    for task in all_tasks[:20]:  # Show first 20
        print(f"  - {task['id']}: {task['title'][:60]}...")
    if len(all_tasks) > 20:
        print(f"  ... and {len(all_tasks) - 20} more")

if __name__ == '__main__':
    main()

