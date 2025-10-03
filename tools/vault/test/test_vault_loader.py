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
    with tempfile.TemporaryDirectory() as tmpdir:
        path = os.path.join(tmpdir, "vault.msgpack")
        save_vault(VAULT_FIXTURE, path, validate=True)
        loaded = load_vault(path, validate=True)
        assert loaded == VAULT_FIXTURE


def test_hash_stability():
    h1 = vault_hash(VAULT_FIXTURE)
    h2 = vault_hash(VAULT_FIXTURE.copy())
    assert h1 == h2


def test_schema_compliance():
    validate_vault(VAULT_FIXTURE)
