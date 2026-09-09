# SCHEDULER.md — The Nightly Build

*Drafted 2026-08-30. **Status: LANDED at the 2026-09-08 audit — on probation.** This file specifies an automated nightly planner that reads Notion, Google Calendar, and this repo, and writes concrete time blocks into Google Calendar for the next day. The operational prompt is `.claude/nightly-build-prompt.md`; when the two disagree, this file is the spec and the prompt is the bug.*

> **✅ Landed 2026-09-08.** The §7 amendments are in `SYSTEM.md`, `CLAUDE.md`, and `habits/tracker.md`; the §8 entry is in `DECISIONS.md`. It was the audit's one addition and it was paid for with five subtractions.
>
> **The audit did not accept the spec as written.** It imposed two amendments on it, both marked below:
> 1. **§9's kill condition became a start condition.** As drafted it was unfalsifiable — you cannot stop doing a glance that has never happened. `/today` stood at **0 runs in 12 days** on audit day.
> 2. **§5 gained a ninth guardrail.** The claim that this "costs nothing when ignored" is **false**: at 0 routes, an unswept month deposits ~90 dead blocks on the calendar, which is exactly the *"a clock cue that fires during a client meeting trains you to ignore cues"* mechanism that retired fixed clock-time cues on 08-27. The run must now sweep its own past, not just tomorrow.

---

## 1. What this is, and what it deliberately is not

**It is:** a nightly pass that computes the real shape of tomorrow from the calendar, selects a *small* number of tasks from Notion, and writes them into Google Calendar as concrete, cued, placed blocks.

**It is not** a reinstatement of the nine-row Daily Protocol or the 9:45 peak window. Both were retired 2026-08-27 and stay retired. The distinction is load-bearing and rests on four constraints, all of which are enforced in the prompt:

| The retired grid | This scheduler |
|---|---|
| Fixed rows, same every day | Computed from tomorrow's actual commitments; different every day |
| Filled the day | **Caps at 3 concrete blocks and ~60% of free time** |
| Clock-time cues (`12:00 ownership block`) | **If-then cues anchored to transitions**, with a place |
| Replaced the decision | **Proposes; `/today` still declares.** A plan the route overrules is a plan working correctly |

**The route stays the fixed part.** The nightly build produces a *proposal for tomorrow*; `/today` in the morning ratifies, amends, or discards it in 60 seconds. If the day changed overnight, the route wins — always, without negotiation.

---

## 2. The three inputs and what each is for

| Source | Supplies | Read path |
|---|---|---|
| **Notion — My Task List** | *What* and *how big*. Task, Date (due), Importance, Urgency, State, Minutes | `collection://185a21f2-73aa-81bc-90d8-000b49835c2e` |
| **Google Calendar** | *What's already fixed*, and where blocks can land | Personal + Family + Hunter |
| **This repo (life-log)** | *How he actually works* — lane status, outstanding items, which habits are mid-install | `raw.githubusercontent.com/reese8272/python-learning-log/main/…` |

**Notion schema note.** The SQL layer does not expose `Date` directly — query the expanded column `"date:Date:start"`. `Hours` is a formula and is not queryable. `Completed` uses the string literals `__YES__` / `__NO__`. **As of the 2026-09-08 audit the `Time` property no longer exists and `Importance` has two options, not three** — see §6.2 and §6.3, both now closed.

**Calendar timezone note.** The Family calendar's default timezone is **UTC** while Personal is America/New_York, and its events come back with a `Z` suffix. Normalize everything to America/New_York before computing gaps or a 2:30pm appointment will be read as 6:30pm.

**Repo read path.** The folder on `desktop-mve0i6r` lives at a WSL UNC path (`\\wsl.localhost\ubuntu\…`), which the desktop bridge refuses and which does not mount. The scheduler therefore reads the repo over `raw.githubusercontent.com`, which works and keeps the task independent of whether the desktop is awake. **This makes the push-to-main discipline in `CLAUDE.md` load-bearing:** the scheduler sees the last pushed state, not the working tree.

---

## 3. The evidence the placement rules are built on

The handoff listed "eat the frog, time blocking, spaced repetition" as candidates. Those were checked. Several did not survive; the rules below are what did.

### What survived

| Finding | Evidence | Rule it produces |
|---|---|---|
| **If-then (contingent) plans beat schedule plans** — d=.43 vs d=.29 | Sheeran/Gollwitzer, 642 tests | Blocks are titled `If <cue> → <action>`, never `10:00 Deep Work` |
| **Time+place d=.46; time alone d=.25** | same | **Every block names a place.** Cheapest available upgrade |
| **Over-specification backfires** — adding how/how-long dropped d to .24 | same | Title carries cue + action + place. Nothing else |
| **Planning >1–3 goals destroys the effect** — 1 goal p<.02, 6 goals p>.25; mechanism is perceived difficulty | Dalton & Spiller 2012, *JCR* | **Hard cap: 3 concrete blocks.** The rest is listed, not scheduled |
| **Slack works only when it feels costly** — 52.5% vs 25.9% attainment; "emergency" framing beat "bonus" | Sharif & Shu | **One named `⛑ Emergency Reserve` block.** Never invisible padding |
| **~50% of planned tasks get done**; 29–43% finish inside their own estimate | Reclaim (weak) + Buehler 1994 (strong) | **Schedule to ~60% of free time**, never 100% |
| **Planning fallacy: 64–84% overruns** | Buehler, Griffin & Ross 1994 | **Multiply `Minutes` by 1.7** |
| **The only validated debias is confronting your own history** — 29%→60% on-time | Buehler Study 4 | Log estimate vs. actual; replace the 1.7 with his real ratio once ~20 tasks exist |
| **Precise scheduling makes things feel work-like and kills enjoyment — but "rough" windows fully remove the penalty, and only for non-work** | Tonietto & Malkoc 2016, 8 studies | **Work blocks get exact times. Movement, meals, personal blocks get rough windows** |
| **Acute exercise → inhibitory control, ADHD-selective, still measurable ~33 min post** | JOGH 2025 meta (acute SMD −0.65); Frontiers 2019 crossover (d=.65–.81) | If movement is placed, the hardest block starts **within ~30 min of it** |
| **Stimulant plateau, not ramp** | Concerta Tmax 6–10h; Wigal LDX crossover, p<.001 at 2–14h | Hardest block avoids the first ~60–90 min post-dose |
| **Day-of-week consistency predicts habit formation; time-of-day does not** | Buyalskaya 2023, *PNAS*, n>30,000 | Habits anchor to a **day and a transition**, not a clock time |
| **Evening planning speeds sleep onset (~9 min), dose-responsive on specificity** | Scullin 2018, polysomnography | The nightly run happens **before the brick**, is short, and is **write-once** |
| **…but evening planning harms detachment in habitual planners** | *Occup Health Sci* 2022, null-to-negative | **No re-surfacing after the brief is written.** No notifications. Don't re-open it |

### What did not survive — do not build on these

| Claim | Status |
|---|---|
| "23 min 15 s to refocus after an interruption" | **Fabricated.** The number appears nowhere in Mark et al. 2008; that paper never measured recovery time |
| Fixed Pomodoro 25/5 | **RCT null** (N=94) — and produced *faster* fatigue and steeper motivation decline than self-regulated breaks |
| Task batching | **Blogs only.** No controlled study found |
| Body doubling | **Near-zero controlled evidence.** Its parent literature (social facilitation) may contraindicate it for hard cognitive work |
| Self-imposed deadlines | **Failed replication, 2026** (*Psych Science*, all null) |
| "66 days to form a habit" | **Overstated.** Median of 39 usable participants; range 18–254; partly extrapolated beyond the study window |
| "Schedule only X% of your day" as a rule | **No research.** The ~60% here is derived from measured completion rates, not from the folk rule |
| "ADHD adults underestimate duration by X%" | **Unsourced.** The lab literature measures 2–40 s intervals and finds *over*estimation. The 1.7× above is general-population planning-fallacy data, honestly labeled |
| Eat the frog | **Contested.** One good paper (N=2,013, non-ADHD): hard-first raised *self-efficacy* (d≈.72) but **had no effect on performance in any study**, and went null in the most realistic task. Do not hard-code an order |

---

## 4. The algorithm

### Step 1 — Compute the real shape of tomorrow
Read Personal + Family + Hunter. Normalize to America/New_York. Waking window **06:30–22:00**. Subtract every commitment, then subtract transitions: **10 min after any meeting**, **30 min around Tay Dropoff** (07:45–08:00 is a 15-minute event and a 45-minute round trip). What remains is *free time*. Find contiguous gaps ≥ 25 min.

### Step 2 — Propose a day type (do not declare it)
| Largest contiguous gap | Proposal |
|---|---|
| ≥ 75 min | 🟩 Deep |
| 30–74 min | 🟨 Split |
| < 30 min, or ≥4 commitments | 🟥 Survival |

Phrase it as `Tomorrow reads like a 🟨` — never as a verdict. **`/today` declares.** If tomorrow reads 🟥, schedule **nothing but the reserve** and say so in one line. Never negotiate a 🟥 upward.

### Step 3 — Budget
`budget = free_time × 0.6`. Blocks stop when the budget is spent, even if the cap in Step 6 has not been reached.

### Step 4 — Rank the Notion tasks
Pull `Completed = __NO__`. Score:

1. **Overdue** (`date:Date:start` < tomorrow) — hard include, highest
2. **Due tomorrow** — hard include
3. **Eisenhower**, read from the matrix that already exists: `⚠️ Important`+`⏰ Urgent` → `⚠️ Important`+`Not Urgent` → `Not Important`+`⏰ Urgent` → the rest
4. **`Habit` is not a point on the urgency line.** Pull it out and place it by cue in Step 5, never by rank
5. Effort = `Minutes × 1.7`. Missing `Minutes` → assume 30, and say so in the brief

### Step 5 — Place by `State`, not by priority
`State` is the sleeper feature of this Notion schema: it encodes **cognitive load and context**, which is the axis a priority-only system lacks.

| `State` | Where it goes |
|---|---|
| **Flow** | The longest contiguous gap. On the medication plateau, not the ramp. Within ~30 min after movement if movement is placed. **Max one per day** |
| **Quick** | The 10–25 min gaps between meetings — the slots nothing else fits in |
| **Easy** | Low-energy windows: post-lunch, late afternoon, after a meeting stack |
| **Personal** | Evening or around family time, and as a **rough window** (`~6–7pm`), never an exact clock time |
| **Habit** *(from Urgency)* | Anchored to a transition that already happens, on a consistent **day of week**. Never a bare clock time |

### Step 6 — Cap, hard
**Maximum 3 concrete blocks**, plus the reserve. Everything else that ranked goes in the brief under *"If there's room"* — visible, unscheduled, carrying no commitment. This cap is not conservatism; it is the Dalton & Spiller result, and exceeding it is the failure mode, not the ambition.

### Step 7 — One Emergency Reserve
A single `⛑ Emergency Reserve` block, 30–45 min, in the day's second half. Description states plainly: *"One reserve. Spending it means something else moves."* Do not create two. Do not silently absorb overruns into it.

### Step 8 — Write the events
**Title format:** `If <transition cue> → <specific start instruction> — <place>`

> ✅ `If Verizon morning meeting ends → open pipeline.py, predict what _flush does before reading — desk`
> ❌ `10:30 Deep Work — pipeline`

The action must be a **start instruction**, not a topic, matching the `/today` Step 4 standard: specific enough that starting requires no further decision.

Every event this task creates carries `[auto:nightly-build]` in its description. **It may only ever delete or modify events carrying that tag.** Anything else on the calendar is untouchable.

### Step 9 — Never schedule
- **The brick.** It is installed, transition-cued, and the most-proven behavior in the log. Automating it can only damage it
- **🏡 Home time.** `SYSTEM.md`: *"You were actually there. No log required."*
- **Saturday or Sunday.** Weekends owe nothing professional
- **A 🟥 day**, beyond the reserve

### Step 10 — Write the brief, then stop
Short, phone-readable, **write-once**. No follow-up notification, no re-surfacing tomorrow's load after it's written — that is the documented harm to evening detachment for habitual planners, which is exactly this user.

---

## 5. Guardrails (verbatim in the task prompt)

1. Never write more than **3** concrete blocks
2. Never fill more than **60%** of free time
3. Never touch an event without the `[auto:nightly-build]` tag
4. Never write to the repo — reads only. The Change Window governs
5. Never negotiate 🟥 upward
6. Never schedule the brick, Home time, or a weekend
7. If Notion returns nothing, **say so in one line and schedule only the reserve.** Do not invent tasks, and do not fill the space with the repo's outstanding items on your own initiative
8. If a source is unreachable, degrade to the sources that answered and name the gap. Never fail silently
9. **Sweep before you write.** At the start of every run, delete **all** `[auto:nightly-build]` events from *prior* days as well as tomorrow's — not just tomorrow's. *(Added by the 2026-09-08 audit. Unswept proposals do not sit there neutrally; they accumulate into a calendar of ignored blocks, and training yourself to ignore calendar blocks is the documented harm this whole design is trying to avoid.)*

---

## 6. Known open questions

1. **The 1.7× multiplier is a placeholder.** It is general-population data. After ~20 completed tasks with a `Minutes` estimate, replace it with his measured ratio — that swap is the single highest-value upgrade available, and it's the only duration debias with experimental support.
2. ~~**`Time` (text) is unused and was abandoned.**~~ ✅ **Closed 2026-09-08 — retired.** Counted at the audit rather than taken on trust: **6** uses, last **2026-04-07**, all on completed rows (the draft's "7 uses, abandoned since 2025-12" was wrong on both figures).
3. ~~**`Moved the needle` has never been used.**~~ ✅ **Closed 2026-09-08 — retired.** Verified 0 of 69 rows at the audit.
4. **Ordering is unresolved and should be instrumented, not assumed.** Hard-first vs. easy-win has no ADHD evidence either way. Vary it and read the completion data at `/audit`.
5. **Dedicated calendar.** Currently writes to Personal with a tag. A separate calendar would be cleaner to bulk-clear, but the API surface here has no create-calendar call. Revisit.

---

## 7. Amendments — ✅ all landed 2026-09-08

*Kept as the record of what was changed and where. All three are live; the audit also added three that §7 didn't anticipate — a `SCHEDULER.md` entry in `CLAUDE.md`'s Blueprint section and Folder Overview, and the Git section upgraded from discipline to **dependency** (this task reads the last pushed state, not the working tree).*

**`SYSTEM.md` Layer 3** — after *"There is no peak window and no fixed daily protocol,"* add:

> The nightly build (`SCHEDULER.md`) writes a proposal for tomorrow into the calendar. It is **not** a protocol and not a grid: it caps at three blocks, it is computed fresh from tomorrow's real commitments, and it has no authority. The route ratifies it or discards it. A plan `/today` overrules is a plan working correctly.

**`CLAUDE.md` — The Router section** — after *"do not build a replacement grid":*

> The one sanctioned exception is the nightly build, adopted 2026-08-30 with the grid's retirement explicitly in view. It survives the rule because it proposes rather than decides, caps at three blocks, and yields to the route. If it ever starts filling days, it has become the thing it replaced — kill it at the audit that notices.

**`habits/tracker.md` → Installing** — add:

| **🌙 The nightly build** | Cowork task, 9:00pm Sun–Thu. Cue: automated. **The human half is the 60-second glance before the brick.** | 2026-08-30 | New. Zero runs. The behavior being installed is *the glance*, not the automation. |

**`PARKING.md`** — nothing. This was built, not parked; the decision is recorded below.

---

## 8. `DECISIONS.md` entry

```
## 2026-08-30 — The nightly build

**Decision:** Adopt an automated nightly scheduler that writes up to three
cued, placed time blocks into Google Calendar for the next weekday.

**Why this is not a reinstatement of the grid.** The 08-27 retirement killed
the peak window and the nine-row protocol on the grounds that a fixed
container cannot survive an unpredictable day. This is computed nightly from
the day's real commitments, capped at three blocks and 60% of free time, and
has no authority — /today ratifies or discards it. The rule it must never
break: it proposes, the route decides.

**What made it worth building anyway.** The route asks for the shape of the
day, the lane, and the one thing. The first of those is a question the
calendar can already answer, and answering it from memory at the cue is
wasted effort. The scheduler does that arithmetic in advance.

**The evidence that changed the design.** Three findings moved this away from
the obvious build: if-then plans beat scheduled appointments (d=.43 vs .29)
and place nearly doubles the effect (.46 vs .25), so blocks are cued and
placed rather than timed; planning more than ~3 goals at once destroys the
benefit entirely (Dalton & Spiller), which is where the hard cap comes from;
and slack only works when it is named and feels costly (Sharif & Shu), which
is why there is one Emergency Reserve rather than invisible padding.
Eat-the-frog, Pomodoro, batching, and body doubling were all checked and none
of them survived — see SCHEDULER.md §3.

**The tension being accepted knowingly.** Fixed clock-time cues were retired
08-27 because a clock cue that fires during a client meeting trains you to
ignore cues. A calendar block is a clock cue. This is mitigated (transition
cues in the title, three blocks not nine, rough windows for anything
non-work) but not eliminated. **The kill condition is written down in
advance:** if the glance stops happening, or the blocks start getting
ignored, it is retired at that audit — not tuned.

**Subtraction owed.** This is an addition. Per the audit rule, the audit that
lands it must cut something. `Moved the needle` (0 uses in 69 rows) and the
`Time` property (abandoned since 2025-12) are both standing candidates.
```

---

## 9. The start condition *(rewritten by the 2026-09-08 audit)*

**As originally drafted this section read:** *"If the morning glance stops happening for a week, the nightly build is retired at the next `/audit`."*

**The audit rejected that wording as unfalsifiable.** On audit day `/today` had run **0 times in 12 days**, and a glance that has never happened cannot stop happening. A stop condition presumes a start. So:

> ### The start condition
> **If `/today` has not run at least 5 times before the next `/audit`, the nightly build is retired — not tuned, not re-scoped, and regardless of how good the plans were.**
>
> The scheduler's entire output is an input to the route. A proposal with no ratifier is not a plan; it is calendar noise. If the ratifier isn't running, the correct move is to stop generating proposals, not to generate better ones.

**The kill condition survives underneath it**, for once the thing is actually running: if the morning glance stops for a week after a genuine start, it is retired at that audit.

**The honest prior, unchanged and not softened.** The Notion time-blocked day (2025-12-04) ran **once**. The nine-row Daily Protocol ran **four days**. This is the **third** attempt at giving the day a shape in advance, and the prior is that it fails. Two things make this attempt different, and only two: it runs whether or not Reese does, and the condition for calling it dead was written before the first run.

**What is *not* a difference:** quality of design. The nine-row protocol was also well-designed. Design has never been the failing variable here.