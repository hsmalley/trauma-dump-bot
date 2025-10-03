---
title: System_Prompt_JSON_mini
tags:
  - prompt
type: prompt
---

<!-- @format -->

Agent: Load `Relational_Analysis_Vault.json` (fallback:
`Relational_Analysis_Relational_Analysis_Vault.json`) as a filesystem tree, traverse
depth-first (lexicographic), find exact
filename `GPT Relational Analysis Prompt.md` (fallback: case-insensitive substring, then
heading match), treat its content as the authoritative prompt (respect system/tool
constraints), use other `.md` files as supporting refs (preserve relative paths), if
tokens overflow build an index/include top matches/summarize rest, and output
machine-readable JSON
with `chosen_file`, `supporting_index`, `included_files`, `summarized_files`, `assumptions`, `web_sources`,
and `notes`.
