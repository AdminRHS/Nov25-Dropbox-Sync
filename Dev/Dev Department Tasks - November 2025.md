# Dev Department Tasks - November 2025

**Department:** Dev Nov25
**Document Type:** Department-Wide Task Consolidation
**Date Range:** November 1-30, 2025
**Source:** November 4, 2025 Admin Call - Processed Transcript, Daily files Nov 4-11, 2025, November 12, 2025 Dev Call
**Last Updated:** November 12, 2025

---

## Executive Summary

The Dev department is leading critical backend development for Remote Helpers' CRM migration, OpenAI GPT Assistants integration, and microservices architecture. The team is prioritizing database structure and backend logic over frontend UI, following the philosophy that AI tools can generate interfaces once the backend is solid.

**Key Initiatives:**
- **CRM Migration:** Talents module in testing phase, progressive old CRM deprecation
- **OpenAI GPT Assistants:** HR automation workflows (BLOCKED - awaiting $5-20 API budget)
- **Database Development:** Task Manager structure, backend-first approach
- **Microservices Architecture:** Documentation of development process for replication

**Critical Blocker:** OpenAI API budget approval ($5-20) required to test and deploy GPT Assistants chain for HR automation.

**Development Philosophy:** Focus on backend/database first. AI tools can generate interfaces if backend is solid. Database design is more critical for long-term scalability.

**Team Members:** Kizilova Olha (Backend Lead), Klimenko Yaroslav, Danylenko Liliia

---

## By Priority Level

### CRITICAL (Immediate - 1-2 days)

*No critical priority tasks assigned to Dev department at this time. Critical items are focused on AI and LG departments.*

### HIGH (This Week)

#### 1. Extract & Migrate Notes from Old CRM
- **Owners:** Kizilova Olha (Backend Developer - Technical), Rekonvald Viktoriia (HR - Requirements)
- **Department:** Dev, HR
- **Profession:** Backend Developer, Recruiter
- **Timeline:** Near term
- **Status:** Not Started
- **Dependencies:** None
- **Related Project:** CRM Migration, Recruitment Platform
- **Tools:** Database migration scripts, data transformation

**Context:** Critical data migration from old CRM to new system. Need to migrate admin notes, HR notes, and communication history. Solution: AI-powered resume cleaning (remove HTML, images), parsing to auto-fill incomplete fields. Single consolidated "Notes" field proposed for archive with section headers.

**Steps:**
1. Coordinate with Rekonvald Viktoriia on notes field structure requirements
2. Design database schema for consolidated Notes field
3. Review all existing notes in old CRM to understand data format
4. Create data transformation scripts for migration
5. Develop AI-powered resume cleaning functionality (remove HTML/images)
6. Implement parsing logic to auto-fill incomplete fields
7. Test migration on sample dataset
8. Validate data integrity after migration
9. Coordinate full migration execution with HR

---

#### 2. Fix & Optimize OpenAI GPT Assistants Chain
- **Owners:** Kizilova Olha (Backend Developer - Technical), Rekonvald Viktoriia (HR - Testing)
- **Department:** Dev, HR
- **Profession:** Backend Developer, Recruiter
- **Timeline:** When budget allows for testing ($5-20 needed)
- **Status:** **BLOCKED** - Awaiting API Budget Allocation from Pasichna Anastasiia
- **Dependencies:** OpenAI API credits
- **Related Project:** CRM, Recruitment Platform
- **Tools:** OpenAI Platform, CRM backend, API integration

**Workflow:** Job Request → Job Template → Post Template → Job Post

**Context:** Implementing AI-powered HR automation using OpenAI GPT Assistants chain. Currently blocked due to lack of API credits for testing. Issues identified: translation functionality problems, billing/API credit preventing validation. Investment is minimal ($5-20) compared to potential time savings for HR recruitment workflows.

**Steps:**
1. Wait for API budget approval ($5-20) from Pasichna Anastasiia
2. Set up OpenAI API integration in CRM backend
3. Implement GPT Assistants chain workflow
4. Debug translation functionality issues
5. Test complete workflow with Rekonvald Viktoriia: Job Request → Template → Post Template → Full Post
6. Optimize API calls for cost efficiency
7. Document workflow for future maintenance
8. Train HR team on using the automated system

---

#### 3. Review & Update Employee User Access Statuses
- **Owners:** Kizilova Olha (Backend Developer - Technical Linking), Rekonvald Viktoriia (HR - Review)
- **Department:** Dev, HR
- **Profession:** Backend Developer, Recruiter
- **Timeline:** Near term
- **Status:** Waiting - Technical Implementation Needed
- **Dependencies:** Talents-Users integration development
- **Related Project:** CRM, User Management
- **Tools:** CRM user management, access control systems

**Context:** Implementing individual login requirements rather than shared admin accounts for accountability and audit trails. Personal logins enable proper user management, status tracking, prevent system contamination. User system needs integration with Talents module.

**Steps:**
1. Develop Talents-Users integration for linking employee records with user accounts
2. Design database schema for user access management
3. Implement personal login authentication system
4. Create access control logic (role-based permissions)
5. Build employee status management (active/inactive/former)
6. Coordinate with Rekonvald Viktoriia on reviewing current employee list
7. Migrate users from shared accounts to personal logins
8. Test access control and audit trail functionality
9. Document user management procedures

---

### MEDIUM (Near Term - 1-2 weeks)

#### 4. Resume Parser for Talents - Edit Mode Development
- **Owner:** Danylenko Liliia
- **Priority:** MEDIUM
- **Status:** In Progress
- **Timeline:** Ongoing
- **Related Project:** CRM, Talents Module

**Context:** Resume Parser currently works only in CREATE mode. Need to add validation for EDIT mode to prevent data overwriting while enabling parser functionality.

**Steps:**
1. Review current implementation (create mode only)
2. Analyze data overwriting risks in edit mode
3. Design validation logic to prevent data loss
4. Implement check for existing data
5. Send existing data to AI for comparison
6. Prevent overwriting of already-filled fields
7. Test with various scenarios (empty fields, partial data, full data)
8. Make decision: enable button for all modes or keep create-only

**Current Implementation:**
- Resume Parser button displayed only in CREATE mode
- Hidden in EDIT mode to prevent accidental data overwriting
- Logic: `if (mode === 'create') { show button }`

**Decision Point:**
- Currently: Button only in CREATE mode (safer, prevents data loss)
- Future consideration: Add smart validation for EDIT mode

---

#### 5. MCP Hub - Develop and Review Architecture and Timeline for Centralized Systems
- **Owner:** Danylenko Liliia, Dev Team
- **Priority:** MEDIUM
- **Status:** In Progress
- **Timeline:** Ongoing
- **Related Project:** MCP Integration, Centralized Systems

**Context:** From November 12 call - Need to develop centralized MCP Hub system for managing MCP servers. Architecture review needed.

**Steps:**
1. Review current MCP implementation in Talents
2. Design centralized MCP Hub architecture
3. Plan unified interface for connecting and managing MCP servers
4. Set up HTTP/HTTPS transport (StreamableHTTPServerTransport)
5. Configure additional transport for extended functionality
6. Create unified management interface
7. Document architecture and timeline
8. Review with team

---

#### 6. Process Video Transcriptions for Knowledge System Integration
- **Owner:** Dev Team (each developer)
- **Priority:** MEDIUM
- **Status:** Not Started
- **Timeline:** Ongoing (1 hour per day scheduled)
- **Related Project:** Knowledge Management, Video Processing

**Context:** From November 12 call - Each developer should process videos related to their work topics (e.g., MCP, development tools) and integrate transcriptions into knowledge system. TurboScribe available on Admin account for hour-long videos.

**Steps:**
1. Each developer schedules 1 hour per day for this work
2. Find videos related to development topics (MCP, tools, etc.)
3. Transcribe videos using TurboScribe (Admin account) or Google AI Studio
4. Process transcriptions through Perplexity with custom instructions
5. Extract taxonomy elements and map to library structure
6. Organize documentation in personal folders
7. Update knowledge system with new terminology and processes
8. Follow video transcription workflow (instructions in Design department)
9. Access prompts: Taxonomy → Libraries → Prompts → Video Transcription

---

#### 7. Optimize Image Sizes for Honeystone Landing Page
- **Owner:** Kizilova Olha
- **Priority:** MEDIUM
- **Status:** Not Started
- **Timeline:** ASAP
- **Related Project:** Honeystone Landing Page

**Context:** From November 12 call - Developer feedback: background images are 13-14 MB each, need optimization to ~500 KB.

**Steps:**
1. Review Honeystone project images in Taxonomia folder
2. Identify all background images that are too large
3. Optimize images to ~500 KB each
4. Maintain visual quality while reducing file size
5. Replace optimized images in project
6. Verify images display correctly after optimization
7. Update project files

---

#### 8. Share Taxonomia Folder for Honeystone Project Collaboration
- **Owner:** Kizilova Olha, Dev Team
- **Priority:** MEDIUM
- **Status:** Completed
- **Timeline:** November 12, 2025
- **Related Project:** Honeystone Landing Page

**Context:** From November 12 call - Taxonomia folder shared with Dev team for collaborative work on Honeystone Landing page.

**Steps:**
1. ✅ Share Taxonomia folder with Dev team
2. ✅ Verify all team members have access (Admin, Dev, DD accounts)
3. ✅ Confirm folder access and collaboration setup

---

#### 9. Develop Short Link System for Prompt Optimization
- **Owner:** Kizilova Olha
- **Department:** Dev
- **Profession:** Backend Developer
- **Timeline:** Future sprint
- **Status:** Not Started - Requirements Gathering
- **Dependencies:** None
- **Related Project:** CRM, Infrastructure
- **Tools:** Backend development environment, database

**Context:** Need for internal URL shortening system to reduce prompt size. Current problem: long Google Drive/Dropbox links consume excessive tokens. Proposed solution: internal short link management with categorization, automatic forwarding, integration with CRM media storage.

**Steps:**
1. Gather requirements from AI team on prompt optimization needs
2. Design short link database schema (URL mapping, categorization, analytics)
3. Implement URL shortening algorithm
4. Create REST API for link creation and retrieval
5. Build automatic forwarding functionality
6. Integrate with CRM media storage system
7. Add categorization and tagging features
8. Implement analytics tracking (click counts, usage patterns)
9. Document API and usage guidelines

---

#### 5. Clean & Parse Resumes in CRM
- **Owner:** Dev team (AI automation task) / AI team collaboration
- **Department:** Dev / AI
- **Profession:** Backend Developer, AI Engineer
- **Timeline:** After notes migration
- **Status:** Not Started
- **Dependencies:** Notes migration completion
- **Related Project:** CRM, Recruitment Platform
- **Tools:** AI parsing tools, HTML cleaning scripts

**Context:** Old CRM contains resumes with HTML formatting, embedded images, and incomplete data fields. Need AI-powered cleaning to remove unnecessary formatting, parse structured data, and auto-fill fields where possible.

**Steps:**
1. Review resume data structure in old CRM
2. Develop HTML cleaning scripts (remove tags, images, formatting)
3. Implement AI parsing to extract structured information (name, skills, experience, education)
4. Create auto-fill logic for incomplete candidate fields
5. Build data validation and quality checks
6. Test parsing accuracy on sample dataset
7. Execute bulk resume cleaning after notes migration
8. Validate cleaned data quality
9. Document parsing methodology for future use

---

#### 6. Document CRM Development Process for Future Microservices
- **Owners:** Kizilova Olha (Developer), Artemchuk Nikolay (PM Documentation)
- **Department:** Dev, AI
- **Profession:** Backend Developer, Project manager
- **Timeline:** Concurrent with Talents completion
- **Status:** In Progress
- **Dependencies:** None
- **Related Project:** CRM, RAC Documentation
- **Tools:** Cursor, documentation templates, file system

**Context:** Critical to capture Talents development process to replicate for subsequent microservices (Accounts, Businesses, Task Manager). Documentation enables consistent development approach and faster future module creation.

**Steps:**
1. Document Talents module development workflow from start to current state
2. Capture key architectural decisions and rationale
3. Record database design patterns and best practices
4. Document testing and QA procedures
5. Create reusable code templates from Talents module
6. Write deployment and migration procedures
7. Add documentation to RAC knowledge base
8. Review with Artemchuk Nikolay for PM perspective
9. Create template for future microservices development

---

## By Employee

### Kizilova Olha (ID: 178) - Backend Developer

**Role:** Backend Lead, CRM Migration Technical Lead

**HIGH Priority Tasks:**
1. Extract & Migrate Notes from Old CRM (with Rekonvald Viktoriia)
2. Fix & Optimize OpenAI GPT Assistants Chain (BLOCKED - with Rekonvald Viktoriia)
3. Review & Update Employee User Access Statuses (with Rekonvald Viktoriia)

**MEDIUM Priority Tasks:**
4. Develop Short Link System for Prompt Optimization
5. Document CRM Development Process (with Artemchuk Nikolay - In Progress)
6. Optimize Image Sizes for Honeystone Landing Page (Nov 12) - Optimize 13-14 MB images to ~500 KB
7. Share Taxonomia Folder for Honeystone Project (Nov 12, Completed) - Folder shared with Dev team

**Workload Assessment:** HIGH - Leading 7 tasks (3 High, 4 Medium), primary technical owner for CRM migration, 1 task blocked awaiting budget. Heavy coordination with HR (Rekonvald Viktoriia) and AI (Artemchuk Nikolay).

**Detailed Task Breakdown:** (Individual task.md file to be created if needed)

---

### Klimenko Yaroslav - Backend Developer

**Role:** Dev team member, supporting CRM development

**Potential Task Assignments:**
- Clean & Parse Resumes in CRM (Medium - Dev team collective task)
- Support CRM Migration (High - supporting Kizilova)
- Short Link System Development (Medium - supporting Kizilova)

**Status:** Available for task assignment from collective Dev team tasks

---

### Danylenko Liliia - Backend Developer

**Role:** Dev team member, Full Stack Developer, supporting CRM development

**HIGH Priority Tasks:**
1. Resume Parser for Talents - Edit Mode Development (In Progress) - Add validation for edit mode

**MEDIUM Priority Tasks:**
2. MCP Hub - Develop and Review Architecture and Timeline (In Progress) - Centralized MCP system
3. MCP Integration in Talents (Completed) - Full MCP integration with API token authentication
4. Video Creation for Claude Code Tutorial (In Progress) - Generate tutorial videos
5. Table Parsing for Excel Export (In Progress) - Export functionality for talent tables
6. Process Video Transcriptions for Knowledge System (Nov 12) - 1 hour/day for video processing
7. Client Landing Page Development (Honeystone) - Multiple completed tasks
8. Excel Export for Talents - Column selection feature (Completed)

**Completed Tasks:**
- Add "reason" field to status change modal
- Resume Parser Edit Mode Validation with Conflict Resolution Dialog
- Toggle Menu Implementation in sidebar
- MCP Integration for Talent Service (production-ready)
- API Token Authentication for MCP
- Talents CRUD routes via API token
- Job Applications CRUD routes via API token
- Client project hosting (Docker deployment)

**Workload Assessment:** HIGH - Active on multiple CRM development tasks, MCP integration, and client projects. Heavy focus on Talents module development and MCP Hub architecture.

---

## Cross-Department Dependencies

### Dependencies on HR Department (Rekonvald Viktoriia, Nealova Evgeniya)
- **CRM Notes Migration:** Requires HR input on field structure and requirements (High)
- **GPT Assistants Testing:** Requires HR testing and feedback on automation workflows (High - Blocked)
- **User Access Review:** Requires HR review of employee statuses and access needs (High)
- **Personal Login Enforcement:** Coordinate with HR on policy enforcement

### Dependencies on Finance/Admin (Pasichna Anastasiia)
- **OpenAI API Budget:** $5-20 approval needed for GPT Assistants testing (BLOCKING High priority task)

### Dependencies on AI Department (Artemchuk Nikolay)
- **CRM Development Documentation:** Collaborative documentation with PM perspective (Medium - In Progress)
- **Short Link Requirements:** Need AI team input on prompt optimization requirements (Medium)
- **Resume Parsing:** May need AI team collaboration on parsing logic (Medium)

### Supports Multiple Departments
- **CRM Migration:** Affects HR (primary), LG, Sales departments
- **User Management:** All departments need proper access control
- **Infrastructure:** Short link system benefits all departments using AI tools

---

## Critical Blockers

### 1. OpenAI API Budget Approval - $5-20
**Impact:** HIGH - Blocking HR automation testing and deployment
**Owner to Resolve:** Pasichna Anastasiia (Finance/Admin)
**Affected Tasks:** Fix & Optimize OpenAI GPT Assistants Chain (High Priority)
**Timeline:** Immediate approval needed
**Affected Departments:** Dev (development blocked), HR (workflow automation delayed)
**Financial Context:** Minimal investment ($5-20) compared to potential time savings for HR recruitment workflows. Previous issue: someone set limit to $200 instead of $20, so proper budget management is critical.
**Workaround:** None - testing cannot proceed without API credits

### 2. CRM Notes Field Structure Approval
**Impact:** MEDIUM - Delaying data migration work
**Owner to Resolve:** Kizilova Olha (Dev) + Rekonvald Viktoriia (HR) coordination
**Affected Tasks:** Extract & Migrate Notes from Old CRM (High Priority)
**Timeline:** Requires coordination meeting for alignment
**Workaround:** Can begin reviewing old CRM notes structure in parallel while awaiting approval

### 3. Talents-Users Integration Development
**Impact:** MEDIUM - Delaying user access management
**Owner to Resolve:** Kizilova Olha (Dev)
**Affected Tasks:** Review & Update Employee User Access Statuses (High Priority)
**Timeline:** Near term development required
**Workaround:** HR can begin manual cleanup of employee statuses while waiting for integration

---

## Department Capacity & Workload

**Total Active Tasks:** 42 tasks (from Nov 4-12 daily files)
**High Priority:** 3 tasks (1 blocked)
**Medium Priority:** 39 tasks (multiple in progress)
**Blocked Tasks:** 1 task (GPT Assistants - awaiting budget)
**In Progress:** Multiple tasks (CRM documentation, Resume Parser, MCP Hub, video processing)
**Completed:** 15+ tasks (MCP integration, Excel export, client projects, etc.)

**Team Capacity:**
- **Kizilova Olha:** Leading 5 tasks (3 High, 2 Medium) - **HIGH** workload, primary technical owner
- **Klimenko Yaroslav:** Available for assignment - **LOW** workload (capacity available)
- **Danylenko Liliia:** Available for assignment - **LOW** workload (capacity available)

**Coordination Requirements:**
- 3 tasks require HR coordination (Rekonvald Viktoriia)
- 1 task requires Finance approval (Pasichna Anastasiia)
- 2 tasks require AI team coordination (Artemchuk Nikolay)
- 1 task is collective Dev team effort (resume parsing)

**Recommendation:** Delegate resume parsing and short link development support to Klimenko and Danylenko to balance workload and accelerate delivery.

---

## Success Metrics

### CRM Migration Progress
- **Current Phase:** Talents module in testing/QA phase with Rekonvald Viktoriia
- **Target:** Complete Talents, begin Accounts module (November), full migration by Q1 2026
- **Migration Path:** Talents → Accounts → Businesses → Task Manager
- **Measurement:** Module completion, bug resolution rate, feature parity with old CRM, user adoption

### Backend Development Quality
- **Current Focus:** Database structure and logic before frontend
- **Target:** Solid backend enabling rapid frontend generation via AI
- **Measurement:** API stability, database performance, scalability metrics, code reusability

### Automation & Integration
- **Current Status:** GPT Assistants designed but untested (Blocked)
- **Target:** HR automation workflows deployed and reducing manual work (December)
- **Measurement:** Workflow completion time, error rates, HR time savings, API cost efficiency

### Documentation & Knowledge Transfer
- **Current Status:** CRM development documentation in progress
- **Target:** Complete Talents documentation, replicate for future microservices
- **Measurement:** Documentation completeness, template reusability, future module development speed

---

## Related Documents

- [Dev Department Guide](./DEPARTMENT_GUIDE.md) - Team capabilities and processes
- [Dev Department README](./DEP_README.md) - Team overview (3 employees)
- [Processed Transcript - November 4](../AI Nov25/Artemchuk Nikolay/04/processed_transcripts_Nov4.md) - Source document
- [CRM Project Documentation](../../) - CRM migration materials
- [Microservices Architecture Documentation](../../) - Future architecture plans
- [RAC Documentation](../../) - Remote AI Context knowledge base

---

## Weekly Schedule Integration

**Dev Department Call Day:** Friday (1-1.5 hours)
**Schedule Status:** To be announced by Artemchuk Nikolay this week
**Purpose:** Bi-weekly check-ins for systematic progress tracking
**Preparation:** Review CRM migration status, blocker resolution, backend development progress

---

## Development Philosophy & Architecture

### Backend-First Approach
Remote Helpers Dev team follows a **backend-first development philosophy:**

**Rationale:**
- AI tools (Claude, Cursor) can generate interfaces if backend is solid
- Database design is more critical for long-term scalability
- Frontend can be rapidly iterated with AI assistance
- Backend changes are more expensive and risky to refactor later

**Benefits:**
- Stronger foundation for rapid scaling
- Faster frontend iterations using AI-generated code
- Better separation of concerns
- Reduced technical debt

### Microservices Architecture
Transitioning from monolithic CRM to microservices:

**Current Module:** Talents (in testing)
**Planned Modules:**
1. Talents (recruitment/employee management) - In Testing
2. Accounts (user accounts and authentication) - Next
3. Businesses (client management) - Future
4. Task Manager (project/task tracking) - Future

**Documentation Strategy:** Capture Talents development process to replicate for subsequent modules. Each module follows same patterns, reducing development time.

### Progressive Migration Strategy
**Approach:** Systematically migrate features from old to new CRM one at a time, then disable old features.

**Benefits:**
- Incremental migration allows thorough testing
- Operations maintain continuity
- Reduces risk of data loss or downtime
- Users adapt gradually to new system

**Current Status:** Talents in testing → Old Talents features will be disabled → Next module begins

---

## Notes & Action Items

### Immediate Actions (Today/Tomorrow):
1. **Follow up with Pasichna Anastasiia** on OpenAI API budget approval ($5-20) - BLOCKING
2. **Schedule coordination meeting with Rekonvald Viktoriia** on CRM notes field structure
3. **Continue Talents module testing** with HR team
4. **Begin Talents-Users integration development** for access management

### This Week:
1. **Resolve CRM notes field structure** and begin migration script development
2. **Continue CRM development documentation** with Artemchuk Nikolay
3. **Test Talents module** thoroughly with Rekonvald Viktoriia, resolve reported bugs
4. **Attend Friday Dev department call** when schedule announced
5. **Delegate tasks** to Klimenko and Danylenko for workload balance

### Next Steps (Near Term - 1-2 weeks):
1. **Test GPT Assistants workflow** once budget approved (immediate after approval)
2. **Execute CRM notes migration** after field structure approved
3. **Complete Talents-Users integration** for access management
4. **Begin requirements gathering** for short link system
5. **Plan Accounts module development** after Talents completion
6. **Resume parsing implementation** after notes migration complete

---

**Document Version:** 1.0
**Department:** Dev Nov25
**Next Review:** November 12, 2025
**Contact:** Kizilova Olha (Backend Lead) | Klimenko Yaroslav | Danylenko Liliia

---

*This document provides department-wide task visibility and coordination for the Dev team. Individual daily tasks and detailed execution steps are maintained in each employee's personal task.md files within their dated folders. The Dev department is leading backend development for CRM migration and microservices architecture, following a backend-first development philosophy that prioritizes database structure and logic for long-term scalability.*
