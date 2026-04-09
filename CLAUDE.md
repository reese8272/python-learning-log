# CLAUDE.md — python-learning-log

This file contains project-specific instructions for Claude Code. These override global defaults where they conflict.

---

## Readings Structure

Each book lives in its own subfolder under `readings/` using kebab-case (e.g. `readings/think-and-grow-rich/`).

A reference template lives at `readings/template.md`. All new `summary.md` files must follow this structure.

Every book folder contains:

```
readings/<book-name>/
  summary.md          ← living master document — follows readings/template.md
  reflection_log/     ← all dated session notes go here
    YYYY-MM-DD.md
```

### 1. `summary.md` — the master file
Follows the structure in `readings/template.md`:
- Personal take on what kind of book it is
- Chapter-by-chapter summaries, each with a **Main Idea** (1-2 sentences), bullet points (as many as the chapter warrants), and a quick **Connection** note
- A **Connections & Application** section at the bottom — deeper synthesis of observations, patterns, and actions forming. Not "observation vs. action" — they're intertwined.
- **Honest Takeaways** — what landed, what didn't
- **Entry Log** — links to dated entries in `reflection_log/`

Update `summary.md` as reading progresses. It does not need to be complete until the book is finished.

### 2. `reflection_log/YYYY-MM-DD.md` — dated session notes
Raw notes from a specific reading session. These feed into `summary.md` over time. They do not need to be polished. Kept for reference in reflections and reviews.

### When routing brain dump content about a book:
- Raw notes, chapter reactions, and in-the-moment thoughts → `reflection_log/YYYY-MM-DD.md`
- Synthesized ideas, chapter summaries, connections, takeaways → update `summary.md`
- If unsure, default to the dated entry and flag it

---

## Folder Entry Structure

Every top-level folder (`career/`, `habits/`, `family/`, `journaling/`, `ideas_and_connections/`, `projects/`, `misc/`) uses this pattern:

```
folder/
  suggestions.md         ← prompts and tone for this folder
  [tracker/summary].md   ← living master document (where applicable)
  reflection_log/        ← all dated daily entries go here
    YYYY-MM-DD.md
```

Dated entries always go inside `reflection_log/`, not the folder root. This keeps the root clean and the living documents easy to find.

**No exception for readings:** `readings/<book>/reflection_log/` follows the same pattern. Dated entries go inside `reflection_log/`, not the book folder root.

---

## Career — CAREER_LOG.md and patterns.md

`career/CAREER_LOG.md` is the living career and expertise tracker. It contains:
- **Skills Tracker** — organized by domain (Agentic Engineering, LLM Systems, System Design, Production Infrastructure, Cloud/AWS, Security, Python Core). Update when understanding genuinely deepens.
- **Judgment Log** — records moments where the *decision rationale* clicked, not just the answer. The bar: "can I explain why THIS over THAT?" This replaces the old Independence Tracker.
- **Consulting Log** — captures moments where he explained, led, or taught. Career data.
- **Active Struggles** — current blockers; delete entries when resolved

**Mastery standard:** Can explain why THIS over THAT. Syntax is handled. Logic and decision rationale is the bar.

Weekly and monthly reflections on career/learning are handled by `/weekly-review` and `/monthly-review`. Do not add CURRENT WEEK or CURRENT MONTH sections back to CAREER_LOG.md.

`career/PYTHON_LOG.md` is archived — superseded by CAREER_LOG.md. Do not update it.

`career/patterns.md` is a reference of reusable patterns and mental models. Sections: Python patterns (existing), Agentic System Design, Production Infrastructure, Security, Cloud/AWS. Add a row when a pattern proves reliable. The "why this over that" framing is the standard for every entry. This is also a review tool — use it to identify gaps relative to what the user wants to become.

---

## Habits Structure

`habits/` contains two types of files:

### 1. `tracker.md` — the master habit tracker
A living document that reflects the honest, current state of the habit practice. It is not a log — it is the picture that emerges from coaching over time.

Sections:
- **Active — Locked In**: habits showing up consistently; protect these
- **Building — In Progress**: intentional but not yet consistent; watch closely
- **Aspirational — On Deck**: worth building eventually, not forcing yet
- **Dropped / Paused**: habits tried and set aside, with context
- **Coach Notes**: timestamped observations from reflections and reviews

Update `tracker.md` when:
- A habit is confirmed working (move to Active)
- A habit slips or is consciously dropped (move to Dropped)
- A new habit is identified (add to Building or Aspirational)
- A review or reflection surfaces a pattern worth noting (add to Coach Notes)

### 2. Dated entry files (`YYYY-MM-DD.md`)
Raw daily check-ins. What showed up, what didn't, energy notes. These feed the tracker over time and are kept for reference in reflections and reviews.

### When routing brain dump content about habits:
- Daily check-in, what happened today → dated entry file
- Pattern confirmed, habit added/dropped/promoted → update `tracker.md`
- If unsure, default to the dated entry and flag it

---

## Folder Overview

| Folder | Purpose |
|---|---|
| `career/` | `CAREER_LOG.md` (skills + judgment + consulting tracker) + `patterns.md` + `reflection_log/` entries |
| `habits/` | `tracker.md` (master habit state) + `reflection_log/` daily check-ins |
| `family/` | `reflection_log/` dated entries — moments with kids, presence, things worth remembering |
| `journaling/` | `reflection_log/` dated entries — raw emotional state, honest reflection |
| `ideas_and_connections/` | `reflection_log/` sandbox entries — quotes, sparks, project seeds, random connections, inspiration not buckled to any folder |
| `readings/` | `template.md` + per-book subfolders with `summary.md` + `reflection_log/` dated session notes |
| `projects/` | `reflection_log/` dated entries — things actively being built or considered |
| `misc/` | `reflection_log/` dated entries — anything that doesn't fit elsewhere |
| `reflections/` | Daily, weekly, and monthly review logs |
| `brain-dump.md` | Single entry point — everything flows from here into folders |
