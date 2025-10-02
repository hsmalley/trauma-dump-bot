<!-- @format -->

# 📂 Obsidian Vault Build Prompt

I need your help building an **Obsidian vault**.  
I will upload my current files as a starting point.

## ✅ Tasks

1. **Analyze Current Content**
   - Review the uploaded notes and structure.
   - Identify gaps, inconsistencies, or missing files.

2. **Generate Missing Files**
   - Create all missing notes, frameworks, and templates.
   - Reference the provided guidance prompt to ensure accuracy.
   - Fill in relevant data so the vault is self-contained and useful.

3. **Standardize & Optimize**
   - Ensure consistent formatting across all notes.
   - Apply the chosen metadata, tags, and structure.
   - Link related notes together with Obsidian-style `[[wikilinks]]`.
   - Use headers, bullet points, and callouts for clarity.

4. **Package the Vault**
   - Deliver a **ready-to-import ZIP archive**.
   - Final structure should include all framework notes, templates, and references.

---

## 📝 Style & Structure Requirements

- **Frontmatter (YAML)**  
   Each note must start with YAML frontmatter:

  ```yaml
  ---
  title: <Descriptive Title>
  tags: [tag1, tag2, …]
  type: [prompt|template|reference|framework|note]
  ---
  ```

- **File Naming**
  - Use `Title Case` for filenames (e.g., `Polyvagal Theory.md`).
  - Keep filenames short, descriptive, and aligned with note titles.
- **Tags & Metadata**
  - Use consistent tags for frameworks, prompts, references, and templates.
  - Example tags: `framework`, `analysis`, `prompt`, `template`.
- **Note Linking**
  - Use `[[Note Title]]` for internal links.
  - Connect frameworks ↔ prompts ↔ references ↔ examples where possible.
- **Folder Hierarchy**

  ```
  📂 VaultRoot
  ├─ 📂 Templates
  ├─ 📂 Frameworks
  ├─ 📂 References
  ├─ 📂 Prompts
  ├─ 📂 Meta
  ├─ Index.md
  ```

---

## 🧩 Core Template Set

### Framework Reference Template

```markdown
---
title: <Framework Name (ACRONYM)>
tags:
  - framework
  - reference
  - relevant-tags
created: 2025-01-01
updated: 2025-01-01
type: framework
---

# <Framework Name>

## Overview

Brief description of the framework.

## Core Principles

- Principle 1
- Principle 2
- Principle 3

## Application

- How it can be used in relational/analysis contexts.

## Related

- [[Other Framework]]
- [[Prompt]]
```

---

### Analysis Prompt Template

```markdown
---
title: Analysis Prompt - <Topic>
tags: [prompt, analysis]
created: 2025-09-30
updated: 2025-09-30
type: prompt
---

# Prompt

<Insert detailed GPT analysis prompt here.>

# Frameworks Referenced

- [[Polyvagal Theory]]
- [[Internal Family Systems (IFS)]]
- [[Nonviolent Communication (NVC)]]

# Use Cases

- When to apply this prompt.
```
