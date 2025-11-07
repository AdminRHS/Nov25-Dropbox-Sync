# Task Breakdown - November 4, 2025

## Instructions
**What**: Detailed action steps
**Include**:
- Break each plan item into specific steps
- Add links and resources
- Clear instructions for execution

---

## Task 1: Complete Edit Mode Implementation

### Steps:
1. Review current edit mode functionality and identify remaining gaps
2. Implement toolbar with all necessary editing controls
3. Create modal windows for photo upload and advanced settings
4. Integrate photo upload functionality with proper file handling
5. Test all edit mode features for smooth interaction
6. Fix any bugs or UI inconsistencies
7. Conduct user testing for feedback

### Resources and Links:
- Gemini Cloud (admin.rh account)
- Claude AI assistant
- AI Catalog / Any Employee project repository
- Previous prompt templates created today
https://www.notion.so/rh-s/Catalog-Redesign-Any-Employee-292b16a314518008825cc00c60b1be74

### Instructions:

Use the optimized prompts created today to guide AI assistants in implementing remaining features. Focus on one component at a time (toolbar, modals, photo upload) to avoid accidental function deletions. Always work with the original AI-generated code and make incremental changes. Test each feature immediately after implementation to catch issues early.


---

## Task 2: Implement Tag Autocomplete System

### Steps:
1. Design the tag input UI with active input field
2. Create autocomplete suggestion logic based on existing tags
3. Implement tag selection without requiring clicks
4. Add keyboard navigation (arrow keys, enter) for tag selection
5. Style the autocomplete dropdown for visual clarity
6. Test tag input with various scenarios (new tags, existing tags, partial matches)
7. Optimize performance for large tag lists

### Resources and Links:
- Gemini Cloud for code generation
- UI/UX best practices for autocomplete interfaces
- Existing tag system in project

### Instructions:

Create a detailed prompt for the AI assistant describing the autocomplete behavior: typing should immediately show suggestions without clicking, arrow keys should navigate options, Enter should select, and Escape should close. The input field should remain active during typing. Focus on making the interaction feel natural and frictionless. Reference successful autocomplete implementations (like search engines) for inspiration.


---

## Task 3: Code Optimization and Cleanup

### Steps:
1. Create backup of current working code
2. Prepare detailed prompt for AI assistant specifying "optimize and clean WITHOUT deleting any functions"
3. Review current codebase for redundant code, unused variables, and inefficient patterns
4. Run AI optimization with careful monitoring
5. Test all functionality after optimization to ensure nothing broke
6. Document any changes made during optimization
7. Commit cleaned code with descriptive commit message

### Resources and Links:
- Version control system (Git)
- Code quality tools (linters, formatters)
- Gemini Cloud with precise optimization prompt

### Instructions:

Use the code optimization prompt created today. Emphasize to the AI assistant that ALL existing functions must be preserved. Break optimization into smaller chunks (e.g., optimize one module at a time) to minimize risk. After each optimization pass, immediately test the affected functionality. If functions get deleted, revert to backup and adjust the prompt to be more specific about preservation.


---

## Task 4: Document AI Prompt Templates

### Steps:
1. Review all prompts used today and identify the most effective ones
2. Create a documentation structure for prompt library
3. Document the "code optimization without deletion" prompt with usage notes
4. Document the "edit mode improvement" prompt with examples
5. Document the "tag autocomplete" prompt with specifications
6. Add notes about differences between Gemini and Claude prompt styles
7. Create guidelines for writing future prompts

### Resources and Links:
- Today's working session notes
- Prompt engineering best practices documentation
- Project documentation repository

### Instructions:

Create a reusable prompt library that can be referenced in future sessions. For each prompt, include: (1) the exact prompt text, (2) which AI assistant it works best with, (3) what it accomplishes, (4) any known limitations, and (5) example results. Add specific notes about how to phrase requests to avoid accidental function deletions. Include lessons learned about working with modified code vs. original AI-generated code.


---

## Task 5: Test Cross-AI Compatibility

### Steps:
1. Identify core functionality that must work with both Gemini and Claude
2. Generate same feature using both AI assistants separately
3. Compare code structure and approach differences
4. Test functionality of both implementations
5. Document compatibility issues and workarounds
6. Create guidelines for writing AI-agnostic code
7. Establish a testing protocol for future AI-assisted development

### Resources and Links:
- Gemini Cloud (admin.rh and personal accounts)
- Claude AI assistant
- Project test environment

### Instructions:

Start with a simple, well-defined feature to compare AI approaches. Request the same functionality from both Gemini and Claude using similar prompts. Analyze how each AI structures the code, what patterns they use, and where incompatibilities arise. Pay special attention to areas that caused issues today (like preserving original functionality). Create a compatibility checklist that can be used before integrating AI-generated code.


---

## Task 6: Establish Version Control Best Practices

### Steps:
1. Set up proper Git workflow for AI-assisted development
2. Create branching strategy (e.g., separate branches for AI experiments)
3. Implement commit message conventions for AI-generated code
4. Set up code review process before merging AI changes
5. Create rollback procedures for when AI deletions occur
6. Document workflow in project README
7. Train team members on new workflow

### Resources and Links:
- Git documentation
- GitHub/GitLab best practices
- Project repository

### Instructions:

Design a workflow that protects against accidental function deletions while allowing rapid AI-assisted development. Key elements: (1) Always commit working code before making AI-assisted changes, (2) Use descriptive branch names indicating AI tool used, (3) Review diffs carefully before committing AI changes, (4) Keep backup branches of stable code, (5) Document which AI assistant was used in commit messages. Create a simple checklist that can be followed before and after each AI coding session.


---

## Reminder
- Break down each plan into steps
- Add all necessary links and resources
- Write clear execution instructions
