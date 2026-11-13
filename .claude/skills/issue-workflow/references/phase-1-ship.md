# Phase 1 - Understand, `ship` mode

Ship mode keeps every engineering gate downstream and replaces the briefing with a fast, evidence-backed scoping
round. It exists because an always-skipped gate teaches that gates are optional; an explicit mode does not.

## 1. Explore pass (you, not the user)

Launch one `Explore` agent (or two when the change spans backend and frontend) with the issue text, the overlay's
`repo_dir`, and the grounding summary. Ask for: the files and functions in scope with line numbers, the existing
pattern to copy (the closest sibling feature), what calls into the area, the tests that already cover it, and any
trap the ISSUES_LOG or decision logs record for it. Read the result; do not paste it to the user.

Before launching, grep `~/.claude/ISSUES_LOG.md` for the issue's key symptoms or component names. A logged root cause
beats re-diagnosis.

## 2. One batched question

Ask exactly one `AskUserQuestion` call with 2-4 questions, each with a "(Recommended)" option first and the evidence
for the recommendation in its description:

- the 2-3 scope decisions the Explore pass surfaced (which variant, what is out of scope, which existing pattern
  to reuse),
- the risk tier if the Explore pass changed your Phase 0 call,
- the DoR gaps (acceptance criteria you drafted) when Phase 0 found any.

Do not ask whether to run the briefing if the user already said "without the briefing" or chose ship mode. Do not
ask things the overlay or the tracker already answers. If every answer is the recommended one, say so in one line.

## 3. Record and stamp

Write each decision and whether the recommendation was taken into the run record's Phase 0 "Decisions" list, update
the tier if it moved, then stamp `<!-- phase: 1 done=<ts> -->`.

Gate: Explore findings written in the run record · one batched question answered · tier confirmed.

Source for the shape: feedback memory 2026-10-19 (four cards shipped in one afternoon with this pattern).
