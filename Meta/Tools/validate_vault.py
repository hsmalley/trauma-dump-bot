#!/usr/bin/env python3
import os, re, sys, json
from pathlib import Path

def read_text(p):
    return Path(p).read_text(encoding="utf-8", errors="ignore")

def parse_frontmatter(text):
    if text.startswith("---"):
        m = re.match(r"---\n(.*?)\n---\n?(.*)$", text, flags=re.DOTALL)
        if m:
            yaml_raw, body = m.group(1), m.group(2)
            fm = {}
            lines = yaml_raw.splitlines()
            i = 0
            while i < len(lines):
                line = lines[i]
                if re.match(r"^\s*[A-Za-z0-9_-]+:\s*$", line):
                    key = line.split(":",1)[0].strip()
                    arr = []
                    i += 1
                    while i < len(lines) and re.match(r"^\s*-\s", lines[i]):
                        arr.append(re.sub(r"^\s*-\s*", "", lines[i]).strip())
                        i += 1
                    fm[key] = arr
                    continue
                if ":" in line:
                    k,v = line.split(":",1)
                    fm[k.strip()] = v.strip()
                i += 1
            return fm, body
    return {}, text

def index_notes(root: Path):
    files = list(root.rglob("*.md"))
    by_stem = {f.stem: f for f in files}
    aliases = {}
    for f in files:
        fm, _ = parse_frontmatter(read_text(f))
        if isinstance(fm.get("aliases"), list):
            for a in fm["aliases"]:
                if a:
                    aliases[a] = f
    return files, by_stem, aliases

def find_broken_links(root: Path, by_stem, aliases):
    broken = []
    for f in root.rglob("*.md"):
        text = read_text(f)
        for m in re.finditer(r"\[\[([^\]]+)\]\]", text):
            target = m.group(1).split("|",1)[0].strip()
            # Resolve by stem match or alias
            if target in by_stem:
                continue
            if target in aliases:
                continue
            # Try exact file path reference (with folders) minus .md
            if "/" in target:
                norm = target.split("/")[-1]
                if norm in by_stem:
                    continue
            broken.append({"file": str(f.relative_to(root)), "link": target})
    return broken

def find_duplicate_titles(root: Path):
    seen = {}
    dups = []
    for f in root.rglob("*.md"):
        text = read_text(f)
        fm, _ = parse_frontmatter(text)
        title = fm.get("title") or f.stem
        if title in seen and str(f) != seen[title]:
            dups.append({"title": title, "files": [str(Path(seen[title]).relative_to(root)), str(f.relative_to(root))]})
        else:
            seen[title] = str(f)
    return dups

def main():
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
    files, by_stem, aliases = index_notes(root)
    report = {
        "total_files": len(files),
        "broken_links": find_broken_links(root, by_stem, aliases),
        "duplicate_titles": find_duplicate_titles(root)
    }
    print(json.dumps(report, indent=2))

if __name__ == "__main__":
    main()
