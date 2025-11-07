# Инструкция по настройке Dropbox → GitHub Sync

## Шаг 1: Создать GitHub репозиторий

1. Перейдите на https://github.com
2. Нажмите **"+"** → **"New repository"**
3. Настройки:
   - **Repository name**: `Nov25-Dropbox-Sync`
   - **Description**: "Automated sync of Nov25 Dropbox folder to GitHub"
   - **Visibility**: **Private**
   - **Initialize**: НЕ ставьте галочки (создадим пустой)
4. Нажмите **"Create repository"**

## Шаг 2: Добавить Dropbox токен в GitHub Secrets

1. В репозитории перейдите: **Settings** → **Secrets and variables** → **Actions**
2. Нажмите **"New repository secret"**
3. Настройки:
   - **Name**: `DROPBOX_ACCESS_TOKEN`
   - **Value**: Ваш Dropbox access token (тот же, что использовали для Employee Profile Sync)
4. Нажмите **"Add secret"**

## Шаг 3: Инициализировать и запушить код

Выполните команды:

```bash
cd "/Users/nikolay/Library/CloudStorage/Dropbox/.sync-automation"

# Инициализировать git
git init

# Добавить все файлы
git add .

# Создать первый коммит
git commit -m "Initial commit: Dropbox to GitHub sync automation"

# Добавить remote (замените YOUR_USERNAME на ваш GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/Nov25-Dropbox-Sync.git

# Переименовать ветку в main
git branch -M main

# Запушить код
git push -u origin main
```

**Примечание**: При push вам понадобится GitHub Personal Access Token (тот же, что использовали ранее).

## Шаг 4: Проверить работу

1. Перейдите в **Actions** tab репозитория
2. Нажмите **"Run workflow"** для первого тестового запуска
3. Дождитесь завершения и проверьте результаты

## Расписание

После настройки workflow будет запускаться автоматически **каждые 2 часа**.

Также можно запускать вручную через GitHub Actions UI.

## Что синхронизируется

- ✅ Папка `/Nov25` из Dropbox
- ✅ Все подпапки и файлы рекурсивно
- ❌ Исключается папка `.automation`

## Changelog

После каждой синхронизации создается/обновляется файл `CHANGELOG.md` с детальной информацией:
- Группировка по отделам (Design, AI, Video, LG, Dev)
- Группировка по сотрудникам
- Типы изменений (добавлено/изменено/удалено)
- Метаданные файлов (размер, дата, автор)

