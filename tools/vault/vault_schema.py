"""Vault schema definition for validation"""

schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "Vault Entry",
    "type": "object",
    "required": ["observedPatterns", "relationalFunction"],
    "properties": {
        "observedPatterns": {"type": "array", "items": {"type": "string"}},
        "relationalFunction": {"type": "string"},
        "psychoeducational": {"type": "string"},
        "repairSuggestions": {"type": "string"},
        "version": {"type": "string"},
    },
    "additionalProperties": False,
}
