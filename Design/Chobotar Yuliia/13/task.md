// ...existing code...
# Task Breakdown - [Date]


## Task 1: Створити shared design-tokens (central config)
### Steps:
1. Зібрати список необхідних токенів (colors, spacing, radii, button variants).
2. Дамп у форматі JSON (example: design-tokens.json) у папці /shared-config.
3. Написати приклад імпорту в academy проект (CSS variables / JS exporter).
4. Додати коротку інструкцію у README та пункт у Figma notes.
### Resources and Links:
- Figma: дизайн-система (позначити в Figma)
- [Onboarding_Yuliia_Files/Dailis/report/plans.md](Onboarding_Yuliia_Files/Dailis/report/plans.md)
### Instructions:
- Використовувати змінні в CSS як --color-primary, --dept-color-<id>.
- Забезпечити backwards compatibility через fallback values.

---

## Task 2: Винести Course Card в спільну бібліотеку
### Steps:
1. Зробити інвентар поля картки в усіх сервісах.
2. Описати data-contract (title, img, author, progress, stats, buttons).
3. Зробити компонент із варіантами (compact/regular) та props для imageAlign.
4. Підготувати package + basic storybook entry (або simple demo page).
### Resources and Links:
- Використати існуючі приклади карток у проектах (search for "Course Card" components).
- [Onboarding_Yuliia_Files/Dailis/report/plans.md](Onboarding_Yuliia_Files/Dailis/report/plans.md)
### Instructions:
- Забезпечити theming через токени.
- Надавати приклад підключення в README.

---

## Task 3: Правки зображень та кнопок у проєкті academy
### Steps:
1. Впровадити правило image-position: center center; додати опцію image-align: right.
2. Додати fallback placeholder для карток (замість gradient loader).
3. Уніфікувати стилі кнопок: primary/secondary/ghost, hover через opacity.
4. Протестувати на різних breakpoints.
### Resources:
- Design tokens config (Task 1)
- Figma components
### Instructions:
- Тестувати на 3 ширинах: 360px, 768px, 1366px.

---
// ...existing code...