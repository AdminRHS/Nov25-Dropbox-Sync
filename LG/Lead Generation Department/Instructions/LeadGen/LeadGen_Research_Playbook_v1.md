# Research Methods Playbook

Single reference for preparing discovery insights before calls. Use it to track everything from the first manual searches through the final summary that the sales team will review.

---

## 1. Manual Discovery Sprint (10–15 min)

1. **Google prompts**
   - Start with `site:linkedin.com headquarters:"[City]" AND industry:"[Vertical]" AND "company size:[Range]"`.
   - Layer exclusions such as `-freelance -recruiting` to keep results relevant.
   - Save effective strings in your prompt tracker (date, query, number of good hits, follow-up ideas).

2. **LinkedIn deep dive**
   - Capture company name, URL, website, size, industry, and HQ.
   - Use the **People** tab to list decision makers (CEO, COO, CMO, CTO, Founders, VPs, Heads of *?, HR, Talent, Marketing, Sales, Product, Customer Success).
   - Copy profile links plus any visible contact data for later enrichment.

3. **Other fast checks**
   - Job boards (Clutch, Upwork, Toptal, Fiverr Pro, GoodFirms, DesignRush, 99Firms) for proof they buy external help.
   - Funding signals in Crunchbase, Dealroom, Product Hunt, Tracxn, BetaList, StartUs, Signal.nfx, StartupBlink.
   - Set Google Alerts for the brand or founder if you expect a longer cycle.

---

## 2. Pre-Call Research Template

> Storage: Drive → Team Lead → Deep Research. Duplicate the template from the same folder before you start.

### Section A – General Company Info
- Company name (exact LinkedIn naming), industry tag, HQ country.
- Public website + social handles.
- Main inbox/phone number.
- Paste the short description already drafted inside the calendar event.
- Update the **Client Call & Research Tracker** spreadsheet: call date/time (Kyiv), company name, and link to this doc.

### Section B – Deep Research Notes
Use Perplexity in Research mode with:
```
Do deep research on [Company] from [Country]. LinkedIn: [URL]. Gather all possible information using the prompt guide.
```
Capture:
- Basic profile (size, mission, locations, founding year, founders, brands/products).
- Financial data (funding stage, investors, revenue hints).
- Tech stack clues (BuiltWith/Wappalyzer, StackShare, hiring posts, GitHub).
- Decision makers (names, titles, responsibilities, hiring ownership).
- News & activity (launches, growth, AI initiatives).
- Needs/pain points from job posts or social comments.
- Competitive positioning and outlook.

### Section C – Summary
- Drop the Deep Research text into Claude and ask for a concise summary. Paste that output here for the call brief.

### Section D – Lead Information
- Lead name + title, LinkedIn link, location, and time zone.
- Use ChatGPT (LG account) with `Gather information about [Lead Name], [Title] at [Company]` to collect experience, previous roles, education.
- Verify you grabbed the correct person—duplicates exist.

### Section E – LinkedIn Post Insights
- Copy the URL of the company’s **Posts** tab.
- Prompt ChatGPT: `Review the posts on this LinkedIn page [link] and share key themes plus improvement ideas`.
- Store insights plus any hooks worth referencing in the outreach.

---

## 3. Research Hygiene

- **Document naming**: `CompanyName_DeepResearch_<YYYYMMDD>`.
- **Version control**: comment in the doc when major info changes (funding, leadership).
- **Media storage**: link to screenshots/videos instead of pasting heavy assets.
- **Prompt library**: keep working Google/LinkedIn/Perplexity prompts in the template so the team can reuse them.
- **Follow-up tracking**: update the tracker and CRM the moment research is complete; do not rely on the doc as the system of record.

Use this playbook as the single source of truth for research flows. Any improvements or new prompts should be added here so the rest of the team benefits immediately.
