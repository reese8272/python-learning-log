# DECISIONS.md — life-log

A log of explicit design decisions that change or deviate from what the planning docs previously said.

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
