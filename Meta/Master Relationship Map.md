---
title: Master Relationship Map
aliases:
  - System Schematic
  - Conceptual Index
tags:
  - meta
  - index
  - flow
type: meta
---

<!-- @format -->

# 🗺️ Master Relationship Map: System Schematic

This map illustrates the operational flow of the entire Relational Analysis Vault,
showing how inputs (Templates) are processed by the Engine (Prompts) to produce
actionable results.

---

## 1. The Core Operational Flow (The Loop)

The system is a closed loop designed to enforce regulation, analysis, and repair.

1.  **Input (Data Collection):** User provides structured data via the **Templates**.
2.  **Triage (Diagnosis):** The **Triage Engine** selects the precise diagnostic tool.
3.  **Analysis (Processing):** The **Analysis Prompts** apply the **Frameworks** (IFS,
    PVT, ACT) to the data.
4.  **Output (Repair/Action):** The **Synthesis Prompt** translates the analysis into a
    final script.
5.  **Audit (Maintenance):** The **Accountability Prompt** checks if the action was
    taken, completing the cycle.

---

## 2. Key Component Dependencies

This table illustrates which parts of the system rely on other parts to function.

| Component                                            | Primary Dependency                                   | Output Feeds Into...                                        |
| :--------------------------------------------------- | :--------------------------------------------------- | :---------------------------------------------------------- |
| **Templates**                                        | N/A (Pure Input)                                     | **Triage Engine** (via Data Logger)                         |
| **Analysis Prompts**                                 | **Frameworks** (IFS, PVT, ACT)                       | **Synthesis Prompt** (for final script generation)          |
| **[[02_MASTER_EXECUTION_Triage_Engine.md]]**         | **Templates** & **Analysis Prompts**                 | **[[Utility Prompt - Safe Relational Feedback Synthesis]]** |
| **Frameworks**                                       | **[[01_META_GOVERNANCE_Knowledge_Vetting.md]]**      | **Analysis Prompts** (The knowledge base)                   |
| **[[02_MASTER_EXECUTION_Accountability_Review.md]]** | **Conflict Repair Template** (to track past actions) | **Maintenance Tasks Template**                              |

---

## 3. The Governance Layer (The Unseen Controllers)

These files control the _logic_ of the map but do not participate in the core analysis
loop. They are the fixed rules.

- **Ethical Constraint:** **[[01_META_GOVERNANCE_Safety_Rules.md]]** (Ensures all
  analysis and output is non-blaming).
- **Information Control:** **[[01_META_GOVERNANCE_Tagging_System.md]]** (Ensures all
  links and connections remain intact).
- **Source Authority:** **[[_REFERENCES_OVERVIEW.md]]** (Verifies the academic integrity
  of the Frameworks).

This map serves as the single source of truth for the system's architecture, completing
your structured documentation.
