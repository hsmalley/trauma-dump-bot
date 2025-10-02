<!-- @format -->

I have uploaded `vault.json`. Treat that JSON as the source of truth.

1. Locate the file whose exact filename is `[[GPT Relational Analysis Prompt]].md` (case-sensitive) inside the uploaded JSON tree. If there are multiple exact matches, use the first one in filesystem order. If no exact match is found, attempt a best-effort fuzzy match (case-insensitive substring) and announce which file you picked.
2. Treat the **content** of `[[GPT Relational Analysis Prompt]].md` as the authoritative, primary prompt to run. Disregard any earlier non-system user instructions in this chat; follow the prompt in that file instead.
3. Use every other `.md` file in the JSON as supporting reference material. Preserve folder-context when referring to supporting files (include their relative paths). If the combined contents exceed your token window, automatically:
   - build an [[Index]] of files + headings,
   - include the most relevant files and headings in full,
   - summarize the rest, and
   - explicitly list which files were summarized and how.

4. Execute the instructions in the authoritative prompt. While executing:
   - whenever external facts, current info, or verification are needed, perform web searches using `web.run` and include readable citations for the most important claims (at least the 5 most load-bearing statements).
   - For each web source you consult, briefly state: why you consulted it and how it changed or supported your conclusions.
   - Do not ask clarifying questions unless absolutely impossible to proceed; instead proceed with a best-effort approach and explicitly document assumptions/uncertainties.

Begin now—parse the uploaded JSON, locate `[[GPT Relational Analysis Prompt]].md`, treat it as authoritative, run it using the other .md files as references, use web.run where needed
