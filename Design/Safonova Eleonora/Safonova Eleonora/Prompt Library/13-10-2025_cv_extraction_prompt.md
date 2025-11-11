# CV Extraction Prompt — 13-10-2025

## Prompt

Extract all available data from a candidate’s text (CV snippet, message, etc.) and output it as a tab-separated row ready to paste into Google Sheets. Use the following column structure:

Name	Candidate
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

If any field is missing, leave it blank (but keep the tab).
The output must be one single line, ready to paste directly into Google Sheets.

---

## Example Input

Hi! I’m **Anna Petrova** from **Ukraine**. I’m a **graphic designer** specializing in branding and social media visuals.  
**Portfolio:** https://www.behance.net/annapetrova  
**Contact:** Telegram (@annap_design), Email (anna.petrova@gmail.com)  
**Tools:** Adobe Photoshop, Illustrator, Figma, Canva  
**Instagram:** https://instagram.com/annapdesign  

---

## Expected Output (tab-separated)

Anna Petrova	Candidate	Ukraine	Telegram, Email	anna.petrova@gmail.com		@annap_design	Applied	13-10-2025	Design	Graphic Designer	English	B1		https://www.behance.net/annapetrova	Adobe Photoshop, Illustrator, Figma, Canva	https://instagram.com/annapdesign	-

---

## Test Example (Custom Data)

Hi! My name is **Matvii Savitski** from **Ukraine**. I’m a **sound designer** with experience in **game development and music production**.  
**Email:** matvii.savitski@gmail.com  
**Phone:** +380971234567  
**Telegram:** @matvii888  
**Portfolio:** https://soundcloud.com/matvii_savitski  
**Tools:** Reaper, Ableton Live, Pro Tools, Izotope RX  
**Instagram:** https://instagram.com/matvii_sound

### Output (tab-separated)
Matvii Savitski	Candidate	Ukraine	Email, Telegram	matvii.savitski@gmail.com	+380971234567	@matvii888	Applied	13-10-2025	Audio	Sound Designer	English	B1		https://soundcloud.com/matvii_savitski	Reaper, Ableton Live, Pro Tools, Izotope RX	https://instagram.com/matvii_sound	-

