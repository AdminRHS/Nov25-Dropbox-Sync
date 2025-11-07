# MAIN PROMPT v2 - Splitting Plan

**Date:** November 5, 2025  
**Purpose:** Organize MAIN PROMPT v2.md into modular, easily accessible topic-specific files  
**Based on:** SummariesOct structure analysis and Remote Helpers framework

---

## 🎯 Objectives

1. **Modularity:** Each section becomes a standalone, reusable file
2. **Easy Access:** Quick reference for specific topics during prompting
3. **Maintainability:** Update individual components without affecting others
4. **Scalability:** Add new sections without restructuring entire prompt
5. **AI-Friendly:** Optimized for Claude/GPT consumption and context management

---

## 📊 Analysis Summary

### Current Structure
- **File Size:** ~45KB (extremely large for a single prompt)
- **Total Sections:** 21 output sections + metadata + processing guidelines
- **Main Components:**
  1. Company Context (Remote Helpers)
  2. Employee Directory (32 employees)
  3. Project Directory (31+ projects)
  4. Output Template (21 sections)
  5. Processing Guidelines (7 major subsections)
  6. Usage Instructions
  7. Version History

### Discovered Patterns from SummariesOct
The existing framework suggests organizing by:
- **Context/** - Company, employee, project context
- **Resources/** - Templates, prompts, guides
- **Documentation/** - Architecture, implementation guides
- **Planning/** - Planning documents, strategies
- **Clusters/** - Business domain organization

---

## 📁 Proposed Directory Structure

```
MAIN_PROMPT_Sections/
│
├── 00-SPLITTING_PLAN.md                      # This file
│
├── 01-Core_Context/                          # Foundation files (3-4 files)
│   ├── Company_Context.md                    # Organizational vision, departments, platforms
│   ├── Employee_Directory.md                 # 32 employees with full details
│   ├── Project_Directory.md                  # 31+ projects with resources
│   └── System_Architecture.md                # Operating systems, tools, tech stack
│
├── 02-Output_Templates/                      # 21 section templates (grouped logically)
│   ├── 01-Meeting_Metadata.md               # Section 1
│   ├── 02-Executive_Summary.md               # Section 2
│   ├── 03-Action_Items_Tasks.md              # Section 3
│   ├── 04-Projects_Features.md               # Section 4
│   ├── 05-Workflows_Processes.md             # Section 5
│   ├── 06-Rules_Best_Practices.md            # Section 6
│   ├── 07-Problems_Solutions.md              # Section 7
│   ├── 08-Tools_Resources.md                 # Section 8
│   ├── 09-Technical_Architecture.md          # Section 9
│   ├── 10-Decisions_Log.md                   # Section 10
│   ├── 11-Documentation_Gaps.md              # Section 11
│   ├── 12-Communication_Announcements.md     # Section 12
│   ├── 13-Blockers_Dependencies.md           # Section 13
│   ├── 14-Key_Insights_Lessons.md            # Section 14
│   ├── 15-Analogies_Frameworks.md            # Section 15
│   ├── 16-Employee_Team_Context.md           # Section 16
│   ├── 17-Lead_Generation_Sales.md           # Section 17 (LG/Sales specific)
│   ├── 18-Design_Creative.md                 # Section 18 (Design specific)
│   ├── 19-Development_Technical.md           # Section 19 (Dev specific)
│   ├── 20-Onboarding_Training.md             # Section 20 (HR/Training specific)
│   └── 21-Follow_Up_Items.md                 # Section 21
│
├── 03-Processing_Guidelines/                 # Core logic (5-7 files)
│   ├── Participant_Identification.md         # Employee matching protocol
│   ├── Project_Recognition.md                # Project matching protocol
│   ├── Language_Handling.md                  # Multi-language support
│   ├── Vocabulary_Recognition.md             # Industry terms, abbreviations
│   ├── Inference_Rules.md                    # Priority, status, ownership inference
│   ├── Quality_Standards.md                  # What to extract, what to skip
│   └── Context_Specific_Extraction.md        # Department-specific extraction rules
│
├── 04-Usage_Documentation/                   # Usage guides (3-4 files)
│   ├── Quick_Start_Guide.md                  # Basic usage instructions
│   ├── Example_Usage.md                      # Examples with expected outputs
│   ├── Tips_Best_Practices.md                # Pro tips for optimal results
│   └── Advanced_Features.md                  # Power user features
│
├── 05-Reference_Materials/                   # Supporting docs (2-3 files)
│   ├── Glossary_Vocabulary.md                # LG, LLM, Design, Business terms
│   ├── Template_Structures.md                # Task/Step/Checklist templates
│   └── Version_History.md                    # Changelog and updates
│
└── 06-Assembled_Prompts/                     # Final combined versions (2-3 files)
    ├── FULL_PROMPT.md                        # Complete assembled prompt
    ├── SHORT_PROMPT.md                       # Condensed version
    └── DEPARTMENT_SPECIFIC/                  # Department-tailored versions
        ├── PROMPT_LG.md                      # Lead Gen focused
        ├── PROMPT_DESIGN.md                  # Design focused
        ├── PROMPT_DEV.md                     # Development focused
        └── PROMPT_HR.md                      # HR/Onboarding focused
```

**Total Files:** ~45-50 modular files organized in 6 main directories

---

## 🔍 Detailed File Breakdown

### 01-Core_Context/ (Foundation)

#### Company_Context.md
**Size:** ~2-3KB  
**Content:**
- Organizational Vision (Mission, Approach, Geographic Reach)
- Departments & Structure (7 departments)
- Multi-Platform Ecosystem (4 platforms)
- Core Operating Systems (RAC, CRM, Tools)
- Team Size and Demographics

#### Employee_Directory.md
**Size:** ~8-10KB  
**Content:**
- Complete directory of 32 employees
- Organized by department (HR, AI, Video, Sales, Design, Dev, LG)
- Full details: ID, name, position, location, contact (email, Telegram)
- Usage notes for participant identification

#### Project_Directory.md
**Size:** ~6-8KB  
**Content:**
- 31+ active projects with descriptions
- Project abbreviations quick reference (RH, DGN, l-gn, etc.)
- Associated resources (Figma, Google Drive, etc.)
- Keywords for project recognition
- Multi-lingual project names

#### System_Architecture.md
**Size:** ~2-3KB  
**Content:**
- Template Hierarchy (Profession → Objects → Task Templates → Actions → Tools)
- Communication Stack (Discord, Gmail, Google Workspace, Notion)
- AI Tools ecosystem (Cursor, Windsurf, Claude, ChatGPT, Midjourney, etc.)
- Architecture layers (Data, Integration, LLM, Application, Monitoring)

---

### 02-Output_Templates/ (21 Sections)

Each file contains:
- Section number and title
- Purpose description
- Output format structure
- Example entries
- Field definitions
- Usage notes

**File naming:** `NN-Section_Title.md` for sequential ordering

**Size per file:** 1-3KB each

**Special considerations:**
- Sections 17-20 are department-specific (can be loaded conditionally)
- Section 1 (Meeting Metadata) includes auto-matching instructions
- Section 4 (Projects & Features) includes project matching logic

---

### 03-Processing_Guidelines/ (Core Logic)

#### Participant_Identification.md
**Size:** ~4-5KB  
**Content:**
- 5 identification strategies (name match, context, handles, voice, multi-lingual)
- Confidence level guidelines (High/Medium/Low)
- Output format examples
- Special cases (external participants, ambiguity)
- Employee directory cross-reference

#### Project_Recognition.md
**Size:** ~3-4KB  
**Content:**
- 5 recognition strategies (direct match, abbreviations, keywords, multi-lingual, context)
- Confidence level guidelines
- Resource auto-referencing logic
- Project directory cross-reference
- Multi-lingual support (Russian/Ukrainian Cyrillic)

#### Language_Handling.md
**Size:** ~2-3KB  
**Content:**
- Supported languages (Russian, Ukrainian, English, Polish, mixed)
- Translation guidelines
- Technical term preservation
- Language preference tracking
- Multi-lingual name handling

#### Vocabulary_Recognition.md
**Size:** ~5-6KB  
**Content:**
- Lead Generation & Sales terms (Leads, Clients, Companies, Prospects, etc.)
- AI & LLM terms (Prompting, Chain of Thought, etc.)
- Design terms (Figma, UI/UX, Typography, etc.)
- Development terms (Frontend, Backend, CI/CD, etc.)
- General Business terms (Task Template, RACI, SOP, etc.)
- 636+ profession variations

#### Inference_Rules.md
**Size:** ~2-3KB  
**Content:**
- Priority inference from urgency, context, emphasis
- Status inference from verb tense, discussion context
- Owner assignment from context
- Department mapping from profession/skills
- Template alignment recognition

#### Quality_Standards.md
**Size:** ~2-3KB  
**Content:**
- What to extract (✅)
- Actions, Tasks (Action+ Object), Skills
- What NOT to include (❌)
- Comprehensiveness guidelines
- Specificity requirements
- Structure alignment with templates
- Cross-referencing rules

#### Context_Specific_Extraction.md
**Size:** ~3-4KB  
**Content:**
- Lead Generation call extraction rules
- Design call extraction rules
- Development call extraction rules
- Sales call extraction rules
- HR/Onboarding call extraction rules
- Department-specific metrics

---

### 04-Usage_Documentation/ (Guides)

#### Quick_Start_Guide.md
**Size:** ~2-3KB  
**Content:**
- Step-by-step usage (10 steps)
- Basic setup
- Input format
- Output expectations
- Common use cases

#### Example_Usage.md
**Size:** ~3-4KB  
**Content:**
- Complete example transcript
- Expected output snippets
- Good vs. poor input examples
- Output quality examples
- Edge cases

#### Tips_Best_Practices.md
**Size:** ~2-3KB  
**Content:**
- Trust the auto-matching
- Provide context hints
- Verify low confidence matches
- Use name variations
- Project abbreviations
- Multi-language tips
- Clarify external participants
- Iterate and refine

#### Advanced_Features.md
**Size:** ~3-4KB  
**Content:**
- Intelligent Participant Matching
- Intelligent Project Matching
- Template Recognition
- Cross-Department Workflow Mapping
- AI Integration Opportunities
- Knowledge Base Integration
- Performance Metrics Extraction

---

### 05-Reference_Materials/ (Supporting)

#### Glossary_Vocabulary.md
**Size:** ~6-8KB  
**Content:**
- Complete vocabulary lists (LG, LLM, Design, Development, Business)
- Term definitions
- Usage contexts
- Multi-lingual equivalents

#### Template_Structures.md
**Size:** ~2-3KB  
**Content:**
- Task Template format (Action + Object)
- Step Template format (Name, Tool, Responsibility)
- Checklist format (Name, Guide, Tools, Items, Formats, Placement)
- RACI Matrix structure
- SOP format

#### Version_History.md
**Size:** ~2-3KB  
**Content:**
- Version changelog (v2.1, v2.0, etc.)
- Changes by version
- Creation date and purpose
- Optimization notes
- Previous version references

---

### 06-Assembled_Prompts/ (Final Versions)

#### FULL_PROMPT.md
**Size:** ~45KB (reassembled from all components)  
**Content:**
- Complete prompt with all sections
- Auto-generated from modular files
- Includes all 21 output sections
- Full processing guidelines
- Complete context

#### SHORT_PROMPT.md
**Size:** ~15-20KB  
**Content:**
- Condensed version
- Essential sections only
- Abbreviated guidelines
- Streamlined for quick use

#### DEPARTMENT_SPECIFIC/ Prompts
**Size:** ~20-30KB each  
**Content:**
- Department-tailored versions
- **PROMPT_LG.md:** Lead Gen + Sales focus (includes Sections 17, 3, 4, 7, 12)
- **PROMPT_DESIGN.md:** Design focus (includes Sections 18, 4, 8, 14)
- **PROMPT_DEV.md:** Development focus (includes Sections 19, 9, 13)
- **PROMPT_HR.md:** HR/Onboarding focus (includes Sections 20, 16, 6, 11)

Each includes:
- Core context (always)
- Relevant output sections
- Department-specific guidelines
- Relevant vocabulary

---

## 🔄 Assembly Strategy

### Modular Loading
Each prompt component can be loaded conditionally:

```
ASSEMBLED_PROMPT = 
  [Company_Context] + 
  [Employee_Directory] + 
  [Project_Directory] + 
  [System_Architecture] +
  [Selected_Output_Sections] +
  [Processing_Guidelines] +
  [Usage_Instructions]
```

### Benefits
1. **Token Optimization:** Load only needed sections
2. **Department Focus:** Tailor prompts to specific use cases
3. **Maintainability:** Update individual files without breaking others
4. **Versioning:** Track changes granularly
5. **Testing:** Test individual components independently

---

## 📋 Implementation Checklist

### Phase 1: Core Context Files
- [ ] Create 01-Core_Context/ directory
- [ ] Extract Company_Context.md
- [ ] Extract Employee_Directory.md
- [ ] Extract Project_Directory.md
- [ ] Extract System_Architecture.md

### Phase 2: Output Templates
- [ ] Create 02-Output_Templates/ directory
- [ ] Split 21 sections into individual files
- [ ] Ensure consistent formatting
- [ ] Add cross-references

### Phase 3: Processing Guidelines
- [ ] Create 03-Processing_Guidelines/ directory
- [ ] Extract Participant_Identification.md
- [ ] Extract Project_Recognition.md
- [ ] Extract Language_Handling.md
- [ ] Extract Vocabulary_Recognition.md
- [ ] Extract Inference_Rules.md
- [ ] Extract Quality_Standards.md
- [ ] Extract Context_Specific_Extraction.md

### Phase 4: Usage Documentation
- [ ] Create 04-Usage_Documentation/ directory
- [ ] Create Quick_Start_Guide.md
- [ ] Create Example_Usage.md
- [ ] Create Tips_Best_Practices.md
- [ ] Create Advanced_Features.md

### Phase 5: Reference Materials
- [ ] Create 05-Reference_Materials/ directory
- [ ] Create Glossary_Vocabulary.md
- [ ] Create Template_Structures.md
- [ ] Create Version_History.md

### Phase 6: Assembled Prompts
- [ ] Create 06-Assembled_Prompts/ directory
- [ ] Create FULL_PROMPT.md (auto-assembled)
- [ ] Create SHORT_PROMPT.md
- [ ] Create DEPARTMENT_SPECIFIC/ subdirectory
- [ ] Create PROMPT_LG.md
- [ ] Create PROMPT_DESIGN.md
- [ ] Create PROMPT_DEV.md
- [ ] Create PROMPT_HR.md

### Phase 7: Integration with SummariesOct
- [ ] Cross-reference with Context/01-Company-Context.md
- [ ] Cross-reference with Context/02-Employee-Directory.md
- [ ] Cross-reference with Context/03-Project-Directory.md
- [ ] Ensure consistency with Resources/MAIN PROMPT v2.md
- [ ] Update SummariesOct/FILES.md if needed

### Phase 8: Testing & Validation
- [ ] Test each modular file independently
- [ ] Validate full assembly
- [ ] Test department-specific versions
- [ ] Verify cross-references
- [ ] Check for missing content

---

## 🎯 Success Criteria

1. ✅ All 21 output sections extracted into individual files
2. ✅ Core context split into 4 foundation files
3. ✅ Processing guidelines split into 7 modular files
4. ✅ Usage documentation created (4 files)
5. ✅ Reference materials organized (3 files)
6. ✅ Assembled prompts generated (7+ files)
7. ✅ All cross-references validated
8. ✅ Directory structure matches SummariesOct patterns
9. ✅ Each file is independently usable
10. ✅ Token optimization achieved (load only what's needed)

---

## 📊 Expected Outcomes

### Before
- **1 massive file:** 45KB, difficult to navigate
- **Maintenance:** Complex, high risk of errors
- **Customization:** All-or-nothing loading
- **Collaboration:** Merge conflicts likely

### After
- **45-50 modular files:** 1-8KB each, easy to navigate
- **Maintenance:** Simple, isolated updates
- **Customization:** Load only needed components
- **Collaboration:** Minimal conflicts, clear ownership

### Token Savings
- **Full prompt:** ~45KB → Load all
- **LG-focused prompt:** ~25KB → 44% reduction
- **Design-focused prompt:** ~20KB → 56% reduction
- **Quick reference:** ~5-10KB → 78-89% reduction

---

## 🔗 Integration Points

### With SummariesOct Structure
- **Context/**: Aligns with 01-Core_Context/
- **Resources/**: Original MAIN PROMPT v2.md remains as reference
- **Documentation/**: Can reference assembled prompts
- **Framework/**: Templates align with 05-Reference_Materials/

### With Remote Helpers Operations
- **RAC (Remote AI Context):** Modular files easier to version control
- **CRM System:** Department-specific prompts match task templates
- **Multi-Platform:** Different prompts for different platforms
- **AI Tools:** Optimized for Claude/GPT context windows

---

## 📝 Notes

- This splitting preserves ALL content from MAIN PROMPT v2.md
- No information is lost, only reorganized
- Files can be reassembled into original format
- Supports both full and partial loading
- Optimized for AI consumption and human readability
- Follows Remote Helpers' template-driven philosophy

---

## 🚀 Next Steps

1. **Review this plan** with stakeholders
2. **Approve directory structure**
3. **Begin Phase 1** (Core Context extraction)
4. **Iterate through Phases 2-6**
5. **Test assembled prompts**
6. **Deploy to production use**
7. **Update documentation** (SummariesOct/FILES.md)
8. **Train team** on modular prompt usage

---

**Plan Status:** ✅ READY FOR IMPLEMENTATION

**Estimated Time:** 2-3 hours for complete splitting and assembly  
**Complexity:** Medium (structured extraction, careful organization)  
**Risk:** Low (all content preserved, reversible changes)

---

**Last Updated:** November 5, 2025  
**Created By:** AI Assistant (Claude)  
**For:** Remote Helpers - Nov25 Folder Organization
