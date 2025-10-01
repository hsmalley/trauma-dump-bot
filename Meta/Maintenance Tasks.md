---
title: "Maintenance Tasks"
tags: ["meta", "maintenance", "checklist", "vault"]
created: 2025-10-01
updated: 2025-10-01
---

<!-- @format -->

# 🛠️ Relational Analysis Vault — Maintenance Tasks

> Last updated: 2025-10-01

A living checklist for maintaining structure, tagging integrity, and tool readiness across the vault.

---

## ✅ Essential Maintenance

### 1. Vault Metadata Index

- [ ] Verify `Vault_Structure_Index.json` is current
- [ ] Regenerate if new folders or categories added
- [ ] Test cross-referencing via meta-tag links

### 2. Tag Consistency Check

- [ ] Run `_tagIndex` utility
- [ ] Resolve orphaned or duplicate tags
- [ ] Validate category anchors in each `.md` frontmatter

### 3. Utilities Health

- [ ] Confirm `Prompt_Utilities/` are accessible
- [ ] Sync `Utilities_Index.md` with tool status
- [ ] Test scripts in `Scripts/` for functionality

---

## 🔄 Framework & Example Alignment

### 4. Framework File Review

- [ ] Confirm all files in `Frameworks/` have consistent headers
- [ ] Cross-check link integrity between frameworks (e.g., IFS, NVC)
- [ ] Tag audit: match frameworks to corresponding lived examples

### 5. Worked Examples Check

- [ ] Validate that examples use current framework references
- [ ] Confirm reflection prompts match updated tags
- [ ] Identify stale or duplicated examples

---

## 🧹 Optional Deep Maintenance

### 6. Visual + Mapping Sync

- [ ] Align `Mapping_Templates/` with active framework use
- [ ] Check that visual tools link back to reflection practices

### 7. Archive & Deprecated Content

- [ ] Move outdated content to `/_Archive`
- [ ] Flag files with legacy formatting or tag mismatch

### 8. Versioning and Changelog

- [ ] Log major edits in `META/Changelog.md`
- [ ] Confirm naming conventions follow semantic clarity

---

## 🧭 Suggested Maintenance Cycle

- [ ] Monthly: Tag audit, prompt testing
- [ ] Quarterly: Framework + script refresh
- [ ] Biannually: Vault structure and index regeneration

> Tip: For automation, link to scripts tagged `#maintenance` or use versioned GitHub releases.
