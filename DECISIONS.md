# DECISIONS.md — life-log

A log of explicit design decisions that change or deviate from what the planning docs previously said.

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
