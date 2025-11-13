// ...existing code...
# Plans - from meeting [Date]

## Plan 1: Центральне сховище дизайн-токенів
**Goal:** Забезпечити єдине місце для зберігання кольорів, відступів, радіусів, поведінки кнопок.
**Steps:**
1. Описати список токенів (primary, secondary, dept-color, border-radius, spacing, button-variants).
2. Створити JSON/YAML конфіг у репо (shared-config) та приклади імпорту в фронтенд мікросервіси.
3. Прототип: реалізувати імпорт токенів у одному сервісі (наприклад, academy) та перевірити реактивність змін.
4. Додати тести і документацію у Figma + Markdown.
**Owner:** frontend lead / design-system dev
**Deadline:** +5 днів
**Resources:** дизайн-система, Figma, приклади компонентів.
**Related tasks:** See tasks in [Onboarding_Yuliia_Files/Dailis/report/task.md](Onboarding_Yuliia_Files/Dailis/report/task.md)

---

## Plan 2: Винести спільну бібліотеку компонентів ("MuiUikid")
**Goal:** Єдина реалізація Course Card, Buttons, Tags, Image wrapper.
**Steps:**
1. Інвентар компонентів в усіх сервісах (academy, m2e, talents).
2. Витягнути Course Card: props, data contract (title, author, progress, stats).
3. Впровадити компоненти як npm-пакет або git-submodule.
4. Додати можливість кастомізації через токени (colors, radii).
5. Документувати у Figma та README.
**Owner:** frontend dev + UI designer
**Deadline:** +7 днів

---

## Plan 3: Правила для зображень і кнопок
**Goal:** Однозначні правила позиціонування та стилів кнопок.
**Steps:**
1. Встановити правило: default image-position = center center; optional right center per card flag.
2. Установити fallback placeholder і правила aspect-ratio.
3. Кнопки: замінити розрізнені стилі на варіанти (primary, secondary, ghost) з використанням токенів; hover/active через opacity/brightness.
4. Оновити Figma компоненти та приклади.
**Owner:** UI designer + frontend dev
**Deadline:** +4 днів

---
// ...existing code...