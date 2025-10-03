<!-- @format -->

# Vault Tooling

Utilities for converting, validating, and exporting relational analysis vaults. These
scripts share a common loader that understands the compact alias format used for
MessagePack storage and the expanded JSON representation.

## Contents

- `vault_loader.py` – core helpers for loading, saving, hashing, and validating vault
  objects (JSON or MessagePack).
- `vault_cli.py` – full-featured CLI for converting between JSON and MessagePack,
  emitting YAML snapshots, and checking hash sync.
- `vault_to_msgpack.py` – lightweight converter wrapper for simple JSON ↔ MessagePack
  transforms.
- `vault_to_json.py` – builds a JSON tree representation of a markdown vault, with
  optional tar extraction and directory exclusion controls.
- `diff_vault.py` – appends a unified diff of `vault.yaml` changes to
  `vault-changelog.md`.
- `vault_schema.json` – JSON Schema definition describing a single vault entry.
- `test/test_vault_loader.py` – pytest coverage for round-trip conversion, hashing, and
  schema validation.

## Requirements

- Python 3.9+
- [`msgpack`](https://pypi.org/project/msgpack/) (required for binary serialization)
- [`PyYAML`](https://pypi.org/project/PyYAML/) (optional; enables richer front-matter
  parsing in `vault_to_json.py`)
- [`jsonschema`](https://pypi.org/project/jsonschema/) (only needed when using the
  `--validate` flag)
- pytest (optional; only for running tests)

Install dependencies, for example:

```bash
pip install msgpack PyYAML jsonschema pytest
```

## Common Workflows

### Convert JSON ↔ MessagePack

Fast path:

```bash
python3 tools/vault/vault_to_msgpack.py Relational_Analysis_Vault.json Relational_Analysis_Vault.msgpack
```

Full CLI with extras:

```bash
python3 tools/vault/vault_cli.py Relational_Analysis_Vault.json Relational_Analysis_Vault.msgpack --pretty --hash vault.sha --yaml vault.yaml
```

Add `--validate` to perform JSON Schema validation before writing output.

### Check Vault Sync

```bash
python3 tools/vault/vault_cli.py Relational_Analysis_Vault.json Relational_Analysis_Vault.msgpack --check-sync
```

Exit status is non-zero if hashes differ.

### Export Markdown Tree JSON

```bash
python3 tools/vault/vault_to_json.py --root Relational_Analysis_Vault --exclude-tag-all .exclude --output markdown_tree.json
```

When working with tar archives:

```bash
python3 tools/vault/vault_to_json.py --tar vault.tar --extract-to ./extracted --record-exclusions
```

### Record Diff to Changelog

```bash
python3 tools/vault/diff_vault.py
```

Appends a timestamped diff of `vault.yaml` compared with the last git commit to
`vault-changelog.md`.

## Testing

```bash
PYTHONPATH=. pytest tools/vault/test/test_vault_loader.py
```

Run in an environment where `msgpack` is installed.

## Troubleshooting

- _"ModuleNotFoundError: No module named 'msgpack'"_: install the `msgpack` package.
- Validation errors list the specific JSON Schema violation; ensure you are validating
  individual vault entries rather than the directory tree JSON exported by
  `vault_to_json.py`.
