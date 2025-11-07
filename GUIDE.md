# Dropbox to GitHub Sync - Complete Guide

Автоматическая синхронизация папки `/Nov25` из Dropbox в GitHub репозиторий с детальным changelog.

---

## Table of Contents

1. [Overview](#overview)
2. [Architecture](#architecture)
3. [Initial Setup](#initial-setup)
4. [How It Works](#how-it-works)
5. [Changelog Format](#changelog-format)
6. [Configuration](#configuration)
7. [Monitoring](#monitoring)
8. [Troubleshooting](#troubleshooting)

---

## Overview

**Source**: `/Nov25` folder in Dropbox  
**Target**: GitHub repository `Nov25-Dropbox-Sync`  
**Schedule**: Every 2 hours  
**Excludes**: `.automation` folder

### Features

- ✅ **Automatic Sync** - Runs every 2 hours via GitHub Actions
- ✅ **Detailed Changelog** - Grouped by department and employee
- ✅ **Change Detection** - Tracks added/modified/deleted files
- ✅ **Metadata Tracking** - File size, modification date, author, revision
- ✅ **Free** - Uses GitHub Actions free tier
- ✅ **Reliable** - Cloud-based, no laptop dependency

### Status

**Current System**: GitHub Actions cloud automation  
**Status**: ✅ Active - Running every 2 hours  
**Repository**: https://github.com/AdminRHS/Nov25-Dropbox-Sync

---

## Architecture

```
GitHub Actions (Cloud)
    ↓
    Runs every 2 hours (cron: 0 */2 * * *)
    ↓
Python Script (sync_dropbox_to_github.py)
    ↓
Dropbox API
    ↓
Downloads all files from /Nov25
    ↓
Compares with git state
    ↓
Detects changes (added/modified/deleted)
    ↓
Generates detailed changelog
    ↓
Commits and pushes to GitHub
```

---

## Initial Setup

### Prerequisites

- GitHub account (free)
- Dropbox account with Developer access
- Dropbox access token (same as Employee Profile Sync)

### Step 1: Create GitHub Repository

1. Go to: https://github.com/new
2. Configure:
   - **Repository name**: `Nov25-Dropbox-Sync`
   - **Description**: "Automated sync of Nov25 Dropbox folder to GitHub"
   - **Visibility**: **Private**
   - **Initialize**: Don't check any boxes
3. Click **"Create repository"**

### Step 2: Add Dropbox Token to GitHub Secrets

**IMPORTANT**: If you see "expired_access_token" error, you need to regenerate the token!

1. **Get Dropbox Access Token**:
   - Go to: https://www.dropbox.com/developers/apps
   - Click on your app (the one you created for Employee Profile Sync)
   - Go to **"Settings"** tab → **"OAuth 2"** section
   - Click **"Generate"** button to create a new access token
   - **Copy the token immediately** (it starts with `sl.u.` and is very long)

2. **Add Token to GitHub Secrets**:
   - Go to: https://github.com/AdminRHS/Nov25-Dropbox-Sync/settings/secrets/actions
   - If `DROPBOX_ACCESS_TOKEN` already exists, click on it and **"Update"**
   - If it doesn't exist, click **"New repository secret"**
   - Configure:
     - **Name**: `DROPBOX_ACCESS_TOKEN` (must match exactly, case-sensitive)
     - **Value**: Paste your NEW Dropbox access token
     - Click **"Add secret"** or **"Update secret"**

**Note**: Dropbox access tokens can expire. If sync fails with "expired_access_token", regenerate the token and update it in GitHub Secrets.

### Step 3: Push Code to GitHub

```bash
cd "/Users/nikolay/Library/CloudStorage/Dropbox/automations/dropbox-sync"

# Add remote (if not already added)
git remote add origin https://github.com/AdminRHS/Nov25-Dropbox-Sync.git

# Push code
git push -u origin main
```

**Note**: Use GitHub Personal Access Token when prompted for password.

### Step 4: Test Workflow

1. Go to: https://github.com/AdminRHS/Nov25-Dropbox-Sync/actions
2. Click **"Run workflow"** → **"Run workflow"**
3. Monitor execution and verify success

---

## How It Works

### Sync Process

1. **Trigger**: GitHub Actions runs every 2 hours (or manually)
2. **Connect**: Script connects to Dropbox using access token
3. **List Files**: Scans `/Nov25` folder recursively via Dropbox API
4. **Exclude**: Skips `.automation` folder
5. **Compare**: Compares Dropbox file list with git tracked files
6. **Detect Changes**:
   - **Added**: Files in Dropbox but not in git
   - **Modified**: Files in both but content hash differs
   - **Deleted**: Files in git but not in Dropbox
7. **Download**: Downloads changed files from Dropbox
8. **Organize**: Groups changes by department and employee
9. **Generate Changelog**: Creates detailed changelog with metadata
10. **Commit**: Stages all changes and commits
11. **Push**: Pushes to GitHub repository

### File Structure in Repository

Files are stored with paths relative to `/Nov25`:
- Dropbox: `/Nov25/Design/Yarmachenko Kristina/daily.md`
- GitHub: `Design/Yarmachenko Kristina/daily.md`

---

## Changelog Format

### Structure

Changelog is organized hierarchically:

```
# Changelog - YYYY-MM-DD

## Summary
- Added: X files
- Modified: Y files
- Deleted: Z files

## Changes by Department

### [Department Name]
**Total changes:** N files

#### [Employee Name]
**Added (X files):**
- `filename.md` → `subfolder/filename.md` (size, modified: date, by: author)
**Modified (Y files):**
- `filename.md` → `subfolder/filename.md` (size, rev: abc12345..., modified: date, by: author)
**Deleted (Z files):**
- `filename.md`

## All Changes
[List of all changed files]
```

### Example

```markdown
# Changelog - 2025-11-07

**Sync Date:** 2025-11-07 15:30:00 UTC
**Total Changes:** 8 files

## Summary

- **Added:** 2 files
- **Modified:** 5 files
- **Deleted:** 1 files

## Changes by Department

### Design
**Total changes:** 6 files

#### Yarmachenko Kristina
**Modified (3 files):**
- `daily.md` → `07/daily.md` (2.5 KB, rev: abc12345..., modified: 2025-11-07T10:30:00, by: Dropbox User)
- `plans.md` → `07/plans.md` (1.2 KB, rev: def67890..., modified: 2025-11-07T11:15:00, by: Dropbox User)
- `task.md` → `07/task.md` (0.8 KB, rev: ghi11111..., modified: 2025-11-07T12:00:00, by: Dropbox User)

#### Bogun Polina
**Added (1 file):**
- `Profile UI UX designer Bogun Polina.md` (3.2 KB, modified: 2025-11-07T14:20:00, by: Dropbox User)

**Modified (1 file):**
- `README.md` (1.5 KB, rev: jkl22222..., modified: 2025-11-07T13:45:00, by: Dropbox User)

### AI
**Total changes:** 2 files

#### Artemchuk Nikolay
**Modified (1 file):**
- `Profile Project manager, Lead generator Artemchuk Nikolay.md` (2.1 KB, rev: mno33333..., modified: 2025-11-07T09:15:00, by: Dropbox User)

**Deleted (1 file):**
- `old_file.md`
```

### Metadata Fields

Each file entry includes:
- **File name**: Original filename
- **Relative path**: Path within employee folder (if different)
- **Size**: File size in bytes or KB
- **Revision**: Dropbox file revision (first 8 chars)
- **Modified**: Last modification date/time
- **Author**: Who made the change (if available)

---

## Configuration

### Change Schedule

Edit `.github/workflows/sync-dropbox.yml`:

```yaml
schedule:
  - cron: '0 */2 * * *'  # Every 2 hours
```

Common schedules:
- `'0 */1 * * *'` - Every hour
- `'0 */6 * * *'` - Every 6 hours
- `'0 8,20 * * *'` - Twice daily (8 AM and 8 PM UTC)
- `'0 8 * * 1-5'` - Weekdays at 8 AM UTC

Use [crontab.guru](https://crontab.guru) to create custom schedules.

### Change Exclusions

Edit workflow file or script:

```yaml
run: |
  python scripts/sync_dropbox_to_github.py --path /Nov25 --exclude .automation folder2
```

### Change Source Path

To sync different folder:

```yaml
run: |
  python scripts/sync_dropbox_to_github.py --path /OtherFolder --exclude .automation
```

---

## Monitoring

### GitHub Actions Dashboard

- **Location**: Repository → Actions tab
- **Shows**: All workflow runs, success/failure, execution time
- **Logs**: Detailed logs for each step
- **Artifacts**: Download CHANGELOG.md after each run

### Changelog File

- **Location**: `CHANGELOG.md` in repository root
- **Updated**: After each successful sync
- **Format**: Markdown with detailed change information
- **History**: All changelogs are preserved (prepended)

### Key Metrics

Each sync reports:
- **Files Found**: Total files in Dropbox
- **Files Added**: New files detected
- **Files Modified**: Changed files detected
- **Files Deleted**: Removed files detected
- **Sync Time**: Duration of sync operation

---

## Troubleshooting

### Workflow Doesn't Run on Schedule

**Possible Causes**:
- GitHub Actions can have up to 10-minute delay
- Cron syntax might be incorrect
- Actions might be disabled

**Solution**:
1. Verify cron syntax: `'0 */2 * * *'` (use [crontab.guru](https://crontab.guru))
2. Check Actions are enabled: Settings → Actions → General
3. Wait up to 10 minutes after scheduled time

### "Invalid Dropbox access token" Error

**Solution**:
1. Verify token in GitHub Secrets
2. Check token hasn't expired
3. Regenerate token if needed
4. Update secret in GitHub

### "File not found" Error

**Solution**:
1. Verify Dropbox path: `/Nov25`
2. Check Dropbox app has Full Dropbox access
3. Verify folder exists in your Dropbox

### No Changes Detected

**Possible Causes**:
- No actual changes in Dropbox
- Files excluded by filter
- Git state matches Dropbox state

**Solution**:
1. Check Dropbox files were actually modified
2. Verify exclusion filters aren't too broad
3. Review workflow logs for details

### Changelog Not Generated

**Solution**:
1. Check if sync detected changes (no changes = no changelog)
2. Verify script completed successfully
3. Check GitHub Actions logs for errors
4. Download artifacts to see CHANGELOG.md

### Large Sync Times

**Possible Causes**:
- Many files to sync
- Large file sizes
- Network latency

**Solution**:
1. Normal for first sync (all files)
2. Subsequent syncs should be faster (only changes)
3. Consider increasing schedule interval if needed

---

## Local Testing

Test the script locally before deploying:

```bash
# Install dependencies
pip install -r requirements.txt

# Set Dropbox token
export DROPBOX_ACCESS_TOKEN="your_token_here"

# Run sync
cd "/Users/nikolay/Library/CloudStorage/Dropbox/automations/dropbox-sync"
python scripts/sync_dropbox_to_github.py --path /Nov25 --exclude .automation
```

---

## File Structure

```
dropbox-sync/
├── .github/
│   └── workflows/
│       └── sync-dropbox.yml          # GitHub Actions workflow
├── scripts/
│   └── sync_dropbox_to_github.py     # Main sync script
├── .gitignore
├── GUIDE.md                          # This file (complete guide)
├── requirements.txt
└── CHANGELOG.md                      # Generated after each sync
```

---

## Security

### Token Security

- ✅ Token stored in GitHub Secrets (encrypted)
- ✅ Never committed to repository
- ✅ Only accessible during workflow execution

### Repository Security

- ✅ Private repository recommended
- ✅ No sensitive data in code
- ✅ All paths use environment variables

### Dropbox Security

- ✅ Scoped access (only required permissions)
- ✅ Monitor app activity in Dropbox dashboard

---

## Cost Analysis

### GitHub Actions

- **Free Tier**: 2,000 minutes/month for private repos
- **Usage**: ~5 minutes per run × 360 runs/month = ~1,800 minutes
- **Percentage**: 90% of free tier
- **Cost**: $0 (within free limits)

**Note**: If usage exceeds free tier, consider:
- Increasing schedule interval (every 3-4 hours instead of 2)
- Optimizing script performance
- Using GitHub Actions minutes more efficiently

### Dropbox API

- **Free Tier**: Unlimited API calls for basic tier
- **Storage**: Files synced to GitHub (no additional Dropbox storage)
- **Cost**: $0

---

## Manual Trigger

You can manually trigger the workflow anytime:

1. Go to: https://github.com/AdminRHS/Nov25-Dropbox-Sync/actions
2. Click **"Run workflow"** → **"Run workflow"**

This is useful for:
- Testing after setup
- Running sync outside scheduled time
- Debugging issues

---

## Support

For issues or questions:
1. Review troubleshooting section above
2. Check GitHub Actions logs
3. Test locally with script
4. Verify Dropbox token and permissions

---

**Last Updated**: November 2025  
**Status**: ✅ Active - Running every 2 hours  
**Version**: 1.0

