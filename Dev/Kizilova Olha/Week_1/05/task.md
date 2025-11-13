# Task Breakdown - November 5, 2025

## Instructions
**What**: Detailed action steps
**Include**:
- Break each plan item into specific steps
- Add links and resources
- Clear instructions for execution

---

## Task 1: Extract & Migrate Notes from Old CRM

**Priority:** HIGH  
**Timeline:** Near term  
**Status:** Not Started  
**Collaboration:** With Rekonvald Viktoriia (requirements)

### Steps:
1. Coordinate with Rekonvald Viktoriia to define notes field structure requirements
2. Identify all note types in old CRM (admin notes, HR notes, communication history)
3. Create database migration scripts for notes extraction
4. Transform data to match new CRM structure
5. Implement single consolidated "Notes" field with section headers for archive
6. Test migration with sample data
7. Execute full migration after approval

### Resources and Links:
- Old CRM system access
- New CRM database
- Database migration scripts
- Data transformation tools
- CRM Migration, Recruitment Platform project references

### Instructions:
Critical migration task to preserve historical candidate and client communication data. Work closely with HR team (Rekonvald Viktoriia) to ensure all note types are captured and properly structured in new system.

---

## Task 2: Fix & Optimize OpenAI GPT Assistants Chain

**Priority:** HIGH  
**Timeline:** When budget allows for testing ($5-20 needed)  
**Status:** Blocked - awaiting API budget allocation  
**Collaboration:** With Rekonvald Viktoriia (testing)

### Steps:
1. Wait for OpenAI API budget approval from Pasichna Anastasiia ($5-20)
2. Review GPT Assistant chain workflow: Job Request → Job Template → Post Template → Job Post
3. Investigate translation functionality issues
4. Test chain with API credits
5. Fix identified bugs
6. Optimize prompt structure for better results
7. Coordinate testing with Rekonvald Viktoriia

### Resources and Links:
- OpenAI Platform
- CRM backend
- API integration documentation
- CRM, Recruitment Platform project references
- GPT Assistant configuration documentation

### Instructions:
**BLOCKED** - Cannot proceed without API budget approval. Once approved, focus on fixing translation issues and validating the complete HR automation workflow. This enables significant time savings for HR team.

---

## Task 3: Disable Old CRM Functions Progressively

**Priority:** HIGH  
**Timeline:** Ongoing migration project  
**Status:** In Progress - Talents module in testing  
**Collaboration:** With Rekonvald Viktoriia (testing)

### Steps:
1. Verify Talents module feature parity with old CRM
2. Complete QA testing with Rekonvald Viktoriia
3. Ensure data migration is complete for Talents
4. Disable Talents-related functions in old CRM
5. Monitor for any issues after deprecation
6. Document deprecation process for future modules
7. Repeat process for Accounts → Businesses → Task Manager modules

### Resources and Links:
- Both CRM systems (old and new)
- Migration documentation
- QA protocols
- CRM Migration project references

### Instructions:
Progressive migration approach ensures thorough testing before deprecating old features. Talents module is currently in testing phase. Document the process to replicate for subsequent modules.

---

## Task 4: Review & Update Employee User Access Statuses

**Priority:** HIGH  
**Timeline:** Near term  
**Status:** Waiting - technical implementation needed  
**Collaboration:** With Rekonvald Viktoriia (HR review)

### Steps:
1. Develop Talents-Users integration (if not yet complete)
2. Coordinate with Rekonvald Viktoriia to review employee statuses
3. Identify former employees still showing as active
4. Update user access statuses in CRM
5. Remove access for former employees
6. Ensure personal logins are enforced (no shared accounts)
7. Test user-Talent linking functionality

### Resources and Links:
- CRM user management system
- Access control systems
- CRM, User Management project references
- Employee directory

### Instructions:
Critical for accountability and audit trails. Ensure all employees use personal logins rather than shared admin accounts. Integrate Talents module with Users system for proper access control.

---

## Task 5: Develop Short Link System for Prompt Optimization

**Priority:** MEDIUM  
**Timeline:** Future sprint  
**Status:** Not Started - requirements gathering

### Steps:
1. Gather requirements for internal URL shortening system
2. Design database structure for short links with categorization
3. Implement automatic forwarding functionality
4. Integrate with CRM media storage
5. Create management interface for link creation/categorization
6. Test system with long Google Drive/Dropbox links
7. Document usage guidelines

### Resources and Links:
- Backend development environment
- Database design tools
- CRM media storage system
- Infrastructure project references

### Instructions:
Addresses problem of long Google Drive/Dropbox links consuming excessive tokens in prompts. Create internal short link management system to reduce prompt size while maintaining functionality.

---

## Task 6: Clean & Parse Resumes in CRM

**Priority:** MEDIUM  
**Timeline:** After notes migration  
**Status:** Not Started

### Steps:
1. Wait for notes migration completion (Task 1)
2. Identify all resumes in old CRM with HTML/images
3. Develop AI-powered cleaning script to remove HTML, images
4. Implement parsing logic to auto-fill incomplete fields
5. Test parsing accuracy with sample resumes
6. Execute cleaning and parsing on all resumes
7. Validate data quality after processing

### Resources and Links:
- CRM database
- AI parsing tools
- HTML cleaning scripts
- CRM, Recruitment Platform project references

### Instructions:
Automate resume processing to improve data quality and reduce manual data entry. Focus on cleaning HTML artifacts and extracting structured data to populate CRM fields automatically.

---

## Task 7: Document CRM Development Process for Future Microservices

**Priority:** MEDIUM  
**Timeline:** Concurrent with Talents completion  
**Status:** In Progress  
**Collaboration:** With Artemchuk Nikolay (PM documentation)

### Steps:
1. Document Talents module development process:
   - Architecture decisions
   - Database structure design
   - API design patterns
   - Development workflow
2. Extract reusable patterns and templates
3. Create documentation structure for microservices replication
4. Coordinate with Artemchuk Nikolay for PM perspective
5. Add to RAC knowledge base
6. Create template for Accounts and Businesses modules

### Resources and Links:
- Talents module codebase
- Cursor IDE
- Documentation templates
- File system
- RAC Documentation project

### Instructions:
Critical documentation to enable replication of successful Talents development process. Capture technical details, decisions, and patterns that can be reused for subsequent microservices development.

---

## Reminder
- Break down each plan into steps
- Add all necessary links and resources
- Write clear execution instructions
