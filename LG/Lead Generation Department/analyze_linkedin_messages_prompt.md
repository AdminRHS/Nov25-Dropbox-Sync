# LinkedIn Message Analysis Prompt

## Objective
Analyze LinkedIn message exports from lead generation accounts to identify successful conversation patterns, extract messages with replies, and determine best practices for engagement.

## Data Structure

### CSV Format
Each messages.csv file contains 11 columns:
1. **CONVERSATION ID** - Unique thread identifier
2. **CONVERSATION TITLE** - Usually empty
3. **FROM** - Sender name
4. **SENDER PROFILE URL** - LinkedIn profile URL
5. **TO** - Recipient name
6. **RECIPIENT PROFILE URLS** - Recipient LinkedIn URL(s)
7. **DATE** - Format: "YYYY-MM-DD HH:MM:SS UTC"
8. **SUBJECT** - Usually empty for direct messages
9. **CONTENT** - Message text (may contain HTML)
10. **FOLDER** - Typically "INBOX"
11. **ATTACHMENTS** - File attachments if any

---

## Analysis Tasks

### 1. IDENTIFY CONVERSATIONS WITH REPLIES

**Definition:** Any conversation thread where the prospect responded at least once.

**How to Identify:**
- Group messages by **CONVERSATION ID**
- Count unique values in **FROM** field per conversation
- If count > 1 (alternating senders), the conversation has replies
- Sort by **DATE** to establish chronological order

**Exclude:**
- One-way outreach with no response
- Automated LinkedIn notifications
- System messages

---

### 2. CATEGORIZE CONVERSATION SUCCESS LEVELS

#### **TIER 1: HIGH SUCCESS** ⭐⭐⭐
Conversations that achieved concrete outcomes:

**Explicit Positive Signals:**
- Agreed to schedule a call or meeting
- Requested to be contacted via email
- Said "yes" or "interested" explicitly
- Moved conversation to another channel (email, phone)
- Created an event or booked a meeting

**Keyword Indicators:**
```
"yes", "interested", "let's schedule", "call", "meeting",
"email me at", "sounds good", "would love to", "please send",
"available", "calendar", "this week", "next week", "let's discuss"
```

**Example Pattern:**
```
Marina → Initial outreach
Prospect → "Yes, interested"
Marina → "Great! When are you available?"
Prospect → "Can you email me at [address]?"
```

---

#### **TIER 2: QUALIFIED INTEREST** ⭐⭐
Conversations with engaged prospects who showed interest but didn't convert immediately:

**Signals:**
- Asked clarifying questions
- Requested more information
- Engaged in 3+ message exchanges
- Polite, detailed responses (even if declining)
- Kept door open for future ("keep my info on file", "not right now but...")
- Responded after 2nd or 3rd follow-up

**Keyword Indicators:**
```
"tell me more", "can you explain", "what does", "how does",
"not right now", "maybe in the future", "keep in touch",
"not hiring but", "interesting", "thanks for reaching out"
```

**Example Pattern:**
```
Marina → Initial outreach + 2 follow-ups
Prospect → Asks detailed questions about service
Marina → Provides answers
Prospect → "Not right now but will keep you in mind"
```

---

#### **TIER 3: FUTURE OPPORTUNITY** ⭐
Conversations that didn't convert but showed potential:

**Signals:**
- Professional, thoughtful decline
- Explained their situation in detail
- Used respectful/appreciative language
- Engaged enough to reply personally
- Prospect reached back out later (even months later)

**Keyword Indicators:**
```
"thank you", "appreciate", "not at this time",
"currently", "already have", "keep your information",
"in the future", "good luck"
```

**Example Pattern:**
```
Marina → Initial outreach
Prospect → "Thanks but we already have internal team"
[Later: Prospect reaches out with new opportunity]
```

---

#### **TIER 4: POLITE DECLINE** (Low Priority)
- Single polite "no thank you"
- Not interested, no elaboration
- Brief decline without questions

---

### 3. EXTRACT SUCCESS PATTERNS

For each successful conversation (Tier 1-3), analyze:

#### **A. Response Timing**
- Time between Marina's first message and prospect's first reply
- Did reply come after 1st, 2nd, or 3rd follow-up?
- Pattern: `First message: [DATE] → First reply: [DATE] (X days later)`

#### **B. Message Sequence**
- Total number of exchanges
- Who ended the conversation?
- Length/depth of responses (brief vs detailed)

#### **C. Engagement Quality**
- Prospect asking questions (high engagement)
- Prospect providing detailed context (high engagement)
- Positive emojis: 👍 🙏 😊 ✅
- Professional tone indicators

#### **D. Follow-Up Effectiveness**
- How many follow-ups before response?
- What type of follow-up worked? (value-add, question, social proof, etc.)

#### **E. Pain Points & Objections**
Extract any mentioned:
- "We already have [solution]"
- "Not hiring right now"
- "Budget constraints"
- "Not the right time"
- "Wrong fit because [reason]"

---

## Output Format

### For replies.md File

Structure the extracted conversations as follows:

```markdown
# LinkedIn Message Analysis - Conversations with Replies

Generated: [DATE]
Total Accounts Analyzed: [X]
Total Conversations with Replies: [X]

---

## Account: [Account Name]

**Export Path:** `C:\Dropbox\LG_DropBox\Lead_Generation_DropBox\LinkedIn Accounts Export\[Account]\messages.csv`

**Statistics:**
- Total Messages Sent: [X]
- Conversations with Replies: [X]
- Reply Rate: [X%]
- Tier 1 Success: [X]
- Tier 2 Success: [X]
- Tier 3 Success: [X]

---

### ⭐⭐⭐ TIER 1: [Prospect Name]

**Conversation ID:** [ID]
**Outcome:** [Call scheduled / Email requested / Event created / etc.]
**Response Time:** [X days after initial outreach]
**Message Count:** [X exchanges]
**Profile URL:** [LinkedIn URL]

**Key Success Indicators:**
- [Specific keywords or actions that indicated success]
- [E.g., "Requested email contact after 2nd follow-up"]

**Full Conversation Thread:**

---

**[DATE] - Marina → Prospect**
[Message content]

---

**[DATE] - Prospect → Marina**
[Message content]

---

**[DATE] - Marina → Prospect**
[Message content]

---

**Analysis:**
- **What worked:** [Specific elements that led to success]
- **Response trigger:** [What message/follow-up got the reply?]
- **Pain point addressed:** [If mentioned]
- **Lessons learned:** [Key takeaways]

---

### ⭐⭐ TIER 2: [Prospect Name]

[Same format as above]

---

### ⭐ TIER 3: [Prospect Name]

[Same format as above]

---

## CROSS-ACCOUNT PATTERNS

### Most Effective Message Elements:
1. [Pattern found across multiple accounts]
2. [E.g., "Mentioning specific company project"]
3. [E.g., "Question-based approach"]

### Follow-Up Best Practices:
- [When to follow up]
- [What type of follow-up gets most responses]

### Industry-Specific Insights:
- [If certain industries respond better]
- [Timing patterns by industry]

### Common Objections & How to Address:
- **Objection:** [Common objection]
  - **How to address:** [Strategy]

---

## RECOMMENDATIONS

### Message Strategy:
1. [Based on analysis]
2. [E.g., "Follow up 3-5 days after initial message"]

### Target Profiles:
- [Types of prospects most likely to respond]
- [Seniority levels, company sizes, etc.]

### Content Improvements:
- [What to emphasize more]
- [What to avoid]

### Timing Optimization:
- [Best days/times to send based on reply patterns]

---
```

---

## Analysis Rules & Guidelines

### DO Include:
✅ All conversations with at least one prospect reply
✅ Complete conversation threads (all messages chronologically)
✅ Conversations where prospect later reached back out
✅ Both successes and instructive failures
✅ Detailed analysis of what worked/didn't work
✅ Emoji sentiment indicators from prospects

### DO NOT Include:
❌ One-way messages with zero replies
❌ System notifications or automated LinkedIn messages
❌ Spam or irrelevant messages
❌ Incomplete conversation threads
❌ Personal/non-business conversations

### Special Attention To:
⚡ Conversations that resulted in calls/meetings
⚡ Prospects who replied after multiple follow-ups (persistence analysis)
⚡ Long conversation threads (5+ exchanges)
⚡ Prospects who came back later (relationship value)
⚡ Detailed objections (learning opportunities)
⚡ Referrals or introductions to others

---

## Success Metrics to Calculate

For each account processed:

1. **Reply Rate:** (Conversations with replies / Total conversations) × 100
2. **Success Rate:** (Tier 1 conversations / Total conversations) × 100
3. **Average Response Time:** Mean days between first message and first reply
4. **Follow-Up Effectiveness:** % of replies that came after follow-ups (vs first message)
5. **Thread Depth:** Average number of exchanges per replied conversation
6. **Conversion Funnel:**
   - Total outreach →
   - Got reply →
   - Qualified interest →
   - Scheduled call/meeting

---

## Processing Instructions

### Step 1: Data Extraction
1. Open messages.csv file
2. Parse all rows into structured data
3. Group by CONVERSATION ID
4. Sort each conversation by DATE (oldest to newest)

### Step 2: Reply Detection
1. For each conversation, count unique FROM values
2. If > 1, mark as "has reply"
3. Identify if Marina's account is sender or recipient

### Step 3: Success Categorization
1. Read all CONTENT fields in conversation
2. Apply keyword analysis for success indicators
3. Count message exchanges
4. Assign Tier (1-4) based on criteria above

### Step 4: Pattern Recognition
1. Look for common phrases in successful conversations
2. Analyze timing patterns
3. Identify follow-up sequences that worked
4. Extract pain points and objections

### Step 5: Output Generation
1. Create markdown sections for each account
2. Order conversations by Tier (highest first)
3. Include full conversation threads
4. Add analysis and insights for each
5. Generate cross-account summary

### Step 6: Logging
1. Record processing timestamp
2. Log statistics for each account
3. Note any errors or data issues
4. Track progress through all accounts

---

## Example: Successful Conversation Analysis

### Real Example from Marina Duka

**Prospect:** Agnieszka Gansiniec
**Tier:** 1 (Initially yes, later declined due to wrong fit)
**Message Count:** 9+ exchanges
**Response Time:** After 2nd follow-up

**Timeline:**
- Nov 8: Marina's initial outreach
- Nov 10: Marina's 1st follow-up
- Nov 12: Marina's 2nd follow-up
- Nov 14: Agnieszka replied "yes," (breakthrough!)
- Nov 14: Marina attempted to schedule call
- Nov 14: Agnieszka clarified not looking for agency
- Later: Conversation ended but relationship established

**What Worked:**
- Persistence (2 follow-ups before response)
- Simple yes/no question
- Professional tone maintained

**Lesson Learned:**
- Follow-up 2-3 times before giving up
- Getting "yes" doesn't guarantee fit - qualification is key
- Even "no" after "yes" is valuable data

---

**Prospect:** Maureen Kilgore
**Tier:** 1 (Requested email contact)
**Message Count:** 2 exchanges
**Response Time:** Immediately after first message

**Timeline:**
- Marina's initial outreach
- Maureen replied: "Can you email me at info@irishagroforestry.ie"
- Marina confirmed and promised to send details

**What Worked:**
- Immediate value proposition
- Direct ask
- Easy for prospect to respond

**Lesson Learned:**
- Some prospects prefer email over LinkedIn
- Quick response = high interest level
- Always have email follow-up ready

---

## Quality Checklist

Before finalizing replies.md, ensure:

- [ ] All conversations have complete message threads
- [ ] Dates are in chronological order
- [ ] Profile URLs are included for all prospects
- [ ] Success indicators are clearly marked
- [ ] Analysis explains WHY conversation succeeded/failed
- [ ] Cross-account patterns are identified
- [ ] Statistics are accurate
- [ ] Formatting is consistent
- [ ] Actionable insights are provided
- [ ] Log file is updated

---

## Priority Accounts to Process

**Location:** `C:\Dropbox\LG_DropBox\Lead_Generation_DropBox\LinkedIn Accounts Export\`

**Account List (35 total):**
1. ✅ Marina Duka (template/example)
2. Anastasia Khvashchevska (ZIP - needs extraction)
3. Artem Dadon (ZIP - needs extraction)
4. Danylo Kitura (ZIP - needs extraction)
5. Daria Chelpanova
6. Diana Kharaman
7. Elena Statsenko (ZIP - needs extraction)
8. Ellina Gudz
9. Hanan Zaheur
10. Inna Fursa
11. Iryna Mazhula (ZIP - needs extraction)
12. Julia Marushchenko (ZIP - needs extraction)
13. Karina Dzholus (ZIP - needs extraction)
14. Kateryna Parfonova
15. Kseniia Matsenko
16. Lilia Voitovych
17. Liudmyla Tkachova
18. Maria Mahola Linkedin
19. Maxim Maryshenko (ZIP - needs extraction)
20. Myroslava Lenko
21. Nadia Omelchenko
22. Natalia Shyianova
23. Natalia Stoliaruk
24. Oksana Bredun (ZIP - needs extraction)
25. Oleksandra Tarasenko (ZIP - needs extraction)
26. Olga Terentieva (ZIP - needs extraction)
27. Olha Hlushchenko
28. Ol'ha Kovalenko
29. Pavlo Netetskyi (ZIP - needs extraction)
30. Tanee Vasyliuk
31. ulviya alakbarova 2
32. Ulviyya Alakbarova (ZIP - needs extraction)
33. Victoria Mirvoda (Complete export ZIP - needs extraction)
34. Yana Titarenko
35. Yana Yatskova (ZIP - needs extraction)

**Note:** 16 accounts are in ZIP format and require extraction before processing.

---

## Version History

**v1.0** - Initial prompt created based on Marina Duka account analysis
- Established 4-tier categorization system
- Defined success indicators and keyword patterns
- Created output format template
- Documented processing workflow

---

## Contact & Updates

**Output Directory:** `C:\Dropbox\LG Nov25\Lead Generation Department\`

**Files Generated:**
- `analyze_linkedin_messages_prompt.md` (this file)
- `replies.md` (conversation extractions)
- `linkedin_analysis_log.md` (processing log)

**Last Updated:** 2025-11-11
