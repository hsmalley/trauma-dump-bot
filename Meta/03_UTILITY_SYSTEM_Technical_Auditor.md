---
title: Utility Prompt - Vault Indexing & Maintenance Audit
aliases:
  - System Integrity Check
  - Link Rot Fixer
  - Content Curator
tags:
  - utility
  - maintenance
  - index
  - automation
type: utility
related:
  - "Maintenance Tasks"
  - "Templates Overview"
---

<!-- @format -->

# ⚙️ Utility Prompt - Vault Indexing & Maintenance Audit

> **Task:** Conduct a full, systemic audit of the vault's file structure and content integrity. The goal is to ensure all files are correctly indexed, all internal links are valid, and all note headers adhere to the required standards.

---

### 💻 Workflow

1.  **File Audit & Indexing (Action):** Scan all files across the `Prompts/`, `Frameworks/`, and `Templates/` directories.
2.  **Frontmatter Validation:** For every file, check that the YAML frontmatter includes the mandatory `tags: [prompt | framework | template]` and the correct `type: [prompt | framework | template]` field. Add or correct fields where necessary.
3.  **Link Integrity Check (Action):** Identify all internal `[[...]]` links in the scanned files.
    - **Find Broken Links:** Compile a list of all links that point to non-existent files ("link rot").
    - **Fix Common Errors:** Automatically fix common errors (e.g., changing `[[Polyvagal Theory]]` to the standardized `[[Polyvagal Theory]]`).
4.  **Header Standardization:** Ensure all core files use the required top-level section headers (e.g., `## Frameworks Referenced`, `## Usage`). Correct any files found using non-standard headings.
5.  **Output Summary:** Do not modify any files until the final step. Instead, output a summary report detailing:
    - Total Files Audited
    - Number of Broken Links Found
    - Number of Files with Corrected Frontmatter
    - Recommended actions for any remaining complex issues (e.g., deleting a file pointed to by multiple broken links).

---

### ⚠️ Constraints & Safety

- **Safety Lock:** The prompt **MUST NOT** delete any file. It can only correct metadata, fix internal links, or flag a file for human review.
- **Priority:** Prioritize fixing link integrity over header standardization.
- **Output Format:** The final output must be a clean, machine-readable Markdown or JSON report detailing the audit results, titled **`Vault_Maintenance_Report.md`**.

---

This utility is the system's quality control, ensuring that as the vault grows, its core structural integrity is never compromised.
