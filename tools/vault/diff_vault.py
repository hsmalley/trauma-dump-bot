#!/usr/bin/env python3
"""
diff_vault.py

Append YAML diff between the working and last committed vault to a changelog.
"""

import difflib
import subprocess
from datetime import datetime
from pathlib import Path


def get_git_previous(path: str) -> str:
    """Return the last committed version of a file (or empty if none)."""
    try:
        return subprocess.check_output(["git", "show", f"HEAD:{path}"], text=True)
    except subprocess.CalledProcessError:
        return ""


def get_current(path: str) -> str:
    """Read the current contents of a file."""
    return Path(path).read_text(encoding="utf-8")


def diff_and_append(current_path: str, changelog_path: str = "vault-changelog.md"):
    """Generate a unified diff and append to changelog if content changed."""
    old = get_git_previous(current_path)
    new = get_current(current_path)

    if old.strip() == new.strip():
        print("⏭️ No changes detected. Skipping changelog update.")
        return

    diff = difflib.unified_diff(
        old.splitlines(keepends=True),
        new.splitlines(keepends=True),
        fromfile=f"{current_path} (old)",
        tofile=f"{current_path} (new)",
        lineterm="",
    )

    timestamp = datetime.now().isoformat(timespec="seconds")
    header = f"\n\n## Vault Update – {timestamp}\n\n"
    full_diff = header + "".join(diff)

    changelog = Path(changelog_path)
    existing = ""
    if changelog.exists():
        existing = changelog.read_text(encoding="utf-8")
    changelog.write_text(existing + full_diff, encoding="utf-8")
    print(f"📝 Changelog updated: {changelog_path}")


if __name__ == "__main__":
    diff_and_append("vault.yaml")
