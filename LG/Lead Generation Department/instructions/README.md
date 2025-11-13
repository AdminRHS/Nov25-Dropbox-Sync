# Instruction Repository Structure

## Purpose
Provide a consistent hierarchy and naming system so every Markdown instruction file is easy to locate, maintain, and onboard new team members with minimal friction.

## Recommended Folder Hierarchy
Each top-level folder covers one operational pillar. Use two-digit prefixes to keep the order consistent in file explorers.

1. 01_Onboarding_and_Training - Global onboarding guides, new-hire checklists, team playbooks.
2. 02_Account_and_Tool_Setup - Access requests, security policies, tool setup walkthroughs.
3. 03_CRM_Operations - CRM workflows, data hygiene rules, reporting standards.
4. 04_Lead_Research_and_Prospecting - Research frameworks, data sources, enrichment flows.
5. 05_Outreach_and_Messaging - LinkedIn, email, and multi-channel messaging templates.
6. 06_Calendar_and_Event_Management - Scheduling, event tracking, and follow-up processes.
7. 07_LinkedIn_Operations - Platform-specific tactics: profile optimization, SSI guidance, inbox management.
8. 08_CRM_Playbooks - Deep dives into specific pipelines, automations, integrations.
9. 09_Recruitment_Enablement - Candidate sourcing, screening rubrics, recruiter workflows.
10. 10_Analytics_and_Reporting - Dashboards, KPI definitions, recurring report SOPs.
11. 11_Templates_and_Checklists - Reusable forms, QA checklists, decision trees.
12. 99_General_and_Shared - Cross-functional references, mixed-topic notes, parking lot items.

Add optional subfolders (for example, 01_Onboarding_and_Training/Role_Specific) when a topic grows beyond one Markdown file.

## Handling Documents Without a Clear Category
- Place them temporarily in 99_General_and_Shared with a short descriptor (for example, LinkedIn_Pilot_Notes.md).
- Add a comment at the top noting the intended future home.
- Schedule a monthly housekeeping pass to either create a new category or merge the doc into an existing one.

## Naming Rules
### Top-Level Folders
- Format: NN_Topic_Title where NN is a two-digit sequence (01, 02, ... 99).
- Use Title Case with underscores for readability.
- Reserve 99_ for temporary or mixed-topic content that still needs classification.

### Subfolders
- Format: TopicKeyword_Descriptor without numeric prefixes unless order matters (for example, 01_Preboarding, 02_First_Week for sequential guides).
- Keep names concise (under 40 characters) and descriptive of the process or audience.

### Markdown Files
- Use kebab-case or snake_case aligned with folder naming (linkedin_inbox_workflow.md, crm-data-validation.md).
- Start each file with an H1 title that matches the filename in Title Case.
- Include metadata (owner, last update, related SOPs) in the file header when relevant.

## Maintenance Tips
- Review the hierarchy quarterly to ensure new initiatives (for example, AI tooling, compliance) have dedicated folders.
- Keep README files in large folders to summarize their contents and link related docs.
- When deprecating a guide, move it to an Archive subfolder inside the same topic folder and record the reason and date in the filename.
