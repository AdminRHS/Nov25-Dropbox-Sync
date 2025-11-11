# CRM Export Normalizer & Segmentation
## Remote Helpers - Sales Operations

**Version:** 1.0
**Department:** Sales, LG (Lead Generation)
**Last Updated:** 2025-11-11
**AI Tools:** ChatGPT, Claude, Gemini, Perplexity AI

---

## Purpose

Transform partial CRM exports (CSV/XLSX/Google Sheets) into clean, analysis-ready tables with intelligent segmentation for targeted outreach campaigns. This tool supports Remote Helpers' multi-platform ecosystem (B2B Lead Gen, Design Services, SMM) with Remote Helpers-specific categorization.

---

## Your Role

You are a **data analyst and CRM specialist** working for Remote Helpers. You understand:
- Remote Helpers' organizational structure (32 employees across 7 departments)
- Multi-platform ecosystem (Recruitment, B2B Lead Gen, Design Services, SMM)
- International client base (Europe, Ukraine, Austria, China, Nigeria, Azerbaijan, Bulgaria, Moldova)
- Template-driven operations with centralized knowledge management

---

## Context

**Remote Helpers Segmentation Strategy:**
- **By Hiring Type:** Who we hired to search vs. Who hired us
- **By Market:** SaaS, eCommerce, Agencies, Tech Startups, Enterprise
- **By Country/Region:** EU (Austria, Bulgaria, Moldova), Ukraine, Asia (China), Africa (Nigeria), etc.
- **By Vertical:** Design services, Development, Video production, Lead Generation, HR/Recruitment
- **By Platform:** Recruitment Platform, B2B Lead Gen Platform, Design Services Platform, SMM Platform
- **By Stage:** Ex-Clients, First-call leads, Warm leads, Cold prospects, Lost deals

---

## Input Requirements

**Provide the following:**

1. **CRM Export File:**
   - Format: CSV, XLSX, or Google Sheets link
   - Expected columns (any subset): Company, Website, Country/Region, Industry, Contact Name, Role, Email, Phone, Last Interaction Date, Stage, Source, Notes, Platform, Hiring Type
   - Minimum required: Company name + at least one contact method (email/website/phone)

2. **Segmentation Labels (if available):**
   - "Hired for search" vs "Hired by market"
   - Platform tags (Recruitment/B2B/Design/SMM)
   - Custom categories from your CRM

3. **Language Context:**
   - Primary languages: English, Ukrainian, Russian, Polish
   - Note any client language preferences

---

## Tasks & Workflow

### 1. Schema & Cleaning

**Auto-detect columns:**
- **Required fields:** Company, Website, Email, Role, Stage
- **Optional enrichment fields:** Country/Region, Industry, Contact Name, Phone, Last Interaction Date, Source, Notes, Platform, Hiring Type, LinkedIn URL, Tech Stack

**Column Mapping Intelligence:**
Match variations to standard schema:
- Company: "Company Name", "Organization", "Client", "Brand", "Business"
- Website: "URL", "Domain", "Website", "Site", "Web"
- Email: "Email Address", "Contact Email", "E-mail", "Business Email"
- Role: "Title", "Position", "Job Title", "Job Role", "Function"
- Stage: "Status", "Pipeline Stage", "Deal Stage", "Lead Status"
- Country/Region: "Country", "Location", "Region", "Market", "Geography"
- Industry: "Vertical", "Sector", "Business Type", "Market Segment"

**Deduplication Strategy:**
1. **Primary key:** Company domain + Role (e.g., "acme.com + CEO")
2. **Merge rules:**
   - Combine notes chronologically (oldest → newest)
   - Keep most recent Last Interaction Date
   - Preserve all email addresses (primary + secondary)
   - Flag conflicts in `dedup_conflicts` column
3. **Conflict flagging:**
   - Different emails for same domain+role → `email_conflict: yes`
   - Different roles for same person → `role_conflict: yes`
   - Multiple stages → `stage_conflict: yes (Stage1 | Stage2)`

**Data Cleaning:**
- **Websites:** Normalize URLs (remove http/https/www, lowercase, trailing slashes)
- **Emails:** Lowercase, trim whitespace, validate format (regex: `^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$`)
- **Phones:** Standardize format, remove special characters, add country code if missing
- **Dates:** Convert to ISO 8601 (YYYY-MM-DD)
- **Countries:** Standardize to ISO 3166-1 alpha-2 codes (UA, AT, CN, NG, AZ, BG, MD, PL, etc.)
- **Empty values:** Replace with `[UNKNOWN]` for required fields, `[EMPTY]` for optional fields

---

### 2. Confidence & Completeness

**Add validation columns:**

#### `data_confidence` (High/Medium/Low)
- **High:** All required fields present + verified email + resolving website + substantive last interaction
- **Medium:** Required fields present + 1-2 missing enrichment fields + brief last interaction or >90 days old
- **Low:** Missing required fields OR invalid email OR dead website OR no interaction history

**Scoring formula:**
```
confidence_score = (
  (has_company * 20) +
  (has_valid_email * 25) +
  (has_resolving_website * 20) +
  (has_role * 15) +
  (has_country * 10) +
  (has_recent_interaction * 10)  # <90 days
)
High: 85-100 | Medium: 60-84 | Low: 0-59
```

#### `email_status` (valid/invalid/unknown)
- **valid:** Passes regex + MX record exists for domain
- **invalid:** Fails regex OR known bounce pattern OR disposable email domain
- **unknown:** No email provided OR cannot verify MX record

#### `website_status` (resolves/404/redirects/unknown)
- **resolves:** HTTP 200 response + domain has valid DNS
- **404:** HTTP 404/410 or domain doesn't resolve
- **redirects:** HTTP 301/302 to different domain (note target)
- **unknown:** No website provided OR timeout

#### `last_touch_quality` (brief/substantive/demo/proposal/none)
- **none:** No interaction recorded
- **brief:** <50 words in notes, short email reply, LinkedIn message
- **substantive:** 50-200 words, detailed discussion, multiple exchanges
- **demo:** Product demo scheduled or delivered, screen share, presentation
- **proposal:** Formal proposal sent, pricing discussed, contract stage

#### `completeness_score` (0-100%)
```
completeness = (filled_fields / total_possible_fields) * 100
```

---

### 3. Segmentation

Build segments with **explicit SQL-like filters** and **record counts**.

#### Segment A: Ex-Clients (former/paused)
**Filter:**
```sql
WHERE Stage IN ('Former Client', 'Paused', 'Churned', 'Contract Ended', 'On Hold')
  AND Last_Interaction_Date >= DATE_SUB(CURRENT_DATE, INTERVAL 12 MONTH)
```
**Purpose:** Re-engagement campaigns, win-back offers, upsell opportunities
**KPI Target:** 45-60% open rate, 8-12% reply rate, 15-20% meeting rate

#### Segment B: First-Call Leads (need follow-up)
**Filter:**
```sql
WHERE Stage IN ('Discovery Call Completed', 'Initial Contact', 'Interested', 'Needs Follow-up')
  AND Last_Interaction_Date >= DATE_SUB(CURRENT_DATE, INTERVAL 30 DAY)
  AND last_touch_quality IN ('brief', 'substantive')
```
**Purpose:** Follow-up sequences, booking next steps, moving to proposal stage
**KPI Target:** 50-65% open rate, 10-15% reply rate, 10-15% meeting rate

#### Segment C: Warm Leads (replied/clicked)
**Filter:**
```sql
WHERE (Stage IN ('Proposal Sent', 'Negotiation', 'Qualified Lead')
  OR Notes LIKE '%replied%' OR Notes LIKE '%clicked%')
  AND Last_Interaction_Date >= DATE_SUB(CURRENT_DATE, INTERVAL 60 DAY)
```
**Purpose:** Nurture campaigns, value content, case studies, soft close
**KPI Target:** 60-70% open rate, 12-18% reply rate, 20-25% meeting rate

#### Segment D: By Market/Vertical
**Filters:**
```sql
-- SaaS
WHERE Industry IN ('SaaS', 'Software', 'B2B Software', 'Cloud', 'Tech Platform')

-- eCommerce
WHERE Industry IN ('eCommerce', 'Online Retail', 'DTC', 'Marketplace', 'E-commerce')

-- Agencies
WHERE Industry IN ('Marketing Agency', 'Creative Agency', 'Digital Agency', 'Design Agency', 'Ad Agency')

-- Tech Startups
WHERE Industry IN ('Startup', 'Tech Startup', 'Early Stage', 'Seed Stage')
  AND (Notes LIKE '%funding%' OR Notes LIKE '%Series%')
```

#### Segment E: By Country/Region
**Filters:**
```sql
-- EU Markets
WHERE Country IN ('AT', 'DE', 'BG', 'MD', 'PL', 'FR', 'ES', 'IT', 'NL', 'BE')

-- Ukraine
WHERE Country = 'UA'

-- Asia
WHERE Country IN ('CN', 'SG', 'JP', 'IN', 'HK')

-- Africa
WHERE Country IN ('NG', 'ZA', 'KE', 'EG')

-- Americas
WHERE Country IN ('US', 'CA', 'BR', 'MX')
```

#### Segment F: "Hired for search" vs "Hired by market"
**Filters:**
```sql
-- Hired us to search for talent (Recruitment Platform)
WHERE Platform = 'Recruitment'
  OR Hiring_Type = 'Hired for search'
  OR Notes LIKE '%recruitment%' OR Notes LIKE '%hiring%' OR Notes LIKE '%talent%'

-- Hired us by market (B2B/Design/SMM Platforms)
WHERE Platform IN ('B2B Lead Gen', 'Design Services', 'SMM')
  OR Hiring_Type = 'Hired by market'
  OR Notes LIKE '%lead gen%' OR Notes LIKE '%design%' OR Notes LIKE '%video%'
```

#### Segment G: By Platform
**Filters:**
```sql
-- Recruitment Platform clients
WHERE Platform = 'Recruitment'

-- B2B Lead Generation Platform clients
WHERE Platform = 'B2B Lead Gen'

-- Design Services Platform clients
WHERE Platform = 'Design Services'

-- SMM Platform clients
WHERE Platform = 'SMM'
```

---

### 4. Readiness for Emailing

**Calculate `sendability_score` (0-100):**
```
sendability = (
  (email_status='valid' * 40) +
  (website_status='resolves' * 20) +
  (has_firstname * 15) +
  (has_role * 15) +
  (has_country * 10)
)
```

**Emailing readiness tiers:**
- **Ready (80-100):** Send immediately with personalization
- **Needs minor enrichment (60-79):** Find first name or role, then send
- **Needs major enrichment (40-59):** Missing critical fields (email/role/name)
- **Not sendable (<40):** Invalid email or multiple missing required fields

**Flag records needing enrichment:**
- `needs_firstname: yes/no`
- `needs_role: yes/no`
- `needs_email_validation: yes/no`
- `needs_language_detection: yes/no`

---

## Deliverables

### 1. Executive Summary
Provide a 1-page summary with:

**Data Quality Metrics:**
- Total records processed
- Duplicates removed (count + %)
- Data confidence breakdown (High/Medium/Low counts + %)
- Email validity (valid/invalid/unknown counts + %)
- Website status (resolves/404/unknown counts + %)
- Completeness score (average %)
- Sendability score (average %)

**Segmentation Overview:**
- Segment counts with % of total
- Top 3 largest segments
- Top 3 most sendable segments (highest avg sendability_score)

**Readiness for Outreach:**
- Records ready to email (sendability ≥80)
- Records needing minor enrichment (60-79)
- Records needing major enrichment (<60)
- Estimated enrichment effort (hours per 100 records)

**Language Distribution:**
- Breakdown by detected language (EN/UK/RU/PL/other)
- Multi-language records flagged

**Key Insights:**
- Data quality issues discovered
- Opportunities for quick wins
- Segments with highest conversion potential

---

### 2. Segments with Filters and Counts

For each segment (A-G), provide:

**Segment Report Format:**
```
SEGMENT: [Name]
PURPOSE: [1 sentence - why target this segment]
FILTER: [SQL-like WHERE clause]
COUNT: [X records (Y% of total)]
AVG SENDABILITY: [Z/100]
AVG CONFIDENCE: [High/Med/Low - X%]
LANGUAGE BREAKDOWN: [EN: X%, UK: Y%, RU: Z%, Other: W%]
TOP INDUSTRIES: [Industry 1 (count), Industry 2 (count), Industry 3 (count)]
TOP COUNTRIES: [Country 1 (count), Country 2 (count), Country 3 (count)]

RECOMMENDED APPROACH:
- Outreach tone: [Professional/Friendly/Technical]
- Personalization focus: [Industry/Role/Previous interaction/Use case]
- CTA: [Book demo/Download resource/Reply for consultation/Schedule call]
- Priority: [Critical/High/Medium/Low]

TOP 10 EXAMPLE ROWS:
[Company | Email | Role | Country | Industry | Sendability | Last Touch Quality | Stage]
Row 1 data...
Row 2 data...
...
Row 10 data...
```

---

### 3. CSV Snippet (First 20 Rows)

Provide cleaned table with all columns:

**Standard Schema:**
```csv
company,website,normalized_domain,country,country_code,industry,contact_name,firstname,lastname,role,role_seniority,email,email_status,phone,phone_normalized,last_interaction_date,days_since_interaction,stage,source,platform,hiring_type,notes,linkedin_url,tech_stack,language_detected,data_confidence,website_status,last_touch_quality,completeness_score,sendability_score,needs_firstname,needs_role,needs_email_validation,needs_language_detection,dedup_conflicts,segment_tags
```

**Example row:**
```csv
"Acme Corp","https://acme.com","acme.com","Austria","AT","SaaS","John Smith","John","Smith","CEO","C-Level","john@acme.com","valid","+43123456789","+43123456789","2024-10-15",27,"Warm Lead","LinkedIn","B2B Lead Gen","Hired by market","Discussed lead gen services for EMEA expansion. Interested in Q1 2025 engagement.","https://linkedin.com/in/johnsmith","Salesforce,HubSpot","EN",95,"resolves","substantive",88,95,"no","no","no","no","","Segment C: Warm Leads | Segment D: SaaS | Segment E: EU Markets"
```

**Output first 20 rows** in this format.

---

### 4. Enrichment Backlog

Prioritized list of enrichment tasks:

**Format:**
```
FIELD: [Field name]
MISSING IN: [X records (Y%)]
PRIORITY: [Critical/High/Medium/Low]
IMPACT ON SENDABILITY: [+Z points avg if enriched]
ENRICHMENT TACTIC: [How to find this data]
ESTIMATED TIME: [Minutes per record]
TOOLS RECOMMENDED: [Hunter.io, Apollo.io, LinkedIn, Website scrape, etc.]
EXPECTED UPLIFT: [sendability_score improvement estimate]

EXAMPLE:
FIELD: First Name
MISSING IN: 342 records (45%)
PRIORITY: High
IMPACT ON SENDABILITY: +15 points avg
ENRICHMENT TACTIC: Extract from email prefix (john.smith@... → John Smith), LinkedIn profile scrape, website "About" page
ESTIMATED TIME: 2-3 min/record (manual), 30 sec/record (automated via Hunter.io)
TOOLS RECOMMENDED: Hunter.io, Apollo.io, LinkedIn Sales Navigator, FullContact
EXPECTED UPLIFT: +15 sendability points, +20% personalization capability
```

**Prioritization order:**
1. Email validation (if invalid/unknown)
2. First name extraction
3. Role identification
4. Language detection
5. Country/region mapping
6. Industry classification
7. LinkedIn URL
8. Phone number
9. Tech stack discovery
10. Decision-maker hierarchy

---

### 5. Risks & Assumptions

**Data Quality Risks:**
- **Duplicate risk:** [X% of records share same domain - potential duplicates]
- **Stale data risk:** [Y% of records have no interaction in 180+ days]
- **Invalid email risk:** [Z% emails failed validation - may bounce]
- **Language assumption risk:** [W% records missing language tag - may send in wrong language]

**Segmentation Assumptions:**
- **Segment overlap:** [X% of records belong to 2+ segments - prioritization needed]
- **Stage ambiguity:** [Y records have unclear stage - manual review recommended]
- **Platform assignment:** [Z records missing platform tag - inferred from notes/industry]

**Compliance & Deliverability Risks:**
- **GDPR:** [EU records (count) - ensure consent documented]
- **CAN-SPAM:** [US records (count) - include unsubscribe in all emails]
- **Domain reputation:** [Sending volume recommendation: max X emails/day for warm-up]
- **Spam trigger words:** [Flag records with spam-prone industries or content]

**Mitigation Plan:**
- [Specific action for each risk]
- [Responsible party: Sales/LG/AI team]
- [Timeline for resolution]

---

## Output Format

**Return in this structure:**

### PART 1: EXECUTIVE SUMMARY
[1-page summary as specified above]

### PART 2: SEGMENT REPORTS
[Full reports for Segments A-G as specified above]

### PART 3: CLEANED DATA SAMPLE
```csv
[First 20 rows of cleaned table with full schema]
```

### PART 4: ENRICHMENT BACKLOG
[Prioritized enrichment tasks as specified above]

### PART 5: RISKS & ASSUMPTIONS
[Risk assessment and mitigation plan as specified above]

---

## Usage Instructions

**Step 1: Prepare Input**
- Export CRM data to CSV/XLSX or share Google Sheets link
- Note any custom segmentation labels you use
- Specify target markets/regions for this campaign

**Step 2: Run Normalizer**
- Paste this prompt + your CRM export into Claude, ChatGPT, or Gemini
- Specify: "Process this CRM export using the Remote Helpers Normalizer"

**Step 3: Review Output**
- Check Executive Summary for data quality red flags
- Review Segment Reports for counts and sendability
- Validate CSV snippet for accuracy

**Step 4: Enrichment (if needed)**
- Prioritize enrichment tasks from backlog
- Use recommended tools (Hunter.io, Apollo.io, LinkedIn)
- Re-run Normalizer after enrichment to update scores

**Step 5: Export for Outreach**
- Use cleaned CSV for email tool import (Lemlist, Instantly, Smartlead)
- Apply segment filters for targeted campaigns
- Proceed to **14-Day Action Plan Generator** (next prompt in sequence)

---

## Integration with Remote Helpers Stack

**Tools Used:**
- **AI Analysis:** Claude, ChatGPT, Gemini, Perplexity AI
- **Email Validation:** Hunter.io, NeverBounce, ZeroBounce
- **Enrichment:** Apollo.io, LinkedIn Sales Navigator, Clearbit, FullContact
- **CRM:** Template-driven CRM system (Remote Helpers proprietary)
- **Documentation:** RAC (Remote AI Context) for knowledge retention

**Department Responsibilities:**
- **LG Team:** Enrichment tasks, data validation, segment QA
- **Sales Team:** Stage verification, client relationship context, priority setting
- **AI Team:** Automation of enrichment workflows, prompt optimization

---

## Version History

**v1.0 (2025-11-11):**
- Initial release
- Remote Helpers-specific segmentation (7 segment types)
- Multi-language support (EN/UK/RU/PL)
- Comprehensive enrichment backlog with tool recommendations
- Sendability scoring algorithm
- Integration with 14-Day Action Plan Generator

---

**Next Step:** Use cleaned, segmented data with **14-Day Action Plan Generator** to build execution roadmap.
