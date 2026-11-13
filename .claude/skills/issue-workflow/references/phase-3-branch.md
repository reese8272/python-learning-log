# Phase 3 - Approve and branch

## Approval

Wait for explicit confirmation. "Just go" or "yes" counts. Quote the approval in the run record. If the approach
changed during discussion, update the brief and the decision-log draft before anything else; the deviation is the
most valuable line in the log.

T2 design visibility: when the overlay's `tracker.transitions.accepted_by` names a person, post the approved brief
(problem, approach, threat model, rollback) to the tracker entry now, before code exists, through the tracker skill
or an approved write. `t2_design_review = "wait"` means stop here until they reply; `"post-and-proceed"` means
continue and let the comment do its job. The second human should see the design, not only the result.

## Branch

1. `git -C <repo_dir> fetch origin` and confirm the tree is clean (the Phase 0 baseline said so; re-check).
2. Never commit on a branch in `protected_branches`. If HEAD is on one, switch away first.
3. `git switch -c <branch_pattern filled in> origin/<base_branch>`. The branch starts from the remote base, not
   from whatever local branch happens to be checked out.
4. For `ship_model = "direct-push"` there is no branch: work on `base_branch`, and the push in Phase 6 is the ship.

Write the branch name and its base SHA in the run record.

## Commit and text discipline

- Follow `commit_style`: an imperative summary line, a body that says why, and the attribution trailer the session
  requires. One concern per commit; a commit should be revertible on its own.
- Obey every `text_rules` entry in code, docs, commit messages, and PR bodies (for example 7-bit ASCII only).
- Run the local CI chain under the overlay's `toolchain` versions (for Node: `nvm use <version>`; for Python: the
  pinned interpreter). Green under a newer local toolchain proves nothing about CI.
- Never run anything in the overlay's `forbidden` list, and never touch servers: verification happens through the
  public surface.

Stamp `<!-- phase: 3 done=<ts> -->`.

Gate: approval quoted · branch created from the remote base (or direct-push declared) · T2 brief posted when an
acceptor is named.

Sources: trunk-based development (https://trunkbaseddevelopment.com/); Conventional Commits
(https://www.conventionalcommits.org/en/v1.0.0/); small CLs (https://google.github.io/eng-practices/review/developer/small-cls.html).
