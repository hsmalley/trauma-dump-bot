---
title: Framework Note Expansion Prompt
tags:
  - template
  - framework
type: template
---

<!-- @format -->

## 🧱 Framework Note Expansion & Standardization Prompt

> **Task:** Standardize and enrich all notes in the `Frameworks/` directory based on the vault’s conventions.

---

### ✅ Actions:

#### 1. Standardize Format

- Apply structured YAML frontmatter, for exampe:
  ```yaml
  ---
  title: Full Framework Name (ACRONYM)
  aliases:
    - ACRONYM
    - Alternate Phrasings
  tags:
    - framework # MUST INCLUDE
    - reference
    - relevant-tags
  type: framework # Static value for classification
  ---
  ```

If frontmatter is missing or incomplete, add or update it accordingly.

- Use consistent markdown headings for example:
  - `## Overview`
  - `## Core`
  - `## Key Elements`
  - `## Core Concepts`
  - `## Core Traits and Themes (Trauma Lens)`
  - `## Definition and Core Traits (Clinical + Contextual)`
  - `## Lived Experience`
  - `## Common Misconceptions`
  - `## Misunderstandings and Relational Reframes`
  - `## Nervous System`
  - `## Nervous System + Parts Work Lens`
  - `## Attachment`
  - `## Attachment & Protest`
  - `## Attachment and Relational Themes`
  - `## Applications`
  - `## Challenges and Strengths`
  - `## Strategies and Support Practices`
  - `## Best Practices & Considerations`
  - `## Key Question Types`
  - `## Reflection Prompts`
  - `## Example Prompts or Practices`
  - `## Clinical Overview (DSM-5 Criteria)`
  - `## Clinical Overview (ICD Criteria)`
  - `## Integration & Related Models`
  - `## Related Frameworks`
  - `## Further Reading`
  - `## Cautions & Ethics`
  - `## Citations`
  -

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
- Offer 3–4 starter prompts for applying the model.
- Consider whether this framework is best used individually, relationally, or systemically.

#### 6. Provide User with the files

- Provide the user with updated in valid markdown formatted files
- Bundle those files into a zip named `standardized_frameworks.zip`

### ⚠️ Constraints

- Preserve code and syntax fidelity inside fenced blocks.
- Keep each file plug-and-play ready.

---

This prompt ensures framework are coherent, rich, and cross-linked for analysis and learning.
