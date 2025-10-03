import argparse
import json
import re
from pathlib import Path
from typing import Any, Dict, List, Set

try:
    import yaml  # type: ignore
except Exception:  # pragma: no cover - optional dependency
    yaml = None


FRONT_MATTER_PATTERN = re.compile(r"^---\s*\n(.*?)\n---\s*\n?", re.S)


def extract_aliases_from_front_matter(text: str) -> Set[str]:
    """Extract aliases from YAML front matter in a markdown file."""
    match = FRONT_MATTER_PATTERN.match(text)
    if not match:
        return set()

    fm_text = match.group(1)

    if yaml:
        try:
            data = yaml.safe_load(fm_text) or {}
            aliases = data.get("aliases") if isinstance(data, dict) else None
            if isinstance(aliases, (list, tuple)):
                return {str(item).strip() for item in aliases if str(item).strip()}
            if isinstance(aliases, str):
                return {
                    part.strip().strip("'\"")
                    for part in aliases.strip("[]").split(",")
                    if part.strip().strip("'\"")
                }
        except Exception:
            pass  # fall back to manual parsing if YAML fails

    aliases: Set[str] = set()
    in_alias_block = False
    for line in fm_text.splitlines():
        stripped = line.strip()
        if not stripped and in_alias_block:
            break
        if stripped.startswith("aliases:"):
            rest = stripped[len("aliases:") :].strip()
            if rest.startswith("[") and rest.endswith("]"):
                for part in rest[1:-1].split(","):
                    cleaned = part.strip().strip("'\"")
                    if cleaned:
                        aliases.add(cleaned)
                in_alias_block = False
            else:
                in_alias_block = True
            continue
        if in_alias_block:
            if stripped.startswith("- "):
                cleaned = stripped[2:].strip().strip("'\"")
                if cleaned:
                    aliases.add(cleaned)
            else:
                in_alias_block = False
    return aliases


def load_vault(path: Path) -> Dict[str, Any]:
    """Load the markdown vault and build a mapping of valid titles and their aliases."""
    vault = {}
    for file_path in path.rglob("*.md"):
        title = file_path.stem
        try:
            content = file_path.read_text(encoding="utf-8")
        except Exception:
            continue
        aliases = extract_aliases_from_front_matter(content)
        vault[title] = {
            "file": str(file_path.relative_to(path)),
            "aliases": aliases,
        }
    return vault


def extract_links(text: str) -> Set[str]:
    """Extract [[links]] from markdown content."""
    return set(re.findall(r"\[\[([^\]]+)\]\]", text))


def candidate_targets(raw: str) -> Set[str]:
    """Return possible note targets for a raw wiki-style link."""
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


def validate_links(vault: Dict[str, Any], path: Path) -> List[Dict[str, str]]:
    """Validate all markdown links in the vault."""
    all_titles = set(vault.keys())
    all_aliases = {alias for data in vault.values() for alias in data["aliases"]}
    valid_targets = all_titles | all_aliases

    relative_targets = {
        data["file"][:-3] if data["file"].lower().endswith(".md") else data["file"]
        for data in vault.values()
    }
    valid_targets |= relative_targets

    broken_links = []
    for title, data in vault.items():
        file_path = path / data["file"]
        try:
            text = file_path.read_text(encoding="utf-8")
        except Exception:
            continue
        links = extract_links(text)
        for raw_link in links:
            targets = candidate_targets(raw_link)
            if not targets:
                continue
            if targets.isdisjoint(valid_targets):
                broken_links.append({"file": data["file"], "link": raw_link})
    return broken_links


def main():
    """CLI entry point for validating markdown links."""
    parser = argparse.ArgumentParser(description="Validate markdown links in a vault.")
    parser.add_argument("vault_path", type=str, help="Path to the markdown vault")
    args = parser.parse_args()

    path = Path(args.vault_path)
    vault = load_vault(path)
    broken_links = validate_links(vault, path)

    report = {
        "total_files": len(vault),
        "broken_links": broken_links,
        "duplicate_titles": [],  # Could be implemented later
    }
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
