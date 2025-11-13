# Task Breakdown - November 5, 2025

## Instructions
**What**: Detailed action steps
**Include**:
- Break each plan item into specific steps
- Add links and resources
- Clear instructions for execution

---

## Task 1: Video Generation for Claude Code Tutorial (COMPLETED)

### Steps:
1. Continue from previous day's file collection
2. Generate new video files in NotebookLM
3. Review generated video content
4. Insert video into the lesson page
5. Verify video playback and quality

### Status: COMPLETED (7:00-7:35)

### Resources and Links:
- NotebookLM Chat: https://notebooklm.google.com/notebook/e6c6ffd4-f326-42fe-b7ee-302a12ee93af
- Lesson URL: https://oa-y.com/lessons/claude-code-for-vs-code-quick-start-guide

### Outcomes:
- New video files generated successfully
- Video reviewed and approved
- Video inserted into lesson page
- Tutorial now complete with video content

---

## Task 2: Resume Parser for Talents - Edit Mode Development (IN PROGRESS)

### Steps:
1. Review current implementation (create mode only)
2. Analyze data overwriting risks in edit mode
3. Design validation logic to prevent data loss
4. Implement check for existing data
5. Send existing data to AI for comparison
6. Prevent overwriting of already-filled fields
7. Test with various scenarios (empty fields, partial data, full data)
8. Make decision: enable button for all modes or keep create-only

### Status: IN PROGRESS (7:35-9:50)

### Resources and Links:
- Current implementation: Job Application Resume Parser
- Target module: Talents service

### Instructions:

**Current Implementation:**
- Resume Parser button displayed only in CREATE mode
- Hidden in EDIT mode to prevent accidental data overwriting
- Logic: `if (mode === 'create') { show button }`

**Design Considerations:**
- **Risk:** In edit mode, parser could overwrite manually entered data
- **Solution Options:**
  1. Keep create-only (current, safer approach)
  2. Add validation: send existing data + new resume to AI for smart merging
  3. Only fill empty fields, preserve filled ones

**Next Steps:**
1. Decide on approach after discussing with team
2. If enabling edit mode:
   - Implement existing data collection
   - Send to AI with instructions: "Don't overwrite filled fields"
   - Add confirmation dialog before applying changes
3. Test thoroughly before enabling in production

**Decision Point:**
- Currently: Button only in CREATE mode (safer, prevents data loss)
- Future consideration: Add smart validation for EDIT mode

---

## Task 3: LG Extension Troubleshooting (COMPLETED)

### Steps:
1. Receive report from LG team about extension errors
2. Investigate error messages and symptoms
3. Identify root cause (extension cache/crash issue)
4. Advise solution (restart extension)
5. Verify issue resolved

### Status: COMPLETED (9:50-10:10)

### Outcomes:
- Problem diagnosed quickly
- Extension was cached/frozen - resolved by restart
- LG team unblocked and working again
- 20-minute resolution time

---

## Task 4: Designer Onboarding & Call (COMPLETED)

### Steps:
1. Participate in call with designers
2. Discuss website design goals and objectives
3. Provide technical input on feasibility

### Status: COMPLETED (10:40-12:40)

### Outcomes:
- Key question identified: "What is the goal of this website?"
- Technical perspective provided to design team

---

## Task 5: Call with Olya (COMPLETED)

### Steps:
1. Participate in extended call with Olya
2. Discuss ongoing projects and priorities
3. Align on next steps

### Status: COMPLETED (10:40-12:40)

### Outcomes:
- Project alignment achieved
- Priorities clarified

---

## Task 6: Client Project MVP Planning with Stas (COMPLETED)

### Steps:
1. Join call with Stas
2. Discuss client project requirements
3. Define MVP scope and features
4. Agree on timeline and deliverables

### Status: COMPLETED (15:00)

### Outcomes:
- Decision: Build MVP for client
- Scope defined
- Next steps identified

---

## Task 7: Table Parsing for Excel Export (PLANNED)

### Steps:
1. Analyze table structure that needs to be parsed
2. Design parsing logic to extract data
3. Implement button to trigger parsing
4. Format data for Excel compatibility
5. Test export functionality
6. Validate data accuracy after export

### Status: PLANNING

### Instructions:

**Goal:** Create a button that can parse a table and provide data ready for pasting into Excel

**Requirements:**
- Parse table structure (rows, columns)
- Extract all data accurately
- Format for Excel (tab-separated or CSV)
- Provide copy-to-clipboard functionality
- Handle special characters and formatting

**Use Cases:**
- Quick data extraction from web tables
- Easy Excel integration
- Reduce manual copy-paste errors

---

## Recurring Tasks

### Add "reason" field to status change modal (PENDING)
**Status:** Carried over from Nov 4
**Priority:** High
**Note:** Still in queue, needs to be scheduled

### Resume Parser Edit Mode Validation (PENDING)
**Status:** In progress, needs decision
**Priority:** High
**Note:** Blocked on design decision - safety vs. functionality

---

## Reminder
- Break down each plan into steps
- Add all necessary links and resources
- Write clear execution instructions
- Update status as tasks progress
