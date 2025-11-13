# Instruction Repository Structure

## Purpose
Provide a single source of truth for every Markdown SOP used by the Lead Generation Department, organized by operational pillar.

## Current Top-Level Folders
1. `01_OnboardingTraining`
2. `02_LinkedInOperations`
3. `03_CRMGuides`
4. `04_RecruitmentPlaybooks`
5. `05_ContentSystems`
6. `06_LeadGenerationWorkflows`
7. `07_InternalWorkflow`
8. `08_ToolsAutomation`
9. `99_ToSort`

Each folder owns its own README with subfolder explanations, status counts, and a “Last Reviewed” placeholder.

## How to Classify Documents
1. Identify the primary audience or workflow (LinkedIn, CRM, Recruitment, etc.).
2. Drop the Markdown file into the matching numbered folder and its subfolder.
3. If no category fits, place the file in `99_ToSort/Incoming` with a short note at the top explaining the context so it can be re-homed.

## Naming Standards
- **Folders:** `NN_PascalCaseTopic` (for example, `02_LinkedInOperations`). Subfolders use `PascalCase` as well and avoid symbols outside `_`.
- **Files:** `kebab-case.md` or `snake_case.md` that mirrors the H1 title inside the document.
- **README files:** One per folder, describing scope, subfolders, status counts, and last-reviewed date.

## Maintenance Rhythm
- Run a monthly grooming session: recategorize anything in `_ToSort`, archive outdated docs, and update status counts.
- When new initiatives launch, create a subfolder + README before adding content to keep the structure predictable.
- If more than three files accumulate in `99_ToSort/ArchiveHold`, spin up a new category or merge them into an existing one.
