# Campaign Strategy Guide

Combined reference for experimenting with new lead sources, balancing outbound/inbound, and leveraging AI tooling.

---

## 1. Channel Mix Overview

### Outbound systems
1. **Email engines**
   - Build lists via Apollo, Lusha, UpLead.
   - Sequence with Lemlist, Instantly, Mailshake, or Smartlead; A/B subject + CTA.
2. **Sales Navigator + enrichment**
   - Filter ICP accounts, export to Clay/N8N/PhantomBuster/Waalaxy for enrichment and drip delivery.

### B2B marketplaces
1. **Upwork / Toptal / Fiverr Pro**
   - Maintain polished agency profiles, respond to briefs that match service strengths, and track win rates per vertical.
2. **Clutch & GoodFirms**
   - Continuously request reviews, update case studies, and optimize SEO tags to stay visible.
3. **High-intent directories**
   - DesignRush, 99Firms, Product Hunt launches, BetaList, StartUs Insights for early adopters.

### Inbound engines
1. **SEO + long-form content**
   - Publish 2–4 thought leadership posts per month (Medium, Dev.to, HackerNoon) with quantifiable outcomes.
2. **Short-form video**
   - Use YouTube Shorts/TikTok/Reels to showcase processes, client wins, and AI capabilities targeting EN/DE/UK markets.

### Communities & events
1. **Slack/Discord**
   - ProductLed, Demand Curve, Indie Hackers, GrowthHackers → share playbooks, answer hiring questions, add value first.
2. **Conferences / webinars**
   - Web Summit, SaaStr, TechCrunch, plus niche webinars where decision makers already gather.

### Paid & partnership experiments
1. **Partner programs**
   - Offer 10–15% referral fees to agencies, consultants, or influencers who bring qualified deals.
2. **Cross-promotions**
   - Co-market with complementary SaaS / service providers; run joint workshops or newsletter swaps.

---

## 2. ICP Research & Prompt Library

1. **Funding & signals**
   - Crunchbase, Dealroom, Product Hunt, Tracxn, BetaList, StartUs Insights, Signal.nfx, StartupBlink. Track funding status, last round, hiring velocity.
2. **Job-posting sweeps**
   - `site:linkedin.com/jobs "contract" AND "remote" AND "developer"` to surface companies hiring remotely; save into a tracker.
3. **Google boolean templates**
   - `site:linkedin.com headquarters:"[City]" AND industry:"[Type]" AND "company size:[Range]"`.
   - `site:linkedin.com (CEO OR Founder OR Director) "[Industry]" "[Location]" "company size:[Range]" -freelance`.
4. **Automation prompts**
   - Use GPT/Claude to summarize company activity, LinkedIn posts, and identify likely gaps before outreach.

---

## 3. B2B Platform Playbooks (Quick Reference)

| Platform | Positioning | Keys to win | Watch-outs |
| --- | --- | --- | --- |
| **Upwork** | Fast project work & retained teams | Maintain optimized agency profile, chase filtered invites, respond with tailored case snippets | Race-to-bottom bids—qualify aggressively |
| **Toptal** | Premium vetted talent | Complete partner intake, showcase senior specialists, prep for interviews | Heavy screening, longer approval |
| **Fiverr Pro** | Productized services | Create packaged offers (e.g., “AI SDR pod for SaaS”), keep delivery SLAs tight | Platform fees; needs constant reviews |
| **Clutch / GoodFirms** | Proof & SEO | Collect reviews, refresh portfolio, cross-link to site & socials | Requires continuous review generation |
| **DesignRush / 99Firms** | Niche directories | Repurpose Clutch assets, monitor category rankings | Low intent unless profile stays updated |

---

## 4. AI Toolkit for Campaigns

| Tool | Use cases for LG | Tips |
| --- | --- | --- |
| **ChatGPT / Claude** | Personalized outreach drafts, call summaries, competitive research | Save winning prompts, define tone, review before sending |
| **Gemini 2.0** | Predictive scoring, workflow simulation, data visualization | Requires curated datasets; pair with Sheets/Looker Studio |
| **NotebookLM** | Organize research packets, compare documents, create knowledge bases | Segment notebooks by vertical/client |
| **Perplexity** | Fast fact-checking, real-time signals, source lists | Use “Copilot” mode for citations, log new triggers |
| **Qwen Chat / Napkin** | Customer support automations, visual ideation for campaigns | Map flows first; export visuals into briefs |

**Best practices**
1. Break complex prompts into steps; include ICP context, tone, CTA, and constraints.
2. Iterate—log output quality, adjust instructions, store final prompt + sample output in a shared doc.
3. Pair AI drafts with human QA for accuracy, compliance, and brand voice before publishing.

---

## 5. Execution Checklist

1. Select 2 outbound + 1 inbound + 1 marketplace channel per quarter to avoid thrash.
2. Document experiment goal, audience, assets needed, and success metric before launch.
3. Track performance in a unified dashboard (response rate, opps created, meetings booked, CAC proxy).
4. Sunset underperforming channels after two learning loops; reinvest in winners.
5. Feed every insight back into the AI prompt library and ICP notes so the next sprint starts smarter.
