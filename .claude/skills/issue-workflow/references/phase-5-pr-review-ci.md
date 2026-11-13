# Phase 5 - PR, review, CI

The pull request is the unit of change control. Everything a reviewer, a future debugger, or an auditor needs lives
in it, not in chat.

## 1. Open the PR (or, for `direct-push`, skip to Phase 6)

1. Commit per `commit_style`; push the branch; open the PR against `base_branch` with the body built from
   `assets/pr-body.md` (Summary with the tracker link, Risk tier, Test plan with real counts, Rollback, Verify after
   merge). Obey `text_rules` in the body.
2. Keep the diff reviewable: roughly one concern, a few hundred lines; split it when it is not.
3. Record `<!-- pr: n=<num> base=<base_branch> head=<sha> ... -->` in the run record as soon as the PR exists; add a
   new `pr:` line every time the head changes.
4. If `gh pr edit` fails with a GraphQL projectCards error (a known trap), PATCH the body through `gh api` instead.

## 2. Wait for CI on the current head SHA

Required checks must pass on the latest commit, not on an earlier push. Use `gh pr checks <n>` or
`gh run list --commit <sha> --json databaseId,conclusion,headSha` and fill in `ci_run=`, `ci_head=`, `ci=` on the
`pr:` marker. A red run is read, not retried blindly: fix, push, and wait again on the new SHA. Never merge red,
never merge on a green that belongs to an older SHA.

## 3. Triage the review bot

When `ci.review_bot` names a marker, read that comment in full. For every finding decide: fixed (push, new SHA,
wait again) or dismissed with a reason that survives a read of the code. Never copy its scores anywhere; the bot
over-reports and its numbers are not evidence. Record `<!-- review: source=bot findings=N fixed=M dismissed=K -->`.

## 4. Fresh-context reviews (tier T1 and up)

Run `/code-review` and `/security-review` on the diff as fresh-context subagents: give them the diff, the brief, and
the tier, not your conclusions. Triage their findings the same way and record a `review:` marker per source. The
author's self-review is not independent; this is.

## 5. Merge, one at a time

Merge only on the user's explicit per-PR approval ("merge it once CI passes" pre-approves that one merge). Use the
repo's merge method. Merge one PR at a time and, when the base branch auto-deploys, wait for that deploy run to
finish before merging anything else: stacked merges have raced the deploy twice. Fill in `merged=<sha>` on the
`pr:` marker and stamp `<!-- phase: 5 done=<ts> -->`.

Gate: PR body complete · CI green on the final head SHA · bot and fresh-context findings each fixed or dismissed
with a reason · merge approved per PR · one merge in flight.

Sources: required checks on the latest SHA (https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches);
Google code review standard and speed (https://google.github.io/eng-practices/review/reviewer/standard.html,
https://google.github.io/eng-practices/review/reviewer/speed.html); ISSUES_LOG 2026-06-22-02 and 2026-09-23-01 (stacked
merges, concurrent deploys).
