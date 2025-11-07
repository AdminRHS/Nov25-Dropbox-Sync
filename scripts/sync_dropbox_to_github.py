#!/usr/bin/env python3
"""
Dropbox to GitHub Sync Script

Синхронизирует папку /Nov25 из Dropbox в GitHub репозиторий.
Исключает папку .automation.
Генерирует детальный changelog с группировкой по отделам и сотрудникам.
"""

import os
import sys
import json
import hashlib
import subprocess
import requests
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Set, Optional, Tuple
from collections import defaultdict

try:
    import dropbox
    from dropbox.exceptions import ApiError, AuthError
except ImportError:
    print("ERROR: Dropbox SDK not installed. Run: pip install dropbox")
    sys.exit(1)


class DropboxToGitHubSync:
    def __init__(self, dropbox_token: str, dropbox_path: str = "/Nov25", exclude_paths: List[str] = None, 
                 app_key: Optional[str] = None, app_secret: Optional[str] = None, refresh_token: Optional[str] = None):
        self.dropbox_path = dropbox_path
        self.exclude_paths = exclude_paths or [".automation"]
        self.app_key = app_key
        self.app_secret = app_secret
        self.refresh_token = refresh_token
        self.changes = {
            "added": [],
            "modified": [],
            "deleted": [],
            "moved": []
        }
        self.file_hashes = {}
        self.file_metadata = {}
        
        # Initialize Dropbox client with token refresh support
        self.dbx = self._init_dropbox_client(dropbox_token)
    
    def _init_dropbox_client(self, access_token: str) -> dropbox.Dropbox:
        """Initialize Dropbox client with automatic token refresh if refresh token is available"""
        try:
            return dropbox.Dropbox(access_token)
        except Exception as e:
            # If token is expired and we have refresh token, try to refresh
            if self.refresh_token and self.app_key and self.app_secret:
                self.log(f"Access token expired, attempting to refresh...", "WARN")
                new_token = self._refresh_access_token()
                if new_token:
                    return dropbox.Dropbox(new_token)
            raise e
    
    def _refresh_access_token(self) -> Optional[str]:
        """Refresh access token using refresh token"""
        if not all([self.app_key, self.app_secret, self.refresh_token]):
            return None
        
        try:
            url = "https://api.dropbox.com/oauth2/token"
            data = {
                "grant_type": "refresh_token",
                "refresh_token": self.refresh_token,
            }
            auth = (self.app_key, self.app_secret)
            
            response = requests.post(url, data=data, auth=auth, timeout=30)
            response.raise_for_status()
            
            result = response.json()
            new_access_token = result.get("access_token")
            
            if new_access_token:
                self.log("Successfully refreshed access token", "INFO")
                # Note: In production, you might want to update GitHub Secret here
                # But that requires GitHub API access, so we'll just use the new token for this session
                return new_access_token
        except Exception as e:
            self.log(f"Failed to refresh token: {e}", "ERROR")
        
        return None
        
    def log(self, message: str, level: str = "INFO"):
        """Log message with timestamp"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] [{level}] {message}")
    
    def should_exclude(self, path: str) -> bool:
        """Check if path should be excluded"""
        # Exclude configured paths
        for exclude in self.exclude_paths:
            if exclude in path:
                return True
        
        # ALWAYS exclude automation files - these must never be synced from Dropbox
        automation_files = [
            '.github/',
            'scripts/',
            'requirements.txt',
            'GUIDE.md',
            '.gitignore',
            'CHANGELOG.md'
        ]
        for auto_file in automation_files:
            if path.startswith(auto_file) or path == auto_file:
                return True
        
        # Exclude paths containing .git directories (nested git repos)
        # This prevents submodule issues
        # Check if path contains /.git/ or is inside a folder with .git
        path_parts = path.split('/')
        for i, part in enumerate(path_parts):
            # Skip if this part or any parent contains .git
            if '.git' in part:
                return True
        
        # Also exclude AdminRHS-AI-Catalog-4 specifically as it contains .git
        if 'AdminRHS-AI-Catalog-4' in path:
            return True
        
        return False
    
    def get_file_hash(self, content: bytes) -> str:
        """Calculate SHA256 hash of file content"""
        return hashlib.sha256(content).hexdigest()
    
    def download_file(self, dropbox_path: str) -> Optional[Tuple[bytes, Dict]]:
        """Download file from Dropbox with metadata"""
        try:
            metadata, response = self.dbx.files_download(dropbox_path)
            content = response.content
            
            # Try to get file history for author information
            author = "Unknown"
            try:
                # Get file revisions (limited to recent)
                revisions = self.dbx.files_list_revisions(dropbox_path, limit=1)
                if revisions.entries:
                    # Note: Dropbox API doesn't provide author email in standard API
                    # This would require Dropbox Business API
                    author = "Dropbox User"
            except:
                pass
            
            return content, {
                "path": metadata.path_display,
                "name": metadata.name,
                "size": metadata.size,
                "modified": metadata.client_modified.isoformat() if metadata.client_modified else None,
                "rev": metadata.rev,
                "author": author,
            }
        except ApiError as e:
            self.log(f"Error downloading {dropbox_path}: {e}", "ERROR")
            return None
    
    def list_all_files(self) -> Dict[str, Dict]:
        """List all files in Dropbox path recursively"""
        files = {}
        
        try:
            self.log(f"Scanning Dropbox path: {self.dropbox_path}")
            result = self.dbx.files_list_folder(self.dropbox_path, recursive=True)
            page_count = 0
            excluded_count = 0
            
            while True:
                page_count += 1
                self.log(f"Processing page {page_count}... (found {len(files)} files so far)")
                
                for entry in result.entries:
                    if isinstance(entry, dropbox.files.FileMetadata):
                        path = entry.path_display
                        
                        # Skip excluded paths
                        if self.should_exclude(path):
                            excluded_count += 1
                            continue
                        
                        files[path] = {
                            "path": path,
                            "name": entry.name,
                            "size": entry.size,
                            "modified": entry.client_modified.isoformat() if entry.client_modified else None,
                            "rev": entry.rev,
                            "id": entry.id,
                        }
                
                if not result.has_more:
                    break
                
                self.log(f"Fetching next page...")
                result = self.dbx.files_list_folder_continue(result.cursor)
        
        except ApiError as e:
            self.log(f"Error listing files: {e}", "ERROR")
            raise
        
        self.log(f"Scanning complete: Found {len(files)} files, excluded {excluded_count} files")
        return files
    
    def get_git_file_status(self) -> Dict[str, str]:
        """Get current git file status"""
        status = {}
        
        try:
            # Get all tracked files
            result = subprocess.run(
                ["git", "ls-files"],
                capture_output=True,
                text=True,
                cwd=os.getcwd()
            )
            
            if result.returncode == 0:
                for line in result.stdout.strip().split('\n'):
                    if line:
                        status[line] = "tracked"
            
            # Get modified files
            result = subprocess.run(
                ["git", "diff", "--name-only"],
                capture_output=True,
                text=True,
                cwd=os.getcwd()
            )
            
            if result.returncode == 0:
                for line in result.stdout.strip().split('\n'):
                    if line:
                        status[line] = "modified"
            
            # Get deleted files
            result = subprocess.run(
                ["git", "ls-files", "--deleted"],
                capture_output=True,
                text=True,
                cwd=os.getcwd()
            )
            
            if result.returncode == 0:
                for line in result.stdout.strip().split('\n'):
                    if line:
                        status[line] = "deleted"
        
        except Exception as e:
            self.log(f"Error getting git status: {e}", "WARN")
        
        return status
    
    def save_file_locally(self, dropbox_path: str, content: bytes, local_path: str):
        """Save file to local filesystem"""
        local_file = Path(local_path)
        local_file.parent.mkdir(parents=True, exist_ok=True)
        
        with open(local_file, 'wb') as f:
            f.write(content)
    
    def detect_changes(self, dropbox_files: Dict[str, Dict], git_files: Set[str]) -> Dict:
        """Detect changes between Dropbox and git"""
        changes = {
            "added": [],
            "modified": [],
            "deleted": [],
            "moved": []
        }
        
        # Normalize paths (remove leading slash and 'Nov25/' prefix for git)
        dropbox_paths = {}
        for path, info in dropbox_files.items():
            # Remove leading slash
            normalized = path.lstrip('/')
            # Remove 'Nov25/' prefix if present
            if normalized.startswith('Nov25/'):
                normalized = normalized[6:]
            dropbox_paths[normalized] = info
        
        git_paths = {path for path in git_files if not self.should_exclude(path)}
        
        # Find added files (in Dropbox but not in git)
        for path, info in dropbox_paths.items():
            if path not in git_paths:
                changes["added"].append({
                    "path": path,
                    "dropbox_path": f"/Nov25/{path}",
                    "name": info["name"],
                    "size": info["size"],
                    "modified": info["modified"],
                    "author": "Unknown",  # Will be updated when downloading
                })
        
        # Find deleted files (in git but not in Dropbox)
        for path in git_paths:
            if path not in dropbox_paths:
                changes["deleted"].append({
                    "path": path,
                })
        
        # Find modified files (in both, but content changed)
        for path, info in dropbox_paths.items():
            if path in git_paths:
                local_file = Path(path)
                if local_file.exists():
                    # Download file to compare
                    dropbox_content, metadata = self.download_file(f"/Nov25/{path}")
                    if dropbox_content:
                        file_hash = self.get_file_hash(dropbox_content)
                        local_hash = self.get_file_hash(local_file.read_bytes())
                        
                        if file_hash != local_hash:
                            # Download again to get author info
                            dropbox_content_full, metadata_full = self.download_file(f"/Nov25/{path}")
                            author = metadata_full.get("author", "Unknown") if metadata_full else "Unknown"
                            
                            changes["modified"].append({
                                "path": path,
                                "dropbox_path": f"/Nov25/{path}",
                                "name": info["name"],
                                "size": info["size"],
                                "modified": info["modified"],
                                "rev": info["rev"],
                                "author": author,
                            })
        
        return changes
    
    def sync_files(self, changes: Dict):
        """Sync files from Dropbox to local filesystem"""
        all_changes = changes["added"] + changes["modified"]
        total = len(all_changes)
        
        for idx, file_info in enumerate(all_changes, 1):
            dropbox_path = file_info["dropbox_path"]
            local_path = file_info["path"]
            
            # Log progress every 50 files or for every file if less than 50
            if total <= 50 or idx % 50 == 0 or idx == 1:
                self.log(f"Syncing [{idx}/{total}]: {local_path}")
            
            result = self.download_file(dropbox_path)
            if result:
                content, metadata = result
                # Update author info in file_info
                file_info["author"] = metadata.get("author", "Unknown")
                self.save_file_locally(dropbox_path, content, local_path)
                self.file_hashes[local_path] = self.get_file_hash(content)
                self.file_metadata[local_path] = metadata
        
        self.log(f"Sync complete: {total} files synced")
    
    def organize_changes_by_department(self, changes: Dict) -> Dict:
        """Organize changes by department and employee"""
        organized = defaultdict(lambda: {
            "department": "",
            "employees": defaultdict(lambda: {
                "name": "",
                "files": {
                    "added": [],
                    "modified": [],
                    "deleted": []
                }
            })
        })
        
        for change_type in ["added", "modified", "deleted"]:
            for file_info in changes[change_type]:
                path = file_info["path"]
                # Remove 'Nov25/' prefix if present
                if path.startswith("Nov25/"):
                    path = path[6:]  # Remove "Nov25/"
                
                parts = path.split('/')
                
                if len(parts) >= 2:
                    department = parts[0]  # e.g., "Design", "AI", "Video"
                    employee = parts[1] if len(parts) > 1 else "Unknown"
                    filename = parts[-1] if parts else path
                    
                    # Get full path relative to employee folder
                    relative_path = '/'.join(parts[2:]) if len(parts) > 2 else filename
                    
                    dept_key = department
                    organized[dept_key]["department"] = department
                    organized[dept_key]["employees"][employee]["name"] = employee
                    organized[dept_key]["employees"][employee]["files"][change_type].append({
                        "file": filename,
                        "path": path,
                        "relative_path": relative_path,
                        "author": file_info.get("author", "Unknown"),
                        **{k: v for k, v in file_info.items() if k not in ["path", "author"]}
                    })
        
        return dict(organized)
    
    def generate_changelog(self, changes: Dict, organized: Dict) -> str:
        """Generate detailed changelog"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S UTC")
        date = datetime.now().strftime("%Y-%m-%d")
        
        changelog = f"""# Changelog - {date}

**Sync Date:** {timestamp}
**Total Changes:** {len(changes['added']) + len(changes['modified']) + len(changes['deleted'])} files

"""
        
        # Summary
        changelog += "## Summary\n\n"
        changelog += f"- **Added:** {len(changes['added'])} files\n"
        changelog += f"- **Modified:** {len(changes['modified'])} files\n"
        changelog += f"- **Deleted:** {len(changes['deleted'])} files\n\n"
        
        # Detailed changes by department
        changelog += "## Changes by Department\n\n"
        
        for dept_key, dept_info in sorted(organized.items()):
            department = dept_info["department"]
            employees = dept_info["employees"]
            
            total_dept_changes = sum(
                len(emp["files"]["added"]) + len(emp["files"]["modified"]) + len(emp["files"]["deleted"])
                for emp in employees.values()
            )
            
            if total_dept_changes == 0:
                continue
            
            changelog += f"### {department}\n\n"
            changelog += f"**Total changes:** {total_dept_changes} files\n\n"
            
            for emp_name, emp_info in sorted(employees.items()):
                emp_changes = (
                    len(emp_info["files"]["added"]) +
                    len(emp_info["files"]["modified"]) +
                    len(emp_info["files"]["deleted"])
                )
                
                if emp_changes == 0:
                    continue
                
                changelog += f"#### {emp_name}\n\n"
                
                # Added files
                if emp_info["files"]["added"]:
                    changelog += f"**Added ({len(emp_info['files']['added'])} files):**\n"
                    for file_info in emp_info["files"]["added"]:
                        file_path = file_info.get("file", file_info["path"])
                        relative_path = file_info.get("relative_path", file_path)
                        size = file_info.get("size", 0)
                        modified = file_info.get("modified", "Unknown")
                        author = file_info.get("author", "Unknown")
                        # Format size
                        size_str = f"{size:,} bytes" if size < 1024 else f"{size/1024:.2f} KB"
                        changelog += f"- `{file_path}`"
                        if relative_path != file_path:
                            changelog += f" → `{relative_path}`"
                        changelog += f" ({size_str}, modified: {modified}, by: {author})\n"
                    changelog += "\n"
                
                # Modified files
                if emp_info["files"]["modified"]:
                    changelog += f"**Modified ({len(emp_info['files']['modified'])} files):**\n"
                    for file_info in emp_info["files"]["modified"]:
                        file_path = file_info.get("file", file_info["path"])
                        relative_path = file_info.get("relative_path", file_path)
                        size = file_info.get("size", 0)
                        modified = file_info.get("modified", "Unknown")
                        rev = file_info.get("rev", "")
                        author = file_info.get("author", "Unknown")
                        # Format size
                        size_str = f"{size:,} bytes" if size < 1024 else f"{size/1024:.2f} KB"
                        changelog += f"- `{file_path}`"
                        if relative_path != file_path:
                            changelog += f" → `{relative_path}`"
                        changelog += f" ({size_str}, rev: {rev[:8]}..., modified: {modified}, by: {author})\n"
                    changelog += "\n"
                
                # Deleted files
                if emp_info["files"]["deleted"]:
                    changelog += f"**Deleted ({len(emp_info['files']['deleted'])} files):**\n"
                    for file_info in emp_info["files"]["deleted"]:
                        file_path = file_info.get("file", file_info["path"])
                        changelog += f"- `{file_path}`\n"
                    changelog += "\n"
            
            changelog += "\n"
        
        # All changes list (for reference)
        changelog += "## All Changes\n\n"
        
        if changes["added"]:
            changelog += "### Added Files\n\n"
            for file_info in changes["added"]:
                changelog += f"- `{file_info['path']}`\n"
            changelog += "\n"
        
        if changes["modified"]:
            changelog += "### Modified Files\n\n"
            for file_info in changes["modified"]:
                changelog += f"- `{file_info['path']}`\n"
            changelog += "\n"
        
        if changes["deleted"]:
            changelog += "### Deleted Files\n\n"
            for file_info in changes["deleted"]:
                changelog += f"- `{file_info['path']}`\n"
            changelog += "\n"
        
        changelog += f"\n---\n*Generated automatically by Dropbox to GitHub sync*\n"
        
        return changelog
    
    def run_sync(self):
        """Main sync process"""
        self.log("=" * 80)
        self.log("Dropbox to GitHub Sync - Starting")
        self.log("=" * 80)
        
        try:
            # Verify Dropbox connection
            try:
                account = self.dbx.users_get_current_account()
                self.log(f"Connected to Dropbox account: {account.email}")
            except AuthError as e:
                if 'expired_access_token' in str(e):
                    raise Exception("❌ Dropbox access token has EXPIRED. Please update DROPBOX_ACCESS_TOKEN in GitHub Secrets with a new token from Dropbox App Console.")
                else:
                    raise Exception(f"Invalid Dropbox access token: {e}")
            
            # List all files in Dropbox
            self.log("Step 1/5: Listing files from Dropbox...")
            dropbox_files = self.list_all_files()
            
            # Get current git file status
            self.log("Step 2/5: Getting git file status...")
            git_status = self.get_git_file_status()
            git_files = set(git_status.keys())
            self.log(f"Found {len(git_files)} files currently in git")
            
            # Detect changes
            self.log("Step 3/5: Detecting changes...")
            changes = self.detect_changes(dropbox_files, git_files)
            
            total_changes = len(changes["added"]) + len(changes["modified"]) + len(changes["deleted"])
            
            if total_changes == 0:
                self.log("No changes detected. Sync complete.")
                return
            
            self.log(f"Detected {total_changes} changes:")
            self.log(f"  - Added: {len(changes['added'])}")
            self.log(f"  - Modified: {len(changes['modified'])}")
            self.log(f"  - Deleted: {len(changes['deleted'])}")
            
            # Sync files
            self.log("Step 4/5: Syncing files from Dropbox...")
            total_to_sync = len(changes["added"]) + len(changes["modified"])
            self.log(f"Will sync {total_to_sync} files ({len(changes['added'])} added, {len(changes['modified'])} modified)")
            self.sync_files(changes)
            
            # Remove deleted files
            for file_info in changes["deleted"]:
                local_file = Path(file_info["path"])
                if local_file.exists():
                    local_file.unlink()
                    self.log(f"Deleted: {file_info['path']}")
            
            # Organize changes by department
            organized = self.organize_changes_by_department(changes)
            
            # Generate changelog
            self.log("Generating changelog...")
            changelog = self.generate_changelog(changes, organized)
            
            # Save changelog
            changelog_file = Path("CHANGELOG.md")
            if changelog_file.exists():
                # Prepend new changelog to existing
                existing = changelog_file.read_text(encoding='utf-8')
                changelog_file.write_text(changelog + "\n\n" + existing, encoding='utf-8')
            else:
                changelog_file.write_text(changelog, encoding='utf-8')
            
            self.log(f"Changelog saved to CHANGELOG.md")
            
            # Stage all changes
            self.log("Staging changes...")
            subprocess.run(["git", "add", "-A"], check=True, cwd=os.getcwd())
            
            # Remove any nested .git directories from staging to prevent submodule issues
            self.log("Cleaning up nested git repositories...")
            try:
                result = subprocess.run(
                    ["git", "ls-files", "--cached"],
                    capture_output=True,
                    text=True,
                    cwd=os.getcwd()
                )
                if result.returncode == 0:
                    for line in result.stdout.strip().split('\n'):
                        if line:
                            # Remove files inside .git directories
                            if '/.git/' in line:
                                subprocess.run(["git", "rm", "--cached", "--ignore-unmatch", line], cwd=os.getcwd())
                                self.log(f"Removed nested .git file from staging: {line}")
                            # Remove files in AdminRHS-AI-Catalog-4 (contains .git)
                            if 'AdminRHS-AI-Catalog-4' in line:
                                subprocess.run(["git", "rm", "--cached", "--ignore-unmatch", line], cwd=os.getcwd())
                                self.log(f"Removed AdminRHS-AI-Catalog-4 file from staging: {line}")
            except Exception as e:
                self.log(f"Warning: Could not clean nested git repos: {e}", "WARN")
            
            self.log("=" * 80)
            self.log("Sync Complete")
            self.log("=" * 80)
            
            return changes
        
        except Exception as e:
            self.log(f"Fatal error: {e}", "ERROR")
            raise


def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="Sync Dropbox folder to GitHub")
    parser.add_argument("--token", help="Dropbox access token (or set DROPBOX_ACCESS_TOKEN env var)")
    parser.add_argument("--path", default="/Nov25", help="Dropbox path to sync")
    parser.add_argument("--exclude", nargs="*", default=[".automation"], help="Paths to exclude")
    parser.add_argument("--app-key", help="Dropbox app key (for token refresh, or set DROPBOX_APP_KEY env var)")
    parser.add_argument("--app-secret", help="Dropbox app secret (for token refresh, or set DROPBOX_APP_SECRET env var)")
    parser.add_argument("--refresh-token", help="Dropbox refresh token (for auto-refresh, or set DROPBOX_REFRESH_TOKEN env var)")
    
    args = parser.parse_args()
    
    # Get access token
    access_token = args.token or os.environ.get('DROPBOX_ACCESS_TOKEN')
    
    if not access_token:
        print("ERROR: Dropbox access token required!")
        print("Set DROPBOX_ACCESS_TOKEN environment variable or use --token argument")
        sys.exit(1)
    
    # Get refresh token credentials (optional, but recommended for long-term tokens)
    app_key = args.app_key or os.environ.get('DROPBOX_APP_KEY')
    app_secret = args.app_secret or os.environ.get('DROPBOX_APP_SECRET')
    refresh_token = args.refresh_token or os.environ.get('DROPBOX_REFRESH_TOKEN')
    
    syncer = DropboxToGitHubSync(
        access_token, 
        args.path, 
        args.exclude,
        app_key=app_key,
        app_secret=app_secret,
        refresh_token=refresh_token
    )
    changes = syncer.run_sync()
    
    if changes:
        total = len(changes["added"]) + len(changes["modified"]) + len(changes["deleted"])
        print(f"\n✅ Sync completed with {total} changes")
        print("Ready to commit and push to GitHub")
    else:
        print("\n✅ No changes detected")


if __name__ == "__main__":
    main()

