# DECISIONS.md — life-log

A log of explicit design decisions that change or deviate from what the planning docs previously said.

---

## 2026-08-04 — Coaching posture flipped: mentor generates insight, not therapist draws it out

**What changed:** New root file **`COACHING.md`** — the Mentor Doctrine — now the governing posture for every coaching session and for ordinary conversation in this repo. The core rule: **every session must leave a read on the table**; a session that only asked questions and mirrored him back is a *failed* session. Defines the four insight moves (cross-time read with dates · named call · reframe · the thing he didn't ask about), how to deliver a read ("here's what I see — does that track?"), and the only three cases where holding beats reading (raw grief · explicit "let me just talk" · genuine ambiguity in the record).

Files edited to match:
- `CLAUDE.md` — new "Coaching Posture" section at the top, pointing at `COACHING.md`
- `reflect.md` — Step 2 is now **form a read before speaking**; deleted *"your job is to draw things out of the user, not present things to them"*, *"lead with listening, not analysis... make them feel heard, not assessed"*, *"only challenge when they're clearly being dishonest with themselves"*, and *"if a contradiction exists, ask about it gently and let them see it themselves."* "Reflective listening" dropped from the toolkit; new **Insight toolkit** added above the (now demoted) Question toolkit; steps renumbered (the file had two "Step 5"s)
- `weekly-review.md` — *"let them arrive at it themselves, don't present it like a finding"* → **present patterns as findings with dates attached**; challenge whenever the record supports it, not only on self-dishonesty
- `monthly-review.md` — *"ask about it gently — let them arrive at the honest read themselves"* → **say it plainly with the evidence**; minimum deliverable is one month-spanning cross-time read + one named call
- `checkin.md` — unchanged in length; gains a hard-capped **one-sentence** optional read, explicitly outranked by the re-entry rule and forbidden when it would land as criticism at 10:40pm

**Why:** Reese's call, opening this session: *"I want Claude to be like a person who is able to generate insight now rather than just 'hearing me out.'"* The audit confirmed the gap was real and was in the *mechanics*, not the identity — every skill already declared "you are a mentor, not a therapist" in its Tone section while the step-by-step instructions enforced textbook Rogerian practice (withhold conclusions, let the client discover it). Net effect: `/brutally-honest` was the only skill in the system permitted to state a finding, so the only two settings were *validate* and *audit with receipts*, with nothing in between. The doctrine fills that middle. Tone is explicitly unchanged — process praise, "and" not "but", cue-level habit diagnosis, gaps-are-data — the only change is that the coach now shows up with something.

**Source / evidence:** Reese's request, 2026-08-04. Offending lines quoted above were pulled verbatim from the pre-change files. New file: `COACHING.md`. Related: memory `feedback_mentoring_tone.md` (2026-04, established the mentor *tone*) — this decision supplies the missing *mechanics*.

---

## 2026-07-07 — `/learn new`: an on-demand mode (Reese names the topic)

**What changed:** Added a fourth `/learn` mode — **`/learn new <topic>`** (aliases `adhoc`, `work`, `just-in-time`) — where Reese supplies the topic himself instead of it coming from a curated roadmap. New home: `career/on-demand-learning/` (`summary.md` is a *ledger/index* of what's been learned on demand, not a pre-planned unit list; + `reflection_log/`). Same `/learn` rigor (research-first → probe → teach → explain-back → build-before-bank). **Adaptive** on two axes: technical topic → writes a `.py` worksheet in `lesson_assignments/` and may enter `concept_queue.md` for `/sharpen`; conceptual topic → no worksheet, bank by using it (like `soft`). At persist, the "roadmap update" is appending a ledger row, not ticking a `[ ]`. When a cluster of related topics forms, the mode offers to **graduate** it into its own full track (the precedent: soft-skills, created earlier today). `.claude/commands/learn.md` updated: intro, Step 0 table + adaptation bullet, Step 1 (skip roadmap scan), Step 8 (ledger append).

**Why:** Reese's request — work regularly hands him something new he must learn *before* he can use or add it, and he wanted that just-in-time learning **banked here** rather than lost. The three existing tracks are all pre-curated roadmaps; none had a slot for emergent, work-driven topics. This closes that gap without polluting the curated tracks, and the graduation path means a recurring on-demand topic can become a real curriculum when it earns it.

**Source / evidence:** Reese's request during the 2026-07-07 `/learn soft` session, immediately after the three-track restructure. Files: `.claude/commands/learn.md`, new `career/on-demand-learning/`.

---

## 2026-07-07 — `/learn` goes from two tracks to three; mid-python repurposed; soft-skills added

**What changed (three linked decisions):**
1. **`/learn` now drives THREE parallel tracks, not two.** Step 0 of `.claude/commands/learn.md` updated: `ai` (AI Engineering — master track), `py` (Python Mastery), and new `soft` (Senior Engineering — Soft Skills). Track selected by token; ASK-ONCE fallback now names all three.
2. **The mid-python track was repurposed, not deleted.** The specific mid-level Python role that seeded `career/mid-python-developer-prep/` ($115k FastAPI weather-data shop) **closed before it was filled.** Rather than discard the work, its purpose was re-pointed from "demolish this one interview" → "Python mastery underpinning the AI-eng path." The FastAPI/weather intel is retained as realistic practice material, not *the* target job. Summary header reframed; `/learn` table updated.
3. **New `soft` track is worksheet-exempt and does NOT use `concept_queue.md`.** Soft skills have no code to green-light, so Step 7.5's `.py` worksheet is skipped for this track; the Step 7 "build" becomes a **real interaction** (interview answer, Slack/PR message, design doc). They're not defended cold in `/sharpen` either — soft skills are deployed under real conditions. Roadmap lives at `career/senior-engineering-soft-skills/summary.md` (6 units, Larson/Reilly/Fournier/Orosz as the resource pool).

**Why:** (1+2) Reese's mid-level dev job closed, but he explicitly chose to preserve the prep rather than let the loss collapse the work — Python mastery is genuinely foundational for AI engineering, so the content's value survives the job. (3) He asked to make senior/soft-skills a full track ("just as important as everything else"). At ~1yr in, aiming $120k+, the social/communication layer is the differentiator on top of technical skill — and unlike an API it has no runnable-test artifact, so the machinery was adapted honestly rather than faked.

**Source / evidence:** Reese's request during the 2026-07-07 `/learn` session (Unit 1 — Scope of Impact, the first soft-skills unit). Files touched: `.claude/commands/learn.md`, `career/mid-python-developer-prep/summary.md`, new `career/senior-engineering-soft-skills/`.

---

## 2026-06-22 — `/learn` now leaves a solo worksheet (lesson assignments)

**What changed:** Every `/learn` session now produces a self-contained, runnable **lesson assignment** at `career/lesson_assignments/YYYY-MM-DD_<kebab-unit>.py` — a struggle-first worksheet Reese can re-do alone. Added as **Step 7.5** in `.claude/commands/learn.md`. Three parts: (1) a short soliloquy on the target, (2) tiny isolated coding exercises with boilerplate pre-filled (concept/flow over syntax) and **Claude pre-writes the assert-based tests** for red/green solo feedback, (3) concept questions with a stated requirement + a gated answer key. Reference template: `career/lesson_assignments/2026-06-22_llm-call-anatomy.py`.

**Cross-skill guardrail:** `/sharpen` and `/drill` were updated with an "inspiration, not a crutch" note — they may borrow *angles* from a worksheet but must never read its prompts verbatim or surface the answer key before cold recall. Cold defense stays cold.

**Why:** Reese asked for it — a conversational `/learn` evaporates once the chat scrolls away; a runnable worksheet with pre-written tests turns the lesson into repeatable, phone-friendly homework with built-in feedback, and preserves the struggle-first principle when he works solo. The worksheet hits the *other* facets of the unit (not the Step-7 build he already did), widening coverage of the same primitive.

**Source / evidence:** Reese's request (2026-06-22) during the §1.1 `/learn` session. First worksheet (`2026-06-22_llm-call-anatomy.py`) shipped as the template; his `llm_cost.py` build confirmed the unit landed.

**Date:** 2026-06-22

---

## 2026-06-22 — Learning system: concept-driven engine replaces course-driven curriculum

**What changed:** The AI Engineering Master Guide was demoted from a course-completion curriculum ("complete in order, no skipping") to a **reference / source-of-truth**. The primary daily learning engine is now `/sharpen` + `career/concept_queue.md` — concept-driven, struggle-first, tied to Reese's own shipped code, logged to `CAREER_LOG.md`, maintained by `/drill`. Courses are reframed as **gap-fillers pulled on demand**, not a syllabus.

**Specifically:**
- Master Guide gained a "How to Use This Guide" section; Phase 1 retitled to a "Course Library — gap-fillers, pulled on demand"; Learning Philosophy rewritten around the sharpen→build→bank→drill loop.
- `concept_queue.md` Notes hardened with the rule: *concepts pull resources; resources don't push concepts.* Syllabi may be mined for candidate concepts, but they enter the pool **unprioritized** — never transcribed wholesale into a completion checklist.
- `CLAUDE.md` ADHD Learning Protocol reconciled: "One active course / Pre-commit a project / Build before next lesson" replaced with a concept-driven primary engine + a non-negotiable build anchor ("build before you bank") + course rules scoped to gap-filler mode only.
- **Capstone preserved as dedicated** (not folded into autoclip). The build mandate stays explicit so concept-grilling doesn't become passive consumption with extra steps.

**Why:** Structured courses don't survive the ADHD motivation system — Reese abandons them mid-way. The concept-queue loop delivers immediate reward, phone-friendly access (Claude Code mobile), and always-visible progress in `CAREER_LOG.md`, while directly producing the thing that matters for the AI-consultant target: defensible "why THIS over THAT" judgment, not passive exposure.

**Source / evidence:** Reese's own proposal (2026-06-22) + the `/sharpen` skill and `concept_queue.md` shipped the same day (commits `100600d`, `896c3b6`). The main tradeoff considered: a full deletion of the guide would have dropped the capstone build mandate and North Star context — rejected in favor of demote-to-reference + keep-dedicated-capstone.

**Date:** 2026-06-22

---

## 2026-06-22 — Technical learning moves fully in-catalog: `/learn` skill + live-researched curriculum replace online courses

**What changed:** Built a third learning skill, **`/learn`** (`.claude/commands/learn.md`), the *acquisition-from-zero* front of the pipeline: `/learn` (acquire, researched live) → `/sharpen` (defend cold) → `/drill` (retain). It walks a new technical curriculum at **`readings/ai-engineering-curriculum/summary.md`** — a sequenced, tiered **skeleton** of ~60 units across 8 sections (Foundations, LangChain Core, Agents, LangGraph, RAG, MCP, Evals/Observability, Async/Production) plus the Tier-2 periphery. Online technical courses are **no longer taken**; their content was mined into the curriculum and the actual teaching is generated **live against current docs** each session, so it never goes stale.

**Specifically:**
- Curriculum is a skeleton (objectives + tier + source + currency flags), not pre-written lessons — per the earlier 2026-06-22 decision that pre-baked content goes stale.
- Added a **⚠ Currency Watch** section capturing the breaking changes live research surfaced: LangChain v1 (`create_agent` over `AgentExecutor`, `langchain-classic`, `system_prompt`, TypedDict state), MCP 2025-11-25 (SSE-as-transport deprecated, structured output, elicitation, tasks, OAuth 2.1), RAGAS collections API + metric renames, LangGraph v1 (`interrupt()`, durability modes, supervisor/swarm split out), prompt-eng 2026 (prefilling removed, adaptive thinking, over-prompting backfires).
- Wired the three-stage pipeline into the Master Guide ("How to Use"), `concept_queue.md` (pipeline position), and `CLAUDE.md` ADHD Protocol.
- Two ledgers kept distinct: curriculum tracks *acquisition*; concept_queue tracks *defense*; CAREER_LOG tracks *mastery + cadence*.

**Why:** Online courses don't survive the ADHD motivation system AND go stale fast (a 2024 course teaches deprecated patterns). Learning in-catalog with live research solves both: immediate-reward + phone-friendly + always-tracked, AND always-current. Reese's own framing: "the technical things can be completely learned through here, as long as everything is backed and researched live (which is also helpful so the courses aren't outdated)."

**Source / evidence:** Reese's proposal (2026-06-22) + 5 parallel research subagents that pulled the current syllabi/docs for Eden Marco LangChain/LangGraph, MCP Masterclass + spec, RAG-evals + RAGAS, LangChain Academy + LangGraph/LangSmith, and Anthropic prompt-eng — each returning current topics plus a "potentially outdated" delta. Those deltas became the Currency Watch. Design forks confirmed via AskUserQuestion: new `/learn` skill (not folded into `/sharpen`), skeleton-map (not pre-written), research real syllabi live (not docs-only).

**Date:** 2026-06-22
