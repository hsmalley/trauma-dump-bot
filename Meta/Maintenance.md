---
title: Maintenance
tags:
  - meta
type: meta
---

<!-- @format -->

# 🧰 Vault Maintenance

This note collects quick commands, checklists, and tips to keep the vault healthy: validated links, consistent metadata, and working diagrams.

---

## 🚀 Quick Commands

### Validate links & titles

```bash
python Meta/Tools/validate_vault.py .
```

- Reports **broken wikilinks** and **duplicate titles**.
- Resolves references by **filename** and `aliases:` frontmatter.

### (Optional) Rebuild the Master Map

> The master map is generated from real links in notes. If you add many new items and want to refresh the map, re-run the **“Master Map”** update steps:

1. Ensure new notes link frameworks via markdown [[Framework Name (ACRONYM)]]

2. Run the “Maintenance → Master Map: Refresh” checklist below (manual update steps).

---

## ✅ Regular Maintenance Checklist

- [ ] **Validate**: Run the validator; fix any `broken_links` or `duplicate_titles` it reports.
- [ ] **Aliases**: If you add a framework with an acronym, add `aliases:` (e.g., `NVC`, `EFT`, `IFS`) to the canonical note (see template below).
- [ ] **Frontmatter**: Ensure each note has block-style `tags:` and a `type:` matching its folder (`framework`, `prompt`, `reference`, `template`, `meta`, or `note`).
- [ ] **Mermaid**: Open Mermaid notes; confirm they render in Obsidian (IDs should be simple, no spaces; use classDefs sparingly; wrap in triple backticks).

---

## 🏷 Aliases Template (for frameworks)

Add aliases to the canonical framework note (keep filename stable with acronym):

```yaml
---
title: Nonviolent Communication (NVC)
tags:
  - framework
aliases:
  - Nonviolent Communication
  - NVC
type: framework
---
```

> Use the same pattern for **Internal Family Systems (IFS)**, **Emotionally Focused Therapy (EFT)**, etc.

---

## 🧩 Master Map: Refresh

The master map is in **Meta/Master Relationship Map.md** and is generated based on links from prompts/references/analyses to frameworks.

1. Ensure new notes include concrete links like `[[Polyvagal Theory]]`, `[[Internal Family Systems (IFS)]]`.
2. In large batches of changes, re-run your local generation script (or request the assistant to rebuild the map):
   - Confirm Mermaid block syntax:
     `
     `mermaid
     graph TD
     F_Framework --> P_Prompt

````
     ```
   - Node IDs: use only letters, numbers, underscores.
3. Open the map in Obsidian and confirm it renders.

---

## 🛠 Fixing Common Issues

### Broken links
- Replace deleted/renamed targets with canonical titles (prefer acronym forms).
- If two notes refer to the same concept with different names, merge content into the canonical file and add `aliases:` to it.

### Duplicate titles
- Keep the canonical acronym version as the primary title.
- Update or remove the duplicate; move any unique content into a `## Additional Notes (Merged)` section on the canonical note.

### Mermaid errors
- Use code fences with the `mermaid` language tag.
- Simplify IDs: `F_Polyvagal_Theory` instead of names with spaces.
- Place `classDef` lines before nodes/edges or at top of the graph block.

---

## 📎 Reference Indexes

- [[Vault Guide]]
- [[Master Relationship Map]]
- [[Workflow Map]]
- [[Vault Graph Overview]]
- [[Worked Analyses]]
````
