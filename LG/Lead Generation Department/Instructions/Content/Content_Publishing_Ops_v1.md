# Publishing Operations Guide

How to move content ideas from brief → production → approval → distribution across LinkedIn, email, and knowledge bases.

---

## 1. Intake & Briefing

1. Capture the idea in your daily log or a request form.
2. Build a mini brief:
   - Audience + intent.
   - Channel (LinkedIn post, nurture email, instruction update, etc.).
   - Source materials (campaign data, research kit, meeting transcript).
   - CTA and success metric.
3. Log the brief in `PublishingWorkflows/board.csv` (create if needed) with owner + due date.

---

## 2. Production Flow

| Step | Owner | Reference |
| --- | --- | --- |
| Draft content | Content ops | Voice pillars (`BrandVoice/brand-voice-guide.md`) |
| Validate data | Research | `06_LeadGenerationWorkflows/ResearchMethods/research-playbook.md` |
| SME review | Channel lead | Daily logs / CRM notes |
| Tool prep | Ops | `08_ToolsAutomation/Extensions/core-extensions-guide.md` for prompts/automation |

Keep Whisper Flow on during reviews that involve stakeholders; store transcripts in `AssetLibrary/transcripts/`.

---

## 3. Approval & QA

1. Run the Brand Voice checklist (tone, CTA, proof).
2. Double-check compliance items:
   - Meeting info matches `07_InternalWorkflow/MeetingOps/meeting-setup-guide.md`.
   - Tool instructions align with latest `08_ToolsAutomation` docs.
3. Obtain sign-off:
   - Lightweight content → async emoji approval in Slack.
   - Major launches → Loom walkthrough or live review.
4. Update the asset’s status in `content-asset-inventory.md`.

---

## 4. Distribution & Logging

| Channel | Actions |
| --- | --- |
| LinkedIn | Schedule via native scheduler; tag campaign in spreadsheet; monitor replies using Task 1 workflow in `daily.md`. |
| Email | Load copy into Lemlist/Instantly or CRM automation; test send; screenshot final version for AssetLibrary. |
| Knowledge base | Update relevant folder (`06`, `07`, or `08`); add entry to README changelog. |

After publishing, note performance highlights in the daily log and share with Sales/Ops during stand-ups.

---

## 5. Retrospectives

1. Weekly: review top-performing posts/emails; capture learnings in this doc.
2. Monthly: select one asset from each channel to refresh or repurpose.
3. Record the decision + owner below.

| Date | Asset | Action | Owner |
| --- | --- | --- | --- |
| 2025-11-13 | LinkedIn AI pod post | Repurpose into case-study email. | Content Ops |
