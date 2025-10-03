---
title: Tagging System Governance
aliases:
  - Tag Master List
  - Indexing Rules
tags:
  - meta
  - governance
  - indexing
type: meta
---

<!-- @format -->

# 🏷️ 01_META_GOVERNANCE_Tagging_System

> **Task:** This document dictates the standardized usage, naming conventions, and hierarchy of all tags used across the entire vault. Consistency in tagging is mandatory for the **[[Utility Prompt - Vault Indexing & Maintenance Audit]]** to function correctly.

---

## I. Tagging Rules (System Integrity)

1.  **Case:** All tags must be written in **lowercase** and **snake_case** (using underscores for spaces, e.g., `core_wound`).
2.  **Exclusivity:** Every file must have exactly **one** primary `type:` tag and at least **one** primary `tags:` category tag (e.g., `analysis` or `framework`).
3.  **No Redundancy:** Avoid creating new tags if an existing one can be accurately applied.

---

## II. Primary Tag Categories

Every file in the vault must use tags drawn from these three categories to ensure proper indexing.

### A. System Tags (The "What Kind of File?")

These tags describe the function and location of the file within the vault's structure.

| Tag              | Usage                                                                                   | Example Files                           |
| :--------------- | :-------------------------------------------------------------------------------------- | :-------------------------------------- |
| `type:meta`      | Used for all governance and indexing documents in the **Meta/** folder.                 | `01_META_GOVERNANCE_Safety_Rules.md`    |
| `type:prompt`    | Used for all files that contain executable AI instructions (Analysis, Master, Utility). | `Analysis Prompt - Core Conflict Cycle` |
| `type:template`  | Used for all standardized input or output containers.                                   | `Conflict Data Logger.md`               |
| `type:framework` | Used for all theoretical knowledge files.                                               | `Polyvagal Theory (PVT).md`             |

### B. Core Framework Tags (The "Knowledge Lens")

These tags link files to the primary theoretical models they utilize.

| Tag          | Framework                         | Usage                                                       |
| :----------- | :-------------------------------- | :---------------------------------------------------------- |
| `ifs`        | Internal Family Systems           | For Parts work, protectors, exiles, and self-energy.        |
| `pvtagent`   | Polyvagal Theory                  | For nervous system states, regulation, and body-based work. |
| `act`        | Acceptance and Commitment Therapy | For values, committed action, and cognitive fusion.         |
| `attachment` | Attachment Theory                 | For security, abandonment, and anxious/avoidant patterns.   |

### C. Relational Topic Tags (The "What is the Problem?")

These tags categorize the file by the specific domain of relational work.

| Tag              | Focus                                                      | Usage                                                     |
| :--------------- | :--------------------------------------------------------- | :-------------------------------------------------------- |
| `trauma`         | Past wounds, re-enactment, systemics, and dissociation.    | `Analysis Prompt - Systemic & Trauma Mapping`             |
| `conflict`       | General fighting, cycle mapping, and basic communication.  | `Conflict Data Logger.md`                                 |
| `core_wound`     | Shame, guilt, fear of abandonment, and deep internal pain. | `Analysis Prompt - Exile/Core Wound Mapping`              |
| `enm`            | Ethical Non-Monogamy and complex structures.               | `Analysis Prompt - Ethical Non-Monogamy (ENM) Assessment` |
| `neurodivergent` | Sensory processing, communication, and social differences. | `Analysis Prompt - Neurodivergent Relationality Audit`    |
| `safety`         | Security checks, de-escalation, and immediate regulation.  | `Analysis Prompt - Dissociation & Fragmentation Check`    |
