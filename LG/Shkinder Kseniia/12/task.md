# Lead Generation Department - Detailed Action Plan & Instructions

## Overview
This document contains a comprehensive breakdown of all projects, tasks, and procedures discussed in the team meeting. Follow these instructions step-by-step to ensure proper execution of all departmental initiatives.

---

## PART 1: DAILY MANAGEMENT TASKS

### 1.1 Morning Review - Newcomers and Juniors Check

#### **Objective**: Monitor team members' progress and provide necessary support

**Steps:**
1. **Review Newcomer Cards**
   - Open team tracking system
   - Check each newcomer's progress
   - Review task completion status
   - Identify any blockers or issues
   - Document areas needing support

2. **Review Junior Employee Cards**
   - Check current assignments
   - Assess work quality
   - Track skill development
   - Note performance concerns or achievements

3. **LinkedIn Profile Review**
   - Verify professional profiles are complete
   - Check company affiliation is correct
   - Review recent activity
   - Ensure brand compliance

4. **Messages Review**
   - Check internal messaging systems (Slack, Teams, etc.)
   - Review emails from team members
   - Respond to pending questions
   - Follow up on previous conversations
   - Document action items

### 1.2 Manager Information Update

**Steps:**
1. Compile comprehensive reports for each team member including:
   - Performance metrics
   - Progress updates
   - Attendance and engagement
   - Challenges identified
   - Achievements
   - Recommended next steps

2. Format reports using standardized templates
3. Send to respective managers
4. Be available for follow-up discussions

### 1.3 Previous Day Statistics Review (New Strategy)

**Steps:**
1. Access analytics dashboard
2. Review KPIs:
   - Productivity metrics
   - Engagement metrics
   - Learning metrics
   - Team collaboration
3. Compare against previous strategy metrics
4. Document findings and trends
5. Prepare recommendations for optimization

### 1.4 Working Hours Assistance

**Provide continuous support including:**
- General guidance and problem-solving
- Technical assistance (software, hardware, access issues)
- Training and documentation
- Proactive check-ins

---

## PART 2: MAJOR PROJECTS

### PROJECT 1: Building the Knowledge Base (AI-Powered Department Brain)

#### **Project Goal**:
Create a comprehensive, organized library of all instructions, templates, and knowledge that can be processed by AI (VS Code, Cursor, Claude, GPT) to assist with department management, analysis, and optimization.

#### **Why This Matters:**
VS Code/Cursor with AI becomes your assistant that helps you:
- Control and analyze everything
- Send recommendations for improvements
- Automate routine tasks
- Provide intelligent suggestions

**For this, the AI needs "brains" = all your knowledge and instructions loaded properly.**

---

#### **MILESTONE 1: Download and Organize All Instructions**

##### **Step 1.1: Set Up Your Environment**

**Required Tools:**
- VS Code installed and configured
- Cursor installed
- Access to Claude
- Access to GPT
- Dropbox access to Lead Generation folders

**Folder Structure Setup:**
```
Dropbox/
├── LG November/
│   ├── LG Department/
│   │   ├── Instructions/
│   │   ├── Prompt/
│   │   └── Team Leads/
│   ├── Online Academy/
│   └── Libraries/
│       └── professions/
```

##### **Step 1.2: Download Instructions from Google Drive**

**Actions:**
1. Go to Google Drive
2. Search for "LG" (Lead Generation)
3. Identify all relevant folders:
   - LG Teacher
   - LG Knowledge
   - LG Custom Projects
   - Message templates
   - Queries
   - Any other LG-related content

**Download Process for Each Document:**
1. Open the document/file
2. Click File → Download
3. Select format: **Markdown** (preferred for AI processing)
4. Save location: `Dropbox/LG November/LG Department/Instructions/`
5. Use descriptive filenames

**Organize by Categories:**
After downloading, create subcategories:
- `/Instructions/Messaging/` - all message templates and rules
- `/Instructions/Processes/` - workflow and procedures
- `/Instructions/Training/` - training materials
- `/Instructions/Templates/` - reusable templates

##### **Step 1.3: Download from Custom GPT Configurations**

**What to Extract:**
- Custom instructions from GPT configurations
- Prompts used in custom GPTs
- Rules and guidelines

**How to Download:**
1. Open each Custom GPT
2. Go to Settings
3. Copy custom instructions
4. Save as Markdown files in `Instructions/` folder
5. Name files clearly (e.g., `custom-gpt-messaging-instructions.md`)

##### **Step 1.4: Set Up VS Code/Cursor Integration**

**Configure Dropbox Access in VS Code:**
1. Open VS Code/Cursor
2. Click File → Add Folder to Workspace
3. Navigate to `Dropbox/LG November/LG Department/`
4. Right-click on the folder
5. Select "Pin to Quick Access" (for Windows) or add to favorites

**Link Professions Library:**
1. Locate the `professions` folder in libraries
2. Copy the relative path: `Dropbox/libraries/professions`
3. Open the prompt file: `LG Department/Prompt/legend.md` (or similar)
4. Find line 25 (or the line with "Use only approved professions")
5. Add the reference: `Dropbox/libraries/professions`
6. Save (Ctrl+S)

##### **Step 1.5: Configure AI Prompts**

**Edit the Main Prompt File:**

Location: `LG Department/Prompt/` folder

**Key sections to verify/update:**
```markdown
# Lead Generation Instructions

## Message Rules
- No AI clichés
- No empty promises
- No word repetition
- No surprise website links (only in first message)
- No farewell with "single kind regards" etc.
- Use only approved professions and departments

## Professions Reference
See list: Dropbox/libraries/professions

## Message Structure
[Define structure here]

## Research Observations
[Guidelines for research]

## Specialist Solutions
[Solutions approach]
```

---

#### **MILESTONE 2: Organize and Structure the Knowledge Base**

##### **Task: Assign a Dedicated Team Member**

**Profile Needed:**
- Curious and loves to read
- Interested in AI technology
- Quick learner
- Attention to detail
- Someone who has experience writing research papers or thesis
- Willing to do administrative tasks

**Adjust their workload:**
- Reduce their regular quota
- Assign them to administrative/knowledge management tasks

##### **Task: Create "School Library" Organization**

**Requirements:**
Everything should be organized neatly like a school library:
- Clear folder structure
- Consistent naming conventions
- Easy to find and navigate
- Categorized by topic
- Tagged appropriately

**Organization Process:**
1. **Create Main Categories:**
   ```
   Instructions/
   ├── 01-Messaging/
   ├── 02-LinkedIn-Strategy/
   ├── 03-Research-Methods/
   ├── 04-Client-Communication/
   ├── 05-Tools-and-Software/
   ├── 06-Templates/
   └── 07-Best-Practices/
   ```

2. **Within Each Category:**
   - Create subcategories as needed
   - Use numbered prefixes for sequence (01-, 02-, etc.)
   - Include README.md files explaining category contents

3. **Naming Conventions:**
   - Use lowercase
   - Use hyphens instead of spaces
   - Be descriptive: `first-message-template.md` not `template1.md`
   - Include version dates if relevant: `messaging-guide-2025-11.md`

##### **Task: AI Processing Preparation**

**Create Metadata Files:**
For each major category, create an `index.md` file:

```markdown
# Category: LinkedIn Messaging

## Contents
- first-message-template.md - Template for initial outreach
- follow-up-template.md - Template for follow-up messages
- response-handling.md - How to handle client responses

## Purpose
Templates and guidelines for LinkedIn messaging

## Last Updated
2025-11-11

## Tags
#messaging #linkedin #templates
```

**Create Rules Document:**
Document how the knowledge base should be:
- Updated (who, when, how)
- Maintained (review cycles, quality checks)
- Used (access permissions, best practices)
- Expanded (how to add new content)

---

#### **MILESTONE 3: AI Integration and Testing**

##### **Task: Load Knowledge into AI Tools**

**For Claude/GPT/Cursor:**
1. Create master prompts that reference the knowledge base
2. Test with sample queries
3. Refine based on results
4. Document what works best

**For VS Code/Cursor:**
1. Configure workspace settings to include all relevant folders
2. Set up keyboard shortcuts for common tasks
3. Create snippets for frequently used templates

##### **Task: Create AI Usage Guidelines**

Document how team members should:
- Use AI to find information
- Ask questions effectively
- Interpret AI responses
- Verify AI suggestions
- Report issues or improvements

---

### PROJECT 2: Message Export Analysis

#### **Project Goal**:
Analyze successful LinkedIn messages to identify patterns, improve templates, and build a data-driven messaging strategy.

#### **Success Criteria:**
Messages are considered successful if:
- Client responded
- Call/meeting was scheduled

---

#### **MILESTONE 1: Data Collection**

##### **Step 2.1: Locate Message Exports**

**Where to Find:**
```
General Dropbox/
└── Archive/
    └── LinkedIn Accounts Export/
```

**Look for exports from successful team members:**
- Svetlana (много назначала звонков - scheduled many calls)
- Marina
- Other top performers

##### **Step 2.2: Extract Successful Messages**

**Process:**
1. Open each export file
2. Filter for messages with:
   - Responses from clients
   - Scheduled meetings/calls
3. Extract only the message content (not metadata initially)
4. Create a new file: `successful-messages-compilation.md`

**Export Format:**
For each message, capture:
```markdown
## Message ID: [unique-id]
**Account**: [account name]
**Date**: [date]
**Outcome**: [Response/Meeting Scheduled]
**Industry**: [client industry]
**Company Size**: [if available]
**Country**: [if available]

### Message Content:
[full message text]

---
```

##### **Step 2.3: Organize by Categories**

Create separate files for:
- `first-messages-successful.md`
- `follow-up-messages-successful.md`
- `response-handling-successful.md`

---

#### **MILESTONE 2: Data Enrichment**

##### **Step 2.4: Add CRM Data**

**For each successful message, add:**
- Country/Region
- Industry/Sector
- Company size
- Job title/role of recipient
- Project outcome (if available)

**This can be partially automated:**
- Use CRM exports
- Match by account/contact name
- Fill in data using AI assistance

##### **Step 2.5: Categorize Message Components**

**For each message, identify and tag:**

1. **Greeting Section**
   - How did we start?
   - Personalization used?

2. **Value Proposition**
   - What did we offer?
   - How was it framed?

3. **Social Proof/Credibility**
   - What evidence did we provide?
   - Companies mentioned?
   - Results mentioned?

4. **Call to Action**
   - How did we ask?
   - What was requested?

5. **Closing**
   - How did we end?
   - Tone used?

**Create Tagged Version:**
```markdown
[GREETING]
Hi [Name],
[/GREETING]

[VALUE_PROP]
I noticed your company is expanding in [region]...
[/VALUE_PROP]

[SOCIAL_PROOF]
We've helped companies like [Company X] achieve [Result Y]
[/SOCIAL_PROOF]

[CTA]
Would you be open to a brief call next week?
[/CTA]

[CLOSING]
Best regards,
[/CLOSING]
```

---

#### **MILESTONE 3: Analysis and Pattern Recognition**

##### **Step 2.6: AI-Powered Analysis**

**Create Analysis Prompts for AI:**

1. **Greeting Analysis:**
   ```
   Analyze all [GREETING] sections from successful messages.
   Identify:
   - Most common patterns
   - Personalization techniques
   - Length preferences
   - Tone variations
   ```

2. **Value Proposition Analysis:**
   ```
   Analyze all [VALUE_PROP] sections.
   Identify:
   - Most effective frameworks
   - Industries where specific approaches work best
   - Length and structure patterns
   ```

3. **Question/Response Analysis:**
   - What questions did clients ask?
   - How did we respond effectively?
   - Common objections and successful responses

**Run these analyses and document findings.**

##### **Step 2.7: Statistical Analysis**

**Create Reports:**
1. **Success Rate by Industry**
   - Which industries respond best?
   - What messaging works in each?

2. **Success Rate by Region**
   - Geographic patterns
   - Cultural adaptations needed

3. **Success Rate by Company Size**
   - SMB vs Enterprise messaging differences

4. **Message Length Analysis**
   - Optimal length for first message
   - Optimal length for follow-ups

5. **Response Time Analysis**
   - When do people respond?
   - Optimal follow-up timing

---

#### **MILESTONE 4: Template Improvement and FAQ Creation**

##### **Step 2.8: Update Templates**

Based on analysis findings:
1. Update existing message templates
2. Create industry-specific variations
3. Create region-specific variations
4. Document when to use each variation

##### **Step 2.9: Create FAQ Database**

**Structure:**
```markdown
# FAQ: Client Questions and Proven Responses

## Category: Pricing Questions

### Q: How much does this cost?
**Context**: Early in conversation
**Proven Response**: [Best performing response from data]
**Success Rate**: [X%]

**Context**: After demonstrating value
**Proven Response**: [Best performing response from data]
**Success Rate**: [X%]

## Category: Timeline Questions
[...]
```

##### **Step 2.10: Build Department Brain**

**Integration:**
Combine all findings into the knowledge base so AI can:
- Suggest best message templates based on context
- Recommend responses to client questions
- Identify patterns in new messages
- Continuously improve recommendations

---

### PROJECT 3: Online Academy Management and Updates

#### **Project Goal**:
Maintain and update the Online Academy content to ensure team members have current, accurate training materials.

---

#### **MILESTONE 1: Access and Setup**

##### **Step 3.1: Get Access to Online Academy**

**Platforms:**
1. Online Academy website (login required)
2. Dropbox folder: `Online Academy/`

**Share Access:**
1. Request access from administrator
2. Accept invitation
3. Verify login works

##### **Step 3.2: Download Academy Content**

**From Website:**
1. Navigate to each course/module
2. Use browser extension or download feature
3. Save as Markdown to: `Dropbox/Online Academy/Courses/`

**From Dropbox:**
1. Accept shared folder invitation
2. Open in VS Code/Cursor
3. Pin to quick access

---

#### **MILESTONE 2: Content Review and Organization**

##### **Step 3.3: Audit Current Content**

**For Each Course:**
1. Open course page
2. Review all modules
3. Check all lessons
4. Document:
   - What exists (even if just titles)
   - What has full content
   - What is outdated
   - What is missing

**Create Audit Document:**
```markdown
# Online Academy Content Audit - 2025-11-11

## Course 1: [Course Name]

### Module: LinkedIn Messaging
**Lessons:**
- ✅ First Message - COMPLETE, needs update
- ✅ Second Message - COMPLETE, current
- ⚠️ Follow-up Strategy - TITLE ONLY, no content
- ❌ Response Handling - MISSING

**Status**: 50% complete, 25% outdated
**Priority**: High - core skill

### Module: Lead Status Management
**Lessons:**
- ✅ Status Overview - COMPLETE, current
- ⚠️ CRM Integration - OUTDATED (pre-2024)
[...]
```

##### **Step 3.4: Identify Priority Updates**

**Categorize by Urgency:**

**HIGH PRIORITY (Update within 1 week):**
- Core skills used daily
- Outdated information causing confusion
- Missing content for critical processes

**MEDIUM PRIORITY (Update within 1 month):**
- Important but not daily-use
- Partially complete content
- Enhancement opportunities

**LOW PRIORITY (Update when possible):**
- Nice-to-have content
- Advanced topics
- Supplementary materials

---

#### **MILESTONE 3: Content Updates**

##### **Step 3.5: Update Outdated Content**

**Example: LinkedIn Messaging Module**

**Current Issues:**
- Old message templates
- Outdated platform features
- Missing new best practices

**Update Process:**
1. Review current lesson content
2. Compare with latest instructions from Project 1
3. Incorporate findings from Project 2 (message analysis)
4. Update with screenshots if needed
5. Add video if applicable
6. Test with team members
7. Publish updates

**Documentation:**
Keep track in: `academy-updates-log.md`
```markdown
# Update Log

## 2025-11-11: LinkedIn Messaging Module

**What Changed:**
- Updated first message template based on analysis
- Added industry-specific examples
- Removed outdated features
- Added new compliance guidelines

**Updated By**: [Name]
**Reviewed By**: [Name]
**Status**: Published
```

##### **Step 3.6: Create Missing Content**

**For lessons that exist as titles only:**
1. Define learning objectives
2. Outline content structure
3. Write content using findings from Projects 1 & 2
4. Add examples and exercises
5. Include assessments/tests
6. Review and publish

##### **Step 3.7: Organize with Hashtags/Tags**

**Tagging System:**
```markdown
#lead-generation #messaging #linkedin #template #2025

Course: LinkedIn Messaging Mastery
Level: Beginner
Duration: 2 hours
Prerequisites: Basic LinkedIn knowledge
```

**This helps with:**
- Searchability
- Filtering content
- Recommending related courses
- AI processing

---

#### **MILESTONE 4: Integration and Maintenance**

##### **Step 3.8: Link to Knowledge Base**

**Cross-Reference:**
- Link academy content to Instructions folder
- Ensure consistency between training and practice
- Update both when changes occur

**Example:**
```markdown
# Lesson: First Message Templates

## Content
[Lesson content here]

## Related Resources
- See also: `/Instructions/Messaging/first-message-template.md`
- Practice: [Link to practice exercises]
- Latest guidelines: [Link to current instructions]
```

##### **Step 3.9: Create Update Schedule**

**Regular Review Cycle:**
- Weekly: Check for urgent updates needed
- Monthly: Review one complete course
- Quarterly: Full academy audit
- Annually: Major refresh

**Assign Responsibility:**
- Content owner for each course
- Review committee
- Update workflow

##### **Step 3.10: Extract and Save Content**

**What to Extract:**
From online academy courses like "Lead Status Management":

1. **Lesson Content:**
   - Full text of lessons
   - Instructions and guidelines
   - Examples and case studies

2. **Format for Saving:**
   ```markdown
   # Course: [Course Name]
   ## Module: [Module Name]
   ### Lesson: Lead Status Management

   #### Content:
   [Full lesson text]

   #### Key Takeaways:
   - [Point 1]
   - [Point 2]

   #### Examples:
   [Examples from lesson]

   #### Practice Exercises:
   [If available]
   ```

3. **Save Location:**
   `Dropbox/Online Academy/Courses/[course-name]/[module-name]/lesson-[name].md`

**Why This Matters:**
This content needs to be:
- Combined with instructions
- Processed by AI
- Referenced quickly
- Kept up to date

**Integration Goal:**
Academy content + Instructions + Successful message analysis = Complete department knowledge that AI can use to:
- Guide team members
- Answer questions
- Suggest improvements
- Maintain quality

---

## PART 3: TEAM MANAGEMENT EXPECTATIONS

### 3.1 Desired Team Profile

**We want people who are:**
- Energetic with technology ("бодрячком с технологией")
- Fast learners who grasp concepts quickly
- Love to read and learn
- Curious and interested in new topics
- Think critically and analyze
- Contribute ideas
- Execute quickly (not slowly over weeks)

**With this team, things will move forward rapidly.**

### 3.2 Performance Criteria

**Evaluation Points:**

1. **Responsibility Over Desire**
   - Desire is great, but requires decisiveness
   - Responsibility makes you show up at 9 AM regardless of:
     - Weather
     - Mood
     - Season
     - Personal feelings
   - Desire alone is insufficient

2. **Quick Adoption**
   - Can't spend weeks on simple tasks
   - "You installed VS Code? Come on!" - should be fast
   - Time should be spent on development, not verification

3. **Understanding from First Explanation**
   - Should remember from first call
   - Better yet: take notes (you can't remember everything)
   - Read what was written and follow it
   - Much communication will be via documents, not voice calls
   - Must be able to:
     - Read documentation carefully
     - Follow written instructions
     - Execute while referencing docs
     - Master after first repetition

### 3.3 Current Team Decisions

**Newcomers/Juniors Under Review:**
- Give them a chance, but later (not now)
- Time between attempts must pass
- Next onboarding: when available (Monday/Tuesday)
- If they're free and we have capacity: one of the two
- Focus now on development, not constant checking

**Testing Period:**
- Check tomorrow if they meet criteria
- If yes: continue
- If no: may need to wait for next onboarding cycle

### 3.4 Training and Knowledge Transfer

**Tomorrow's Schedule (Example):**
- 11:00 AM: Call/training session
- 14:00-15:00: Next session
- Deadline: Must come with results

**Training Approach:**
1. **First Training (Today):**
   - Explain everything
   - Demonstrate processes
   - Record if possible

2. **Practice Assignment:**
   - Before 11 AM tomorrow: Ksenia teaches Dana
   - Dana must be able to demonstrate what she learned
   - "Relay race" approach - passing knowledge forward

3. **Expectations:**
   - AI tools work fast (15 minutes per iteration)
   - Must come prepared with results
   - Must read written materials
   - "Estafeta" (relay) - when you receive tasks, execute and pass forward

**Key Principle:**
- We're stretched thin ("загибаемся")
- Can't spend time on basics
- Need to move at rapid pace ("семимильными шагами")
- Everyone must keep up

---

## PART 4: TECHNICAL PROCEDURES

### 4.1 Working with Dropbox in VS Code/Cursor

**Initial Setup:**
1. Install VS Code or Cursor
2. Sign into Dropbox
3. Ensure Dropbox folder is synced locally

**Adding Folders:**
1. Open VS Code/Cursor
2. File → Add Folder to Workspace
3. Navigate to `Dropbox/LG November/LG Department/`
4. Click "Add"

**Pinning for Quick Access:**
1. Right-click on folder in sidebar
2. Select "Pin to Quick Access" (Windows) or equivalent
3. Folder will appear highlighted/at top

**Navigating:**
- Use arrow keys or mouse to expand folders
- Look for yellow/orange highlighting for quick access items
- Collapse/expand as needed

### 4.2 Downloading Documents from Online Tools

**From Google Docs/Drive:**
1. Open document
2. File → Download
3. Select "Markdown" (preferred for AI)
4. Choose save location (use organized folder structure)
5. Save with descriptive name

**From Custom GPT:**
1. Open GPT configuration
2. Copy custom instructions
3. Paste into new .md file
4. Save in Instructions folder
5. Name clearly (e.g., `custom-gpt-messaging.md`)

**From Online Academy:**
1. Navigate to course/lesson
2. Use download feature if available
3. If not: File → Download → Markdown
4. Save to: `Online Academy/Courses/[course-name]/`

### 4.3 Working with Paths and Links

**Copying File Paths:**
1. Right-click on file in VS Code
2. "Copy Path" (full path) or "Copy Relative Path" (preferred)
3. Paste where needed

**Linking in Documents:**
```markdown
See also: Dropbox/libraries/professions
Reference: /Instructions/Messaging/template.md
```

**Relative vs Absolute Paths:**
- Relative: `libraries/professions` (better for sharing)
- Absolute: `C:/Users/Name/Dropbox/libraries/professions` (machine-specific)

### 4.4 Using AI Tools Effectively

**Claude/GPT/Cursor Best Practices:**

1. **Give Context:**
   - Reference relevant files from knowledge base
   - Provide background on the task
   - Specify desired output format

2. **Iterative Refinement:**
   - First pass: 15 minutes
   - Review results
   - Refine prompt
   - Second pass: 15 minutes
   - Should have good results in 2-3 iterations

3. **Prompt Structure:**
   ```
   Task: [What you need]
   Context: [Background information]
   References: [Relevant files/docs]
   Format: [How output should look]
   Constraints: [Any limitations]
   ```

### 4.5 File Organization Best Practices

**Naming Conventions:**
- Use lowercase
- Use hyphens not spaces: `first-message-template.md`
- Be descriptive: `linkedin-messaging-guide.md` not `guide.md`
- Include dates if versioned: `template-2025-11.md`

**Folder Structure:**
- Use numbered prefixes for sequence: `01-getting-started/`
- Group by topic/function
- Keep hierarchy shallow (max 3-4 levels)
- Include README.md in major folders

**Markdown Formatting:**
- Use headers (# ## ###) for structure
- Use lists for steps
- Use code blocks for examples
- Use tables for comparisons
- Add links to related docs

---

## PART 5: PROJECT MANAGEMENT CONCEPTS

### 5.1 Understanding Projects vs Tasks

**Task:**
- Single action item
- Can be completed relatively quickly
- Standalone
- Example: "Download template from Google Drive"

**Project:**
- Can run for a long time
- Contains multiple tasks
- Tasks can be grouped into stages
- Has defined milestones
- Example: "Build Knowledge Base"

### 5.2 Milestones

**What is a Milestone:**
- Significant stage completion in a project
- Represents meaningful progress
- Often has multiple tasks leading to it
- Example in "Dropsite Project":
  - Milestone 1: Deep research for each site completed
  - Milestone 2: Automation of deep research completed

**How to Use:**
- Break large projects into milestones
- Focus on one milestone at a time
- Celebrate milestone completion
- Review and adjust for next milestone

### 5.3 Current Projects Overview

**Project 1: Knowledge Base Building**
- **Milestones**: Download → Organize → AI Integration → Testing
- **Team**: Dedicated person + support
- **Timeline**: Ongoing, first milestone ASAP

**Project 2: Message Export Analysis**
- **Milestones**: Collection → Enrichment → Analysis → Implementation
- **Team**: Analytical person + AI support
- **Timeline**: Start today, first results within days

**Project 3: Online Academy Management**
- **Milestones**: Access → Audit → Updates → Maintenance
- **Team**: Content owner + reviewers
- **Timeline**: Ongoing, priority updates weekly

---

## PART 6: IMMEDIATE ACTION ITEMS

### For Ksenia (Team Lead/Manager):

**By Tomorrow 11:00 AM:**
- [ ] Train Dana on today's learnings
- [ ] Dana should be able to demonstrate understanding
- [ ] Come with initial results from one of the projects
- [ ] Check newcomers/juniors against criteria
- [ ] Make decision on their continuation

**By End of Week:**
- [ ] Have dedicated person assigned to Project 1
- [ ] Begin downloading instructions systematically
- [ ] Start collecting successful message exports
- [ ] Complete Online Academy audit
- [ ] Update at least one outdated lesson

### For Team Members:

**Immediate:**
- [ ] Set up VS Code/Cursor with Dropbox integration
- [ ] Access shared folders (accept invitations)
- [ ] Read all instructions shared
- [ ] Take detailed notes
- [ ] Practice with AI tools

**Daily:**
- [ ] Check for new instructions/updates
- [ ] Complete assigned tasks
- [ ] Document progress
- [ ] Ask questions in writing
- [ ] Share results

### For New/Reviewed Team Members:

**Prove You Can:**
- [ ] Install and set up tools quickly (VS Code)
- [ ] Follow written instructions without constant supervision
- [ ] Learn from first explanation
- [ ] Take initiative with AI tools
- [ ] Work at pace (not weeks for simple tasks)
- [ ] Show responsibility (be on time, be prepared)
- [ ] Read and comprehend documentation
- [ ] Execute independently while referencing materials

---

## PART 7: IMPORTANT REMINDERS

### 7.1 Communication Principles

**Remember:**
- Most communication will be via documents, not voice calls
- You MUST read what is written
- You MUST follow what is written
- Can't rely on constant voice explanations
- Document everything for reference
- Ask questions in writing for clarity

### 7.2 Learning Expectations

**You Must:**
- Understand from first explanation
- Take comprehensive notes
- Remember or reference notes
- Master processes after first repetition
- Work independently using documentation
- Not need weeks to learn basic tasks

### 7.3 Time Management

**Focus On:**
- Development, not constant verification
- Progress, not just process
- Results, not just activity
- Speed with quality
- Moving forward rapidly

**Avoid:**
- Spending time on trivial tasks
- Needing hand-holding for basics
- Waiting for permission for standard tasks
- Over-checking simple items

### 7.4 Tools and AI

**Expectations:**
- AI processes run ~15 minutes per iteration
- Should get results in 2-3 iterations
- Use AI proactively, not reactively
- Document what works
- Share successful prompts/approaches
- Continuously improve AI usage

---

## PART 8: QUALITY STANDARDS

### 8.1 For Knowledge Base Content

**All content must:**
- Be in Markdown format
- Have clear, descriptive filenames
- Be properly categorized
- Include metadata (dates, tags, purpose)
- Link to related materials
- Be up to date
- Be verified for accuracy

### 8.2 For Message Templates

**All templates must:**
- Be based on successful examples
- Include usage context
- Specify industries/situations
- Show success rates when possible
- Follow brand guidelines
- Avoid AI clichés
- Be tested before widespread use

### 8.3 For Academy Content

**All lessons must:**
- Have clear learning objectives
- Include practical examples
- Provide practice opportunities
- Be current and accurate
- Link to related resources
- Be reviewed regularly
- Include assessments when appropriate

### 8.4 For Documentation

**All documentation must:**
- Be clear and concise
- Use proper formatting
- Include step-by-step instructions
- Provide context and explanations
- Include examples
- Be maintained and updated
- Be accessible to intended audience

---

## PART 9: SUCCESS METRICS

### 9.1 For Projects

**Project 1 (Knowledge Base):**
- Number of documents downloaded and organized
- Percentage of knowledge base complete
- AI query success rate
- Team member usage frequency
- Time saved on common questions

**Project 2 (Message Analysis):**
- Number of successful messages analyzed
- Patterns identified
- Templates created/updated
- Success rate improvement
- Response rate increase

**Project 3 (Online Academy):**
- Percentage of content audited
- Number of lessons updated
- Number of missing lessons created
- Team member completion rates
- Knowledge test scores

### 9.2 For Team Members

**Individual Metrics:**
- Speed of task completion
- Quality of output
- Independence level
- Initiative shown
- Documentation quality
- Learning curve
- Contribution to knowledge base

**Team Metrics:**
- Overall project progress
- Knowledge sharing effectiveness
- Response time to questions
- Process improvement suggestions implemented
- Tool adoption rate

---

## PART 10: TROUBLESHOOTING & SUPPORT

### 10.1 Common Issues

**"Folder not appearing in Dropbox":**
- Check if invitation was accepted
- Refresh Dropbox sync
- Check sync settings
- Restart Dropbox app

**"Can't download from Google Drive":**
- Check permissions
- Try different format
- Use download all option
- Contact file owner

**"VS Code not showing files":**
- Check if folder was added to workspace
- Refresh workspace
- Check file explorer view
- Restart VS Code

**"AI not understanding prompts":**
- Add more context
- Reference specific files
- Break into smaller tasks
- Show examples of desired output

### 10.2 Getting Help

**When Stuck:**
1. Check documentation first
2. Search knowledge base
3. Ask AI tools
4. Ask team members in writing
5. Escalate to team lead if unresolved

**When Asking for Help:**
- Describe what you tried
- Share error messages
- Provide context
- Suggest what you think might work
- Be specific about what you need

---

## APPENDIX: Quick Reference

### A. Folder Structure Quick Reference

```
Dropbox/
├── LG November/
│   ├── LG Department/
│   │   ├── Instructions/
│   │   │   ├── 01-Messaging/
│   │   │   ├── 02-LinkedIn-Strategy/
│   │   │   ├── 03-Research-Methods/
│   │   │   ├── 04-Client-Communication/
│   │   │   ├── 05-Tools-and-Software/
│   │   │   ├── 06-Templates/
│   │   │   └── 07-Best-Practices/
│   │   ├── Prompt/
│   │   │   └── legend.md
│   │   └── Team Leads/
│   ├── Online Academy/
│   │   └── Courses/
│   │       ├── Course-1/
│   │       └── Course-2/
│   └── Libraries/
│       └── professions/
└── General Dropbox/
    └── Archive/
        └── LinkedIn Accounts Export/
```

### B. Key File Locations

- Main prompt: `LG Department/Prompt/legend.md`
- Professions list: `libraries/professions/`
- Message exports: `Archive/LinkedIn Accounts Export/`
- Instructions: `LG Department/Instructions/`
- Academy content: `Online Academy/Courses/`

### C. Essential Shortcuts

**VS Code/Cursor:**
- `Ctrl+P` - Quick file open
- `Ctrl+Shift+F` - Search across files
- `Ctrl+S` - Save file
- `Ctrl+B` - Toggle sidebar
- `Ctrl+` ` - Open terminal

**Dropbox:**
- Right-click → "Pin to Quick Access"
- Right-click → "Copy Path"
- Sync status icons

### D. Template for New Instructions

```markdown
# [Title of Instruction]

## Purpose
[Why this exists]

## When to Use
[Situations where this applies]

## Steps
1. [First step]
2. [Second step]
3. [Continue...]

## Examples
[Practical examples]

## Related Resources
- [Link to related doc 1]
- [Link to related doc 2]

## Last Updated
[Date]

## Tags
#tag1 #tag2 #tag3
```

---

## CONCLUSION

This action plan provides a comprehensive roadmap for:
- Daily management tasks
- Three major departmental projects
- Team development and expectations
- Technical procedures
- Quality standards
- Success metrics

**Remember:**
- Work quickly but thoroughly
- Document everything
- Use AI tools proactively
- Learn from first explanation
- Execute independently
- Communicate in writing
- Move forward rapidly

**Next Steps:**
1. Review this entire document
2. Take detailed notes
3. Begin immediate action items
4. Track progress daily
5. Update this document as you learn
6. Share knowledge with team

**Success Factors:**
- Responsibility (showing up and executing)
- Speed (not weeks for simple tasks)
- Independence (following written docs)
- Initiative (using AI proactively)
- Quality (meeting standards)
- Collaboration (sharing knowledge)

---

*Document Created: 2025-11-11*
*Last Updated: 2025-11-11*
*Owner: Ksenia Shkinder*
*Department: Lead Generation*
*Status: Active - Living Document*
