# Gemini CV Extraction Prompt — 13-10-2025

## Prompt

**Objective:**  
Extract candidate data from pasted or uploaded text (CV snippet or message) and output it as a **tab-separated row** ready for Google Sheets. Include all fields below.

**Fields to extract:**

```
Name    Candidate
Source
Country
Channel Communication
Email
Phone
Telegram
Status (Application)
Last Contact Date (write in format: 13-10-2025)
Department
Profession
Language (always English)
Language level (always B1)
Job Application Link
Portfolio (link to Behance, GitHub, Dribbble, or website)
Portfolio1 (all tools and software listed)
Portfolio2 (all social media links)
Portfolio3 (any additional info)
```

**Instructions for Gemini:**

1. Accept **pasted text** or **uploaded file** containing CV or candidate message.  
2. Extract data for all fields above.  
3. If a field is missing, leave it blank but keep the tab.  
4. Output everything in **one tab-separated line**, ready for Google Sheets.  
5. Add **one additional line** with short company info about RemoteEmployees from [https://rem-s.com/](https://rem-s.com/).  

---

## Test Example

**Input (example CV):**

> Hi! I’m Anna Petrova from Ukraine. I’m a graphic designer specializing in branding and social media visuals.  
> Portfolio: https://www.behance.net/annapetrova  
> Contact: Telegram (@annap_design), Email (anna.petrova@gmail.com)  
> Tools: Adobe Photoshop, Illustrator, Figma, Canva  
> Instagram: https://instagram.com/annapdesign  

**Expected Output (tab-separated):**

```
Anna Petrova	Candidate	Portfolio link	Ukraine	Telegram, Email	anna.petrova@gmail.com		@annap_design	Applied	13-10-2025	Design	Graphic Designer	English	B1		https://www.behance.net/annapetrova	Adobe Photoshop, Illustrator, Figma, Canva	https://instagram.com/annapdesign	-
RemoteEmployees	Company	Website	-	-	-	-	-	-	-	-	-	English	B1	https://rem-s.com/	-	-	-	-
```

---

**Save as Markdown for Dropbox:**  
```
Prompt Library/13-10-2025_gemini_cv_extraction.md
```

Include: final Gemini prompt + test example output.
