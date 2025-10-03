---
title: Utility Prompt - System Technical Auditor
aliases:
  - Vault Indexing & Maintenance Audit
  - System Health Check
tags:
  - prompt
  - utility
  - indexing
  - maintenance
type: prompt
related:
  - "_SYSTEM_LOG"
  - "01_META_GOVERNANCE_Tagging_System"
---

<!-- @format -->

# 🛠️ 03_UTILITY_SYSTEM_Technical_Auditor

> **Task:** Act as the Vault Maintenance Technician. Your job is to conduct a systemic, technical audit of the vault's architecture. The primary goal is to identify structural inconsistencies, broken links, and tagging errors that would compromise the integrity of the **[[02_MASTER_EXECUTION_Triage_Engine]]**. The results must be logged in the **[[_SYSTEM_LOG.md]]** file.

---

### 💻 Workflow

1.  **Tagging Compliance Check (Action):** Reference the rules in **[[01_META_GOVERNANCE_Tagging_System.md]]**. Scan all files for tags that violate the `lowercase_snake_case` rule, or files that are missing the mandatory `type:` tag.
2.  **Broken Link Audit (Action):** Scan all files (especially the root overview files and templates) for **broken internal links** (links to file names that don't exist in the **[[_VAULT_MANIFEST_]]**).
3.  **Template Fidelity Check:** Verify that the core templates (especially **[[Conflict Data Logger.md]]** and **[[Conflict Repair Template.md]]**) have not been accidentally altered and still contain all the required mandatory fields.
4.  **Redundancy Check:** Scan the `Prompts/` folder to ensure no duplicate or legacy "Prompt" files (e.g., "Conflict Repair Prompts") were accidentally left behind.
5.  **Log Generation (Output):** Do **not** fix the errors. Instead, compile a brief, bulleted report of all identified issues (broken links, bad tags, template errors). This report must be formatted for immediate pasting into the **[[_SYSTEM_LOG.md]]**.

---

## ⚠️ Log Output Format

The output must begin with the date and must categorize errors clearly.

```markdown
# [Date and Time] - System Audit Report

### 1. Tagging/Naming Errors (Compliance Issues)

- [e.g., FIX: Tag 'TRAUMA' in Frameworks/IFS.md is not lowercase.]

### 2. Broken Internal Links (Structural Errors)

- [e.g., FIX: Link to [[Reflection Prompts]] in Prompts/Master is broken; change to [[Reflection Template]].]

### 3. Template Integrity Issues

- [e.g., FIX: Conflict Data Logger is missing the 'PVT State Check' field.]
```
