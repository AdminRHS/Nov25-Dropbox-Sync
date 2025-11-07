# Как создать долгоживущий Dropbox токен (Refresh Token)

## Проблема
Dropbox access tokens истекают через несколько часов. Для постоянной автоматизации нужен refresh token механизм.

## Решение: OAuth 2.0 с Offline Access

### Быстрый способ (используя готовый скрипт) ⚡

1. **Запустите скрипт**:
```bash
cd "/Users/nikolay/Library/CloudStorage/Dropbox/automations/dropbox-sync"
python get_refresh_token.py
```

2. Скрипт проведет вас через весь процесс:
   - Попросит App Key и App Secret
   - Даст ссылку для авторизации
   - Попросит код авторизации
   - Выдаст все необходимые токены

3. **Добавьте секреты в GitHub**:
   - Откройте: https://github.com/AdminRHS/Nov25-Dropbox-Sync/settings/secrets/actions
   - Добавьте/обновите:
     - `DROPBOX_ACCESS_TOKEN` - access token из скрипта
     - `DROPBOX_REFRESH_TOKEN` - refresh token из скрипта
     - `DROPBOX_APP_KEY` - ваш App Key
     - `DROPBOX_APP_SECRET` - ваш App Secret

### Ручной способ

#### Шаг 1: Получите App Key и App Secret

1. Откройте: https://www.dropbox.com/developers/apps
2. Найдите ваше приложение (то же, что для Employee Profile Sync)
3. Перейдите в **"Settings"** tab
4. Найдите:
   - **App key** (например: `abc123xyz`)
   - **App secret** (например: `def456uvw`)
5. Скопируйте оба значения

#### Шаг 2: Получите Refresh Token

1. Откройте в браузере (замените YOUR_APP_KEY на ваш App Key):
```
https://www.dropbox.com/oauth2/authorize?client_id=YOUR_APP_KEY&response_type=code&token_access_type=offline
```

2. Авторизуйте приложение и скопируйте код из URL (параметр `code=...`)

3. Выполните команду (замените значения):
```bash
curl https://api.dropbox.com/oauth2/token \
  -d code=ВАШ_КОД_АВТОРИЗАЦИИ \
  -d grant_type=authorization_code \
  -u YOUR_APP_KEY:YOUR_APP_SECRET
```

4. В ответе JSON будут:
   - `access_token` - текущий access token
   - `refresh_token` - долгоживущий refresh token

#### Шаг 3: Добавьте секреты в GitHub

1. Откройте: https://github.com/AdminRHS/Nov25-Dropbox-Sync/settings/secrets/actions

2. Добавьте/обновите следующие секреты:
   - **DROPBOX_ACCESS_TOKEN** - access token из шага 2
   - **DROPBOX_REFRESH_TOKEN** - refresh token из шага 2
   - **DROPBOX_APP_KEY** - ваш App Key
   - **DROPBOX_APP_SECRET** - ваш App Secret

### Как это работает

- **Refresh token** - долгоживущий токен (не истекает месяцами/годами)
- **Access token** - короткоживущий токен (истекает через несколько часов)
- Скрипт автоматически обновляет access token при истечении используя refresh token
- **Вам НЕ нужно будет обновлять токены вручную!**

### Важно

- Используйте `token_access_type=offline` при авторизации - это дает refresh token
- Refresh token можно использовать многократно для получения новых access tokens
- После настройки синхронизация будет работать постоянно без перерывов

### Проверка

После добавления всех 4 секретов в GitHub, запустите синхронизацию. Если токен истечет, скрипт автоматически обновит его.
