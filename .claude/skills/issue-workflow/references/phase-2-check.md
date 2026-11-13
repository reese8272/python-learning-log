# Phase 2 - Check: research with evidence, then brief

Now, and only now, settle the approach. Two hard rules govern this phase; they are unchanged from v3 because they
have caught real traps (TextField max_length, react-router 7, the DRF detail-action permission path).

**Rule 1 - live lookup, never memory.** When picking or deciding any standard, framework, library, pattern, or
version, look it up live against current documentation or an accredited source. Training has a cutoff and these
facts move. Use `WebSearch` / `WebFetch`, the `best-practices` skill, and the relevant SDK docs for any
external-service decision (the `/claude-api` skill for Anthropic). The value is the *process* (how we reliably reach
a current, correct choice every time), not a remembered snapshot.

**Rule 2 - no source, no approach (HARD GATE).** An approach only qualifies for the brief if it is backed by
concrete documentation with a literal link - official docs, release notes, a maintainer's guide, or an accredited
engineering source - that you actually fetched and read this session, not a link recalled from memory. If the search
does not surface support for a candidate approach, it does not become the approach. Vary the search terms, go to the
official docs directly, check the project's GitHub issues and release notes for deprecations. If after an exhaustive
search nothing authoritative supports any candidate, do not silently pick one: bring the user what was searched,
what was found, and a recommended path, and let them decide.

For each non-trivial choice capture: the current de-facto standard, the maintained options, known failure modes,
recent deprecations, and the literal URL where each fact was found.

## Security-by-design and reversibility (new in v4)

- Tier T2: read `references/security.md` first and answer the four threat-modelling questions for this change
  (what are we working on, what can go wrong, what will we do about it, did we do enough). Three to five STRIDE-lite
  bullets are enough; the point is to find the new input, trust boundary, or data exposure before code exists.
- Every tier: decide how the change is undone. "Revert the PR" is fine when the change is a single reversible
  commit. A schema change, a data backfill, a deleted field, or an external side effect needs expand/contract, a
  flag, or a named backup. "Not reversible" is an honest answer and bumps the tier to T2.
- T1 and up: state the data volume the hot path sees and whether a per-row query or an unbounded loop is possible.

## The brief

Present it in exactly this format and stop:

> **Issue N - [title]** (tier Tn, mode)
> **Problem:** [the problem, as we now jointly understand it]
> **Approach:** [specific pattern, library, or architecture]
> **Why for this project:** [1-2 sentences tying it to the stack, constraints, and decision log]
> **Documentation:** [literal URL(s) backing the approach, each labelled with the claim it supports and verified
> fetched this session]
> **Alternatives ruled out:** [what was considered and why it lost, with links where a source drove the ruling-out]
> **Threat model:** [T2: the STRIDE-lite bullets; T0/T1: "no new trust boundary or data exposure" if true]
> **Rollback:** [how this is undone]
> **Scale:** [data volume on the hot path and the N+1 risk, or "n/a: no data path"]
> **Good to go?**

A brief with an empty or hand-waved **Documentation** field is invalid; go back and search more. Copy the brief into
the run record and tick the threat / rollback / migration items there with typed evidence (`url=` for fetched docs,
`file=` for the code you read).

## Decision-log seed

The approved brief is the decision record. Draft the entry now in the format the overlay names
(`what-why-source-date` for workspace logs per the global CLAUDE.md rule; `do-dont-why-evidence` for repo rule logs).
Only a T0 change with no alternatives may skip it, with a one-line reason in the run record.

Stamp `<!-- phase: 2 done=<ts> -->`. **Do not write implementation code until the user confirms.**

Sources: OWASP Threat Modeling Cheat Sheet (https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html);
MADR decision records (https://adr.github.io/madr/); Parallel Change (https://martinfowler.com/bliki/ParallelChange.html);
Google SRE launch checklist (https://sre.google/sre-book/launch-checklist/).
