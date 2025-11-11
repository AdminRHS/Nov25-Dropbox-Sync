# Call Transcription Processing - Daily Discussion

**Processed Date:** November 11, 2025  
**Source File:** daily.md  
**Processing Prompt:** MAIN PROMPT v3.1  
**Language:** Russian/Ukrainian (mixed)

---

## 1. MEETING METADATA

**Date:** November 11, 2025 (inferred from folder structure)

**Participants:**
- **Artemchuk Nikolay** (ID: 37226) - Project manager, Lead generator | AI | Confidence: High
  - Referenced as "Коля Артемчук" / "Коля" in transcript
  - Primary speaker discussing entities, employee data, and automation
- **Unknown Participant** - Unknown | Possibly AI Department | Confidence: Low - *Requires manual verification*
  - Referenced in conversation ("ты", "твой фреймворк")
  - Likely a colleague working on similar projects

**Duration:** Not specified

**Main Topics:**
1. Entities and libraries modification with department templates
2. CRM employee data export processing and filtering
3. Employee folder structure and automation architecture
4. Research and knowledge base collection processes
5. Script-based preprocessing for large files and token optimization

**Related Project(s):**
- **CRM** - Matched from Project Directory - Confidence: High
  - Discussion of employees.json export file processing
- **Online Academy** - Matched from Project Directory - Confidence: High
  - Mentioned for knowledge base integration and content tagging
- **RAC (Remote AI Context)** - Referenced in discussion - Confidence: High
  - Knowledge base system mentioned for research collection

**Related Platforms:** 
- Recruitment Platform (employee data processing)
- Infrastructure (automation and scripting systems)

**Department(s) Involved:** 
- **AI** (Primary) - Entities, prompts, automation, scripting
- **HR** (Secondary) - Employee data management
- **All Departments** (Future) - Employee folder structure, Daily Prompt improvements

---

## 2. EXECUTIVE SUMMARY

The discussion focused on three main strategic directions for improving Remote Helpers' AI-first operations: (1) upgrading entities and libraries by integrating department-specific task and step templates, requiring backup of existing prompts to v1 folders and creation of v2 versions enhanced with entity data; (2) processing the massive CRM employee export file (employees.json with ~97,000 lines) to filter and create a smaller, manageable dataset for importing into the new Talent service, requiring script-based preprocessing due to token limitations; and (3) establishing an employee folder structure with scripts, agents, libraries, and templates to enable individual-level data processing and knowledge management. Key decisions included moving from department-level to individual employee folders for better data identification and processing, implementing script-based preprocessing for large files to save tokens, creating department-specific Daily Prompts with automated daily report generation, and establishing a centralized research/knowledge base collection system. The strategic direction emphasizes AI-first automation, token optimization through scripting, and individual employee knowledge containers that can aggregate research and learning materials.

---

## 3. ACTION ITEMS & TASKS

### Upgrade Entities and Libraries with Department Templates
- **Description:** Modify entities in entities folder by integrating existing department task templates and step templates. Backup current prompts to v1 folders, create v2 versions based on v1 prompts upgraded with data from entities (libraries, task templates, task manager, talents, employees export). Include all entities, not just libraries.
- **Owner/Assignee:** Artemchuk Nikolay (ID: 37226)
- **Department:** AI
- **Profession:** Project manager, Lead generator
- **Priority:** High
- **Timeline:** Not specified
- **Dependencies:** Access to entities folder, department template files
- **Status:** Not Started
- **Related Project:** CRM, RAC
- **Task Template:** Upgrade + Entities/Libraries
- **Tools Required:** Cursor, VS Code, file system access

### Process CRM Employee Export File
- **Description:** Process employees.json file from CRM export (~97,000 lines, ~500 lines per employee). Filter to find employees with "institution date" field. Extract from Google Drive folder (people/employees with "available" status). Create mini-file for import into Talent service. Archive original file to backup location.
- **Owner/Assignee:** Artemchuk Nikolay (ID: 37226)
- **Department:** AI
- **Profession:** Project manager, Lead generator
- **Priority:** Critical
- **Timeline:** Not specified
- **Dependencies:** Access to CRM export, Google Drive folder, script development
- **Status:** In Progress (units folder already created)
- **Related Project:** CRM, Recruitment Platform
- **Task Template:** Process + Employee Export File
- **Tools Required:** Scripts, Google Drive, CRM system

### Create Employee Folder Structure
- **Description:** Establish employee folder structure containing: scripts/, agents/, library/, template/ subfolders. Library may contain templates, mini-entities (department-specific), AI tokens, connected agents (email, Google Calendar, Online Academy). Enable individual employee-level processing and knowledge management.
- **Owner/Assignee:** Artemchuk Nikolay (ID: 37226)
- **Department:** AI
- **Profession:** Project manager, Lead generator
- **Priority:** High
- **Timeline:** Not specified
- **Dependencies:** Folder structure design, script development
- **Status:** Planning
- **Related Project:** RAC, Recruitment Platform
- **Task Template:** Create + Employee Folder Structure
- **Tools Required:** File system, Cursor, VS Code

### Develop Department-Specific Daily Prompts
- **Description:** Create separate Daily Prompt versions for each department. Store in department folders. Develop Cursor Rules or Composer Skills to automatically run prompts at end of each day, scan department folders, and generate Daily Reports automatically.
- **Owner/Assignee:** Artemchuk Nikolay (ID: 37226)
- **Department:** AI
- **Profession:** Project manager, Lead generator
- **Priority:** High
- **Timeline:** Not specified
- **Dependencies:** Daily Prompt template, Cursor Rules/Composer setup
- **Status:** Planning
- **Related Project:** RAC
- **Task Template:** Develop + Daily Prompt (Department-Specific)
- **Tools Required:** Cursor, Composer, prompt templates

### Create Research and Knowledge Base Collection Process
- **Description:** Establish process for collecting research materials (videos, articles) into centralized knowledge base/library. Define what to collect and where to put it. Enable employees to conduct their own research that aggregates into central database. Eventually push to Online Academy. Create research plan template that can be populated by AI recommendations.
- **Owner/Assignee:** Artemchuk Nikolay (ID: 37226)
- **Department:** AI
- **Profession:** Project manager, Lead generator
- **Priority:** Medium
- **Timeline:** Not specified
- **Dependencies:** Knowledge base structure, research template
- **Status:** Planning
- **Related Project:** RAC, Online Academy
- **Task Template:** Create + Research Collection Process
- **Tools Required:** Knowledge base system, Online Academy platform

### Develop Scripts for Large File Processing
- **Description:** Create scripts to process large files (50k+ lines) that exceed AI token limits. Scripts should: extract content from files, encode to UTF-8, clean empty fields, generate reports, extract and filter data. Scripts can be triggered by n8n actions or other automation tools. Save tokens by preprocessing before AI processing.
- **Owner/Assignee:** Artemchuk Nikolay (ID: 37226)
- **Department:** AI
- **Profession:** Project manager, Lead generator
- **Priority:** Critical
- **Timeline:** Not specified
- **Dependencies:** Script development environment, n8n setup
- **Status:** Planning
- **Related Project:** CRM, Infrastructure
- **Task Template:** Develop + Processing Scripts
- **Tools Required:** Scripting language, n8n, file processing tools

### Set Up GitHub Actions and Repositories
- **Description:** Establish GitHub repositories and GitHub Actions for automation workflows. Connect with GitHub MCP and Cursor Rules. Enable script-based automation that can run on GitHub infrastructure. Make scripts and automation accessible via GitHub.
- **Owner/Assignee:** Artemchuk Nikolay (ID: 37226)
- **Department:** AI
- **Profession:** Project manager, Lead generator
- **Priority:** Medium
- **Timeline:** Not specified
- **Dependencies:** GitHub account, repository setup, MCP configuration
- **Status:** Planning
- **Related Project:** Infrastructure
- **Task Template:** Set Up + GitHub Automation
- **Tools Required:** GitHub, GitHub Actions, GitHub MCP, Cursor

### Create Mini-Frameworks/Prompts for Individual Employees
- **Description:** Develop mini-frameworks and prompts designed for processing individual employee data. Each prompt should process one employee at a time to stay within token limits. Frameworks should be profession-specific. Use AI to help generate these mini-frameworks.
- **Owner/Assignee:** Artemchuk Nikolay (ID: 37226)
- **Department:** AI
- **Profession:** Project manager, Lead generator
- **Priority:** High
- **Timeline:** Not specified
- **Dependencies:** Employee folder structure, profession templates
- **Status:** Planning
- **Related Project:** RAC, Recruitment Platform
- **Task Template:** Create + Mini-Frameworks (Employee-Specific)
- **Tools Required:** AI tools (Claude, ChatGPT), prompt templates

### Process Agent Transcription Summaries
- **Description:** Process two existing transcriptions about agents. Extract summaries and key information. Use to inform agent development and integration into employee folder structure.
- **Owner/Assignee:** Artemchuk Nikolay (ID: 37226)
- **Department:** AI
- **Profession:** Project manager, Lead generator
- **Priority:** Low
- **Timeline:** Not specified
- **Dependencies:** Access to transcription files
- **Status:** Not Started
- **Related Project:** RAC
- **Task Template:** Process + Agent Transcriptions
- **Tools Required:** Transcription files, AI processing tools

### Enhance Daily Prompt with Research Recommendations
- **Description:** Add "what is next step recommendation" and "what research is missing" fields to Daily Prompt. Enable AI to suggest research topics that need deeper exploration. Extract both tasks and research items from daily processing.
- **Owner/Assignee:** Artemchuk Nikolay (ID: 37226)
- **Department:** AI
- **Profession:** Project manager, Lead generator
- **Priority:** Medium
- **Timeline:** Not specified
- **Dependencies:** Daily Prompt template
- **Status:** Planning
- **Related Project:** RAC
- **Task Template:** Enhance + Daily Prompt
- **Tools Required:** Prompt templates, AI tools

---

## 4. PROJECTS & FEATURES

### CRM - Employee Data Processing Enhancement
**Project Match:** **CRM** - Matched from Project Directory - Confidence: High

**Status:** In Development

**Platform:** Recruitment Platform

**Description:** Processing and filtering employee data from CRM export for import into new Talent service. Addressing data structure issues (department vs team, position vs profession) and creating manageable datasets from large export files.

**Key Features:**
- Employee export file processing (employees.json)
- Data filtering by institution date
- Unit-based data structure (one unit = one employee section)
- Mini-file creation for service import
- Data validation and cleaning

**Current Issues:**
- Large file size (~97,000 lines) exceeds AI processing capabilities
- Data structure inconsistencies (old CRM, third-party created)
- Missing or incorrect field mappings (department/team, position/profession)
- Need for script-based preprocessing

**Next Steps:**
1. Develop scripts for file processing and filtering
2. Create unit-based data extraction
3. Validate and clean employee data
4. Generate mini-file for Talent service import
5. Archive original export file

**Stakeholders:**
- **Artemchuk Nikolay** (ID: 37226) - AI Department

**Related Resources:**
- Google Drive: people/employees folder
- CRM export: employees.json
- Units folder structure (already created)

**AI Integration:** Script-based preprocessing to reduce token usage, AI-assisted data validation and cleaning

### Online Academy - Knowledge Base Integration
**Project Match:** **Online Academy** - Matched from Project Directory - Confidence: High

**Status:** Planning

**Platform:** Infrastructure

**Description:** Integrating employee research and knowledge base materials into Online Academy platform. Enabling content tagging, template identification, and structured knowledge aggregation.

**Key Features:**
- Research material collection and aggregation
- Content tagging with headers and templates
- JSON content structure for course materials
- Template identification in text (actions, objects)
- Knowledge push to Online Academy platform

**Current Issues:**
- No defined process for research collection
- Missing guidelines for what to collect and where
- Need for centralized knowledge base structure

**Next Steps:**
1. Define research collection process
2. Create knowledge base structure
3. Develop content tagging system
4. Integrate with Online Academy platform
5. Enable employee-level research contribution

**Stakeholders:**
- **Artemchuk Nikolay** (ID: 37226) - AI Department

**Related Resources:**
- Online Academy platform
- Research materials (videos, articles)
- Knowledge base/library structure

**AI Integration:** AI-assisted content tagging, template extraction, research recommendation generation

### RAC (Remote AI Context) - Research and Knowledge Management
**Project Match:** **RAC System** - Referenced in discussion - Confidence: High

**Status:** Enhancement Planning

**Platform:** Infrastructure

**Description:** Enhancing RAC system with research collection processes, knowledge base aggregation, and automated daily report generation. Moving toward individual employee-level knowledge management.

**Key Features:**
- Research plan template with AI recommendations
- Knowledge base aggregation from employee research
- Automated daily report generation
- Department-specific prompt processing
- Employee folder integration

**Current Issues:**
- Missing research collection guidelines
- No centralized knowledge aggregation process
- Daily reports require manual processing
- Need for automated workflows

**Next Steps:**
1. Create research collection guidelines
2. Develop knowledge base aggregation process
3. Implement automated daily report generation
4. Integrate with employee folder structure
5. Enable AI-powered research recommendations

**Stakeholders:**
- **Artemchuk Nikolay** (ID: 37226) - AI Department

**Related Resources:**
- RAC GitHub repository
- Research materials
- Daily Prompt templates

**AI Integration:** AI-powered research recommendations, automated report generation, content analysis and tagging

---

## 5. WORKFLOWS & PROCESSES

### Employee Folder Creation Workflow

**Purpose:** Establish standardized employee folder structure enabling individual-level data processing, knowledge management, and automation.

**SOP Reference:** Employee Folder Structure Template (to be created)

**Steps:**
1. Create base employee folder
   - **Responsibility:** HR/AI Department
   - **Tool:** File system, Cursor
   - **Placement:** Department employee directory
2. Create subfolder structure (scripts/, agents/, library/, template/)
   - **Responsibility:** AI Department
   - **Tool:** File system
   - **Placement:** Within employee folder
3. Populate library with department-specific mini-entities and templates
   - **Responsibility:** AI Department
   - **Tool:** Entity templates, file system
   - **Placement:** library/ subfolder
4. Configure agents (email, Google Calendar, Online Academy)
   - **Responsibility:** AI Department
   - **Tool:** Agent configuration tools
   - **Placement:** agents/ subfolder
5. Set up AI tokens and access credentials
   - **Responsibility:** AI Department
   - **Tool:** Credential management
   - **Placement:** Secure storage within folder

**Responsible Parties:**
- **Accountable:** Artemchuk Nikolay (ID: 37226) - AI Department
- **Responsible:** AI Department team
- **Consulted:** HR Department
- **Informed:** All departments

**Tools/Platforms Used:** File system, Cursor, VS Code, agent configuration tools, credential management

**Success Criteria:** 
- All employees have standardized folder structure
- Subfolders contain appropriate templates and configurations
- Agents are connected and functional
- Individual-level processing is enabled

**Automation Opportunities:** 
- Automated folder creation script
- Template population automation
- Agent configuration automation via scripts

### Research Collection and Knowledge Base Workflow

**Purpose:** Collect research materials from employees, process and tag content, and aggregate into centralized knowledge base for eventual push to Online Academy.

**SOP Reference:** Research Collection Guidelines (to be created)

**Steps:**
1. Employee identifies research material (video, article, documentation)
   - **Responsibility:** Individual employees
   - **Tool:** Research sources, content discovery
   - **Placement:** Employee research folder
2. Employee conducts research and documents findings
   - **Responsibility:** Individual employees
   - **Tool:** Research tools, documentation tools
   - **Placement:** Employee research folder
3. Research is collected and tagged with headers/templates
   - **Responsibility:** AI Department (automated) or employee
   - **Tool:** Content tagging system, AI tools
   - **Placement:** Centralized knowledge base
4. Extract actions and objects from research content
   - **Responsibility:** AI Department (automated)
   - **Tool:** AI processing, template extraction
   - **Placement:** Knowledge base processing
5. Aggregate research into centralized knowledge base
   - **Responsibility:** AI Department (automated)
   - **Tool:** Knowledge base system, aggregation scripts
   - **Placement:** Centralized knowledge base repository
6. Push aggregated knowledge to Online Academy
   - **Responsibility:** AI Department
   - **Tool:** Online Academy platform, integration tools
   - **Placement:** Online Academy content repository

**Responsible Parties:**
- **Accountable:** Artemchuk Nikolay (ID: 37226) - AI Department
- **Responsible:** All employees (research), AI Department (aggregation)
- **Consulted:** Department leads
- **Informed:** All departments

**Tools/Platforms Used:** Research tools, content tagging system, AI processing tools, knowledge base system, Online Academy platform

**Success Criteria:**
- Research materials are consistently collected
- Content is properly tagged and structured
- Knowledge base contains aggregated research
- Online Academy receives updated content

**Automation Opportunities:**
- Automated content tagging
- Automated template extraction
- Automated aggregation scripts
- Automated push to Online Academy

### Script-Based Data Processing Workflow

**Purpose:** Process large data files (50k+ lines) using scripts to preprocess and reduce token usage before AI processing.

**SOP Reference:** Large File Processing Scripts (to be created)

**Steps:**
1. Identify large file requiring processing
   - **Responsibility:** Data processing team
   - **Tool:** File system, file analysis tools
   - **Placement:** Source data location
2. Break file into units (if not already unitized)
   - **Responsibility:** AI Department (scripted)
   - **Tool:** File splitting scripts
   - **Placement:** Processing workspace
3. Run preprocessing scripts (extract, encode, clean, filter)
   - **Responsibility:** AI Department (automated)
   - **Tool:** Processing scripts, n8n or GitHub Actions
   - **Placement:** Processing workspace
4. Generate processing report
   - **Responsibility:** AI Department (automated)
   - **Tool:** Reporting scripts
   - **Placement:** Reports folder
5. Process cleaned data with AI tools
   - **Responsibility:** AI Department
   - **Tool:** AI tools (Claude, ChatGPT)
   - **Placement:** AI processing workspace
6. Archive original file to backup location
   - **Responsibility:** AI Department (automated)
   - **Tool:** Archive scripts, backup system
   - **Placement:** Backup storage

**Responsible Parties:**
- **Accountable:** Artemchuk Nikolay (ID: 37226) - AI Department
- **Responsible:** AI Department
- **Consulted:** Data owners
- **Informed:** Relevant departments

**Tools/Platforms Used:** Processing scripts, n8n, GitHub Actions, AI tools, backup system

**Success Criteria:**
- Large files are successfully preprocessed
- Token usage is reduced significantly
- Data is cleaned and ready for AI processing
- Original files are safely archived

**Automation Opportunities:**
- Automated file detection and processing
- Automated script execution via n8n/GitHub Actions
- Automated reporting
- Automated archiving

### Daily Report Automation Workflow

**Purpose:** Automatically generate daily reports by running department-specific Daily Prompts at end of each day, scanning department folders, and compiling reports.

**SOP Reference:** Daily Report Automation (to be created)

**Steps:**
1. End of day trigger (scheduled)
   - **Responsibility:** Automation system
   - **Tool:** Scheduler, Cursor Rules, Composer
   - **Placement:** Automation system
2. Run department-specific Daily Prompt
   - **Responsibility:** Automation system
   - **Tool:** Cursor, Composer, Daily Prompt templates
   - **Placement:** Department folders
3. Scan department folders for updates and activities
   - **Responsibility:** Automation system
   - **Tool:** File system scanning, activity tracking
   - **Placement:** Department folders
4. Process information and generate Daily Report
   - **Responsibility:** Automation system (AI-powered)
   - **Tool:** AI tools, report generation templates
   - **Placement:** Reports folder
5. Distribute Daily Report to relevant stakeholders
   - **Responsibility:** Automation system
   - **Tool:** Communication tools (Discord, Email)
   - **Placement:** Communication channels

**Responsible Parties:**
- **Accountable:** Artemchuk Nikolay (ID: 37226) - AI Department
- **Responsible:** Automation system
- **Consulted:** Department leads
- **Informed:** All departments

**Tools/Platforms Used:** Cursor, Composer, Cursor Rules, Daily Prompt templates, AI tools, communication tools

**Success Criteria:**
- Daily reports are generated automatically
- Reports contain relevant department activities
- Reports are distributed on time
- Reports follow consistent format

**Automation Opportunities:**
- Fully automated workflow
- AI-powered content generation
- Automated distribution

---

## 6. RULES & BEST PRACTICES

### Individual Employee Folders Over Department-Level Processing

**Rule/Practice:** Use individual employee folders instead of department-level processing for data management and knowledge organization.

**Rationale:** 
- Enables better data identification (when multiple people use shared admin accounts, folder location identifies owner)
- Allows processing of employee-specific data without overwhelming system with department-wide data
- Enables targeted updates (can update Employee Profile, past assignments, and library in one operation)
- Reduces token usage by processing smaller, focused datasets
- Improves data traceability and accountability

**Application:** 
- Create individual folders for each employee
- Store employee-specific templates, research, and data in their folder
- Process employee data at individual level, not department level
- Use folder location for data identification and logging

**Examples:**
- Employee folder contains 10 task templates they work with vs department folder with 1000 templates
- System can search across employee folders (library, past assignments, Employee Profile) and update all in one operation
- Folder location identifies who made updates when using shared admin account

**Affected Departments:** All departments

**Template Integration:** Employee Folder Structure Template, Employee Data Processing SOP

### Script-First Approach for Large Data Files

**Rule/Practice:** Use scripts to preprocess large data files (50k+ lines) before AI processing to reduce token usage and improve efficiency.

**Rationale:**
- AI systems cannot process very large files due to token limits
- Scripts can handle large files efficiently without token constraints
- Preprocessing reduces token usage for AI processing
- Scripts can be automated via n8n or GitHub Actions
- Scripts provide reusable, consistent processing

**Application:**
- Identify files exceeding AI processing capabilities
- Develop scripts for extraction, encoding, cleaning, and filtering
- Run scripts before AI processing
- Use scripts for repetitive processing tasks
- Automate script execution where possible

**Examples:**
- employees.json (97,000 lines) → break into units → process with scripts → clean data → then process with AI
- Scripts extract content, encode to UTF-8, clean empty fields, generate reports
- Scripts can be triggered by n8n actions or GitHub Actions

**Affected Departments:** AI, HR, All departments processing large datasets

**Template Integration:** Large File Processing Scripts, Data Preprocessing SOP

### Research Collection Guidelines

**Rule/Practice:** Collect research materials into centralized knowledge base. Employees conduct their own research, which aggregates into central database. Eventually push to Online Academy.

**Rationale:**
- Enables knowledge sharing across organization
- Reduces duplication of research efforts
- Creates centralized knowledge repository
- Supports Online Academy content development
- Empowers employees to contribute to knowledge base

**Application:**
- Employees identify and conduct research on relevant topics
- Research is documented and tagged
- Research aggregates into centralized knowledge base
- Content is eventually pushed to Online Academy
- Research plan template guides what to collect

**Examples:**
- Employee finds design system documentation → conducts research → documents findings → aggregates to knowledge base → pushes to Online Academy
- Research plan template populated by AI recommendations for missing research topics

**Affected Departments:** All departments

**Template Integration:** Research Collection Guidelines, Research Plan Template, Knowledge Base Structure

### Token Optimization Strategies

**Rule/Practice:** Optimize token usage through script-based preprocessing, unit-based file breakdown, and individual-level processing.

**Rationale:**
- Token limits constrain AI processing capabilities
- Large files exceed token limits
- Script preprocessing reduces token usage
- Unit-based processing enables manageable chunks
- Individual-level processing uses fewer tokens than department-level

**Application:**
- Use scripts for preprocessing large files
- Break large files into units before AI processing
- Process data at individual employee level
- Use mini-frameworks and prompts for single employee processing
- Avoid processing entire departments or large datasets at once

**Examples:**
- 50,000 line file → break into units → script preprocessing → individual unit AI processing
- Process one employee at a time with mini-framework instead of all employees
- Use scripts to clean and filter before AI processing

**Affected Departments:** AI, All departments using AI tools

**Template Integration:** Token Optimization Guidelines, Script Development Standards, Processing Workflows

---

## 7. PROBLEMS & SOLUTIONS

### Problem: Token Limits Blocking AI Processing

**Description:** AI systems cannot process very large files (50k+ lines, 97k+ lines) due to token limitations. Even framework files exceed processing capabilities. System cannot handle large datasets for AI processing.

**Impact:** 
- Cannot process CRM employee export file (employees.json) directly with AI
- Cannot process large framework files
- Limits ability to use AI for data processing and analysis
- Blocks automation workflows requiring large file processing

**Root Cause:** 
- Token limits in AI systems (Claude, ChatGPT, etc.)
- Large file sizes exceed context windows
- Attempting to process entire datasets at once

**Proposed Solution:** 
- Use scripts to preprocess large files before AI processing
- Break large files into units (manageable chunks)
- Process units individually with AI
- Use script-based extraction, encoding, cleaning, and filtering
- Automate script execution via n8n or GitHub Actions

**AI Solution Potential:** 
- Scripts can be AI-generated initially, then converted to permanent scripts
- AI can help design preprocessing workflows
- AI can process cleaned, smaller datasets after script preprocessing

**Decision Made:** 
- Implement script-first approach for large files
- Develop reusable scripts for common preprocessing tasks
- Break files into units before AI processing
- Use automation tools (n8n, GitHub Actions) for script execution

**Implementation Owner:** 
- **Artemchuk Nikolay** (ID: 37226) - AI Department

**Status:** Approved, In Progress

**Documentation Needed:** 
- Large File Processing Scripts documentation
- Script development standards
- Token optimization guidelines
- Should go in RAC knowledge base

### Problem: Data Identification in Shared Admin Accounts

**Description:** When multiple employees (Вася, Петя, Маша, Даша) use shared admin accounts, system cannot identify which person made specific updates or changes. Logging shows admin account but not individual user.

**Impact:**
- Cannot track individual contributions
- Cannot identify who made specific changes
- Reduces accountability and traceability
- Makes it difficult to attribute work to specific employees

**Root Cause:**
- Shared admin account usage
- System logs show account, not individual user
- No individual identification mechanism

**Proposed Solution:**
- Move to individual employee folders
- Use folder location to identify data owner
- Process data at individual employee level
- Folder structure enables identification even with shared accounts
- Context within folder can also help identify user

**AI Solution Potential:**
- AI can help identify user from context clues
- Folder-based processing enables individual-level AI assistance
- Can track changes by folder location

**Decision Made:**
- Implement individual employee folder structure
- Use folder location for data identification
- Process at individual level, not department level
- Enable individual-level AI processing and knowledge management

**Implementation Owner:**
- **Artemchuk Nikolay** (ID: 37226) - AI Department

**Status:** Approved, Planning

**Documentation Needed:**
- Employee Folder Structure documentation
- Individual Processing Guidelines
- Should go in RAC knowledge base

### Problem: Large File Processing Exceeds System Capabilities

**Description:** Files with 50,000+ lines cannot be processed by AI systems. employees.json has 97,000 lines (~500 lines per employee). System cannot handle processing entire file or even framework files.

**Impact:**
- Cannot process employee export data
- Cannot use AI for large dataset analysis
- Blocks automation workflows
- Limits data processing capabilities

**Root Cause:**
- File sizes exceed AI token limits
- Attempting to process entire files at once
- No preprocessing or chunking strategy

**Proposed Solution:**
- Break large files into units (one unit = one employee section)
- Use scripts to process units
- Scripts handle extraction, encoding, cleaning, filtering
- Process units individually with AI after preprocessing
- Develop reusable script library for common tasks

**AI Solution Potential:**
- AI can help design unit breakdown strategy
- AI can process cleaned, smaller units
- AI can help generate initial scripts, then convert to permanent scripts

**Decision Made:**
- Implement unit-based file breakdown
- Develop script library for preprocessing
- Use scripts for large file handling
- Process units individually with AI

**Implementation Owner:**
- **Artemchuk Nikolay** (ID: 37226) - AI Department

**Status:** Approved, In Progress (units folder already created)

**Documentation Needed:**
- Unit-Based Processing Guidelines
- Script Library Documentation
- Should go in RAC knowledge base

---

## 8. TOOLS & RESOURCES

### Cursor
- **Type:** AI Development Tool
- **Category:** AI Tools, Dev Tools
- **Purpose:** AI-powered code editor with agents, rules, and Composer features
- **Use Case:** 
  - Developing employee folder structure
  - Creating scripts and automation
  - Processing transcriptions and daily reports
  - Agent development and configuration
- **Access/Links:** Cursor IDE application
- **Recommended For:** AI Department, Dev Department
- **Current Users:** Artemchuk Nikolay, development team
- **Notes:** Cursor 2.0 includes Agents feature. Can be used with Rules and Composer for automation. Can run Daily Prompt automation at end of day.
- **Integration with Stack:** Integrates with GitHub MCP, supports script development, enables automation workflows

### VS Code
- **Type:** Development Tool
- **Category:** Dev Tools
- **Purpose:** Code editor for development work
- **Use Case:** 
  - General code editing
  - Script development
  - File management
- **Access/Links:** VS Code application
- **Recommended For:** All development work
- **Current Users:** Development team
- **Notes:** Mentioned in conversation about Cursor interface differences
- **Integration with Stack:** Standard development tool, works alongside Cursor

### GitHub / GitHub Actions
- **Type:** Development Tool, Automation Platform
- **Category:** Dev Tools
- **Purpose:** Version control, repository management, CI/CD automation
- **Use Case:** 
  - Storing scripts and automation code
  - Running GitHub Actions for automated workflows
  - Making scripts accessible via GitHub
  - Connecting with GitHub MCP for Cursor integration
- **Access/Links:** GitHub platform, GitHub Actions
- **Recommended For:** AI Department, Dev Department, Infrastructure
- **Current Users:** Development team
- **Notes:** Needed for script automation, repository management, GitHub MCP integration
- **Integration with Stack:** Integrates with Cursor via GitHub MCP, enables script automation, supports RAC repository

### n8n
- **Type:** Automation Tool
- **Category:** Digital Tools, Automation Platform
- **Purpose:** Workflow automation and task orchestration
- **Use Case:** 
  - Triggering script execution
  - Automating data processing workflows
  - Orchestrating multi-step processes
- **Access/Links:** n8n platform
- **Recommended For:** AI Department, Automation workflows
- **Current Users:** Automation team
- **Notes:** Can trigger scripts for large file processing, can automate preprocessing workflows
- **Integration with Stack:** Can trigger scripts, integrate with other tools, support automation workflows

### Open Router
- **Type:** AI Service Aggregator
- **Category:** AI Tools
- **Purpose:** Aggregation service providing access to multiple AI models and tokens
- **Use Case:** 
  - Accessing various AI models through single service
  - Managing AI token usage
  - Cost optimization for AI services
- **Access/Links:** Open Router platform
- **Recommended For:** AI Department
- **Current Users:** AI team
- **Notes:** Tokens are expensive. Provides access to multiple AI services. Can be integrated into automation workflows.
- **Integration with Stack:** Can provide AI capabilities to scripts and automation, supports multiple AI model access

### Google Drive
- **Type:** Collaboration Platform
- **Category:** Digital Tools
- **Purpose:** File storage and collaboration
- **Use Case:** 
  - Storing CRM export files (employees.json)
  - Managing employee data folders (people/employees)
  - Storing research materials
  - Collaboration on documents
- **Access/Links:** Google Drive platform
- **Recommended For:** All departments
- **Current Users:** All employees
- **Notes:** Contains CRM export data, employee folders, research materials
- **Integration with Stack:** Source for data processing, storage for processed files, integration with other Google services

### Google Calendar
- **Type:** Collaboration Platform
- **Category:** Digital Tools
- **Purpose:** Calendar and scheduling
- **Use Case:** 
  - Scheduling and time management
  - Integration with employee folder agents
  - Calendar-based automation triggers
- **Access/Links:** Google Calendar platform
- **Recommended For:** All departments
- **Current Users:** All employees
- **Notes:** Can be connected as agent in employee folder structure
- **Integration with Stack:** Integrates with employee folder agents, supports scheduling automation

### Online Academy Platform
- **Type:** Educational Platform
- **Category:** Digital Tools
- **Purpose:** Online learning and knowledge sharing platform
- **Use Case:** 
  - Hosting aggregated research and knowledge base content
  - Providing structured learning materials
  - Content tagging and organization (JSON content, headers)
  - Template identification and extraction
- **Access/Links:** Online Academy platform
- **Recommended For:** All departments (content consumers), AI Department (content management)
- **Current Users:** All employees (learners), AI team (content managers)
- **Notes:** Can receive aggregated research content, supports JSON content structure, enables template tagging
- **Integration with Stack:** Receives content from knowledge base, integrates with research collection workflow, supports content tagging

### CRM System
- **Type:** Business Management Tool
- **Category:** Digital Tools
- **Purpose:** Customer and employee relationship management, task templates
- **Use Case:** 
  - Employee data management
  - Task template storage
  - Employee export functionality (employees.json)
  - Data source for Talent service import
- **Access/Links:** CRM system platform
- **Recommended For:** HR Department, AI Department
- **Current Users:** HR team, management
- **Notes:** Contains employee export data, has data structure issues (old CRM, third-party created), needs data cleaning and restructuring
- **Integration with Stack:** Source for employee data, exports to Google Drive, data processed for Talent service

### Composer (Cursor Feature)
- **Type:** AI Development Tool Feature
- **Category:** AI Tools
- **Purpose:** Cursor feature for AI-powered code generation and automation
- **Use Case:** 
  - Generating scripts and automation code
  - Creating Daily Prompt automation
  - Developing Cursor Rules and Skills
  - AI-assisted development
- **Access/Links:** Cursor Composer feature
- **Recommended For:** AI Department
- **Current Users:** AI team
- **Notes:** Can be used with Cursor Rules to create Daily Prompt automation, can generate scripts that are then converted to permanent scripts
- **Integration with Stack:** Part of Cursor IDE, works with Rules, supports script generation

### Claude (Anthropic)
- **Type:** AI Tool
- **Category:** AI Tools - Large Language Models
- **Purpose:** Advanced AI assistant with long context, document analysis, code generation
- **Use Case:** 
  - Processing transcriptions and daily reports
  - Analyzing large documents
  - Generating scripts and automation code
  - Creating mini-frameworks and prompts
- **Access/Links:** https://claude.ai/login?returnTo=%2F%3F
- **Recommended For:** AI Department, All departments
- **Current Users:** AI team, various departments
- **Notes:** Has token limits, but can process cleaned/preprocessed data. Can help generate scripts and frameworks.
- **Integration with Stack:** Primary AI tool for processing, can be accessed via Open Router, supports automation workflows

### ChatGPT (OpenAI)
- **Type:** AI Tool
- **Category:** AI Tools - Large Language Models
- **Purpose:** Conversational AI, text generation, multimodal capabilities
- **Use Case:** 
  - General AI assistance
  - Content generation
  - Research assistance
  - Code generation
- **Access/Links:** https://chatgpt.com/?model=gpt-4o
- **Recommended For:** All departments
- **Current Users:** All employees
- **Notes:** GPT-4o model with multimodal capabilities. Can be used for various AI tasks.
- **Integration with Stack:** Can be accessed via Open Router, supports various automation workflows

---

## 9. TECHNICAL ARCHITECTURE

### Employee Folder Structure Architecture

**Architecture Layer:**
- Data Layer (Employee data, templates, research)
- Integration & Preprocessing (Scripts, agents)
- LLM/AI Services (AI processing, automation)
- Application Layer (Folder structure, file organization)
- Monitoring & Governance (Folder-based logging, access control)

**Technology Stack:** 
- File system (folder structure)
- Scripts (Python, PowerShell, or other)
- AI tools (Claude, ChatGPT)
- Agent frameworks (email, calendar, Online Academy)
- Automation tools (n8n, GitHub Actions)

**Architecture Pattern:** 
- Hierarchical folder structure
- Modular subfolder organization (scripts/, agents/, library/, template/)
- Individual-level data processing
- Agent-based integration

**Key Components:**
- **Base Employee Folder:** Root folder for each employee
- **scripts/ subfolder:** Contains processing and automation scripts
- **agents/ subfolder:** Contains configured agents (email, Google Calendar, Online Academy)
- **library/ subfolder:** Contains templates, mini-entities, department-specific resources
- **template/ subfolder:** Contains employee-specific templates and configurations
- **AI Token Storage:** Secure storage for AI access credentials
- **Research Materials:** Employee research and knowledge contributions

**Integration Points:**
- Google Drive (employee data source)
- CRM system (employee data export)
- Online Academy (knowledge base push)
- Email systems (agent integration)
- Google Calendar (agent integration)
- GitHub (script storage and automation)

**Legacy Tool Integration:**
- Google Drive folders
- CRM system exports
- Email systems
- Calendar systems

**Documentation Location:** 
- RAC GitHub repository
- Employee Folder Structure documentation
- Department guides

**AI Enhancement:**
- AI-powered folder population
- AI-assisted template generation
- Automated agent configuration
- AI processing of employee data

### Script-Based Preprocessing Layer Architecture

**Architecture Layer:**
- Data Layer (Large files, raw data)
- Integration & Preprocessing (Scripts, ETL pipelines)
- LLM/AI Services (Post-processed AI analysis)
- Application Layer (Processed data, reports)
- Monitoring & Governance (Processing logs, error handling)

**Technology Stack:**
- Scripting languages (Python, PowerShell, JavaScript)
- File processing libraries
- Data encoding/decoding tools
- Data cleaning and filtering tools
- Automation platforms (n8n, GitHub Actions)

**Architecture Pattern:**
- Preprocessing pipeline
- Unit-based processing
- Script-first approach
- Automated execution

**Key Components:**
- **File Detection:** Identify large files requiring preprocessing
- **Unit Breakdown:** Split large files into manageable units
- **Extraction Scripts:** Extract content from files
- **Encoding Scripts:** Convert to UTF-8 or required encoding
- **Cleaning Scripts:** Remove empty fields, validate data
- **Filtering Scripts:** Filter data based on criteria
- **Reporting Scripts:** Generate processing reports
- **Automation Triggers:** n8n actions, GitHub Actions

**Integration Points:**
- Source data systems (CRM, Google Drive)
- AI processing systems (Claude, ChatGPT)
- Automation platforms (n8n, GitHub Actions)
- Reporting systems
- Backup storage

**Legacy Tool Integration:**
- CRM export files
- Google Drive files
- File system storage

**Documentation Location:**
- RAC GitHub repository
- Script Library documentation
- Processing workflow documentation

**AI Enhancement:**
- AI-assisted script generation
- AI-powered data validation
- Automated error detection and handling
- AI analysis of processed data

### GitHub Integration Architecture

**Architecture Layer:**
- Data Layer (Code repositories, scripts)
- Integration & Preprocessing (GitHub Actions, CI/CD)
- LLM/AI Services (GitHub MCP, AI integration)
- Application Layer (Repositories, automation)
- Monitoring & Governance (GitHub logs, access control)

**Technology Stack:**
- GitHub platform
- GitHub Actions
- GitHub MCP (Model Context Protocol)
- Cursor integration
- Repository management

**Architecture Pattern:**
- Repository-based organization
- Automated workflows
- MCP integration
- Script accessibility

**Key Components:**
- **Repositories:** Store scripts, automation code, documentation
- **GitHub Actions:** Automated workflow execution
- **GitHub MCP:** Integration with Cursor and AI tools
- **Cursor Rules:** Automation rules stored in GitHub
- **Script Libraries:** Reusable scripts in repositories
- **Documentation:** RAC and process documentation

**Integration Points:**
- Cursor IDE (via GitHub MCP)
- AI tools (via GitHub MCP)
- Automation systems
- Script execution environments
- Documentation systems

**Legacy Tool Integration:**
- Existing GitHub repositories
- Cursor IDE
- Development tools

**Documentation Location:**
- GitHub repositories
- RAC GitHub repository
- GitHub Actions documentation

**AI Enhancement:**
- AI-powered code generation
- Automated script creation
- AI-assisted repository management
- GitHub MCP AI integration

### Knowledge Base Aggregation System Architecture

**Architecture Layer:**
- Data Layer (Research materials, employee contributions)
- Integration & Preprocessing (Content tagging, template extraction)
- LLM/AI Services (AI-powered analysis and recommendations)
- Application Layer (Knowledge base, Online Academy)
- Monitoring & Governance (Content quality, access control)

**Technology Stack:**
- Knowledge base system
- Content tagging tools
- AI processing tools
- Online Academy platform
- JSON content structure
- Template extraction tools

**Architecture Pattern:**
- Centralized aggregation
- Distributed contribution (employees)
- AI-powered processing
- Platform integration

**Key Components:**
- **Research Collection:** Employee research materials
- **Content Tagging:** Headers, templates, metadata
- **Template Extraction:** Identify actions, objects, templates in content
- **Aggregation System:** Centralize research into knowledge base
- **Online Academy Integration:** Push content to platform
- **Research Plan Template:** Guide research collection
- **AI Recommendations:** Suggest missing research topics

**Integration Points:**
- Employee folders (research source)
- Knowledge base system (aggregation target)
- Online Academy platform (content destination)
- AI tools (processing and recommendations)
- Content tagging systems

**Legacy Tool Integration:**
- Existing research materials
- Online Academy platform
- Content management systems

**Documentation Location:**
- RAC GitHub repository
- Knowledge Base documentation
- Research Collection Guidelines

**AI Enhancement:**
- AI-powered content tagging
- Automated template extraction
- AI research recommendations
- Automated content analysis
- AI-assisted knowledge organization

---

## 10. DECISIONS LOG

### Decision: Individual Employee Folders Over Department-Level Processing

**Date:** November 11, 2025

**Context:** 
Need to process employee data and manage knowledge at individual level. Current department-level approach causes issues with data identification when using shared admin accounts and creates token limit problems with large datasets.

**Options Considered:**
1. Continue department-level processing
2. Move to individual employee folders
3. Hybrid approach (department folders with employee subfolders)

**Decision Made:** 
Move to individual employee folders with standardized structure (scripts/, agents/, library/, template/).

**Rationale:**
- Enables better data identification (folder location identifies owner even with shared accounts)
- Allows processing of smaller, focused datasets (reduces token usage)
- Enables targeted updates across multiple employee files in one operation
- Improves traceability and accountability
- Supports individual-level knowledge management and research

**Impact:**
- Affects all departments (new folder structure)
- Changes data processing workflows
- Impacts automation and AI processing approaches
- Requires migration from department-level to individual-level

**Alignment with AI-First Vision:**
- Enables efficient AI processing at individual level
- Supports AI-powered individual assistance
- Reduces token usage through focused processing
- Enables AI automation at employee level

**Follow-up Required:**
- Design employee folder structure template
- Create migration plan
- Develop folder creation automation
- Update processing workflows

**Documentation:** 
- RAC: Employee Folder Structure documentation
- Department guides: Individual processing guidelines
- SOP: Employee Folder Creation Workflow

### Decision: Script-Based Preprocessing for Large Files

**Date:** November 11, 2025

**Context:** 
Large files (50k+ lines, 97k+ lines) exceed AI token limits. Cannot process employee export files or large framework files directly with AI. Need solution to handle large datasets.

**Options Considered:**
1. Increase token limits (not feasible, cost prohibitive)
2. Process files in smaller chunks manually
3. Use scripts to preprocess before AI processing
4. Use different AI models with larger context windows

**Decision Made:** 
Implement script-first approach: use scripts to preprocess large files (extract, encode, clean, filter) before AI processing. Break files into units. Automate script execution via n8n or GitHub Actions.

**Rationale:**
- Scripts can handle large files without token limits
- Preprocessing reduces token usage for AI
- Scripts provide reusable, consistent processing
- Automation enables efficient workflow
- Unit-based approach enables manageable AI processing

**Impact:**
- Affects AI Department (script development)
- Changes data processing workflows
- Requires script library development
- Impacts automation infrastructure

**Alignment with AI-First Vision:**
- Optimizes AI token usage
- Enables AI processing of previously inaccessible data
- Supports automation and efficiency
- Complements AI capabilities with script preprocessing

**Follow-up Required:**
- Develop script library for common tasks
- Create automation workflows
- Document script standards
- Train team on script usage

**Documentation:**
- RAC: Large File Processing Scripts documentation
- Script Library: Reusable scripts repository
- SOP: Script-Based Data Processing Workflow

### Decision: Department-Specific Daily Prompts

**Date:** November 11, 2025

**Context:** 
Current Daily Prompt is generic. Could be improved by making it department-specific. Need automated daily report generation.

**Options Considered:**
1. Keep single generic Daily Prompt
2. Create department-specific versions
3. Create department-specific versions with automation

**Decision Made:** 
Create separate Daily Prompt versions for each department. Store in department folders. Develop Cursor Rules or Composer Skills to automatically run prompts at end of day, scan department folders, and generate Daily Reports.

**Rationale:**
- Department-specific prompts provide more relevant, focused processing
- Automation reduces manual work
- End-of-day automation ensures timely reports
- Department folders enable organized prompt storage
- Cursor Rules/Composer enable automation integration

**Impact:**
- Affects all departments (department-specific prompts)
- Changes daily report generation process
- Requires automation setup
- Impacts Cursor/Composer configuration

**Alignment with AI-First Vision:**
- Leverages AI for automated report generation
- Provides department-specific AI assistance
- Reduces manual processing time
- Enables consistent, timely reporting

**Follow-up Required:**
- Create department-specific Daily Prompt templates
- Develop Cursor Rules/Composer Skills
- Set up automation schedules
- Test automation workflows

**Documentation:**
- RAC: Daily Prompt templates (department-specific)
- Cursor Rules: Automation rules
- SOP: Daily Report Automation Workflow

### Decision: Automated Daily Report Generation

**Date:** November 11, 2025

**Context:** 
Daily reports need to be generated consistently and on time. Manual processing is time-consuming. Need automation to generate reports at end of day.

**Options Considered:**
1. Continue manual daily report generation
2. Semi-automated (AI-assisted but manual trigger)
3. Fully automated (scheduled, AI-powered)

**Decision Made:** 
Implement fully automated daily report generation using Cursor Rules or Composer Skills. Run department-specific Daily Prompts at end of day, scan department folders, generate reports automatically.

**Rationale:**
- Ensures timely report generation (end of day)
- Reduces manual work
- Provides consistent format
- Enables AI-powered content generation
- Frees up time for other tasks

**Impact:**
- Affects all departments (automated reports)
- Changes daily workflow
- Requires automation infrastructure
- Impacts report distribution

**Alignment with AI-First Vision:**
- Fully automated AI-powered process
- Reduces manual work through automation
- Ensures consistent, timely reporting
- Leverages AI for content generation

**Follow-up Required:**
- Develop automation workflows
- Set up scheduling
- Configure report distribution
- Test automation system

**Documentation:**
- RAC: Daily Report Automation documentation
- Cursor Rules: Automation configuration
- SOP: Daily Report Automation Workflow

### Decision: Centralized Research and Knowledge Base Collection

**Date:** November 11, 2025

**Context:** 
Research materials are scattered. Need centralized knowledge base. Employees should contribute research that aggregates into central database. Eventually push to Online Academy.

**Options Considered:**
1. Keep research scattered (no centralization)
2. Centralized collection by AI team only
3. Distributed contribution with centralized aggregation

**Decision Made:** 
Implement distributed research contribution (employees conduct their own research) with centralized aggregation into knowledge base. Eventually push aggregated content to Online Academy.

**Rationale:**
- Empowers employees to contribute to knowledge base
- Reduces duplication of research efforts
- Creates centralized knowledge repository
- Supports Online Academy content development
- Enables knowledge sharing across organization

**Impact:**
- Affects all departments (research contribution)
- Changes knowledge management approach
- Requires knowledge base infrastructure
- Impacts Online Academy content

**Alignment with AI-First Vision:**
- AI-powered content tagging and processing
- Automated aggregation and organization
- AI research recommendations
- Supports knowledge-driven operations

**Follow-up Required:**
- Create research collection guidelines
- Develop knowledge base structure
- Create research plan template
- Set up aggregation process

**Documentation:**
- RAC: Research Collection Guidelines
- Knowledge Base: Structure documentation
- Research Plan: Template documentation
- SOP: Research Collection and Knowledge Base Workflow

---

## 11. DOCUMENTATION & KNOWLEDGE GAPS

### Employee Folder Structure Documentation

**Type:** Technical Doc, Process Doc, Architecture

**Purpose:** 
Document the standardized employee folder structure, subfolder organization, and usage guidelines. Enable consistent folder creation and usage across all employees.

**Target Audience:** 
AI Department, HR Department, All departments

**Current Status:** Missing

**Location(s):** 
- RAC GitHub repository
- Department guides
- Employee onboarding materials

**Owner:** 
**Artemchuk Nikolay** (ID: 37226) - AI Department

**Priority:** Critical

**Template Format:** 
Architecture documentation with folder structure diagram, subfolder descriptions, usage guidelines, examples

**Language Needs:** English (primary), Russian/Ukrainian (as needed)

### Script Templates and Library Documentation

**Type:** Technical Doc, Process Doc

**Purpose:** 
Document reusable scripts for large file processing, data extraction, cleaning, filtering. Provide script templates and usage guidelines.

**Target Audience:** 
AI Department, Development teams

**Current Status:** Missing

**Location(s):** 
- RAC GitHub repository
- Script library repository
- Technical documentation

**Owner:** 
**Artemchuk Nikolay** (ID: 37226) - AI Department

**Priority:** High

**Template Format:** 
Script documentation with code examples, usage instructions, parameters, automation integration

**Language Needs:** English (primary), code comments in English

### Research Collection Guidelines

**Type:** Process Doc, Guide, SOP Template

**Purpose:** 
Define what research materials to collect, how to document research, where to store research, and how research aggregates into knowledge base.

**Target Audience:** 
All departments, All employees

**Current Status:** Missing

**Location(s):** 
- RAC GitHub repository
- Department guides
- Employee handbook

**Owner:** 
**Artemchuk Nikolay** (ID: 37226) - AI Department

**Priority:** High

**Template Format:** 
SOP with steps, guidelines, examples, templates

**Language Needs:** English (primary), Russian/Ukrainian (as needed)

### Daily Prompt Department Versions

**Type:** Process Doc, Template, Guide

**Purpose:** 
Create department-specific Daily Prompt templates tailored to each department's needs and context.

**Target Audience:** 
All departments, AI Department (for automation)

**Current Status:** Missing (need department-specific versions)

**Location(s):** 
- RAC GitHub repository
- Department folders
- Prompt library

**Owner:** 
**Artemchuk Nikolay** (ID: 37226) - AI Department

**Priority:** High

**Template Format:** 
Prompt templates with department-specific sections, automation integration instructions

**Language Needs:** English (primary), Russian/Ukrainian (as needed)

### Large File Processing Guidelines

**Type:** Technical Doc, Process Doc, Guide

**Purpose:** 
Document strategies for processing large files, script-based preprocessing, unit breakdown, token optimization.

**Target Audience:** 
AI Department, Development teams

**Current Status:** Missing

**Location(s):** 
- RAC GitHub repository
- Technical documentation
- Script library

**Owner:** 
**Artemchuk Nikolay** (ID: 37226) - AI Department

**Priority:** High

**Template Format:** 
Technical guide with strategies, examples, best practices, script references

**Language Needs:** English (primary)

### Token Optimization Guidelines

**Type:** Technical Doc, Best Practices, Guide

**Purpose:** 
Document strategies for optimizing AI token usage, script preprocessing, unit-based processing, individual-level processing.

**Target Audience:** 
AI Department, All departments using AI tools

**Current Status:** Missing

**Location(s):** 
- RAC GitHub repository
- Technical documentation
- AI Department guide

**Owner:** 
**Artemchuk Nikolay** (ID: 37226) - AI Department

**Priority:** Medium

**Template Format:** 
Best practices guide with strategies, examples, metrics, recommendations

**Language Needs:** English (primary)

### GitHub Automation Setup Guide

**Type:** Technical Doc, Setup Guide

**Purpose:** 
Document how to set up GitHub repositories, GitHub Actions, GitHub MCP integration with Cursor, automation workflows.

**Target Audience:** 
AI Department, Development teams

**Current Status:** Missing

**Location(s):** 
- RAC GitHub repository
- Technical documentation
- Setup guides

**Owner:** 
**Artemchuk Nikolay** (ID: 37226) - AI Department

**Priority:** Medium

**Template Format:** 
Setup guide with step-by-step instructions, configuration examples, troubleshooting

**Language Needs:** English (primary)

### Knowledge Base Structure Documentation

**Type:** Technical Doc, Architecture, Guide

**Purpose:** 
Document the knowledge base structure, content organization, tagging system, aggregation process, Online Academy integration.

**Target Audience:** 
AI Department, Content managers, All employees (contributors)

**Current Status:** Missing

**Location(s):** 
- RAC GitHub repository
- Knowledge base documentation
- Online Academy documentation

**Owner:** 
**Artemchuk Nikolay** (ID: 37226) - AI Department

**Priority:** Medium

**Template Format:** 
Architecture documentation with structure diagram, tagging guidelines, aggregation process, integration instructions

**Language Needs:** English (primary)

### Research Plan Template

**Type:** Template, Checklist

**Purpose:** 
Template for planning research activities, identifying research gaps, tracking research progress. Can be populated by AI recommendations.

**Target Audience:** 
All employees, AI Department

**Current Status:** Missing

**Location(s):** 
- RAC GitHub repository
- Template library
- Research guidelines

**Owner:** 
**Artemchuk Nikolay** (ID: 37226) - AI Department

**Priority:** Medium

**Template Format:** 
Template with fields for research topics, sources, findings, recommendations, status

**Language Needs:** English (primary), Russian/Ukrainian (as needed)

### Mini-Framework Template for Individual Employees

**Type:** Template, Guide

**Purpose:** 
Template for creating mini-frameworks and prompts designed for processing individual employee data. Profession-specific versions.

**Target Audience:** 
AI Department, Prompt engineers

**Current Status:** Missing

**Location(s):** 
- RAC GitHub repository
- Prompt library
- Employee folder templates

**Owner:** 
**Artemchuk Nikolay** (ID: 37226) - AI Department

**Priority:** High

**Template Format:** 
Template with framework structure, profession-specific sections, usage guidelines

**Language Needs:** English (primary)

---

## 12. COMMUNICATION & ANNOUNCEMENTS

### Daily Report Automation Announcement

**What:** 
Announce new automated daily report generation system. Daily reports will be generated automatically at end of day using department-specific Daily Prompts.

**To Whom:** 
All staff, All departments

**Channel:** 
Discord channels, Email, All-hands meeting

**Message Type:** 
Initial announcement, Training

**Timing:** 
Before automation goes live, during setup phase

**Owner:** 
**Artemchuk Nikolay** (ID: 37226) - AI Department

**Language:** 
English (primary), Russian/Ukrainian (as needed)

**Follow-up Plan:**
- Training session on new system
- Documentation distribution
- Feedback collection
- System refinement based on feedback

**Documentation Link:**
- RAC: Daily Report Automation documentation
- Department guides: Daily Prompt usage

### Employee Folder Structure Rollout

**What:** 
Announce new individual employee folder structure. Explain structure, benefits, migration plan, and usage guidelines.

**To Whom:** 
All staff, All departments, HR Department

**Channel:** 
Discord channels, Email, Department meetings, All-hands meeting

**Message Type:** 
Initial announcement, Training, Onboarding

**Timing:** 
Before folder structure implementation, during migration phase

**Owner:** 
**Artemchuk Nikolay** (ID: 37226) - AI Department

**Language:** 
English (primary), Russian/Ukrainian (as needed)

**Follow-up Plan:**
- Training sessions on folder structure
- Migration support and assistance
- Documentation distribution
- Q&A sessions

**Documentation Link:**
- RAC: Employee Folder Structure documentation
- Department guides: Individual processing guidelines
- Employee handbook: Folder usage

### Research Collection Process Announcement

**What:** 
Announce new research collection process. Explain how employees can contribute research, how research aggregates into knowledge base, and benefits of centralized knowledge management.

**To Whom:** 
All staff, All departments

**Channel:** 
Discord channels, Email, Department meetings

**Message Type:** 
Initial announcement, Training

**Timing:** 
When research collection process is ready, before knowledge base launch

**Owner:** 
**Artemchuk Nikolay** (ID: 37226) - AI Department

**Language:** 
English (primary), Russian/Ukrainian (as needed)

**Follow-up Plan:**
- Training on research collection
- Research plan template distribution
- Examples and best practices sharing
- Feedback collection

**Documentation Link:**
- RAC: Research Collection Guidelines
- Knowledge Base: Structure documentation
- Research Plan: Template

---

## 13. BLOCKERS & DEPENDENCIES

### Token Limits Blocking AI Processing

**Description:** 
AI systems cannot process very large files (50k+ lines) due to token limitations. Blocks processing of employee export files and large framework files.

**Impact:** 
- Cannot process employees.json file (97,000 lines) directly with AI
- Cannot process large framework files
- Limits automation workflows requiring large file processing
- Blocks data analysis and processing tasks

**Waiting On:** 
- Script development for preprocessing
- Automation setup (n8n or GitHub Actions)
- Unit breakdown strategy implementation

**Resolution Path:**
- Develop scripts for file preprocessing
- Implement unit-based file breakdown
- Set up automation for script execution
- Process files through script pipeline before AI

**Priority:** Critical

**Escalation Needed:** No (being addressed)

**Alternative Solutions:**
- Manual file splitting (temporary workaround)
- Process smaller subsets of data
- Use different AI models (may have different limits but still constrained)

### Need for Script Development

**Description:** 
Scripts are needed for preprocessing large files, but script library and development standards are not yet established. Scripts need to be developed and documented.

**Impact:** 
- Blocks large file processing workflows
- Delays employee data processing
- Prevents automation implementation
- Limits token optimization strategies

**Waiting On:** 
- Script development resources
- Script standards definition
- Automation platform setup
- Script library structure

**Resolution Path:**
- Define script development standards
- Develop initial script library
- Create script templates
- Document script usage and integration

**Priority:** Critical

**Escalation Needed:** No (in progress)

**Alternative Solutions:**
- Use existing scripts if available
- Manual preprocessing (temporary)
- External script development resources

### GitHub Integration Setup Required

**Description:** 
GitHub repositories, GitHub Actions, and GitHub MCP integration need to be set up for script storage, automation, and Cursor integration.

**Impact:** 
- Blocks script storage and version control
- Prevents GitHub Actions automation
- Delays Cursor MCP integration
- Limits script accessibility and sharing

**Waiting On:** 
- GitHub account and repository setup
- GitHub Actions configuration
- GitHub MCP setup and Cursor integration
- Repository structure definition

**Resolution Path:**
- Set up GitHub repositories
- Configure GitHub Actions
- Integrate GitHub MCP with Cursor
- Create repository structure and documentation

**Priority:** Medium

**Escalation Needed:** No

**Alternative Solutions:**
- Use local script storage (temporary)
- Use n8n for automation (alternative to GitHub Actions)
- Manual script management (temporary)

### Employee Folder Structure Design Needed

**Description:** 
Employee folder structure needs to be designed and documented before implementation. Structure must support scripts, agents, library, and templates.

**Impact:** 
- Blocks employee folder creation
- Delays individual-level processing implementation
- Prevents migration from department-level to individual-level
- Limits knowledge management capabilities

**Waiting On:** 
- Folder structure design
- Subfolder organization definition
- Usage guidelines creation
- Migration plan development

**Resolution Path:**
- Design folder structure
- Define subfolder organization
- Create usage guidelines
- Develop migration plan

**Priority:** High

**Escalation Needed:** No

**Alternative Solutions:**
- Use basic folder structure (temporary)
- Implement incrementally
- Start with pilot employees

### Daily Prompt Automation Setup Required

**Description:** 
Cursor Rules or Composer Skills need to be set up for automated daily report generation. Department-specific Daily Prompts need to be created.

**Impact:** 
- Blocks automated daily report generation
- Requires continued manual report processing
- Delays department-specific prompt implementation
- Limits automation capabilities

**Waiting On:** 
- Department-specific Daily Prompt creation
- Cursor Rules/Composer Skills development
- Automation schedule configuration
- Testing and validation

**Resolution Path:**
- Create department-specific Daily Prompts
- Develop Cursor Rules/Composer Skills
- Configure automation schedules
- Test automation workflows

**Priority:** High

**Escalation Needed:** No

**Alternative Solutions:**
- Manual daily report generation (temporary)
- Semi-automated process (AI-assisted but manual trigger)
- Department-by-department rollout

### Knowledge Base Infrastructure Needed

**Description:** 
Knowledge base structure, aggregation system, and Online Academy integration need to be set up for research collection and knowledge management.

**Impact:** 
- Blocks research collection process
- Prevents knowledge base aggregation
- Delays Online Academy integration
- Limits knowledge sharing capabilities

**Waiting On:** 
- Knowledge base structure design
- Aggregation system development
- Online Academy integration setup
- Research collection guidelines creation

**Resolution Path:**
- Design knowledge base structure
- Develop aggregation system
- Set up Online Academy integration
- Create research collection guidelines

**Priority:** Medium

**Escalation Needed:** No

**Alternative Solutions:**
- Use existing storage systems (temporary)
- Manual aggregation process
- Phased implementation

---

## 14. KEY INSIGHTS & LESSONS

### Individual Folders Enable Better Data Identification

**Insight:** 
Moving from department-level to individual employee folders enables better data identification and traceability, especially when using shared admin accounts. Folder location identifies data owner even when account information doesn't.

**Context:** 
Discussion about problem of identifying who made changes when multiple people use shared admin accounts. Folder location provides identification mechanism.

**Application:** 
- Use individual employee folders for all employee data
- Use folder location for data identification and logging
- Process data at individual level, not department level
- Enable folder-based traceability

**Related Concepts:**
- Data ownership and accountability
- Traceability and audit trails
- Individual-level processing

**Impact on Operations:**
- Improves data traceability
- Enables better accountability
- Supports individual-level AI processing
- Reduces confusion about data ownership

**Template/SOP Update:**
- Employee Folder Structure Template
- Individual Processing Guidelines
- Data Identification Procedures

**Department Relevance:** All departments

### Script Preprocessing Saves Tokens

**Insight:** 
Using scripts to preprocess large files before AI processing significantly reduces token usage and enables processing of files that would otherwise exceed AI capabilities.

**Context:** 
Discussion about token limits blocking AI processing of large files. Scripts can handle large files without token constraints, then cleaned data can be processed with AI using fewer tokens.

**Application:**
- Always preprocess large files with scripts before AI processing
- Use scripts for extraction, encoding, cleaning, filtering
- Break large files into units for manageable AI processing
- Automate script execution where possible

**Related Concepts:**
- Token optimization
- Preprocessing pipelines
- Cost optimization
- Efficiency improvement

**Impact on Operations:**
- Enables processing of previously inaccessible data
- Reduces AI token costs
- Improves processing efficiency
- Supports automation workflows

**Template/SOP Update:**
- Large File Processing Guidelines
- Script Development Standards
- Token Optimization Best Practices

**Department Relevance:** AI Department, All departments processing large datasets

### Department-Specific Prompts Improve Relevance

**Insight:** 
Creating department-specific Daily Prompts provides more relevant, focused processing compared to generic prompts. Automation ensures timely, consistent report generation.

**Context:** 
Discussion about improving Daily Prompt by making it department-specific and automating report generation at end of day.

**Application:**
- Create separate Daily Prompt versions for each department
- Tailor prompts to department context and needs
- Automate prompt execution at end of day
- Store prompts in department folders

**Related Concepts:**
- Context-specific processing
- Automation and efficiency
- Department customization
- Timely reporting

**Impact on Operations:**
- Improves report relevance and quality
- Reduces manual work through automation
- Ensures timely report generation
- Provides department-specific insights

**Template/SOP Update:**
- Daily Prompt Templates (department-specific)
- Automation Configuration Guidelines
- Report Generation Procedures

**Department Relevance:** All departments

### Research Should Be Collected Centrally

**Insight:** 
Enabling employees to conduct their own research and aggregating it into a centralized knowledge base creates a powerful knowledge repository. Eventually pushing to Online Academy enables knowledge sharing and learning.

**Context:** 
Discussion about research collection process, knowledge base aggregation, and Online Academy integration. Employees contribute research, it aggregates centrally, then pushes to Online Academy.

**Application:**
- Enable employees to conduct and contribute research
- Aggregate research into centralized knowledge base
- Tag and organize research content
- Push aggregated content to Online Academy

**Related Concepts:**
- Knowledge management
- Distributed contribution
- Centralized aggregation
- Knowledge sharing

**Impact on Operations:**
- Creates comprehensive knowledge repository
- Reduces duplication of research efforts
- Enables knowledge sharing across organization
- Supports Online Academy content development

**Template/SOP Update:**
- Research Collection Guidelines
- Knowledge Base Structure
- Online Academy Integration Procedures

**Department Relevance:** All departments

### Unit-Based Processing Enables Manageable AI Workflows

**Insight:** 
Breaking large files into units (one unit = one employee section) enables manageable AI processing while maintaining data relationships. Scripts handle unit breakdown, then AI processes units individually.

**Context:** 
Discussion about processing employees.json file (97,000 lines). Breaking into units enables processing one employee at a time, staying within token limits.

**Application:**
- Break large files into logical units before processing
- Process units individually with AI
- Use scripts for unit breakdown and preprocessing
- Maintain unit relationships and context

**Related Concepts:**
- Chunking strategies
- Token management
- Data relationships
- Processing efficiency

**Impact on Operations:**
- Enables processing of large datasets
- Maintains data relationships
- Reduces token usage
- Supports automation workflows

**Template/SOP Update:**
- Unit-Based Processing Guidelines
- File Breakdown Procedures
- Processing Workflow Templates

**Department Relevance:** AI Department, HR Department, All departments processing large datasets

---

## 15. ANALOGIES & FRAMEWORKS

### "Focus Points" Analogy

**Analogy:** 
"Focus points" mentioned in conversation - like focus points on a table or in a kitchen. Represents concentrated areas of attention or work.

**Explanation:** 
Employee folders serve as "focus points" - concentrated areas where individual employee data, knowledge, and work are organized and processed. Each folder is a focus point for that employee's information.

**Application:** 
- Use employee folders as focus points for individual processing
- Concentrate employee-related data and knowledge in their folder
- Process and manage at focus point level
- Enable focused AI assistance per employee

**Relevance to Remote Helpers:**
- Supports individual-level organization and processing
- Enables focused attention on each employee's needs
- Creates manageable units of work and data
- Supports personalized AI assistance

**Training Potential:**
- Can be used to explain employee folder concept
- Helps visualize individual-level organization
- Useful for onboarding and training

### Employee Folder as Knowledge Container

**Analogy:** 
Employee folder serves as a knowledge container - holding templates, research, scripts, agents, and other knowledge resources specific to that employee.

**Explanation:** 
Each employee folder contains knowledge and resources relevant to that employee - their templates, research contributions, scripts, configured agents, and learning materials. The folder aggregates and organizes this knowledge.

**Application:**
- Use employee folders to contain employee-specific knowledge
- Aggregate research and learning materials in folders
- Organize templates and resources by employee
- Enable knowledge management at individual level

**Relevance to Remote Helpers:**
- Supports knowledge management strategy
- Enables individual knowledge accumulation
- Facilitates knowledge sharing through aggregation
- Supports learning and development

**Training Potential:**
- Useful for explaining knowledge management approach
- Helps employees understand folder purpose
- Supports research contribution training

---

## 16. EMPLOYEE & TEAM CONTEXT

### Employee Mentions

**Name:** Artemchuk Nikolay  
**Department:** AI  
**Role:** Project manager, Lead generator  
**Context:** 
Primary participant in discussion. Leading entities/libraries upgrade, employee data processing, employee folder structure design, Daily Prompt improvements, research collection process, and automation development.

**Action Items:** 
- Upgrade entities and libraries with department templates
- Process CRM employee export file
- Create employee folder structure
- Develop department-specific Daily Prompts
- Create research collection process
- Develop scripts for large file processing
- Set up GitHub automation
- Create mini-frameworks for individual employees

**Skills/Tools Mentioned:** 
- Cursor, VS Code
- Script development
- Prompt engineering
- Automation (n8n, GitHub Actions)
- AI tools (Claude, ChatGPT)
- Project management

**Development Needs:** 
- Script development skills enhancement
- GitHub Actions and MCP integration knowledge
- Automation workflow design

### Team Dynamics

- **Cross-Department Coordination:** 
  - AI Department leading employee folder structure (affects all departments)
  - HR Department involved in employee data processing
  - All departments will use department-specific Daily Prompts
  - All employees will contribute to research collection

- **Skill Gaps Identified:**
  - Need for prompt engineer role (constantly improving prompts and scripts)
  - Need for administrative assistant role (helping with administration)
  - Script development capabilities needed
  - Automation setup expertise needed

- **Resource Needs:**
  - Script development resources
  - Automation infrastructure (n8n, GitHub Actions)
  - Knowledge base infrastructure
  - GitHub repository setup

- **Collaboration Patterns:**
  - AI Department designing systems for all departments
  - Distributed contribution (employees) with centralized aggregation (AI Department)
  - Individual-level work with department-level coordination

---

## 17. LEAD GENERATION & SALES CONTEXT

*(Not applicable - this call did not involve LG or Sales departments)*

---

## 18. DESIGN & CREATIVE CONTEXT

*(Not applicable - this call did not involve Design department, though design system research was mentioned)*

---

## 19. DEVELOPMENT & TECHNICAL CONTEXT

### Development Work

**Project Type:** Infrastructure, Automation, Data Processing

**Technologies:** 
- Scripting languages (Python, PowerShell, JavaScript - inferred)
- File processing libraries
- Automation platforms (n8n, GitHub Actions)
- AI tools (Claude, ChatGPT)
- Version control (Git, GitHub)
- Cursor IDE with MCP integration

**Development Stage:** 
- Planning (employee folder structure, automation workflows)
- In Progress (employee data processing, units folder creation)
- Script Development (needed)

**Technical Challenges:**
- Token limits in AI systems
- Large file processing
- Data structure inconsistencies (old CRM)
- Automation setup and integration
- Script development and standardization

**Code Quality:**
- Need for script development standards
- Reusable script library needed
- Code documentation required
- Testing strategies needed

**Integration Needs:**
- GitHub MCP with Cursor
- n8n or GitHub Actions for automation
- Online Academy platform integration
- Google Drive integration
- CRM system integration

**DevOps:**
- GitHub Actions for CI/CD
- Automated script execution
- Repository management
- Deployment processes (for scripts and automation)

**AI Coding Tools:** 
- Cursor (primary IDE with AI features)
- Claude (AI assistance)
- ChatGPT (AI assistance)
- Composer (Cursor feature for code generation)

**AI Development Tools:** 
- Cursor, Claude, ChatGPT, Composer
- Script generation capabilities
- AI-assisted development workflows

---

## 20. ONBOARDING & TRAINING CONTEXT

*(Not applicable - this call did not involve HR or training topics, though employee folder structure will impact onboarding)*

---

## 21. FOLLOW-UP ITEMS

### Scheduled Meetings
- None specified in transcript

### Reviews Needed
- Employee folder structure design review
- Script library review and approval
- Daily Prompt department versions review
- Research collection guidelines review
- Knowledge base structure review

### Reports Due
- Daily reports (once automation is set up)
- Processing reports from script execution
- Research aggregation reports

### Template Updates
- **Task Templates:** Need to integrate with entities/libraries upgrade
- **Step Templates:** Need to integrate with entities/libraries upgrade
- **Daily Prompt Templates:** Need department-specific versions
- **Research Plan Template:** Need to create
- **Employee Folder Structure Template:** Need to create
- **Script Templates:** Need to create
- **Mini-Framework Templates:** Need to create (employee-specific, profession-specific)

### RAC Documentation
- Employee Folder Structure documentation
- Script Library documentation
- Large File Processing Guidelines
- Token Optimization Guidelines
- Research Collection Guidelines
- Knowledge Base Structure documentation
- Daily Prompt templates (department-specific)
- GitHub Automation Setup Guide
- Unit-Based Processing Guidelines
- Mini-Framework Template documentation

---

## Processing Notes

**Confidence Levels:**
- **High Confidence:** Artemchuk Nikolay identification, CRM project, Online Academy project, RAC system
- **Medium Confidence:** Some action items inferred from context
- **Low Confidence:** Second participant identification (requires manual verification)

**Manual Review Required:**
- Second participant identification
- Some inferred action items may need clarification
- Timeline estimates need to be determined
- Some technical details may need verification

**Language Handling:**
- Original transcript in Russian/Ukrainian (mixed)
- Processed and translated to English for documentation
- Technical terms preserved where appropriate
- Proper nouns maintained in original form where relevant

**Template Alignment:**
- Action items formatted in "Action + Object" format where possible
- Tasks structured according to Remote Helpers standards
- References to Task Templates and Step Templates included
- RAC integration points identified

---

**End of Document**

