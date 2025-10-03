---
title: Utility Prompt - Reference Compiler
aliases:
  - Master Bibliography Generator
  - Source Indexer
tags:
  - utility
  - reference
  - documentation
type: utility
related:
  - "Framework Reference Template"
  - "Maintenance Tasks"
---

<!-- @format -->

# 📜 Utility Prompt - Reference Compiler

> **Task:** Conduct a full vault scan to identify and compile all citations listed in
> the `## Citations` section of all Framework and Analysis Prompt files. The goal is to
> generate a clean, comprehensive **Master Bibliography** file
> (`_REFERENCES_OVERVIEW.md`).

---

### 💻 Workflow

1. **Source Identification (Action):** Scan all files in the `Frameworks/` and
   `Prompts/Analysis/` directories. Use `web.run` only when vault lacks context or
   external validation is required
2. **Extraction:** Extract all entries found within the `## Citations` sections of the
   files.
3. **Deduplication:** Remove all duplicate entries to create a unique list of sources.
4. **Categorization:** Organize the final list into relevant thematic categories to
   enhance readability (e.g., Core Theories, Specialized Dynamics, Trauma/ACT).
5. **Output Formatting:** Format the final output alphabetically within each category,
   adhering to a consistent citation style (e.g., APA or a simple Author/Year format).

### ⚠️ Constraint

- The generated file must be titled **`_REFERENCES_OVERVIEW.md`** and structured for
  deployment in the vault's root folder.

---

This final prompt ensures the knowledge base is transparent, verifiable, and provides a
clear path for users who wish to research the source material.
