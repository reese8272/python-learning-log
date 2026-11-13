# Overlay schema: `<project>/.claude/issue-workflow.toml`

`gate.py overlay <path>` enforces the types and required keys below and warns on the combinations that will
collapse a phase. Unknown top-level keys are errors (they are almost always typos). All paths are relative to the
project directory (`${CLAUDE_PROJECT_DIR}`), not to `repo_dir`.

| Key | Type | Required | Read in | Meaning |
|---|---|---|---|---|
| `project` | string | yes | all | label in run records and summaries |
| `ship_model` | `pr-then-promote` / `trunk-pr` / `direct-push` / `manual` | yes | 3, 5, 6 | the shape of shipping; decides which of phases 5/6 apply |
| `repo_dir` | string | no (`.`) | 0, 3 | git repo relative to the project dir, for workspaces that wrap a repo |
| `base_branch` | string | yes | 3, 5 | feature branches start here and PRs target it |
| `protected_branches` | list | no | 3 | never commit directly on these |
| `branch_pattern` | string | no | 3 | e.g. `reese/<id>-<slug>` |
| `commit_style` | string | no | 3 | one line describing the commit convention |
| `text_rules` | list | no | 0, 3, 5 | rules echoed in Phase 0 and obeyed in code, commits, PR bodies |
| `state_doc` | string | no | 0, 7 | the status / session-log doc (`docs/STATUS.md`, `docs/PROJECT_STATE.md`) |
| `toolchain` | table | no | 3, 4 | versions CI uses (`node`, `python`, `runner`); run the local chain under them |
| `[ci]` | table | no | 4, 5 | `local_chain` (list, required inside the table), `provider`, `required_checks`, `review_bot {marker, trust}` |
| `audit_cmds` | list | no | 4 | dependency audits to run when a manifest or lockfile changed |
| `[migrations]` | table | no | 2, 4, 6 | `check_cmd`, `auto_apply_on_deploy`, `rollback`, `backup_tool` |
| `[[environments]]` | array of tables | no | 6 | each: `name`, `deployed_by`, `verify` (list), optional `rollback`, `watch_minutes` |
| `[tracker]` | table | no | 0, 3, 7 | `kind` (required), `board` or `path`, `id_format`, `skill`, `t2_design_review`, `secondary`, `transitions {start, shipped, accepted_by}`, `evidence_comment` |
| `[decision_logs]` | table of tables | no | 2, 7 | each: `path`, `format` (`what-why-source-date` or `do-dont-why-evidence`), optional `when` |
| `[handoff]` | table | no | 7 | `kind` (`single` / `lane`), `file`, `commit` |
| `[run_record]` | table | no | 0 | `dir` (required inside the table), `commit` |
| `forbidden` | list | no | 0, 3, 6 | actions never taken in this project; echoed verbatim in Phase 0 |
| `[comms]` | table | no | 7 | `audience`, `rule` for the release note or email draft |
| `changelog` | string | no | 7 | path of a changelog that gets a line per shipped change |

## `deployed_by` values and what Phase 6 does with them

| Value | Phase 6 behaviour |
|---|---|
| `auto-on-merge-to:<branch>` | after the merge, wait for the deploy run on that branch, run `verify`, stamp `deploy:`; the gate also requires a merged `pr:` marker with `base=<branch>` |
| `promotion-pr:<branch>` | reopen Phase 5, build the promotion PR with its own evidence, its own `pr:` marker with `base=<branch>`, then `deploy:` as above |
| `manual-dispatch:<workflow>` | ask the user to trigger it (or trigger it on approval), then wait, verify, stamp |
| `human:<name>` | hand off with a `handoff:` marker naming the person; SHIPPED is allowed with the handoff stamp |

## Collapsing rules

- No `[ci]`: Phase 4 still runs the project's own test command; Phase 5 has no CI wait, so the gate only needs the
  PR to be merged (or, for `direct-push`, a `push:` marker).
- No `[[environments]]` and `ship_model = "direct-push"`: Phase 6 is "push, then confirm the push landed on the
  remote" (`push:` marker with `confirmed=`).
- No `[tracker]`: Phase 0 and 7 skip transitions and say so in the run record.
- No `[decision_logs]`: the global rule applies, `DECISIONS.md` at the project root in `what-why-source-date` form.
