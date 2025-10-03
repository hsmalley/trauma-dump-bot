---
title: Add Topic Template
tags:
  - template
  - framework
type: template
---

<!-- @format -->

````
Generate a framework notes .md file for "<TOPIC>".

Requirements:
- Output ONLY a single fenced code block with language tag 'markdown' (i.e. ```markdown ... ```), and nothing else outside that block.
- The fenced markdown must contain a complete Markdown file with YAML frontmatter including these fields: title, description, author ("GPT Relational Analysis Triage Engine"), created (YYYY-MM-DD), updated (YYYY-MM-DD), version (1.0.0), tags (list), audience (list), license, schema, filename.
- Set created and updated to today's date.
- No HTML, repo-ready Markdown only.
- Output nothing outside the fenced code block.
````

---

````prompt
Generate a framework notes .md file for "<TOPIC>". Follow the full prompt template and output only the Markdown file wrapped inside a fenced code block. Use ```markdown as the opening fence and ``` as the closing fence. Do not output any text outside the code block.
````

````prompt
Generate a framework notes .md file for "<TOPIC>".

Requirements:
- Output ONLY a fenced code block containing the full Markdown file (no extra commentary, no explanations).
- Use triple backticks with language tag 'markdown' (i.e. ```markdown) at the start and triple backticks to end.
- Inside the code block include YAML frontmatter with these fields: title, description, author ("GPT Relational Analysis Triage Engine"), created (YYYY-MM-DD), updated (YYYY-MM-DD), version, tags (list), audience (list), license, schema, filename. Set created and updated to today's date.
- Keep the Markdown repo-ready (no HTML). The assistant must output nothing except the single fenced code block.
````

```prompt
SYSTEM RULE: Whenever the user requests "Generate a framework notes .md file for <TOPIC>", produce a single fenced code block labeled 'markdown' that contains the complete Markdown file and nothing else. The output must include YAML frontmatter (title, description, author, created, updated, version, tags, audience, license, schema, filename). Use today's date for created/updated. No text outside the code block.
```

```prompt
Wrap the output in a triple-tilde fence labeled markdown (~~~markdown ... ~~~) and output nothing else.
```
