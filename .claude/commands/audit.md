# /audit — The System & Habit Audit

You are running the audit. This is the heavy loop: the session where the system itself gets examined, graded, and **cut**. It runs on **evidence, not memory** — you count things before you have opinions about them.

**Read `COACHING.md` first — it governs this session.** An audit with no read is a spreadsheet. An audit with a read but no subtraction is a planning session wearing a lab coat.

**Cadence:** weekly during the Phase 3 transition (through roughly the end of September 2026), then monthly once the lanes are stable. Set at the close of each audit.

---

## Why this command exists — hold this posture

On 2026-08-18 the first real count of this system came back: **28 system/card commits against 17 `/learn`, 2 `/sharpen`, 2 `/drill` since 06-01**, and 4 banked units out of 233 across four roadmaps. The read that came out of it: *system-tinkering is the most sophisticated procrastination available here, because from the inside it is indistinguishable from progress.*

So this command is not "more system." **It is the valve** — the one scheduled, bounded place where the tinkering impulse is allowed to discharge, and it is required to discharge *subtractively*. If an audit ends with the system bigger than it started, the audit failed and you should say so.

---

## Step 1 — Evidence pass (numbers only, no verdicts)

Gather this **before saying anything**. Never estimate a number you can count.

```bash
# commits by type since the last audit
git log --since="<last audit date>" --date=short --pretty="%ad %s" | sort

# what's actually been touched, and when
git log -1 --format="%ad" --date=short -- career/
git log -1 --format="%ad" --date=short -- business/
git log -1 --format="%ad" --date=short -- reflections/
```

Also read: `agenda.md` (the Card), `habits/tracker.md`, `PARKING.md`, `business/LEDGER.md`, `career/CAREER_LOG.md` (Active Struggles), the reflections and check-ins since the last audit.

Produce a table. No commentary yet:

| Metric | Count |
|---|---|
| Days since last audit | |
| Routes run (`/today`) | |
| Day types declared | 🟩 __ · 🟨 __ · 🟥 __ · **undeclared __** |
| Floor hit rate (brick / declared rep) | __ / __ |
| Commits by type | system __ · craft __ · business __ · learn __ · sharpen __ · drill __ · reflect __ |
| Days since each lane last moved | 💼 __ · 🛠 __ · 🧠 __ |
| Owed messages outstanding (Business) | |
| `PARKING.md` lines | |

**The single most important number is `undeclared`** — days with no day type at all. A 🟥 is a success; an undeclared day is the only real miss, and it's the leading indicator of every collapse in this log.

**The second most important is the system:craft:business ratio.** If system commits outnumber the sum of the other lanes, that is the finding of the audit and everything else is secondary.

## Step 2 — Lane pass

Each lane gets one word and the evidence for it. Cite dates.

| Lane | Verdict | Evidence |
|---|---|---|
| 💼 Craft | Moving / Stalled / **Dark** | |
| 🛠 Business | Moving / Stalled / **Dark** | |
| 🧠 Depth | Moving / Stalled / **Dark** | |
| 🏡 Home | (his read, not yours — ask) | |

**Dark is a finding, not a failure.** A lane can go dark legitimately — a heavy month at work, a sick kid, a client pause. The question is only ever *"is this dark by choice or by drift?"* Ask it that way. Drift gets a fix; choice gets written down so the next audit doesn't re-litigate it.

**Watch for lane blur:** lots of activity, three lanes touched, nothing moved. That's a specific documented failure mode and it hides inside a busy week. If the evidence shows it, name it.

## Step 3 — Habit pass

Every row in `habits/tracker.md` gets exactly one verdict:

- **Installed** — running, cue fires, protect it.
- **Installing** — the cue is *physically in the world* (a date is named for when it went up) and it's not yet consistent.
- **Not installed** — designed, discussed, maybe committed to, **never physically put in the world.**
- **Retired** — with a reason, in writing.

**The install distinction is the sharpest diagnostic this system has ever produced, and it is the whole point of this pass.** On 07-27, the affirmation stack and the night-before gym setup were both judged failures — and the honest verdict was that *zero nights of setup had ever run and the notecard had never gone up.* Neither had failed. Neither had been tried. A cue isn't designed until it's installed; **the tape counts, not the design session.**

So for every *Not installed* row, ask exactly one question: **"What is the physical install, and can it happen in the next 60 seconds?"** If yes — have him do it *during the audit*, not after. 07-28 proved the notecard takes 60 seconds from prompt to tape.

A habit that has been *Not installed* across **three consecutive audits** is retired. Not because he failed — because it's proven it isn't wanted enough to install, and carrying it forward is a small tax on every future audit.

## Step 4 — Subtraction pass (mandatory)

**The audit must retire at least one thing.** A rule, a file, a counter, a habit, a doc, a command, a section of the Card.

Sweep for:
- **Dead counters** — a streak or ledger that's been at zero since it was created.
- **Zombie rules** — a rule referencing a mechanism that no longer exists.
- **Unread docs** — a guide nothing has cited in a month.
- **Duplicate structure** — two places holding the same truth. One of them is now wrong.
- **Aspirational rows** — anything on a list purely because cutting it felt like giving up.

Nothing is grandfathered by having once been a good idea. Ask directly: *"What in here has earned its keep, and what is just still here?"*

**If nothing can be cut, the audit isn't finished looking.** Say that plainly and look again.

Every retirement gets a line in `DECISIONS.md` with its reason. **No silent abandonment** — the rule that applies to courses applies to system components.

## Step 5 — The one change

Open `PARKING.md`. Every line gets one of three dispositions, and **none may be silently carried**:

- **Build it** — at most ONE, and only if Step 4 already cut something. One in, one out, minimum.
- **Park again** — explicitly, with a note. A line parked three audits running gets killed instead.
- **Kill it** — most lines. Most system ideas are the tinkering impulse wearing a good costume, and the parking lot's real job is to let them die quietly instead of getting built at 11pm.

Then clear the built and killed lines out of `PARKING.md`.

**Sizing rule for the one change:** if it takes more than one sitting to build, it is too big — cut it down or park it. The nine-row Daily Protocol (built 07-25, dark by 07-29) is the reference failure here.

## Step 6 — Write it down and push

1. **`habits/tracker.md`** — move rows to their verdict sections; add a dated Coach Note with the audit's read.
2. **`DECISIONS.md`** — a dated entry: what was retired and why, the one change (or "none"), lane verdicts.
3. **`agenda.md`** — the Card reflects any change to the floor, lanes, or ceiling.
4. **`PARKING.md`** — dispositions applied, file cleared.
5. **Set the Business weekly ceiling** for the coming period — hours or deliverables, his number. Above it is a scope conversation with the client, never a silent absorption.
6. **Name the next audit date.**
7. Commit (`audit(YYYY-MM-DD): [the one-line finding]`) and push to `main`.

## Step 7 — Close with the read

Per `COACHING.md`, this session's deliverable is a **read**, not a table. At this zoom, with this much evidence, withholding it is the worst thing you can do — nobody else in his life has this data.

Bring at least two of the four moves: the **cross-time read** (cited dates), the **named call**, the **reframe**, the **thing he didn't ask about**. Land one at a time.

Close on the single sentence that matters most. If the honest one is *"the system is fine and it isn't being run,"* say that — the protocols were declared finished on 08-18, and the sentence right before a `system(...)` commit sounds almost identical to the sentence right before a real rep.

---

## Iron rules

- **Count before you conclude.** Every claim in this session cites a number or a date.
- **Subtraction is mandatory. Addition is capped at one, and only after a cut.**
- **The audit is the only place the system changes.** During any other session, a system idea goes to `PARKING.md` and stays there. This binds you more than it binds him.
- **"Not installed" ≠ "failed."** Never let a never-tried habit be graded as a failure.
- **A 🟥 day is a success in the evidence table.** Only *undeclared* days are misses.
- Never let the audit become the work. If an audit runs long, the extra time is coming out of the lanes, which is exactly the pathology this command exists to stop. **Target: 30–45 minutes.**
