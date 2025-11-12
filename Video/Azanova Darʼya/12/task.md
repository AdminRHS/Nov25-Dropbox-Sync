# Task Breakdown - November 12, 2025

## Instructions
**What**: Detailed action steps
**Include**:
- Break each plan item into specific steps
- Add links and resources
- Clear instructions for execution

---

## Task 1: Review and Assess Chronicle Bot AI-Generated Summaries

### Steps:
1. Locate Chronicle Bot's output in admin channels
2. Compare bot-generated summaries with actual daily reports
3. Document specific inaccuracies (outdated problems, wrong project names, incorrect priorities)
4. Create list of what bot got right vs. wrong
5. Determine if bot saves time or creates more work
6. Provide structured feedback to Artemchuk/Kolya
7. Recommend continuation, refinement, or discontinuation

### Resources and Links:
- Chronicle Bot output (admin Discord channels)
- Daily reports that bot analyzed
- Artemchuk (technical contact)
- Kolya (worked late on bot implementation)

### Instructions:

**Current Situation:**
From daily transcript, Chronicle Bot is generating automated project summaries from team reports with mixed results:
- **Accurate items**: "Maria Glushko power outages" - correctly identified
- **Inaccurate items**: Solved problems marked as current, wrong project names ("Mosik" vs "Storyboards"), invented priorities
- **Formatting issues**: Looks different for everyone, some outputs are incomprehensible

**Review Process:**

**Step 1: Collect Examples**
- Gather 5-10 bot-generated summaries from past week
- Save screenshots or copies
- Note dates and which reports bot analyzed

**Step 2: Accuracy Assessment**
Create comparison table:

| Bot Statement | Reality | Accurate? | Issue Type |
|---------------|---------|-----------|------------|
| "Maria Glushko power outages - determine support options" | Active ongoing issue | ✅ Yes | None |
| "Check Maria Glushko's project - work completed without feedback" | Already resolved | ❌ No | Temporal - didn't see resolution |
| "Mosik rate increase negotiation" | Wrong name (Storyboards project) | ❌ No | Entity confusion |
| "Black Friday company high priority" | Not actually high priority | ❌ No | Priority hallucination |
| "Complete research, testing companies..." | Vague/incomprehensible | ❌ No | Word salad |

**Step 3: Pattern Analysis**

**Error Pattern 1: Temporal Issues**
- Bot shows old problems as current
- Doesn't recognize when issues resolved
- **Fix needed**: Better timestamp awareness

**Error Pattern 2: Entity Confusion**
- Mixes up project names, people, clients
- Confuses similar terms
- **Fix needed**: Better entity recognition

**Error Pattern 3: Priority Hallucination**
- Assigns priorities never stated
- Makes things "critical" or "high priority" incorrectly
- **Fix needed**: Only report explicit priorities

**Error Pattern 4: Comprehensibility**
- Some outputs are gibberish
- Formatting inconsistent between users
- **Fix needed**: Better natural language generation

**Step 4: Calculate Accuracy Rate**
- Count total bot statements
- Count accurate statements
- Calculate: (Accurate / Total) × 100 = Accuracy %
- **Goal**: Accuracy should be 80%+ to be useful

**Step 5: Time Impact Assessment**

**Time Saved:**
- How long would manual summary take? (e.g., 30 minutes)
- How long does bot take? (e.g., instant)
- **Potential savings**: 30 minutes

**Time Cost:**
- How long to review bot output? (e.g., 10 minutes)
- How long to correct errors? (e.g., 20 minutes)
- **Actual cost**: 30 minutes

**Net Result**: No time saved if correction time = manual time

**Step 6: Feedback Document**

Create structured feedback for Artemchuk/Kolya:

```
Chronicle Bot Feedback Report
Date: November 12, 2025
Reviewer: Dasha

## Summary
Chronicle Bot currently shows ~[X]% accuracy in generating project summaries.

## Strengths
✅ Successfully identifies ongoing infrastructure issues (power outages)
✅ Tracks multiple projects simultaneously
✅ Automated - requires no manual input

## Critical Issues
❌ Shows resolved problems as current (temporal awareness)
❌ Confuses project names (Mosik vs Storyboards)
❌ Assigns incorrect priorities not stated in reports
❌ Some outputs incomprehensible
❌ Formatting inconsistent between users

## Specific Examples
[Include 3-5 clear examples with corrections]

## Recommendation
[Choose one:]
- **Continue with refinements**: If accuracy >60%, list specific improvements needed
- **Pause for major rework**: If accuracy 40-60%, needs significant fixes before deployment
- **Discontinue**: If accuracy <40%, creates more problems than it solves

## Process Suggestion
If bot continues:
1. Manual review of bot output before sharing with leadership
2. Clear labeling: "AI-Generated Summary - Verify Accuracy"
3. Weekly accuracy tracking
4. Team feedback channel for reporting bot errors
```

**Step 7: Communicate Findings**

**To Team:**
"I've reviewed Chronicle Bot outputs. Current accuracy is approximately [X]%. Main issues are [list top 3]. My recommendation is [continue/refine/pause]. Don't fully trust bot outputs yet - always cross-check with original reports."

**To Leadership (if bot outputs being shared up):**
"Chronicle Bot is still in testing phase with mixed accuracy. Recommend manual review before using for decision-making. Will provide detailed assessment by [date]."

**Success Criteria:**
- ✅ Bot outputs reviewed and accuracy calculated
- ✅ Error patterns identified and documented
- ✅ Feedback provided to technical team
- ✅ Recommendation made (continue/refine/discontinue)
- ✅ Team aware of bot limitations

---

## Task 2: Understand New Discord Time Tracking Bot Requirements

### Steps:
1. Contact Artemchuk for official bot details and launch timeline
2. Understand exactly what bot tracks (presence, activity, idle time)
3. Clarify 8-hour requirement (continuous, split, breaks)
4. Determine integration with Timetracker/CRM
5. Understand flexible schedule exceptions for power outages
6. Learn enhanced screenshot requirements
7. Communicate requirements clearly to team

### Resources and Links:
- Discord server
- Timetracker/CRM system
- Artemchuk (technical contact)
- Svetushka (information source)
- Enhanced CRM screenshot guidelines

### Instructions:

**What We Know:**
- Discord bot will monitor channel presence (login/logout times)
- Goal: Verify 8-hour workdays
- Will cross-check with CRM/Timetracker
- Flexible schedules allowed for power outages
- Enhanced screenshot requirements coming
- Still in development stage

**Key Principle:**
> "The main thing is that there are 8 hours and work is done"

**Step 1: Get Official Details from Artemchuk**

Questions to ask:
```
1. Launch Timeline
   - When does bot go live?
   - Will there be testing period?
   - When will team be trained?

2. What Bot Tracks
   - Just presence in Discord or active participation?
   - Does idle time count?
   - Can you be in multiple channels?
   - What if Discord crashes/disconnects?

3. Eight-Hour Requirement
   - Must be continuous 8 hours or can split?
   - How are breaks counted?
   - What about lunch breaks?
   - Weekend work counted?

4. Timetracker Integration
   - Must times match exactly?
   - Acceptable discrepancy range?
   - Which system is "official"?
   - What if times don't match?

5. Flexible Schedule for Power Outages
   - Can work be split (e.g., 3hrs morning, 5hrs evening)?
   - How to log power outage interruptions?
   - Do all sessions need to total 8 hours?
   - Grace period for infrastructure issues?

6. Screenshot Requirements
   - How many per day?
   - When should they be taken?
   - What should screenshots show?
   - Where uploaded?

7. Compliance and Consequences
   - Warning system or immediate action?
   - Who monitors compliance?
   - How are violations handled?
   - Appeal process?

8. Exemptions
   - Who's subject to bot tracking?
   - Any roles exempt?
   - Project workers vs. hourly workers?
```

**Step 2: Create Compliance Guide**

Once details confirmed, create guide for team:

```
# Discord Time Tracking Bot - Compliance Guide

## Basic Requirements
✅ Work 8 hours per day (verified in Discord + Timetracker)
✅ Log into Discord when starting work
✅ Log out of Discord when ending work
✅ Times in Discord must match Timetracker
✅ Complete actual work (not just sit in Discord)
✅ Attach required screenshots in CRM

## For Standard Schedule Workers
**Regular 9am-5pm:**
- 9:00am: Log into Discord, start Timetracker
- 9:00am-5:00pm: Work in Discord channels
- Take reasonable breaks (note in Timetracker)
- 5:00pm: Stop Timetracker, log out Discord
- Upload screenshots to CRM

## For Flexible Schedule Workers (Power Outages)
**Split Schedule Example:**

Morning Session:
- 8:00am: Log into Discord, start Timetracker session 1
- Post: "Starting work (Session 1: 8am-11am)"
- 11:00am: Power outage - log out, stop Timetracker
- Note in Timetracker: "Power outage - 3 hours completed"

Afternoon Session:
- 4:00pm: Power returns - log in, start Timetracker session 2
- Post: "Resuming work (Session 2: 4pm-9pm)"
- 9:00pm: Complete work - log out, stop Timetracker
- Note in Timetracker: "Session 2 complete - 5 hours"
- Post: "Finished for day (Total: 8 hours)"

**Key Points for Flexible Schedules:**
- Multiple sessions allowed
- Must total 8 hours across all sessions
- Log each start/stop clearly
- Note power outages/interruptions
- Take screenshots during each session

## Best Practices

**Start of Day:**
1. Log into Discord
2. Start Timetracker
3. Post in channel: "Starting work for the day"
4. Take first screenshot

**During Work:**
1. Stay in Discord channels while actively working
2. Take screenshots at regular intervals (every 2 hours recommended)
3. If stepping away >15 minutes, note it
4. Document any interruptions (power, water, internet)

**End of Day:**
1. Post in channel: "Finished for the day"
2. Stop Timetracker
3. Log out of Discord
4. Upload all screenshots to CRM
5. Verify total hours = 8

## What NOT to Do
❌ Leave Discord open while not working (inflates hours)
❌ Forget to log in/out (creates discrepancies)
❌ Miss taking screenshots (can't verify work)
❌ Work less than 8 hours without approval
❌ Claim hours during power outage when can't work

## Troubleshooting

**Power outage mid-work:**
- Mark pause in Timetracker
- Log out of Discord (if possible)
- Resume when power returns
- Explain in notes

**Forgot to log in/out:**
- Message manager immediately
- Explain what happened
- Provide approximate times
- Don't make it a pattern

**Discord/Timetracker mismatch:**
- Check both systems
- Identify discrepancy
- Explain reason in notes
- Contact manager if significant

**Can't make 8 hours:**
- Request PTO in advance, OR
- Get approval to make up hours, OR
- Explain infrastructure issue

## FAQ

**Q: What if I need bathroom break?**
A: Take it. Reasonable breaks are expected. If >15 min, note in Timetracker.

**Q: What if power goes out 3x in one day?**
A: Work in available windows. Document each session. Total should reach 8 hours across all sessions.

**Q: What if I can't make 8 hours due to no power?**
A: Communicate immediately. Options: make up hours next day, use PTO, or get exception approval.

**Q: Does lunch count toward 8 hours?**
A: Depends on policy - ask Artemchuk. Typically: 30min lunch is fine within 8 hours.

**Q: What if I'm more productive in 6 hours than others in 8?**
A: Still need 8 hours logged. Productivity AND time both matter.
```

**Step 3: Team Communication**

Message to send once details confirmed:

```
Subject: New Discord Time Tracking Bot - Important Information

Team,

We're implementing a Discord bot to track work hours and support our flexible schedule policy.

📊 **What It Does:**
- Tracks when you're logged into Discord
- Monitors total hours per day
- Verifies against Timetracker
- Ensures 8-hour completion

⚡ **Why:**
- Enables flexible schedules for power outages
- Provides accountability
- Protects both company and workers
- Allows split shifts when needed

✅ **What You Do:**
1. Log into Discord when starting work
2. Stay in channels while working
3. Match Discord time with Timetracker
4. Complete 8 hours total (can be split)
5. Take required CRM screenshots

📱 **For Power Outage Workers:**
- Split work across day is OK (e.g., 3hrs + 5hrs)
- Must total 8 hours
- Log each session start/stop
- Note power outages
- We understand infrastructure challenges

🔍 **Screenshots:**
- More screenshots may be required
- Shows what you're working on
- Upload to CRM regularly

**Launch Date:** [TBD - still in development]

**Questions:** Contact Artemchuk (technical) or me (policy)

**Attached:** Compliance Guide (read carefully)

Let's make this work for everyone!
```

**Step 4: Monitor Team Adaptation**

**Week 1 (Launch):**
- Daily check-ins with team
- Help troubleshoot issues
- Collect feedback on bot accuracy
- Identify and escalate bugs

**Ongoing:**
- Weekly review of compliance
- Support struggling team members
- Advocate if requirements unreasonable
- Maintain 8 hours + work done standard

**Success Criteria:**
- ✅ Official bot requirements documented
- ✅ Compliance guide created and shared
- ✅ Team understands before launch
- ✅ Clear process for flexible schedules
- ✅ Support system in place

---

## Task 3: Prepare for Convenient Brands Video Needs

### Steps:
1. Research Convenient Brands company and email newsletter business
2. Understand typical video content for email newsletters
3. Review Dasha's video editing capabilities and availability
4. Prepare portfolio examples of email newsletter videos
5. Clarify with team what client actually needs
6. Position Dasha as video editor option if client requires
7. Monitor opportunity development

### Resources and Links:
- Convenient Brands website
- Email newsletter video examples (MailChimp, etc.)
- Dasha's video portfolio
- Nastya (project manager contact)

### Instructions:

**Current Situation:**
- New American client (Convenient Brands)
- Woman owner does email newsletters
- May need video content inserted into newsletters
- Looking for designer originally, but may need video editor
- Dasha identified as potential video resource

**Step 1: Research Convenient Brands**

**Company Research:**
- Visit company website
- Understand their business model
- Identify their target audience
- Review current email newsletters (if public)
- Note brand style and tone

**Questions to Answer:**
- What industry are they in?
- Who are their customers?
- What's their visual brand style?
- What email platform do they use?
- How often do they send newsletters?

**Step 2: Understand Email Newsletter Videos**

**Common Video Types for Newsletters:**
- Product demonstrations (15-30 seconds)
- Customer testimonials (30-60 seconds)
- Behind-the-scenes clips (20-40 seconds)
- Promotional announcements (15-30 seconds)
- Tutorial snippets (30-60 seconds)

**Technical Requirements:**
- Usually short (15-60 seconds max)
- Eye-catching thumbnail
- Silent/subtitled (many people don't enable sound)
- Optimized file size for email
- GIF format or embedded video link

**Step 3: Assess Dasha's Capabilities**

**Check Dasha's Skills:**
- Short-form video editing
- Quick turnaround time
- Subtitle creation
- Brand-style matching
- Newsletter format optimization

**Availability Considerations:**
- Power outages 3x daily
- Working from tablet sometimes
- Connection instability
- Current workload (video interviews)

**Strengths for This Project:**
- Experience with video editing
- Can work with mobile tools (demonstrated with CapCut)
- Flexible schedule management
- Quick adaptation to client needs

**Challenges:**
- Infrastructure issues may affect deadlines
- Internet instability for large file transfers
- Power availability timing

**Step 4: Prepare Portfolio Examples**

**Gather Dasha's Best Work:**
- Video interviews (show editing skills)
- Any short-form content (if available)
- Motion graphics (if applicable)
- Before/after editing examples

**Create Email Newsletter Specific Examples:**
If time allows, create 2-3 sample videos:
- 30-second product showcase
- 20-second announcement
- 15-second teaser
All with:
- Subtitles
- Brand-style flexibility
- Email-optimized format

**Step 5: Clarify Client Needs with Nastya**

Questions to ask:
```
1. What exactly does Convenient Brands need?
   - Videos for sure, or maybe?
   - How many per week?
   - What topics/types?

2. What's the timeline?
   - When do they need first video?
   - Regular weekly schedule?
   - Test assignment first?

3. What's the budget?
   - Hourly rate?
   - Per-video rate?
   - Long-term contract?

4. Technical requirements?
   - What email platform (Zoho mentioned)?
   - File format preferences?
   - Length restrictions?
   - Brand guidelines available?

5. Who creates content?
   - Do they provide footage?
   - Do we create from scratch?
   - Stock footage allowed?

6. Review process?
   - How many revision rounds?
   - Who approves?
   - Turnaround expectations?
```

**Step 6: Position Dasha as Solution**

**If Client Needs Video:**

Pitch to Nastya:
```
"Dasha is perfect for Convenient Brands video needs:

✅ **Strengths:**
- Experienced video editor
- Quick turnarounds
- Understands email newsletter format
- Flexible schedule
- Works well with American clients

⚠️ **Considerations:**
- Power outages may affect same-day deadlines
- Best with 24-48 hour turnarounds
- Strong portfolio of video interview work

**Recommendation:**
Present Dasha as video editor option. Set realistic expectations about infrastructure challenges, but emphasize quality and reliability."
```

**Backup Plan:**
If Dasha's infrastructure issues are concern:
- Identify backup video editor on team
- Propose tag-team approach (Dasha when power available, backup when not)
- Be transparent with client about infrastructure

**Step 7: Monitor Opportunity**

**Stay Updated:**
- Weekly check with Nastya on client status
- Ask: "Any movement on Convenient Brands?"
- Offer: "Dasha ready when needed"

**Be Prepared:**
- Have portfolio ready to send immediately
- Have rate/availability information current
- Have sample work prepared

**If Opportunity Materializes:**
- Respond quickly
- Set realistic expectations
- Deliver quality work
- Build long-term relationship

**Success Criteria:**
- ✅ Convenient Brands researched and understood
- ✅ Email newsletter video requirements identified
- ✅ Dasha's capabilities assessed
- ✅ Portfolio examples prepared
- ✅ Client needs clarified with Nastya
- ✅ Dasha positioned as video solution
- ✅ Opportunity monitored regularly

---

## Task 4: Coordinate with Stas on Website Feedback

### Steps:
1. Follow up on yesterday's ghosted 3pm call
2. Reschedule website feedback session
3. Review website work requiring feedback
4. Prepare specific feedback points
5. Conduct feedback session
6. Document outcomes and next steps
7. Ensure Stas has clear action items

### Resources and Links:
- Website project files
- Design system work
- Previous feedback notes
- Stas contact info

### Instructions:

**Current Situation:**
- Stas working on website project
- Scheduled call yesterday at 3pm
- Stas ghosted the call
- Still need to provide feedback
- Design system work in progress
- Uncertainty if Stas did this accidentally or intentionally

**Step 1: Professional Follow-Up**

**Message to Stas (Today):**
```
Hi Stas,

We had a call scheduled for 3pm yesterday that didn't happen. Not sure if you missed it or something came up.

I still need to give you feedback on the website work. Can we reschedule?

Available times:
- Today: [list specific times]
- Tomorrow: [list specific times]

Let me know what works for you.

Thanks!
```

**Tone:**
- Professional, not accusatory
- Assume positive intent
- Give benefit of doubt ("something came up")
- Focus on solution (rescheduling)

**Step 2: Understand What Happened**

**If Stas Responds:**
- Thank him for responding
- Don't dwell on missed call
- Move forward to rescheduling

**If Stas Doesn't Respond:**
- Wait 24 hours
- Send follow-up
- If still no response, escalate to manager

**Possible Reasons for Ghost:**
- Genuinely forgot
- Emergency came up
- Calendar confusion
- Avoiding difficult feedback
- Overloaded with work
- Folder chaos mentioned in transcript

**Step 3: Review Website Work**

**Before Feedback Session:**
- Review all website files Stas has worked on
- Check design system progress
- Identify what's working well
- Identify what needs improvement
- Prepare specific, constructive feedback

**Feedback Structure:**
1. **Strengths** (start positive):
   - What's working well
   - Good decisions made
   - Quality work delivered

2. **Improvements Needed** (constructive):
   - Specific issues
   - Why they're problems
   - Suggested solutions

3. **Next Steps** (action-oriented):
   - Clear action items
   - Deadlines
   - Support needed

**Step 4: Prepare Specific Feedback**

**Good Feedback Example:**
✅ "The design system colors are well-chosen and match the brand. However, the component library is missing the button variants we discussed. Can you add those by Friday?"

**Bad Feedback Example:**
❌ "This isn't right, fix it."

**Feedback Categories:**

**Design System:**
- Colors: Are they correct?
- Components: What's missing?
- Consistency: Is it unified?
- Documentation: Is it clear?

**Website Work:**
- Layout: Does it match requirements?
- Responsiveness: Does it work on mobile?
- Performance: Does it load fast?
- Completeness: What's still needed?

**Client Requirements:**
- Does work match client brief?
- Are deadlines being met?
- Is quality at client's standards?

**Step 5: Conduct Effective Feedback Session**

**Session Structure (30-45 minutes):**

**First 5 Minutes: Reconnect**
- Thank Stas for joining
- Briefly address missed call (no dwelling)
- Set agenda for call

**Next 10 Minutes: Review Work**
- Stas presents what he's done
- Ask clarifying questions
- Understand his thinking

**Next 15 Minutes: Feedback**
- Share prepared feedback
- Start with positives
- Move to improvements
- End with next steps

**Last 10 Minutes: Action Items**
- Document agreed changes
- Set deadlines
- Clarify priorities
- Confirm understanding

**Final 5 Minutes: Support**
- Ask: "What do you need from me?"
- Offer help/resources
- Schedule next check-in

**Step 6: Document Session**

**Create Feedback Summary Document:**
```
Website Feedback Session - November [Date], 2025
Attendees: Stas, [Your Name]

## Work Reviewed
- [List what was reviewed]

## Positive Feedback
- [Strength 1]
- [Strength 2]
- [Strength 3]

## Improvements Needed
1. [Issue 1]
   - Why: [Explanation]
   - Action: [What needs to be done]
   - Deadline: [Date]

2. [Issue 2]
   - Why: [Explanation]
   - Action: [What needs to be done]
   - Deadline: [Date]

## Action Items
☐ Stas: [Action 1] - Due [Date]
☐ Stas: [Action 2] - Due [Date]
☐ [Your Name]: [Support Action] - Due [Date]

## Next Check-in
Date: [Date]
Time: [Time]
Agenda: Review progress on action items

## Notes
[Any additional context or decisions]
```

**Share Document:**
- Send to Stas immediately after call
- CC manager if appropriate
- Reference in calendar invite for next meeting

**Step 7: Prevent Future Ghosts**

**Calendar Best Practices:**
- Send calendar invites (not just messages)
- Include Zoom/meeting link
- Add agenda in invite
- Send reminder 1 hour before
- Confirm attendance day of

**Communication:**
- If someone seems overwhelmed, ask
- Be flexible with rescheduling
- Build relationship, not just transactional
- Follow up after meetings

**Escalation Path:**
- 1st missed meeting: Friendly follow-up
- 2nd missed meeting: Direct conversation about communication
- 3rd missed meeting: Escalate to manager

**Success Criteria:**
- ✅ Rescheduled call completed
- ✅ Specific, constructive feedback provided
- ✅ Stas has clear action items
- ✅ Deadlines set
- ✅ Session documented
- ✅ Next check-in scheduled
- ✅ Relationship maintained professionally

---

## Reminder
- Break down each plan into steps
- Add all necessary links and resources
- Write clear execution instructions
