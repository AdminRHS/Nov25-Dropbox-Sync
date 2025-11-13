> Merged from: InternalWorkflow/MeetingOps/create-event.md and Onboarding/GeneralGuides/Scheduling_Google_Calendar.md on 2025-11-14.

# Meeting Setup Playbook

One flow for logging calls in the CRM and scheduling them in Google Calendar—whether we host the event or the lead shares their own booking link.

---

## 1. Pre-call Checklist

Collect before you change any statuses:
- Lead name, company name, LinkedIn profile, email, phone/backup channel.
- Confirmed date & time (Kyiv time). Use [worldtimebuddy.com](https://www.worldtimebuddy.com) for conversions.
- Preferred meeting tool (default Google Meet; involve Sales if the lead insists on Zoom).

---

## 2. Update the CRM (Company + Lead)

1. **Find the record**
   - Locate the company via search (company or lead name).
2. **Company status**
   - Set status to `Event`, choose the agreed date/time in the modal, and save.
3. **Lead status**
   - Open the company card → Contacts → select the lead → set status to `Event` → `Update`.
4. **Communication log**
   - `Communication` → `Add communication`.
   - Date = call date, Type = `Event`, Channel = the platform used to message the lead (LinkedIn/Email/etc.), Account = your LG account, Project company = `Remote Helpers`.
   - Paste the GPT-cleaned conversation (no clutter) in **Note**.
5. **Sales follow-up**
   - Same date as the call, same channel/account, and paste the conversation again.
6. **Save** and confirm all statuses show `Event`.

---

## 3. Create the Google Calendar Event (lg@rh-s.com)

1. Log into the shared Gmail account (ask your Team Lead for credentials). This account also holds our ChatGPT/GPT access—use only for work.
2. Open Calendar → `Create` → `Event` → `More options`.
3. **Title**: `Company Name – Remote Helpers`.
4. **Date & time**: agreed slot, 30-minute duration. Add Google Meet link (default). Add 20‑ and 10‑minute reminders.
5. **Guests**: `sales@rh-s.com`, the lead’s email, and any supporting teammates if needed.
6. **Description template** (replace bracketed text):
   ```
   Join the online meeting with Remote Helpers in Ukraine and [Company Name]

   Website: rh-s.com
   Company website: [client site]
   Company info: [short GPT summary]
   Comments: [Lead name], [LinkedIn URL], [what the lead wants]
   Country: [lead country]
   Industry: [company industry]
   Manager: [your name]
   ```
   - Use LeadGen GPT with the standard prompt to produce the company summary; only paste the final summary.
7. **Save** → send invitations to all guests.
8. **Notify the lead** (LinkedIn/email):
   ```
   Hi [Name], I’ve scheduled our call for [Date] at [Time, Time zone] and sent an invite—please let me know if you received it.
   ```
9. **Same-day reminder** before the call using a short LinkedIn/Email check-in.

---

## 4. Booking via the Lead’s Calendar

When the lead sends a Calendly/HubSpot/etc. link:
1. Open their calendar page and our LG calendar side by side to find a matching slot.
2. Switch the lead’s booking tool to **Kyiv time** before confirming.
3. Select the slot → enter `Remote Helpers` as the organizer name → add `sales@rh-s.com` as the contact email (plus any requested fields).
4. In the description/comments, note: `Intro call to present Remote Helpers services`. Include the lead’s expected topics if the form allows it.
5. Submit the booking. If the event doesn’t auto-appear in lg@rh-s.com, open that inbox, accept the invite, and verify it shows on the calendar.
6. Update CRM statuses and communication logs exactly as in Section 2.
7. Inform Sales (Slack/email) with date, time, lead name, company, and summary.

---

## 5. Post-Scheduling Rituals

- Double-check both LG and Sales calendars to ensure the event synced.
- Store the WhisperFlow transcript link in your daily log once the call happens.
- If the lead reschedules or cancels, repeat the CRM + calendar updates immediately so Sales is never surprised.

Follow this playbook each time to keep invites consistent, CRM data accurate, and Sales fully aligned.

