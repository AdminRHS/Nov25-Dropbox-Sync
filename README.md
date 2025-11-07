# Nov25 Dropbox to GitHub Sync

Автоматическая синхронизация папки `/Nov25` из Dropbox в GitHub репозиторий с детальным changelog.

## Описание

Этот проект автоматически синхронизирует содержимое папки `/Nov25` из Dropbox в GitHub репозиторий каждые 2 часа. При каждом запуске:

- Скачивает все файлы из Dropbox `/Nov25` (исключая `.automation`)
- Сравнивает с текущим состоянием в git
- Определяет изменения (добавлено/изменено/удалено)
- Генерирует детальный changelog с группировкой по отделам и сотрудникам
- Автоматически коммитит и пушит изменения

## Структура

```
.sync-automation/
├── .github/
│   └── workflows/
│       └── sync-dropbox.yml    # GitHub Actions workflow
├── scripts/
│   └── sync_dropbox_to_github.py  # Основной скрипт синхронизации
├── requirements.txt            # Python зависимости
├── .gitignore                  # Git ignore правила
└── README.md                   # Этот файл
```

## Настройка

### 1. Создать GitHub репозиторий

Создайте приватный репозиторий `Nov25-Dropbox-Sync` на GitHub.

### 2. Добавить Dropbox токен

В настройках репозитория добавьте секрет:
- **Name**: `DROPBOX_ACCESS_TOKEN`
- **Value**: Ваш Dropbox access token

### 3. Запушить код

```bash
cd .sync-automation
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/YOUR_USERNAME/Nov25-Dropbox-Sync.git
git push -u origin main
```

## Расписание

Workflow запускается автоматически **каждые 2 часа** (cron: `0 */2 * * *`).

Также можно запустить вручную через GitHub Actions UI.

## Changelog

После каждой синхронизации создается/обновляется файл `CHANGELOG.md` с детальной информацией:

- Группировка по отделам (Design, AI, Video, LG, Dev)
- Группировка по сотрудникам
- Типы изменений (добавлено/изменено/удалено)
- Метаданные файлов (размер, дата изменения, ревизия)

## Исключения

По умолчанию исключается папка `.automation` из синхронизации.

## Локальный запуск

Для тестирования локально:

```bash
export DROPBOX_ACCESS_TOKEN="your_token_here"
python scripts/sync_dropbox_to_github.py --path /Nov25 --exclude .automation
```

## Требования

- Python 3.11+
- Dropbox SDK (`pip install dropbox`)
- Git
- Dropbox access token с правами на чтение файлов

