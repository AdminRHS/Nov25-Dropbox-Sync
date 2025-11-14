// ...existing code...
# Task Breakdown - [Date]

## Instructions
**What**: Detailed action steps  
**Include**:
- Break each plan item into specific steps
- Add links and resources
- Clear instructions for execution

---

## Task 1: Redesign Homepage (Minimal + Interactive Video Cards)
### Steps:
1. Создать доску в Figma: страницы (Desktop, Mobile), сетки, типографика, цвета.
2. Нарисовать ключевые блоки: герой, списки курсов/карточки, видео-картки, footer.
3. Детализувати компонент відео-картки (thumbnail, duration, play overlay, transcript link).
4. Провести ревью з Стасом → внести правки.
5. Експорт компонентів і стиль-гайду для розробки.

### Resources and Links:
- Figma project (создать ссылку в таске)
- Reference: [Pages/video_page.md](Onboarding_Yuliia_Files/Dailis/web/Pages/video_page.md)

### Instructions:
- Priority: High. Виконувати послідовно; дизайн має бути готовий для handoff.

---

## Task 2: Implement Transcription Panel (Right-side accordion)
### Steps:
1. Спроєктувати API/структуру даних для транскрипту (массив рядків з data-start).
2. Реалізувати UI: аккордеон, контейнер рядків, стилізація, підсвітка активного рядка.
3. Додати логіку: по клику на таймстемп викликати video.currentTime = start.
4. Підключити timeupdate для синхронізації активного рядка.
5. Тестувати на різних відео/довжинах.

### Resources and Links:
- Референс розмітки: [Onboarding_Yuliia_Files/Dailis/web/video_page/index.html](Onboarding_Yuliia_Files/Dailis/web/video_page/index.html)
- Примеры transcript-line в коді сторінки.

### Instructions:
- Priority: High. Dev реалізує PoC, потім дизайн додає стилі.

---

## Task 3: Move RH site blocks to separate page
### Steps:
1. Ідентифікувати блоки для екстракції.
2. Підготувати компоненти/контент (HTML/CSS).
3. Додати новий роут/сторінку, перевірити адаптивність.
4. Поставити на рев'ю.

### Resources and Links:
- RH blocks reference (существующие файлы на проекте)
- Контентні матеріали від маркетингу

### Instructions:
- Priority: Medium.

---

## Task 4: Generate Visual Content (images & short videos)
### Steps:
1. Зібрати референси та вимоги (розміри, стилі).
2. Протестувати інструменти: Runway, Hi- algo, інші.
3. Згенерувати чернетки, віддати дизайнерам на рев'ю.
4. Підготувати пакет для верстки.

### Resources and Links:
- Design guidelines in Figma
- Runway / рекомендовані інструменти (посилання в таску)

### Instructions:
- Priority: Medium. Design lead відповідає.

---

## Reminder
- Для кожного таску додавати чеклист та відповідального в таск-трекер.
// ...existing code...