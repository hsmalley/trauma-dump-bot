---
title: Utility Prompt - Framework Content Generator
aliases:
  - Framework Creation Engine
  - Template Populator
  - Research Synthesis Tool
tags:
  - utility
  - generation
  - framework
  - automation
type: utility
related:
  - "Framework Reference Template"
  - "Maintenance Tasks"
---

<!-- @format -->

# ⚙️ Utility Prompt - Framework Content Generator

> **Task:** Synthesize raw source material (e.g., research summary, web article, book
> notes) on a new psychological framework and accurately populate all required fields
> within the **[[Theory Reference Sheet]]**. The output must be a valid, standalone
> Markdown file, ready to be saved in the `Frameworks/` directory.

---

### 💻 Workflow

1.  **Ingest Source Material:** Accept and process the raw research data and the **name
    of the Framework** (e.g., "Somatic Experiencing," "Solution-Focused Brief Therapy").
2.  **Structural Initialization:** Begin the file by inserting the complete **YAML
    Frontmatter** and Markdown headings from the **[[Theory Reference Sheet]]**.
3.  **Content Synthesis & Mapping:** Fill each section of the template by synthesizing
    the source material, ensuring the following critical relational elements are
    included:
    - **Neurodivergent Considerations:** Explicitly state how the framework's core
      tenets (e.g., _Cognitive Behavioral Therapy_'s emphasis on thought-stopping) might
      negatively impact **Neurodivergent** processing (e.g., increased masking or
      shame).
    - **PVT/IFS Alignment:** Clearly map the framework's concepts to the vault's core
      relational frameworks:
      - **PVT Lens:** How does the framework affect the **Sympathetic** or **Ventral
        Vagal** state?
      - **IFS Lens:** How does the framework interact with **Protectors** and
        **Exiles**?
    - **Relational Impact:** Specifically address how the framework's practices play out
      in a **dyadic (two-person) context**, not just individually.

4.  **Citations (Action):** Identify the primary academic sources for the framework and
    format them accurately in the final `## Citations` section.

5.  **Clean Output:** Ensure the final output contains **no instructional text, no
    placeholders, and no remaining `[... fill in ...]` prompts** from the template.
6.  - **Do not include human-readable label prefixes inside frontmatter values.**  
      ❌ Bad: `source: Synthesis: kink scholarship, sexual-health guidance`  
      ✅ Good: `source: kink scholarship, sexual-health guidance`

---

### ⚠️ Constraints & Validation

- **Integrity Check:** The final output **MUST** conform to the structural rules of the
  **[[Theory Reference Sheet]]** (e.g., it must have the
  `## Traits and Lived Experience` section).
- **Tone:** The synthesized content must be **educational, trauma-informed, and
  non-pathologizing**.
- **Completeness:** If any section cannot be fully populated from the source material, a
  placeholder must be used: `[NOTE: More research needed on <Section Name>]`—but this
  should be avoided when possible.
- **Final Delivery:** The output is a single, clean Markdown file.

---

This utility ensures every framework is fully **vetted, relational-aware, and
immediately integrated** into the vault's diagnostic and therapeutic capabilities.
