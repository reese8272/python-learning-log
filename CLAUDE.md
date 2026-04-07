# CLAUDE.md — python-learning-log

This file contains project-specific instructions for Claude Code. These override global defaults where they conflict.

---

## Readings Structure

Each book lives in its own subfolder under `readings/` using kebab-case (e.g. `readings/think-and-grow-rich/`).

Every book folder contains two types of files:

### 1. `summary.md` — the master file
This is the canonical record of the book. It is not a log entry — it is a living document that builds as the book is read and gets refined afterward. It should read like a thoughtful person explaining the book through their own lens, not a Wikipedia summary.

Contents:
- A short personal take on the book overall (what kind of book is it, who is it for)
- Major ideas and themes, in the reader's own words
- Connections to other books, experiences, or ideas in other folders
- Quotes or passages worth keeping
- One or two honest takeaways — what actually landed, what didn't

Update `summary.md` as reading progresses. It does not need to be complete until the book is finished.

### 2. Dated entry files (`YYYY-MM-DD.md`)
Raw notes from a specific reading session. These feed into `summary.md` over time and are kept for reference in reflections and reviews. They do not need to be polished.

### When routing brain dump content about a book:
- Raw notes, chapter reactions, and in-the-moment thoughts → dated entry file
- Synthesized ideas, connections, takeaways → update `summary.md`
- If unsure, default to the dated entry and flag it

---

## Folder Entry Structure

Every top-level folder (`career/`, `habits/`, `family/`, `journaling/`, `ideas/`, `projects/`, `misc/`) uses this pattern:

```
folder/
  suggestions.md         ← prompts and tone for this folder
  [tracker/summary].md   ← living master document (where applicable)
  reflection_log/        ← all dated daily entries go here
    YYYY-MM-DD.md
```

Dated entries always go inside `reflection_log/`, not the folder root. This keeps the root clean and the living documents easy to find.

**Exception:** `readings/` book subfolders keep dated entries flat inside the book folder — they're already one level deep and don't need further nesting.

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
| `ideas/` | `reflection_log/` dated entries — half-baked thoughts, sparks, random connections |
| `readings/` | Per-book subfolders with `summary.md` + flat dated entries inside the book folder |
| `projects/` | `reflection_log/` dated entries — things actively being built or considered |
| `misc/` | `reflection_log/` dated entries — anything that doesn't fit elsewhere |
| `reflections/` | Daily, weekly, and monthly review logs |
| `brain-dump.md` | Single entry point — everything flows from here into folders |
