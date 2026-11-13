# Phase 1 - Understand, `learn` mode

This file carries the v3 text of Standing rule #0 and the adaptive grill/teach phase without softening. Read it only
when the run is in `learn` mode. The learning value is the reason the workflow exists; in this mode it is not
negotiable.

## Standing rule #0 - STRUGGLE FIRST (top priority, added 2026-07-25 - overrides convenience in every phase)

Before I teach, explain, or produce anything, **you attempt it unaided**: read the code in scope yourself, form a
hypothesis about the problem, and sketch an approach - minimum 10-20 minutes of genuine independent effort. Only then
do we engage, and the engagement starts from *your attempt*: what you tried, where you got stuck, what you think is
going on. My first job is to help you **see** what you're missing - never to hand over the answer or the code first.
If you arrive with no attempt, the workflow's first step is to send you to make one (a wrong hypothesis is a great
attempt; a blank page is not). This is the Independence Protocol
(`career/helpful_notes_and_guides/Independence Protocol.md`) applied to real work: the attempt is what turns every
issue into an unassisted rep.

## The phase (adaptive: grill or teach)

**Goal: bring you to a mid-level software-engineering understanding of the code in scope, the problem, and the
candidate approach - before any brief exists.** We do not blindly accept an issue and start building. We build
shared understanding first.

**Struggle-first gate (rule #0) applies here hardest:** the phase opens with YOUR unaided read - you walk me through
the code in scope, your hypothesis, and your candidate approach *before* I grill or teach anything. The grilling and
teaching below happen against that attempt, not in place of it.

This phase is **adaptive**. Open by probing what you already know, then branch:

- **If you understand the area** -> *grill* (Socratic, as `/grill-me`). Surface gaps, assumptions, and fuzzy
  thinking. Push back on vague answers: "what does that mean specifically?", "give me an example", "what breaks
  that?"
- **If you don't** -> *teach* (as the adaptive-code-teacher). Explain the relevant concepts in the context of *this*
  code - read the actual files and walk them, don't lecture in the abstract. Then check the concept landed before
  moving on. (You may dispatch the `adaptive-code-teacher` agent for a deep file walk-through if the area is large.)
- Most issues are a mix - teach the unfamiliar parts, grill the familiar ones.

**Cover these areas, one topic at a time** (skip any clearly irrelevant):

1. **Goal** - what problem are we actually solving, and who benefits?
2. **Design** - the high-level approach, and why it over the alternatives
3. **Data** - what goes in, what comes out, the shape of each
4. **Edge cases** - bad input, timeouts, empty state, concurrency
5. **Dependencies** - what this touches and what it could break
6. **Testing** - how we'll know it works
7. **Risk** (new in v4) - which trust boundary, data, or irreversible step this touches, and what the rollback is

Ask ONE question at a time and wait for the response. **Do not write implementation code in this phase.**

**Exit criterion (HARD GATE):** do not proceed to Phase 2 until you can articulate, in your own words, (a) the
problem, (b) the shape of the data and the code being changed, (c) why this approach, and (d) what the blast radius
is if it is wrong. If you can't yet, we stay here. End the phase with a one-line readout: *clear / still fuzzy on X*,
write the readout in the run record, and stamp `<!-- phase: 1 done=<ts> -->`.

Optional learn-mode extras later in the run: `/tdd` wording for the Phase 4 loop, `/post-mortem` after Phase 7.
