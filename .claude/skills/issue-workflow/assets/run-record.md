# Run record: {id} ({project})

<!-- run: id={id} mode={mode} tier={tier} started={started} -->

Marker grammar (gate.py parses these; humans read the rest):
`<!-- phase: N done=<ts> -->` · `<!-- phase: N reopened=<ts> reason="..." -->` ·
`<!-- evidence: cmd="<command>" exit=0 -->` · `<!-- evidence: file=path:line -->` · `<!-- evidence: url=https://... -->` ·
`<!-- evidence: note="..." -->` (advisory only) · `<!-- pr: n=<num> base=<branch> head=<sha> ci_run=<id> ci_head=<sha> ci=success merged=<sha> -->` ·
`<!-- review: source=bot|code-review|security-review findings=N fixed=M dismissed=K -->` ·
`<!-- deploy: env=<name> run=<id> attempt=1 verify=<ok>/<total> at=<ts> -->` · `<!-- handoff: env=<name> to="<person>" at=<ts> -->` ·
`<!-- push: branch=<b> sha=<sha> confirmed=<ts> -->` (direct-push projects). Timestamps are ISO 8601 UTC, e.g. 2026-10-20T19:50Z.
Every `- [x]` needs an evidence marker on the same line or the line right after it.

## 0. Ground
<!-- section: name=ground -->
- Overlay: `{overlay}` · Baseline: repo=`{repo_dir}` branch=`{branch}` head=`{head}` dirty_files={dirty} upstream=`{upstream}`
- Tracker ref: {tracker_ref}
- Mode: {mode} · Tier: {tier} · Tier reasoning:
- Forbidden actions echoed from the overlay:
- Definition of ready
  - [ ] acceptance criteria exist, are testable, name the user, and bound the scope (or were drafted and approved below)
  - [ ] tracker moved to the "start" transition (or noted why not)
- Decisions from the batched question (option chosen, recommendation taken y/n):

## 1. Understand
<!-- section: name=understand -->
- (learn) attempt summary / articulation readout, or (ship) Explore findings:

## 2. Check and brief
<!-- section: name=brief -->
- Problem:
- Approach:
- Why for this project:
- Documentation (fetched this session):
- Alternatives ruled out:
- Scale (data volume on the hot path, N+1 risk):

### Threat model
<!-- section: name=threat required=T2 -->
- New inputs / trust boundaries / data exposed, STRIDE-lite:
  - [ ] no new unauthenticated surface, or it is listed here with its permission class
  - [ ] no new data leaves the server that the caller could not already read

### Rollback
<!-- section: name=rollback required=T1 -->
- [ ] how this change is undone is written here (revert PR / flag / expand-contract / "not reversible" bumps tier to T2)

### Migration safety
<!-- section: name=migration required=T2 -->
- [ ] no schema or data migration in this diff (evidence: git diff --name-only against the base, filtered to migrations), OR every item below
- [ ] migration check command clean
- [ ] backward-compatible with the running code (expand before contract)
- [ ] data migration has a reverse, or its irreversibility is written in the brief
- [ ] backup named (tool + tag) before the production migrate

## 3. Approve and branch
<!-- section: name=branch -->
- Approval quote:
- Branch: · base: · DECISIONS entry drafted at:
- (T2, when the tracker names an acceptor) brief posted to the tracker at:

## 4. Build
<!-- section: name=build -->
Per unit of work, copy the checklist from references/phase-4-build.md and tick with evidence.

### Unit 1:
- [ ] ...

### Full local CI chain under the CI toolchain
- [ ] every command in overlay ci.local_chain ran green

## 5. PR, review, CI
<!-- section: name=pr -->
- PR markers (one per PR; add a new line each time the head changes):
- Review bot triage (finding -> fixed / dismissed with reason):
- Fresh-context reviews (T1+):
- Merge approval quote:

## 6. Deploy, verify, watch
<!-- section: name=deploy -->
- Per environment: deploy marker, the verify commands and their results, watch window outcome, rollback used y/n.

## 7. Close
<!-- section: name=close -->
- [ ] docs updated (state doc, decision log(s), tracker entry)
- [ ] tracker evidence posted and moved to the "shipped" transition (never to the acceptor's state)
- [ ] changelog / release note line (if the overlay names one)
- [ ] /log-issue run if a non-trivial root cause was found (or "none found")
- [ ] /close-out run for the lane
- Verdict (quote `gate.py run --verify --metrics`):
