#!/usr/bin/env python3
"""CLI for converting vaults between JSON and MessagePack formats."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import List


def _import_loader():
    """Import loader helpers with a fallback for direct script execution."""
    try:
        from .vault_loader import (
            load_vault,
            save_vault,
            save_vault_yaml,
            vault_hash,
            write_vault_hash,
            read_vault_hash,
        )

        return (
            load_vault,
            save_vault,
            save_vault_yaml,
            vault_hash,
            write_vault_hash,
            read_vault_hash,
        )
    except (
        ImportError
    ):  # pragma: no cover - fallback when invoked via python path/to/script.py
        package_dir = Path(__file__).resolve().parent
        if str(package_dir) not in sys.path:
            sys.path.insert(0, str(package_dir))
        from vault_loader import (  # type: ignore
            load_vault,
            save_vault,
            save_vault_yaml,
            vault_hash,
            write_vault_hash,
            read_vault_hash,
        )

        return (
            load_vault,
            save_vault,
            save_vault_yaml,
            vault_hash,
            write_vault_hash,
            read_vault_hash,
        )


(
    load_vault,
    save_vault,
    save_vault_yaml,
    vault_hash,
    write_vault_hash,
    read_vault_hash,
) = _import_loader()


def run_cli(argv: List[str] | None = None) -> int:
    """Parse CLI arguments and perform the requested vault conversion."""
    parser = argparse.ArgumentParser(
        description="Vault converter for JSON ↔ MessagePack"
    )
    parser.add_argument("input", help="Input file (.json or .msgpack)")
    parser.add_argument("output", help="Output file (.json or .msgpack)")
    parser.add_argument(
        "--pretty", action="store_true", help="Pretty-print JSON output"
    )
    parser.add_argument(
        "--hash",
        metavar="PATH",
        help="Write SHA256 vault hash to this file after conversion",
    )
    parser.add_argument(
        "--check-sync",
        action="store_true",
        help="Check that INPUT and OUTPUT vaults resolve to the same hash",
    )
    parser.add_argument(
        "--skip-unchanged",
        action="store_true",
        help="Skip conversion when --hash matches the current vault",
    )
    parser.add_argument(
        "--yaml",
        metavar="YAML_PATH",
        help="Export full vault as .yaml with optional Git metadata",
    )
    parser.add_argument(
        "--validate",
        action="store_true",
        help="Validate the vault against the JSON schema before writing",
    )

    args = parser.parse_args(argv)

    if args.skip_unchanged and not args.hash:
        parser.error("--skip-unchanged requires --hash")

    if args.check_sync:
        return 0 if check_sync(args.input, args.output, validate=args.validate) else 1

    try:
        vault = load_vault(args.input, validate=args.validate)
    except Exception as exc:  # pragma: no cover - surfaced to CLI
        print(f"❌ Failed to load vault: {exc}", file=sys.stderr)
        return 1

    current_hash = vault_hash(vault) if args.hash else None
    if args.skip_unchanged and args.hash:
        previous_hash = read_vault_hash(args.hash)
        if previous_hash == current_hash:
            print(f"⏭️ Vault unchanged, skipping write: {args.hash}")
            return 0

    try:
        save_vault(vault, args.output, pretty=args.pretty, validate=args.validate)
        print(f"✅ Converted: {args.input} → {args.output}")
    except Exception as exc:  # pragma: no cover - surfaced to CLI
        print(f"❌ Failed to write vault: {exc}", file=sys.stderr)
        return 1

    if args.yaml:
        try:
            save_vault_yaml(vault, args.yaml, git_meta=True, validate=args.validate)
            print(f"📘 YAML export written: {args.yaml}")
        except Exception as exc:  # pragma: no cover - surfaced to CLI
            print(f"❌ Failed to export YAML: {exc}", file=sys.stderr)
            return 1

    if args.hash and current_hash is not None:
        try:
            write_vault_hash(vault, args.hash)
            print(f"🔐 Hash written: {args.hash} ({current_hash})")
        except Exception as exc:  # pragma: no cover - surfaced to CLI
            print(f"❌ Failed to write hash: {exc}", file=sys.stderr)
            return 1

    return 0


def check_sync(json_path: str, msgpack_path: str, *, validate: bool = False) -> bool:
    """Verify two vault files resolve to the same canonical hash."""
    try:
        vault_json = load_vault(json_path, validate=validate)
        vault_msgpack = load_vault(msgpack_path, validate=validate)
    except Exception as exc:
        print(f"❌ Failed to load vaults: {exc}")
        return False

    hash_json = vault_hash(vault_json)
    hash_msgpack = vault_hash(vault_msgpack)
    if hash_json == hash_msgpack:
        print(f"✅ Vaults in sync: {hash_json}")
        return True

    print(f"❌ Vault mismatch!\nJSON:    {hash_json}\nMsgpack: {hash_msgpack}")
    return False


if __name__ == "__main__":
    raise SystemExit(run_cli())
