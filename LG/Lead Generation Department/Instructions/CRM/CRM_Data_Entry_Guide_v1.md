> Merged from: CRM/DataEntry/Add_New_Lead.md, CRM/DataEntry/CRM_usage_guide_for_lead_generators.md, CRM/DataEntry/fields.filling-when-adding-a-company-to-the-CRM.md, CRM/DataEntry/How_to_update_a_card.md on 2025-11-14.

# CRM Data Entry Guide

Comprehensive instructions for creating and maintaining accurate company and lead cards inside the Remote Helpers CRM. Use this as the single source of truth—if a step is missing, update this guide instead of creating a parallel doc.

---

## 1. Before You Add Anything

- **Confirm you are working in the correct market.** Only add companies from your assigned country/region unless your lead gen manager explicitly reassigns you.
- **Deduplicate.** From the `Leads` page press **Add New Lead** and search by company name, website, and LinkedIn URL. Only proceed if all three checks return “available.”
- **Research first.** Open the company’s website, LinkedIn page, and any public news to confirm: headquarters location, headcount (use LinkedIn’s employee range), industry, and that the firm is active.
- **Quota & cadence.** Minimum of **50 new companies per workday** unless your manager sets a different target. Every card you touch must be complete—speed never beats accuracy.

---

## 2. Company & Lead Fields to Complete

| Section | Required Fields | Notes |
| --- | --- | --- |
| **Lead Agent Details** | `LG Manager`, `Lead Source`, `Lead Accounts`, `Lead Type`, `Lead Status` | Default values are prefilled; update only if you were instructed to use a different account or funnel. |
| **Company Details** | `Company Name`, `Website`, `Country`, `Company Size`, `Industry`, `Sub Industry`, `Year Established`, `Projects Companies` | Size must reflect total employees worldwide. Use LinkedIn “About” or Crunchbase as reference. |
| **Corporation Details** | `Contact type`, `Contact value` | Log every unique channel (LinkedIn, email, phone, socials). |
| **Lead Details** | `Name`, `Position`, `Status`, `Lead Status`, `Contact type`, `Contact value` | Add up to 5 qualified leads per company. Prefill status = `Sent Request`. |

> **Tip:** Use clear English capitalization (Title Case for company names, First Last for people). Avoid emojis or informal wording inside the CRM.

---

## 3. Adding a Company (Step-by-Step)

1. **Start from Google** using a targeted query such as `site:linkedin.com "headquarters: Poland" industry:"marketing" "11-50 employees"`. Bookmark your best performing queries.
2. **Open the prospect’s LinkedIn page** in a new tab. Confirm the HQ matches your target country and that the company is operating in a serviceable industry.
3. **Validate a lead exists.** From the company LinkedIn page click **People** and filter for decision-makers (Founders, CEOs, Heads of Marketing/Sales/HR). Prioritize profiles with **100+ connections** (500+ ideal).
4. **Return to CRM → Add New Lead.** If the system warns “company already taken,” stop and pick another company.
5. **Fill out the Company section** using the research gathered in steps 1–3.
6. **Save the company card first,** then proceed to the **Contacts** tab to add leads (see section 4).

---

## 4. Adding Leads to the Company Card

- **Quality bar:** Add only decision-makers relevant to Remote Helpers (CEO, Founder, Co-founder, Head of Sales/Marketing/Growth, HR/Recruiting, Operations, Product leads).
- **Connections:** Prefer 500+ connections; never add profiles with less than 100 unless approved by the team lead.
- **Contact info:** Log LinkedIn URLs, corporate emails (if public), and phone numbers. For each contact method, select the proper `Contact type` and paste the clean URL/value.
- **Maximum per company:** Five leads. If you find more, save them for later once the first set responds.
- **Status & tags:** Default lead status is `Sent Request`. If you already messaged them (e.g., via email) before saving the card, note that inside the `Note` field when you add the contact.

---

## 5. Data Captured by the RE Extension

When you run the Remote Helpers (RE) Chrome extension on LinkedIn it auto-scrapes:

- **From the lead profile:** Name, Position, LinkedIn URL, Company location.
- **From the company page:** Company name, industry, foundation year, headcount, LinkedIn URL, website.
- **From the website:** Company Facebook, Instagram, general email, and phone (if detected).

Always review the scraped values—edit any incorrect capitalization, remove tracking parameters from URLs, and add missing data manually.

---

## 6. Updating Existing Cards

- **Real-time updates:** Change the lead status immediately after every interaction (`Connected`, `Interested`, `Not Interested`, etc.). Never leave a response unlogged.
- **Notes:** Summarize each touchpoint (channel + what was discussed + next action). Proofread via ChatGPT if needed before saving.
- **Quarterly refresh:** Every 3 months filter your portfolio (Country, exclude `Call`, `Not Relevant`, `Client`) and refresh outdated fields: job titles, company size, needed candidate notes, etc.
- **Duplicate handling:** If you accidentally create a duplicate card, tag it in the `crm-duplicates` Slack/Discord channel and merge per operations guidance.

---

## 7. Final Quality Checklist

- [ ] Duplicate check (company name, website, LinkedIn) completed.
- [ ] Company HQ, size, industry verified via LinkedIn or official site.
- [ ] At least one qualified lead with 100+ connections saved.
- [ ] All contact methods captured and labeled.
- [ ] Notes include how you found the company and next action.
- [ ] Lead status reflects the latest touchpoint.
- [ ] Company added to your daily quota tracker and Discord report.

Keeping the CRM clean is the fastest way to book calls—treat every card like you are handing it directly to Sales.


