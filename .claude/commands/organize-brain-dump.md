You are organizing a brain dump into the user's personal knowledge folders.

## Folders available

The repository at `/home/reese/workspace/python-learning-log/` contains these folders:

- `readings/` — things read, watched, or listened to; each book gets its own subfolder (e.g. `readings/think-and-grow-rich/`); dated entries go flat inside the book folder
- `ideas_and_connections/` — half-baked thoughts, things bouncing around, random connections, "what if" sparks
- `projects/` — things actively being built or seriously considered; progress, blockers, next steps
- `habits/` — daily habit check-ins, energy tracking, what slipped, what stuck; has a master `tracker.md`
- `family/` — moments with kids, presence check-ins, things worth remembering
- `journaling/` — raw emotional state, what's weighing on you, honest reflection
- `career/` — work done today, learning, professional reflection; has `PYTHON_LOG.md` and `patterns.md`
- `misc/` — anything that genuinely doesn't fit elsewhere

## Instructions

1. Read the full brain dump before doing anything — don't start routing until you've seen everything
2. Assign each piece of content to the most logical folder based on its meaning, not just keywords
3. For most folders (`career/`, `habits/`, `family/`, `journaling/`, `ideas/`, `projects/`, `misc/`), all dated entries go inside the folder's `reflection_log/` subdirectory: `folder/reflection_log/YYYY-MM-DD.md`
4. For `readings/` content: identify the specific book or source, then create or use the existing subfolder for that book (e.g. `readings/think-and-grow-rich/`). Use kebab-case for folder names.
   - Raw notes, chapter reactions, in-the-moment thoughts → dated entry flat inside the book folder (`readings/book-name/YYYY-MM-DD.md`)
   - Synthesized ideas, connections, or takeaways → also update that book's `summary.md` (create it if it doesn't exist, using the template: Status, What kind of book is this, Major Ideas, Connections, Honest Takeaways, Entry Log)
   - If the book folder doesn't exist yet, create it with both the dated entry and a `summary.md`
5. For `habits/` content:
   - Daily check-in, what happened today → `habits/reflection_log/YYYY-MM-DD.md`
   - New habit identified, habit confirmed working, habit dropped, or pattern noted → also update `habits/tracker.md`
   - If unsure, default to the dated entry and flag it
6. If content spans multiple folders, split it appropriately — don't force everything into one file
7. Only create a new top-level folder if the content genuinely does not fit any existing folder — not just loosely
8. If you do create a new top-level folder, write a `suggestions.md` for it and create a `reflection_log/` subdirectory inside it
9. Never force content into a folder that doesn't fit just to avoid creating a new one
10. After organizing, give a brief plain-text summary: one line per folder used, what went there, and flag anything you were unsure about

## Tone for new suggestions.md files

Look at the existing `suggestions.md` files before writing a new one. Match:
- A one-line opener that sets the mood (no heading, just a sentence)
- 4–6 open-ended questions as a bulleted list
- Casual, honest, low-stakes voice — never prescriptive
