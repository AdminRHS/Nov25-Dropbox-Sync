// ...existing code...
# Task Breakdown - 2025-11-12

## Task 1: Implement transcription pipeline (High)
**Goal:** от MD-транскрипта получать индексированную запись в /promp/.

### Steps:
1. Написать шаблон System Instructions (promp v4) — включить поля: title, source_link, tools[], use_cases[], suggested_tasks[].  
2. Регламент: копировать MD из Google AI Studio → сохранить в /transcribation/video-XYZ.md.  
3. Парсер: взять первую часть MD → заполнить meta (title, short summary, tags) → создать запись в /promp/index.json или markdown.  
4. Создать тикет на тест: прогонять 5 видео, проверить теги и summary.

### Resources:
- Пример страницы просмотра видео: [web/video_page/index.html](Onboarding_Yuliia_Files/Dailis/web/video_page/index.html)
- Daily (контекст): [report/daily.md](Onboarding_Yuliia_Files/Dailis/report/daily.md)

**Owner:** Yulia  
**ETA:** 2025-11-17

---

## Task 2: ZOHO test email campaign (Medium)
**Goal:** подготовить MVP email-шаблона и провести тестовую отправку.

### Steps:
1. Сделать список функциональных требований ZOHO (limits, template insertion).  
2. Сгенерировать HTML-шаблон (responsive, простая таблица) — протестировать на разных клиентах.  
3. Подготовить тестовый список, отправить и собрать результаты.

### Resources:
- Тестовые требования: daily notes — [report/daily.md](Onboarding_Yuliia_Files/Dailis/report/daily.md)

**Owner:** Dev + Designer  
**ETA:** 2025-11-14

---

## Task 3: Black Friday storyboard assets (Medium)
**Goal:** подготовить серию постов и сторіборд.

### Steps:
1. Сформировать 3 сторітелінг-концепції.  
2. Сгенерировать героїв / mascots (purple accents), full-body для анімації.  
3. Подготовить 5 постів + 3 сторіз, оформить copy.

**Owner:** Art Lead / Social  
**ETA:** 2025-11-18

---

## Task 4: Organize Dropbox folders & permissions (Quick)
**Goal:** упорядочить design-department, transcribation, promp в DD.

### Steps:
1. Подтвердить path и список пользователей; создать backup v1.1.  
2. Документировать структуру и права доступа (README в папке).

**Owner:** Kolya  
**ETA:** 2025-11-14

---

## Reminder
- Для каждого таска добавить чек-лист и ссылку на результаты.
- Если нужен пример парсера MD → index, отмечайте в таске 1 (Dev).
// ...existing code...
