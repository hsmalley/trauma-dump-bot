#!/usr/bin/env python3
"""
vault_to_json.py

Extract a tar archive (or operate on an existing directory), skip directories that
contain one or more specified tag files (same semantics as
`tar --exclude-tag-all=TAG`), and build a JSON representation of all Markdown
files (.md) while preserving folder structure.

Usage examples:
  # Extract and build JSON, excluding dirs that contain ".exclude"
  python Meta/Tools/vault_to_json.py \
    --tar Relational_Analysis_Vault.tar \
    --extract-to ./extracted \
    --exclude-tag-all .exclude \
    --output markdown_tree.json

  # Exclude multiple tag names:
  python Meta/Tools/vault_to_json.py \
    --tar archive.tar \
    --extract-to ./extracted \
    --exclude-tag-all .exclude .gitignore TAGFILE \
    --record-exclusions \
    --output result.json

  # If you already extracted the archive:
  python Meta/Tools/vault_to_json.py \
    --root ./Relational_Analysis_Vault \
    --exclude-tag-all .exclude \
    --output markdown_tree.json
"""

from __future__ import annotations

import argparse
import json
import os
import posixpath
import re
import tarfile
from datetime import date, datetime
from typing import Dict, Optional, Set, Tuple

# Optional YAML support for frontmatter parsing
try:
    import yaml  # type: ignore
except Exception:
    yaml = None  # fallback parser will be used if needed


def default_converter(o):
    """Convert datetime values to ISO strings for JSON dumping."""
    if isinstance(o, (datetime, date)):
        return o.isoformat()
    raise TypeError(f"Object of type {o.__class__.__name__} is not JSON serializable")


def parse_frontmatter(text: str) -> Tuple[Optional[Dict], str]:
    """
    Return (frontmatter_dict_or_None, body_text).
    Accepts frontmatter delimited by leading '---' and trailing '---'.
    Uses PyYAML if available, otherwise a simple fallback parser for basic mappings and lists.
    """
    m = re.match(r"^\s*---\s*\n(.*?\n?)^---\s*\n", text, re.S | re.M)
    if not m:
        return None, text
    fm_text = m.group(1)
    body = text[m.end() :]

    if yaml:
        try:
            data = yaml.safe_load(fm_text) or {}
            return data, body
        except Exception:
            pass  # fallback to simple parser

    # Simple fallback parser (handles simple key: value and - list items)
    data: Dict = {}
    cur_key: Optional[str] = None
    for raw_line in fm_text.splitlines():
        line = raw_line.rstrip()
        if not line.strip():
            continue
        stripped = line.strip()
        if stripped.startswith("- "):
            if cur_key:
                data.setdefault(cur_key, []).append(stripped[2:].strip())
            continue
        if ":" in stripped:
            key, val = stripped.split(":", 1)
            key = key.strip()
            val = val.strip()
            if val.lower() in ("null", "none", "~"):
                val_conv = None
            elif val.lower() in ("true", "false"):
                val_conv = val.lower() == "true"
            else:
                try:
                    val_conv = int(val)
                except Exception:
                    val_conv = val
            data[key] = val_conv
            cur_key = key
        else:
            # continuation line for last key
            if cur_key:
                prev = data.get(cur_key, "")
                if isinstance(prev, list):
                    prev.append(stripped)
                else:
                    data[cur_key] = (prev or "") + "\n" + stripped
    return data, body


def find_excluded_dirs_in_tar(tar_path: str, tagfiles: Set[str]) -> Set[str]:
    """
    Scan the tarfile members and return a set of POSIX directory paths (relative to archive root)
    that contain any of the tagfiles. A member whose basename matches a tagfile indicates its
    immediate directory should be excluded.
    """
    excluded: Set[str] = set()
    with tarfile.open(tar_path, "r:*") as tf:
        for m in tf.getmembers():
            name = m.name  # POSIX path inside tar
            base = posixpath.basename(name)
            if base in tagfiles:
                dirpath = posixpath.dirname(name)  # '' for top-level
                excluded.add(dirpath)
    return excluded


def find_excluded_dirs_in_fs(root_dir: str, tagfiles: Set[str]) -> Set[str]:
    """
    Walk the filesystem and collect POSIX-relative directories that contain any
    tagfile as an immediate child.
    """
    excluded: Set[str] = set()
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for tag in tagfiles:
            if tag in filenames:
                rel = os.path.relpath(dirpath, root_dir).replace(os.sep, "/")
                if rel == ".":
                    rel = ""  # represent top-level as empty string to match tar semantics
                excluded.add(rel)
                break
    return excluded


def member_is_in_excluded(member_name: str, excluded_dirs: Set[str]) -> bool:
    """
    Return True if the POSIX member path is inside any excluded directory. For
    example, 'foo/bar' excludes 'foo/bar/baz.txt' and everything beneath it.
    """
    if not excluded_dirs:
        return False
    for d in excluded_dirs:
        if d == "":
            return True
        if member_name == d or member_name.startswith(d + "/"):
            return True
    return False


def extract_tar_excluding(tar_path: str, out_dir: str, tagfiles: Set[str]) -> Set[str]:
    """
    Extract members that are *not* under directories containing a tagfile and
    return the excluded directories (POSIX paths relative to the archive root).
    """
    excluded = find_excluded_dirs_in_tar(tar_path, tagfiles)
    if excluded:
        print(
            f"Excluded directories found in archive (tags={sorted(tagfiles)}): {sorted(excluded)}"
        )
    else:
        print(f"No excluded directories found in archive (tags={sorted(tagfiles)}).")

    with tarfile.open(tar_path, "r:*") as tf:
        for m in tf.getmembers():
            mn = m.name  # POSIX-style member name
            if member_is_in_excluded(mn, excluded):
                # skip this member
                continue
            target_path = os.path.join(out_dir, *mn.split("/"))
            parent = os.path.dirname(target_path)
            if parent and not os.path.exists(parent):
                os.makedirs(parent, exist_ok=True)
            try:
                try:
                    tf.extract(m, path=out_dir, set_attrs=False)  # Python 3.12+
                except TypeError:
                    tf.extract(m, path=out_dir)
            except Exception:
                if m.isreg():
                    f = tf.extractfile(m)
                    if f:
                        with open(target_path, "wb") as outf:
                            outf.write(f.read())
                else:
                    print(f"Warning: could not extract member {mn!r}; skipping.")
    return excluded


def build_md_tree(root_dir: str, tagfiles: Set[str]):
    """
    Walk the directory tree and build a JSON structure of directories and .md files,
    excluding any directory that contains any tagfile (immediate children check).
    """

    def dir_contains_tag(path: str) -> bool:
        """Return True if the directory directly contains any exclusion tag."""
        try:
            names = os.listdir(path)
            for tag in tagfiles:
                if tag in names:
                    return True
            return False
        except Exception:
            return False

    def node_for_dir(path: str, relbase: str):
        """Build a tree node for a directory unless it is excluded."""
        if dir_contains_tag(path):
            return None
        node = {
            "name": os.path.basename(path) or ".",
            "type": "directory",
            "children": [],
        }
        try:
            entries = sorted(os.listdir(path))
        except Exception:
            return node
        for e in entries:
            full = os.path.join(path, e)
            if os.path.isdir(full):
                child = node_for_dir(full, relbase)
                if child and child.get("children"):
                    node["children"].append(child)
            else:
                if e.lower().endswith(".md"):
                    try:
                        with open(full, "r", encoding="utf-8", errors="replace") as f:
                            raw = f.read()
                    except Exception as exc:
                        raw = f"***FAILED TO READ: {exc}***"
                    fm, body = parse_frontmatter(raw)
                    stat = os.stat(full)
                    rel = os.path.relpath(full, relbase).replace(os.sep, "/")
                    file_node = {
                        "name": e,
                        "type": "file",
                        "relpath": rel,
                        "size_bytes": stat.st_size,
                        "mtime_utc": datetime.fromtimestamp(stat.st_mtime, datetime.UTC).isoformat() + "Z",
                        "frontmatter": fm,
                        "content": body,
                    }
                    node["children"].append(file_node)
        if node["children"]:
            return node
        return None

    root_node = node_for_dir(root_dir, root_dir)
    if root_node is None:
        return {"name": os.path.basename(root_dir), "type": "directory", "children": []}
    return root_node


def main():
    """CLI entry point for building a JSON tree from a vault archive or folder."""
    p = argparse.ArgumentParser(
        description=(
            "Extract tar and build markdown JSON, excluding directories that contain "
            "one or more tag files."
        )
    )
    p.add_argument(
        "--tar",
        help=(
            "Path to .tar archive (optional). If provided, will extract to --extract-to "
            "before processing."
        ),
    )
    p.add_argument(
        "--extract-to",
        help="Directory to extract into (default: ./extracted)",
        default="./extracted",
    )
    p.add_argument(
        "--root",
        help="If you already have an extracted folder, point this to it instead of --tar",
    )
    p.add_argument(
        "--exclude-tag-all",
        nargs="+",
        dest="exclude_tag_all",
        help=(
            "One or more tag filenames that, if present in a directory, cause that "
            "directory and its subtree to be excluded. Default: .exclude"
        ),
        default=[".exclude"],
    )
    p.add_argument(
        "--output",
        help="JSON output file (default markdown_tree.json)",
        default="markdown_tree.json",
    )
    p.add_argument(
        "--record-exclusions",
        action="store_true",
        help=(
            "If set, include the discovered excluded directories in the top-level "
            "JSON as 'excluded_dirs'."
        ),
    )
    args = p.parse_args()

    tagfiles: Set[str] = set(args.exclude_tag_all)

    if not args.tar and not args.root:
        p.error("One of --tar or --root must be provided.")

    excluded_dirs: Set[str] = set()
    if args.tar:
        outdir = os.path.abspath(args.extract_to)
        os.makedirs(outdir, exist_ok=True)
        msg = (
            "Extracting {tar} into {outdir} while excluding directories that contain "
            "tags {tags} ..."
        ).format(tar=args.tar, outdir=outdir, tags=sorted(tagfiles))
        print(msg)
        # capture excluded dirs returned from extraction function
        excluded_dirs = extract_tar_excluding(args.tar, outdir, tagfiles)
        root_dir = outdir
    else:
        root_dir = os.path.abspath(args.root)
        # if working on an existing tree, scan filesystem to discover exclusions
        excluded_dirs = find_excluded_dirs_in_fs(root_dir, tagfiles)
        if excluded_dirs:
            msg = ("Excluded directories discovered in filesystem (tags={tags}): {dirs}").format(
                tags=sorted(tagfiles), dirs=sorted(excluded_dirs)
            )
            print(msg)
        else:
            msg = "No excluded directories discovered in filesystem (tags={tags}).".format(
                tags=sorted(tagfiles)
            )
            print(msg)

    msg = (
        "Building markdown JSON tree from root: {root} (skipping dirs that contain tags {tags})"
    ).format(root=root_dir, tags=sorted(tagfiles))
    print(msg)
    tree = build_md_tree(root_dir, tagfiles)

    # Save JSON (optionally record exclusions)
    if args.record_exclusions:
        result = {
            "generated_at": datetime.utcnow().isoformat() + "Z",
            "root_name": os.path.basename(root_dir),
            "excluded_dirs": sorted(excluded_dirs),
            "tree": tree,
        }
        with open(args.output, "w", encoding="utf-8") as outf:
            json.dump(result, outf, default=default_converter, indent=2, ensure_ascii=False)
    else:
        with open(args.output, "w", encoding="utf-8") as outf:
            json.dump(tree, outf, default=default_converter, indent=2, ensure_ascii=False)

    print(f"Wrote JSON to {args.output}")


if __name__ == "__main__":
    main()
