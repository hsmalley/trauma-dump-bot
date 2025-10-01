import argparse
import json
from pathlib import Path
import re
from typing import Any, Dict, List, Set


def extract_aliases_from_front_matter(text: str) -> Set[str]:
    """Extract aliases from YAML front matter in a markdown file."""
    aliases = set()
    if text.startswith("---"):
        end = text.find("---", 3)
        if end != -1:
            front_matter = text[3:end]
            match = re.search(r"aliases\s*:\s*\[([^\]]+)\]", front_matter)
            if match:
                items = match.group(1).split(",")
                for item in items:
                    cleaned = item.strip().strip("'\"")
                    if cleaned:
                        aliases.add(cleaned)
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


def validate_links(vault: Dict[str, Any], path: Path) -> List[Dict[str, str]]:
    """Validate all markdown links in the vault."""
    all_titles = set(vault.keys())
    all_aliases = {alias for data in vault.values() for alias in data["aliases"]}
    valid_targets = all_titles | all_aliases

    broken_links = []
    for title, data in vault.items():
        file_path = path / data["file"]
        try:
            text = file_path.read_text(encoding="utf-8")
        except Exception:
            continue
        links = extract_links(text)
        for link in links:
            if "|" in link:
                link = link.split("|")[0].strip()
            if link not in valid_targets:
                broken_links.append({"file": data["file"], "link": link})
    return broken_links


def main():
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

