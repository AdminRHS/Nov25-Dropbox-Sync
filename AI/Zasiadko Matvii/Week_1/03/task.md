### Детальна таска на день (по кроках)

- Відновити дані БД і стабільність API
  - Перевірити підключення до БД і доступність ендпоінтів:
    - GET `api/get-employees` → очікується масив співробітників
    - POST `api/add-violation` → очікується запис порушення за валідним `employeeId`
    - POST `api/update-data` → приймає JSON-рядок у полі `data`
  - Засідити таблицю `employees` даними з `data.json`:
    - Виконати підготовлений INSERT зі всіма записами
    - Перевірити `SELECT COUNT(*) FROM employees;`
    - Вирівняти `id` за потреби:
      - Якщо треба з 0: `UPDATE employees SET id = id - 33;` (або перезапустити sequence)
      - Переконатися, що sequence синхронізований: `SELECT setval('employees_id_seq', (SELECT MAX(id) FROM employees));`
  - Smoke-тест API (локально/стейджинг):
    - GET `get-employees` → не порожній
    - POST `add-violation` (body: employeeId існує + violation) → статус 200/ok
    - POST `update-data` (data — валідний JSON-рядок) → статус 200/ok

- Перевірка фронтенду після рефакторингу (визначені модулі)
  - Переконатися, що скрипти підключені в правильному порядку:
    - `lib/modals.js` → `lib/render-stats.js` → `lib/frontend-api.js` → `lib/actions.js` → `lib/ui.js` → `lib/theme.js`
  - Перевірити наявність глобальних функцій у консолі:
    - `renderAll`, `renderCalendar`, `renderStats`, `renderLeaderboard`, `renderTeamGrids`, `renderModals`
    - `addViolationViaAPI`, `saveViaAPI`, `loadEmployeesFromAPI`, `persistIfPossible`
    - `switchTab`, `changeMonth`, `navigateToEmployee`
    - `initializeTheme`, `toggleTheme`, `updateThemeButton`
  - Переконатися, що `API_CONFIG` ініціалізується до виклику `loadEmployeesFromAPI` (в `DOMContentLoaded` порядок вірний)

- Manual QA — ключові сценарії
  - Yellow Card
    - Відкрити “Give Yellow Card” → заповнити → “Issue Yellow Card”
    - Перевірити статуси: “Saving…” → “✓ Saved”
    - Переконатися, що запис одразу з’явився в таблиці; календар підсвітив день; оглядові метрики оновилися
    - Клікнути на підсвічений день у календарі → модалка дня зчитує дати без `T00:00:00.000Z`
  - Team
    - Клік по співробітнику → модалка з ініціалами, роллю, відділом, контактами, історією порушень
    - Кнопки копіювання (Email/Discord) → “Copied!” + заміна іконки на галочку на 1.5s, потім відкат
    - Натиснути Edit → змінити дані → Save → статус “✓ Saved”, зміни видимі на сторінці
  - Leaderboard
    - Змінювати Department/Period/Search → таблиця і п’єдестал оновлюються коректно
    - Клік по рядку → переходить на вкладку Team і відкриває модалку співробітника
  - Theme
    - Перемкнути Dark/Light → застосовується миттєво, стан зберігається після reload

- Узгодження фронт ↔ бекенд (схеми даних)
  - Вирівняти назви полів:
    - БД: `discord_id`, фронт: `discordId` → в бекенді додати мапінг або змінити селект/DTO
    - Дата порушення: фронт зберігає `YYYY-MM-DD` (без часу), бекенд приймає і повертає в узгодженому форматі
  - Валідація в бекенді:
    - `add-violation`: перевірка `employeeId`, структура `violation`, контроль типів
    - Обробка помилок з чіткими повідомленнями (JSON), HTTP-коди 4xx/5xx

- Прибирання і консистентність у фронті
  - Видалити зайві коментарі-мітки з `index.html`, залишити тільки справді потрібні
  - Перевірити, що всі колбеки/виклики посилаються на винесені функції (відсутні дублікати у `index.html`)
  - Перевірити обробники подій на клік (делегування для таблиць, модалок, dropdown)
  - Розв’язати можливі гонки завантаження (всі виклики, що залежать від `employees`, після `loadEmployeesFromAPI`)

- Поліпшення UX (за часом)
  - Замінити текстовий статус збереження на toast-компонент (success/error)
  - Додавати disable-стан кнопок під час запитів (`saving`)
  - Для великих наборів даних — додати пагінацію/віртуалізацію Leaderboard
  - Перевірити доступність (aria-атрибути для модалок/кнопок)

- Надійність і fallback-и
  - Якщо `get-employees` повернув порожньо — показати дружнє повідомлення й CTA “Reload” (без автопідміни локальним `data.json`, щоб не маскувати проблему)
  - Додати кнопку “Force reload from API” (перевиклик `loadEmployeesFromAPI`, `renderAll`)

- Документація і нотатки
  - Короткий README:
    - Архітектура фронту: що в якому файлі (`actions.js`, `modals.js`, `render-stats.js`, `ui.js`, `theme.js`, `frontend-api.js`)
    - Порядок ініціалізації сторінки (DOMContentLoaded → loadEmployeesFromAPI → renderAll)
    - Опис ендпоінтів і вимог до форматів
  - SQL-cheatsheet:
    - Вставка даних з `data.json` (готовий INSERT)
    - Рестарт sequence/зсув `id`
    - Базові перевірки (`SELECT COUNT(*)`, вибірка top-N)
  - Список known issues і ідей на завтра:
    - Audit trail (хто/коли видав картку)
    - Bulk-import endpoint
    - Ролі доступу (admin/operator/viewer)

- Релізні кроки
  - Стейджинг: на “чистій” БД пройти smoke-тести
  - Прод деплой: перевірити логи й помилки, підтвердити роботу основних сценаріїв
  - План відкату (якщо БД знову порожня): швидкий repeat SQL-seed + перезапуск sequence

- Контрольні точки дня
  - [ ] Дані в БД засіяні, `id` вирівняний
  - [ ] API працює: GET/POST успішні
  - [ ] Усі вкладки/модалки/календар/статистика працюють
  - [ ] Формат дат без `T00:00:00.000Z` усюди, де потрібно
  - [ ] Порядок скриптів коректний, глобальні функції доступні
  - [ ] README + SQL-cheatsheet оновлені
  - [ ] Записані known issues і план на завтра
