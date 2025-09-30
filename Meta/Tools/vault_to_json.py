#!/usr/bin/env python3
"""
extract_and_build_json.py

Usage examples:
  # Extract and build JSON, excluding dirs that contain ".exclude"
  python extract_and_build_json.py --tar Relational_Analysis_Vault.tar --extract-to ./extracted --tag .exclude --output markdown_tree.json

  # If you already extracted the archive:
  python extract_and_build_json.py --root ./Relational_Analysis_Vault --tag .exclude --output markdown_tree.json
"""

import argparse
import os
import json
import datetime
import tarfile
import posixpath  # to handle tar member paths robustly


def find_excluded_dirs_in_tar(tar_path, tagfile):
    """
    Scan the tarfile members and return a set of POSIX directory paths that contain the tagfile.
    We'll treat a member whose basename == tagfile as indicating its immediate directory should be excluded.
    """
    excluded = set()
    with tarfile.open(tar_path, "r:*") as tf:
        for m in tf.getmembers():
            # normalize to posix
            name = m.name
            base = posixpath.basename(name)
            if base == tagfile:
                dirpath = posixpath.dirname(name)  # '' for top-level
                # represent root as '.' for clarity; but use '' consistent with member names
                excluded.add(dirpath)
    return excluded


def member_is_in_excluded(member_name, excluded_dirs):
    """
    Return True if member_name (posix path) is inside any excluded_dir.
    Example: excluded_dir 'foo/bar' excludes 'foo/bar/baz.txt', 'foo/bar/sub/...' and also 'foo/bar' itself.
    """
    if not excluded_dirs:
        return False
    # exact match or startswith dir + '/'
    for d in excluded_dirs:
        if d == "":
            # tag at root: exclude everything
            return True
        if member_name == d or member_name.startswith(d + "/"):
            return True
    return False


def extract_tar_excluding(tar_path, out_dir, tagfile):
    """
    Extract members from tar that are NOT under directories that contain tagfile.
    Returns the set of excluded directories discovered.
    """
    excluded = find_excluded_dirs_in_tar(tar_path, tagfile)
    print(
        f"Excluded directories found in archive (tag='{tagfile}'): {sorted(excluded)}"
    )

    with tarfile.open(tar_path, "r:*") as tf:
        for m in tf.getmembers():
            # use posix member names for prefix checks
            mn = m.name
            if member_is_in_excluded(mn, excluded):
                # skip this member
                # (optional) print(f"Skipping {mn}")
                continue
            # safe extraction path join
            target_path = os.path.join(out_dir, *mn.split("/"))
            # create parent dirs if needed
            parent = os.path.dirname(target_path)
            if parent and not os.path.exists(parent):
                os.makedirs(parent, exist_ok=True)
            try:
                tf.extract(m, path=out_dir, set_attrs=False)
            except Exception as e:
                # some tar members (like hardlinks) might fail with default extract; fallback to manual write for files
                if m.isreg():
                    f = tf.extractfile(m)
                    if f:
                        with open(target_path, "wb") as outf:
                            outf.write(f.read())
                else:
                    print(f"Warning: could not extract member {mn}: {e}")
    return excluded


def build_md_tree(root_dir, tagfile):
    """
    Walk the directory tree and build a JSON structure of directories and .md files,
    excluding any directory that contains tagfile (anywhere directly inside that directory).
    The semantics: if a directory contains a file whose basename == tagfile, skip that directory and its subtree.
    """

    def dir_contains_tag(path):
        # check immediate children for tagfile (not recursive)
        try:
            return tagfile in os.listdir(path)
        except Exception:
            return False

    def node_for_dir(path, relbase):
        # If this dir contains tagfile, treat as excluded
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
                if child and child.get(
                    "children"
                ):  # include dir only if it has md children or subdirs with md
                    node["children"].append(child)
            else:
                if e.lower().endswith(".md"):
                    try:
                        with open(full, "r", encoding="utf-8", errors="replace") as f:
                            content = f.read()
                    except Exception as exc:
                        content = f"***FAILED TO READ: {exc}***"
                    stat = os.stat(full)
                    rel = os.path.relpath(full, relbase)
                    file_node = {
                        "name": e,
                        "type": "file",
                        "relpath": rel.replace(os.sep, "/"),
                        "size_bytes": stat.st_size,
                        "mtime_utc": datetime.datetime.utcfromtimestamp(
                            stat.st_mtime
                        ).isoformat()
                        + "Z",
                        "content": content,
                    }
                    node["children"].append(file_node)
        return node

    root_node = node_for_dir(root_dir, root_dir)
    # If root was excluded entirely, return empty directory node with note
    if root_node is None:
        return {"name": os.path.basename(root_dir), "type": "directory", "children": []}
    return root_node


def main():
    p = argparse.ArgumentParser(
        description="Extract tar and build markdown JSON, excluding directories that contain a tag file."
    )
    p.add_argument(
        "--tar",
        help="Path to .tar archive (optional). If provided, will extract to --extract-to before processing.",
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
        "--tag",
        help="Tag filename to trigger excluding parent directory (default: .exclude)",
        default=".exclude",
    )
    p.add_argument(
        "--output",
        help="JSON output file (default markdown_tree.json)",
        default="markdown_tree.json",
    )
    args = p.parse_args()

    if not args.tar and not args.root:
        p.error("One of --tar or --root must be provided.")

    root_dir = None
    if args.tar:
        outdir = os.path.abspath(args.extract_to)
        os.makedirs(outdir, exist_ok=True)
        print(
            f"Extracting {args.tar} into {outdir} while excluding directories that contain tag '{args.tag}' ..."
        )
        excluded = extract_tar_excluding(args.tar, outdir, args.tag)
        root_dir = outdir
    else:
        root_dir = os.path.abspath(args.root)

    print(
        f"Building markdown JSON tree from root: {root_dir} (skipping dirs that contain '{args.tag}')"
    )
    tree = build_md_tree(root_dir, args.tag)
    # Save JSON
    with open(args.output, "w", encoding="utf-8") as outf:
        json.dump(tree, outf, indent=2, ensure_ascii=False)
    print(f"Wrote JSON to {args.output}")


if __name__ == "__main__":
    main()
