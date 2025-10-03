#!/usr/bin/env python3
"""Utility to convert vault files between JSON and MessagePack."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import List


def _import_loader():
    try:
        from .vault_loader import load_vault, save_vault

        return load_vault, save_vault
    except ImportError:  # pragma: no cover - fallback for script execution
        package_dir = Path(__file__).resolve().parent
        if str(package_dir) not in sys.path:
            sys.path.insert(0, str(package_dir))
        from vault_loader import load_vault, save_vault  # type: ignore

        return load_vault, save_vault


load_vault, save_vault = _import_loader()


def convert(
    input_path: str,
    output_path: str,
    pretty: bool = False,
    validate: bool = False,
) -> None:
    vault = load_vault(input_path, validate=validate)
    save_vault(vault, output_path, pretty=pretty, validate=validate)
    print(f"✅ Converted: {input_path} → {output_path}")


def main(argv: List[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Convert a vault between JSON and MessagePack formats."
    )
    parser.add_argument("input", help="Input vault file (.json, .mpack, .msgpack)")
    parser.add_argument("output", help="Output vault file (.json, .mpack, .msgpack)")
    parser.add_argument(
        "--pretty",
        action="store_true",
        help="Pretty-print JSON output (ignored for MessagePack)",
    )
    parser.add_argument(
        "--validate",
        action="store_true",
        help="Validate the vault against the JSON schema before writing",
    )

    args = parser.parse_args(argv)

    try:
        convert(args.input, args.output, pretty=args.pretty, validate=args.validate)
    except Exception as exc:  # pragma: no cover - surfaced to CLI
        print(f"❌ Conversion failed: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
