# Phase 6 - Deploy, verify, watch

A merge is not a ship. The change is shipped when it is observably live on every environment this run owns, and
each one has evidence in the run record. Work through the overlay's `[[environments]]` in order.

## Per environment

1. **Deploy** per `deployed_by`:
   - `auto-on-merge-to:<branch>`: find the run (`gh run list --branch <branch> --limit 3 --json databaseId,status,conclusion,headSha`),
     `gh run watch <id>` until it finishes. A failed deploy is a Phase 4 reopen, not a retry loop.
   - `promotion-pr:<branch>`: reopen Phase 5 (`<!-- phase: 5 reopened=<ts> reason="promotion PR" -->`), build the
     promotion branch the way the project does it (for WorldCovers: branch off `main`, cherry-pick the staging
     squash commits in order, prove the tree matches), open the promotion PR with its own evidence table, its own
     `pr:` marker with `base=<branch>`, CI on its own head, and a named human merging it when the overlay says so.
   - `manual-dispatch:<workflow>`: ask the user to trigger it, or trigger it on approval; then watch as above.
   - `human:<name>`: hand off with `<!-- handoff: env=<name> to="<person>" at=<ts> -->` and the exact steps they run.
2. **Verify** through the public surface only, with every command in the environment's `verify` list, and record
   each as `cmd=` evidence. Typical: the health endpoint returns 200; the served bundle's hash changed and contains a
   string the change introduced; an anonymous probe of a new route returns 403 (live) rather than 404 (absent); a
   leak fix returns nothing it should not. Never SSH, never run management commands, never query the database when
   the overlay forbids it; and even when it does not, verify as a user would.
3. **Stamp** `<!-- deploy: env=<name> run=<id> attempt=<n> verify=<ok>/<total> at=<ts> -->`. `verify` must be
   `total/total` for the gate to pass.
4. **Watch** for `watch_minutes` (tier T1 and up): re-run the probes at the end of the window and look at whatever
   error signal the project has (CI health workflows, a log endpoint, the next scheduled job). Record the outcome.
5. **Roll back** when the verify fails or the watch shows user-visible breakage, using the environment's `rollback`
   text. Record the rollback as a new `deploy:` line with `attempt` incremented once the redeploy is verified, and
   write a three-sentence blameless note (what happened, why, what changes) in the run record.

## `direct-push` projects

Push `base_branch`, confirm the remote has the commit (`git ls-remote origin <branch>` equals local HEAD), and stamp
`<!-- push: branch=<b> sha=<sha> confirmed=<ts> -->`. If a scheduler or external reader consumes the branch, say
when it will next pick the change up.

## Two environments, two phases

For `pr-then-promote` projects the first environment is Reese's to ship and the second is usually someone else's to
accept. SHIPPED for this run means every environment has a `deploy:` or `handoff:` stamp; "accepted" is the
tracker's word and never this skill's.

Stamp `<!-- phase: 6 done=<ts> -->` after the last environment.

Gate: each environment has a `deploy:` stamp with full verify, or a `handoff:` stamp · watch window done or waived
by tier · any rollback recorded with its redeploy.

Sources: SRE launch checklist (https://sre.google/sre-book/launch-checklist/); blameless postmortems
(https://sre.google/workbook/postmortem-culture/); DORA four keys (https://dora.dev/guides/dora-metrics-four-keys/);
GitHub environments (https://docs.github.com/en/actions/deployment/targeting-different-environments/using-environments-for-deployment).
