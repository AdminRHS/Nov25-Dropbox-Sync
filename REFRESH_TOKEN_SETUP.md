# Как создать долгоживущий Dropbox токен (Refresh Token)

## Проблема
Dropbox access tokens истекают через несколько часов. Для постоянной автоматизации нужен refresh token механизм.

## Решение: OAuth 2.0 с Offline Access

### Шаг 1: Получите App Key и App Secret

1. Откройте: https://www.dropbox.com/developers/apps
2. Найдите ваше приложение (или создайте новое)
3. Перейдите в **"Settings"** tab
4. Найдите:
   - **App key** (например: `abc123xyz`)
   - **App secret** (например: `def456uvw`)
5. Скопируйте оба значения

### Шаг 2: Получите Refresh Token через OAuth Flow

**Вариант A: Используя Python скрипт (рекомендуется)**

Создайте файл `get_refresh_token.py`:

```python
import dropbox
from dropbox import DropboxOAuth2FlowNoRedirect

APP_KEY = "ваш_app_key"
APP_SECRET = "ваш_app_secret"

auth_flow = DropboxOAuth2FlowNoRedirect(APP_KEY, APP_SECRET, token_access_type='offline')

authorize_url = auth_flow.start()
print(f"1. Перейдите по ссылке: {authorize_url}")
print("2. Авторизуйте приложение")
print("3. Скопируйте код авторизации и вставьте ниже:")

auth_code = input("Введите код авторизации: ").strip()

try:
    oauth_result = auth_flow.finish(auth_code)
    print("\n✅ Успешно!")
    print(f"Access Token: {oauth_result.access_token}")
    print(f"Refresh Token: {oauth_result.refresh_token}")
    print("\nСохраните эти значения в GitHub Secrets:")
    print(f"DROPBOX_ACCESS_TOKEN = {oauth_result.access_token}")
    print(f"DROPBOX_REFRESH_TOKEN = {oauth_result.refresh_token}")
except Exception as e:
    print(f"Ошибка: {e}")
```

Запустите скрипт:
```bash
python get_refresh_token.py
```

**Вариант B: Используя curl (альтернатива)**

1. Откройте в браузере (замените YOUR_APP_KEY):
```
https://www.dropbox.com/oauth2/authorize?client_id=YOUR_APP_KEY&response_type=code&token_access_type=offline
```

2. Авторизуйте и скопируйте код из URL (параметр `code=...`)

3. Выполните (замените YOUR_APP_KEY, YOUR_APP_SECRET, AUTHORIZATION_CODE):
```bash
curl https://api.dropbox.com/oauth2/token \
  -d code=AUTHORIZATION_CODE \
  -d grant_type=authorization_code \
  -u YOUR_APP_KEY:YOUR_APP_SECRET
```

4. В ответе будут `access_token` и `refresh_token`

### Шаг 3: Добавьте секреты в GitHub

1. Откройте: https://github.com/AdminRHS/Nov25-Dropbox-Sync/settings/secrets/actions

2. Добавьте/обновите следующие секреты:
   - **DROPBOX_ACCESS_TOKEN** - текущий access token
   - **DROPBOX_APP_KEY** - ваш App Key
   - **DROPBOX_APP_SECRET** - ваш App Secret  
   - **DROPBOX_REFRESH_TOKEN** - refresh token (полученный выше)

### Шаг 4: Как это работает

- Скрипт автоматически обновит access token при истечении
- Refresh token не истекает (или истекает через очень долгое время)
- Синхронизация будет работать постоянно без ручного обновления токенов

## Важно

- **Refresh token** - это долгоживущий токен, который позволяет получать новые access tokens
- **Access token** - короткоживущий токен, который автоматически обновляется
- После настройки refresh token механизма, вам НЕ нужно будет обновлять токены вручную

## Проверка

После добавления всех секретов, запустите синхронизацию. Скрипт автоматически обновит токен при необходимости.

