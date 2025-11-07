# Team Performance Analysis Prompt - LG Nov25 Department

**Purpose:** Comprehensive guide for analyzing daily team performance  
**Date:** November 6, 2025 (Yesterday)  
**Department:** LG Nov25 (Lead Generation)  
**Created:** November 7, 2025

---

## Analysis Objective

Analyze the LG Nov25 team's performance for November 6, 2025, by examining all employee daily logs, plans, and task completion reports to provide a comprehensive performance overview.

---

## Data Sources to Examine

### Primary Files (Per Employee)
1. **daily.md** - Daily activity log with timestamps, activities, transcripts, outcomes
2. **plans.md** - Daily plan showing intended tasks and goals
3. **task.md** - Task completion report showing completed work

### Employee Folders to Review
- All employee folders in `LG Nov25/` directory
- Focus on `06/` subfolder (November 6, 2025)
- Exclude `Left/` folder (former employees)
- Exclude `Projects/` folder (project-specific, not daily performance)

### Supporting Files
- `Profile*.md` files - Employee profiles for context (profession, skills, status)
- `DEPARTMENT_GUIDE.md` - Department standards and metrics
- `LG Department Tasks - November 2025.md` - Department-wide priorities

---

## Key Metrics to Extract and Count

### 1. Activity Metrics

**Daily Activity Volume:**
- Total number of activities logged per employee
- Number of activities with completed outcomes vs. incomplete
- Activities with Whisper Flow transcripts vs. without transcripts
- Time range of activities (earliest start, latest end)

**Activity Types:**
- Lead generation activities (prospecting, research, outreach)
- Data entry/management activities
- Strategy documentation activities
- Research activities (e.g., China market research)
- Administrative activities
- Meeting/call activities
- Other activities

### 2. Task Completion Metrics

**Planned vs. Completed:**
- Number of tasks planned in `plans.md`
- Number of tasks completed (from `task.md`)
- Completion rate per employee (%)
- Tasks marked as incomplete or pending

**Task Categories:**
- Lead identification/research tasks
- Outreach tasks (emails, LinkedIn, calls)
- Data entry/CRM tasks
- Strategy documentation tasks
- Research tasks
- Administrative tasks
- Other tasks

### 3. Lead Generation Specific Metrics

**Lead Generation Activities:**
- Number of leads identified/researched
- Number of outreach attempts (emails sent, LinkedIn messages, calls)
- Number of responses received
- Number of appointments scheduled
- Number of qualified leads
- Lead sources identified (LinkedIn, databases, etc.)

**Outreach Volume:**
- Emails sent
- LinkedIn connection requests
- LinkedIn messages/InMails
- Phone calls made
- Follow-up messages sent

**Engagement Metrics:**
- Response rate (%)
- Positive responses
- Negative responses
- No responses
- Meeting/appointment booking rate

### 4. Quality Indicators

**Documentation Quality:**
- Activities with detailed descriptions
- Activities with outcomes documented
- Activities with transcripts included
- Activities with timestamps
- Completeness of daily logs

**Strategic Work Indicators:**
- Strategy documentation activities
- Research activities (beyond data entry)
- Analysis and reporting activities
- Process improvement activities

**Compliance with Standards:**
- Following daily log format
- Including Whisper Flow transcripts
- Documenting outcomes
- Updating files throughout the day

### 5. Employee Status & Availability

**Active Employees:**
- Employees with activity on November 6
- Employees with no activity (missing daily.md or empty)
- Employees with partial activity (incomplete logs)

**Employee Status (from Profile files):**
- Available
- Project
- Work
- Part Time
- On Leave
- LEFT (exclude from analysis)

**Shift Coverage:**
- Day shift employees active
- Night shift employees active
- Shift distribution

### 6. Department Priorities Alignment

**Critical Tasks (from LG Department Tasks document):**
- Strategy documentation progress (Burda Anna, Shkinder Kseniia)
- China market research (Hanan Zaheur - 1 hour/day)
- Analytics transition activities
- File system training completion
- Other department priorities

**Work Focus:**
- Data entry activities (to be reduced)
- Strategic work activities (to be increased)
- Research activities
- Documentation activities

---

## Details to Look Up

### Per Employee Analysis

**1. Employee Profile Context:**
- Name and ID
- Profession(s) - Lead generator, Translator, Sales Manager, etc.
- Status - Available, Project, Work, Part Time, On Leave
- Shift - Day or Night
- Skills and capabilities

**2. Daily Activity Breakdown:**
- All activities with timestamps
- What was worked on
- Whisper Flow transcripts (if any)
- Outcomes and results
- Time spent per activity (if available)

**3. Plan vs. Execution:**
- Planned tasks from `plans.md`
- Completed tasks from `task.md`
- Tasks not completed
- Reasons for non-completion (if documented)

**4. Specific Accomplishments:**
- Leads generated
- Outreach volume
- Responses received
- Appointments scheduled
- Documents created
- Research completed
- Other measurable outputs

**5. Issues or Challenges:**
- Missing documentation
- Incomplete logs
- No activity recorded
- Technical issues mentioned
- Blockers or dependencies

### Department-Wide Analysis

**1. Overall Activity Level:**
- Total employees with activity
- Total activities logged
- Total tasks completed
- Average activities per active employee
- Average completion rate

**2. Lead Generation Performance:**
- Total leads identified
- Total outreach attempts
- Total responses
- Total appointments scheduled
- Overall response rate
- Overall conversion rate

**3. Strategic Work Progress:**
- Strategy documentation activities
- Research activities
- Analysis activities
- Documentation quality

**4. Department Priorities Status:**
- Progress on critical tasks
- Alignment with department goals
- Work focus (data entry vs. strategic)

**5. Team Engagement:**
- Employees following documentation standards
- Employees with complete logs
- Employees with transcripts
- Employees documenting outcomes

---

## Analysis Structure

### Report Sections

**1. Executive Summary**
- Overall performance snapshot
- Key metrics overview
- Highlights and concerns

**2. Department-Wide Metrics**
- Activity volume
- Task completion rates
- Lead generation metrics
- Strategic work indicators

**3. Individual Employee Performance**
- Per employee breakdown
- Activity volume
- Task completion
- Specific accomplishments
- Issues or gaps

**4. Lead Generation Performance**
- Outreach volume
- Response rates
- Appointment booking
- Lead quality indicators

**5. Strategic Work Analysis**
- Strategy documentation progress
- Research activities
- Analysis and reporting
- Process improvement

**6. Compliance & Documentation Quality**
- Log completeness
- Transcript inclusion
- Outcome documentation
- Format compliance

**7. Department Priorities Alignment**
- Critical tasks progress
- Work focus analysis
- Priority alignment

**8. Recommendations**
- Areas for improvement
- Best practices observed
- Action items
- Follow-up needed

---

## Counting Methodology

### Activity Counting Rules

**Count as ONE Activity:**
- Each timestamped activity entry in `daily.md`
- Each distinct task in `task.md`
- Each planned item in `plans.md`

**Activity Categories:**
- Categorize each activity based on description
- Use keywords: "lead", "outreach", "email", "LinkedIn", "research", "data entry", "strategy", "documentation", "meeting", "call", etc.

**Lead Generation Counting:**
- Count each lead identified/researched
- Count each outreach attempt (email, LinkedIn message, call)
- Count each response received
- Count each appointment scheduled
- Extract numbers from descriptions (e.g., "sent 15 emails" = 15 outreach attempts)

### Task Completion Counting

**Completed Tasks:**
- Tasks marked as completed in `task.md`
- Tasks with outcomes documented in `daily.md`
- Tasks explicitly stated as finished

**Incomplete Tasks:**
- Tasks in `plans.md` not found in `task.md`
- Tasks mentioned but not completed
- Tasks marked as pending or incomplete

**Completion Rate:**
- (Completed Tasks / Planned Tasks) × 100
- Handle division by zero (no planned tasks = N/A)

### Quality Scoring

**Documentation Quality Score (per employee):**
- +1 point: Has daily.md file
- +1 point: Has activities logged
- +1 point: Has timestamps
- +1 point: Has outcomes documented
- +1 point: Has transcripts included
- +1 point: Has plans.md file
- +1 point: Has task.md file
- Maximum: 7 points

**Activity Detail Score:**
- +1 point: Detailed description
- +1 point: Clear outcomes
- +1 point: Time spent mentioned
- +1 point: Results quantified
- Maximum: 4 points per activity

---

## Special Considerations

### Missing Data Handling

**Empty Files:**
- If `daily.md` is empty or template only → No activity recorded
- If `plans.md` is empty → No plan documented
- If `task.md` is empty → No tasks completed or documented

**Incomplete Logs:**
- Activities without outcomes → Count as incomplete
- Activities without timestamps → Note as incomplete documentation
- Activities without transcripts → Note missing transcript

### Employee Status Handling

**Exclude from Analysis:**
- Employees in `Left/` folder
- Employees with Status: "LEFT" in profile
- Project-specific folders (Projects/)

**Include with Notes:**
- Employees with Status: "On Leave" → Note but include if activity exists
- Employees with Status: "Part Time" → Include, note part-time status
- Employees with no activity → Include in summary, note inactivity

### Date Verification

**Confirm Date:**
- Verify folder is `06/` (November 6, 2025)
- Check file headers for date confirmation
- Note any date discrepancies

---

## Output Format Requirements

### Metrics Summary Table

| Metric | Value | Notes |
|--------|-------|-------|
| Total Active Employees | X | Employees with activity |
| Total Activities Logged | X | All activities across team |
| Total Tasks Completed | X | Completed tasks |
| Average Completion Rate | X% | Team average |
| Total Leads Identified | X | Leads researched/found |
| Total Outreach Attempts | X | Emails, LinkedIn, calls |
| Total Responses | X | Responses received |
| Total Appointments | X | Appointments scheduled |
| Response Rate | X% | Responses / Outreach |
| Strategy Work Activities | X | Strategic activities |

### Employee Performance Table

| Employee Name | Activities | Tasks Completed | Leads | Outreach | Responses | Appointments | Quality Score | Status |
|---------------|------------|-----------------|-------|----------|-----------|--------------|---------------|--------|
| Name 1 | X | X/Y | X | X | X | X | X/7 | Available |
| Name 2 | X | X/Y | X | X | X | X | X/7 | Available |

### Activity Breakdown Table

| Activity Type | Count | % of Total |
|--------------|-------|------------|
| Lead Generation | X | X% |
| Data Entry | X | X% |
| Strategy Documentation | X | X% |
| Research | X | X% |
| Administrative | X | X% |
| Meetings/Calls | X | X% |
| Other | X | X% |

---

## Analysis Checklist

Before finalizing analysis, verify:

- [ ] All employee folders checked (except Left/ and Projects/)
- [ ] All `06/` subfolders examined
- [ ] All `daily.md` files read
- [ ] All `plans.md` files read
- [ ] All `task.md` files read
- [ ] All Profile files checked for employee status
- [ ] All metrics counted accurately
- [ ] All activities categorized correctly
- [ ] All tasks matched between plans and completion
- [ ] All lead generation activities quantified
- [ ] All quality scores calculated
- [ ] All missing data noted
- [ ] All recommendations provided
- [ ] Report formatted clearly

---

## Notes for Analysis

**Context Awareness:**
- Department is under evaluation (from LG Department Tasks document)
- Focus shifting from data entry to strategic work
- Critical priorities: Strategy documentation, China research, Analytics transition
- Team size: 11 employees
- Financial context: $5,000/month department cost

**Performance Expectations:**
- Daily activity logging expected
- Whisper Flow transcripts expected for meetings
- Outcome documentation expected
- Task completion tracking expected
- Strategic work prioritized over data entry

**Success Indicators:**
- High activity volume
- Complete documentation
- Strategic work activities
- Lead generation results
- Task completion rates
- Quality documentation

---

**End of Analysis Prompt**

