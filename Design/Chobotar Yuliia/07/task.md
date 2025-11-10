# Task Breakdown - 2025-11-06

## Instructions
**What**: Detailed action steps
**Include**:
- Break each plan item into specific steps
- Add links and resources
- Clear instructions for execution

---

## Reference: full call transcript (06.11)
Звук 2025 11 06 09 53 12 152
(полная транскрибация звонка см. файл: c:\Users\chobo\Dropbox\Onboarding_Yuliia_Files\Dailis\report\06.11.md)

---

## Task 1: Audit employee profiles (High, due 2025-11-10)
### Steps:
1. Request latest master CSV from бухгалтерии / HR (if нет — запросить доступ).
2. Normalize fields: ID, full name, email, project assignment.
3. Iterate по Dropbox -> department root -> employee folders:
   - Check presence of profile file (profile.md / profile.json) and portrait.
   - Note mismatches (employee in CSV but no folder; folder but not in CSV).
4. Fill audit CSV: ID, name, status (available/project/absent), has_profile (Y/N), has_portrait (Y/N), action_required (request_photo / create_placeholder / update_profile).
5. Push CSV в /Onboarding_Yuliia_Files/Dailis/report/ и расшарить с Kolia/Villy.
6. Create backlog tickets for missing items (owner + due date).

### Resources:
- Meeting transcript: c:\Users\chobo\Dropbox\Onboarding_Yuliia_Files\Dailis\report\06.11.md
- Master file (accounting/HR export) — retrieve from Dropbox (admin link).

### Notes:
- Start со списка первых 15 (приоритет).
- Работать пачками (по 50), отмечая прогресс в CSV.

---

## Task 2: Portraits for first 15 positions (High, due 2025-11-10)
### Steps:
1. Pull first-15 list из результата Task 1.
2. For each person:
   - If portrait exists — check resolution/format, экспортировать 800x800 JPG/PNG.
   - If missing — запросить фото в рабочем чате; если нет — сгенерировать placeholder (AI avatar) и пометить.
3. Save into: /Onboarding_Yuliia_Files/Dailis/report/portraits/2025-11-06/
4. Update audit CSV с ссылками на файлы и статусом QA.
5. QA: Polina — визуальная проверка, переименовать файлы по шаблону ID_name.jpg.

### Resources:
- Shared folder: /Onboarding_Yuliia_Files/Dailis/report/portraits/

---

## Task 3: Process Dasha Azanova video folder (High, due 2025-11-10)
### Steps:
1. Locate Dasha Azanova folder in Dropbox (ask Dasha for exact path if not known).
2. Run transcription (Whisper/WhisperFlow/OCAMP) on each video file.
3. Export SRT and plain-text transcripts with timestamps.
4. Place transcripts in: /Onboarding_Yuliia_Files/Dailis/report/video-transcripts/Dasha_Azanova/2025-11-06/
5. Add summary CSV: video_filename, duration, transcript_link, key_timestamps.
6. If transcription quality low — re-run with adjusted params or request original audio.

### Resources:
- Tools: Whisper/WhisperFlow, Otter/OCAMP (as available).
- Meeting transcript for context: c:\Users\chobo\Dropbox\Onboarding_Yuliia_Files\Dailis\report\06.11.md

---

## Task 4: CapCut best-practices guide (Medium, due 2025-11-14)
### Steps:
1. Collect notes from call re: CapCut behaviour (free vs pro, export/version limits, subtitles).
2. Test common flows: export limits, version history, subtitle generation.
3. Draft one-pager: recommended version, export checklist, subtitle tips, what to avoid (paid-only transitions), fallback workflows (Premiere / Runway).
4. Publish guide: /Onboarding_Yuliia_Files/Dailis/docs/capcut-best-practices.md and share link.

### Outcome:
- 1-page markdown guide + short screencast (optional).

---

## Task 5: Reporting process (Medium, due 2025-11-14)
### Steps:
1. Create templates for Daily and Weekly reports (fields: tasks done, blockers, next steps, links).
2. Communicate format to team (Natasha case: clarify working hours and expected delivery times).
3. Digitize: make a simple checklist/Google Form to collect daily updates.

### Owner:
- Project lead (confirm Kolia). Implementation: Yuliia.

---

## Task 6: Onboarding presentation scenario (Medium, due 2025-11-14)
### Steps:
1. Draft slide-by-slide script using meeting notes (purpose: onboarding designers).
2. For each slide: title, content, speaker notes, required visual.
3. Generate or brief 10 reference images via AI (Midjourney / internal tool).
4. Package draft PPT/Google Slides and ask for review.

---

## Reminders & Notes
- Attach links to all outputs in master audit CSV.
- Notify owners in chat and set short daily check-ins for high-priority items.
- Use the full call transcript (06.11.md) as the factual source.

(Полный текст транскрибації доступний у файлі: c:\Users\chobo\Dropbox\Onboarding_Yuliia_Files\Dailis\report\06.11.md)
