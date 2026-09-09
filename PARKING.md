# PARKING.md — system ideas, parked

**This file exists because of one number:** 28 system/card commits against 17 `/learn`, 2 `/sharpen`, 2 `/drill` since 2026-06-01. System-tinkering is the most sophisticated procrastination available here, because from the inside it is indistinguishable from progress.

---

## The rule

> **The system may only be changed during an `/audit`.**
>
> Outside an audit, a system idea — a new command, a new file, a restructure, a renamed block, a better tracker, a smarter format — goes here as **one line** and **is not built.** Not that day, not that night, not "while I'm in here anyway."

This costs one line to obey. It removes the only mechanism by which this system has ever eaten itself.

**The one exception:** a genuine *contradiction or breakage* — a path that doesn't exist, a rule that references a retired mechanism — is a **repair**, not a change. Fix it and note it.

**What happens to these lines:** at the next `/audit`, every line gets one of three dispositions — **build it** (at most one, and only after something was cut), **park again** (explicitly, with a note), or **kill it** (most of them). A line parked across three audits gets killed. Nothing is silently carried.

**Most of these should die here.** That's not the file failing — that's the file working. The parking lot's real job is to let a good idea die quietly at 11pm instead of getting built.

---

## Parked

*Format: `YYYY-MM-DD — one line. (why it appealed)`*

<!-- add lines below; do not build them -->

2026-09-08 — `/plan-tomorrow`: run the nightly build on demand instead of waiting for 9pm. (Appealing because the day changes after 9pm and the plan goes stale. **Parked at audit 1 of 3** — it is a second addition and the audit allows one; the nightly build was it. Revisit only once the nightly build has cleared its start condition, since an on-demand rerun of a task nobody reads is two ways of generating the same noise.)

---

## Killed / Built

*Moved here at audits, with the date and disposition. Kept so the same idea doesn't get re-proposed every month.*

| Date | Idea | Disposition |
|---|---|---|
| 2026-08-27 | *(file created — nothing parked yet)* | — |
| 2026-09-08 | **The nightly build** (automated 9pm scheduler → 3 cued calendar blocks) | ✅ **Built** — audit 1's one addition, on probation with a start condition. Never parked; built outside the Change Window on 08-30 and ratified retroactively at the audit. Paid for with 5 subtractions. See `SCHEDULER.md`, `DECISIONS.md` 2026-09-08. |
