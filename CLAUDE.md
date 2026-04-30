# CLAUDE.md — life-log

This file contains project-specific instructions for Claude Code. These override global defaults where they conflict.

---

## Git — Direct to Main

This is a personal journaling repo with a single owner. **Always commit and push directly to `main`.** No feature branches, no PRs. Every session ends with a clean push to main.

---

## Core Philosophy — The 3-Iteration Filter

This system is a personal reflection journal and knowledge base. Everything here exists to help the user get better — not to store trivia.

Content flows through three review cycles: **daily → weekly → monthly**. Each level filters and elevates what matters. If something survives all three iterations, it belongs in a living document. If it didn't get picked up in three passes, it's not load-bearing and doesn't need to be kept.

- **Living documents** (tracker.md, CAREER_LOG.md, summary.md, index.md) are the permanent layer — glanceable, findable, evolving.
- **Dated logs** (reflection_log/YYYY-MM-DD.md) are working memory — raw input that feeds the living documents through reflections and reviews.
- **Reflections** (reflections/) are the coaching record — full conversations that capture how thinking evolved over time.

---

## Readings Structure

Each book lives in its own subfolder under `readings/` using kebab-case (e.g. `readings/think-and-grow-rich/`).

A reference template lives at `readings/template.md`. All new `summary.md` files must follow this structure.

`readings/index.md` is the cross-book patterns document. It captures connections and themes that span multiple books — not per-book summaries (those live in each book's `summary.md`). Update `index.md` when a new cross-book pattern is identified or an existing pattern gains a new data point from a new book.

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
- Cross-book connections or patterns → update `readings/index.md`
- If unsure, default to the dated entry and flag it

---

## Folder Entry Structure

Every top-level folder (`career/`, `ideas_and_connections/`, `projects/`, `misc/`) uses this pattern:

```
folder/
  suggestions.md         ← prompts and tone for this folder
  [living document].md   ← master document (where applicable)
  reflection_log/        ← all dated daily entries go here
    YYYY-MM-DD.md
```

Dated entries always go inside `reflection_log/`, not the folder root. This keeps the root clean and the living documents easy to find.

**No exception for readings:** `readings/<book>/reflection_log/` follows the same pattern. Dated entries go inside `reflection_log/`, not the book folder root.

**Habits is an exception:** `habits/` has only `tracker.md` and `suggestions.md` — no reflection_log. Habit check-ins happen through daily reflections; the tracker is updated directly when habits are confirmed, dropped, or noted.

---

## Career — CAREER_LOG.md and patterns.md

`career/CAREER_LOG.md` is the living career and expertise tracker. It contains:
- **Skills Tracker** — organized by domain (Agentic Engineering, LLM Systems, System Design, Production Infrastructure, Cloud/AWS, Security, Python Core). Update when understanding genuinely deepens.
- **Judgment Log** — records moments where the *decision rationale* clicked, not just the answer. The bar: "can I explain why THIS over THAT?"
- **Consulting Log** — captures moments where he explained, led, or taught. Career data.
- **Active Struggles** — current blockers; delete entries when resolved

**Mastery standard:** Can explain why THIS over THAT. Syntax is handled. Logic and decision rationale is the bar.

Weekly and monthly reflections on career/learning are handled by `/weekly-review` and `/monthly-review`. Do not add CURRENT WEEK or CURRENT MONTH sections back to CAREER_LOG.md.

`career/patterns.md` is a reference of reusable patterns and mental models. Sections: Python patterns (existing), Agentic System Design, Production Infrastructure, Security, Cloud/AWS. Add a row when a pattern proves reliable. The "why this over that" framing is the standard for every entry. This is also a review tool — use it to identify gaps relative to what the user wants to become.

---

## Habits Structure

`habits/` contains `tracker.md` and `suggestions.md` — no reflection_log.

### `tracker.md` — the master habit tracker
A living document that reflects the honest, current state of the habit practice. It is not a log — it is the picture that emerges from coaching over time.

Sections:
- **Ideal Day — Full Habit Map**: reference for the morning; all target habits mapped to time of day
- **Active — Locked In**: habits showing up consistently; protect these
- **Building — In Progress**: intentional but not yet consistent; watch closely
- **Aspirational — On Deck**: worth building eventually, not forcing yet
- **Dropped / Paused**: habits tried and set aside, with context and reason
- **Coach Notes**: timestamped observations from reflections and reviews

Update `tracker.md` when:
- A habit is confirmed working (move to Active)
- A habit slips or is consciously dropped (move to Dropped, include reason)
- A new habit is identified (add to Building or Aspirational)
- A review or reflection surfaces a pattern worth noting (add to Coach Notes)

Habit check-ins happen through `/reflect` conversations, not separate dated entries.

---

## Ideas & Connections Structure

`ideas_and_connections/` captures quotes, sparks, insights, and connections that stuck — things worth finding again.

- `index.md` — the living document. Contains the ideas that survived a reflection cycle and earned their place. Each entry: the idea, why it stuck, source, and date. This is the retrieval layer — the place to look when asking "what was that one thing...?"
- `reflection_log/YYYY-MM-DD.md` — raw dated entries for ideas as they arrive
- `suggestions.md` — prompts for the folder

### When routing brain dump content about ideas:
- Raw sparks, quotes, half-baked thoughts → `reflection_log/YYYY-MM-DD.md`
- Ideas that survived a reflection and proved worth keeping → add to `index.md`
- If unsure, default to the dated entry and flag it

---

## Folder Overview

| Folder | Purpose |
|---|---|
| `career/` | `CAREER_LOG.md` (skills + judgment + consulting tracker) + `patterns.md` + `reflection_log/` entries |
| `habits/` | `tracker.md` (master habit state) — no reflection_log; check-ins happen through daily reflections |
| `ideas_and_connections/` | `index.md` (living highlights) + `reflection_log/` raw entries — quotes, sparks, insights worth finding again |
| `readings/` | `index.md` (cross-book patterns) + `template.md` + per-book subfolders with `summary.md` + `reflection_log/` session notes |
| `projects/` | `reflection_log/` dated entries — things actively being built or considered |
| `misc/` | `reflection_log/` dated entries — anything that doesn't fit elsewhere |
| `reflections/` | Daily, weekly, and monthly review logs — the coaching record |
| `brain-dump.md` | Single entry point — everything flows from here into folders |
