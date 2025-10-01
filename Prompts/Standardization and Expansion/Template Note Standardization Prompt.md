---
title: Template Note Standardization Prompt
tags: [template, meta]
type: template
---

<!-- @format -->

## 🧩 Template Note Standardization Prompt

> **Objective:** Normalize all files in the `Templates/` directory to conform to a consistent format, improve usability, and enable reliable internal linking.

---

### 🔧 Required Actions

#### 1. Standardize Format

- Apply structured YAML frontmatter:
- include:

```
---
title: [Template Name]         # Human-readable title of the template
tags: [template]               # Must include the 'template'
tag type: template                 # Static value for classification
---
```

If frontmatter is missing or incomplete, add or update it accordingly.

---

#### 2. **Embed Contextual Links**

Where applicable, insert Markdown links to related:

- Prompts
- Frameworks
- Workflows

Links must be relative or Obsidian-compatible (e.g., `[[Frameworks/NVC]]`).

---

#### 3. **Output and Delivery**

- Return each revised file in valid Markdown syntax.
- Package all updated files into a `.zip` archive named `standardized_templates.zip`.

---

### ⚠️ Constraints

- Do not modify template content beyond formatting.
- Preserve code and syntax fidelity inside fenced blocks.
- Keep each file minimal and plug-and-play ready.
