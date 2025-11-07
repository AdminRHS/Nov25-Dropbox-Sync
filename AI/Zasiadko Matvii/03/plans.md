### План на день 

- Високий пріоритет: Негайно відновити дані та стабільність
  - Перевірити підключення до БД та доступність `get-employees`, `add-violation`, `update-data`.
  - Засідити таблицю `employees` даними з `data.json`:
    - Виконати INSERT (вже згенерований), перевірити `SELECT COUNT(*)`.
    - Вирівняти `id` (за потреби):
      - Якщо старт із 0: `ALTER SEQUENCE ... RESTART WITH 0` або `UPDATE employees SET id = id - 33;`.
  - Smoke-тест API:
    - `GET /api/get-employees` → має повертати список.
    - `POST /api/add-violation` із валідним `employeeId` → має зберігати.
    - `POST /api/update-data` → має приймати JSON-рядок.
  - На фронті:
    - Перезавантажити, пересвідчитись, що дані відмальовуються (Overview, Leaderboard, Yellow Card, Team).
    - Перевірити, що дати в модалках без `T00:00:00.000Z`.

- Рефакторинг фронтенду: завершення, прибирання, узгодження
  - Винесені модулі: `lib/actions.js`, `lib/modals.js`, `lib/render-stats.js`, `lib/ui.js`, `lib/theme.js`, `lib/frontend-api.js`.
  - Пройтись і видалити зайві коментарі-мітки в `index.html` (залишити тільки справді корисні).
  - Перевірити порядок підключення скриптів:
    - `modals.js` → `render-stats.js` → `frontend-api.js` → `actions.js` → `ui.js` → `theme.js`.
  - Зробити швидкий аудит глобальних функцій:
    - У консолі: `typeof renderAll`, `renderCalendar`, `renderStats`, `renderLeaderboard`, `renderTeamGrids`, `renderModals`, `addViolationViaAPI`, `saveViaAPI`, `loadEmployeesFromAPI`, `persistIfPossible`, `switchTab`, `changeMonth`, `navigateToEmployee`, `initializeTheme`, `toggleTheme` → всі повинні бути "function".
  - Перевірити, що `API_CONFIG` ініціалізується до виклику `loadEmployeesFromAPI`.

- Функціональні перевірки (manual QA)
  - Yellow Card
    - Відкрити “Give Yellow Card”, видати картку, перевірити статус “Saving → ✓ Saved”, миттєве оновлення таблиці та календаря.
    - Клік на підсвічений день → модалка дня, дати без `T...Z`.
  - Team
    - Клік по співробітнику → модалка профілю (значки, контакти, історія порушень).
    - Кнопка копіювання (Email/Discord) → “Copied!” та зміна іконки.
    - Edit → Save → статус збереження, оновлення записів.
  - Leaderboard
    - Фільтри Department/Period/Search → таблиця та п’єдестал оновлюються.
  - Theme
    - Перемикання Dark/Light, збереження стану після refresh.

- Backend tasks (узгодження/перевірка)
  - Переконатися, що ендпоінти використовують однакові назви полів: `discord_id` (БД) ↔ `discordId` (UI). Вирішити через мапінг у бекенді.
  - Валідація вхідних даних в `add-violation` (наявність `employeeId`, структура `violation`).
  - Додати логування помилок (рівні: info/warn/error) з кореляцією запитів.
  - Переконатися, що `update-data` справді потрібен; якщо ні — прибрати/змінити призначення.

- Поліпшення UX/UI (сьогодні, якщо залишиться час)
  - Тости замість текстового статусу збереження.
  - Disable-стани кнопок під час запитів.
  - Пагінація/віртуалізація таблиці, якщо набагато більше співробітників.
  - Лінки в модалці (клік по email → `mailto:`, discord → копіювання id, опційно deep-link).

- Надійність і telemetry
  - Обробка failover: якщо `get-employees` повертає порожньо → опційний fallback із `data.json` (за вимкненням — ні, щоб не маскувати проблеми з БД).
  - Мінімальні health-check-и:
    - Кнопка “Force reload from API” для ручного рефрешу.
    - Обробка 4xx/5xx з дружніми повідомленнями.

- Документація (коротко, щоб завтра не згадувати)
  - README технічний блок:
    - Архітектура фронту (що де винесено).
    - Порядок ініціалізації (`API_CONFIG`, скрипти).
    - Формати API.
  - SQL-cheatsheet:
    - Insert з `data.json`.
    - Рестарт sequence/зсув id.
    - Перевірка даних (`SELECT COUNT(*)`, top-10).

- Реліз/деплой
  - Staging-перевірка з “чистою” БД.
  - Smoke-тести користувацьких сценаріїв.
  - Деплой на прод, пост-релізний моніторинг логів і помилок.

- Stretch (за наявності часу)
  - Ендпоінт для bulk-import із `data.json`.
  - Версіонування змін (audit trail: хто і коли видав картку).
  - Ролі/права (admin/operator/viewer).

Чек-лист сьогодні:
- [ ] Засідити БД і вирівняти `id`.
- [ ] Перевірити всі ендпоінти (GET/POST).
- [ ] Пройтись по всіх вкладках і модалках (UI/UX).
- [ ] Провірити форматування дат у всіх місцях.
- [ ] Перевірити ініціалізацію `API_CONFIG` і порядок скриптів.
- [ ] Написати короткий технічний README і SQL-cheatsheet.
- [ ] Зафіксувати known issues і план на завтра.
