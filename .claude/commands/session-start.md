You are running a pre-learning session ritual. This is structured, not conversational — it takes 2 minutes and gets the user into the session with full context and the right structure enforced.

> ## ⚠️ PHASE 3 — mostly superseded (2026-08-27)
>
> **`/today` is the session-opening ritual now.** It replaces this command's job of getting into a block with the right context, and it works for all four lanes rather than only learning.
>
> This command still assumes an ACTIVE course with a Build Log and a "Next Build Task." **There is no active track** — all four curricula are paused as a reference catalog. Run this only if a specific paused roadmap is deliberately re-opened at an `/audit`.
>
> Retiring it outright is a candidate for the next audit's **subtraction pass**.


## Step 1 — Read silently

Before saying anything, read:
- The active course's `summary.md` — find the Build Log and the current "Next Build Task"
- The most recent entry in the course's `reflection_log/` — find the ready-to-resume note at the bottom ("Stopped at: X. Next step: Y")

Do not respond yet.

## Step 2 — ADHD check-in

Three questions, one at a time. Fast — this is a pre-flight checklist, not a conversation.

**Question 1 — Peak window**
Ask: "Is this your peak window — roughly 90–180 min after your medication kicked in?"

- Yes → continue
- No → flag it honestly: "You're outside your peak window. Fine to continue, but save the hardest new material for peak. Passive review or easier content is better suited for now."

**Question 2 — Build rule**
Check the Build Log. Ask: "Did you build something from last session's content before coming back?"

- Yes → confirm what they built, mark that Build Log row as complete
- No → stop. "Build rule isn't satisfied. Before opening the course, spend 5–15 minutes on this: [Next Build Task from the Build Log]. Come back when it's done." Do not proceed until they confirm it's done.

**Question 3 — Ready-to-resume**
Surface the ready-to-resume note from the last session log. Read it back: "Your note from last time: '[note text]'. Does that land — anything to add before we start?"

- No note found → note it: "No ready-to-resume note from last session. We'll write one at the end of this one."

## Step 3 — Open the session

Confirm the next build task so it's front of mind going in:
"After this session, your build task will be: [next task from Build Log]."

Then: "You're clear. Go."

## Step 4 — Session close

When the user signals they're done, ask two things:

1. "Ready-to-resume note — one line. Stopped at X, next step Y."
2. "Build task this session: did you get to it, or still queued?"

Then write the session log and update the Build Log.

**Session log** → `readings/[course-folder]/reflection_log/YYYY-MM-DD.md`:
```
# Session — YYYY-MM-DD

## What was covered
[What the user worked through this session]

## Ready-to-resume
Stopped at: [X]. Next step: [Y].

## Build task
[What was built, or "queued" if not yet done]
```

**Build Log update** → in the course `summary.md`:
- Mark today's session row with what was covered and built
- Update "Next Build Task" based on what was learned — specific enough to start immediately, no figuring out required

## Tone

Two minutes max for the check-in. Fast and clean. This is infrastructure, not coaching. The goal is to get the user into the session with context locked in and the rules enforced — not to have a conversation about them.
