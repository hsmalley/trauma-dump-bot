---
title: Framework Note Expansion Prompt
tags:
  - template
  - framework
  - prompt
type: template
---

<!-- @format -->

## 🧱 Analysis Expansion & Standardization Prompt

> **Task:** Standardize and enrich all notes that start with `Analysis Prompt` in the
> `Prompts/` directory based on the vault’s conventions.

---

### ✅ Actions:

#### 1. Standardize Format

- Apply structured YAML frontmatter, for exampe:
  ```yaml
  ---
  title: Analysis Prompt - <Analysis Name>
  aliases:
    - Alternate Phrasings
  tags:
    - prompt # MUST INCLUDE
    - relevant-tags
  type: prompt # Static value for classification
  ---
  ```

If frontmatter is missing or incomplete, add or update it accordingly.

Use consistent markdown headings:

- `# Prompt`
- `# Frameworks Referenced`
- `# Use Cases`

#### 2. Expand Content

- Provide a detailed GPT analysis prompt in `# Prompt section`
- Update or rewrite prompt if needed

#### 3. Frameworks Referenced

- Improve Cross-Linking
- Update Frameworks Referenced to include additional or missed frameworks from
  `Frameworks/` folder.
- Link to related notes using Obsidian’s double-bracket style:
  - e.g., `[[Polyvagal Theory]]`, `[[Consent Culture]]`, `[[Reflection Prompts]]`
  - Consider what frameworks may be most useful in the context of this prompt, sort them
    at the top of the list, sort the rest of the list in A-Z style

#### 4. Use Cases

- Update when to apply this prompt, use evidence based suggestions when considering this

#### 5. Cite Sources

- Include a `## Citations` section with APA-style formatting:
  ```markdown
  - Schwartz, R. (1995). _Internal Family Systems Therapy_. Guilford Press.
  - Porges, S. W. (2011). _The Polyvagal Theory_. Norton.
  ```

#### 5. Optional Enhancements

- Add tentative limitations or assumptions of the model.
- Consider whether this framework is best used individually, relationally, or
  systemically.
- When possible provide additional frameworks in the `# Frameworks Referenced` section
  that are not in the `/Framworks` folder but could be helpful and fit the theme of this
  model.

#### 6. Provide User with the files

- Provide the user with updated in valid markdown formatted files
- Bundle those files into a zip named `standardized_frameworks.zip`

### ⚠️ Constraints

- Preserve code and syntax fidelity inside fenced blocks.
- Keep each file plug-and-play ready.
- Keep the tone of the prompt friendly and educational
- Use plain language were possible, use clinical language when needed.
- Use web.run when needed
- If there are ethical concerns create/update an `# ⚠️ Ethical Concerns` section at the
  **BOTTOM** of the note

---

This prompt ensures Analysis Prompts are coherent, rich, and cross-linked
