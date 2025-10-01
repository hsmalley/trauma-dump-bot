---
title: Framework Note Expansion Prompt
tags: [template, framework]
type: template
---

<!-- @format -->

## 🧱 Framework Note Expansion & Standardization Prompt

> **Task:** Standardize and enrich all notes in the `Frameworks/` directory based on the vault’s conventions.

---

### ✅ Actions:

#### 1. Standardize Format

- Apply structured YAML frontmatter:
  ```yaml
  ---
  title: Full Framework Name (ACRONYM)
  tags: [framework, relevant-tags]
  aliases: [ACRONYM, Alternate Phrasings]
  type: framework
  ---
  ```
- Use consistent markdown headings:
  - `## Overview`
  - `## Core Concepts`
  - `## Applications`
  - `## Best Practices & Considerations`
  - `## Integration & Related Models`
  - `## Example Prompts or Practices`
  - `## Citations`

#### 2. Expand Content

- Provide context (origin, developer, purpose).
- Elaborate on 3–5 key concepts, using subheadings if helpful.
- Note where it overlaps or contrasts with other frameworks.
- Include clinical/relational relevance.
- Use web.run if needed

#### 3. Improve Cross-Linking

- Link to related notes using Obsidian’s double-bracket style:
  - e.g., `[[Polyvagal Theory]]`, `[[Consent Culture]]`, `[[Reflection Prompts]]`

#### 4. Cite Sources

- Include a `## Citations` section with APA-style formatting:
  ```markdown
  - Schwartz, R. (1995). _Internal Family Systems Therapy_. Guilford Press.
  - Porges, S. W. (2011). _The Polyvagal Theory_. Norton.
  ```

#### 5. Optional Enhancements

- Add tentative limitations or assumptions of the model.
- Offer 2–3 starter prompts for applying the model.
- Consider whether this framework is best used individually, relationally, or systemically.

#### 6. Provide User with the files

- Provide the user with updated markdown formatted files
- Bundle those files into a zip

---

This prompt ensures framework notes are coherent, rich, and cross-linked for analysis and learning.
