# Qualification Workflow Blueprint

Unified guide for processing interested leads: from deep research through measurement.

---

## 1. Core Concept

Shift from high-volume templated replies to **depth per lead**:
1. **Deep research** – manually analyze the company (site, case studies, social feeds, reviews, mentions) to understand product, market, buying influences, and obvious gaps. Use Claude/Gemini/ChatGPT/Perplexity to augment but do not skip human review.
2. **Lead magnet** – deliver immediate value (Gamma mini-deck, AI video, audit, design mock) that proves we understand their pain.
3. **Context packaging** – feed research and magnet summary into Custom LG GPT to draft a hyper-personalized reply anchored in our updated services/cases.
4. **Send + monitor** – deliver the message, log it in CRM, track performance, and loop learnings back into GPT prompts.

Always run the flow manually until the logic is solid, then automate (Chrome extension, scripts) without losing quality.

---

## 2. Implementation Stages

| Stage | Focus | Key Actions |
| --- | --- | --- |
| **0. Prep & Discipline** | Pause responses, set standards | Announce temporary freeze, ensure every rep has VS Code + Dropbox + WhisperFlow, check daily that logs and recordings exist, form an implementation squad (LG TLs + AI dept). |
| **1. Update Context & Tools (3–5 days)** | Refresh what we sell & how we research | Rewrite service list with AI capabilities, collect recent case studies per industry, reload Custom GPT knowledge, document standard prompts/checklists for Claude/Gemini/ChatGPT. |
| **2. Training & Documentation (5–7 days)** | Teach the manual process | Build courses on deep research, lead magnet creation, GPT usage. Run “train the trainers”, then hands-on workshops. Test and certify reps before they can reply again. |
| **3. Restart & Optimization** | Run live, measure quality | Process backlog using the new workflow, adjust KPIs toward quality (e.g., 4–5 deep replies/day, target negative-response reduction from 95% → 70–80%), assign a daily QA “shift” lead to review LG-Messages and iterate GPT core settings. |
| **4. Automation (Future)** | Layer tooling once behavior sticks | Scope Chrome extension (scrape open tabs, pass structured context to GPT, speed up logging) only after stages 0–3 are stable. |

---

## 3. Data & Tracking Infrastructure

### Lead Database (Google Sheets)
Required columns:
- **Company info** – name, LinkedIn, website, industry, employee count, HQ, followers, revenue band.
- **Contact details** – lead name, role, LinkedIn, email, phone, location, time zone.
- **Engagement** – initial contact date, connection & response status, last/next follow-up, touches count, current stage.
- **Qualification** – score, budget range, decision-maker level, pain points, requirements, notes.

Supporting sheets:
- `Daily Activity Tracker` – connections sent, replies, meetings, notes.
- `Campaign Performance` – template used, sent volume, response/meeting rates, success metric.
- `Message Template Library` – prompt name, use case, copy, performance, A/B notes.
- `Prompt Log` – Google/LinkedIn query strings with conditional formatting to catch duplicates.

Automation ideas:
- COUNTIF/COUNTIFS formulas for status counts, follow-up SLAs.
- Conditional formatting to flag overdue tasks or hot leads.
- Pivot tables and charts for conversion and geography analysis.

### Dashboard KPIs
- Response rate, meetings booked, win rate.
- Negative response %, deep research SLA, lead magnet utilization.
- Channel attribution (Outbound, Marketplaces, Inbound).

---

## 4. Research & Prompt Best Practices

1. **Google setup**
   - Disable personalization, set display language to English, target the prospect’s region.
2. **Essential operators**
   - `site:linkedin.com headquarters:"[City]" AND industry:"[Type]" AND "company size:[Range]"`.
   - Decision makers: `site:linkedin.com (CEO OR Founder OR Director OR HR) "[Industry]" "[Location]" "company size:[Range]" -job -hiring`.
   - Role-specific: `site:linkedin.com "Head of Marketing" AND "SaaS" AND "Germany" -freelance`.
   - Multi-city: `(headquarters:"Berlin" OR headquarters:"Munich")`.
3. **Search workflow**
   - Start broad, then add filters; rotate titles/industry synonyms; log each query’s performance.
   - Update prompts monthly; retire strings that no longer return quality results.
4. **Seasonal tweaks**
   - Adjust searches for hiring seasons/industry cycles; respect local holidays/time zones.
5. **Scoring**
   - Build a simple scoring model (fit, funding, response intent, email verified) to prioritize manual effort.

---

## 5. Ops Checklist

1. Update CRM immediately after deep research, lead magnet creation, and send.
2. Save WhisperFlow transcripts inside daily logs for every conversation.
3. QA captain reviews LG-Messages channel daily and documents insights + GPT adjustments.
4. Weekly retro: review top wins/losses, refine prompts, refresh lead magnets, and archive outdated context.
5. Once automation starts, keep humans in the loop for qualification decisions and template updates.
