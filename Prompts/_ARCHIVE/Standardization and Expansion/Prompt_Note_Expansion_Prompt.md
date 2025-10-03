---
title: Prompt Note Expansion Prompt
tags:
  - template
  - prompt
type: template
---

<!-- @format -->

## 🎯 Prompt Note Expansion & Standardization

> **Task:** Standardize and enrich notes in the `Prompts/` directory using vault-wide
> clarity and relational insight standards.

---

### ✅ Actions:

#### 1. Standardize Format

- Apply structured YAML frontmatter
- Add frontmatter:
  ```yaml
  ---
  title: [Prompt Name]
  tags: [prompt]
  type: prompt
  ---
  ```
- Use sections like:
  - `## Prompt`
  - `## Frameworks Referenced`
  - `## Use Cases`
  - `## Workflow`

#### 2. Expand Workflow

- Break the analysis task into clear bullet steps.
- Add sub-steps where needed (e.g., “spot protest → map to style”).

#### 3. Improve Framework Referencing

- Link each framework used via `[[...]]` and describe what it adds.

#### 4. Add Examples (if appropriate)

- Include sample use case or sentence stem showing the prompt in action.

#### 5. Provide User with the files

- Provide the user with updated markdown formatted files
- Bundle those files into a zip

#### 6. Explicitly Define Output Constraints and Failure Modes

- State the exact **required output format** (e.g., JSON schema, specific Markdown
  headings).
- Add a constraint instructing the model on **fallback behavior** if critical input
  fields are missing (e.g., “If `conversation` is empty, return only a JSON object with
  `status: 'error'` and a human-readable explanation in the `notes` field.”).

---

This keeps prompts clear, structured, and reference-rich for guided analysis.
