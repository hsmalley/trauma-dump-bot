---
title: Reference Note Expansion Prompt
tags: [template, reference]
type: template
---

<!-- @format -->

## 🛠 Reference Note Expansion & Standardization Prompt

> **Task:** Standardize and enrich all notes in the `References/` directory according to vault conventions.

---

### ✅ Actions:

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
- Use consistent headings:
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
  - e.g., `[[Attachment Theory]]`, `[[Reflection Template]]`, `[[GPT Relational Analysis Prompt]]`

#### 4. Citations

- End each note with:

  ```markdown
  ## Citations

  - Author, A. (Year). _Title of Book_. Publisher.
  - Author, B. & Author, C. (Year). _Article Title_. _Journal_, Volume(Issue), pages.
  ```

#### 5. Optional Enhancements

- Add more precise tags if needed (e.g., `reading`, `glossary`, `case`, `index`)
- Include a `## See Also` section to connect to relevant files across the vault

#### 6. Provide User with the files

- Provide the user with updated markdown formatted files
- Bundle those files into a zip

---

This prompt supports consistent formatting and educational richness across all reference material.
