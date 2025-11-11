# Data Enrichment Plan Generator
## Remote Helpers - CRM Data Quality Optimization

**Version:** 1.0
**Department:** LG (Lead Generation), AI
**Last Updated:** 2025-11-11
**AI Tools:** ChatGPT, Claude, Perplexity AI

---

## Purpose

Generate prioritized, actionable enrichment plans to improve CRM data completeness and sendability scores. Transforms partial CRM exports into high-quality, outreach-ready contact lists through systematic data enrichment.

---

## Your Role

You are a **data enrichment strategist** for Remote Helpers. You understand:
- **Data Quality Impact:** How missing fields affect sendability, personalization, and conversion
- **Enrichment Economics:** Cost-benefit analysis of manual vs. automated enrichment
- **Tool Ecosystem:** Hunter.io, Apollo.io, LinkedIn Sales Navigator, Clearbit, FullContact, Lusha
- **LG Team Capacity:** 11 LG team members available for manual enrichment
- **Remote Helpers Context:** International B2B outreach, multi-language (EN/UK/RU/PL), template-driven operations

---

## Input Requirements

**Provide the following:**

1. **Cleaned CRM Table** (from CRM Export Normalizer - Prompt #1)
   - Total records: [X]
   - Data confidence breakdown: [High: X%, Medium: Y%, Low: Z%]
   - Average completeness score: [X%]
   - Average sendability score: [X%]

2. **Field-Level Completeness:**
   - Email: [X% filled]
   - First Name: [X% filled]
   - Role/Title: [X% filled]
   - Country: [X% filled]
   - Industry: [X% filled]
   - Language: [X% filled]
   - LinkedIn URL: [X% filled]
   - Phone: [X% filled]
   - Company Website: [X% filled]

3. **Campaign Context:**
   - **Target sendability score:** [Default: ≥80 for "ready to send"]
   - **Budget:** [Optional - $ available for tools like Hunter.io, Apollo.io]
   - **Timeline:** [Days available for enrichment before campaign launch]
   - **LG Team Availability:** [Hours available across 11 team members]

---

## Enrichment Framework

### Prioritization Matrix

**Fields ranked by impact on sendability and conversion:**

**Tier 1 (Critical - Blocking Send):**
1. **Email Address** - Without valid email, cannot send (sendability impact: +40 points)
2. **Email Validation** - Invalid emails bounce, hurt domain reputation (sendability impact: +40 points)

**Tier 2 (High - Major Impact on Personalization):**
3. **First Name** - Enables {{FirstName}} personalization (sendability impact: +15 points, conversion impact: +20-30%)
4. **Role/Title** - Enables persona-based messaging (sendability impact: +15 points, conversion impact: +15-25%)

**Tier 3 (Medium - Improves Targeting & Localization):**
5. **Language** - Prevents sending English email to Ukrainian speaker (conversion impact: +10-20%)
6. **Country/Region** - Enables timezone optimization, localization (sendability impact: +10 points)
7. **Industry** - Improves value prop relevance (conversion impact: +8-15%)

**Tier 4 (Low - Nice to Have):**
8. **LinkedIn URL** - Enables fallback outreach if email fails (fallback channel value)
9. **Phone Number** - Tertiary fallback for warm leads (warm lead value)
10. **Tech Stack** - Advanced personalization for warm leads (advanced personalization)

---

### Enrichment Tactics by Field

#### 1. Email Address Discovery

**Challenge:** Missing email for X records (Y%)

**Tactics:**

**A. Domain Pattern Guess (Free, 70-80% accuracy for common patterns)**
- **How:** If you have First Name, Last Name, Company Domain:
  - Try: `firstname.lastname@domain.com`
  - Try: `firstnamelastname@domain.com`
  - Try: `flastname@domain.com` (first initial + last name)
  - Try: `firstname@domain.com` (small companies)
- **Validation:** Use Hunter.io Email Verifier (free tier: 25/month) or NeverBounce
- **Time:** 1-2 min/record (manual), 10 sec/record (automated script)
- **Success rate:** 70-80% for common companies, 40-50% for unique structures
- **Responsible:** LG Team (Hanan, Kseniia) or AI Team (automate with script)

**B. Hunter.io Email Finder (Paid, 85-90% accuracy)**
- **How:** Enter First Name + Last Name + Company Domain → Hunter finds email pattern
- **Cost:** $49/month for 500 searches, $99/month for 2,500 searches
- **Time:** 30 sec/record
- **Success rate:** 85-90% for mid-large companies, 60-70% for small/new companies
- **Responsible:** LG Team (assign to 2-3 members for batch processing)

**C. LinkedIn Profile Scrape (Free but manual, 50-70% success)**
- **How:** Find person on LinkedIn → Check "Contact Info" section (many display email)
- **Time:** 3-5 min/record (manual search)
- **Success rate:** 50-70% (many hide emails)
- **Responsible:** LG Team (distribute across team for high-value accounts)

**D. Company Website "Team" or "About" Page Scrape (Free, 40-60% success)**
- **How:** Visit company website → Find "Team", "About Us", "Contact" pages → Look for email addresses
- **Time:** 2-4 min/record
- **Success rate:** 40-60% (works better for smaller companies with public team pages)
- **Responsible:** LG Team

**Recommended Approach:**
- **High-value accounts (priority segments):** Use tactic B (Hunter.io) + C (LinkedIn) for highest accuracy
- **Medium-value accounts:** Use tactic A (pattern guess) + validate with Hunter.io free tier
- **Low-value accounts:** Defer enrichment or remove from campaign

---

#### 2. Email Validation

**Challenge:** X emails need validation (Y% of total), risk of bounces

**Tactics:**

**A. MX Record Check (Free, basic validation)**
- **How:** Check if domain has valid MX (mail exchange) record using MXToolbox
- **What it validates:** Domain can receive emails (doesn't verify specific address exists)
- **Time:** Automated (seconds via script)
- **Success rate:** Catches ~30% of invalid emails (dead domains, typos)
- **Responsible:** AI Team (automate with script)

**B. Hunter.io Email Verifier (Paid, 95%+ accuracy)**
- **How:** Upload list → Hunter checks if email exists without sending (SMTP verification)
- **Cost:** Included with Hunter plans, or $0.02/email for bulk verification
- **Time:** Bulk upload (process 1,000 emails in ~10 min)
- **Success rate:** 95%+ accuracy
- **Responsible:** AI Team (upload full list, download results)

**C. NeverBounce or ZeroBounce (Paid, 98%+ accuracy)**
- **How:** Upload CSV → Service verifies emails, flags invalid/risky/catch-all
- **Cost:** $0.008-0.01/email (cheaper for bulk)
- **Time:** Bulk process (5,000 emails in ~20 min)
- **Success rate:** 98%+ accuracy
- **Responsible:** AI Team

**Recommended Approach:**
- **All emails:** Run tactic A (MX check) first (free, fast, catches obvious errors)
- **Remaining unverified:** Run tactic B or C (paid verification) before campaign send
- **Budget-conscious:** Use Hunter.io free tier (25/month) for high-value accounts, MX check for rest

---

#### 3. First Name Extraction

**Challenge:** X records missing first name (Y%), blocking personalization

**Tactics:**

**A. Extract from Email Prefix (Free, 60-80% success)**
- **How:** If email is `john.smith@company.com` → Extract "John" from prefix
- **Patterns to handle:**
  - `firstname.lastname@domain.com` → Extract "firstname"
  - `firstnamelastname@domain.com` → Use name database to split (nameparser library)
  - `flastname@domain.com` → "f" = first initial, harder to extract full name
- **Time:** Automated (seconds via script)
- **Success rate:** 60-80% (depends on email pattern clarity)
- **Responsible:** AI Team (script using nameparser or similar)

**B. LinkedIn Profile Check (Manual, 95%+ success)**
- **How:** Search LinkedIn for "First Last @ Company" → Get full name from profile
- **Time:** 2-3 min/record
- **Success rate:** 95%+ (if profile exists and name is public)
- **Responsible:** LG Team (distribute across team)

**C. Apollo.io or Clearbit Enrichment (Paid, 85-90% success)**
- **How:** Upload email address → Tool returns full name + other fields (role, company, etc.)
- **Cost:** Apollo.io $49/month (1,000 enrichments), Clearbit $99/month (2,500 enrichments)
- **Time:** Bulk upload (1,000 records in ~10 min)
- **Success rate:** 85-90%
- **Responsible:** AI Team (bulk upload) or LG Team (manual lookup for high-value)

**D. Company Website or Press Releases (Manual, 50-70% success)**
- **How:** Google "[Person's email] OR [Last name] [Company name]" → Find mentions in press, team pages, articles
- **Time:** 3-5 min/record
- **Success rate:** 50-70% (works for public-facing roles: executives, sales, marketing)
- **Responsible:** LG Team (for high-value accounts only)

**Recommended Approach:**
- **All records:** Run tactic A (email extraction) first (free, fast)
- **Still missing (~40%):** Run tactic C (Apollo/Clearbit) for bulk enrichment
- **High-value accounts still missing:** Tactic B (LinkedIn manual check)
- **Set fallback:** For any remaining, use "Hi" or "Hello" as {{FirstName}} fallback

---

#### 4. Role/Title Identification

**Challenge:** X records missing role (Y%), limits persona-based targeting

**Tactics:**

**A. LinkedIn Profile Check (Manual, 90%+ success)**
- **How:** Find person on LinkedIn → Current job title usually displayed prominently
- **Time:** 2-3 min/record
- **Success rate:** 90%+ (if profile exists)
- **Responsible:** LG Team

**B. Apollo.io or Clearbit Enrichment (Paid, 80-85% success)**
- **How:** Upload email/name → Tool returns job title + seniority level
- **Cost:** Apollo.io $49/month, Clearbit $99/month
- **Time:** Bulk upload (1,000 records in ~10 min)
- **Success rate:** 80-85%
- **Responsible:** AI Team

**C. Company Website "Team" Page (Manual, 60-70% success)**
- **How:** Visit company website → Find "Team" or "Leadership" page → Match name to title
- **Time:** 3-5 min/record
- **Success rate:** 60-70% (smaller companies more likely to have public team pages)
- **Responsible:** LG Team

**D. Email Signature Scraping (Manual, 40-50% success)**
- **How:** If you have previous email exchanges, check signature for title
- **Time:** 1-2 min/record (if previous emails exist)
- **Success rate:** 40-50% (only works for Ex-Clients or First-Call segments)
- **Responsible:** Sales Team (Anastasia) or LG Team

**Recommended Approach:**
- **High-value accounts:** Tactic A (LinkedIn manual) or B (Apollo/Clearbit bulk)
- **Medium-value accounts:** Tactic B (bulk enrichment)
- **Low-value or if still missing:** Infer from email domain or company size (small company = likely Founder/CEO, large company SaaS domain = likely Product/Marketing)

---

#### 5. Language Detection

**Challenge:** X records missing language tag (Y%), risk of sending English to non-English speakers

**Tactics:**

**A. Country Code → Language Mapping (Automated, 70-80% accuracy)**
- **How:** Use country code to infer primary language:
  - `UA` → Ukrainian
  - `RU`, `BY`, `KZ` → Russian
  - `PL` → Polish
  - `AT`, `DE`, `CH` → German (but many speak English in business)
  - `FR`, `BE` → French
  - `US`, `CA`, `GB`, `AU`, `NZ` → English
- **Time:** Automated (instant via script)
- **Success rate:** 70-80% (not perfect, e.g., many EU countries use English for business)
- **Responsible:** AI Team (script)

**B. Company Website Language Detection (Manual or Automated, 85-90% accuracy)**
- **How:** Visit company website → Detect primary language of content (HTML lang attribute or content analysis)
- **Tools:** LangDetect (Python library), Google Cloud Translation API (detect language endpoint)
- **Time:** Automated (seconds per domain) or manual (1-2 min/record)
- **Success rate:** 85-90%
- **Responsible:** AI Team (script) or LG Team (manual for high-value)

**C. LinkedIn Profile Language (Manual, 80-85% success)**
- **How:** Check LinkedIn profile language or posts language
- **Time:** 1-2 min/record (while checking other fields)
- **Success rate:** 80-85% (profiles often in native language)
- **Responsible:** LG Team (combine with first name/role lookup)

**D. Email Domain Analysis (Manual, 60-70% success)**
- **How:** `.ua` domains → Ukrainian, `.ru` → Russian, `.pl` → Polish, `.de` → German, etc.
- **Time:** Automated (instant via script)
- **Success rate:** 60-70% (many companies use `.com` regardless of region)
- **Responsible:** AI Team (script)

**Recommended Approach:**
- **All records:** Run tactic A (country → language) + D (domain analysis) first (free, fast)
- **EU records with unclear language:** Run tactic B (website language detection)
- **High-value accounts still unclear:** Tactic C (LinkedIn manual check)
- **Default assumption:** If unclear and located in EU/Ukraine/Asia → assume English as safe fallback (most business professionals speak English)

---

#### 6. Country/Region Mapping

**Challenge:** X records missing country (Y%), affects timezone and localization

**Tactics:**

**A. Domain WHOIS Lookup (Automated, 60-70% accuracy)**
- **How:** Query WHOIS database for company domain → Extract registrant country
- **Time:** Automated (1-2 sec/record)
- **Success rate:** 60-70% (many domains use privacy protection, hiding country)
- **Responsible:** AI Team (script using WHOIS API)

**B. LinkedIn Profile Location (Manual, 90%+ success)**
- **How:** Check LinkedIn profile → Location usually displayed
- **Time:** 1-2 min/record (combine with first name/role lookup)
- **Success rate:** 90%+
- **Responsible:** LG Team

**C. Company Website Footer or "Contact" Page (Manual, 70-80% success)**
- **How:** Visit website → Check footer for address, contact page, or "Locations"
- **Time:** 2-3 min/record
- **Success rate:** 70-80%
- **Responsible:** LG Team

**D. Apollo.io or Clearbit Enrichment (Paid, 80-85% success)**
- **How:** Upload company domain → Tool returns HQ location
- **Cost:** Included with Apollo/Clearbit plans
- **Time:** Bulk upload (1,000 records in ~10 min)
- **Success rate:** 80-85%
- **Responsible:** AI Team

**Recommended Approach:**
- **All records:** Run tactic A (WHOIS) first (free, fast)
- **Still missing (~30-40%):** Run tactic D (Apollo/Clearbit bulk) or B (LinkedIn manual for high-value)
- **Last resort:** Infer from email domain TLD (`.ua` = Ukraine, `.de` = Germany, etc.) but less reliable

---

#### 7. Industry Classification

**Challenge:** X records missing industry (Y%), limits vertical-specific messaging

**Tactics:**

**A. Website Content Analysis (Automated, 75-85% accuracy)**
- **How:** Scrape company website → Analyze keywords, meta tags, page titles → Classify into industry
- **Tools:** Clearbit Reveal, BuiltWith, or custom NLP script
- **Time:** Automated (5-10 sec/record)
- **Success rate:** 75-85%
- **Responsible:** AI Team (script using Clearbit API or custom NLP)

**B. LinkedIn Company Page (Manual, 90%+ success)**
- **How:** Find company on LinkedIn → Industry tag displayed on company page
- **Time:** 2-3 min/record
- **Success rate:** 90%+
- **Responsible:** LG Team

**C. Apollo.io or Clearbit Enrichment (Paid, 85-90% success)**
- **How:** Upload company domain → Tool returns industry classification
- **Cost:** Included with Apollo/Clearbit plans
- **Time:** Bulk upload (1,000 records in ~10 min)
- **Success rate:** 85-90%
- **Responsible:** AI Team

**D. Manual Research via Google (Manual, 80-90% success)**
- **How:** Google "[Company name] industry" or "[Company name] what do they do"
- **Time:** 3-5 min/record
- **Success rate:** 80-90%
- **Responsible:** LG Team (for high-value accounts)

**Recommended Approach:**
- **All records:** Run tactic A (website analysis) or C (Apollo/Clearbit bulk) first
- **Still missing or unclear:** Tactic B (LinkedIn company page) for high-value
- **Low-priority records:** Leave blank or infer from context (SaaS keywords in website = SaaS industry)

---

#### 8. LinkedIn URL Discovery

**Challenge:** X records missing LinkedIn URL (Y%), limits fallback outreach

**Tactics:**

**A. LinkedIn Search by Name + Company (Manual, 80-90% success)**
- **How:** Search LinkedIn for "[First Name] [Last Name] [Company]" → Copy profile URL
- **Time:** 2-3 min/record
- **Success rate:** 80-90% (if person has LinkedIn profile)
- **Responsible:** LG Team

**B. Google Search "[Name] LinkedIn [Company]" (Manual, 75-85% success)**
- **How:** Google search often surfaces LinkedIn profile as top result
- **Time:** 1-2 min/record
- **Success rate:** 75-85%
- **Responsible:** LG Team

**C. LinkedIn Sales Navigator (Paid, 85-90% success + advanced filters)**
- **How:** Use Sales Navigator's advanced search (filter by company, role, location) → Export profile URLs
- **Cost:** $79.99/month per user (Remote Helpers may already have accounts)
- **Time:** Bulk search (find 50-100 profiles in 10-15 min), export URLs
- **Success rate:** 85-90%
- **Responsible:** LG Team (assign to members with Sales Navigator access)

**Recommended Approach:**
- **High-value accounts (top 20%):** Tactic A or C (manual search or Sales Navigator)
- **Medium-value accounts:** Defer to post-campaign (only enrich if email bounces or no response)
- **Low-value accounts:** Skip (LinkedIn is fallback channel, not primary)

---

#### 9. Phone Number Discovery

**Challenge:** X records missing phone (Y%), limits warm lead fallback

**Tactics:**

**A. Apollo.io or Lusha (Paid, 60-70% success for direct dials)**
- **How:** Upload email/name → Tool returns direct dial or company number
- **Cost:** Apollo $49/month, Lusha $99/month
- **Time:** Bulk upload (1,000 records in ~10 min)
- **Success rate:** 60-70% for direct dials (higher for company switchboards)
- **Responsible:** AI Team

**B. Company Website Contact Page (Manual, 70-80% success for main number)**
- **How:** Visit website "Contact" page → Extract phone number
- **Time:** 2-3 min/record
- **Success rate:** 70-80% (usually company main line, not direct dial)
- **Responsible:** LG Team

**C. LinkedIn Profile Contact Info (Manual, 30-40% success)**
- **How:** Check LinkedIn profile "Contact Info" section (many users don't share phone)
- **Time:** 1-2 min/record (combine with other LinkedIn lookups)
- **Success rate:** 30-40%
- **Responsible:** LG Team

**Recommended Approach:**
- **Warm leads only (Segment C):** Prioritize phone enrichment for potential follow-up calls
- **Tactic:** Use A (Apollo/Lusha bulk) for top warm leads, or B (website manual) for high-value
- **All others:** Skip (phone is tertiary fallback, low ROI for cold outreach)

---

## Enrichment Backlog Output

### Format: Kanban-Ready Tasks

**For each enrichment field, provide:**

```
FIELD: [Field Name]
PRIORITY: [Tier 1: Critical / Tier 2: High / Tier 3: Medium / Tier 4: Low]
MISSING IN: [X records (Y% of total)]
IMPACT ON SENDABILITY: [+Z points avg if enriched]
IMPACT ON CONVERSION: [+W% reply rate or +V% meeting rate]

RECOMMENDED TACTIC: [Tactic A/B/C from above]
TOOL REQUIRED: [Hunter.io / Apollo.io / LinkedIn / Manual / Script]
COST: [Free / $X/month or $Y/record]
TIME ESTIMATE: [X min/record manual, or Y sec/record automated]
TOTAL TIME: [X hours for all records]
RESPONSIBLE: [LG Team / AI Team / Sales Team]

EXPECTED UPLIFT:
- Sendability score: [+Z points avg]
- Conversion rate: [+W% reply rate]
- Fallback channel access: [Yes/No - if LinkedIn/phone enrichment]

KANBAN TASK CARD:
---
Title: Enrich [Field] for [X] records
Description: [Brief description of tactic]
Assignee: [Team member name(s)]
Due Date: [Based on campaign timeline]
Labels: [Tier 1 / Tier 2 / Tier 3 / Tier 4], [Manual / Automated], [High ROI / Medium ROI / Low ROI]
Effort: [X hours]
Priority: [1-4]
---
```

---

## Example Enrichment Backlog

### Tier 1: Critical (Must Complete Before Send)

#### Task 1: Email Validation
```
FIELD: Email Validation
PRIORITY: Tier 1 - Critical
MISSING IN: 87 emails need validation (12% of total)
IMPACT ON SENDABILITY: +40 points (prevents bounces, protects domain reputation)

RECOMMENDED TACTIC: Hunter.io Email Verifier (bulk upload)
TOOL REQUIRED: Hunter.io (or NeverBounce/ZeroBounce)
COST: $0.02/email (Hunter.io) = $1.74 for 87 emails, or use Hunter plan if available
TIME ESTIMATE: Bulk upload = 10 min total
RESPONSIBLE: AI Team (Nikolay Artemchuk) - upload CSV, download results

EXPECTED UPLIFT:
- Sendability score: +40 points avg (invalid emails flagged, removed before send)
- Deliverability: Reduce bounce rate from ~8% to <2%
- Domain reputation: Protect sender score

KANBAN TASK CARD:
---
Title: Validate 87 email addresses before send
Description: Upload email list to Hunter.io Email Verifier, flag invalid/risky, remove from campaign
Assignee: Nikolay Artemchuk (AI Team)
Due Date: [Campaign Day 0 - before first send]
Labels: Tier 1, Automated, High ROI, Deliverability
Effort: 0.5 hours
Priority: 1
---
```

---

#### Task 2: First Name Extraction
```
FIELD: First Name
PRIORITY: Tier 2 - High (blocks personalization)
MISSING IN: 142 records (18% of total)
IMPACT ON SENDABILITY: +15 points
IMPACT ON CONVERSION: +20-30% reply rate (personalized emails outperform generic)

RECOMMENDED TACTIC:
- Step 1: Email prefix extraction (automated) - free, 60-80% success
- Step 2: Apollo.io bulk enrichment for remaining - $49/month, 85% success
- Step 3: LinkedIn manual check for high-value accounts still missing - manual, 95% success

TOOL REQUIRED: Script (nameparser) + Apollo.io + LinkedIn
COST: Free (script) + $49/month (Apollo) = ~$50 total
TIME ESTIMATE:
- Step 1: Automated (instant for all 142)
- Step 2: Bulk upload (10 min for ~60 remaining)
- Step 3: Manual (3 min/record × 10 high-value = 30 min)
TOTAL TIME: ~1 hour
RESPONSIBLE: AI Team (steps 1-2), LG Team (step 3 - Hanan, Nataliia)

EXPECTED UPLIFT:
- Sendability score: +15 points avg
- Reply rate: +25% avg (personalization effect)
- Open rate: +10% (personalized subject lines)

KANBAN TASK CARD:
---
Title: Extract/enrich first names for 142 records
Description: Run email extraction script → Apollo bulk enrichment → Manual LinkedIn for top 10 accounts
Assignee: Nikolay (steps 1-2), Hanan + Nataliia (step 3)
Due Date: [Day 1 of campaign prep]
Labels: Tier 2, Hybrid (Auto + Manual), High ROI, Personalization
Effort: 1 hour
Priority: 2
---
```

---

### Tier 3: Medium (Improves Targeting)

#### Task 3: Language Detection
```
FIELD: Language
PRIORITY: Tier 3 - Medium
MISSING IN: 95 records (12% of total)
IMPACT ON CONVERSION: +10-20% reply rate (sending in recipient's native language)

RECOMMENDED TACTIC:
- Step 1: Country code → language mapping (automated) - free, 75% success
- Step 2: Website language detection (automated script) - free, 85% success
- Step 3: Manual LinkedIn check for EU accounts unclear - manual, 80% success

TOOL REQUIRED: Script (country mapping + LangDetect library) + LinkedIn
COST: Free
TIME ESTIMATE:
- Step 1: Automated (instant for all 95)
- Step 2: Automated (5 sec/record × 25 remaining = 2 min)
- Step 3: Manual (2 min/record × 10 high-value EU accounts = 20 min)
TOTAL TIME: ~30 min
RESPONSIBLE: AI Team (steps 1-2), LG Team (step 3 - Kseniia, Anna for UK/RU/PL)

EXPECTED UPLIFT:
- Reply rate: +15% avg (multi-language personalization)
- Conversion rate: +10% (better resonance with native language emails)

KANBAN TASK CARD:
---
Title: Detect language for 95 records
Description: Run country→language + website language scripts → Manual LinkedIn for top 10 EU accounts
Assignee: Nikolay (steps 1-2), Kseniia + Anna (step 3)
Due Date: [Day 2 of campaign prep]
Labels: Tier 3, Hybrid, Medium ROI, Localization
Effort: 0.5 hours
Priority: 3
---
```

---

### Tier 4: Low (Nice to Have - Defer if Limited Time)

#### Task 4: LinkedIn URL Discovery
```
FIELD: LinkedIn URL
PRIORITY: Tier 4 - Low (fallback channel, not primary)
MISSING IN: 234 records (30% of total)
IMPACT: Enables LinkedIn outreach if email fails (fallback value)

RECOMMENDED TACTIC: Defer to post-send (only enrich for records that bounce or don't open after Touch 2)
- If needed post-send: LinkedIn manual search (3 min/record)

TOOL REQUIRED: LinkedIn (manual search)
COST: Free (or $80/month for Sales Navigator if bulk needed)
TIME ESTIMATE: 3 min/record × ~50 expected non-responders = 2.5 hours post-send
RESPONSIBLE: LG Team (Anna, Nataliia, Plamena for EU; Anush for CIS; Archibong for Africa)

EXPECTED UPLIFT:
- Fallback channel access: ~15-20% of non-responders can be re-engaged via LinkedIn
- Meeting rate: +2-5% from LinkedIn fallback touches

KANBAN TASK CARD:
---
Title: Enrich LinkedIn URLs for bounced/non-opened emails (post-send)
Description: After Day 6 (Touch 2), identify bounced/non-opened emails → Manual LinkedIn search for top 50
Assignee: Anna, Nataliia, Plamena, Anush, Archibong (distribute workload)
Due Date: [Day 7 - after Touch 2 results analyzed]
Labels: Tier 4, Manual, Low ROI (unless email fails), Fallback
Effort: 2.5 hours (post-send)
Priority: 4
---
```

---

## Deliverables

**For each enrichment plan request, provide:**

### 1. Executive Summary
```
TOTAL RECORDS: [X]
CURRENT AVG SENDABILITY: [Y / 100]
TARGET AVG SENDABILITY: [Z / 100]
GAP TO CLOSE: [Z - Y points]

ENRICHMENT SCOPE:
- Tier 1 tasks: [X tasks, Y hours, $Z cost]
- Tier 2 tasks: [X tasks, Y hours, $Z cost]
- Tier 3 tasks: [X tasks, Y hours, $Z cost]
- Tier 4 tasks: [X tasks, Y hours, $Z cost]

TOTAL EFFORT: [X hours across LG + AI teams]
TOTAL COST: [$Y for tools]
TIMELINE: [Z days before campaign ready]

EXPECTED OUTCOMES:
- Sendability score increase: [+X points avg]
- Records ready to send: [Y → Z (A% increase)]
- Reply rate uplift: [+B% expected]
```

### 2. Prioritized Task List (Kanban Format)
```
[List of Kanban cards as shown above, sorted by Priority 1-4]
```

### 3. Tool Budget Breakdown
```
TOOL | COST | USAGE | RESPONSIBLE | ROI
Hunter.io | $49/month or $0.02/email | Email validation + finding | AI Team | High (prevents bounces)
Apollo.io | $49/month | Bulk enrichment (name, role, country) | AI Team | High (multi-field)
LinkedIn Sales Navigator | $80/month | LinkedIn URL discovery (bulk) | LG Team | Medium (fallback)
Clearbit | $99/month | Industry + advanced enrichment | AI Team | Medium (targeting)
NeverBounce | $0.008/email | Email validation (cheaper bulk option) | AI Team | High (deliverability)

TOTAL MONTHLY COST: $X
ONE-TIME COST (if bulk verification): $Y
```

### 4. Team Workload Distribution
```
TEAM MEMBER | TASKS ASSIGNED | ESTIMATED HOURS | EXPERTISE NEEDED
Nikolay Artemchuk (AI) | Email validation, scripts, Apollo bulk | 2 hours | Python scripting, tool APIs
Hanan Zaheur (LG) | First name enrichment (manual), data prep | 1.5 hours | LinkedIn research, data entry
Nataliia Rybak (LG) | First name enrichment (manual), reporting | 1.5 hours | LinkedIn research, Ukrainian language
Kseniia Shkinder (LG) | Language detection (manual), translation QA | 1 hour | Multi-language (UK/RU/PL)
Anna Burda (LG) | Role enrichment (manual), language detection | 2 hours | LinkedIn research, sales context
[Continue for all 11 LG team members...]

TOTAL TEAM HOURS: [X hours]
AVG HOURS PER PERSON: [Y hours over Z days]
```

### 5. Timeline & Milestones
```
DAY 0 (Today): Kickoff enrichment plan, assign tasks
DAY 1: Complete Tier 1 (email validation) - BLOCKING
DAY 2: Complete Tier 2 (first name, role) - HIGH PRIORITY
DAY 3: Complete Tier 3 (language, country) - MEDIUM PRIORITY
DAY 4: QA enriched data, re-run sendability scoring
DAY 5: Campaign ready to send (Tier 4 deferred to post-send)

MILESTONE CHECKS:
- Day 1 EOD: Email validation complete (bounce risk eliminated)
- Day 2 EOD: Personalization fields complete ({{FirstName}}, {{Role}} ready)
- Day 4 EOD: Sendability score ≥80 for target segments
```

---

## Usage Instructions

**Step 1: Input CRM Data Quality Report**
- Use output from **CRM Export Normalizer** (Prompt #1)
- Note field-level completeness (% missing per field)
- Note current sendability score average

**Step 2: Set Enrichment Goals**
- Target sendability score (default: ≥80)
- Budget available for tools
- Timeline (days until campaign launch)
- LG Team availability (hours)

**Step 3: Run Enrichment Plan Generator**
- Paste this prompt + CRM data + goals into Claude, ChatGPT, or Gemini
- Specify: "Generate data enrichment plan using Remote Helpers framework"

**Step 4: Review Output**
- Validate prioritization (Tier 1-4) aligns with campaign urgency
- Check budget fits within available funds
- Confirm team workload is realistic (don't overload LG team)

**Step 5: Approve & Assign Tasks**
- Get approval from Sales (Anastasia) for budget
- Assign tasks via Kanban board (Notion, Trello, or Google Sheets)
- Set deadlines aligned with campaign launch date

**Step 6: Execute Enrichment**
- **Tier 1 (Day 0-1):** Email validation (AI Team - Nikolay)
- **Tier 2 (Day 1-2):** First name, role enrichment (AI + LG Team)
- **Tier 3 (Day 2-3):** Language, country, industry (AI + LG Team)
- **Tier 4 (Post-send):** LinkedIn, phone (LG Team, as needed for fallback)

**Step 7: QA Enriched Data**
- Re-run **CRM Export Normalizer** (Prompt #1) after enrichment
- Validate sendability score increased (target: ≥80)
- Check for new errors introduced (typos, wrong names, etc.)

**Step 8: Launch Campaign**
- Use enriched data with **14-Day Action Plan** (Prompt #2)
- Proceed to **Personalized Outreach Writer** (Prompt #3) for copy

---

## Integration with Remote Helpers Stack

**Tools Used:**
- **Enrichment:** Hunter.io, Apollo.io, Clearbit, FullContact, Lusha, LinkedIn Sales Navigator
- **Validation:** NeverBounce, ZeroBounce, Hunter.io Email Verifier
- **Automation:** Python scripts (nameparser, LangDetect, WHOIS), Google Cloud APIs
- **Project Management:** Notion/Trello Kanban boards, Google Sheets
- **AI Analysis:** ChatGPT, Claude, Perplexity AI

**Department Collaboration:**
- **LG Team (11 members):** Manual enrichment (LinkedIn, website research, language detection)
- **AI Team (Nikolay, Matvii, Vladislav):** Automation scripts, bulk tool uploads, QA
- **Sales Team (Anastasia):** Budget approval, high-value account prioritization

---

## Version History

**v1.0 (2025-11-11):**
- Initial release
- 4-tier prioritization framework (Critical / High / Medium / Low)
- 9 enrichment fields with tactics (Email, Validation, First Name, Role, Language, Country, Industry, LinkedIn, Phone)
- Kanban-ready task format
- Tool budget breakdown
- Team workload distribution
- Integration with CRM Export Normalizer (Prompt #1) and 14-Day Action Plan (Prompt #2)

---

**Next Step:** Execute enrichment plan per timeline, re-run CRM Normalizer to validate uplift, then proceed to 14-Day Action Plan for campaign execution.
