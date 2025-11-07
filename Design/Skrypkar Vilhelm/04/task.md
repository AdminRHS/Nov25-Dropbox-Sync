# Task Breakdown - November 4, 2025

## Instructions
**What**: Detailed action steps
**Include**:
- Break each plan item into specific steps
- Add links and resources
- Clear instructions for execution

---

## Task 1: Discuss ChatGPT Memory Management with Yulia Kucherenko

### Steps:
1. Schedule meeting with Yulia Kucherenko for tomorrow morning
2. Prepare overview of the memory limit issue: symptoms, impact on quality
3. Compile examples showing degraded output (missing accessories, wrong formats)
4. Research potential solutions beforehand:
   - Deleting old memories in ChatGPT
   - Starting a new conversation and migrating context
   - Using conversation branching
   - Alternative AI tools with better memory management
5. Present the issue and proposed solutions
6. Decide on immediate action plan
7. Document the chosen approach
8. Implement the solution
9. Test with new image generation to verify resolution

### Resources and Links:
- [ChatGPT Conversation with memory issues](https://chatgpt.com/c/6908c075-972c-832a-ad66-06e7b731455c)
- [Notion Task: Redesign courses cover images](https://www.notion.so/rh-s/Redesign-courses-cover-images-for-Game-Academy-285b16a3145180bab7afc2878d7eeed5?source=copy_link)
- [Course tracking spreadsheet](https://docs.google.com/spreadsheets/d/1ev_tOOysOAyC6zhmBINmZTjYYTppeKr4/edit?usp=sharing&ouid=114579329951199111949&rtpof=true&sd=true)

### Instructions:

**Before the meeting:**
Take screenshots of the problematic outputs showing:
- Mascots with cross-contaminated accessories
- Images generated in wrong format (vertical vs. square)
- Incomplete clothing elements

**During the meeting:**
Clearly explain the issue: "ChatGPT's memory storage filled up during extended image generation session, causing inconsistent outputs. This is blocking continued progress on course covers."

Present options with pros/cons:
- Option A: Delete memories - Fast but loses training context
- Option B: New conversation with context summary - Preserves key learnings
- Option C: Explore alternative tools - Long-term solution but immediate time investment

**After the meeting:**
Implement agreed solution immediately and generate 2-3 test images to confirm resolution before proceeding with full production.

---

## Task 2: Complete Remaining Game Academy Course Cover Images

### Steps:
1. Access the course tracking spreadsheet to identify remaining courses
2. Implement the memory management solution from Task 1
3. For each remaining course:
   - Review course theme and content
   - Select appropriate mascot
   - Design unique accessory concept relevant to course topic
   - Generate prompt following established format
   - Explicitly instruct ChatGPT not to reuse elements from other mascots
   - Generate image (multiple attempts if needed for quality)
   - Review output for consistency and quality
   - Save approved version with clear naming: [CourseName]_[Mascot]_raw.png
4. Update tracking spreadsheet with progress after each course
5. Organize all generated images in dedicated folder
6. Create backup of all raw files

### Resources and Links:
- [ChatGPT Conversation](https://chatgpt.com/c/6908c075-972c-832a-ad66-06e7b731455c) (or new conversation if memory reset)
- [Notion Task with course list](https://www.notion.so/rh-s/Redesign-courses-cover-images-for-Game-Academy-285b16a3145180bab7afc2878d7eeed5?source=copy_link)
- [Course tracking spreadsheet](https://docs.google.com/spreadsheets/d/1ev_tOOysOAyC6zhmBINmZTjYYTppeKr4/edit?usp=sharing&ouid=114579329951199111949&rtpof=true&sd=true)

### Instructions:

**Prompt Template for Each Course:**
"Generate a course cover image for [Course Name] featuring [Mascot Name - e.g., falcon, praying mantis]. The mascot should have [unique accessory relevant to course - e.g., welding goggles, programming keyboard].

Important requirements:
- Square format image suitable for extending to 1280x720
- Design elements concentrated on the right side
- DO NOT include any design elements from previous mascots (no yellow scarves, orange gloves, or other accessories from prior generations)
- Only use the specific accessory mentioned for this course
- Maintain mascot's core visual identity (colors, basic features)

Style: [existing Game Academy visual style]"

**Quality Checklist Before Saving:**
- ✓ Correct mascot
- ✓ Only specified accessories (no cross-contamination)
- ✓ Appropriate format (square or easily extendable)
- ✓ Design concentrated on right side
- ✓ Matches Game Academy visual style
- ✓ High enough quality for professional use

**File Naming Convention:**
[CourseName]_[MascotName]_raw.png
Example: "ProgrammingBasics_Falcon_raw.png"

---

## Task 3: Post-Process Generated Images in Photoshop

### Steps:
1. Set up Photoshop workspace with all raw images
2. Create action/template for consistent processing:
   - Canvas size: 1280x720
   - Left side: empty space for text overlay
   - Right side: mascot design
3. For each image:
   - Open raw image file
   - Evaluate current dimensions and composition
   - Use Generative Fill to extend background horizontally (left side)
   - Ensure seamless blending between original and generated areas
   - Adjust canvas to exact 1280x720 if needed
   - Position design elements optimally on right side
   - Verify left side provides good contrast for text
   - Export as high-quality PNG
   - Save working PSD file for future edits
   - Name final file: [CourseName]_[Mascot]_1280x720_final.png
4. Create contact sheet or preview grid of all covers
5. Review all covers as a set for consistency
6. Make final adjustments if needed
7. Upload finals to designated storage location

### Resources and Links:
- Raw images folder (from Task 2)
- [Notion Task](https://www.notion.so/rh-s/Redesign-courses-cover-images-for-Game-Academy-285b16a3145180bab7afc2878d7eeed5?source=copy_link)
- [Course tracking spreadsheet](https://docs.google.com/spreadsheets/d/1ev_tOOysOAyC6zhmBINmZTjYYTppeKr4/edit?usp=sharing&ouid=114579329951199111949&rtpof=true&sd=true)
- Adobe Photoshop with Generative Fill feature

### Instructions:

**Photoshop Generative Fill Workflow:**

1. **Initial Setup:**
   - Image → Canvas Size → Set to 1280x720
   - Anchor image to right side
   - New canvas area will be on left

2. **Generative Fill Process:**
   - Select the empty left area with Rectangle Marquee Tool
   - Use Generative Fill with prompt: "Seamless continuation of [background description - e.g., 'sky background', 'abstract blue pattern']"
   - Generate 2-3 variations
   - Select the most seamless option
   - Blend edges if necessary using Clone Stamp or Healing Brush

3. **Quality Check:**
   - Zoom to 100% to check blend quality
   - Ensure no visible seams
   - Verify left side provides adequate contrast for text (typically white or light-colored text)
   - Check that design elements remain on right 40-50% of image
   - Confirm overall composition is balanced

4. **Export Settings:**
   - Format: PNG
   - Quality: Maximum
   - Dimensions: Exactly 1280x720 pixels
   - Color profile: sRGB

5. **Organization:**
   - Working files: /WorkingFiles/[CourseName]_work.psd
   - Finals: /Finals/[CourseName]_[Mascot]_1280x720_final.png

---

## Task 4: Complete and Share Second Training Video with Designers

### Steps:
1. Follow up with Sviatoslav Pokrovsky on video editing status
2. Review edited video for quality and content accuracy
3. Check audio levels are balanced
4. Verify screen demonstrations are clear and visible
5. Add timestamps or chapters if helpful
6. Export in appropriate format (MP4, 1080p recommended)
7. Upload to Google Drive or designated sharing platform
8. Set appropriate sharing permissions
9. Compose message to designers with:
   - Link to new video
   - Brief description of improvements from first version
   - Key timestamps for quick reference
   - Reminder about the first video and admin session video
10. Post in designers' chat
11. Monitor for questions or clarifications needed
12. Update documentation with final video link

### Resources and Links:
- [First explanation video](https://drive.google.com/file/d/1MdZ3JKxHO-tf7Lgt4vv9kGWZ78DciNoP/view?usp=sharing)
- [Administration training session](https://drive.google.com/file/d/18AyqrSfuumITeloDTSZsYC7hudv8de7_/view?usp=drive_link)
- Sviatoslav Pokrovsky's video file (pending completion)
- Designers' Discord chat

### Instructions:

**Message Template for Designers:**

"Hi team! 👋

The improved training video for our new reporting system is ready. This version has better audio quality than yesterday's recording.

**Training Resources:**
1. **NEW - Improved explanation video**: [Link to new video]
2. Administration training session: https://drive.google.com/file/d/18AyqrSfuumITeloDTSZsYC7hudv8de7_/view?usp=drive_link
3. Original explanation: https://drive.google.com/file/d/1MdZ3JKxHO-tf7Lgt4vv9kGWZ78DciNoP/view?usp=sharing

**Quick Reference - Key Points:**
- Use Whisper Flow to record detailed transcripts of all your work
- Include: tasks, tools, prompts, analysis, and result links
- Use the AI assistant in Cursor to process your transcripts
- Files are in your Dropbox folder: Design Nov25/[YourName]/[Date]/

**The AI Prompt to Use:**
```
In the daily.md file, the path to which I attached below, you will find the transcript of the call. I need to process this transcript. Translate in to English, fill in the rest of the daily.md file according to the structure specified in it. Also, generate plans and tasks and enter this information into the plans.md and tasks.md files and fill them in according to the structure specified within these files.
[Your file paths]
```

Questions? Ask anytime!"

**Follow-up Actions:**
- Be available for questions throughout the day
- Check in with team members individually if needed
- Note common questions for potential FAQ document

---

## Task 5: Monitor Team Adoption of New Reporting System

### Steps:
1. Create checklist of team members who need to submit reports
2. Check Dropbox folders daily for new reports
3. Review submitted reports for:
   - Proper file structure (all three .md files present)
   - Complete Whisper Flow transcripts
   - Proper use of AI processing
   - English language output
   - Adequate detail level
4. Identify common issues or patterns
5. Provide individual feedback to team members:
   - Positive reinforcement for correct implementation
   - Constructive guidance for improvements needed
6. Document common questions/issues for FAQ
7. Schedule check-in meetings with team members struggling with the system
8. Collect feedback on the process (what's working, what's confusing)
9. Refine training materials based on real-world usage
10. Report progress to administration

### Resources and Links:
- Dropbox folder structure: Design Nov25/[TeamMember]/[Date]/
- [Training videos](https://drive.google.com/file/d/1MdZ3JKxHO-tf7Lgt4vv9kGWZ78DciNoP/view?usp=sharing)
- Team member roster
- Discord designers' chat for quick questions

### Instructions:

**Daily Review Checklist:**

For each team member's submission, verify:
- ✓ Folder structure: Design Nov25/[Name]/04/
- ✓ All three files present: daily.md, plans.md, task.md
- ✓ daily.md has timestamps and activity descriptions
- ✓ Whisper Flow transcripts are included
- ✓ Transcripts are translated to English
- ✓ "What I worked on" sections are filled
- ✓ "Outcomes" sections are completed
- ✓ plans.md has prioritized action items
- ✓ task.md has detailed steps and resources
- ✓ Files use proper markdown formatting

**Feedback Examples:**

*Good Implementation:*
"Great job on your report! Your Whisper Flow transcripts were detailed and the AI processing worked perfectly. The level of detail in your 'Outcomes' sections is exactly what we need. Keep it up!"

*Needs Improvement:*
"Thanks for submitting your report! A few suggestions:
- Try to include more detail in your Whisper Flow transcripts (mention specific tools, prompts, and links)
- The 'Outcomes' section should describe results, not just restate what you did
- Make sure to run the AI prompt to fill in plans.md and task.md

Let me know if you'd like to hop on a quick call to review together!"

**Escalation Criteria:**
- If team member misses 2 days: Direct message
- If reports are consistently incomplete: Schedule 1-on-1 training session
- If technical issues (AI not working): Troubleshoot immediately

---

## Task 6: Create Design Guidelines for Game Academy Mascots

### Steps:
1. Audit all existing Game Academy mascots
2. For each mascot, document:
   - Name and base character (animal/creature)
   - Primary color palette (with hex codes)
   - Secondary colors
   - Defining permanent features (eyes, body proportions, etc.)
   - Core accessories (elements that should always appear)
   - Variable accessories (elements that can change per course)
   - Personality/character description
3. Take screenshots of best examples for each mascot
4. Create visual reference sheet showing correct vs. incorrect usage
5. Define rules:
   - What must remain consistent
   - What can vary
   - What should never be mixed between mascots
6. Add examples of cross-contamination issues to avoid
7. Format as visual design system document with:
   - Cover page
   - Table of contents
   - Individual mascot profiles
   - Do's and Don'ts section
   - Quick reference guide
8. Review with design team
9. Incorporate feedback
10. Publish final version to team knowledge base

### Resources and Links:
- [Notion Task with existing covers](https://www.notion.so/rh-s/Redesign-courses-cover-images-for-Game-Academy-285b16a3145180bab7afc2878d7eeed5?source=copy_link)
- [Course tracking spreadsheet](https://docs.google.com/spreadsheets/d/1ev_tOOysOAyC6zhmBINmZTjYYTppeKr4/edit?usp=sharing&ouid=114579329951199111949&rtpof=true&sd=true)
- Existing course cover files
- Design tools: Figma, Adobe Illustrator, or similar

### Instructions:

**Mascot Profile Template:**

```
# [Mascot Name] - [Base Character]

## Visual Identity

**Primary Colors:**
- Main: #HEXCODE (Color Name)
- Accent: #HEXCODE (Color Name)

**Secondary Colors:**
- Background compatible: #HEXCODE, #HEXCODE

**Permanent Features:**
- [Feature 1]: Description
- [Feature 2]: Description
- Body proportions: Description

**Core Accessories:**
- [Accessory that appears in most/all variations]

**Variable Accessories:**
- Can change based on course theme
- Examples: [list examples from existing covers]

**Personality:**
Brief description that informs visual design choices

## Examples

[Good Example Image]
✓ Correct use of color palette
✓ Proper proportions
✓ Appropriate accessories

[Bad Example Image]
✗ Wrong colors
✗ Accessories from different mascot
✗ Inconsistent proportions

## Usage Rules

DO:
- Maintain core color palette
- Keep defining features consistent
- Use thematically appropriate variable accessories

DON'T:
- Use accessories from other mascots
- Change primary colors
- Alter core personality/character
```

**Visual Layout:**
Create a grid showing all mascots side-by-side with their key attributes for quick reference. This should be printable as a one-page cheat sheet.

---

## Task 7: Document ChatGPT Training Process for Image Generation

### Steps:
1. Review the trained ChatGPT conversation chronologically
2. Identify key training moments and corrections
3. Document initial problems encountered
4. Record the specific prompts/instructions that improved results
5. Create step-by-step guide:
   - How to start a new image generation project
   - Initial prompts to establish context
   - How to handle cross-contamination issues
   - When to provide corrections vs. start over
   - Memory management strategies
6. Include before/after examples
7. Create troubleshooting section for common issues
8. Develop template prompts for different scenarios
9. Add section on quality control checks
10. Format as reusable training document
11. Test the guide by having another team member follow it
12. Refine based on testing feedback
13. Publish to team knowledge base

### Resources and Links:
- [ChatGPT Conversation to analyze](https://chatgpt.com/c/6908c075-972c-832a-ad66-06e7b731455c)
- Examples of good and problematic outputs
- [Related Notion task](https://www.notion.so/rh-s/Redesign-courses-cover-images-for-Game-Academy-285b16a3145180bab7afc2878d7eeed5?source=copy_link)

### Instructions:

**Document Structure:**

1. **Overview**
   - Challenge: Generating consistent character designs across multiple images
   - Solution: Systematic ChatGPT training process

2. **Initial Setup**
   - Starting a fresh conversation
   - Establishing context and requirements
   - Initial prompt template

3. **The Training Process**
   - How to provide feedback on outputs
   - Recognizing signs of cross-contamination
   - Corrective prompt examples
   - Building memory/context over time

4. **Common Issues & Solutions**
   - Issue: Mixing accessories between characters
     - Solution: Explicit instruction not to reuse elements
   - Issue: Memory limit reached
     - Solution: [from Task 1 discussion]
   - Issue: Wrong format generated
     - Solution: Re-emphasize format requirements

5. **Template Prompts**
   - Initial project setup
   - Individual image generation
   - Correction prompts
   - Format refinement

6. **Quality Control**
   - Checklist for evaluating outputs
   - When to accept vs. regenerate
   - How to iterate efficiently

7. **Best Practices**
   - Be explicit about requirements
   - Reference the specific character being generated
   - Explicitly state what NOT to include
   - Provide feedback immediately when issues arise
   - Keep track of successful approaches

**Testing Instructions:**
Ask a team member unfamiliar with the process to follow the guide and generate 2-3 images. Observe where they get stuck or confused, and refine those sections.

---

## Reminder
- Break down each plan into steps
- Add all necessary links and resources
- Write clear execution instructions
