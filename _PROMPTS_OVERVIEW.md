---
title: Prompts Overview and Functional Guide
aliases:
  - Prompts Map
  - Triage Flow
tags:
  - meta
  - prompt
  - index
type: meta
---

<!-- @format -->

# ⚙️ Prompts Overview and Functional Guide

This guide maps the complete prompt architecture of the vault, organized by **function** in the relational workflow. Use this guide to quickly select the right tool based on your immediate need.

---

## I. Governance & System Management (Meta & Master Prompts)

These prompts define the ethical rules and control the overall workflow of the vault. They are executed by the system, not directly by the user.

| Prompt Title                                      | Primary Function                                                                              | Workflow Stage        |
| :------------------------------------------------ | :-------------------------------------------------------------------------------------------- | :-------------------- |
| **[[02_MASTER_EXECUTION_Triage_Engine]]**         | **Master Triage.** Selects and runs the single, most appropriate specialized analysis prompt. | Execution Start       |
| **[[01_META_GOVERNANCE_Safety_Rules]]**           | **Ethical Governor.** Ensures all output is trauma-informed and non-judgmental.               | Continuous Constraint |
| **[[02_MASTER_EXECUTION_Accountability_Review]]** | **Long-Term Health.** Forces periodic review of skill integration and assigned actions.       | Maintenance/Review    |

---

## II. Diagnostic Tools (Specialized Analysis Prompts)

These twelve prompts are the analytical engine. They are run by the **Triage Engine** to diagnose a specific, narrow problem.

| Prompt Title                                                    | Focus Area                                                                             | When to Use                                                        |
| :-------------------------------------------------------------- | :------------------------------------------------------------------------------------- | :----------------------------------------------------------------- |
| **[[Analysis Prompt - Core Conflict Cycle]]**                   | Basic "Pursue/Withdraw" patterns and circular dynamics.                                | Initial diagnosis of recurring conflict.                           |
| **[[Analysis Prompt - Attachment Cycle Mapping]]**              | Conflict rooted in core security/abandonment fears (Anxious/Avoidant).                 | When the argument is about closeness or space.                     |
| **[[Analysis Prompt - Multi-Modal Conflict Assessment]]**       | Comprehensive deep-dive covering Gottman, PVT, and NVC lenses simultaneously.          | When the conflict is complex and confusing.                        |
| **[[Analysis Prompt - Systemic & Trauma Mapping]]**             | Conflict rooted in family history, past trauma, or external pressures.                 | When reactions are disproportionate to the current event.          |
| **[[Analysis Prompt - Boundary & Accountability Audit]]**       | Failures in structural rules, consent, and follow-through.                             | When the same broken promise keeps causing pain.                   |
| **[[Analysis Prompt - Linguistic & Cognitive Audit]]**          | Jargon, catastrophizing, mind-reading, and other cognitive distortions.                | When the _words_ and _thoughts_ are the main source of escalation. |
| **[[Analysis Prompt - Future-Focus & Relational Vision]]**      | Disagreements on long-term goals, direction, and feasibility.                          | When the couple is "stuck" or lacks shared purpose.                |
| **[[Analysis Prompt - Values & Goals Alignment (ACT Lens)]]**   | Misalignment between actions, conflicts, and stated core values.                       | When behavior contradicts stated desires.                          |
| **[[Analysis Prompt - Neurodivergent Relationality Audit]]**    | Conflicts caused by differences in social processing, energy, and communication needs. | When one or both partners are neurodivergent.                      |
| **[[Analysis Prompt - Repair Attempts]]**                       | Quality and effectiveness of apologies, de-escalation, and post-conflict repair.       | When "I'm sorry" doesn't fix the rupture.                          |
| **[[Analysis Prompt - Kink & Power Dynamics Assessment]]**      | Conflicts involving negotiation, aftercare, safety, and power exchange.                | For dynamics involving kink or structured power dynamics.          |
| **[[Analysis Prompt - Ethical Non-Monogamy (ENM) Assessment]]** | Conflicts involving third parties, jealousy, structure, and time management.           | For open, polyamorous, or swinging relationships.                  |

---

## III. Operational Tools (Utility Prompts)

These prompts are used directly by the user or the system to manage content, practice skills, and deliver feedback safely.

| Prompt Title                                                | Primary Function                                                                               | Output/Action           |
| :---------------------------------------------------------- | :--------------------------------------------------------------------------------------------- | :---------------------- |
| **[[Utility Prompt - Safe Relational Feedback Synthesis]]** | **Safety Filter.** Translates complex analysis into a simple, non-blaming script for the user. | 3-Part Repair Script    |
| **[[Utility Prompt - Structured Reflection Guide]]**        | **Self-Work Guide.** Walks the user through internal processing using IFS/ACT/PVT.             | Structured Reflection   |
| **[[Utility Prompt - Dynamic Role-Play & Skill Practice]]** | **Rehearsal Tool.** System acts as a defensive partner to practice scripts and de-escalation.  | Iterative Role-Play     |
| **[[Utility Prompt - Framework Content Generator]]**        | **Knowledge Builder.** Automates the creation of new Framework files.                          | Vetted Markdown File    |
| **[[Utility Prompt - Glossary Generator]]**                 | **Reference Builder.** Compiles technical terms into a single lookup file.                     | `_GLOSSARY_OF_TERMS.md` |
| **[[Meta/03_UTILITY_SYSTEM_Technical_Auditor]]**            | **System Integrity.** Audits links, tags, and structure for errors.                            | Maintenance Report      |
