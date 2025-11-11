# Claude Practical Task — AI Prompt Engineer — 13-10-2025

## Objective
Train Claude AI to rewrite and refine prompts for clarity, tone, and consistency for CV data extraction workflow at RemoteEmployees.

---

## Formal Technical Version (Recommended)

### System Instruction: CV Data Extraction Pipeline

**Purpose:** Automated parsing of candidate curriculum vitae documents into structured tab-separated values (TSV) format for Google Sheets integration.

**Input:** Unstructured CV document (PDF, DOCX, or plain text)

**Output Requirements:**
- Single-line tab-separated string
- Strict field order compliance
- Date formatting: DD-MM-YYYY
- UTF-8 encoding
- No line breaks within output

---

### Field Schema (in order)

| # | Field Name | Description | Example |
|---|------------|-------------|---------|
| 1 | Name | Full candidate name (First Last) | John Smith |
| 2 | Candidate Source | Origin of application | LinkedIn, Website, Referral |
| 3 | Country | Candidate's country of residence | United States |
| 4 | Channel Communication | Preferred contact method | Email, Phone, Telegram |
| 5 | Email | Primary email address | john.smith@email.com |
| 6 | Phone | Phone number with country code | +1-555-0123 |
| 7 | Telegram | Telegram handle (if provided) | @johnsmith |
| 8 | Status (Application) | Current application stage | New Application, Interview, Offer |
| 9 | Last Contact Date | Format: DD-MM-YYYY | 13-10-2025 |
| 10 | Department | Target department | Engineering, Marketing, Sales |
| 11 | Profession | Job title/role | Software Engineer, Designer |
| 12 | Language | Default value: "English" | English |
| 13 | Language level | Default value: "B1" | B1 |
| 14 | Job Application Link | URL to job posting | https://rem-s.com/jobs/123 |
| 15 | Portfolio | Primary portfolio link | github.com/johnsmith |
| 16 | Portfolio1 | Comma-separated list of tools and software | Python, JavaScript, React, Docker |
| 17 | Portfolio2 | Comma-separated list of social media profiles | linkedin.com/in/johnsmith, twitter.com/john |
| 18 | Portfolio3 | Additional relevant information | 5 years experience, AWS certified |

---

### Processing Rules

1. **Field Order:** Maintain strict field order as specified above
2. **Missing Data:** If field is missing → output empty tab delimiter (do not skip the tab)
3. **Date Format:** Always use DD-MM-YYYY format (e.g., 13-10-2025)
4. **Default Values:** 
   - Language → "English"
   - Language level → "B1"
5. **Text Formatting:**
   - Remove line breaks from multi-line text
   - Preserve URLs without modification
   - Use comma-separated lists for multiple items
6. **Output Format:** Single line with tab separators, ready for direct paste into Google Sheets

---

### Example

**Input CV:**
```
John Smith
Software Engineer

Contact Information:
Email: john.smith@email.com
Phone: +1-555-0123
Telegram: @johnsmith

Location: United States

Skills:
- Python
- JavaScript
- React
- Docker
- PostgreSQL

Portfolio:
GitHub: github.com/johnsmith
LinkedIn: linkedin.com/in/johnsmith

Experience: 5 years in full-stack development
AWS Certified Solutions Architect
```

**Expected Output:**
```
John Smith	Unknown	United States	Email	john.smith@email.com	+1-555-0123	@johnsmith	New Application	13-10-2025		Software Engineer	English	B1		github.com/johnsmith	Python, JavaScript, React, Docker, PostgreSQL	linkedin.com/in/johnsmith	5 years in full-stack development, AWS Certified Solutions Architect
```

---

### Implementation Notes

- **Automation Ready:** This prompt is designed for integration with document processing APIs and automation workflows
- **Error Handling:** System should handle malformed CVs gracefully, filling available fields
- **Scalability:** Suitable for batch processing of multiple CVs
- **Validation:** Output can be validated against field count (18 fields expected)

---

## My Choice & Reasoning

**Selected Version:** Formal Technical (for Documentation/API Integration)

**Reasoning:**

1. **Scalability:** RemoteEmployees processes multiple CVs daily. A formal, structured prompt ensures consistency across different team members and potential API integrations.

2. **Documentation Value:** Technical format serves as both operational instruction and internal documentation. New team members can reference it without additional training materials.

3. **Error Reduction:** Clear field schema table and processing rules minimize human error and ambiguity during CV parsing.

4. **Future-Proof:** Formal structure allows easy integration with automation tools, ATS systems, or custom scripts as RemoteEmployees scales.

5. **Professional Standards:** As a B2B service company, maintaining professional documentation standards reflects organizational maturity and operational excellence.

---

**Task Completed:** 13-10-2025  
**Created with:** Claude AI  
**For:** RemoteEmployees (https://rem-s.com/)  
**Save to:** Prompt Library/13-10-2025_claude_prompt_refinement.md