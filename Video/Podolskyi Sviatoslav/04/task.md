# Task Breakdown - [Date]

## Instructions
**What**: Detailed action steps
**Include**:
- Break each plan item into specific steps
- Add links and resources
- Clear instructions for execution

---

## Task 1: Create Comprehensive Setup Documentation

### Steps:
1. Review and organize screenshots from today's setup session
2. Create VS Code setup guide with step-by-step instructions
3. Create Cursor setup guide with step-by-step instructions
4. Document the exact prompt format to use with Claude Code
5. Create troubleshooting section for common errors
6. Review with team and gather feedback
7. Publish documentation to team knowledge base

### Resources and Links:
- [Claude Code Extension](https://marketplace.visualstudio.com/items?itemName=Anthropic.claude-code)
- [Git Bash Download](https://git-scm.com/downloads)
- [Cursor IDE](https://cursor.sh/)
- Video recording from 2025-11-04 setup session

### Instructions:

**For VS Code Setup Documentation:**
1. Include screenshots of: Extension installation, Git Bash requirement error, authentication flow
2. Document exact steps: Open Extensions → Search "Claude Code" → Install → Login with admin account
3. Include settings configuration: Plan mode (Shift+Tab), model selection
4. Provide the standard prompt template for processing daily.md files

**For Cursor Setup Documentation:**
1. Include screenshots of: Extension installation, AI pane toggle, model selection dropdown
2. Document how to: Disable Auto mode → Select Composer1 model → Use "Keep" button after changes
3. Explain AI pane vs Chat differences

**For Troubleshooting Guide:**
- "Require git bash" error → Install Git Bash and restart IDE
- API limit errors → Use admin account login
- Slow performance → Check region settings, reduce API calls
- Transcription quality issues → Consider manual structured notes as backup


---

## Task 2: Address Whisper Flow Transcription Quality Issues

### Steps:
1. Document current transcription quality problems encountered
2. Research Whisper Flow status and recent updates
3. Test current Whisper Flow with different languages (Ukrainian, Russian, English)
4. Research alternative transcription tools (Otter.ai, AssemblyAI, Deepgram, etc.)
5. Create comparison matrix of tools (accuracy, cost, language support)
6. Run pilot tests with top 2-3 alternatives
7. Present findings and recommendations to team

### Resources and Links:
- [Whisper Flow Documentation](https://whisperflow.ai/)
- [Reddit discussions on Whisper Flow](https://www.reddit.com/)
- [Otter.ai](https://otter.ai/)
- [AssemblyAI](https://www.assemblyai.com/)
- [Deepgram](https://deepgram.com/)

### Instructions:

**Quality Issues to Document:**
- Language detection errors (switching between Ukrainian/Russian/English)
- Name misidentification (e.g., "client" interpreted as "Kolya")
- Date/time confusion (e.g., "tomorrow" recorded as "today")
- Context misinterpretation (e.g., "30 folders received" vs "plan timing for 30 folders")

**Evaluation Criteria for Alternatives:**
- Transcription accuracy (especially for multi-language conversations)
- Support for Ukrainian and Russian languages
- Cost per minute/hour of transcription
- Integration options with current workflow
- Real-time vs batch processing
- Speaker identification capabilities

**Testing Protocol:**
- Use same 2-3 sample recordings across all tools
# Task Breakdown - 2025-11-04

## Instructions
**What**: Actionable tasks derived from `plans.md` items. Each task below is broken into clear steps, includes resources, owner and an estimate.

---

## Task 1: Improve Whisper Flow transcription reliability

### Owner:
Sviatoslav (or assigned engineer)

### Estimate:
3 days (investigation + quick fixes) + follow-up testing

### Steps:
1. Reproduce problematic transcripts: gather 5–10 recent call audio files that produced poor transcriptions (start with the calls saved in `daily.md`).
2. Run Whisper Flow with current settings and log results (note language detection, name/date mistakes).
3. Test tuning options: force language to English when calls are in English, try different sampling/rate settings, and experiment with model variants if available.
4. If Whisper Flow cannot be sufficiently improved, implement a lightweight human-in-the-loop correction step: mark required fields (names, dates, next actions) for a quick manual pass before automation.
5. Document the recommended transcription settings and the fallback instruction (where to correct the transcript in `daily.md`).
6. Run end-to-end test: paste fixed transcript into automation, generate `plans.md` & `task.md`, and confirm >90% accuracy on names/dates for the test set.

### Resources and Links:
- Call transcripts / daily file: C:\Users\neozo\Dropbox\Nov 25\Video\Podolskyi Sviatoslav\04\daily.md
- Whisper Flow docs / settings (add internal link if available)
- Local test audio files (place them in the same folder under /audio-test/)

### Instructions:
Run tests locally or in a controlled environment. Capture before/after examples to include in the documentation. If manual correction is used, create a short checklist for what to correct (names, dates, decisions, next steps).

---

## Task 2: Finalize automation workflow (Claude Code) & config

### Owner:
Automation lead / Dev

### Estimate:
1–2 days to stabilize + 1 half-day for verification in Cursor and VS Code

### Steps:
1. Verify Claude Code extension installation steps and pre-requisites (Git Bash, login using admin account).
2. Confirm model setting: make Composer1 the recommended model for plan generation in the docs.
3. Create a small script or alias for the common automation prompt used to generate `plans.md` and `task.md` from `daily.md` (store prompt in repo as `/automation/prompt.txt`).
4. Test the flow in both environments:
	- VS Code: open `daily.md`, copy contents, paste into chat/extension, run Plan mode.
	- Cursor: paste transcript into AI pane, select Composer1, run plan mode.
5. Capture any differences and create a short troubleshooting list (login issues, Git Bash error, subscription/credit issues).
6. Add a one-click or documented checklist to run the automation safely using the admin account.

### Resources and Links:
- `daily.md`: C:\Users\neozo\Dropbox\Nov 25\Video\Podolskyi Sviatoslav\04\daily.md
- `plans.md` and `task.md` (targets): C:\Users\neozo\Dropbox\Nov 25\Video\Podolskyi Sviatoslav\04\plans.md
- Suggested prompt file: C:\Users\neozo\Dropbox\Nov 25\Video\Podolskyi Sviatoslav\04\automation\prompt.txt (create this file)

### Instructions:
Stabilize the workflow, then run 3 end-to-end tests with different transcripts. Capture errors and update the prompt or steps as needed. Add the prompt file to repo and reference it in the onboarding docs.

---

## Task 3: Create onboarding doc and short tutorial

### Owner:
Documentation / Video owner

### Estimate:
1–2 days to write the doc + 1 day to record short video

### Steps:
1. Draft a concise 1–2 page guide that covers:
	- Where to paste transcripts in `daily.md`.
	- How to open the AI/chat pane in VS Code and Cursor.
	- Which model to select (Composer1) and how to disable Auto.
	- How to run Plan mode and accept results.
	- Git Bash and login notes for Claude Code extension.
2. Capture 6–8 screenshots showing the key steps (open folder, paste transcript, model selector, run plan mode, accept results).
3. Record a 5–8 minute screencast (optional) demonstrating 1 end-to-end run.
4. Publish doc and video link in the project folder and notify the team.

### Resources and Links:
- Example files: C:\Users\neozo\Dropbox\Nov 25\Video\Podolskyi Sviatoslav\04\daily.md
- Plans & tasks files: C:\Users\neozo\Dropbox\Nov 25\Video\Podolskyi Sviatoslav\04\plans.md
- Folder for assets: C:\Users\neozo\Dropbox\Nov 25\Video\Podolskyi Sviatoslav\04\assets\ (create for screenshots/video)

### Instructions:
Keep the guide short and action-oriented. Use numbered steps and screenshots. Link the video in the doc and add a short checklist at the end for daily usage.

---

## Reminder
- Break down each plan into steps and add resources.
- Add any missing links or local files to the `assets/` folder for team access.
- After implementation, run a verification pass and update `plans.md` if priorities shift.
**Credit Limit Configuration:**
- Default limit: $20 per account per month
- Review process for requesting higher limits
- Alerts at 50%, 75%, 90% usage

**Training Materials:**
- Why admin accounts are required
- How to check credit usage
- What to do if limit is reached
- How to optimize usage (use Plan mode, batch requests)

**Monthly Review:**
- Track which projects/team members use most credits
- Identify optimization opportunities
- Adjust limits as needed based on actual usage patterns


---

## Task 5: Test Workflow with Multiple Daily Calls

### Steps:
1. Select 1-2 team members for pilot testing
2. Have them process a full day with 3+ meetings
3. Document any issues or edge cases
4. Test with different types of meetings (client calls, internal standups, planning sessions)
5. Verify quality of auto-generated outputs
6. Gather feedback on time savings
7. Refine workflow based on findings

### Resources and Links:
- Pilot tester feedback form
- Sample multi-call daily.md files

### Instructions:

**Pilot Testing Scope:**
- Minimum 3 different calls in one day
- Mix of meeting types and lengths
- Include both Ukrainian/Russian and English conversations
- Process at end of day using standard workflow

**What to Monitor:**
- Does Claude Code handle multiple transcripts correctly?
- Are activities properly separated and categorized?
- Is the quality consistent across all summaries?
- How long does processing take for multiple calls?
- Are there any API timeout or limit issues?

**Success Criteria:**
- All meetings properly documented
- Summaries are accurate and useful
- Plans and tasks correctly extracted
- Process takes less than 10 minutes total
- Team member would use this workflow regularly


---

## Task 6: Optimize Model Selection Strategy

### Steps:
1. Test different Claude models (Composer1, Sonnet, Opus, Haiku) with same transcripts
2. Document quality differences and processing times
3. Test with varying transcript lengths (short 15min calls vs long 2hr meetings)
4. Calculate cost per processing task for each model
5. Create decision matrix for model selection
6. Document guidelines in team standards
7. Train team on when to use which model

### Resources and Links:
- [Claude Model Comparison](https://docs.anthropic.com/claude/docs/models-overview)
- Cost calculator spreadsheet

### Instructions:

**Testing Protocol:**
- Use 5-10 sample transcripts of varying lengths and complexities
- Process each with Composer1, Sonnet, and Haiku models
- Measure: accuracy, completeness, processing time, cost

**Model Selection Guidelines (Draft):**
- **Haiku**: Short calls (<30 min), simple topics, quick daily updates
- **Composer1**: Standard meetings (30-60 min), mixed topics - CURRENT STANDARD
- **Sonnet**: Complex meetings (60+ min), technical discussions, multiple topics
- **Opus**: Critical meetings requiring highest accuracy (use sparingly due to cost)

**Documentation to Create:**
- Quick reference chart: "Which model should I use?"
- Cost implications of each choice
- How to switch models in VS Code and Cursor
- When to escalate to higher-tier model


---

## Task 7: Research Whisper Flow Alternatives

### Steps:
1. Compile list of transcription tools to evaluate
2. Check each tool's language support and accuracy ratings
3. Sign up for free trials where available
4. Test with sample recordings from actual team calls
5. Compare accuracy, cost, features, and integration options
6. Create detailed comparison report
7. Make recommendation for primary and backup transcription tools

### Resources and Links:
- [Otter.ai](https://otter.ai/)
- [Rev.ai](https://www.rev.ai/)
- [AssemblyAI](https://www.assemblyai.com/)
- [Deepgram](https://deepgram.com/)
- [Descript](https://www.descript.com/)
- [Fireflies.ai](https://fireflies.ai/)

### Instructions:

**Tools to Evaluate:**
1. Otter.ai - Popular, good UI, may have better language support
2. AssemblyAI - Developer-friendly API, good accuracy
3. Deepgram - Fast processing, good for real-time
4. Rev.ai - High accuracy, human-in-the-loop option
5. Fireflies.ai - Meeting-focused, automatic integration with calendars
6. Native Whisper API from OpenAI

**Evaluation Criteria:**
- Ukrainian/Russian language support and accuracy
- Multi-speaker identification
- Timestamp accuracy
- Export format options (text, SRT, JSON)
- Integration with current workflow
- Cost per hour of audio
- Processing time
- Privacy/security features (important for client calls)

**Testing Process:**
- Use 3 sample recordings: Ukrainian only, Russian only, Mixed languages
- Measure word error rate if possible
- Check for specific errors noted in current Whisper Flow usage
- Test API integration if available

**Recommendation Format:**
- Primary tool: [Best overall choice]
- Backup tool: [Alternative if primary fails]
- Cost analysis: Monthly estimated cost
- Migration plan: Steps to switch from Whisper Flow


---

## Task 8: Establish Manual Note-Taking Backup Process

### Steps:
1. Identify scenarios where manual notes are better than automated transcription
2. Create structured note-taking template
3. Develop guidelines for when to use manual vs automated
4. Create quality control checklist
5. Train team on hybrid approach
6. Document the backup process
7. Create examples of good manual notes vs poor transcriptions

### Resources and Links:
- Manual note-taking template (to be created)
- Quality control checklist
- Team training materials

### Instructions:

**When to Use Manual Notes:**
- Transcription quality is consistently poor for certain call types
- Highly sensitive information that shouldn't be auto-processed
- Very short updates where transcription overhead isn't worth it
- Strategic planning calls where human interpretation adds value
- Client calls where exact wording matters (legal, contractual)

**Manual Note-Taking Template Structure:**
```markdown
### [TIME] - [MEETING NAME]
**Participants:** [Names]
**Topic:** [Brief description]

**Key Discussion Points:**
- Point 1
- Point 2
- Point 3

**Decisions Made:**
- Decision 1
- Decision 2

**Action Items:**
- [ ] Task 1 - Owner - Deadline
- [ ] Task 2 - Owner - Deadline

**Next Steps:**
- Next step 1
- Next step 2
```

**Quality Control Guidelines:**
- Manual notes should be written immediately after call (within 15 min)
- Use structured format for consistency
- Focus on decisions and action items, not verbatim transcript
- Include specific names, dates, and numbers mentioned
- Link to any referenced documents or resources

**Hybrid Approach:**
- Run Whisper Flow for basic transcription
- Listen to key moments while reviewing auto-generated transcript
- Manually correct critical errors (names, dates, decisions)
- Add context that automated system missed
- Use automated output as starting point, not final product


---

## Reminder
- Break down each plan into steps
- Add all necessary links and resources
- Write clear execution instructions
