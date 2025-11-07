# Call Organized Notes - October 24, 2025

## 1. MEETING METADATA

**Date:** October 24, 2025 (Friday)
**Participants:** Oля (Olya), Женя (Zhenya), team members
**Duration:** Not specified
**Main Topics:**
- Talent management system (LibDev/Talents microservice) QA issues
- Job application intake process improvements
- Resume parser development with AI integration
- New employee onboarding system requirements
- Client call with TipCan Solutions

---

## 2. EXECUTIVE SUMMARY

The team conducted a detailed QA review of the new Talents microservice, identifying critical gaps in the job application intake workflow and data field management. Key decisions were made to implement structured issue tracking via Excel for all microservice QA findings, develop an AI-powered resume parser to auto-populate applicant fields, and create a comprehensive new employee onboarding system within the Talents platform. A client call with Alan from TipCan Solutions revealed opportunities for freelance platform improvements and identified needs for notification systems and web generation training.

---

## 3. ACTION ITEMS & TASKS

### Implement Resume/Document Parser
- **Description:** Create parser functionality to automatically extract data from resumes in multiple formats (PDF, DOCX, RTF, images) and auto-populate applicant fields in the job application system
- **Owner/Assignee:** Development team
- **Priority:** Critical
- **Timeline:** Not specified
- **Dependencies:** AI integration capability, field mapping defined
- **Status:** Not Started
- **Related Project:** LibDev Talents Microservice

### Create Clipboard/Buffer Parser
- **Description:** Develop parser for clipboard/buffer that allows copying data from Excel or tables and automatically distributing it across appropriate fields in the system
- **Owner/Assignee:** Development team
- **Priority:** Critical
- **Timeline:** Not specified
- **Dependencies:** Field mapping specification
- **Status:** Not Started
- **Related Project:** LibDev Talents Microservice

### Add Multi-status System for Applications
- **Description:** Implement unique status system for job applications (cannot reuse "new" status across different entities). Add tags or multi-select capability for statuses
- **Owner/Assignee:** Development team
- **Priority:** High
- **Timeline:** Not specified
- **Dependencies:** Status refresh mechanism (page doesn't auto-refresh on status change)
- **Status:** Not Started
- **Related Project:** LibDev Talents Microservice

### Fix Page Refresh Issues
- **Description:** Resolve issue where status updates require full page refresh to display; implement auto-refresh or partial page updates
- **Owner/Assignee:** Development team
- **Priority:** Critical
- **Timeline:** Not specified
- **Dependencies:** None
- **Status:** Not Started
- **Related Project:** LibDev Talents Microservice

### Create New Employee Onboarding System
- **Description:** Develop employee registration/onboarding module within Talents system where new employees can self-register and input required data
- **Owner/Assignee:** Olya (requirements), Development team (implementation)
- **Priority:** High
- **Timeline:** Not specified
- **Dependencies:** Requirements document from Olya, Tango documentation link
- **Status:** Waiting - needs requirements document
- **Related Project:** LibDev Talents - Employee Module

### Create QA Issue Tracking Excel
- **Description:** Zhenya to create and share structured Excel file for logging all Talents microservice QA issues with columns: Page, Screenshot, Critical Level, Issue Description, Comments
- **Owner/Assignee:** Zhenya
- **Priority:** Critical
- **Timeline:** Immediate
- **Dependencies:** None
- **Status:** In Progress
- **Related Project:** LibDev Talents Microservice QA

### Filter Contact Tools by Messenger Types Only
- **Description:** In contact fields, filter tools/options to show only messaging platforms (Telegram, WhatsApp, Viber, Phone, Email, VK) - remove irrelevant tools like Photoshop, Illustrator
- **Owner/Assignee:** Development team
- **Priority:** Medium
- **Timeline:** Not specified
- **Dependencies:** None
- **Status:** Not Started
- **Related Project:** LibDev Talents Microservice

### Implement YouTube Notifications for TipCan
- **Description:** Set up YouTube notification system for TipCan Solutions client
- **Owner/Assignee:** Not specified
- **Priority:** Medium
- **Timeline:** Not specified
- **Dependencies:** Client requirements
- **Status:** Not Started
- **Related Project:** TipCan Solutions

### Implement Email Notifications for New Employees
- **Description:** Create automated email notification system for new employee onboarding/alerts
- **Owner/Assignee:** Development team
- **Priority:** Medium
- **Timeline:** Not specified
- **Dependencies:** New employee system implementation
- **Status:** Not Started
- **Related Project:** TipCan Solutions / Employee Management

### Create Web Generation Training for Marta
- **Description:** Provide video lessons to Marta on SiteBoon AI web generation capabilities and usage
- **Owner/Assignee:** Not specified
- **Priority:** Low
- **Timeline:** Not specified
- **Dependencies:** SiteBoon AI access
- **Status:** Not Started
- **Related Project:** SiteBoon AI Training

---

## 4. PROJECTS & FEATURES

### LibDev Talents Microservice

**Status:** In Development / QA Phase

**Description:** Talent management and job application tracking system for managing candidates, employees, and recruitment workflows

**Key Features:**
- Job application intake and management
- Resume/candidate data tracking
- Contact information management
- Status tracking for applications
- Employee onboarding module

**Current Issues:**
- Page refresh required after status updates
- No automated data parsing from resumes or clipboard
- Status system needs restructuring (unique statuses per entity type)
- Contact field tools not filtered properly (showing irrelevant options)
- Missing search functionality
- Missing reporting/analytics capabilities
- No structured QA issue tracking system

**Next Steps:**
1. Create structured QA issue log (Excel)
2. Prioritize critical issues: search, save, data entry
3. Implement resume parser with AI
4. Implement clipboard/buffer parser
5. Fix page refresh mechanism
6. Add reporting and analytics

**Stakeholders:** Olya, Zhenya, development team

**Related Resources:** LibDev platform, Google Drive for documentation

---

### TipCan Solutions Client Project

**Status:** Active Client Relationship

**Description:** Freelance website and design services client engagement

**Key Features:**
- UI/UX design sourcing
- Notification systems (YouTube, Email)
- Employee management notifications

**Current Issues:**
- Client finds existing freelance websites inadequate ("crappy")
- Need better UI/UX design sourcing solutions

**Next Steps:**
- Implement YouTube notifications
- Implement email notifications for new employees
- Improve freelance platform offering

**Stakeholders:** Alan (Compliance Specialist at TipCan Solutions)

**Related Resources:** None specified

---

### SiteBoon AI Training Program

**Status:** Planning

**Description:** Web generation AI tool training for team member Marta

**Key Features:**
- AI-powered web generation
- Video-based learning materials

**Next Steps:**
- Create video lessons for Marta
- Demonstrate web generation capabilities

**Stakeholders:** Marta

**Related Resources:** SiteBoon AI platform

---

## 5. WORKFLOWS & PROCESSES

### Job Application Intake Workflow (Proposed Improvement)

**Purpose:** Streamline the process of adding new job applicants from initial contact to full application entry

**Steps:**
1. Applicant contacts via messenger (Telegram, etc.) before sending resume
2. Create new job application with minimal data: Name + Messenger contact
3. Save partial application
4. When resume received, upload document (PDF, DOCX, RTF, image)
5. AI parser automatically extracts and populates fields
6. Review and verify auto-populated data
7. Update status as application progresses
8. System auto-refreshes to show status updates

**Responsible Parties:**
- Recruitment team: Initial data entry
- System: Automated parsing
- Hiring managers: Review and status updates

**Tools/Platforms Used:** LibDev Talents, AI parsing service, Google Drive

**Success Criteria:**
- Reduced manual data entry time
- Accurate field population from resumes
- Smooth workflow without page refresh issues

---

### Microservice QA and Issue Tracking Process

**Purpose:** Establish structured approach to testing and tracking issues for new microservices

**Steps:**
1. Create Excel/spreadsheet with standardized columns:
   - Page/Section
   - Screenshot
   - Critical Level (Critical/High/Medium/Low)
   - Issue Description
   - Comments/Additional Info
   - Solution/Parser type needed
2. Share document with edit access across team (Google Drive)
3. Log all QA findings during testing
4. Prioritize critical issues: Create, Search, Save, Reports
5. Review and assign to development
6. Track resolution status

**Responsible Parties:**
- QA team (Olya, Zhenya): Issue logging
- Development team: Issue resolution
- Product owner: Prioritization

**Tools/Platforms Used:** Excel/Google Sheets, Google Drive, Screenshot tools

**Success Criteria:**
- All issues documented before deployment
- Critical issues resolved
- Clear communication between QA and development

---

## 6. RULES & BEST PRACTICES

### Microservice Launch Protocol

**Rule/Practice:** Every new microservice release must include: list of pages/screens, screenshot analysis, field analysis, structured QA documentation

**Rationale:** Ensures thorough testing and clear communication of issues before widespread deployment; prevents rushed launches with critical bugs

**Application:** Apply to all microservice deployments, starting with LibDev Talents

**Examples:** The Talents microservice QA revealed multiple critical issues that would have blocked user adoption if launched without proper documentation and tracking

---

### Structured Issue Logging

**Rule/Practice:** Do not rely on verbal communication or chat messages for tracking technical issues. All QA findings must be logged in structured format (Excel/sheets) with screenshots, criticality levels, and clear descriptions

**Rationale:** Prevents issues from being forgotten, enables prioritization, creates accountability, and provides historical record

**Application:** Use for all microservice QA, feature testing, and bug tracking

**Examples:** Creating the Talents QA Excel with columns for page, screenshot, critical level, description, comments

---

### Contact Field Tool Filtering

**Rule/Practice:** Contact/communication fields should only display relevant messenger and communication platforms (Telegram, WhatsApp, Viber, Phone, Email, VK) - not unrelated tools like design software

**Rationale:** Reduces clutter, prevents user confusion, speeds up data entry

**Application:** Apply to all contact fields across all microservices and platforms

**Examples:** Talents contact fields were showing Photoshop, Illustrator, and hundreds of irrelevant options

---

### Minimal Initial Data Entry

**Rule/Practice:** Allow creation of records with minimal required fields (e.g., just name + contact method), then expand data later when more information is available

**Rationale:** Matches real-world workflow where initial contact happens before full information is received; prevents data loss from delayed entry

**Application:** Job applications, client intake, any multi-step information gathering process

**Examples:** Creating job application with just Telegram username when applicant first makes contact, before resume is received

---

## 7. PROBLEMS & SOLUTIONS

### Problem: Manual Resume Data Entry is Time-Consuming

**Description:** Recruitment team must manually read resumes and type all information into system fields, which is slow and error-prone

**Impact:** Slows down hiring process, reduces productivity, increases errors

**Root Cause:** No automated data extraction from documents

**Proposed Solution:** Implement AI-powered parser that can read multiple document formats (PDF, DOCX, RTF, images) and automatically extract and populate fields

**Decision Made:** Approved to develop resume parser with AI integration

**Implementation Owner:** Development team

**Status:** Approved - awaiting implementation

---

### Problem: Excel/Table Data Cannot Be Bulk Imported

**Description:** When candidate data comes in Excel/table format, there's no way to paste and automatically distribute data to correct fields

**Impact:** Forces manual field-by-field data entry even when data is already structured

**Root Cause:** No clipboard/buffer parser functionality

**Proposed Solution:** Develop clipboard parser that recognizes structured data and maps it to appropriate fields in the application

**Decision Made:** Approved as critical feature

**Implementation Owner:** Development team

**Status:** Approved - awaiting implementation

---

### Problem: Page Doesn't Refresh After Status Updates

**Description:** When updating application status, the page must be manually refreshed to see changes; unsaved field data may be lost during refresh

**Impact:** Poor user experience, potential data loss, workflow interruption

**Root Cause:** Missing auto-refresh or reactive state management

**Proposed Solution:** Implement automatic page updates when status changes, or use reactive framework to update UI without full refresh

**Decision Made:** Identified as critical issue to fix

**Implementation Owner:** Development team

**Status:** Critical - needs immediate attention

---

### Problem: Status System Conflicts

**Description:** Cannot reuse status names (like "new") across different entity types; system needs unique statuses for each context

**Impact:** Confusion in status tracking, potential data integrity issues

**Root Cause:** Status system not designed for multi-entity usage

**Proposed Solution:** Implement either: (1) unique status sets per entity type, or (2) tagging system with multi-select capability

**Decision Made:** Needs architectural decision on approach

**Implementation Owner:** Development team

**Status:** Proposed - awaiting technical design decision

---

### Problem: No Structured QA Process for New Microservices

**Description:** Team was approaching new microservice QA in ad-hoc manner without systematic issue tracking

**Impact:** Issues forgotten, priorities unclear, developer communication poor

**Root Cause:** No established QA workflow or documentation standards

**Proposed Solution:** Create standardized Excel template for QA issue logging with required fields (page, screenshot, criticality, description, comments)

**Decision Made:** Approved and implemented immediately

**Implementation Owner:** Zhenya (creating template), all QA team (using it)

**Status:** In Progress

---

## 8. TOOLS & RESOURCES

### Artificial Intelligence / AI Parser

**Type:** AI Tool - Data Extraction

**Purpose:** Extract structured data from unstructured documents (resumes, forms, etc.)

**Use Case:** Automatically parse uploaded resumes in any format and populate applicant database fields

**Access/Links:** To be integrated into LibDev Talents

**Recommended For:** Recruitment workflow, document processing, data entry automation

**Notes:** Should support PDF, DOCX, RTF, and image formats; possibly use existing AI tools like Claude, ChatGPT, or similar

---

### Excel / Google Sheets

**Type:** Documentation / Data Management Tool

**Purpose:** QA issue tracking, structured data management

**Use Case:** Log all microservice QA findings with screenshots, criticality levels, and descriptions

**Access/Links:** Google Drive with shared access

**Recommended For:** QA teams, issue tracking, temporary data staging before system import

**Notes:** Must be shared with edit access across team; needs clear column structure

---

### LibDev Talents Microservice

**Type:** Development Tool / Internal Platform

**Purpose:** Talent management, job application tracking, employee onboarding

**Use Case:** Central system for managing recruitment pipeline and employee data

**Access/Links:** Internal platform

**Recommended For:** HR team, recruitment team, hiring managers

**Notes:** Currently in QA phase with multiple critical issues to resolve

---

### Tango

**Type:** Documentation Tool

**Purpose:** Process documentation, workflow guides

**Use Case:** Document new employee onboarding process with step-by-step instructions

**Access/Links:** Link to be provided in Excel comments for new employee requirements

**Recommended For:** Process documentation, training materials

**Notes:** Use for creating visual step-by-step guides

---

### SiteBoon AI

**Type:** AI Tool - Web Generation

**Purpose:** AI-powered website generation

**Use Case:** Training Marta on web generation capabilities; potentially offering to clients

**Access/Links:** Not specified

**Recommended For:** Web design, rapid prototyping, client projects

**Notes:** Plan to create video lessons demonstrating capabilities

---

## 9. TECHNICAL ARCHITECTURE

### LibDev Talents - Data Import Architecture

**Technology Stack:** Not fully specified - uses AI integration

**Architecture Pattern:** Document processing pipeline with AI extraction

**Key Components:**
- **Resume Parser Module**: Accepts multiple file formats (PDF, DOCX, RTF, images)
- **AI Extraction Service**: Processes documents and extracts structured data
- **Field Mapping Engine**: Maps extracted data to database fields
- **Clipboard Parser Module**: Accepts tabular data from clipboard and distributes to fields

**Integration Points:**
- AI service (external or internal)
- File upload system
- Database (applicant/employee tables)
- UI layer for data review and correction

**Documentation Location:** To be created in project documentation

---

### Status Management System

**Technology Stack:** Database with state management

**Architecture Pattern:** State machine (needs redesign)

**Key Components:**
- Status definitions (needs unique namespace per entity type)
- Status transitions
- UI refresh mechanism (currently broken)

**Integration Points:**
- Frontend UI (reactive state needed)
- Database persistence layer
- Notification system (future)

**Documentation Location:** Technical specs needed

---

## 10. DECISIONS LOG

### Decision: Implement AI-Powered Resume Parser

**Date:** October 24, 2025

**Context:** Manual resume data entry is time-consuming and error-prone; team receives resumes in multiple formats

**Options Considered:**
1. Continue manual entry
2. Require standardized format from applicants
3. Implement AI-powered parser for automatic extraction

**Decision Made:** Implement AI-powered parser supporting PDF, DOCX, RTF, and image formats

**Rationale:** Significantly reduces manual work, improves data accuracy, scales better as hiring increases

**Impact:** Development effort required; once implemented, will dramatically speed up application intake process

**Follow-up Required:** Define field mapping specifications, select/integrate AI service

---

### Decision: Create Structured QA Tracking System

**Date:** October 24, 2025

**Context:** New microservice launch revealed need for better QA issue tracking; ad-hoc approach was insufficient

**Options Considered:**
1. Continue verbal/chat-based communication
2. Use existing project management tool
3. Create custom Excel template for QA tracking

**Decision Made:** Create Excel template with structured columns (page, screenshot, criticality, description, comments)

**Rationale:** Quick to implement, familiar to team, flexible, shareable via Google Drive

**Impact:** Improves communication between QA and development, ensures issues aren't forgotten, enables prioritization

**Follow-up Required:** Zhenya to create template immediately and share with team

---

### Decision: Implement Minimal Initial Data Entry

**Date:** October 24, 2025

**Context:** Applicants often make initial contact via messenger before providing full resume

**Options Considered:**
1. Wait for full resume before creating application record
2. Allow minimal record creation (name + contact only)

**Decision Made:** Allow minimal record creation with just name and messenger contact

**Rationale:** Matches real-world workflow, prevents data loss, allows earlier engagement tracking

**Impact:** Requires UI to support partial record creation and completion later

**Follow-up Required:** Implement UI that allows saving with minimal fields

---

### Decision: Develop New Employee Onboarding in Talents System

**Date:** October 24, 2025

**Context:** Need system for new employee registration and data collection

**Options Considered:**
1. Use existing external HR system
2. Build into LibDev Talents platform

**Decision Made:** Build into LibDev Talents platform

**Rationale:** Centralized talent management (applicants + employees in one system), custom workflow control

**Impact:** Requires requirements gathering from Olya, development effort

**Follow-up Required:** Olya to create detailed requirements document with Tango process documentation

---

## 11. DOCUMENTATION & KNOWLEDGE GAPS

### Talents Microservice QA Documentation

**Type:** Technical Doc / QA Report

**Purpose:** Comprehensive list of all issues found during QA testing of Talents microservice

**Target Audience:** Development team, product manager

**Current Status:** In Progress (Zhenya creating Excel)

**Location(s):** Google Drive (to be shared)

**Owner:** Zhenya (creation), QA team (maintenance)

---

### New Employee Onboarding Requirements

**Type:** Process Doc / Requirements Specification

**Purpose:** Define complete onboarding workflow, required data fields, employee self-registration process

**Target Audience:** Development team, HR team

**Current Status:** Missing

**Location(s):** To be created - link to be placed in Talents QA Excel

**Owner:** Olya

---

### Resume Parser Field Mapping Specification

**Type:** Technical Doc / Data Mapping

**Purpose:** Define which extracted data elements map to which database fields

**Target Audience:** Development team, AI integration team

**Current Status:** Missing

**Location(s):** Project documentation (to be created)

**Owner:** Product/Development team

---

### Talents Microservice Page/Screen List

**Type:** Technical Doc / Feature Inventory

**Purpose:** Complete list of all pages/screens in Talents with screenshots and field analysis

**Target Audience:** QA team, development team, stakeholders

**Current Status:** Missing (should be created before any microservice launch)

**Owner:** Product team / Development team

---

## 12. COMMUNICATION & ANNOUNCEMENTS

### TipCan Solutions Client Updates

**What:** Progress on YouTube notifications and email notification systems

**To Whom:** Alan (Compliance Specialist at TipCan Solutions)

**Channel:** Client communication (email/meeting)

**Message Type:** Progress update

**Timing:** After implementation milestones

**Owner:** Account manager / Project manager

**Follow-up Plan:** Regular status updates until features deployed

---

### Talents Microservice QA Findings

**What:** Summary of critical issues found during QA and timeline for fixes

**To Whom:** Development team, stakeholders

**Channel:** Internal team communication

**Message Type:** Initial report + ongoing updates

**Timing:** Immediate (after QA Excel completed)

**Owner:** Olya / Zhenya

**Follow-up Plan:** Weekly updates until critical issues resolved

---

## 13. BLOCKERS & DEPENDENCIES

### New Employee System Blocked on Requirements

**Description:** Cannot develop new employee onboarding module in Talents system

**Impact:** Employee tracking and onboarding features cannot proceed

**Waiting On:** Olya to provide detailed requirements document with Tango process documentation

**Resolution Path:** Olya to create requirements doc, share link in Excel, development can begin

**Priority:** High

---

### Parser Development Needs Field Mapping

**Description:** AI resume parser cannot be fully developed without clear field mapping specification

**Impact:** Parser may extract data that doesn't align with database schema

**Waiting On:** Product/Development team to define field mapping

**Resolution Path:** Create technical specification document mapping resume fields to database fields

**Priority:** Critical

---

## 14. KEY INSIGHTS & LESSONS

### Structured QA Approach Prevents Launch Issues

**Insight:** Taking a systematic, documented approach to QA (with screenshots, criticality levels, structured tracking) reveals critical issues that would block adoption if launched prematurely

**Context:** Team initially approached Talents microservice QA informally; structured Excel approach revealed numerous critical issues

**Application:** Apply structured QA template to all future microservice launches before deployment; prioritize Critical issues: Create, Search, Save, Reports

**Related Concepts:** Quality gates, launch checklists, issue prioritization

---

### Match System to Real-World Workflow

**Insight:** Systems should accommodate how work actually happens, not force users to adapt to rigid workflows

**Context:** Applicants contact via messenger before sending resume; system should allow minimal record creation at that point rather than requiring full data upfront

**Application:** When designing data entry workflows, map actual user journey and allow incremental data collection

**Related Concepts:** User-centered design, progressive disclosure, form design best practices

---

### Automation ROI is High for Repetitive Data Entry

**Insight:** Investing in AI-powered parsing for resume data extraction will dramatically reduce time spent on manual data entry and improve accuracy

**Context:** Team currently manually reads and types resume data into system fields

**Application:** Identify other high-volume data entry tasks that could benefit from AI extraction (client intake forms, vendor information, etc.)

**Related Concepts:** Process automation, AI integration, productivity improvement

---

### Contact Management Needs Filtering

**Insight:** Tools and contact methods should be filtered to show only relevant options for the context (messengers for contact fields, not design software)

**Context:** Contact fields were showing hundreds of irrelevant tools including Photoshop, Illustrator

**Application:** Review all dropdown/selection fields to ensure options are contextually relevant; implement filtering logic

**Related Concepts:** UI/UX best practices, context-aware interfaces, cognitive load reduction

---

## 15. ANALOGIES & FRAMEWORKS

No specific analogies or frameworks were discussed in this call.

---

## 16. FOLLOW-UP ITEMS

### Scheduled Meetings
- None explicitly scheduled

### Reviews Needed
- QA Excel template review (after Zhenya creates)
- New employee requirements document review (after Olya creates)
- Field mapping specification review (when created)

### Reports Due
- Talents QA issue summary (Zhenya - immediate)
- New employee onboarding requirements (Olya - soon)

---

**Document processed with Call Organizer AI Prompt v1.0**
**Original file:** 241025.md
**Processing date:** October 31, 2025