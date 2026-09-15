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

2026-09-15 — **Protected lunch carve-out** in the nightly build (never schedule over ~12:00–13:00). (Asked for directly at audit #2 as part of the energy curve. **Parked, audit 1 of 3** — on the current calendar the only Flow window is 10:40–14:00, so a hard lunch block would cut it roughly in half. Revisit at audit #3 with a week of real placed blocks showing whether lunch is actually getting eaten through.)

2026-09-15 — **Raise the 3-block cap.** (Asked for at audit #2 — "a very very efficient schedule." **Parked, audit 1 of 3.** The cap is the Dalton & Spiller result and the nine-row Daily Protocol is the local body count: built 07-25, dark by 07-29. Revisit only after a full period where three blocks a day were actually worked.)

---

## Killed / Built

*Moved here at audits, with the date and disposition. Kept so the same idea doesn't get re-proposed every month.*

| Date | Idea | Disposition |
|---|---|---|
| 2026-08-27 | *(file created — nothing parked yet)* | — |
| 2026-09-08 | **The nightly build** (automated 9pm scheduler → 3 cued calendar blocks) | ✅ **Built** — audit 1's one addition, on probation with a start condition. Never parked; built outside the Change Window on 08-30 and ratified retroactively at the audit. Paid for with 5 subtractions. See `SCHEDULER.md`, `DECISIONS.md` 2026-09-08. |
| 2026-09-15 | `/plan-tomorrow` — run the nightly build on demand instead of waiting for 9pm | ❌ **Killed** at audit #2. Its own revisit trigger was *"once the nightly build has cleared its start condition"* — and that condition was retired at this audit as unfalsifiable. The trigger no longer exists, and the underlying complaint (plans go stale after 9pm) has never been observed, because until 09-16 the build had never written a plan. Re-propose it only if a real stale-plan problem shows up in evidence. |
| 2026-09-15 | **The build declares the day type** (replacing `/today`'s ratification) | ✅ **Built** — audit 2's one addition, after 4 subtractions. See `DECISIONS.md` 2026-09-15. |
