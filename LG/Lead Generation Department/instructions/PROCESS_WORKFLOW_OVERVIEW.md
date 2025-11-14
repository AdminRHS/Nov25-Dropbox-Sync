# Lead Generation Department — Unified Process Workflow

## A) Detailed Process Map

### Phase 0 – Access, Alignment, and Environment
- **Purpose:** Ensure every Lead Generator (LG) has the right accounts, tools, and working guardrails before touching data.
- **Steps:**
  1. **Account Provisioning**
     - *Inputs:* Hiring ticket, onboarding_day1 checklist.
     - *Actions:* Create work Gmail + Chrome profile (`Tools_Gmail_Workflow_v1`), spin up LinkedIn account (`Tools_LinkedIn_Account_Workflow_v1`), enable Discord access (`Onboarding_Join_Channels_v1`).
     - *Outputs:* Verified Gmail/LinkedIn credentials, Discord presence, bookmarks baseline.
     - *Roles/Tools:* IT/Team Lead, new LG; Chrome, Discord, Gmail, LinkedIn.
  2. **Tool Stack Activation**
     - *Inputs:* Access list from leadgen_tools + Tools_VPN policy.
     - *Actions:* Install Google Scrape, RE extension, SalesQL, Whisper Flow, AI tools (ChatGPT/Claude/Gemini), configure VPN, bookmark workspace.
     - *Outputs:* Sandbox-ready browser profile with pinned extensions.
     - *Roles/Tools:* LG, Automation team; Chrome extensions, VPN, AI portals.
  3. **Orientation & KPIs**
     - *Inputs:* Onboarding Day plans, Bonus System, Daily workflow guide.
     - *Actions:* Review ICP/fundamentals, KPI definitions (50 companies created/updated, call targets), Yellow-card rules.
     - *Outputs:* Signed acknowledgment of expectations, onboarding trackers.
     - *Roles/Tools:* Onboarding lead, LG; oa-y academy, Google Sheets trackers.

### Phase 1 – Market & ICP Targeting
- **Purpose:** Define where to hunt and what “good” looks like before sourcing.
- **Steps:**
  1. **ICP Calibration**
     - *Inputs:* `Ideal_Customer_Profile`, `LeadGen_Target_Audience`, Restructure Report.
     - *Actions:* Select tier-1/2 countries, acceptable industries, decision-maker roles, company size (3–500 employees).
     - *Outputs:* Country/industry assignments stored in LG tracker.
     - *Roles/Tools:* Team Leads, LGs; Google Sheets, CRM filters.
  2. **Channel & Campaign Planning**
     - *Inputs:* `LeadGen_Campaign_Strategy`, `LeadGen_AI_Strategies`.
     - *Actions:* Choose channel mix (LinkedIn, job sites, email, communities), define prompts, experiments, automation.
     - *Outputs:* Quarterly experiment sheet, AI prompt library updates.
     - *Roles/Tools:* Campaign strategist, LGs; Sales Navigator, AI tools, Notion/Sheets.

### Phase 2 – Prospect Discovery & Research
- **Purpose:** Generate net-new qualified companies and contacts.
- **Steps:**
  1. **Sourcing**
     - *Inputs:* ICP filters, search prompts, job-site tables.
     - *Actions:*
       - Run Google Scrape queries, job-site spreadsheets, Sales Navigator saved searches, Upwork/Clutch monitoring.
       - Use RE extension to capture company/lead data when visiting LinkedIn profiles.
     - *Outputs:* Candidate company list, draft contact set.
     - *Roles/Tools:* LGs; Google Scrape, RE extension, SalesQL, Sales Navigator, Google Sheets job tables.
  2. **Deep Research**
     - *Inputs:* `LeadGen_Research_Playbook`, Whisper Flow transcripts, company websites, AI prompts.
     - *Actions:* Execute 10–15 min research sprint (website, LinkedIn, Crunchbase, social content); log discoveries in Deep Research doc/Google Drive; capture decision makers and pain points.
     - *Outputs:* Structured research doc link + summary snippet for CRM/plan.
     - *Roles/Tools:* LGs; Perplexity, Claude, ChatGPT, Drive, Whisper Flow.
  3. **Qualification & Scoring**
     - *Inputs:* Research findings, `LeadGen_Qualification_Workflow`.
     - *Actions:* Assess fit, budget signals, hiring triggers; choose lead magnet (deck, audit, video CV) if they show intent.
     - *Outputs:* “Go/hold” decision recorded in tracker; prioritized outreach queue.
     - *Roles/Tools:* LG + Team Lead; Google Sheets, CRM, AI tools.

### Phase 3 – CRM Data Entry & Hygiene
- **Purpose:** Make CRM the single source of truth with clean, deduplicated records.
- **Steps:**
  1. **Company & Lead Creation**
     - *Inputs:* Research data, `CRM_Data_Entry_Guide`, RE extension output.
     - *Actions:* Deduplicate (company name, website, LinkedIn); fill required fields (HQ, size, industry, contacts); log up to 5 decision makers; add notes referencing research.
     - *Outputs:* Complete company + lead cards in CRM.
     - *Roles/Tools:* LGs; CRM, RE extension, SalesQL.
  2. **Status & Needed Candidate Updates**
     - *Inputs:* `CRM_Pipeline_Management`, conversation insights.
     - *Actions:* Apply correct status (New, Sent Request, Connected, Interested, Follow-Up, Event, Call, Not Interested); fill Needed Candidate tab when talent specs provided; mark call events as “Happen”.
     - *Outputs:* Accurate pipeline, candidate demand dashboard.
     - *Roles/Tools:* LGs, Sales; CRM, Google Calendar.
  3. **Time Tracking & Screenshots**
     - *Inputs:* `Tools_Integration_Playbook`, Yellow-card policy.
     - *Actions:* Clock in/out, break logs, screenshot prompts; store Whisper Flow links inside daily.md.
     - *Outputs:* Verified attendance and audit trail.
     - *Roles/Tools:* LGs; CRM timer, Discord bot, Whisper Flow.

### Phase 4 – Outreach & Nurture
- **Purpose:** Engage decision makers with personalized sequences until qualification.
- **Steps:**
  1. **Message Crafting**
     - *Inputs:* Deep research notes, `LinkedIn_Message_Templates`, `LeadGen_Email_Templates`.
     - *Actions:* Generate first touch via Custom GPT/ChatGPT following system instruction; tailor with pain points; ensure CTA progression; log template use for A/B tracking.
     - *Outputs:* Approved copy stored in New Message Templates sheet + CRM communication log.
     - *Roles/Tools:* LGs, Team Leads for QA; LinkedIn, Gmail, AI tools.
  2. **Connection & Email Execution**
     - *Inputs:* Messaging plan, `LinkedIn_Connection_Request_Guide`, job-site SOP.
     - *Actions:* Send connection requests (max daily quotas, no note per SOP unless required); upon acceptance, send sequence (LinkedIn -> Email -> SMS if available); log each touch in CRM Send Email tab/SMS module.
     - *Outputs:* Contacted leads with timestamps, statuses adjusted.
     - *Roles/Tools:* LGs; LinkedIn, Gmail, CRM SMS, SalesQL.
  3. **Follow-Up Cadence & Re-engagement**
     - *Inputs:* Templates, `old_connections.md`, `templates_draft.md`.
     - *Actions:* Schedule follow-ups (2–3 day gaps initial, 5–7 day later); use job-site statuses (True/False) to handle existing companies; re-engage old connections quarterly; update Daily log/plans.
     - *Outputs:* Structured multi-channel sequence record.
     - *Roles/Tools:* LGs; Google Calendar reminders, CRM tasks, Discord #lg-messages review.
  4. **Decision Handling**
     - *Inputs:* Replies captured in #lg-messages, `LeadGen_Qualification_Workflow`.
     - *Actions:* For interested responses, craft deep-research reply + lead magnet; for objections, log reason, adjust status (Not Interested/Ignoring), plan nurture; escalate high-potential leads to Team Lead/Sales.
     - *Outputs:* Qualified prospects ready for meeting or archived leads with rationale.
     - *Roles/Tools:* LGs, Team Leads; CRM, Discord, AI.

### Phase 5 – Meeting Scheduling & Handover
- **Purpose:** Move qualified leads into live conversations with Sales.
- **Steps:**
  1. **Meeting Booking**
     - *Inputs:* Positive reply, `InternalWorkflow_Meeting_Setup`, `Scheduling_Google_Calendar`.
     - *Actions:* Confirm time zone via WorldTimeBuddy; update company & lead status to Event; log communication; schedule via `lg@rh-s.com` (title format, agenda, description, guest list); send confirmation message.
     - *Outputs:* Calendar event, CRM event entry, Sales notified.
     - *Roles/Tools:* LGs, Sales, Calendar; Google Calendar, CRM, Discord #lg-sales.
  2. **Rescheduling & Call Completion**
     - *Inputs:* `InternalWorkflow_Rescheduling_Guide`, CRM instructions.
     - *Actions:* If call misses, reschedule event + CRM communication; after call, mark “Happen,” change status to Call/Interested – Needs Proposal; attach Whisper Flow transcript link; note outcomes.
     - *Outputs:* Updated pipeline, follow-up tasks for Sales/talent.
     - *Roles/Tools:* LGs, Sales; CRM, Google Calendar, Whisper Flow.

### Phase 6 – Reporting, QA, and Incentives
- **Purpose:** Maintain transparency, improve processes, and reward performance.
- **Steps:**
  1. **Daily Documentation**
     - *Inputs:* `daily.md`, `plans.md`, `task.md` templates, Daily Workflow Guide.
     - *Actions:* Log activities chronologically with timestamps + transcripts; draft next-day plan; break tasks into actionable checklists.
     - *Outputs:* Complete daily package stored in `Department/Name/DD/`.
     - *Roles/Tools:* LGs; Whisper Flow, Markdown files, Discord.
  2. **Reporting & Leaderboards**
     - *Inputs:* `CRM_Daily_Report_Template`, Bonus System guide.
     - *Actions:* Submit CRM daily report + Discord post (metrics, positives, AI tools used); update statistics vouchers/leadgen updates sheets; review leaderboard standings.
     - *Outputs:* Manager-ready metrics, eligibility for bonuses (lead volume, call booking, leaderboard top 3).
     - *Roles/Tools:* LGs, Team Leads, Finance; CRM, Google Sheets, Discord.
  3. **Quality Control & Escalations**
     - *Inputs:* Yellow-card checklist, `InternalWorkflow_Bonus_System` QA rules, `Tools_Integration_Playbook`.
     - *Actions:* Team Leads audit CRM data, duplicate reports, adherence to cadence; escalate issues (#crm-mistakes); enforce warnings/Yellow Cards; refresh docs/README when Restructure Report flags gaps.
     - *Outputs:* Clean data, continuous improvements, maintained compliance.
     - *Roles/Tools:* Team Leads, Ops, Automation; CRM, Discord, Restructure Report.

---

## B) Flowchart Outline (Text)
Start
→ Phase 0: Access & Environment Setup
→ Phase 1: Define ICP & Campaign Plan
→ Phase 2: Source + Research Prospects
→ Decision: Does prospect meet ICP?
    → No → Log in tracker as “Hold/Discard” → Return to sourcing
    → Yes → Phase 3: Enter/Update CRM
→ Decision: Status “Reachable” (contact data available)?
    → No → Attempt enrichment (SalesQL/AI) → If still no, park lead and note gap → Return to sourcing
    → Yes → Phase 4: Launch Outreach Sequence
→ Decision: Positive engagement?
    → No → Follow-up cadence → If exhausted, set Not Interested/Ignoring, schedule re-engagement → Reporting
    → Yes → Phase 5: Schedule Meeting (Event → Call)
→ Decision: Call completed?
    → No → Reschedule per guide, update CRM → continue follow-ups
    → Yes → Handover to Sales/Talent & document outcomes
→ Phase 6: Daily reporting + QA + incentives
→ End (loop daily)

---

## C) ASCII Visual Diagram
```
[Start]
   |
   v
[Phase 0: Setup]
   |
   v
[Phase 1: ICP & Plan]
   |
   v
[Phase 2: Source & Research]
   |
   v
+---------------------------+
| Prospect matches ICP?     |
+---------------------------+
   |Yes                        |No
   v                           v
[Phase 3: CRM Entry]    [Log & discard]
   |                          |
   v                          +--> back to sourcing
+---------------------------+
| Contact data ready?      |
+---------------------------+
   |Yes                        |No
   v                           v
[Phase 4: Outreach]      [Enrich / park]
   |
   v
+---------------------------+
| Positive engagement?     |
+---------------------------+
   |Yes                        |No
   v                           v
[Phase 5: Schedule Call] [Follow-up / Recycle]
   |
   v
+---------------------------+
| Call completed?          |
+---------------------------+
   |Yes                        |No
   v                           v
[Phase 6: Report & QA]   [Reschedule]
   |
   v
[Continuous loop / End]
```

---

## Source Files Referenced
- CRM_Overview_v1.md
- CRM_Data_Entry_Guide_v1.md
- CRM_Pipeline_Management_v1.md
- LeadGen_Campaign_Strategy_v1.md
- LeadGen_Research_Playbook_v1.md
- LeadGen_Qualification_Workflow_v1.md
- LinkedIn_Message_Templates_v1.md
- LeadGen_Email_Templates_v1.md
- InternalWorkflow_Bonus_System_v1.md
- InternalWorkflow_Meeting_Setup_v1.md
- Tools_Gmail_Workflow_v1.md / Tools_LinkedIn_Account_Workflow_v1.md
- Tools_Core_Extensions_v1.md / Tools_SalesQL_Guide_v1.md / Tools_Integration_Playbook_v1.md
- Onboarding_* guides, Daily Workflow Guide, Yellow Card policy
