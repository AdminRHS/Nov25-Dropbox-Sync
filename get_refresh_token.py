#!/usr/bin/env python3
"""
Скрипт для получения Dropbox Refresh Token

Этот скрипт поможет получить долгоживущий refresh token для автоматического обновления access token.
"""

import sys

try:
    from dropbox import DropboxOAuth2FlowNoRedirect
except ImportError:
    print("ERROR: Dropbox SDK not installed. Run: pip install dropbox")
    sys.exit(1)


def get_refresh_token():
    print("=" * 80)
    print("Dropbox Refresh Token Generator")
    print("=" * 80)
    print()
    
    # Get App Key and Secret
    print("Шаг 1: Получите App Key и App Secret")
    print("1. Откройте: https://www.dropbox.com/developers/apps")
    print("2. Найдите ваше приложение (или создайте новое)")
    print("3. Перейдите в Settings → App key и App secret")
    print()
    
    app_key = input("Введите App Key: ").strip()
    app_secret = input("Введите App Secret: ").strip()
    
    if not app_key or not app_secret:
        print("❌ App Key и App Secret обязательны!")
        sys.exit(1)
    
    print()
    print("=" * 80)
    print("Шаг 2: Авторизация")
    print("=" * 80)
    print()
    
    # Create OAuth flow
    auth_flow = DropboxOAuth2FlowNoRedirect(
        app_key, 
        app_secret, 
        token_access_type='offline'  # Это важно! offline дает refresh token
    )
    
    # Get authorization URL
    authorize_url = auth_flow.start()
    
    print(f"1. Откройте эту ссылку в браузере:")
    print()
    print(f"   {authorize_url}")
    print()
    print("2. Войдите в Dropbox и авторизуйте приложение")
    print("3. После авторизации вы будете перенаправлены на страницу с кодом")
    print("4. Скопируйте код авторизации (authorization code)")
    print()
    
    auth_code = input("Введите код авторизации: ").strip()
    
    if not auth_code:
        print("❌ Код авторизации обязателен!")
        sys.exit(1)
    
    print()
    print("Получение токенов...")
    
    try:
        # Exchange authorization code for tokens
        oauth_result = auth_flow.finish(auth_code)
        
        print()
        print("=" * 80)
        print("✅ УСПЕШНО!")
        print("=" * 80)
        print()
        print("Сохраните эти значения в GitHub Secrets:")
        print()
        print(f"DROPBOX_ACCESS_TOKEN = {oauth_result.access_token}")
        print()
        
        if oauth_result.refresh_token:
            print(f"DROPBOX_REFRESH_TOKEN = {oauth_result.refresh_token}")
            print()
            print("✅ Refresh token получен! Теперь токены будут обновляться автоматически.")
        else:
            print("⚠️  Refresh token не получен. Убедитесь, что использовали token_access_type='offline'")
        
        print()
        print("Также добавьте:")
        print(f"DROPBOX_APP_KEY = {app_key}")
        print(f"DROPBOX_APP_SECRET = {app_secret}")
        print()
        print("=" * 80)
        print("Инструкция:")
        print("1. Откройте: https://github.com/AdminRHS/Nov25-Dropbox-Sync/settings/secrets/actions")
        print("2. Добавьте/обновите все 4 секрета выше")
        print("3. Запустите синхронизацию - токены будут обновляться автоматически!")
        print("=" * 80)
        
    except Exception as e:
        print(f"❌ Ошибка: {e}")
        print()
        print("Возможные причины:")
        print("- Неверный код авторизации")
        print("- Код уже использован")
        print("- Истек срок действия кода (попробуйте снова)")
        sys.exit(1)


if __name__ == "__main__":
    get_refresh_token()

