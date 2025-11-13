> Merged from: CRM/PipelineManagement/Changing_the_status_of_a_lead.md, CRM/PipelineManagement/CRM_Succesful_Call.md, CRM/PipelineManagement/lead-generation-panel.md, CRM/PipelineManagement/Needed_Candidate.md, CRM/PipelineManagement/crm-updates.instruction.md on 2025-11-14.

# CRM Pipeline Management Guide

Everything you need to move leads through the Remote Helpers pipeline, keep statuses accurate, and surface hiring intent fast. Reference this guide whenever you update a card—do **not** create separate status cheat sheets.

---

## 1. Lead Generation Panel at a Glance

| Section | Purpose | Key Actions |
| --- | --- | --- |
| **Leads** | Master list of all company + lead cards. | Search by name/email, open cards to update statuses, log comms. |
| **Leads Test** | Fast inspector that shows company details without opening each card. | Double-check duplicates by website/LinkedIn, verify social links, spot missing data. |
| **My Lead Accounts** | Displays the LinkedIn/Gmail work accounts assigned to you. | Confirm you are using the correct account for outreach. |
| **Lead Reports (LG Daily)** | Displays how many companies you created today (filter = `create`). | Cross-check before sending your daily Discord & CRM reports. |

---

## 2. Status Definitions

| Status | Trigger | Required Action |
| --- | --- | --- |
| **Sent Request** *(default)* | Card just created or connection request sent. | Log outreach channel in notes. |
| **Connected** | Lead accepted your LinkedIn invite. | Send the first message within the same day, note any personalization used. |
| **Interested** | Lead replied positively (wants info, pricing, call). | Capture specifics in Notes, add Needed Candidate info if they request roles. |
| **Not Interested** | Lead explicitly declined. | Record reason. Schedule a nurture reminder only if they invited future follow-up. |
| **Ignoring** | Lead was responsive but stopped replying after 2+ nudges. | Set a future follow-up date and outline last touchpoint. |
| **Follow Up** | Lead asked to reconnect later or provided a date. | Add a follow-up date in the communication log + Calendar reminder. |
| **Event** | Call/meeting scheduled. | Include calendar link, agenda, participants. Update to **Call** once the meeting happens. |
| **Call** | Call completed. | Log summary + outcome, mark the communication as “Happen” (see section 5). |

Status changes must happen in real time. Nothing should sit in “Sent Request” or “Event” longer than the actual state of the relationship.

---

## 3. Movement Rules & Best Practices

1. **Use filters first.** On the Leads panel filter by country/manager/status before bulk editing—prevents accidental changes.
2. **Edit from the company card.** Click **Edit** → update the status dropdown → save. Never leave the card until the status and note are aligned.
3. **Document every transition.** When you move to `Interested`, add a note summarizing what they requested (budget, department, timing).
4. **Closed-loop follow-ups.** If you set `Follow Up`, add the same date to Google Calendar (orange) and to the CRM communication entry.
5. **Reverting statuses.** If a lead regresses (e.g., “Interested” → “Ignoring”), explain why in the notes so Sales understands context.

---

## 4. Needed Candidate Workflow

Use the **Needed Candidate** tab whenever a lead requests a specific role.

1. Open the lead card → **Needed Candidate** tab.
2. Fill in:
   - **Department** (e.g., Marketing, Design, AI/Automation).
   - **Position** (exact title requested).
   - **Client Needed Skills** (top 2–3 must-haves).
   - **Client Needed Status** (`Required`, `Hunting`, `Demand`, `Closed`, `Hired`, `Candidate`).
   - **Demanded Date** (today’s date).
   - **Notes** (short sentence, e.g., “App developer with Firebase experience”).
3. Switch the lead status from `Sent Request` to `Needed Candidate` or `Interested` depending on the conversation.

This data feeds hiring forecasts, so keep it pristine and update the status as soon as the client moves from “looking” to “closed” or “hired.”

---

## 5. Logging Events & Calls

1. **Scheduling:** After Sales confirms the meeting, ensure the event is on the CRM + Google Calendar (status = `Event`).
2. **After the call:** Open the company card → **Communication** tab → locate the `Event` entry.
3. Click **Edit**, tick **Happen**, add concise call notes (attendees, needs, next step), and save.
4. Change lead status to `Call` (or whatever Sales instructed, e.g., `Interested – Needs Proposal`).
5. Update the daily report and notify Sales in Discord if there are critical follow-ups.

If you skip marking “Happen,” the call will not count toward your bonus or pipeline metrics.

---

## 6. Update Cadence & Trackers

- **Quarterly refresh:** Review every company you own at least once per quarter (industry shifts, job changes, new hiring signals).
- **Statistics Voucher sheet:** Log daily creation/update totals in the shared Google Sheet so Operations can audit throughput.
- **Leadgen Updates sheet:** Record duplicate findings, blocked accounts, and LinkedIn-specific issues (link provided in the Ops bookmarks).
- **Duplicate escalation:** Post the card link + reason inside `crm-duplicates` on Discord whenever you find conflicting entries. Do not delete cards yourself unless Ops confirms.

---

## 7. Final Checklist

- [ ] Status accurately reflects the latest touchpoint.
- [ ] Notes include date, channel, summary, and next step.
- [ ] Needed Candidate tab filled when roles are requested.
- [ ] All events marked “Happen” after calls.
- [ ] Tracker spreadsheets updated (statistics + leadgen updates).
- [ ] Daily report mirrors what is inside the CRM.

Clean pipelines close faster. Treat the CRM like the single source of truth for Sales, Finance, and Leadership.


