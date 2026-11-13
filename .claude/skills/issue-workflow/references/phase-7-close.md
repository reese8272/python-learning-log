# Phase 7 - Close

This phase judges, records, and hands off. It does not patch code: anything below the bar goes back to Phase 4 with
a reopen stamp.

## 1. Judge

Run `python3 ${CLAUDE_SKILL_DIR}/scripts/gate.py run <record> --overlay <overlay> --verify --metrics --cwd <project dir>`
and read every row. A FAIL row is fixed at its source (missing evidence is gathered, not typed; a red CI is a
reopen). Spot-check the single riskiest change in the diff against its acceptance criterion by hand once more.

## 2. Cleanup sweep

- [ ] no TODO without an owner, no commented-out blocks, no leftover debug output
- [ ] temp files and scratch artifacts removed; nothing new that belongs in `.gitignore` is unignored
- [ ] every new config value is in the committed env example with a description
- [ ] no dead code left behind by the change

## 3. Documents

- [ ] the overlay's `state_doc` gets a status line and a session-log entry
- [ ] the tracker entry: acceptance criteria ticked, status set to the "shipped" wording, PR and deploy links added
- [ ] decision log(s): the approved brief written as an entry in each log the overlay names, in that log's format
      (`what-why-source-date`: What changed or was decided / Why / Source or evidence / Date;
      `do-dont-why-evidence`: an imperative rule heading with Do / Don't / Why / Evidence, only when a code-change
      rule changed)
- [ ] `changelog` (when named): one line under Added / Changed / Fixed / Security
- [ ] project `CLAUDE.md` updated if this issue resolved a standing item
- [ ] core understanding files stubbed in Phase 0 are populated now

## 4. Tracker evidence and transition

Post the evidence comment the overlay describes (environment, revision or bundle hash, what to check, the PR link)
through `tracker.skill` when set, otherwise by an approved write. Move the entry along `transitions.shipped`.
Never move it to the acceptor's state; acceptance belongs to `accepted_by`.

## 5. Learning and handoff

- `/log-issue` when a non-trivial bug was root-caused during the run and the obvious hypothesis was wrong; write
  "none found" in the run record otherwise.
- `[comms]` named an audience: draft the note in that audience's register (for state editors: short, plain,
  re-read the thread first, engineering detail in a Notes block) and leave it for the user to send.
- `/close-out` for the lane this run touched (`handoff.kind = "lane"` means the lane table in the project
  `CLAUDE.md` decides the file). Include the handoff in the same commit only when `handoff.commit` is true.
- Learn mode, optional: `/post-mortem` on the two or three decisions that taught the most.

## 6. Final readout

Stamp `<!-- phase: 7 done=<ts> -->`, run the gate once more, and end with:

- **SHIPPED**, **NEEDS WORK**, or **BLOCKED**, followed by the gate table and the metrics block verbatim.
- SHIPPED means every environment this run owns is verified live or handed off with a stamp. It never means
  accepted.
- Anything deferred, descoped, or left for a named person is listed explicitly. A partial result is never reported
  as complete.
- A `/brief`-shaped summary for the user: bottom line, where things stand, what is in the way, their call.

Sources: Keep a Changelog (https://keepachangelog.com/en/2.0.0/); DORA metrics (https://dora.dev/guides/dora-metrics-four-keys/);
global CLAUDE.md DECISIONS.md and ISSUES_LOG rules.
