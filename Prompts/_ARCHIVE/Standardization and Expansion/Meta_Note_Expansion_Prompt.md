---
title: Meta Note Expansion Prompt
tags:
  - template
  - meta
type: template
---

<!-- @format -->

## 🧭 Meta Note Standardization Prompt

> **Task:** Clarify and maintain notes in the `Meta/` directory for system coherence.

---

### ✅ Actions:

#### 1. Standardize Format

- Apply structured YAML frontmatter like:
  ```yaml
  ---
  title: Note Title
  tags: meta
  type: meta
  ---
  ```

If frontmatter is missing or incomplete, add or update it accordingly.

#### 2. Use Clear Structure

- Headings like `## Purpose`, `## Usage`, `## Structure`, `## Maintenance`.

#### 3. Add Navigation Links

- Link to index notes (e.g., `[[Index]]`, `[[Vault Guide]]`).

#### 4. Clarify Processes

- Make any instructions or maps actionable and human-readable.

#### 5. Provide User with the files

- Provide the user with updated in valid markdown formatted files
- Bundle those files into a zip named `standardized_meta.zip`

### ⚠️ Constraints

- Preserve code and syntax fidelity inside fenced blocks.
- Meta notes guide vault upkeep—keep them lean, legible, and linked.

---

This prompt ensures meta files are coherent, rich, and cross-linked for vault upkeep
