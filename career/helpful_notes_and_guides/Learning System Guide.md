# Learning System Guide — What to Use and When

This is the operating manual for the system. When in doubt, come here first.

---

## Something just crossed your mind
**→ `brain-dump.md`**

Doesn't matter what it is — a random idea, something you want to read, a career thought, a frustration, a quote. Everything goes here first. Don't route it yourself. That's what `/organize-brain-dump` is for.

---

## Before a course session
**→ `/session-start`**

Run this before you open Eden Marco or any course. It takes 2 minutes. It checks whether the peak window is actually open, surfaces your ready-to-resume note from last session so you know exactly where to pick up, and confirms you satisfied the build rule before advancing. If you didn't build anything from the last lesson yet — it stops you there. Build first, then come back.

It also reads your latest session notes and gives you a specific, concrete build task for your paired project based on what you covered last time. Not vague — something you can start immediately.

At the end of the session, it prompts you to write the ready-to-resume note so the next session costs nothing to restart.

---

## During a course session
**→ Code-along in the course repo + build in your own repo**

Code-along follows the instructor. Your paired project is where you apply what you just learned on your own terms. The rule: don't advance to the next lesson until something from the last lesson exists in your own project, even if it's five lines.

**How the paired project grows:**
- `/session-start` generates the specific build task from your session notes
- The Build Log in the course `summary.md` tracks what's been built and what's queued
- You don't have to figure out what to add — the session notes tell you, and the command surfaces it

---

## Downtime — coffee, post-lunch, afternoon slump
**→ `/drill`**

This is your non-peak window. Not for new learning — for testing what's already in you. It pulls from your `CAREER_LOG.md` — judgment log entries and skills — and asks you to explain them cold. You answer, it gives honest feedback, it updates Last Reviewed. Five to ten minutes. No peak window needed.

---

## Something happened today worth reflecting on
**→ `/reflect`**

Your daily coaching session. It reads everything — your recent logs, habit tracker, brain dump — and opens a real conversation. At the end it logs the session, updates the habit tracker if anything shifted, clears the brain dump, and sets tomorrow's one intention.

Run this whenever the day feels worth processing. Ideally evening, but timing isn't rigid.

---

## End of the week (Sunday)
**→ `/weekly-review`**

Three questions: what did you actually finish learning this week, what's the one learning goal for next week, what got in the way. Also scans your CAREER_LOG for skills with stale Last Reviewed dates and flags them as your next drill targets. Takes 15 minutes.

---

## End of the month
**→ `/monthly-review`**

Highest altitude view. Are you moving toward the right things? What shifted in the career picture? What habits locked in, what dropped? This is when the living documents — CAREER_LOG, habits tracker, readings index — get meaningfully updated based on everything that accumulated across the month.

---

## Starting a new course or book
**→ Create the folder, fill in the template**

Use `readings/template.md` as the base. The Paired Project field must be filled before session 1 — non-negotiable. If you can't define what you're building alongside it, you're not ready to start it. Log sessions in `reflection_log/YYYY-MM-DD.md`, synthesize into `summary.md` as you go.

---

## You learned something at a level deeper than before
**→ Update `CAREER_LOG.md`**

Only when something genuinely shifted — not on every session. If a "why THIS over THAT" moment clicked, add a row to the Judgment Log. If a skill level actually moved, update the Skills Tracker. The bar is real understanding, not exposure.

---

## Quick Reference

| Trigger | Tool |
|---|---|
| Anything on your mind | `brain-dump.md` |
| Before a course session | `/session-start` |
| Non-peak downtime | `/drill` |
| Processing the day | `/reflect` |
| End of week | `/weekly-review` |
| End of month | `/monthly-review` |
| Starting a new course or book | New folder + template |
| Something genuinely clicked | `CAREER_LOG.md` |

---

## The Rules That Govern Learning Sessions

These live in `CLAUDE.md` and are enforced automatically. Listed here for reference.

1. **Peak window is sacred** — 90–180 min post-medication for hardest learning only. No email, Slack, or system-tinkering.
2. **One active course** — finish or formally retire before starting another.
3. **Pre-commit a project** — defined before session 1, lives in `summary.md` under Paired Project.
4. **Build before next lesson** — code using the last session's concept must exist in your own repo before advancing.
5. **Ready-to-resume note** — one line before any context switch: "Stopped at: [X]. Next step: [Y]."
6. **Struggle first** — 10–20 min of independent effort before using AI. Bring your attempt as context.
7. **Cardio before peak** — morning gym pre-loads dopamine for the learning block that follows.
