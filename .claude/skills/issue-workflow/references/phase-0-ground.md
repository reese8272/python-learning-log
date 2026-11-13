# Phase 0 - Ground

Goal: know the project, the issue, the risk, and the rules before anything else is read closely. Everything here is
cheap; skipping it is how a session builds the wrong thing or breaks a rule it never saw.

## 1. Load the overlay and the project's memory

1. Overlay: `${CLAUDE_PROJECT_DIR}/.claude/issue-workflow.toml`. Run
   `python3 ${CLAUDE_SKILL_DIR}/scripts/gate.py overlay <path>` and read the warnings. If the overlay is absent,
   say so, proceed with generic defaults, and offer to write one from `assets/overlay.example.toml` in Phase 7.
2. If `~/.claude/scripts/sync-issue-workflow.sh` exists, run it with `--check`; drift means a stale copy of this
   skill is in play somewhere. Report it, do not fix it mid-run.
3. Read, in this order, whichever exist: the project `CLAUDE.md` (root and nested), the overlay's `state_doc`, the
   tracker entry for this issue, the decision log(s), the lane's handoff file, and any architecture or requirements
   doc the state doc points to. Use absolute paths; the shell cwd drifts.
4. Core understanding files that are missing (`CLAUDE.md`, the state doc, the tracker file, the decision log): create
   a minimal stub now (header, one-line purpose, `<!-- populated during issue close-out -->`). Note which ones you
   stubbed; Phase 7 populates them. Never block on this, never silently skip it.

## 2. Echo the rules you are bound by

Print the overlay's `forbidden` list and `text_rules` verbatim in your first message of the run. A rule that was
read but not said out loud is the one that gets broken three hours later.

## 3. Definition of ready

The issue is ready when its acceptance criteria exist, are testable (each one maps to a check you can run or a
thing a human can see), name who benefits, and bound the scope (what is explicitly out). If any of these is missing,
draft them from the tracker text and get them approved inside the Phase 1 batched question (ship mode) or at the
Phase 1 exit (learn mode). Record the AC list in the run record; Phase 4 maps tests onto it.

## 4. Classify the risk tier

Read `references/risk-tiers.md` and pick T0, T1, or T2 from what the change touches, not from how big it looks.
Write the tier and one line of reasoning in the run record. The tier can rise during the run; it can only fall with
a logged decision and the user's agreement.

## 5. Capture the baseline and open the run record

```
python3 ${CLAUDE_SKILL_DIR}/scripts/new_run.py --id <tracker id> --mode <learn|ship> --tier <T0|T1|T2> \
  --project-dir ${CLAUDE_PROJECT_DIR} --tracker-ref "<card or issue url/path>"
```

This writes `<run_record.dir>/<id>.md` with branch, HEAD, dirty-file count and upstream. Add the current test
counts and the latest CI conclusion on the base branch (`gh run list --branch <base> --limit 1`) by hand. If the
working tree is dirty, stop and ask: uncommitted work from another card must not ride along.

## 6. Move the tracker to "start"

Use the overlay's `tracker.transitions.start`. When `tracker.skill` is set, invoke that skill and let it handle the
fresh read, the dry run, and the approved write. Otherwise: Trello writes always dry-run first and are approved by
the user per call; markdown trackers get the status line edited in place. Write the resulting state (or the reason
you could not move it) in the run record.

## 7. Grounding summary and gate

End the phase with 3-5 lines: what this project is, where this issue sits, which files it will likely touch, the
tier, and the mode. Then stamp `<!-- phase: 0 done=<ts> -->` in the run record.

Gate: overlay validated (or declared absent) · rules echoed · DoR met or AC drafted for approval · tier written ·
run record exists with a baseline · tracker transition attempted and recorded.

Sources: Scrum Guide 2020, Definition of Done (https://scrumguides.org/docs/scrumguide/v2020/2020-Scrum-Guide-US.pdf);
NIST SP 800-218 SSDF PW.1 (https://csrc.nist.gov/pubs/sp/800/218/final).
