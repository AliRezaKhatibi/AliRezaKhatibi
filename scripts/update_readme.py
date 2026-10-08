#!/usr/bin/env python3
"""Refresh the recent-repositories and complete-catalog sections of the GitHub profile.

Standard library only. Uses public GitHub REST endpoints with GITHUB_TOKEN where available.
No user-generated README content outside section markers is changed.
"""

from __future__ import annotations

import json
import os
import re
import sys
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen

OWNER = os.environ.get("PROFILE_OWNER", "AliRezaKhatibi")
README = Path(os.environ.get("PROFILE_README_PATH", "README.markdown"))
API_BASE = os.environ.get("GITHUB_API_BASE", "https://api.github.com").rstrip("/")
RECENT_LIMIT = 5
TIMEOUT = 25


def get_json(url: str):
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "profile-readme-refresh/1.0",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    request = Request(url, headers=headers)
    with urlopen(request, timeout=TIMEOUT) as response:
        return json.load(response)


def list_public_repositories():
    """Paginate rather than assuming an account has fewer than 100 repositories."""
    output = []
    page = 1
    while True:
        url = f"{API_BASE}/users/{quote(OWNER, safe='')}/repos?type=public&per_page=100&page={page}"
        batch = get_json(url)
        if not isinstance(batch, list):
            raise ValueError("Unexpected GitHub API response for repositories")
        output.extend(repo for repo in batch if not repo.get("private", False))
        if len(batch) < 100:
            break
        page += 1
        if page > 100:
            raise ValueError("Repository pagination exceeded safety limit")
    output.sort(key=lambda repo: (repo.get("pushed_at") or "", repo["name"].lower()), reverse=True)
    return output


def sanitize(value, default="—") -> str:
    text = " ".join(str(value or "").split())
    text = re.sub(r"<[^>]*>", "", text)
    text = text.replace("|", r"\|").replace("[", r"\[").replace("]", r"\]")
    return text or default


def date_only(raw: str | None) -> str:
    return raw[:10] if raw else "—"


def render_recent(repos) -> str:
    repos = [repo for repo in repos if repo["name"].casefold() != OWNER.casefold()]
    lines = ["_Based on the latest public repository push timestamps; updated automatically._", ""]
    for repo in repos[:RECENT_LIMIT]:
        link = repo.get("html_url") or f"https://github.com/{OWNER}/{quote(repo['name'])}"
        description = sanitize(repo.get("description"), "Public repository")
        lines.append(f"- **[{sanitize(repo['name'])}]({link})** · `{date_only(repo.get('pushed_at'))}` · {description}")
    if not repos:
        lines.append(f"[Explore all public repositories](https://github.com/{OWNER}?tab=repositories)")
    return "\n".join(lines)


def render_directory(repos) -> str:
    latest_push = date_only(max((repo.get("pushed_at") or "") for repo in repos))
    lines = [
        "<details>",
        f"<summary><b>View all {len(repos)} public repositories</b> (including forks and archived projects)</summary>",
        "",
        f"<sub>Latest repository push: {latest_push} · Ordered by last push · Public repositories only</sub>",
        "",
        "| Repository | Language | Description | Last push |",
        "|:--|:--|:--|:--|",
    ]
    for repo in repos:
        link = repo.get("html_url") or f"https://github.com/{OWNER}/{quote(repo['name'])}"
        flags = []
        if repo.get("fork"):
            flags.append("fork")
        if repo.get("archived"):
            flags.append("archived")
        label = sanitize(repo["name"])
        if flags:
            label += " (" + ", ".join(flags) + ")"
        lines.append(
            f"| [{label}]({link}) | {sanitize(repo.get('language'))} | "
            f"{sanitize(repo.get('description'), 'No description yet')} | "
            f"{date_only(repo.get('pushed_at'))} |"
        )
    lines.extend(["", f"[Open full GitHub directory ↗](https://github.com/{OWNER}?tab=repositories)", "</details>"])
    return "\n".join(lines)


def replace_section(content: str, name: str, replacement: str) -> str:
    begin = f"<!-- {name}:START -->"
    end = f"<!-- {name}:END -->"
    if content.count(begin) != 1 or content.count(end) != 1:
        raise ValueError(f"Expected exactly one {name} marker pair in {README}")
    before, tail = content.split(begin, 1)
    _, after = tail.split(end, 1)
    return before + begin + "\n" + replacement.rstrip() + "\n" + end + after


def main():
    if not README.is_file():
        raise FileNotFoundError(f"README not found: {README}")
    repos = list_public_repositories()  # Fail without touching README on API errors.
    if not repos:
        raise ValueError("No public repositories returned; refusing to erase existing directory")
    original = README.read_text(encoding="utf-8")
    updated = replace_section(original, "RECENT_REPOS", render_recent(repos))
    updated = replace_section(updated, "ALL_REPOS", render_directory(repos))
    if updated != original:
        README.write_text(updated, encoding="utf-8")
        print(f"Updated {README}: {len(repos)} public repositories")
    else:
        print(f"No changes: {len(repos)} public repositories")


if __name__ == "__main__":
    try:
        main()
    except (HTTPError, URLError, OSError, ValueError, KeyError) as exc:
        print(f"Profile update failed safely: {exc}", file=sys.stderr)
        sys.exit(1)
