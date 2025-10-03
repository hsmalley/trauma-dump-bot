#!/usr/bin/env python3
"""
vault_loader.py

Unified vault loader and saver for .json and .msgpack formats.

from vault_loader import load_vault, save_vault

vault = load_vault("vault.json")
save_vault(vault, "vault.msgpack")

vault2 = load_vault("vault.msgpack")
save_vault(vault2, "vault-pretty.json", pretty=True)

"""

import os
import json

try:
    import msgpack
except ModuleNotFoundError as exc:
    raise ModuleNotFoundError(
        "msgpack is required for vault serialization; install with `pip install msgpack`."
    ) from exc
import hashlib
import yaml
import jsonschema
from typing import Any, Dict

try:
    from .vault_schema import schema as vault_schema
except ImportError:  # pragma: no cover - fallback when run as a script
    from vault_schema import schema as vault_schema  # type: ignore


# Aliases
ALIAS_MAP = {
    "observedPatterns": "O",
    "relationalFunction": "R",
    "psychoeducational": "P",
    "repairSuggestions": "S",
    "version": "v",
}
REVERSE_ALIAS_MAP = {v: k for k, v in ALIAS_MAP.items()}


def aliasify_object(obj: Dict[str, Any]) -> Dict[str, Any]:
    result: Dict[str, Any] = {}
    for long_key, val in obj.items():
        if val is None or (isinstance(val, (list, dict)) and not val):
            continue
        short_key = ALIAS_MAP.get(long_key, long_key)
        if isinstance(val, dict):
            val = aliasify_object(val)
        elif isinstance(val, list):
            val = [aliasify_object(v) if isinstance(v, dict) else v for v in val]
        result[short_key] = val
    return result


def de_aliasify_object(obj: Dict[str, Any]) -> Dict[str, Any]:
    result: Dict[str, Any] = {}
    for short_key, val in obj.items():
        long_key = REVERSE_ALIAS_MAP.get(short_key, short_key)
        if isinstance(val, dict):
            val = de_aliasify_object(val)
        elif isinstance(val, list):
            val = [de_aliasify_object(v) if isinstance(v, dict) else v for v in val]
        result[long_key] = val
    return result


def validate_vault(vault: Dict[str, Any]) -> Dict[str, Any]:
    """Validate vault structure against the bundled JSON schema."""
    try:
        jsonschema.validate(vault, vault_schema)
    except jsonschema.ValidationError as exc:
        raise ValueError(f"Vault schema validation failed:\n{exc.message}") from exc
    return vault


def load_vault(path: str, *, validate: bool = False) -> Dict[str, Any]:
    _, ext = os.path.splitext(path.lower())
    if ext == ".json":
        with open(path, "r", encoding="utf-8") as f:
            raw = json.load(f)
    elif ext in [".mpack", ".msgpack"]:
        with open(path, "rb") as f:
            raw = msgpack.unpackb(f.read(), raw=False)
    else:
        raise ValueError(f"Unsupported file format: {ext}")
    vault = de_aliasify_object(raw)
    return validate_vault(vault) if validate else vault


def save_vault(
    vault: Dict[str, Any], path: str, pretty: bool = False, validate: bool = False
) -> None:
    _, ext = os.path.splitext(path.lower())
    if validate:
        validate_vault(vault)
    compact = aliasify_object(vault)

    if ext == ".json":
        with open(path, "w", encoding="utf-8") as f:
            json.dump(
                compact,
                f,
                indent=2 if pretty else None,
                separators=(",", ":") if not pretty else None,
                ensure_ascii=False,
            )
    elif ext in [".mpack", ".msgpack"]:
        with open(path, "wb") as f:
            f.write(msgpack.packb(compact, use_bin_type=True))
    else:
        raise ValueError(f"Unsupported file format: {ext}")


def vault_hash(vault: Dict[str, Any]) -> str:
    """
    Compute a deterministic SHA256 hash of the vault content.
    Uses aliasified + minified JSON for canonicalization.
    """
    compact = aliasify_object(vault)
    as_bytes = json.dumps(
        compact, separators=(",", ":"), sort_keys=True, ensure_ascii=False
    ).encode("utf-8")
    return hashlib.sha256(as_bytes).hexdigest()


def write_vault_hash(vault: Dict[str, Any], path: str) -> str:
    """
    Write the hash of a vault to a file (used for caching or validation).
    Returns the computed hash string.
    """
    h = vault_hash(vault)
    with open(path, "w", encoding="utf-8") as f:
        f.write(h + "\n")
    return h


def read_vault_hash(path: str) -> str:
    """
    Read hash from a .vault.hash file.
    """
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read().strip()
    except FileNotFoundError:
        return ""


def save_vault_yaml(
    vault: Dict[str, Any],
    path: str,
    git_meta: bool = True,
    validate: bool = False,
) -> None:
    """
    Save the full vault to a .yaml file, optionally including Git metadata.
    """
    if validate:
        validate_vault(vault)
    data = vault.copy()

    if git_meta:
        try:
            import subprocess

            meta = {
                "git_commit": subprocess.check_output(
                    ["git", "rev-parse", "HEAD"], text=True
                ).strip(),
                "git_author": subprocess.check_output(
                    ["git", "log", "-1", "--pretty=format:%an <%ae>"], text=True
                ).strip(),
                "git_date": subprocess.check_output(
                    ["git", "log", "-1", "--date=iso", "--pretty=format:%ad"],
                    text=True,
                ).strip(),
            }
            data["_meta"] = meta
        except Exception:
            pass  # fail silently if not in git repo

    with open(path, "w", encoding="utf-8") as f:
        yaml.safe_dump(data, f, sort_keys=False, allow_unicode=True)
