# Prompt Parts Constructor - Documentation

## Overview

This folder contains the JSON structure and rules for constructing department-specific daily report prompts. The system defines how prompt parts are formed, classified, and assembled.

---

## Files

### `prompt_parts_structure.json`
Main JSON file containing:
- Prompt section definitions
- Classification system
- Formation rules
- Data source mappings
- Department configurations
- Templates and validation rules

---

## Structure Overview

### 1. Metadata
- Version information
- Creation date
- Purpose and author

### 2. Prompt Structure
Defines all 10 sections with:
- **ID**: Unique identifier
- **Name**: Human-readable name
- **Classification**: Type (header, context, instructions, etc.)
- **Category**: Grouping (introduction, department_specific, standard)
- **Required**: Boolean requirement flag
- **Order**: Sequence number
- **Template**: Text template with variables
- **Variables**: List of required variables
- **Validation Rules**: Rules for content validation

### 3. Classifications
Three classification systems:
- **By Type**: Groups sections by their nature
- **By Category**: Groups sections by their purpose
- **By Requirement**: Separates required vs optional sections

### 4. Formation Rules
- **Section Order**: Enforces correct sequence
- **Variable Substitution**: Rules for replacing variables
- **Dependency Rules**: What each section depends on
- **Validation Rules**: Completeness and correctness checks

### 5. Data Sources
Maps to external data files:
- Employee Directory
- Project Directory
- Tools Library
- Vocabulary Library

### 6. Department Configurations
Specific settings for each department:
- Folder paths
- Section mappings
- Focus areas
- Activity descriptions

### 7. Templates
Reusable template strings for:
- Section templates
- Entry formats
- Standard structures

### 8. Generation Rules
Step-by-step process for:
- Prompt construction
- Validation checks
- File generation

---

## Section Classifications

### By Type
- **Header**: Introduction sections (Purpose)
- **Context**: Information sections (Department Context, Base Context)
- **Instructions**: Action-oriented sections (Department Instructions)
- **Reference**: Reference sections (Vocabulary, Project Matching)
- **Standards**: Quality and format sections (Quality Standards)
- **Example**: Usage examples (Example Usage)
- **Metadata**: Version and footer information

### By Category
- **Introduction**: Purpose and overview
- **Department Specific**: Customized for each department
- **Integration**: References to base documents
- **Standard**: Common across all departments

---

## Usage

### To Generate a New Department Prompt:

1. **Load Configuration**
   ```json
   {
     "department": "HR",
     "department_folder": "HR Nov25",
     "team_size": 2
   }
   ```

2. **Fetch Data**
   - Employees from employee directory
   - Projects from project directory
   - Tools from tools library
   - Vocabulary from vocabulary library

3. **Apply Templates**
   - Substitute variables in templates
   - Format data according to templates
   - Assemble sections in order

4. **Validate**
   - Check all required sections present
   - Verify all variables substituted
   - Validate formatting and structure

5. **Generate**
   - Create markdown file
   - Save to appropriate location

---

## Section Dependencies

```
Purpose
  ↓
Department Context
  ├── Employee Directory
  ├── Project Directory
  └── Tools Library
  ↓
Base Context Integration
  ├── MAIN PROMPT v3.md
  └── PROMPT_Daily_Report_Collection.md
  ↓
Department Instructions
  └── Department Context
  ↓
Department Vocabulary
  └── Vocabulary Library
  ↓
Project Matching
  └── Project Directory
  ↓
Quality Standards
Example Usage
Version History
Footer
```

---

## Variable Substitution

All variables follow the format: `{variable_name}`

### Common Variables:
- `{department_name}` - Department name (e.g., "HR", "AI")
- `{department_folder}` - Folder path (e.g., "HR Nov25")
- `{DAY}` - Day number (e.g., "05", "25")
- `{team_size}` - Number of employees
- `{employee_name}` - Employee full name
- `{employee_id}` - Employee ID number
- `{project_name}` - Project name
- `{tool_name}` - Tool name

---

## Validation Rules

### Section Completeness
- All 10 required sections must be present
- Subsections must be complete
- All variables must be substituted

### Content Validation
- Minimum/maximum lengths enforced
- Required keywords must be present
- Format consistency checked

### Dependency Validation
- Data sources must be accessible
- References must be valid
- Links must be correct

---

## Department-Specific Customizations

Each department has:
- **Section Mappings**: Which MAIN PROMPT sections to emphasize
- **Focus Areas**: What to highlight in reports
- **Activity Descriptions**: How to describe activities
- **Tool Usage**: How to describe tool usage
- **Deliverables**: How to describe deliverables

---

## Example: HR Department

```json
{
  "department": "HR",
  "department_folder": "HR Nov25",
  "section_mapping": [20, 16, 3],
  "focus_areas": [
    "Recruitment activities (CVs, interviews, job postings)",
    "Onboarding activities (training, documentation, tool setup)",
    "Employee management (directory updates, status changes)",
    "HR-specific metrics and statistics"
  ],
  "activities": "recruitment and onboarding activities",
  "tool_usage": "HR tool usage",
  "deliverables": "HR deliverables"
}
```

---

## Extending the System

### Adding a New Department:

1. Add department configuration to `department_configurations`
2. Define section mappings
3. Specify focus areas
4. Add vocabulary categories if needed
5. Test generation

### Adding a New Section:

1. Add section definition to `sections` array
2. Assign classification and category
3. Define template and variables
4. Update dependencies if needed
5. Add to required sections list

### Modifying Templates:

1. Update template string in `templates` section
2. Update variable list
3. Test with all departments
4. Validate output

---

## Version History

**v1.0** - November 25, 2025
- Initial JSON structure creation
- All 7 departments configured
- Complete classification system
- Formation rules defined
- Validation rules established

---

## Notes

- All paths are relative to `Dropbox/Nov25/`
- Department folders follow pattern: `{Department} Nov25`
- Report folders follow pattern: `Reports/{DAY}/`
- File naming: `PROMPT_{Department}_Daily_Report.md`
- Report naming: `Daily_Activity_Report_Nov{DAY}_2025.md`

---

*Last Updated: November 25, 2025*

