<!-- @format -->

# Vault Schema Overview

The vault tooling uses a compact alias format for MessagePack storage and validates
vault entries against the JSON Schema defined in `tools/vault/vault_schema.json`. This
document explains the structure and how it maps to human-readable keys.

## Schema Summary

| Field                | Type             | Required | Description                                          |
| -------------------- | ---------------- | -------- | ---------------------------------------------------- |
| `observedPatterns`   | array of strings | ✅       | Describes observed relational behaviour patterns.    |
| `relationalFunction` | string           | ✅       | Captures the primary relational dynamic or function. |
| `psychoeducational`  | string           | ❌       | Optional psychoeducation notes or frameworks.        |
| `repairSuggestions`  | string           | ❌       | Recommended interventions or repair steps.           |
| `version`            | string           | ❌       | Semantic version or revision marker for the entry.   |

No additional properties are allowed by the schema; any unexpected keys will fail
validation when the `--validate` flag is provided to CLI tools.

## Alias Mapping

To reduce MessagePack payload size, keys are aliased in the binary format. The mapping
is handled automatically by `vault_loader.py`:

| Long Key             | Alias |
| -------------------- | ----- |
| `observedPatterns`   | `O`   |
| `relationalFunction` | `R`   |
| `psychoeducational`  | `P`   |
| `repairSuggestions`  | `S`   |
| `version`            | `v`   |

When you load a vault file, these aliases are expanded back to the long-form keys. You
do **not** need to alias keys manually when editing JSON; the tooling handles
conversions in both directions.

## Validation Modes

- `load_vault(..., validate=True)` and `save_vault(..., validate=True)` enforce the
  schema.
- The CLI tools expose a `--validate` flag to enable schema checks during conversion or
  YAML export.
- Validation targets individual vault entries, not the directory tree JSON produced by
  `vault_to_json.py`.

## Adding New Fields

1. Update `tools/vault/vault_schema.json` with the new property definition.
2. Extend the alias maps in `tools/vault/vault_loader.py` if the new field should be
   compacted.
3. Document the field in this file and any relevant README sections.
4. Add or update tests in `tools/vault/test` to cover the new structure.

## Example Entry

```json
{
  "observedPatterns": ["shutdown", "looping"],
  "relationalFunction": "protective withdrawal",
  "psychoeducational": "polyvagal + IFS",
  "repairSuggestions": "co-regulate then name",
  "version": "1.0"
}
```

Use this shape when authoring JSON or validating external data before conversion.
