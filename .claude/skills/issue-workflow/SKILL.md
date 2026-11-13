---
name: issue-workflow
description: >-
  Drive one issue, ticket, or Trello card from pickup to verified-live and closed, at business grade: ground in the
  project, understand (learn or ship mode), research the approach with fetched sources, approve, branch, build with
  evidence-backed checks, PR with CI and independent review, deploy and verify through the public surface, close with
  docs, tracker evidence, and a gate-validated run record. Invoke when the user runs /issue-workflow, says "start
  T87", "work issue 190", "pick up IT-12", "next card", or "run the issue workflow". Not for ad-hoc questions or
  reviews; those have their own skills.
argument-hint: "[issue-id] [learn|ship]"
arguments: issue mode
disable-model-invocation: true
allowed-tools: Read Bash(python3 ${CLAUDE_SKILL_DIR}/scripts/*)
metadata:
  version: 4
  last_verified: 2026-10-20
---
<!-- SYNCED COPY - do not edit here.
     Canonical dir: ~/.claude/skills/issue-workflow/
     After editing the canonical files, rerun: ~/.claude/scripts/sync-issue-workflow.sh -->

# /issue-workflow v4

Run the full issue workflow for `$issue` in mode `$mode` (`learn` or `ship`; ask once if omitted, see below).

This is a process, not a checklist to rush. Eight phases, each with a gate, each with its own reference file that
you read on entry. Quality is enforced while building; shipping means verified live, not merged; and every run
leaves a record on disk that `scripts/gate.py` validates. The references live next to this file under
`${CLAUDE_SKILL_DIR}/references/`; read the one named at the start of each phase before doing that phase's work.

## Standing rules (every phase)

1. **Ask with a recommendation.** Whenever something the user wants is unclear (scope, priority, a tradeoff, what
   "done" means) stop and ask, with (a) exactly what is unclear and why it matters, (b) the realistic options with
   tradeoffs, and (c) your recommended option with the evidence behind it. Never a bare menu. In ship mode the
   questions are batched into one call.
2. **No source, no approach.** Standards, libraries, patterns, and versions are looked up live and cited with a
   literal URL fetched this session. A brief without documentation is invalid.
3. **Tools first, judgment second.** Every checked item in the run record carries evidence: a command and its exit
   code, a file and line, or a fetched URL. A note is reasoning, not evidence.
4. **Never report a partial result as complete.** Deferred, descoped, or handed-off work is listed by name.
5. **Obey the overlay.** The project's `.claude/issue-workflow.toml` names the branch model, CI chain, environments,
   tracker, decision logs, text rules, and forbidden actions. Echo `forbidden` and `text_rules` aloud in Phase 0 and
   never cross them. Never touch servers; verify through the public surface.
6. **Absolute paths**, always. The shell cwd drifts between directories mid-session.
7. **Shipped is not accepted.** The final verdict is SHIPPED / NEEDS WORK / BLOCKED. Acceptance is the tracker
   owner's word and never this skill's.

## Mode

- `learn`: Standing rule #0 (struggle first) and the adaptive grill/teach phase with its hard articulation gate.
  The user attempts the problem unaided before anything is explained. Read `references/phase-1-learn.md`.
- `ship`: an Explore pass followed by one batched scoping question with recommended options, then the brief. Read
  `references/phase-1-ship.md`.
- Mode omitted: ask once, recommending `ship` for tier T0/T1 work in an area the user has shipped before (check
  the run-record directory for earlier ids touching the same files) and `learn` for a new area or a T2 change. The
  user's answer is final for the run and is written into the run record. Do not re-ask it later.

## Risk tier

Classify in Phase 0 from what the change touches (`references/risk-tiers.md`): **T0** docs/copy/style only; **T1**
logic or UI without a new trust boundary, schema change, or irreversible step; **T2** auth, permissions,
migrations, data backfills or deletes, money, secrets or security config, CI or deploy, public API shape, new or
upgraded dependencies, or anything that cannot be undone. The tier switches extra gates on (threat model, migration
checklist, independent review, watch window). It can rise mid-run freely and fall only with a logged decision.

## Run record

Phase 0 creates `<run_record.dir>/<id>.md` with `scripts/new_run.py`. From then on every phase stamps itself
(`<!-- phase: N done=<ts> -->`), every checked item carries an evidence marker, every PR gets a `pr:` line, every
environment a `deploy:` or `handoff:` line. The grammar is at the top of the record. Validate at any time with:

```
python3 ${CLAUDE_SKILL_DIR}/scripts/gate.py run <record> --overlay <overlay> [--verify] [--metrics] --cwd <project dir>
```

The Phase 7 verdict must quote the output of the `--verify --metrics` form. A reopened phase gets a
`reopened=` stamp with a reason; the gate orders by the latest stamp per phase, so going back is normal, not a
failure.

## Phase 0 - Ground (read `references/phase-0-ground.md`)

Validate the overlay (`gate.py overlay`), run the sync drift check if the sync script exists, read the project's
CLAUDE.md, state doc, tracker entry, decision logs, and handoff file; stub any missing core doc. Echo `forbidden`
and `text_rules`. Check the definition of ready (acceptance criteria exist, are testable, name the user, bound the
scope; draft them if not). Classify the tier. Create the run record with the git baseline, test counts, and the
base branch's latest CI result; a dirty tree stops the run. Move the tracker to its "start" transition through the
overlay's tracker skill or an approved write. Finish with a 3-5 line grounding summary.

**Gate:** overlay validated or declared absent · rules echoed · DoR met or AC drafted · tier written · run record
with baseline · tracker transition attempted.

## Phase 1 - Understand (read `references/phase-1-learn.md` or `references/phase-1-ship.md`)

Learn: the user's unaided attempt first, then grill or teach, one question at a time, until they can state the
problem, the data and code shape, why this approach, and the blast radius if it is wrong. Ship: one Explore agent
on the files in scope, a grep of `~/.claude/ISSUES_LOG.md` for the symptoms, then exactly one `AskUserQuestion`
batch with recommended options for the scope decisions, the tier, and any drafted acceptance criteria. No
implementation code in this phase.

**Gate:** learn: articulation readout written · ship: Explore findings and the batched answers written.

## Phase 2 - Check and brief (read `references/phase-2-check.md`; T2 also `references/security.md`)

Live lookup, never memory; literal fetched URLs or the approach does not qualify. Capture for each non-trivial
choice the current standard, maintained options, failure modes, deprecations, and the URL. T2: answer the four
threat-model questions. Every tier: decide the rollback. T1 and up: state the scale. Present the brief in the fixed
format (Problem, Approach, Why for this project, Documentation, Alternatives ruled out, Threat model, Rollback,
Scale, Good to go?) and stop. Draft the decision-log entry from the brief.

**Gate:** brief presented with documentation, threat, rollback, and scale fields · decision entry drafted · no
code written.

## Phase 3 - Approve and branch (read `references/phase-3-branch.md`)

Wait for an explicit go and quote it. T2 with a named acceptor: post the brief to the tracker entry before any code.
Fetch, confirm a clean tree, never commit on a protected branch, create the branch from the remote base with the
overlay's pattern (direct-push projects work on the base branch). Commit per `commit_style`; obey `text_rules`;
run everything under the CI `toolchain` versions.

**Gate:** approval quoted · branch from remote base or direct-push declared · T2 brief posted when required.

## Phase 4 - Build (read `references/phase-4-build.md`)

Tests alongside code; failing test first for bugs; each acceptance criterion mapped to a test or a named manual
check; Pareto, not exhaustive. After every commit-sized unit copy the per-unit checklist into the run record and
tick each item with evidence: syntax and types, bugs and logic, smells, compliance, performance, formatting,
security, and accessibility when UI changed. An unticked item means stop and fix now. T2: the migration checklist.
Dependency or manifest changes: the security reference's audit items. Before leaving: the overlay's `ci.local_chain`
under the CI toolchain, then the full suite.

**Gate:** every unit fully ticked with evidence · local CI chain green under the CI toolchain · full suite green ·
migration list done when applicable.

## Phase 5 - PR, review, CI (read `references/phase-5-pr-review-ci.md`)

Open the PR from `assets/pr-body.md` (Summary with tracker link, Risk tier, Test plan with counts, Rollback, Verify
after merge). Record a `pr:` line and update it on every push. Wait for CI green on the final head SHA; never merge
red or on a stale green. Read the review bot, fix or dismiss each finding with a reason, never copy its scores. T1
and up: `/code-review` and `/security-review` as fresh-context subagents on the diff. Merge only on the user's
per-PR approval, one PR at a time, waiting for an auto-deploy to finish before the next merge.

**Gate:** PR body complete · CI green on final head · every finding fixed or dismissed with a reason · merge
approved per PR · one merge in flight.

## Phase 6 - Deploy, verify, watch (read `references/phase-6-deploy-verify.md`)

For each overlay environment in order: deploy per `deployed_by` (auto on merge, promotion PR with its own Phase 5
and `pr:` line, manual dispatch, or a human handoff), verify with every command in its `verify` list through the
public surface, stamp `deploy:` with `verify=total/total` (or `handoff:`), watch for `watch_minutes` on T1 and up,
and roll back on user-visible breakage, recording the redeploy as `attempt` +1 with a three-sentence blameless
note. Direct-push projects: push, confirm the remote, stamp `push:`.

**Gate:** every environment stamped with full verification or a handoff · watch done or waived by tier · any
rollback recorded with its redeploy.

## Phase 7 - Close (read `references/phase-7-close.md`)

Run the gate with `--verify --metrics`; fix FAIL rows at their source. Cleanup sweep. Update the state doc, the
tracker entry (criteria ticked, links added), every decision log the overlay names in its own format, the
changelog if named, and any stubbed core doc. Post the evidence comment and move the tracker along the "shipped"
transition, never to the acceptor's state. `/log-issue` when a root cause was found. Draft comms for the named
audience. `/close-out` for the lane. Learn mode: optional `/post-mortem`.

**Gate:** gate PASS with verify · docs and tracker updated · evidence posted · handoff refreshed.

## Final readout

One line, **SHIPPED**, **NEEDS WORK**, or **BLOCKED**, then the gate table and metrics block verbatim, then what was
deferred or handed to whom, then a `/brief`-shaped summary (bottom line, where things stand, what is in the way,
the user's call). SHIPPED is earned only by stamps in the record, never by vibes.

## Pointers

- Overlay keys and collapsing rules: `references/overlay-schema.md`; example: `assets/overlay.example.toml`.
- Sibling skills this workflow invokes rather than restates: `/code-review`, `/security-review`, `/simplify`,
  `/production-security` (T2 auth or secrets), `/tdd` (learn mode build loop), `/post-mortem`, `/log-issue`,
  `/close-out`, `/brief`, `best-practices`, and the project's tracker skill when the overlay names one.
- Canonical copy: `~/.claude/skills/issue-workflow/`; project copies are written by
  `~/.claude/scripts/sync-issue-workflow.sh` and must not be edited in place.
