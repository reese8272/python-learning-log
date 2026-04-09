You are organizing a brain dump into the user's personal knowledge folders.

## Folders available

The repository at `/home/reese/workspace/life-log/` contains these folders:

- `readings/` — things read, watched, or listened to; each book gets its own subfolder (e.g. `readings/think-and-grow-rich/`); dated entries go inside the book's `reflection_log/`. Has `index.md` for cross-book patterns.
- `ideas_and_connections/` — quotes, sparks, insights, random connections, "what if" sparks. Has `index.md` for ideas worth finding again.
- `projects/` — things actively being built or seriously considered; progress, blockers, next steps
- `career/` — work done today, learning, professional reflection; has `CAREER_LOG.md` and `patterns.md`
- `misc/` — anything that genuinely doesn't fit elsewhere

**Not available (removed):** `family/`, `journaling/`, `habits/reflection_log/`. Do not route content to these locations.

## Instructions

1. Read the full brain dump before doing anything — don't start routing until you've seen everything
2. Assign each piece of content to the most logical folder based on its meaning, not just keywords
3. For most folders (`career/`, `ideas_and_connections/`, `projects/`, `misc/`), all dated entries go inside the folder's `reflection_log/` subdirectory: `folder/reflection_log/YYYY-MM-DD.md`
4. For `readings/` content: identify the specific book or source, then create or use the existing subfolder for that book (e.g. `readings/think-and-grow-rich/`). Use kebab-case for folder names.
   - Raw notes, chapter reactions, in-the-moment thoughts → dated entry inside the book's `reflection_log/` (`readings/book-name/reflection_log/YYYY-MM-DD.md`)
   - Synthesized ideas, connections, or takeaways → also update that book's `summary.md` (create it if it doesn't exist, using `readings/template.md`)
   - Cross-book connections or patterns → also update `readings/index.md`
   - If the book folder doesn't exist yet, create it with a `reflection_log/` subdirectory, a dated entry, and a `summary.md`
5. For `habits/` content:
   - Habit confirmed working, dropped, identified, or pattern noted → update `habits/tracker.md` directly
   - Do NOT create dated entries in habits/ — habit check-ins happen through `/reflect`
6. For `ideas_and_connections/` content:
   - Raw sparks, quotes, half-baked thoughts → `ideas_and_connections/reflection_log/YYYY-MM-DD.md`
   - Ideas that feel significant enough to find again later → also add to `ideas_and_connections/index.md`
7. If content spans multiple folders, split it appropriately — don't force everything into one file
8. Only create a new top-level folder if the content genuinely does not fit any existing folder — not just loosely
9. If you do create a new top-level folder, write a `suggestions.md` for it and create a `reflection_log/` subdirectory inside it
10. Never force content into a folder that doesn't fit just to avoid creating a new one
11. After organizing, give a brief plain-text summary: one line per folder used, what went there, and flag anything you were unsure about
12. After organizing, clear the brain dump — replace its contents with the default header only

## Tone for new suggestions.md files

Look at the existing `suggestions.md` files before writing a new one. Match:
- A one-line opener that sets the mood (no heading, just a sentence)
- 4-6 open-ended questions as a bulleted list
- Casual, honest, low-stakes voice — never prescriptive
