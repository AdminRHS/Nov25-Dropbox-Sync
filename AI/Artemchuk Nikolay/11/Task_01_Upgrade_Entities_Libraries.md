# Task 01: Upgrade Entities and Libraries with Department Templates

**Department:** AI  
**Status:** Not Started  
**Priority:** High  
**Assignee:** Artemchuk Nikolay (ID: 37226)  
**Date Created:** November 11, 2025

---

## Quick Info

- **Action:** Upgrade
- **Object:** Entities and Libraries
- **Tool:** Cursor, VS Code, file system access
- **Related Projects:** CRM, RAC

---

## Description

Modify entities in entities folder by integrating existing department task templates and step templates. Backup current prompts to v1 folders, create v2 versions based on v1 prompts upgraded with data from entities (libraries, task templates, task manager, talents, employees export). Include all entities, not just libraries.

---

## Full Template

```yaml
task_id: Task_01
task_name: Upgrade Entities and Libraries with Department Templates
metadata:
  status: Not Started
  priority: High
  created_date: '2025-11-11'
  extraction_date: '2025-11-11'
ownership:
  department: AI
  assigned_to: Artemchuk Nikolay (ID: 37226)
  profession: Project manager, Lead generator
taxonomy:
  action: Upgrade
  object: Entities and Libraries
  object_type: Entity Templates, Department Templates
  tool: Cursor, VS Code, file system access
  context: Entity-Integration, Template-Upgrade
dependencies:
  prerequisites:
  - Access to entities folder
  - Department template files
  - Existing prompts to backup
  related_tasks: []
  related_projects:
  - CRM
  - RAC (Remote AI Context)
deliverables:
- Backed up prompts in v1 folders
- Upgraded v2 versions of prompts with entity data
- Integrated department task templates
- Integrated department step templates
- Updated entities folder structure
source_tracking:
  source_file: daily_processed.md
  extraction_date: '2025-11-11'
  source_section: "3. ACTION ITEMS & TASKS - Upgrade Entities and Libraries with Department Templates"
```

---

## Steps

1. **Backup Current Prompts**
   - Identify all prompts in entities folder
   - Create v1 backup folders for each department
   - Copy current prompts to v1 folders

2. **Review Department Templates**
   - Identify existing department task templates
   - Identify existing department step templates
   - Document template structure and content

3. **Integrate Templates into Entities**
   - Map department templates to entity structure
   - Integrate task templates into entities
   - Integrate step templates into entities

4. **Upgrade Prompts with Entity Data**
   - Extract data from libraries
   - Extract data from task templates
   - Extract data from task manager
   - Extract data from talents
   - Extract data from employees export
   - Integrate all entity data into v2 prompts

5. **Create v2 Prompt Versions**
   - Create v2 folders for each department
   - Generate upgraded prompts with entity data
   - Ensure all entities are included (not just libraries)

6. **Validate and Test**
   - Review upgraded prompts for completeness
   - Test prompt functionality
   - Verify entity integration

7. **Document Changes**
   - Document upgrade process
   - Document entity integration
   - Update entity folder structure documentation

---

## Tools Required

- Cursor
- VS Code
- File system access
- Entity folder access
- Department template files

---

## Notes

- Include all entities, not just libraries
- Ensure proper backup before making changes
- Maintain version control (v1 → v2)
- Document all changes for future reference

---

**Source:** Extracted from daily_processed.md  
**Date:** 2025-11-11

