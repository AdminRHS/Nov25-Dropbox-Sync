# Daily Report Collection Prompts - Department Index

## Overview

This folder contains department-specific prompts for processing call transcriptions and generating daily activity reports. Each prompt combines:

1. **MAIN PROMPT v3.md** - Comprehensive call organization framework
2. **PROMPT_Daily_Report_Collection.md** - Daily report automation template
3. **Department-specific context** - Employees, projects, tools, and vocabulary

---

## Available Department Prompts

### 1. HR Department
**File:** `PROMPT_HR_Daily_Report.md`
**Team Size:** 2 employees
**Focus Areas:**
- Recruitment and talent acquisition
- Employee onboarding and training
- CV processing and candidate evaluation
- Interview coordination
- Employee management

**Key Employees:**
- Rekonvald Viktoriia (ID: 83953) - Recruiter
- Nealova Evgeniya (ID: 72889) - Recruiter

**Prompt Log Location:** `Dropbox/Nov25/HR Nov25/HR prompt log.md`
**Reports Location:** `Dropbox/Nov25/HR Nov25/Reports/{DAY}/`

---

### 2. AI Department
**File:** `PROMPT_AI_Daily_Report.md`
**Team Size:** 3 employees
**Focus Areas:**
- Prompt engineering and optimization
- AI tool integration and automation
- Framework development and maintenance
- Technical infrastructure management
- AI workflow automation

**Key Employees:**
- Artemchuk Nikolay (ID: 37226) - Project manager
- Perederii Vladislav (ID: 86246) - Prompt engineer
- Zasiadko Matvii (ID: 86981) - Prompt engineer

**Prompt Log Location:** `Dropbox/Nov25/AI Nov25/AI prompt log.md`
**Reports Location:** `Dropbox/Nov25/AI Nov25/Reports/{DAY}/`

---

### 3. Video Department
**File:** `PROMPT_Video_Daily_Report.md`
**Team Size:** 3 employees
**Focus Areas:**
- Video editing and post-production
- Animation and motion graphics
- Video content creation
- Video tool integration
- Creative video production

**Key Employees:**
- Podolskyi Sviatoslav (ID: 299) - Video Editor
- Azanova Darʼya (ID: 80190) - Video Editor

**Prompt Log Location:** `Dropbox/Nov25/Video Nov25/Video prompt log.md`
**Reports Location:** `Dropbox/Nov25/Video Nov25/Reports/{DAY}/`

---

### 4. Sales Department
**File:** `PROMPT_Sales_Daily_Report.md`
**Team Size:** 1 employee
**Focus Areas:**
- B2B sales and client acquisition
- Client relationship management
- Sales pipeline management
- Deal closure and negotiation
- CRM management

**Key Employees:**
- Kovalska Anastasiya (ID: 45405) - Sales Manager

**Prompt Log Location:** `Dropbox/Nov25/Sales Nov25/Sales prompt log.md`
**Reports Location:** `Dropbox/Nov25/Sales Nov25/Reports/{DAY}/`

---

### 5. Design Department
**File:** `PROMPT_Design_Daily_Report.md`
**Team Size:** 9+ employees
**Focus Areas:**
- UI/UX design and user research
- Graphic design and branding
- Web design and layout
- Illustration and creative assets
- Design system development

**Key Employees:**
- Shelep Olha (ID: 86641) - UI/UX designer
- Bogun Polina (ID: 87537) - UI/UX designer
- Kucherenko Iuliia (ID: 228) - Graphic Designer
- And 6+ more designers

**Prompt Log Location:** `Dropbox/Nov25/Design Nov25/Design prompt log.md`
**Reports Location:** `Dropbox/Nov25/Design Nov25/Reports/{DAY}/`

---

### 6. Dev Department
**File:** `PROMPT_Dev_Daily_Report.md`
**Team Size:** 3 employees
**Focus Areas:**
- Frontend development
- Backend development
- Full-stack development
- QA testing
- System integration
- Technical infrastructure

**Key Employees:**
- Kizilova Olha (ID: 178) - Backend Developer
- Danylenko Liliia (ID: 72754) - Full-Stack Developer
- Klimenko Yaroslav (ID: 86478) - Frontend Developer

**Prompt Log Location:** `Dropbox/Nov25/Dev Nov25/Dev prompt log.md`
**Reports Location:** `Dropbox/Nov25/Dev Nov25/Reports/{DAY}/`

---

### 7. LG Department (Lead Generation)
**File:** `PROMPT_LG_Daily_Report.md`
**Team Size:** 11+ employees
**Focus Areas:**
- Lead generation and prospecting
- Data scraping and research
- Lead qualification and scoring
- Outreach campaigns
- CRM data management

**Key Employees:**
- Hanan Zaheur (ID: 87984) - Lead generator
- Shkinder Kseniia (ID: 87157) - Lead generator
- Archibong Isaac (ID: 86453) - Lead generator
- And 8+ more lead generators

**Prompt Log Location:** `Dropbox/Nov25/LG Nov25/LG prompt log.md`
**Reports Location:** `Dropbox/Nov25/LG Nov25/Reports/{DAY}/`

---

## Usage Instructions

### For Each Department:

1. **Read the department prompt log:**
   - Navigate to the department's prompt log file
   - Review today's activities

2. **Process call transcripts (if applicable):**
   - Use the department-specific prompt file
   - Follow the MAIN PROMPT v3.md framework
   - Extract department-specific information

3. **Generate daily activity report:**
   - Use the department-specific template
   - Create report in `Reports/{DAY}/` folder
   - Follow the 14-section structure

4. **Copy to Admin collection:**
   - Copy report to `/Admin/Reports/Nov25/{DAY}/`
   - Add department prefix to filename

### Example Command:

```
Process [DEPARTMENT] department activities and create comprehensive daily activity report for November [DAY], 2025.

1. Read [DEPARTMENT] prompt log: Dropbox/Nov25/[DEPARTMENT] Nov25/[DEPARTMENT] prompt log.md
2. Process any [DEPARTMENT]-related call transcripts using MAIN PROMPT v3.md framework
3. Create Reports/{DAY} folder in [DEPARTMENT] department
4. Generate detailed [DEPARTMENT] activity report following [DEPARTMENT]-specific template
5. Create Admin/Reports/Nov25/{DAY} folder if needed
6. Copy report to Admin folder with [DEPARTMENT] prefix
```

---

## Common Features Across All Prompts

### Base Context Integration
- ✅ MAIN PROMPT v3.md framework
- ✅ PROMPT_Daily_Report_Collection.md template
- ✅ Employee Directory integration
- ✅ Project Directory integration

### Report Structure (14 Sections)
1. Executive Summary
2. Department-Specific Activities
3. Tool Integration Activities
4. Deliverables
5. Metrics and Statistics
6. Key Deliverables
7. Department Impact Analysis
8. Technical Achievements
9. Challenges and Solutions
10. Files Created/Modified Summary
11. Recommendations for Follow-up
12. Success Indicators
13. Conclusion
14. Report Footer

### Quality Standards
- ✅ Comprehensive activity tracking
- ✅ Metrics and statistics calculation
- ✅ Impact analysis
- ✅ Professional formatting
- ✅ Consistent structure

---

## File Structure

```
PROMPT_Daily_Report_Collection/
├── README.md (this file)
├── PROMPT_Daily_Report_Collection.md (base template)
├── PROMPT_HR_Daily_Report.md
├── PROMPT_AI_Daily_Report.md
├── PROMPT_Video_Daily_Report.md
├── PROMPT_Sales_Daily_Report.md
├── PROMPT_Design_Daily_Report.md
├── PROMPT_Dev_Daily_Report.md
└── PROMPT_LG_Daily_Report.md
```

---

## Version History

**v1.0** - November 25, 2025
- Initial creation of all 7 department-specific prompts
- Integrated MAIN PROMPT v3.md context
- Integrated PROMPT_Daily_Report_Collection.md context
- Added department-specific employees, projects, tools, and vocabulary
- Created comprehensive README index

---

## Notes

- Each prompt is customized for its specific department
- All prompts follow the same base structure for consistency
- Department-specific sections are emphasized in each prompt
- Employee lists are based on `November 2025 - Employees_Public.md`
- Folder structure follows `Dropbox/Nov25/` organization

---

*Last Updated: November 25, 2025*
*Total Departments: 7*
*Total Prompt Files: 7*

