import os
import tempfile
from tools.vault import load_vault, save_vault, vault_hash, validate_vault

VAULT_FIXTURE = {
    "observedPatterns": ["looping", "shutdown"],
    "relationalFunction": "protective withdrawal",
    "psychoeducational": "polyvagal + IFS",
    "repairSuggestions": "co-regulate then name",
    "version": "1.0",
}


def test_roundtrip_msgpack():
    """Ensure a vault survives save/load through MessagePack."""
    with tempfile.TemporaryDirectory() as tmpdir:
        path = os.path.join(tmpdir, "Relational_Analysis_Vault.msgpack")
        save_vault(VAULT_FIXTURE, path, validate=True)
        loaded = load_vault(path, validate=True)
        assert loaded == VAULT_FIXTURE


def test_hash_stability():
    """Vault hash should remain stable for identical content."""
    h1 = vault_hash(VAULT_FIXTURE)
    h2 = vault_hash(VAULT_FIXTURE.copy())
    assert h1 == h2


def test_schema_compliance():
    """The fixture must satisfy the validation schema."""
    validate_vault(VAULT_FIXTURE)
