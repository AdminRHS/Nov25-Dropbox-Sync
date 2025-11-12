# Call Processing - December 12, 2025

## 1. MEETING METADATA

**Date:** December 12, 2025 (extracted from folder path)

**Participants:**
- **Artemchuk Nikolay** (ID: 37226) - Project manager, Lead generator | AI | Confidence: High - *Primary speaker, directing discussion*
- **Kizilova Olha** (ID: 178) - Backend Developer | Dev | Confidence: High - *Mentioned by name "Оля", folder owner, discussing Task Manager*
- **Danylenko Liliia** (ID: 72754) - Frontend/Full-Stack Developer | Dev | Confidence: High - *Mentioned "Лилия", discussing calendar event, electricity issues*
- **Zasiadko Matvii** (ID: 86981) - Prompt engineer | AI | Confidence: Medium - *Mentioned "Коля", helping with preparation*
- **Perederii Vladislav** (ID: 86246) - Prompt engineer | AI | Confidence: Medium - *Mentioned "Влад", previously asked to transcribe videos*
- **Skrypkar Vilhelm** (ID: 333) - Illustrator, Graphic Designer | Design | Confidence: Medium - *Mentioned "Вильгельм" as artist who drew pictures*
- **Unknown Participant - Марианка** - Unknown | Unknown | Confidence: Low - *Mentioned as recording, requires manual verification*

**Duration:** Not explicitly mentioned (appears to be extended team meeting)

**Main Topics:**
1. Task Manager workflow structure and data parsing requirements
2. Data architecture optimization for RAG (Retrieval-Augmented Generation) systems
3. Employee profile data structure and CRM export integration
4. Library organization and taxonomy synchronization
5. Training and onboarding strategy for data architecture understanding
6. Tool integration (MCP, Claude, Perplexity) and automation workflows

**Related Project(s):**
- **CRM** - Matched from Project Directory - Confidence: High - *Discussed employee exports, profiles, unit templates*
- **Online Academy** - Matched from Project Directory - Confidence: High - *Mentioned course updates, documentation needs*
- **Task Manager** - Not in Project Directory - *New project or infrastructure component* - Confidence: Medium - *Requires manual mapping*
- **Microservices** - Not in Project Directory - *Architecture discussion* - Confidence: Medium - *Mentioned as dev-specific project*

**Related Platforms:** 
- Recruitment Platform (employee profiles, talent management)
- Infrastructure (data architecture, library systems)

**Department(s) Involved:** 
- Dev (primary - Kizilova Olha, Danylenko Liliia)
- AI (Artemchuk Nikolay, Zasiadko Matvii, Perederii Vladislav)
- Design (Skrypkar Vilhelm mentioned)

---

## 2. EXECUTIVE SUMMARY

The meeting focused on restructuring Remote Helpers' data architecture to support AI-first operations through RAG (Retrieval-Augmented Generation) systems. The primary challenge is organizing massive amounts of unstructured data (millions of files) into clean, structured formats that AI systems can efficiently process. Key decisions include: implementing data deduplication strategies, creating synchronization workflows between Dropbox and library systems, establishing training programs for developers to understand data architecture, and migrating microservices data to file-based structures. The strategic direction emphasizes moving from manual data entry to automated, AI-driven data processing and generation, with immediate focus on employee profile data, Task Manager workflows, and library taxonomy organization. The team committed to dedicating half a day per week per developer to work on file systems and libraries as AI assistants.

---

## 3. ACTION ITEMS & TASKS

### Parse and Sort Task Manager Data
- **Description:** Parse Task Manager data (use cases, workflows, steps) and sort into proper structure - convert "use cases" to "responsibilities", separate tasks from steps, maintain claim workbook
- **Owner/Assignee:** Kizilova Olha (ID: 178) - Backend Developer | Dev
- **Department:** Dev
- **Profession:** Backend Developer
- **Priority:** High
- **Timeline:** Immediate
- **Dependencies:** Understanding Task Manager structure
- **Status:** Not Started
- **Related Project:** Task Manager
- **Task Template:** Parse data + Sort structure
- **Tools Required:** Task Manager system, Data parsing tools

### Remove Duplicate Data from Library Actions
- **Description:** Remove processes and results from library actions file - they are duplicated 3 times (exist in separate Process folder), causing excessive data consumption
- **Owner/Assignee:** Kizilova Olha (ID: 178) - Backend Developer | Dev
- **Department:** Dev
- **Profession:** Backend Developer
- **Priority:** Critical
- **Timeline:** Immediate
- **Dependencies:** None
- **Status:** Not Started
- **Related Project:** Library Infrastructure
- **Task Template:** Remove duplicates + Clean data
- **Tools Required:** File editor, Claude (for bulk changes)

### Convert Markdown to JSON for Task Manager Steps
- **Description:** Evaluate converting Task Manager step data from Markdown to JSON format for better AI processing
- **Owner/Assignee:** Kizilova Olha (ID: 178) - Backend Developer | Dev
- **Department:** Dev
- **Profession:** Backend Developer
- **Priority:** Medium
- **Timeline:** After parsing task
- **Dependencies:** Parse and Sort Task Manager Data
- **Status:** Not Started
- **Related Project:** Task Manager
- **Task Template:** Convert format + Evaluate structure
- **Tools Required:** Format conversion tools, Claude

### Fix MCP Integration Placement in Task Manager
- **Description:** Move MCP integration from tools array to proper tool category (currently incorrectly placed in line 32)
- **Owner/Assignee:** Kizilova Olha (ID: 178) - Backend Developer | Dev
- **Department:** Dev
- **Profession:** Backend Developer
- **Priority:** Medium
- **Timeline:** During Task Manager cleanup
- **Dependencies:** Parse and Sort Task Manager Data
- **Status:** Not Started
- **Related Project:** Task Manager
- **Task Template:** Fix placement + Update structure
- **Tools Required:** Task Manager system

### Replace Claude Desktop with Claude Code
- **Description:** Update Task Manager to use Claude Code instead of Claude Desktop
- **Owner/Assignee:** Kizilova Olha (ID: 178) - Backend Developer | Dev
- **Department:** Dev
- **Profession:** Backend Developer
- **Priority:** Medium
- **Timeline:** During Task Manager cleanup
- **Dependencies:** Fix MCP Integration Placement
- **Status:** Not Started
- **Related Project:** Task Manager
- **Task Template:** Update tool + Replace reference
- **Tools Required:** Task Manager system

### Create Employee Profile Data Structure Analysis
- **Description:** Analyze employees unit template (400 lines per employee) - understand all fields, identify what can be auto-filled from scenarios/scripts/closables
- **Owner/Assignee:** Kizilova Olha (ID: 178) - Backend Developer | Dev
- **Department:** Dev
- **Profession:** Backend Developer
- **Priority:** High
- **Timeline:** Within week
- **Dependencies:** Access to CRM export folder
- **Status:** Not Started
- **Related Project:** CRM
- **Task Template:** Analyze structure + Document fields
- **Tools Required:** CRM export files, Data analysis tools

### Clean and Organize Library Actions File
- **Description:** Clean library actions file - remove unnecessary fields, keep only IDs for processes (processes exist in separate Process folder), understand object structure
- **Owner/Assignee:** Kizilova Olha (ID: 178) - Backend Developer | Dev
- **Department:** Dev
- **Profession:** Backend Developer
- **Priority:** High
- **Timeline:** Immediate
- **Dependencies:** None
- **Status:** Not Started
- **Related Project:** Library Infrastructure
- **Task Template:** Clean data + Remove duplicates
- **Tools Required:** Claude, File editor

### Add Perplexity Browser Integration
- **Description:** Add Perplexity browser to tool stack (currently using Google Chrome) - productivity tool that can sync with library/laboratory by action objects
- **Owner/Assignee:** Kizilova Olha (ID: 178) - Backend Developer | Dev
- **Department:** Dev
- **Profession:** Backend Developer
- **Priority:** Medium
- **Timeline:** Within month
- **Dependencies:** Library synchronization setup
- **Status:** Not Started
- **Related Project:** Library Infrastructure
- **Task Template:** Add tool + Configure integration
- **Tools Required:** Perplexity AI, Library system

### Create Lips Database Copy and Synchronization
- **Description:** Create copy of Lips database (empty base), populate with accumulated Lips data, set up synchronization to update database every 3 hours
- **Owner/Assignee:** Kizilova Olha (ID: 178) - Backend Developer | Dev
- **Department:** Dev
- **Profession:** Backend Developer
- **Priority:** High
- **Timeline:** Within month
- **Dependencies:** Lips data collection
- **Status:** Not Started
- **Related Project:** Online Academy
- **Task Template:** Create database + Setup sync
- **Tools Required:** Database system, Synchronization scripts

### Update Online Academy Courses
- **Description:** Update Online Academy courses (most are outdated) - use browser tools (Perplexity) to update content
- **Owner/Assignee:** Kizilova Olha (ID: 178) - Backend Developer | Dev
- **Department:** Dev
- **Profession:** Backend Developer
- **Priority:** Medium
- **Timeline:** After Lips database setup
- **Dependencies:** Create Lips Database Copy
- **Related Project:** Online Academy
- **Task Template:** Update content + Refresh courses
- **Tools Required:** Perplexity AI, Online Academy system

### Create Account Data Templates
- **Description:** Create unified template for all account fields (job accounts, lead accounts, accounts prod) - clean empty fields, define all fields, consult and upload
- **Owner/Assignee:** Kizilova Olha (ID: 178) - Backend Developer | Dev
- **Department:** Dev
- **Profession:** Backend Developer
- **Priority:** High
- **Timeline:** Within month
- **Dependencies:** Access to account files
- **Status:** Not Started
- **Related Project:** CRM
- **Task Template:** Create template + Standardize data
- **Tools Required:** Account files, Template system

### Fix Dev-Specific Project References
- **Description:** Find and replace "WordPress Developer" with "microservices" in dev-specific project files (project 29 DWS) - use Composer to find all references
- **Owner/Assignee:** Kizilova Olha (ID: 178) - Backend Developer | Dev
- **Department:** Dev
- **Profession:** Backend Developer
- **Priority:** Medium
- **Timeline:** Immediate
- **Dependencies:** None
- **Status:** Not Started
- **Related Project:** Microservices
- **Task Template:** Find references + Replace text
- **Tools Required:** Composer, File search tools

### Organize and Classify Reversal Prompts
- **Description:** Sort and classify reversal prompts so they can be easily found - create index with metadata for prompt location and use cases
- **Owner/Assignee:** Kizilova Olha (ID: 178) - Backend Developer | Dev
- **Department:** Dev
- **Profession:** Backend Developer
- **Priority:** Medium
- **Timeline:** Within month
- **Dependencies:** Prompt collection
- **Status:** Not Started
- **Related Project:** Library Infrastructure
- **Task Template:** Organize prompts + Create index
- **Tools Required:** Prompt files, Indexing system

### Move Dev Prompts to Prompts Folder
- **Description:** Move developer prompts to centralized prompts folder (organized by process, flow, libraries)
- **Owner/Assignee:** Kizilova Olha (ID: 178) - Backend Developer | Dev
- **Department:** Dev
- **Profession:** Backend Developer
- **Priority:** Low
- **Timeline:** After prompt organization
- **Dependencies:** Organize and Classify Reversal Prompts
- **Status:** Not Started
- **Related Project:** Library Infrastructure
- **Task Template:** Move files + Update references
- **Tools Required:** File system, Prompts folder

### Setup Weekly Training Sessions
- **Description:** Schedule half-day per week training sessions for each developer (Kizilova Olha, Danylenko Liliia) to work on file systems and libraries as AI assistants
- **Owner/Assignee:** Artemchuk Nikolay (ID: 37226) - Project manager | AI
- **Department:** AI / Dev
- **Profession:** Project Manager
- **Priority:** High
- **Timeline:** Starting next week
- **Dependencies:** Calendar coordination
- **Status:** Not Started
- **Related Project:** Training & Onboarding
- **Task Template:** Schedule sessions + Coordinate calendars
- **Tools Required:** Google Calendar, Discord

### Share Calendar Event with Team
- **Description:** Danylenko Liliia to share calendar event (11:00 Ukraine time) with Kizilova Olha, Admin, and Discord chat - event about electricity outage
- **Owner/Assignee:** Danylenko Liliia (ID: 72754) - Frontend/Full-Stack Developer | Dev
- **Department:** Dev
- **Profession:** Frontend/Full-Stack Developer
- **Priority:** Low
- **Timeline:** Immediate
- **Dependencies:** None
- **Status:** Not Started
- **Related Project:** Communication
- **Task Template:** Share event + Notify team
- **Tools Required:** Google Calendar, Discord

---

## 4. PROJECTS & FEATURES

### Task Manager - Infrastructure Component

**Project Match:** Not in Project Directory - *New infrastructure component* - Confidence: Medium - *Requires manual mapping*

**Status:** In Development

**Platform:** Infrastructure

**Description:** Workflow and task management system that organizes tasks, steps, and checklists. Currently contains data that needs parsing and restructuring - use cases should be responsibilities, tasks need to be separated from steps, step templates need to be properly organized.

**Key Features:**
- Task creation and management
- Step templates system
- Workflow definitions
- Checklist integration
- MCP integration (needs fixing)
- Tool references

**Current Issues:**
- Data structure needs parsing (use cases vs responsibilities confusion)
- MCP integration incorrectly placed in tools array
- Steps and tasks are mixed together
- Markdown format may need conversion to JSON
- Claude Desktop reference should be Claude Code
- Missing step templates after transcription

**Next Steps:**
1. Parse existing Task Manager data
2. Separate tasks from steps
3. Convert use cases to responsibilities
4. Fix MCP integration placement
5. Update Claude Desktop to Claude Code
6. Evaluate Markdown to JSON conversion

**Stakeholders:**
- **Artemchuk Nikolay** (ID: 37226) - AI Department - *System architect*
- **Kizilova Olha** (ID: 178) - Dev Department - *Implementation*

**Related Resources:**
- Task Manager system files
- Step templates folder
- Prompts folder

**AI Integration:** 
- Claude (for data parsing and restructuring)
- MCP integration (needs proper placement)
- AI-driven workflow generation

### CRM - Employee Data Management

**Project Match:** **CRM** - Matched from Project Directory - Confidence: High

**Status:** In Development

**Platform:** Recruitment Platform

**Description:** Customer Relationship Management system handling employee profiles, exports, and data synchronization. Employee unit template contains 400 lines of data per employee including photos, resumes, video interviews, tasks, and various metadata fields.

**Key Features:**
- Employee profile management
- CRM export functionality
- Employee unit templates (400 lines per employee)
- Integration with Dropbox
- Task assignment tracking
- Media file management (photos, resumes, videos)

**Current Issues:**
- Employee profiles not filled (old skills, unknown libraries)
- Data structure needs understanding and cleaning
- Export functionality exists but data quality issues
- Need to understand which fields can be auto-filled from scenarios/scripts

**Next Steps:**
1. Analyze employees unit template structure
2. Identify auto-fillable fields from scenarios/scripts/closables
3. Clean and organize employee data
4. Update profile information
5. Connect tasks to employee profiles

**Stakeholders:**
- **Artemchuk Nikolay** (ID: 37226) - AI Department - *Data architecture*
- **Kizilova Olha** (ID: 178) - Dev Department - *Backend implementation*
- **Skrypkar Vilhelm** (ID: 333) - Design Department - *Artist/designer mentioned in employee data*

**Related Resources:**
- CRM export folder: `/ExportCRMS/employees/`
- Employee unit templates
- Niko November 25 positions folder

**AI Integration:**
- AI-driven data population
- Automated profile updates
- Task generation from employee data

### Online Academy - Educational Platform

**Project Match:** **Online Academy** - Matched from Project Directory - Confidence: High

**Status:** Needs Update

**Platform:** Educational Platform

**Description:** Educational platform with courses that need updating. Most courses created are outdated and require refresh. Integration with library system and Lips database for content synchronization.

**Key Features:**
- Course management
- Content updates
- Lips database integration
- Browser tool integration (Perplexity)
- Taxonomy synchronization

**Current Issues:**
- Most courses are outdated (more than half)
- Need browser tools (Perplexity) for updates
- Library synchronization not working
- Taxonomy updates not reflected

**Next Steps:**
1. Create Lips database copy
2. Populate with accumulated Lips data
3. Setup 3-hour synchronization schedule
4. Update courses using Perplexity browser
5. Integrate with library taxonomy

**Stakeholders:**
- **Artemchuk Nikolay** (ID: 37226) - AI Department - *Content strategy*
- **Kizilova Olha** (ID: 178) - Dev Department - *Technical implementation*

**Related Resources:**
- Lips database
- Online Academy system
- Library taxonomy files

**AI Integration:**
- Perplexity AI for content research and updates
- AI-driven course generation
- Automated taxonomy synchronization

### Microservices - Architecture Project

**Project Match:** Not in Project Directory - *Architecture discussion* - Confidence: Medium - *Mentioned as dev-specific project*

**Status:** In Development

**Platform:** Infrastructure

**Description:** Microservices architecture project replacing WordPress Developer references. Dev-specific project (project 29 DWS) that needs reference cleanup.

**Key Features:**
- Microservices architecture
- Service separation
- API integration

**Current Issues:**
- Incorrect references to "WordPress Developer" instead of "microservices"
- Need to find and replace all references using Composer

**Next Steps:**
1. Find all "WordPress Developer" references
2. Replace with "microservices"
3. Verify no remaining references

**Stakeholders:**
- **Kizilova Olha** (ID: 178) - Dev Department - *Implementation*

**Related Resources:**
- Dev-specific project files
- Composer tool

**AI Integration:** Not specified

---

## 5. WORKFLOWS & PROCESSES

### Task Manager Workflow Creation Process

**Purpose:** Create workflows from objects, form steps from actions plus objects. Workflow defines task structure, steps define execution sequence.

**SOP Reference:** Task Template structure (Action + Object format)

**Steps:**
1. **Define Workflow Concept** - Identify the overall workflow purpose
   - **Responsibility:** Project Manager / Developer
   - **Tool:** Task Manager system
   - **Placement:** Task Manager workflow definition
2. **Generate Steps from Actions** - Break down workflow into actionable steps
   - **Responsibility:** Developer
   - **Tool:** Task Manager, Claude
   - **Placement:** Step templates section
3. **Create Task from Workflow** - Convert workflow into executable task
   - **Responsibility:** Developer
   - **Tool:** Task Manager
   - **Placement:** Task creation interface
4. **Assign Tools and Resources** - Link appropriate tools to each step
   - **Responsibility:** Developer
   - **Tool:** Task Manager
   - **Placement:** Step configuration

**Responsible Parties:**
- **Artemchuk Nikolay** (ID: 37226) - AI - *Workflow design*
- **Kizilova Olha** (ID: 178) - Dev - *Implementation*

**Tools/Platforms Used:** Task Manager, Claude, MCP integration

**Success Criteria:** 
- Workflows properly structured with clear steps
- Steps can be executed independently
- Tools correctly assigned to steps

**Automation Opportunities:**
- AI-driven workflow generation from descriptions
- Automatic step creation from action objects
- Tool assignment suggestions based on step type

### Daily Report Processing Workflow

**Purpose:** Process daily call transcriptions into structured data that feeds into library system and updates employee profiles with latest tasks.

**SOP Reference:** MAIN PROMPT v3.md processing instructions

**Steps:**
1. **Transcribe Call** - Record and transcribe team calls
   - **Responsibility:** Recording system / Marianka
   - **Tool:** Recording device
   - **Placement:** Call recording
2. **Process with MAIN PROMPT** - Apply MAIN PROMPT v3.md to extract structured data
   - **Responsibility:** AI Assistant (Claude)
   - **Tool:** Claude, MAIN PROMPT v3.md
   - **Placement:** Processing pipeline
3. **Extract Action Items** - Identify tasks, steps, and action items
   - **Responsibility:** AI Assistant
   - **Tool:** Claude
   - **Placement:** Structured output
4. **Update Library** - Add new taxonomy terms, tools, responsibilities to library
   - **Responsibility:** Automated system
   - **Tool:** MCP integration, Library system
   - **Placement:** Library taxonomy files
5. **Update Employee Profiles** - Add latest completed tasks to employee profiles
   - **Responsibility:** Automated system
   - **Tool:** MCP integration, Employee system
   - **Placement:** Employee profile files

**Responsible Parties:**
- **Artemchuk Nikolay** (ID: 37226) - AI - *Process design*
- **Kizilova Olha** (ID: 178) - Dev - *Automation implementation*

**Tools/Platforms Used:** Claude, MCP, Library system, Employee profiles, Dropbox

**Success Criteria:**
- Daily reports automatically processed
- Library taxonomy stays current
- Employee profiles reflect latest work

**Automation Opportunities:**
- Fully automated transcription processing
- Real-time library updates
- Automatic profile synchronization

### Data Architecture Optimization Process

**Purpose:** Optimize data structure for RAG (Retrieval-Augmented Generation) systems by removing duplicates, organizing files, and creating efficient data access patterns.

**SOP Reference:** RAG system architecture principles

**Steps:**
1. **Identify Duplicates** - Find and catalog duplicate data across files
   - **Responsibility:** Developer
   - **Tool:** Claude, File analysis tools
   - **Placement:** Library files
2. **Remove Redundancies** - Eliminate duplicate processes, results, and data
   - **Responsibility:** Developer
   - **Tool:** Claude (for bulk changes)
   - **Placement:** Library structure
3. **Organize by Priority** - Structure data with top 10 most important items per folder (not 1500)
   - **Responsibility:** Developer
   - **Tool:** Claude, Data organization scripts
   - **Placement:** Folder structure
4. **Create Metadata Indexes** - Build indexes with metadata for efficient searching
   - **Responsibility:** Developer
   - **Tool:** Indexing system
   - **Placement:** Library indexes

**Responsible Parties:**
- **Artemchuk Nikolay** (ID: 37226) - AI - *Architecture design*
- **Kizilova Olha** (ID: 178) - Dev - *Implementation*

**Tools/Platforms Used:** Claude, File system, Indexing tools

**Success Criteria:**
- No duplicate data in system
- Each folder contains only top 10 relevant items
- Fast AI processing of data structures
- Efficient search and retrieval

**Automation Opportunities:**
- Automated duplicate detection
- AI-driven data prioritization
- Automatic metadata generation

### Reversal Prompting Process

**Purpose:** Improve prompts by rewriting them after task completion, capturing optimized versions for reuse.

**SOP Reference:** Prompt engineering best practices

**Steps:**
1. **Complete Task** - Finish the original task using initial prompt
   - **Responsibility:** Developer / AI Assistant
   - **Tool:** Claude, Task execution tools
   - **Placement:** Task execution
2. **Request Reversal** - Ask AI to rewrite the original prompt with improvements
   - **Responsibility:** Developer
   - **Tool:** Claude
   - **Placement:** Prompt optimization
3. **Save Optimized Prompt** - Store improved prompt for future use
   - **Responsibility:** Developer
   - **Tool:** Prompt storage system
   - **Placement:** Prompts folder with metadata
4. **Classify and Index** - Organize prompts by use case and create searchable index
   - **Responsibility:** Developer
   - **Tool:** Indexing system
   - **Placement:** Prompt index with metadata

**Responsible Parties:**
- **Artemchuk Nikolay** (ID: 37226) - AI - *Process design*
- **Kizilova Olha** (ID: 178) - Dev - *Implementation*

**Tools/Platforms Used:** Claude, Prompt storage, Indexing system

**Success Criteria:**
- Prompts continuously improved
- Easy to find relevant prompts
- Reduced prompt creation time

**Automation Opportunities:**
- Automated prompt optimization suggestions
- AI-driven prompt classification
- Automatic indexing of new prompts

---

## 6. RULES & BEST PRACTICES

### Data Architecture - RAG System Optimization

**Rule/Practice:** Apply data architecture knowledge for RAG systems - use many small scripts that monitor content quality, not large files that consume excessive resources.

**Rationale:** AI systems cannot efficiently process massive amounts of information, especially during prompt execution. Large files slow down processing and increase costs.

**Application:** 
- Keep individual files small and focused
- Remove duplicate data (processes, results exist in separate folders)
- Organize data with top 10 items per folder, not 1500
- Create metadata indexes for efficient searching

**Examples:**
- Library actions file should not contain processes/results (they exist in Process folder)
- Each folder should contain only most relevant items
- Use metadata to enable fast AI navigation

**Affected Departments:** All departments (Dev, AI, Design, Video, LG, HR)

**Template Integration:** Should become part of RAG system architecture SOP

### Prompt Engineering - Reversal Prompting

**Rule/Practice:** After completing a task, use reversal prompting - ask AI to rewrite your original prompt with all improvements and corrections, then save the optimized version.

**Rationale:** Continuously improves prompt quality, reduces future prompt creation time, creates reusable prompt library.

**Application:**
- After task completion, request prompt rewrite
- Save optimized prompts with metadata
- Classify prompts by use case and process type
- Create searchable index for prompt discovery

**Examples:**
- Complete microservice task → request reversal → save optimized prompt
- Organize prompts by process, flow, libraries
- Use metadata to enable "find prompt for X task" queries

**Affected Departments:** AI, Dev (primary users of prompts)

**Template Integration:** Should become part of Prompt Engineering SOP

### Data Processing - Top 10 Principle

**Rule/Practice:** When organizing data for AI processing, include only top 10 most relevant items per folder, not hundreds or thousands.

**Rationale:** AI systems can more easily navigate and process smaller, prioritized datasets. Large folders slow down processing and reduce accuracy.

**Application:**
- Prioritize data by usage frequency (log tool usage to rank)
- Keep only top 10 items per folder
- Use metadata to guide AI to relevant subfolders
- Apply "Turkish horde" principle - break large territories into small groups

**Examples:**
- Library folder: top 10 tools, not 1500
- Action folder: top 10 actions, not all actions
- Process folder: top 10 processes, not all processes

**Affected Departments:** All departments

**Template Integration:** Should become part of Data Organization SOP

### AI Tool Usage - Manual Review Required

**Rule/Practice:** When using Claude for bulk changes, do NOT use auto-playlist/auto-confirmation - use manual confirmation, review each change, read what Claude writes, and gradually accumulate feedback.

**Rationale:** Ensures quality, prevents errors, allows learning from AI suggestions, builds institutional knowledge.

**Application:**
- Review Claude's plans before execution
- Confirm each change individually
- Read and understand AI reasoning
- Document feedback for future improvements

**Examples:**
- Claude suggests folder reorganization → review plan → confirm changes one by one
- AI proposes data structure changes → understand reasoning → approve with modifications

**Affected Departments:** All departments using AI tools

**Template Integration:** Should become part of AI Collaboration SOP

### Training - Incremental Learning

**Rule/Practice:** Teach new concepts like English lessons - one new word at a time, gradually building understanding of data architecture and file systems.

**Rationale:** Reduces cognitive overload, allows gradual skill building, makes complex systems approachable.

**Application:**
- Introduce one concept per session
- Build on previous knowledge
- Use practical examples
- Provide hands-on practice

**Examples:**
- Session 1: Understand folder structure
- Session 2: Learn about data deduplication
- Session 3: Practice with AI tools
- Continue building complexity

**Affected Departments:** All departments (especially new employees)

**Template Integration:** Should become part of Onboarding and Training SOP

### Data Synchronization - Single Source of Truth

**Rule/Practice:** Maintain single source of truth - Dropbox structure should match Library structure, synchronized automatically. All changes go through main folder manager script, which coordinates with subfolder scripts.

**Rationale:** Prevents data conflicts, ensures consistency, enables reliable automation.

**Application:**
- Dropbox structure mirrors Library structure
- Synchronization scripts run on schedule (e.g., every 3 hours)
- Main script coordinates, subfolder scripts handle local changes
- No data duplication between systems

**Examples:**
- Library taxonomy updated → syncs to Dropbox
- Dropbox file changed → syncs to Library
- Both systems stay in sync automatically

**Affected Departments:** All departments

**Template Integration:** Should become part of Data Synchronization SOP

---

## 7. PROBLEMS & SOLUTIONS

### Problem: Massive Unstructured Data Files

**Description:** Millions of files exist in unorganized state, making it impossible for AI systems to efficiently process information. Files are too large, contain duplicates, and lack proper structure.

**Impact:** 
- AI processing is slow and expensive
- Difficult to find relevant information
- Data quality issues
- Cannot effectively use RAG systems

**Root Cause:** 
- Lack of data architecture planning
- Manual data entry without structure
- No deduplication processes
- Files created without organization principles

**Proposed Solution:** 
- Implement RAG-optimized data architecture
- Remove duplicates (processes/results exist in separate folders)
- Organize data with top 10 principle per folder
- Create metadata indexes for efficient searching
- Use small, focused files instead of large ones

**AI Solution Potential:** High - Claude can help identify duplicates, reorganize data, create indexes

**Decision Made:** Proceed with data architecture optimization, starting with library actions file cleanup

**Implementation Owner:** Kizilova Olha (ID: 178) - Backend Developer | Dev

**Status:** In Progress

**Documentation Needed:** RAG system architecture guide, data organization SOP

### Problem: Task Manager Data Structure Confusion

**Description:** Task Manager contains mixed data - use cases labeled incorrectly (should be responsibilities), tasks and steps are mixed together, step templates are missing after transcription.

**Impact:**
- Cannot properly parse Task Manager data
- Workflows cannot be correctly generated
- Steps and tasks are confused
- Missing step templates

**Root Cause:**
- Data was entered without clear structure
- Transcription process lost some data
- No validation of data format

**Proposed Solution:**
- Parse and sort Task Manager data
- Convert "use cases" to "responsibilities"
- Separate tasks from steps
- Recreate missing step templates
- Evaluate Markdown to JSON conversion

**AI Solution Potential:** High - Claude can help parse and reorganize data

**Decision Made:** Proceed with parsing and restructuring Task Manager data

**Implementation Owner:** Kizilova Olha (ID: 178) - Backend Developer | Dev

**Status:** Not Started

**Documentation Needed:** Task Manager data structure documentation

### Problem: Employee Profiles Not Filled

**Description:** Employee profiles in system are not filled - contain old skills, unknown libraries, outdated information. Clients request employee resumes and see outdated data.

**Impact:**
- Poor client perception
- Inaccurate employee representation
- Cannot showcase company growth
- Missing current skills and tasks

**Root Cause:**
- Manual data entry is too slow
- No automation for profile updates
- Data not synchronized from daily work
- Lack of data sources

**Proposed Solution:**
- Automate profile updates from daily reports
- Connect tasks to employee profiles
- Synchronize library skills to profiles
- Update profiles with latest completed work
- Use MCP integration for automatic updates

**AI Solution Potential:** Very High - AI can extract task information from daily reports and update profiles automatically

**Decision Made:** Implement automated profile updates via MCP integration

**Implementation Owner:** Kizilova Olha (ID: 178) - Backend Developer | Dev

**Status:** Proposed

**Documentation Needed:** Employee profile automation workflow

### Problem: Online Academy Courses Outdated

**Description:** More than half of Online Academy courses are outdated and need updating. Current process is manual and slow.

**Impact:**
- Students learn outdated information
- Poor educational quality
- Cannot generate new courses efficiently
- Wasted development effort

**Root Cause:**
- Manual course update process
- No browser tools for research
- Library not synchronized with courses
- No automation for content updates

**Proposed Solution:**
- Add Perplexity browser for research
- Create Lips database copy
- Setup 3-hour synchronization
- Use AI tools to update course content
- Integrate with library taxonomy

**AI Solution Potential:** Very High - Perplexity AI and other tools can research and update content automatically

**Decision Made:** Proceed with Perplexity integration and Lips database setup

**Implementation Owner:** Kizilova Olha (ID: 178) - Backend Developer | Dev

**Status:** Proposed

**Documentation Needed:** Online Academy update workflow

### Problem: Developers Lack Data Architecture Understanding

**Description:** Developers understand code but not data architecture. They cannot identify data structure issues, organize files effectively, or work with RAG systems.

**Impact:**
- Cannot effectively help with data organization
- Slow progress on data architecture
- Dependence on single person (Artemchuk Nikolay)
- Cannot scale data work

**Root Cause:**
- Focus on code, not data
- No training on data architecture
- Data work seen as separate from development
- Lack of understanding of RAG systems

**Proposed Solution:**
- Weekly half-day training sessions
- Work together on file systems and libraries
- Learn data architecture principles
- Practice with AI tools
- Gradually build understanding

**AI Solution Potential:** Medium - AI can assist in training and provide examples

**Decision Made:** Implement weekly training sessions starting next week

**Implementation Owner:** Artemchuk Nikolay (ID: 37226) - Project Manager | AI

**Status:** Approved

**Documentation Needed:** Data architecture training curriculum

### Problem: Microservices Data Not Accessible

**Description:** Microservices are developed but data cannot be easily added because data is not prepared in correct format. Manual data entry is too slow and impractical.

**Impact:**
- Microservices exist but are not usable
- Cannot populate systems with data
- Manual entry is too slow
- Data format mismatch

**Root Cause:**
- Data not structured for microservices
- No file-based data structure
- Data exists only in old CRM format
- No migration path

**Proposed Solution:**
- Migrate microservices data to file-based structure
- Structure data in Dropbox to match microservices needs
- Create data templates
- Enable easy editing and consultation
- Generate content from data or vice versa

**AI Solution Potential:** High - AI can help structure data and create templates

**Decision Made:** Proceed with file-based data structure migration

**Implementation Owner:** Kizilova Olha (ID: 178) - Backend Developer | Dev

**Status:** Proposed

**Documentation Needed:** Microservices data migration guide

---

## 8. TOOLS & RESOURCES

### Claude (Anthropic)

**Type:** AI Tool

**Category:** Large Language Models

**Purpose:** Primary AI assistant for data processing, prompt engineering, bulk file changes, and workflow generation

**Use Case:** 
- Parsing Task Manager data
- Removing duplicates from library files
- Creating data structure plans
- Processing daily reports
- Reversal prompting

**Access/Links:** https://claude.ai/login?returnTo=%2F%3F

**Recommended For:** All departments, especially Dev and AI

**Current Users:** Artemchuk Nikolay, Kizilova Olha, Danylenko Liliia

**Notes:** 
- Do NOT use auto-playlist/auto-confirmation
- Use manual confirmation for bulk changes
- Review each change and read AI reasoning
- Gradually accumulate feedback

**Integration with Stack:** Core tool for all data processing and AI workflows

### Claude Code

**Type:** AI Tool

**Category:** AI Development Tools

**Purpose:** Claude's code-focused interface (replacing Claude Desktop)

**Use Case:** 
- Code generation and review
- Development workflows
- Task Manager integration

**Access/Links:** Part of Claude ecosystem

**Recommended For:** Dev department

**Current Users:** Kizilova Olha (to be implemented)

**Notes:** Should replace Claude Desktop references in Task Manager

**Integration with Stack:** Integrated with Task Manager, MCP

### MCP (Model Context Protocol)

**Type:** Integration Tool

**Category:** Integration & Automation

**Purpose:** Protocol for connecting AI tools to external systems, enabling automatic data updates

**Use Case:**
- Connecting library to daily reports
- Updating employee profiles automatically
- Synchronizing taxonomy
- Adding tools to library from video transcriptions

**Access/Links:** MCP integration system

**Recommended For:** Dev and AI departments

**Current Users:** In development

**Notes:** 
- Currently incorrectly placed in Task Manager tools array
- Should be in proper tool category
- Enables automatic library and profile updates

**Integration with Stack:** Connects Claude to Library, Employee profiles, Dropbox

### Perplexity AI

**Type:** AI Tool

**Category:** AI Research & Analysis Tools

**Purpose:** AI-powered search engine for research and content updates

**Use Case:**
- Updating Online Academy courses
- Researching current information
- Content generation
- Browser-based productivity tool

**Access/Links:** https://www.perplexity.ai/

**Recommended For:** All departments needing research, especially for content updates

**Current Users:** To be added (replacing/supplementing Google Chrome)

**Notes:** 
- Productivity tool that can sync with library/laboratory
- Should be added to tool stack
- Can work with action objects from library

**Integration with Stack:** Can sync with library system, used for Online Academy updates

### Task Manager

**Type:** Development Tool

**Category:** Workflow Management

**Purpose:** System for managing tasks, workflows, steps, and checklists

**Use Case:**
- Creating and managing tasks
- Defining workflows
- Organizing step templates
- Tracking task completion

**Access/Links:** Task Manager system

**Recommended For:** All departments

**Current Users:** Artemchuk Nikolay, Kizilova Olha

**Notes:** 
- Needs data parsing and restructuring
- Contains step templates
- MCP integration needs fixing
- May need Markdown to JSON conversion

**Integration with Stack:** Integrates with MCP, Claude, Library system

### Composer

**Type:** Development Tool

**Category:** Code Search & Replacement

**Purpose:** Tool for finding and replacing text across multiple files

**Use Case:**
- Finding "WordPress Developer" references
- Replacing with "microservices"
- Bulk text replacement

**Access/Links:** Development tool

**Recommended For:** Dev department

**Current Users:** Kizilova Olha

**Notes:** Used for fixing project references

**Integration with Stack:** Part of development workflow

### Google Calendar

**Type:** Communication Platform

**Category:** Digital Tools

**Purpose:** Calendar and event management

**Use Case:**
- Scheduling training sessions
- Coordinating team meetings
- Sharing events with team

**Access/Links:** Google Workspace

**Recommended For:** All departments

**Current Users:** Danylenko Liliia, Artemchuk Nikolay

**Notes:** 
- Danylenko Liliia has event at 11:00 Ukraine time
- Needs to share with team (Kizilova Olha, Admin, Discord)

**Integration with Stack:** Part of Google Workspace, integrates with Discord

### Discord

**Type:** Communication Platform

**Category:** Digital Tools

**Purpose:** Team communication and coordination

**Use Case:**
- Team chat
- Sharing calendar events
- Daily communication

**Access/Links:** Discord platform

**Recommended For:** All departments

**Current Users:** All team members

**Notes:** Used for sharing calendar events and team coordination

**Integration with Stack:** Part of communication stack

### Dropbox

**Type:** File Storage

**Category:** Digital Tools

**Purpose:** File storage and synchronization

**Use Case:**
- Storing employee data
- CRM exports
- Library files
- Data synchronization with Library system

**Access/Links:** Dropbox storage

**Recommended For:** All departments

**Current Users:** All team members

**Notes:** 
- Should sync with Library structure
- Main data storage location
- Contains CRM export folders

**Integration with Stack:** Syncs with Library, MCP, Employee profiles

### ElevenLabs

**Type:** AI Tool

**Category:** AI Voice Generation

**Purpose:** Voice generation and design for videos, tutorials, presentations

**Use Case:**
- Voice design for videos
- Narrating tutorials
- Voice presentations
- Academy content
- Client testimonials

**Access/Links:** ElevenLabs platform

**Recommended For:** Video and AI departments

**Current Users:** Referenced in Task Manager data

**Notes:** Mentioned in Task Manager use cases (should be responsibilities)

**Integration with Stack:** Part of video production workflow

---

## 9. TECHNICAL ARCHITECTURE

### RAG (Retrieval-Augmented Generation) System Architecture

**Architecture Layer:**
- Data Layer: Dropbox file structure, Library system, Employee profiles
- Integration & Preprocessing: MCP integration, synchronization scripts
- LLM/AI Services: Claude, Perplexity AI, other AI tools
- Application Layer: Task Manager, Online Academy, CRM interfaces
- Monitoring & Governance: Data quality scripts, usage logging

**Technology Stack:** 
- File-based data storage (Dropbox)
- MCP protocol for AI integration
- Claude for processing
- Synchronization scripts
- Metadata indexing systems

**Architecture Pattern:** 
- Distributed file-based architecture
- Single source of truth principle
- Hierarchical folder structure with top 10 principle
- Metadata-driven navigation

**Key Components:**
1. **Main Folder Manager Script** - Coordinates all folder operations, prevents data duplication
2. **Subfolder Scripts** - Handle local changes within specific folders
3. **Synchronization Engine** - Keeps Dropbox and Library in sync (3-hour intervals)
4. **Metadata Index System** - Enables fast AI navigation and search
5. **Data Quality Monitors** - Small scripts that check content quality

**Integration Points:**
- Dropbox ↔ Library system (bidirectional sync)
- Daily reports → Library taxonomy (automatic updates)
- Daily reports → Employee profiles (automatic task updates)
- MCP → All systems (AI integration layer)

**Legacy Tool Integration:**
- Google Calendar (event sharing)
- Discord (team communication)
- Google Workspace (collaboration)
- Dropbox (file storage)

**Documentation Location:** 
- RAC GitHub (Remote AI Context)
- Library structure documentation
- Data architecture guides

**AI Enhancement:**
- AI-driven data organization
- Automated duplicate detection
- Intelligent data prioritization
- Prompt-based data queries

### Task Manager Architecture

**Architecture Layer:**
- Data Layer: Task definitions, step templates, workflow structures
- Processing Layer: Data parsing, format conversion
- Integration Layer: MCP, tool references
- Application Layer: Task execution interface

**Technology Stack:**
- Markdown (current, may convert to JSON)
- MCP integration
- Tool reference system

**Architecture Pattern:**
- Template-driven task creation
- Workflow → Steps → Actions hierarchy
- Tool assignment per step

**Key Components:**
1. **Task Definitions** - High-level task descriptions
2. **Step Templates** - Reusable step definitions
3. **Workflow Engine** - Combines steps into workflows
4. **Tool Registry** - Maps tools to steps and tasks

**Integration Points:**
- MCP integration (needs proper placement)
- Claude Code integration
- Library system (for tool references)

**Documentation Location:** Task Manager system files, step templates folder

**AI Enhancement:**
- AI-driven workflow generation
- Automatic step creation from descriptions
- Tool suggestion based on step type

---

## 10. DECISIONS LOG

### Decision: Implement Weekly Training Sessions for Developers

**Date:** December 12, 2025

**Context:** Developers lack understanding of data architecture, making it difficult to scale data organization work. Single person (Artemchuk Nikolay) cannot handle all data architecture tasks alone.

**Options Considered:**
1. Continue with single person handling all data work
2. Hire dedicated data architect
3. Train existing developers on data architecture

**Decision Made:** Option 3 - Train existing developers (Kizilova Olha, Danylenko Liliia) through weekly half-day sessions

**Rationale:** 
- Developers already understand code structure and logic
- Data architecture is similar to code architecture (order, frameworks, inheritance)
- Most cost-effective solution
- Builds internal capability
- Enables scaling of data work

**Impact:** 
- Dev department: Time commitment (half day per week per developer)
- AI department: Training delivery (Artemchuk Nikolay)
- Overall: Faster data architecture progress, reduced bottleneck

**Alignment with AI-First Vision:** 
- Enables more team members to work with AI tools effectively
- Builds AI literacy across organization
- Supports data-driven operations

**Follow-up Required:** 
- Schedule first training session
- Prepare training curriculum
- Coordinate calendars

**Documentation:** 
- Training curriculum in RAC
- Data architecture guide
- Onboarding materials

### Decision: Migrate Microservices Data to File-Based Structure

**Date:** December 12, 2025

**Context:** Microservices are developed but cannot be populated with data because data format doesn't match. Manual data entry is too slow and impractical.

**Options Considered:**
1. Continue manual data entry
2. Build data import tools for microservices
3. Migrate data to file-based structure matching microservices needs

**Decision Made:** Option 3 - Migrate to file-based structure in Dropbox

**Rationale:**
- Enables easy editing and consultation
- Can generate content from data or vice versa
- Matches microservices data requirements
- Supports AI-driven data processing
- More flexible than database-only approach

**Impact:**
- Dev department: Data migration work
- All departments: New data access patterns
- Microservices: Can now be populated with data

**Alignment with AI-First Vision:**
- Enables AI to work with data directly
- Supports automated data generation
- Facilitates data-driven decision making

**Follow-up Required:**
- Create data templates
- Plan migration process
- Test with sample data

**Documentation:**
- Microservices data migration guide
- Data template specifications
- Migration process SOP

### Decision: Implement Top 10 Data Organization Principle

**Date:** December 12, 2025

**Context:** AI systems cannot efficiently process folders with 1500+ items. Large folders slow down processing and increase costs.

**Options Considered:**
1. Keep all data in large folders
2. Organize by strict hierarchy only
3. Implement top 10 principle - keep only most relevant items per folder

**Decision Made:** Option 3 - Top 10 principle with metadata navigation

**Rationale:**
- Dramatically improves AI processing speed
- Reduces data consumption
- Enables faster navigation
- Metadata guides AI to relevant subfolders
- Based on "Turkish horde" principle - break large into small groups

**Impact:**
- All departments: Need to prioritize data
- Library system: Restructuring required
- AI processing: Much faster and more efficient

**Alignment with AI-First Vision:**
- Optimizes AI tool usage
- Reduces processing costs
- Improves AI accuracy

**Follow-up Required:**
- Prioritize existing data
- Create metadata indexes
- Update folder structures

**Documentation:**
- Data organization SOP
- Top 10 principle guide
- Metadata indexing standards

### Decision: Use Manual Confirmation for AI Bulk Changes

**Date:** December 12, 2025

**Context:** When using Claude for bulk file changes, auto-confirmation can lead to errors. Need to ensure quality and learn from AI suggestions.

**Options Considered:**
1. Use auto-confirmation for speed
2. Manual review of all changes
3. Manual confirmation with feedback accumulation

**Decision Made:** Option 3 - Manual confirmation, review each change, accumulate feedback

**Rationale:**
- Ensures quality and prevents errors
- Allows learning from AI reasoning
- Builds institutional knowledge
- Creates feedback loop for improvement

**Impact:**
- All departments using AI: Slightly slower but higher quality
- AI department: Better prompt development
- Overall: Improved AI collaboration

**Alignment with AI-First Vision:**
- Human-in-the-loop approach
- Continuous improvement
- Quality over speed

**Follow-up Required:**
- Document feedback patterns
- Update prompts based on feedback
- Share learnings across team

**Documentation:**
- AI collaboration SOP
- Feedback accumulation process
- Prompt improvement guidelines

---

## 11. DOCUMENTATION & KNOWLEDGE GAPS

### RAG System Architecture Guide

**Type:** Technical Doc

**Purpose:** Comprehensive guide on how to structure data for RAG (Retrieval-Augmented Generation) systems, including principles, best practices, and examples

**Target Audience:** Dev department, AI department, all data workers

**Current Status:** Missing

**Location(s):** RAC GitHub, Library documentation folder

**Owner:** Artemchuk Nikolay (ID: 37226) - AI Department (with Kizilova Olha input)

**Priority:** Critical

**Template Format:** Technical documentation with examples

**Language Needs:** English (primary), Russian/Ukrainian for team reference

### Task Manager Data Structure Documentation

**Type:** Technical Doc

**Purpose:** Document Task Manager data structure - how tasks, steps, workflows, and templates are organized and related

**Target Audience:** Dev department, AI department

**Current Status:** Missing

**Location(s):** Task Manager system files, RAC GitHub

**Owner:** Kizilova Olha (ID: 178) - Dev Department

**Priority:** High

**Template Format:** Technical documentation with data schema

**Language Needs:** English

### Data Organization SOP

**Type:** Process Doc

**Purpose:** Standard operating procedure for organizing data according to RAG principles - top 10 principle, deduplication, metadata creation

**Target Audience:** All departments

**Current Status:** Missing

**Location(s):** RAC GitHub, Process documentation

**Owner:** Artemchuk Nikolay (ID: 37226) - AI Department

**Priority:** Critical

**Template Format:** SOP template with step-by-step instructions

**Language Needs:** English (primary), multilingual support

### Employee Profile Automation Workflow

**Type:** Process Doc

**Purpose:** Document how employee profiles are automatically updated from daily reports, tasks, and library skills

**Target Audience:** Dev department, HR department

**Current Status:** Missing

**Location(s):** RAC GitHub, Employee system documentation

**Owner:** Kizilova Olha (ID: 178) - Dev Department

**Priority:** High

**Template Format:** Workflow documentation with MCP integration details

**Language Needs:** English

### Prompt Engineering SOP

**Type:** Process Doc

**Purpose:** Standard operating procedure for prompt engineering, including reversal prompting technique and prompt organization

**Target Audience:** AI department, Dev department

**Current Status:** Missing

**Location(s):** RAC GitHub, Prompts folder

**Owner:** Artemchuk Nikolay (ID: 37226) - AI Department

**Priority:** High

**Template Format:** SOP template with examples

**Language Needs:** English

### Data Architecture Training Curriculum

**Type:** Guide

**Purpose:** Step-by-step training curriculum for teaching developers data architecture principles, RAG systems, and file organization

**Target Audience:** Dev department (training material)

**Current Status:** Missing

**Location(s):** RAC GitHub, Training materials folder

**Owner:** Artemchuk Nikolay (ID: 37226) - AI Department

**Priority:** High

**Template Format:** Training guide with lessons and exercises

**Language Needs:** English (primary), Russian/Ukrainian for team

### Microservices Data Migration Guide

**Type:** Technical Doc

**Purpose:** Guide for migrating microservices data to file-based structure, including templates, formats, and migration process

**Target Audience:** Dev department

**Current Status:** Missing

**Location(s):** RAC GitHub, Microservices documentation

**Owner:** Kizilova Olha (ID: 178) - Dev Department

**Priority:** High

**Template Format:** Technical documentation with migration steps

**Language Needs:** English

### Online Academy Update Workflow

**Type:** Process Doc

**Purpose:** Document workflow for updating Online Academy courses using Perplexity AI and Lips database synchronization

**Target Audience:** Dev department, Content creators

**Current Status:** Missing

**Location(s):** RAC GitHub, Online Academy documentation

**Owner:** Kizilova Olha (ID: 178) - Dev Department

**Priority:** Medium

**Template Format:** Workflow documentation

**Language Needs:** English

### AI Collaboration SOP

**Type:** Process Doc

**Purpose:** Standard operating procedure for collaborating with AI tools - manual confirmation, feedback accumulation, quality assurance

**Target Audience:** All departments using AI tools

**Current Status:** Missing

**Location(s):** RAC GitHub, AI tools documentation

**Owner:** Artemchuk Nikolay (ID: 37226) - AI Department

**Priority:** High

**Template Format:** SOP template with best practices

**Language Needs:** English

### Data Synchronization SOP

**Type:** Process Doc

**Purpose:** Document how Dropbox and Library systems stay synchronized, including scripts, schedules, and conflict resolution

**Target Audience:** Dev department, System administrators

**Current Status:** Missing

**Location(s):** RAC GitHub, System documentation

**Owner:** Kizilova Olha (ID: 178) - Dev Department

**Priority:** High

**Template Format:** Technical documentation with scripts

**Language Needs:** English

---

## 12. COMMUNICATION & ANNOUNCEMENTS

### Weekly Training Sessions Announcement

**What:** Announcement of weekly half-day training sessions for developers on data architecture and file systems

**To Whom:** Dev department (Kizilova Olha, Danylenko Liliia), potentially other departments later

**Channel:** Discord, Email, Team meeting

**Message Type:** Initial announcement

**Timing:** Before first session (next week)

**Owner:** Artemchuk Nikolay (ID: 37226) - AI Department

**Language:** Russian/Ukrainian (primary), English for documentation

**Follow-up Plan:** 
- Send calendar invites
- Prepare training materials
- Schedule first session

**Documentation Link:** Training curriculum (to be created)

### Data Architecture Changes Announcement

**What:** Announcement of new data organization principles (top 10, deduplication, RAG optimization) and impact on daily work

**To Whom:** All departments

**Channel:** All-hands meeting, Discord, Documentation

**Message Type:** Training/Onboarding

**Timing:** After training sessions begin

**Owner:** Artemchuk Nikolay (ID: 37226) - AI Department

**Language:** Multilingual (Russian/Ukrainian/English)

**Follow-up Plan:**
- Provide documentation
- Answer questions
- Monitor adoption

**Documentation Link:** Data Organization SOP (to be created)

### Task Manager Restructuring Update

**What:** Update on Task Manager data parsing and restructuring progress

**To Whom:** Dev department, AI department

**Channel:** Discord, Status update

**Message Type:** Progress update

**Timing:** As work progresses

**Owner:** Kizilova Olha (ID: 178) - Dev Department

**Language:** English (technical), Russian/Ukrainian for team

**Follow-up Plan:** Regular updates on progress

**Documentation Link:** Task Manager documentation (to be created)

---

## 13. BLOCKERS & DEPENDENCIES

### Blocker: Lack of Data Architecture Understanding

**Description:** Developers cannot effectively help with data organization because they don't understand data architecture principles, RAG systems, or file organization strategies.

**Impact:** 
- Cannot proceed with data cleanup without training
- Single person bottleneck (Artemchuk Nikolay)
- Slow progress on critical data architecture work

**Waiting On:** 
- Training sessions to begin (Artemchuk Nikolay to schedule)
- Training curriculum to be prepared

**Resolution Path:** 
- Implement weekly training sessions
- Gradually build understanding
- Provide hands-on practice

**Priority:** Critical

**Escalation Needed:** No - solution identified (training sessions)

**Alternative Solutions:** 
- Continue with single person (not scalable)
- Hire external data architect (expensive, slower)

### Blocker: Task Manager Data Needs Parsing Before Use

**Description:** Task Manager contains unstructured data that needs parsing before it can be properly used - use cases vs responsibilities, tasks vs steps confusion.

**Impact:**
- Cannot use Task Manager effectively
- Workflows cannot be generated
- Step templates are missing

**Waiting On:**
- Kizilova Olha to begin parsing work
- Understanding of correct data structure

**Resolution Path:**
- Parse Task Manager data
- Separate tasks from steps
- Convert use cases to responsibilities
- Recreate missing templates

**Priority:** High

**Escalation Needed:** No

**Alternative Solutions:** 
- Manual recreation (time-consuming)
- AI-assisted parsing (preferred approach)

### Blocker: Employee Profile Data Structure Unknown

**Description:** Employee unit template is 400 lines but structure and which fields can be auto-filled is not yet understood.

**Impact:**
- Cannot automate profile updates
- Don't know what data to collect
- Manual entry remains necessary

**Waiting On:**
- Analysis of employee unit template
- Understanding of field purposes
- Identification of auto-fillable fields

**Resolution Path:**
- Analyze template structure
- Document all fields
- Identify automation opportunities
- Create data collection plan

**Priority:** High

**Escalation Needed:** No

**Alternative Solutions:** 
- Manual analysis (time-consuming)
- AI-assisted analysis (preferred)

### Blocker: Library Actions File Has Duplicates

**Description:** Library actions file contains processes and results that are duplicated 3 times (exist in separate Process folder), causing excessive data consumption.

**Impact:**
- AI cannot efficiently process files
- Wasted storage and processing resources
- Confusion about data location

**Waiting On:**
- Kizilova Olha to remove duplicates
- Confirmation of what to keep vs remove

**Resolution Path:**
- Remove processes and results from library actions
- Keep only in Process folder
- Verify no data loss

**Priority:** Critical

**Escalation Needed:** No

**Alternative Solutions:** None - must remove duplicates

---

## 14. KEY INSIGHTS & LESSONS

### Insight: Data Architecture is Like Code Architecture

**Insight:** Understanding data architecture requires similar skills to understanding code architecture - order, frameworks, inheritance, logic. Developers already have these skills and can learn data architecture.

**Context:** Discussion about why developers are best candidates for data architecture work, despite current lack of understanding.

**Application:** 
- Use code architecture analogies when teaching data architecture
- Leverage developers' existing skills
- Build on familiar concepts (order, structure, logic)

**Related Concepts:** 
- Code structure (files, folders, modules)
- Data structure (files, folders, metadata)
- Both require organization and hierarchy

**Impact on Operations:** 
- Enables training developers instead of hiring specialists
- Faster skill development
- Better integration of data and code work

**Template/SOP Update:** Should be included in data architecture training curriculum

**Department Relevance:** Dev department (primary), AI department (training delivery)

### Insight: Small Scripts Monitor Quality Better Than Large Files

**Insight:** For RAG systems, many small scripts that monitor content quality work better than large files that consume excessive resources. AI cannot efficiently process massive files.

**Context:** Discussion about RAG system architecture and why data needs to be organized in small, focused files.

**Application:**
- Break large files into smaller, focused files
- Create monitoring scripts for each data type
- Keep individual files small and manageable
- Use metadata to connect related files

**Related Concepts:**
- Microservices architecture (small, focused services)
- Single responsibility principle
- Modular design

**Impact on Operations:**
- Faster AI processing
- Lower costs
- Better data quality
- Easier maintenance

**Template/SOP Update:** Should be part of RAG system architecture guide

**Department Relevance:** All departments (data organization affects all)

### Insight: Top 10 Principle Enables Efficient AI Processing

**Insight:** Keeping only top 10 most relevant items per folder (instead of 1500) dramatically improves AI processing speed and accuracy. Metadata guides AI to relevant subfolders when needed.

**Context:** Discussion about "Turkish horde" principle - breaking large territories into small groups of 10 for efficient management.

**Application:**
- Prioritize data by usage frequency
- Log tool usage to determine top items
- Keep only top 10 per folder
- Use metadata for navigation to subfolders
- Apply to all data organization

**Related Concepts:**
- Pareto principle (80/20 rule)
- Information architecture
- Search optimization

**Impact on Operations:**
- Much faster AI processing
- Reduced data consumption
- Better search results
- Lower costs

**Template/SOP Update:** Should be core principle in Data Organization SOP

**Department Relevance:** All departments

### Insight: Reversal Prompting Creates Reusable Knowledge

**Insight:** After completing a task, asking AI to rewrite the original prompt with improvements creates optimized, reusable prompts. These should be organized and indexed for easy discovery.

**Context:** Discussion about reversal prompting technique and need to organize prompts for easy access.

**Application:**
- Always request reversal after task completion
- Save optimized prompts with metadata
- Organize by use case and process type
- Create searchable index
- Enable "find prompt for X" queries

**Related Concepts:**
- Continuous improvement
- Knowledge management
- Prompt engineering best practices

**Impact on Operations:**
- Faster prompt creation
- Better prompt quality
- Reusable prompt library
- Reduced prompt development time

**Template/SOP Update:** Should be part of Prompt Engineering SOP

**Department Relevance:** AI department (primary), Dev department (users)

### Insight: Manual Confirmation Builds Institutional Knowledge

**Insight:** Using manual confirmation for AI bulk changes (instead of auto-confirmation) ensures quality, allows learning from AI reasoning, and builds institutional knowledge through feedback accumulation.

**Context:** Discussion about Claude usage - importance of reviewing plans, confirming changes, reading AI reasoning.

**Application:**
- Always review AI plans before execution
- Confirm each change individually
- Read and understand AI reasoning
- Document feedback for future improvements
- Accumulate learnings over time

**Related Concepts:**
- Human-in-the-loop AI
- Quality assurance
- Continuous learning
- Feedback loops

**Impact on Operations:**
- Higher quality outputs
- Better AI collaboration
- Improved prompts over time
- Reduced errors

**Template/SOP Update:** Should be part of AI Collaboration SOP

**Department Relevance:** All departments using AI tools

### Insight: File-Based Data Enables AI Processing

**Insight:** Migrating microservices data to file-based structure (instead of database-only) enables AI to work with data directly, supports automated generation, and allows easy editing and consultation.

**Context:** Discussion about why microservices cannot be populated - data format mismatch, need for file-based structure.

**Application:**
- Use file-based data structures
- Enable AI to read and write data files
- Support both human and AI editing
- Generate content from data or vice versa
- Match data format to AI capabilities

**Related Concepts:**
- Data format optimization
- AI-friendly data structures
- Human-AI collaboration

**Impact on Operations:**
- Enables AI-driven data processing
- Faster data population
- More flexible data access
- Supports automation

**Template/SOP Update:** Should be part of Microservices data migration guide

**Department Relevance:** Dev department (primary), all departments (data users)

---

## 15. ANALOGIES & FRAMEWORKS

### Analogy: Turkish Horde Territory Management

**Analogy:** Turkish horde captured huge territories by breaking into groups of 10 people - each group managed a small area efficiently, rather than trying to manage everything at once.

**Explanation:** When organizing data for AI processing, break large folders (1500 items) into smaller groups (top 10 items) for efficient management and processing.

**Application:** 
- Apply to all data organization
- Keep top 10 items per folder
- Use metadata to navigate to subfolders when needed
- Prevents AI from being overwhelmed

**Relevance to Remote Helpers:** 
- Directly applicable to library organization
- Enables efficient AI processing
- Reduces data consumption
- Improves search accuracy

**Training Potential:** 
- Good analogy for explaining top 10 principle
- Visual and memorable
- Can be used in data architecture training

### Framework: Data Architecture = Code Architecture

**Framework:** Data architecture follows same principles as code architecture - order, structure, frameworks, inheritance, logic, organization.

**Explanation:** Developers already understand code structure, so they can learn data structure using similar mental models and principles.

**Application:**
- Use code architecture concepts when teaching data architecture
- Leverage developers' existing skills
- Build on familiar patterns
- Apply software engineering principles to data

**Relevance to Remote Helpers:**
- Enables training developers instead of hiring specialists
- Faster skill development
- Better integration of development and data work

**Training Potential:**
- Core framework for data architecture training
- Helps developers understand data work
- Bridges code and data understanding

---

## 16. EMPLOYEE & TEAM CONTEXT

### Employee Mentions

**Name:** Kizilova Olha (ID: 178)
**Department:** Dev
**Role:** Backend Developer
**Context:** 
- Primary developer working on Task Manager and data architecture
- Discussing Task Manager structure and data parsing needs
- Will receive training on data architecture
- Assigned multiple data organization tasks

**Action Items:** 
- Parse Task Manager data
- Remove duplicates from library actions
- Analyze employee profile structure
- Create account templates
- Fix microservices references

**Skills/Tools Mentioned:** 
- Backend development
- Data parsing
- Task Manager system
- MCP integration

**Development Needs:** 
- Data architecture understanding
- RAG system principles
- File organization strategies

### Employee Mentions

**Name:** Danylenko Liliia (ID: 72754)
**Department:** Dev
**Role:** Frontend/Full-Stack Developer
**Context:** 
- Has calendar event at 11:00 Ukraine time
- Experiencing electricity issues (battery power only)
- Needs to share calendar event with team
- Will receive training on data architecture

**Action Items:** 
- Share calendar event with Kizilova Olha, Admin, Discord
- Attend weekly training sessions

**Skills/Tools Mentioned:** 
- Frontend/Full-Stack development
- Google Calendar
- Discord

**Development Needs:** 
- Data architecture understanding
- RAG system principles

### Employee Mentions

**Name:** Zasiadko Matvii (ID: 86981)
**Department:** AI
**Role:** Prompt engineer
**Context:** 
- Mentioned as "Коля" helping with preparation
- Spent half day yesterday preparing meeting topics
- Will assist with training sessions

**Action Items:** 
- Assist with training delivery
- Help with data architecture work

**Skills/Tools Mentioned:** 
- Prompt engineering
- Meeting preparation

**Development Needs:** None specified

### Employee Mentions

**Name:** Perederii Vladislav (ID: 86246)
**Department:** AI
**Role:** Prompt engineer
**Context:** 
- Previously asked to transcribe videos and break them into pieces
- Work was supposed to include N8N automation step-by-step
- Work was not completed as requested
- Artemchuk Nikolay is now doing this work himself

**Action Items:** None (historical context)

**Skills/Tools Mentioned:** 
- Video transcription
- N8N automation

**Development Needs:** 
- Follow-through on assigned tasks
- Communication about task status

### Employee Mentions

**Name:** Skrypkar Vilhelm (ID: 333)
**Department:** Design
**Role:** Illustrator, Graphic Designer
**Context:** 
- Mentioned as "Вильгельм" - artist who drew pictures/portraits
- Referenced in employee profile data structure discussion
- Employee profile has "employee artist" field

**Action Items:** None

**Skills/Tools Mentioned:** 
- Illustration
- Graphic design
- Portrait creation

**Development Needs:** None specified

### Team Dynamics

- **Cross-Department Collaboration:** Strong collaboration between AI (Artemchuk Nikolay) and Dev (Kizilova Olha, Danylenko Liliia) departments on data architecture
- **Training Commitment:** Team committed to weekly half-day training sessions to build data architecture skills
- **Resource Constraints:** Single person (Artemchuk Nikolay) handling too much work, needs team support
- **Communication:** Using Discord and Google Calendar for coordination
- **Workload Distribution:** Need to distribute data architecture work across team members

---

## 17. LEAD GENERATION & SALES CONTEXT

*Not applicable to this call*

---

## 18. DESIGN & CREATIVE CONTEXT

*Limited applicability - Skrypkar Vilhelm mentioned in employee data context only*

---

## 19. DEVELOPMENT & TECHNICAL CONTEXT

### Development Work

**Project Type:** Backend, Full-Stack, Infrastructure

**Technologies:** 
- Task Manager system
- MCP (Model Context Protocol)
- Markdown (may convert to JSON)
- Dropbox API
- Synchronization scripts
- Metadata indexing
- RAG systems

**Development Stage:** 
- Planning: Data architecture design
- Development: Task Manager parsing, library cleanup
- Testing: Not yet started
- Deployment: Not yet started

**Technical Challenges:**
1. **Data Structure Parsing** - Task Manager data needs parsing and restructuring
   - Use cases vs responsibilities confusion
   - Tasks and steps mixed together
   - Missing step templates
2. **Data Deduplication** - Library files contain 3x duplicate data
   - Processes and results duplicated
   - Need to remove from library actions file
3. **Format Conversion** - May need to convert Markdown to JSON
   - Better for AI processing
   - Easier to parse programmatically
4. **Tool Integration** - MCP integration incorrectly placed
   - Needs proper category placement
   - Claude Desktop should be Claude Code
5. **Synchronization** - Dropbox and Library need bidirectional sync
   - 3-hour update schedule
   - Prevent data conflicts
   - Maintain single source of truth

**Code Quality:**
- Need to establish data quality standards
- Create monitoring scripts for content quality
- Implement validation for data structure

**Integration Needs:**
- MCP integration with Library system
- MCP integration with Employee profiles
- Dropbox ↔ Library synchronization
- Daily reports → Library taxonomy
- Daily reports → Employee profiles
- Perplexity AI integration
- Online Academy ↔ Library sync

**DevOps:**
- Synchronization script deployment
- Scheduled tasks (3-hour intervals)
- Data backup and recovery
- Monitoring and logging

**AI Coding Tools:**
- **Claude** - Primary tool for data processing, bulk changes, prompt engineering
- **Claude Code** - Code-focused interface (replacing Claude Desktop)
- **MCP** - Integration protocol for AI tools
- **Perplexity AI** - Research and content updates (to be added)

**AI Development Tools:**
- Claude (data processing)
- MCP (integration)
- Task Manager (workflow management)
- Composer (code search/replace)

---

## 20. ONBOARDING & TRAINING CONTEXT

### Onboarding Program

**Program Level:** Foundation / Advanced (for existing developers)

**Training Topics:**
- **Data Architecture Fundamentals:**
  - RAG system principles
  - File organization strategies
  - Data deduplication
  - Metadata creation
- **Tool Usage:**
  - Claude for data processing
  - MCP integration
  - Task Manager system
  - Library structure navigation
- **Best Practices:**
  - Top 10 principle
  - Manual confirmation workflow
  - Reversal prompting
  - Data quality monitoring

**Tools Setup:**
- Claude (already have)
- Claude Code (to be set up)
- MCP integration (to be configured)
- Task Manager access
- Library system access
- Dropbox access

**Documentation Needs:**
- RAG system architecture guide
- Data organization SOP
- Task Manager documentation
- Prompt engineering guide
- AI collaboration SOP

**Video Tutorials:**
- 7 transcribed videos available explaining processes
- Starting from extension installation
- How to connect new tools
- Step-by-step automation guides

**Language Considerations:**
- Training in Russian/Ukrainian (primary)
- Documentation in English
- Multilingual support needed

**Memory Techniques:**
- Incremental learning (one concept at a time)
- Hands-on practice
- Real-world examples
- Gradual complexity building

**Progress Tracking:**
- Weekly half-day sessions
- Practical assignments
- Feedback and improvement
- Gradual skill building

---

## 21. FOLLOW-UP ITEMS

### Scheduled Meetings

- **Weekly Training Sessions** - Half-day per week for each developer (Kizilova Olha, Danylenko Liliia)
  - Participants: Artemchuk Nikolay (trainer), Kizilova Olha, Danylenko Liliia, Zasiadko Matvii (assistant)
  - Departments: AI (training), Dev (learning)
  - Frequency: Weekly, starting next week
  - Duration: Half day (4 hours)
  - Focus: Data architecture, file systems, library organization

- **Calendar Event Coordination** - Danylenko Liliia's event at 11:00 Ukraine time
  - Participants: Danylenko Liliia, Kizilova Olha, Admin, Discord team
  - Departments: Dev
  - Topic: Electricity outage notification
  - Action: Share calendar event

### Reviews Needed

- **Task Manager Data Structure** - Review parsed and restructured Task Manager data
  - Reviewer: Artemchuk Nikolay (ID: 37226) - AI Department
  - Timeline: After parsing completion
  - Purpose: Verify correct structure, validate changes

- **Library Actions File Cleanup** - Review after duplicate removal
  - Reviewer: Artemchuk Nikolay (ID: 37226) - AI Department
  - Timeline: After cleanup
  - Purpose: Verify no data loss, confirm structure

- **Employee Profile Template Analysis** - Review analysis of 400-line template
  - Reviewer: Artemchuk Nikolay (ID: 37226) - AI Department
  - Timeline: After analysis completion
  - Purpose: Validate field identification, confirm automation opportunities

### Reports Due

- **Task Manager Parsing Progress** - Status update on data parsing
  - To: Artemchuk Nikolay (ID: 37226) - AI Department
  - From: Kizilova Olha (ID: 178) - Dev Department
  - Format: Status update
  - Channel: Discord
  - Timeline: As work progresses

- **Training Session Feedback** - Feedback from first training session
  - To: Artemchuk Nikolay (ID: 37226) - AI Department
  - From: Kizilova Olha (ID: 178), Danylenko Liliia (ID: 72754) - Dev Department
  - Format: Written feedback
  - Channel: Discord or email
  - Timeline: After first session

### Template Updates

- **Task Templates** - Create/update based on identified action items
  - Parse data + Sort structure
  - Remove duplicates + Clean data
  - Convert format + Evaluate structure
  - Analyze structure + Document fields
  - Create template + Standardize data
  - Schedule sessions + Coordinate calendars

- **Step Templates** - Recreate missing step templates from Task Manager
  - Based on parsed Task Manager data
  - Follow step template structure (Name, Tool, Responsibility)
  - Organize by workflow

- **Checklist Items** - Create checklists for data organization tasks
  - Data deduplication checklist
  - File organization checklist
  - Metadata creation checklist

### RAC Documentation

- **RAG System Architecture Guide** - Add comprehensive guide to RAC
- **Data Organization SOP** - Add standard operating procedure
- **Task Manager Documentation** - Add data structure documentation
- **Prompt Engineering SOP** - Add reversal prompting and organization guide
- **AI Collaboration SOP** - Add manual confirmation and feedback process
- **Employee Profile Automation Workflow** - Add workflow documentation
- **Microservices Data Migration Guide** - Add migration process
- **Data Architecture Training Curriculum** - Add training materials
- **Data Synchronization SOP** - Add synchronization process
- **Online Academy Update Workflow** - Add update process

---

*End of Document*

