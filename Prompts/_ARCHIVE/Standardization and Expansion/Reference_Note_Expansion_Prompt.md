---
title: "Reference Note Expansion & Standardization"
aliases:
  - "Reference Standardization"
  - "Ref Note Maintenance"
tags:
  - utility
  - prompt
  - template
  - maintenance
  - standardization
type: prompt
related:
  - "Meta_Note_Expansion_Prompt"
  - "Prompt_Note_Expansion_Prompt"
---

<!-- @format -->

## 🛠 Reference Note Expansion & Standardization Prompt

> **Task:** Standardize and enrich all notes in the `References/` directory according to
> vault conventions.

---

### ✅ Actions

#### 1. Standardize Format

- Apply structured YAML frontmatter
- include:

  ```yaml
  ---
  title: [Exact Note Title]
  tags: [reference]
  type: reference
  ---
  ```

- Use consistent headings like:
    - `## Overview`
    - `## Key Entries` (or `## Key Concepts`)
    - `## Relevance`
    - `## See Also`

#### 2. Expand Content

- For **reading lists, bibliographies, glossaries**:
    - Add short summaries or rationales for each item.
    - Apply APA-style citations where possible.
    - Note which frameworks/concepts each item supports.

- For **example conversations or case notes**:
    - Provide relational context or character labels.
    - Annotate with themes, nervous system states, or IFS parts.
    - Highlight moments of conflict, bids, or repair.

- Use web.run if needed

#### 3. Link Cross-References

- Use Obsidian-style wikilinks:
    - e.g., `[[Attachment Theory]]`, `[[Reflection Template]]`,
    `[[GPT Relational Analysis Prompt]]`

#### 4. Citations

- End each note with a `## Citations` section with APA-style formatting:

  ```markdown
  - Schwartz, R. (1995). _Internal Family Systems Therapy_. Guilford Press.
  - Porges, S. W. (2011). _The Polyvagal Theory_. Norton.
  ```

#### 5. Optional Enhancements

- Add more precise tags if needed (e.g., `reading`, `glossary`, `case`, `index`)
- Include a `## See Also` section to connect to relevant files across the vault

#### 6. Provide User with the files

- Provide the user with updated markdown formatted files
- Bundle those files into a zip

---

This prompt supports consistent formatting and educational richness across all reference
material.
