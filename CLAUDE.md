# CLAUDE.md — life-log

This file contains project-specific instructions for Claude Code. These override global defaults where they conflict.

---

## Git — Direct to Main

This is a personal journaling repo with a single owner. **Always commit and push directly to `main`.** No feature branches, no PRs. Every session ends with a clean push to main.

---

## ADHD Learning Protocol

These rules exist because the ADHD brain's motivation system requires engineered structure, not more willpower. When coaching a learning session, enforce these — don't work around them.

**The primary learning engine is concept-driven, not course-driven** — a three-stage in-catalog pipeline, all phone-friendly, all logged to `CAREER_LOG.md`:
- **`/learn`** — acquire a concept from zero, researched live against current docs, tied to his code. Walks the technical curriculum at `readings/ai-engineering-curriculum/summary.md`. *Replaces taking online courses.*
- **`/sharpen`** — defend what he's learned/built cold, at the tier bar. Walks `career/concept_queue.md`.
- **`/drill`** — retain landed concepts on a spaced schedule.

Online courses are **not taken**; their content was mined into the curriculum (minus deprecated patterns — see the curriculum's Currency Watch). The Master Guide (`career/helpful_notes_and_guides/AI Engineering Master Guide.md`) is the reference that anchors all of it (North Star, capstone, resource pool). Live research every technical session — never teach/grade from memory; the ecosystem moves too fast.

**Peak window is sacred.** The 90–180 minutes post-medication is reserved for the hardest, most novel learning only — `/sharpen` sessions, a pulled course section, AWS cert material, technical papers. Never burn this window on email, Slack, system-tinkering, or passive review. This single reallocation produces more learning gains than any tool change.

**The build is non-negotiable.** Grilling concepts without building is passive consumption with extra steps. Two anchors keep the build alive: (1) the **dedicated capstone project** (Master Guide Phase 2) is the eventual portfolio piece; (2) **build before you bank** — a grilled concept isn't owned until code using it exists somewhere real (work, autoclip, capstone, a throwaway script). Five minutes counts.

**When you do pull a course** (gap-filler mode only): one at a time, until the gap is filled or formally retired. If shelved, write a 100-word retirement letter in `misc/reflection_log/YYYY-MM-DD.md`. No silent abandonment. Pre-commit which queue concept or build the course section feeds before starting it — never watch a course for completion's sake.

**Ready-to-resume note.** Before any context switch away from a learning session, write one line in the dated session log: "Stopped at: [X]. Next step: [Y]." This reconstructs context faster than re-reading.

**Struggle first.** Minimum 10–20 minutes of independent effort before using AI. When asking AI: share what you tried, where you're stuck, and ask it to help you *see* what you're missing — not give the answer outright.

**Cardio before peak.** 20–30 min of zone-2 cardio before the peak block pre-loads dopamine and BDNF for hours. If morning gym happened, the peak block benefits. If it didn't, that's a variable worth noting.

---

## The Floor & /checkin — the daily minimum interface

The system's #1 documented failure mode is all-or-nothing collapse (4/09, 5/01, 6/16): external pressure takes down the whole stack, then re-entry friction and guilt keep it down for weeks. The engineered counter, added 2026-07-05:

- **The Floor:** a day *counts* when just two things happen — the 10:30pm reading brick (phone-on-charger cue) and one **ownership touch** (a doc/audit line on his own shipped code, or the workday close-out done). Everything else in the habit map is upside, never owed. *(Floor #2 was a job-pipeline touch until 2026-07-25 — retired by choice after John's mid-year review; the priority now is owning and growing the Cognizant role, not the exit pipeline.)* Bad-day rule: one non-negotiable (presence with the kids, or the brick) still makes the day count.
- **`/checkin`** is the daily minimum: 3 minutes, phone-friendly, three questions, updates the Card, logs a micro entry to `reflections/YYYY-MM-DD.md`, pushes to main. It does not replace `/reflect` — that remains the full session when there's something to process.
- **The Card** (Daily section of `agenda.md`) is the front door: floor, streaks, stopped-at line. It must always reflect NOW — a stale Card is a system bug. Any session that changes current state (a learning session, a job application, a reflection) should leave the Card accurate.
- **Re-entry rule — enforce this:** after any gap, the way back is `/checkin`. Gaps are data, never debt. No guilt, no archaeology, no "what happened" interrogation — one warm sentence, streak restarts today, three questions, done.

---

## Core Philosophy — The 3-Iteration Filter

This system is a personal reflection journal and knowledge base. Everything here exists to help the user get better — not to store trivia.

Content flows through three review cycles: **daily → weekly → monthly**. Each level filters and elevates what matters. If something survives all three iterations, it belongs in a living document. If it didn't get picked up in three passes, it's not load-bearing and doesn't need to be kept.

- **Living documents** (tracker.md, CAREER_LOG.md, summary.md, index.md) are the permanent layer — glanceable, findable, evolving.
- **Dated logs** (reflection_log/YYYY-MM-DD.md) are working memory — raw input that feeds the living documents through reflections and reviews.
- **Reflections** (reflections/) are the coaching record — full conversations that capture how thinking evolved over time.

---

## Readings Structure

**Books and courses are treated the same way.** Both live under `readings/` using kebab-case (e.g. `readings/think-and-grow-rich/`, `readings/langchain-eden-marco/`). A course is consumed content with a natural arc — it gets a `summary.md` and dated session logs just like a book.

A reference template lives at `readings/template.md`. All new `summary.md` files must follow this structure. For courses, adapt the language: "sessions" instead of "chapters," "What kind of course this is" instead of "What kind of book this is."

`readings/index.md` is the cross-source patterns document. It captures connections and themes that span multiple books or courses — not per-source summaries (those live in each subfolder's `summary.md`). Update `index.md` when a new cross-source pattern is identified or an existing pattern gains a new data point.

Every book or course folder contains:

```
readings/<source-name>/
  summary.md          ← living master document — follows readings/template.md
  reflection_log/     ← all dated session notes go here
    YYYY-MM-DD.md
```

### 1. `summary.md` — the master file
Follows the structure in `readings/template.md`:
- Personal take on what kind of book/course it is
- Session or chapter summaries, each with a **Main Idea** (1-2 sentences), bullet points (as many as the session warrants), and a quick **Connection** note
- A **Connections & Application** section at the bottom — deeper synthesis of observations, patterns, and actions forming. Not "observation vs. action" — they're intertwined.
- **Honest Takeaways** — what landed, what didn't
- **Entry Log** — links to dated entries in `reflection_log/`

Update `summary.md` as reading/viewing progresses. It does not need to be complete until the source is finished.

### 2. `reflection_log/YYYY-MM-DD.md` — dated session notes
Raw notes from a specific session. These feed into `summary.md` over time. They do not need to be polished. Kept for reference in reflections and reviews.

### 3. Career update loop — after every course session
After routing course notes into `readings/`, always check whether anything warrants an update to the career files:
- A skill genuinely deepened → update the Skills Tracker level + notes in `CAREER_LOG.md`
- A "why THIS over THAT" moment clicked → add a row to the Judgment Log in `CAREER_LOG.md`
- A pattern proved reliable → add a row to the relevant section in `patterns.md`

The bar is genuine deepening, not just exposure. Don't update on every session — update when something actually shifted.

### When routing brain dump content about a book or course:
- Raw notes, chapter/session reactions, and in-the-moment thoughts → `reflection_log/YYYY-MM-DD.md`
- Synthesized ideas, session summaries, connections, takeaways → update `summary.md`
- Cross-source connections or patterns → update `readings/index.md`
- Career-level insights (skill level up, judgment moment, reusable pattern) → update `career/CAREER_LOG.md` and/or `career/patterns.md`
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

Habit check-ins happen through `/checkin` (daily floor) and `/reflect` conversations, not separate dated entries.

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
| `readings/` | `index.md` (cross-source patterns) + `template.md` + per-book/course subfolders with `summary.md` + `reflection_log/` session notes. Courses follow the same structure as books. |
| `projects/` | `reflection_log/` dated entries — things actively being built or considered |
| `misc/` | `reflection_log/` dated entries — anything that doesn't fit elsewhere |
| `reflections/` | Daily, weekly, and monthly review logs — the coaching record |
| `brain-dump.md` | Single entry point — everything flows from here into folders |
