#!/usr/bin/env python3
import json
import re
import sys
from datetime import date, datetime
from pathlib import Path
from typing import Dict, Set, Tuple

try:
    import yaml  # type: ignore
except Exception:  # pragma: no cover - optional dependency
    yaml = None


def default_converter(o):
    if isinstance(o, (datetime, date)):
        return o.isoformat()
    raise TypeError(f"Object of type {o.__class__.__name__} is not JSON serializable")


def read_text(p):
    return Path(p).read_text(encoding="utf-8", errors="ignore")


FRONT_MATTER_PATTERN = re.compile(r"^---\s*\n(.*?)\n---\s*\n?", re.S)


def parse_frontmatter(text: str) -> Tuple[Dict, str]:
    match = FRONT_MATTER_PATTERN.match(text)
    if not match:
        return {}, text

    fm_text = match.group(1)
    body = text[match.end() :]

    if yaml:
        try:
            data = yaml.safe_load(fm_text) or {}
            if isinstance(data, dict):
                return data, body
        except Exception:
            pass

    fm: Dict = {}
    lines = fm_text.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        if re.match(r"^\s*[A-Za-z0-9_-]+:\s*$", line):
            key = line.split(":", 1)[0].strip()
            arr = []
            i += 1
            while i < len(lines) and re.match(r"^\s*-\s", lines[i]):
                arr.append(re.sub(r"^\s*-\s*", "", lines[i]).strip())
                i += 1
            fm[key] = arr
            continue
        if ":" in line:
            k, v = line.split(":", 1)
            val = v.strip()
            if val.startswith("[") and val.endswith("]"):
                items = [
                    item.strip().strip("'\"")
                    for item in val[1:-1].split(",")
                    if item.strip().strip("'\"")
                ]
                fm[k.strip()] = items
            else:
                fm[k.strip()] = val
        i += 1
    return fm, body


def index_notes(root: Path):
    files = list(root.rglob("*.md"))
    by_stem = {f.stem: f for f in files}
    aliases = {}
    for f in files:
        fm, _ = parse_frontmatter(read_text(f))
        aliases_value = fm.get("aliases")
        if isinstance(aliases_value, str):
            aliases_iter = [aliases_value]
        elif isinstance(aliases_value, (list, tuple, set)):
            aliases_iter = aliases_value
        else:
            aliases_iter = []
        for a in aliases_iter:
            if a:
                aliases[str(a)] = f
    return files, by_stem, aliases


def candidate_targets(raw: str) -> Set[str]:
    target = raw.split("|", 1)[0].strip()
    if not target or target.startswith("#") or target.startswith("^"):
        return set()
    target = target.split("#", 1)[0].split("^", 1)[0].strip()
    if target.lower().endswith(".md"):
        target = target[:-3]

    candidates = {target} if target else set()
    if "/" in target:
        candidates.add(target.split("/")[-1].strip())
    return {c for c in candidates if c}


def find_broken_links(root: Path, by_stem, aliases):
    broken = []
    valid_relative = {
        str(path.relative_to(root)).rsplit(".", 1)[0] for path in by_stem.values()
    }
    for f in root.rglob("*.md"):
        text = read_text(f)
        for match in re.finditer(r"\[\[([^\]]+)\]\]", text):
            targets = candidate_targets(match.group(1))
            if not targets:
                continue
            if not targets.isdisjoint(by_stem) or not targets.isdisjoint(aliases):
                continue
            if not targets.isdisjoint(valid_relative):
                continue
            broken.append({"file": str(f.relative_to(root)), "link": match.group(1)})
    return broken


def find_duplicate_titles(root: Path):
    seen = {}
    dups = []
    for f in root.rglob("*.md"):
        text = read_text(f)
        fm, _ = parse_frontmatter(text)
        title = fm.get("title") or f.stem
        if title in seen and str(f) != seen[title]:
            dups.append(
                {
                    "title": title,
                    "files": [
                        str(Path(seen[title]).relative_to(root)),
                        str(f.relative_to(root)),
                    ],
                }
            )
        else:
            seen[title] = str(f)
    return dups


def main():
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
    files, by_stem, aliases = index_notes(root)
    report = {
        "total_files": len(files),
        "broken_links": find_broken_links(root, by_stem, aliases),
        "duplicate_titles": find_duplicate_titles(root),
    }
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
