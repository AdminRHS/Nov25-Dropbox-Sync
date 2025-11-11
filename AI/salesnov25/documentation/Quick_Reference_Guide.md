# Quick Reference Guide
## CRM Export Analysis System - Remote Helpers

**Last Updated:** November 11, 2025

---

## 🎯 One-Page Cheat Sheet

### System Overview

```
RAW CRM → Clean & Segment → Enrich (if needed) → Plan (14 days) → Write Copy → Build Sequence → QA → SEND
  ↓           ↓                  ↓                    ↓              ↓              ↓            ↓      ↓
Prompt #1   Prompt #1          Prompt #6          Prompt #2      Prompt #3      Prompt #4    Prompt #5  Execute
```

---

## 📋 When to Use Each Prompt

| Prompt | Use When... | Time to Run | Output |
|--------|-------------|-------------|---------|
| **#1: Normalizer** | You have a messy CRM export | 5-10 min | Clean table, segments, scores |
| **#2: Action Plan** | You're ready to execute campaign | 10-15 min | 14-day calendar, RACI, dashboards |
| **#3: Outreach Writer** | You need email copy for a segment | 3-5 min | Subject lines, body, P.S. |
| **#4: Sequence Builder** | You need multi-touch cadence | 5-10 min | Touch 1-3 with timing |
| **#5: QA & Risk Check** | Before sending ANY email | 5-7 min | Risk score, fixes, approval |
| **#6: Enrichment Plan** | Data quality is low (<70 sendability) | 10-15 min | Task list, budget, timeline |

---

## ⚡ Quick Wins by Segment

### Ex-Clients (Segment A)
**Best For:** Re-engagement, upsell, win-back
**KPIs:** 50-60% open, 10-15% reply, 15-20% meeting
**Tactics:**
- Use **Prompt #3** with "Ex-Client" segment + "Founder/CEO" persona
- Reference past projects ({{LastInteraction}}, {{Outcome}})
- Warm, familiar tone ("Great working with you on [project]...")
- 3-touch sequence: Day 1 (check-in), Day 5 (case study), Day 10 (soft close)

### First-Call Leads (Segment B)
**Best For:** Following up on discovery calls
**KPIs:** 55-65% open, 12-18% reply, 12-18% meeting
**Tactics:**
- Use **Prompt #3** with "First-Call" segment + persona matching role
- Reference specific call details ({{LastInteraction}} = "our chat about lead gen")
- Action-oriented tone ("Here's what I'm thinking for next steps...")
- 3-touch sequence: Day 1 (follow-up), Day 4 (answer objection), Day 9 (gentle urgency)

### Warm Leads (Segment C)
**Best For:** Moving engaged prospects to meeting
**KPIs:** 60-70% open, 15-20% reply, 20-25% meeting
**Tactics:**
- Use **Prompt #3** with "Warm Lead" segment + persona
- Lead with value (case study, checklist, guide)
- Consultative tone ("Thought you'd find this useful...")
- 3-touch sequence: Day 1 (value asset), Day 7 (educational story), Day 14 (opt-in nurture)

### Cold Outreach (Segment D)
**Best For:** New market expansion, list building
**KPIs:** 25-35% open, 4-8% reply, 3-6% meeting
**Tactics:**
- Use **Prompt #3** with "Cold" segment + persona
- Problem-aware opener (lead with pain point)
- Direct, ROI-focused tone ("We help companies like [X] achieve [Y] in Z days")
- 3-touch sequence: Day 1 (intro), Day 3 (pattern interrupt), Day 6 (breakup email)

---

## 🔥 Common Workflows

### Workflow 1: Simple Re-Engagement (Clean Data)
**Time:** 4-6 hours
1. Export ex-clients → **Prompt #1** (segment) → 30 min
2. **Prompt #2** (plan) → 30 min
3. **Prompt #3** (write ex-client copy) → 20 min
4. **Prompt #5** (QA) → 15 min
5. Load into Lemlist → Send → 2 hours

### Workflow 2: Cold Outreach (Messy Data)
**Time:** 2-3 days
1. Export cold list → **Prompt #1** (clean + segment) → 1 hour
2. **Prompt #6** (enrichment plan) → 30 min
3. Execute enrichment (LG Team) → Day 1-2 (2-4 hours distributed)
4. Re-run **Prompt #1** (validate) → 30 min
5. **Prompt #2** (plan) → 1 hour
6. **Prompt #3** + **#4** (copy + sequence) → 1.5 hours
7. **Prompt #5** (QA) → 30 min
8. Send Day 1

### Workflow 3: Multi-Language Campaign (EU Market)
**Time:** 3-4 days
1. Export EU list → **Prompt #1** (segment by country) → 1 hour
2. **Prompt #6** (enrich language field) → 30 min + 2 hours execution
3. **Prompt #2** (plan, assign translators) → 1 hour
4. **Prompt #3** × 3 (write EN, UK, PL versions) → 2 hours
5. Translation QA (LG Team: Anna, Kseniia) → 1 hour
6. **Prompt #5** × 3 (QA each language) → 1 hour
7. Send Day 1 (stagger by language/timezone)

---

## 📊 KPI Benchmarks (from Prompt #2)

| Segment | Open Rate | Reply Rate | Meeting Rate | Bounce Rate | Unsub Rate |
|---------|-----------|------------|--------------|-------------|------------|
| Ex-Client | 45-60% | 8-12% | 15-20% | <2% | <0.3% |
| First-Call | 50-65% | 10-15% | 10-15% | <2% | <0.5% |
| Warm Lead | 60-70% | 12-18% | 20-25% | <2% | <0.5% |
| Cold | 25-35% | 3-8% | 2-5% | <3% | <1% |

**Red Flags (pause campaign):**
- Bounce rate >5%
- Spam complaints >0.2%
- Open rate <15% (after 50 sends)
- Unsubscribe rate >2%

---

## 🛠️ Tool Costs

| Tool | Cost | Use For | Prompt |
|------|------|---------|--------|
| **Hunter.io** | $49/mo (500 searches) | Email finding + validation | #1, #6 |
| **Apollo.io** | $49/mo (1,000 enrichments) | Bulk enrichment (name, role, country) | #6 |
| **LinkedIn Sales Navigator** | $80/mo | LinkedIn URL discovery, fallback outreach | #4, #6 |
| **NeverBounce** | $0.008/email (bulk) | Email validation (cheaper alternative) | #6 |
| **Lemlist/Instantly** | $59-99/mo | Email campaign execution | #2, #4 |

**Minimum viable stack:** Hunter.io ($49) + Lemlist ($59) = **$108/month**

---

## 🚨 Critical Checklist (Before Every Send)

From **Prompt #5 - Go/No-Go Checklist:**

**Data:**
- [ ] CRM cleaned, deduplicated (Prompt #1)
- [ ] Sendability score ≥70 (ideally ≥80)
- [ ] Email validation complete (bounce risk <2%)
- [ ] {{FirstName}} fallback set ("Hi" not "Hi {{FirstName}}")

**Technical:**
- [ ] SPF/DKIM/DMARC records set (domain authenticated)
- [ ] Unsubscribe link functional (click to test)
- [ ] Sender domain age >30 days (or warm-up plan in place)

**Copy:**
- [ ] Subject line <50 chars (mobile-friendly)
- [ ] Email body 90-120 words
- [ ] No spam triggers (FREE, URGENT, ACT NOW, etc.)
- [ ] Single clear CTA (one Calendly link or reply prompt)

**Compliance:**
- [ ] GDPR compliance (if EU) - unsubscribe + data source transparency
- [ ] CAN-SPAM compliance (if US) - physical address + unsubscribe
- [ ] No attachments (link to hosted PDF instead)

**Team:**
- [ ] Final approval from Anastasia Kovalska (Sales)
- [ ] Sender assignments confirmed (who sends what, when)
- [ ] Dashboard 1 (Engagement) ready for monitoring

---

## 💡 Pro Tips

### Personalization
- **{{FirstName}}** improves reply rate by 20-30% → Enrich this field first (Prompt #6, Tier 2)
- **{{Company}}** + **{{UseCase}}** makes value prop specific → "We help [Company] achieve [UseCase]"
- **{{LastInteraction}}** for ex-clients/first-call → "Following up on our chat about [topic]"

### Timing
- **Best send times:** 9-11 AM or 2-4 PM recipient local time (Prompt #2: Send Window Optimization)
- **Best days:** Tuesday, Wednesday, Thursday (avoid Monday, Friday PM, weekends)
- **Touch spacing:** Day 1 → Day 4-5 → Day 9-10 (3-5 day gaps allow processing time)

### Subject Lines
- **Mobile-first:** <50 chars (most people read on mobile)
- **Curiosity + Relevance:** "Quick update for {{Company}}" beats "Partnership Opportunity"
- **A/B test:** Use 3 variants from Prompt #3 (direct value, curiosity, personalization)

### Email Body
- **Hook (1-2 sentences):** Personalize, establish relevance
- **Value (3 bullets):** Lead with outcomes, not features ("Get X" not "We offer Y")
- **CTA (1 sentence):** Low-friction ("15-min call" not "exploratory discovery session")

### Deliverability
- **New domain (<30 days):** Start 20-50 emails/day, increase 20% every 3 days if metrics healthy
- **Warm domain (30-90 days):** 50-150 emails/day safe
- **Established domain (90+ days):** 150-500 emails/day max (don't exceed or risk spam flags)
- **Bounce rate >5%:** Pause immediately, clean list, re-validate emails

---

## 🎓 Learning Resources

**Inside This System:**
- **README.md** - Full overview, use cases, workflows
- **Prompt #1 - CRM Normalizer** - Data cleaning, segmentation guide
- **Prompt #2 - Action Plan** - Campaign planning, RACI, dashboards
- **Prompt #3 - Outreach Writer** - Copywriting best practices, multi-language
- **Prompt #4 - Sequence Builder** - 3-touch framework, fallback channels
- **Prompt #5 - QA & Risk Check** - Spam triggers, compliance, deliverability
- **Prompt #6 - Enrichment Plan** - Enrichment tactics, tool comparisons

**External Resources:**
- **GDPR Compliance:** https://gdpr.eu (official EU guidelines)
- **CAN-SPAM Guide:** https://www.ftc.gov/tips-advice/business-center/guidance/can-spam-act-compliance-guide-business
- **Sender Score Check:** https://www.senderscore.org (check domain reputation)
- **Spam Tester:** https://www.mail-tester.com (test emails before send)
- **Deliverability Guide:** https://www.validity.com/resource-center/email-deliverability-guide/

---

## 🆘 Quick Troubleshooting

| Problem | Quick Fix | Prompt to Use |
|---------|-----------|---------------|
| Low open rate (<20%) | Shorten subject line, test new variants, check send time | #5 (subject validation), #3 (new subjects) |
| High bounce (>5%) | Validate emails with Hunter.io/NeverBounce | #6 (email validation task) |
| Low reply rate (<3% warm) | Increase personalization, strengthen value prop | #3 (rewrite with more {{variables}}) |
| Spam complaints (>0.2%) | Remove spam triggers, check list quality | #5 (spam trigger check) |
| Team overload | Prioritize Tier 1-2 only, automate where possible | #6 (re-prioritize, use scripts) |

---

## 📞 Remote Helpers Contacts

| Question About | Contact | Department |
|----------------|---------|------------|
| Campaign strategy, final approval | Anastasia Kovalska (@anastasia_kovalska) | Sales |
| Enrichment tasks, data quality | Hanan Zaheur, Nataliia Rybak | LG Team |
| Multi-language copy (UK/RU/PL) | Anna Burda, Kseniia Shkinder | LG Team |
| Technical issues, automation | Nikolay Artemchuk (@twinklelilsta) | AI Team |
| Prompt optimization | Matvii Zasiadko, Vladislav Perederii | AI Team |

---

## 🚀 Next Steps

1. **Read README.md** for full context (10-15 min)
2. **Export your CRM data** (CSV/XLSX)
3. **Run Prompt #1** with your data (30 min)
4. **Choose workflow** based on data quality and campaign type
5. **Execute prompts sequentially** (4-6 hours for simple campaign, 2-3 days for complex)
6. **Send Day 1** and monitor dashboards
7. **Iterate** based on performance (A/B test, adjust copy, optimize)

---

**Ready to turn spreadsheets into meetings? Start with Prompt #1.** 🎯
