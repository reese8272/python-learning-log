# DECISIONS.md — life-log

A log of explicit design decisions that change or deviate from what the planning docs previously said.

---

## 2026-08-27 — **Phase 3**: the system is rebuilt around four lanes, a router, and an audit

**The trigger, in Reese's words:** *"I know I am reworking something but this is simply just my life constantly evolving. I got a great project for my job and learning so much on the job. Ian is giving me great work to continue building my business, and learning is being sidelined because of other life obligations... I need a way to concretely keep my life a series of systems and audit the system and habits heavily."*

**The read that had to be delivered first:** this request is the system's own #1 documented risk. The 08-18 count was **28 system/card commits against 17 `/learn`, 2 `/sharpen`, 2 `/drill` since 06-01**, and the finding was that *system-tinkering is the most sophisticated procrastination available here, because from the inside it is indistinguishable from progress.* A "severe rewrite" nine days after that read is exactly the shape of the failure mode.

**And the rewrite is still correct**, for one reason that doesn't apply to the previous rebuilds: **the life described in `SYSTEM.md` no longer exists.** The 07-23 constitution was built for a life with one engine (learning toward an exit) and a predictable day (the 9:45 peak block). The job pipeline was retired 07-25. The peak block sits inside client hours on a project that is now genuinely good and genuinely teaching. A second income stream (Ian) appeared and has no representation anywhere in the repo. The document was describing July.

**The resolution:** the rewrite is legitimate because it **subtracted far more than it added** — 8 retirements and 4 paused tracks against 2 additions — and because it ships the mechanism that stops the *next* one (the Change Window, below).

### What changed

**1. Life is four lanes.** Every rep belongs to exactly one, named before the rep starts.
- 🏡 **Home** — the ground; the bad-day non-negotiable. Not a competitor for time.
- 💼 **Craft** (Cognizant) — own the project, perform without AI visibly. The rep: predict a file → open it → one non-obvious decision → **what breaks if this is wrong** → verify live → one line.
- 🛠 **Business** (Ian's contract work + own products) — convert skill into money that isn't hours. New folder `business/` with `LEDGER.md`. **Ian is client work, distinct from the Editor/autoclip product thread** (Reese's clarification).
- 🧠 **Depth** — **derived, never scheduled.** Runs on the residue of the other two.

New failure mode named: **lane blur** — three lanes touched in a busy day, none moved. Lanes are audited separately so a Dark lane can't hide behind a busy one.

**2. The peak window is retired.** Reese's call: *"I don't want a peak window or anything — I need a dynamic scheduling program based on the needs of the day."* Replaced by **`/today` — the route**: declare the day type (🟩 Deep / 🟨 Split / 🟥 Survival), pick one lane, name one thing. 60 seconds, phone.

The design principle: **don't schedule the time, schedule the decision.** The route is a fixed cue with dynamic content — which preserves the *infrastructure over intention* lesson (04-06) while letting the content flex, and answers the new failure mode this choice creates (**the fluid-schedule trap**: "dynamic" quietly becoming "never decided").

**The load-bearing rule: 🟥 is a legitimate, counted day that carries no debt.** This is the real counter to the all-or-nothing collapse (six instances: 4/09, 5/01, 6/16, Jul 11–19, Jul 30–Aug 3, Aug 12–17). The collapse has never actually been a discipline problem — it lives in the gap between *"I can't do the full thing"* and *"so I did nothing and felt bad about it."* Every prior counter (the Floor, `/checkin`) reduced the cost of a small day. This one makes the small day a **choice** — the only real miss is now a day with **no declaration at all.** The post-meds window survives as a *routing input*, not a reservation.

**3. All four curriculum tracks are paused** — `api` secure-api-engineering, `ai` ai-engineering-curriculum, `py` mid-python-developer-prep, `soft` senior-engineering-soft-skills. Paused, not deleted: each file carries a banner and remains a **reference catalog**, not a backlog. There is no ACTIVE track and no track menu.

The number: **4 banked units of 233 since April, one `[x]` per track.** Every track launched and stalled at unit 2 — a signature, not a pace problem. **Work generates the curriculum now:** Craft and Business reps throw off things that couldn't be explained; those are captured, and `/drill` and `/sharpen` walk the captures. `/learn new <topic>` handles on-demand acquisition.

The supporting evidence, from 08-18: the one time learning visibly converted to career movement (07-28 → 07-29, the work quiz then the boss call) it was a **defense** rep under real stakes, not an acquisition rep — against a ratio of 17 learn : 2 sharpen : 2 drill. Phase 3 stops manufacturing stakes and uses the real ones.

**4. `/audit` — the new heavy loop, and the answer to "audit heavily."** Five passes: **Evidence** (count before concluding) → **Lane** (Moving/Stalled/Dark) → **Habit** (Installed/Installing/**Not installed**/Retired) → **Subtraction (mandatory)** → **The one change** (capped at one, only after a cut). Weekly through the transition, then monthly.

**5. The Change Window — the rule this whole phase depends on.**

> **The system may only be changed during an `/audit`.** Outside an audit, a system idea goes to `PARKING.md` as one line and is not built.

This converts the tinkering impulse from a leak into a scheduled, bounded, *subtractive* valve. It costs one line to obey and removes the only mechanism by which this system has ever eaten itself. **It binds Claude more than Reese** — most of those 28 system commits happened because a session drifted into improving the system instead of running it. The one exception: a genuine contradiction or breakage is a **repair**, not a change.

**6. The habit tracker is regraded on installation, not consistency.** Active/Building/Aspirational → **Installed / Installing / Not installed / Retired**. The old split conflated *tried and didn't hold* with *never physically put in the world* — on 07-27 both the affirmation stack and the night-before gym setup were called failures when the honest verdict was that neither had ever been installed. **A cue isn't designed until it's physically installed; the tape counts, not the design session.**

The regrade immediately reclassified six habits out of "failing" and into "never tried," and left exactly **one** habit genuinely Installed: the brick. That is the honest picture, and it is the argument for building slowly — one habit that survives every collapse is worth more than six that don't.

### What was retired (no silent abandonment — the rule applies to system components too)

| Retired | Why |
|---|---|
| The 9:45 peak block | Reese's call; the hours aren't predictable and the slot sat inside client hours (which John's review flagged) |
| The nine-row Daily Protocol | Built 07-25, dark by 07-29 — four days. A container, not a fix. |
| The four active curriculum tracks | 4 of 233 banked; every track stalled at unit 2. Paused as a reference catalog. |
| The `$6k rule` | Priced an urgency that ended when the pipeline was retired 07-25 |
| The weekly Cold Bench + its ledger | Ledger at **zero from 07-25 to 08-27**. The principle survives inside the Craft rep (first pass unassisted; AI examines, never authors). A weekly obligation with an empty ledger is theater. |
| Fixed clock-time cues (10:15 set-tomorrow, 12:00 ownership block, 8:30pm drill) | Replaced by transition cues. A clock cue that fires during a client meeting trains you to ignore cues. The brick's 10:25 survives — it's a transition (phone → charger), not an appointment. |
| Wake-at-6am · morning deep-work block · must-listen playlist · 15-min creativity block | Marked Active since 04-01 and unevidenced since May. Carried four months on a good three-week stretch in April. Retired honestly rather than left as decoration. |
| The "Ideal Day — Full Habit Map" | A picture of a day that no longer exists. The lanes replace it. |

### What was added (two things, both mechanisms, neither a habit)

| Added | Why it earns its place |
|---|---|
| `/today` + `PARKING.md` + the Change Window | The router replaces what was retired; the parking lot is what makes the Change Window enforceable (a rule with nowhere to put the idea fails) |
| `/audit` + `business/` | The audit is the explicit ask; `business/` is the only lane with real external commitments and it had **zero** representation in the repo |

### Open, and deliberately not decided here

1. **The AI YouTube Editor.** No recorded work since 08-04; NFL Week 1 is ~2 weeks out; it now competes with two live lanes. Three honest options — re-scope / move the date / shelf it with a retirement note. **First `/audit` decides.** Drifting past 09-10 without choosing is the only bad outcome.
2. **The Business weekly ceiling.** Needs Reese's number. Set at the first audit. This is the counter to **client-load creep** — the Business lane is the only one with someone else waiting, so it expands by default.
3. **The Editor lead's message** — owed since 08-10, **17+ days**. Not a decision, just undone. It is the oldest open item in the system and it costs five minutes.

---

---

## 2026-08-19 — `secure-api-lab` moves inside the repo; all lab/lesson artifacts live under `career/`

**What changed:** `~/workspace/secure-api-lab` is now **`career/lesson_assignments/secure-api-lab/`**, tracked by life-log's git. Its nested `.git` (2 scaffold commits, **no remote**) was removed so life-log can track the files normally; the full history is bundled at `secure-api-lab-history.bundle` in the session scratchpad. Its `.claude/commands/issue-workflow.md` was deleted as a byte-identical duplicate of the repo-root one — nested `.claude/` in a subdirectory is never loaded anyway. Every `~/workspace/secure-api-lab` path reference was rewritten across `agenda.md`, `CAREER_LOG.md`, `concept_queue.md`, `.claude/commands/learn.md`, `DECISIONS.md`, and the `secure-api-engineering` roadmap + session log. The lab's own `.gitignore` moved with it, so `certs/`, `.env`, and venvs stay ignored under life-log's git.

**Why:** Reese's call — nothing lesson- or lab-shaped should live outside `life-log/career/`. The split was a real cost, not a cosmetic one: the top rung of the Ladder (the build) lived in a repo with no remote, no backup, and no connection to the roadmap that assigns it, while every other rung was version-controlled and pushed nightly. The 08-18 read was that four tracks stall at unit 2 and the build is the step that gets skipped — a lab sitting outside the system it belongs to is one more reason to skip it.

**Deliberately NOT moved:** `NLP Learning Course/`, `college_assignments/`, `bootdev/hoopla/`. Dead archives with venvs and their own `.git` dirs; consolidating them would bloat the journal repo without feeding the learning engine. Real products (`Youtube-Video-AI-Editor`, `CFO-analyzer`) stay where they are — they're portfolio work, not lessons.

**Source / evidence:** `git bundle` backup verified before the nested `.git` was removed; post-move `grep -rn "workspace/secure-api-lab"` returns zero hits.

---

## 2026-08-13 — The interview sprint's format work is promoted to the evergreen learning engine; the track is de-timeboxed; a learning-science reference doc is added

**What changed:**

1. **The `⏱ TRACK ADDENDUM` in `.claude/commands/learn.md` is deleted, and everything in it is now evergreen.** It was explicitly marked *"Delete this whole block on 2026-08-18."* Promoted out of it and into all five tracks: the **chunk loop** (teach ~8 min → 2–4 inline checks → one tiny snippet → stop), the **depth bars**, the mandatory **`Breaks if wrong:`** clause on `[A]` units, and the three **check formats**.
2. **Depth bars `[A]`/`[B]`/`[C]` replace Tier 1/Tier 2 as the system's vocabulary**, in `learn.md`, `sharpen.md`, `concept_queue.md`, and `CLAUDE.md`. Three levels with a "done sounds like" sentence and a minute budget beat two levels with neither, and the budget is what makes rationing a ~90-unit curriculum possible. **Legacy `T1`/`T2` rows are mapped (T1 ≈ `[A]`/`[B]`, T2 ≈ `[C]`/`[B]`) and migrated only when touched** — a bulk rewrite of ~150 rows is system-tinkering.
3. **The Ladder is named** — fill-in-the-blank → short answer → spot-the-bug → completion problem → the project. Rungs 1–3 in-session per chunk, rungs 4–5 the solo worksheet. **Spot-the-bug is generalized off security** with a per-track defect catalog (`ai`: prompt injection, unbounded context; `py`: mutable default, N+1, leaked resource).
4. **The delayed-`[x]` rule.** A teaching session may only mark `[~]`. Banking requires the worksheet green **or** a clean cold re-ask at a new **Step 1.5**, which opens every session by re-asking the last session's `Tripped` list. Step 3 is also reframed explicitly as a **pretest** — a wrong guess is the mechanism, not a setback.
5. **`📝 Learning notes` (Asked · Landed · Tripped · Watch) is promoted from the api track to all tracks.** `Tripped` is now load-bearing rather than a record: it is consumed by Step 1.5 and by `/drill`, and `/drill` strikes items from it on a Solid verdict.
6. **`/drill` interleaves.** 3–5 items across *different domains* with *varied question forms*, rather than one topic several ways, and it now skips anything reviewed within the last week.
7. **New: `career/helpful_notes_and_guides/Learning Science Protocol.md`** — seven cited entries with effect sizes, matching the Focus & Time Block Protocol's format. Scope split stated in both: **Focus Protocol owns attention and initiation; this owns encoding and retention.** Wired into `SYSTEM.md` Layer 4 and `CLAUDE.md`.
8. **The track is de-timeboxed and renamed:** `career/api-security-aws-prep/` → **`career/secure-api-engineering/`**. §11 (story bank) deleted, §10 (system-design set-piece) demoted to a recurring `/drill` exercise, §5 mostly re-barred `[A]`→`[B]`, the 7-day map and Interview Intel removed (the JD survives as a short "why these units" market-evidence note). `secure-api-lab` keeps all 8 issues as the Ladder's top rung.
9. **One ACTIVE track at a time**, declared on the Card. `secure-api-engineering` is active; `ai`, `py`, `soft` are dormant; `new` stays always-available. **A bare `/learn` goes straight to the active track — the menu is gone.**
10. **A learning-rep counter is added to the Card's Streaks.** Brick, check-ins, and ownership touches were counted; the rep — the thing the system exists to produce — was not.

**Why:** the secure-API role closed on years-of-experience before an interview happened. The sprint's *content* was interview-shaped but its *format* was the best work in the system's history, and it was five days from automatic deletion. Reese's framing, verbatim: *"I don't think there is a world where integrating the learning I was GOING to do in that is a bad idea… I think having multiple ways to learn UP TO a project might be the move going forward."* That instinct turned out to be a documented effect (guidance fading), which is what made it worth encoding as the Ladder rather than as a preference.

**Source / evidence:** live research this session, all cited in `Learning Science Protocol.md`. The findings that actually changed behavior rather than confirming it:
- **Delayed judgments of learning.** [Knouse, Paradise & Dunlosky 2006](https://pubmed.ncbi.nlm.nih.gov/17085626/) — adults with ADHD show *higher relative accuracy for delayed* metamemory judgments, while [calibration trends toward overconfidence](https://link.springer.com/article/10.1007/s12144-026-09164-9). This is the direct counter to the 08-11 failure mode (four misconceptions survived confident-sounding answers) and is why `[x]` left the teaching session.
- **Guidance fading / expertise reversal.** [Fading worked solution steps](https://link.springer.com/content/pdf/10.1023/B:TRUC.0000021815.74806.f6.pdf), [expertise reversal](https://www.researchgate.net/publication/226748784_The_expertise_reversal_effect_and_worked_examples_in_tutored_problem_solving) — this is the Ladder, and it independently confirms the fading-scaffold row Reese invented at `career/patterns.md:148` on 07-28.
- **Delay-of-reinforcement gradient in ADHD.** [Feedback timing modulates learning in adults with ADHD](https://www.nature.com/articles/s41598-018-33551-3) — the mechanism behind per-chunk grading, and the missing citation under the 07-27 reward-loop note.
- **Correction made:** `sharpen.md` claimed the testing effect at **g ≈ 0.55**. That number is the *exercise → inhibitory control* figure from the Focus Protocol, mis-transcribed. The testing effect is [**g = 0.50** (Rowland 2014)](https://pubmed.ncbi.nlm.nih.gov/25150680/) / **g = 0.61** (Adesope 2017). Fixed.

**What was deliberately NOT done:** the nine-row Daily Protocol stays suspended (it lived four days in July); `/session-start` and `Learning System Guide.md` remain stale and are flagged, not fixed; no bulk re-bar of existing roadmap rows. The 08-04 STOP item is *"building containers during sprints"* — this pass was scoped to consolidation of work that already existed, done outside the peak window, and it is paid for by a rep the following morning.

**Left open, deliberately:** **nothing currently supplies an external deadline.** The seven-day sprint out-produced any comparable stretch in the record and it had a date on it. The only hard date left is the AI Editor's NFL Week 1 (~09-10), now unpaused — which forces a peak-window allocation decision between it and `secure-api-engineering`. Logged in `CAREER_LOG.md` Active Struggles; Reese's call, not the coach's.

---

## 2026-08-11 — Every roadmap section carries a `📝 Learning notes` block; §1 taught before §2 despite the map

**What changed:**

1. **A `### 📝 Learning notes` block is now appended to every section** of `career/api-security-aws-prep/summary.md`, written *during* the session rather than reconstructed after. Four fixed headings: **Asked** (questions he raised unprompted — a better map of the mental model than a check answered) · **Landed** (restated cold, safe to build on) · **Tripped** (wrong or fuzzy, *plus the corrected line* — this doubles as the pre-built `/drill` list) · **Watch** (coach-level patterns, not content). Spec written into the roadmap's *How a session runs* section. Rule: the block gets written even when the section is unfinished — a partial block beats a missing one.
2. **The 7-day map's day assignment was overridden on day 2.** The map put §1 on Sun 08-10 and §2+§3.A–B on Mon 08-11, but 08-10 went to building the track, not walking it. §1 was run today instead of §2. The sprint is now ~1 day behind the written map and §2 must compress into Tuesday.
3. **Standing teaching instruction added:** before teaching an `api` unit from zero, check whether Reese has already *operated* it and merely lacks the vocabulary. §1 demonstrated the failure mode in both directions — he couldn't define ASGI, but already had the "CPU work leaves the request path, that's what Celery does in CreatorClip" answer and didn't recognize it as a Section 1 answer.

**Why:**

- **(1)** This track is taught from zero under a hard clock, and its specific failure mode is marking a unit `[x]` off a confident-sounding explain-back that was actually 80% right. In the first session alone, four misconceptions survived answers that *sounded* correct — "WSGI is better for CPU-bound work," "bad ASGI degrades to WSGI" (it's strictly worse), "the ASGI connection is app-lifetime," "`await` groups coroutines." None would have been recoverable from a `[x]` and a summary. Reese proposed the notes page himself and asked that the convention be written down so future sessions follow it.
- **(2)** §1.2, §1.3, and §1.6 are the three `[A]`s that §4's JWT validation design and §8's PHI story rest on. Teaching auth-in-a-dependency (§3–§4) before dependency injection is owned inverts the build order; §2 is ~85 min and mostly `[B]`, so it's the cheaper thing to slide.
- **(3)** The gap analysis of 08-10 already split the JD into *recalibration* vs *acquisition*, and the 08-10 revision (below) correctly dropped that as a **teaching** directive. This is narrower and survives that: teach from zero regardless, but *source the worked example* from what he's already run, because the recall is free and the salience is real.

**Source / evidence:** the 2026-08-11 session log (`career/api-security-aws-prep/reflection_log/2026-08-11.md`) — Reese's proposal verbatim: *"You think adding a notes page at the end of each section is good? Like simply saying what I asked and understood and what tripped me up."* Currency claims in that session verified live against [FastAPI — Concurrency](https://fastapi.tiangolo.com/async/) and [FastAPI — Server Workers](https://fastapi.tiangolo.com/deployment/server-workers/) (the gunicorn worker-class recipe is absent from current docs; one uvicorn process per container is the stated container guidance).

**Date:** 2026-08-11

---

## 2026-08-10 (later same day) — The `api` track is taught from scratch with three depth bars, in chunks, with inline checks

**What changed** (revising the entry below, written hours earlier):

1. **The "recalibration vs acquisition" split is dropped as a teaching directive.** Every unit starts `[ ]` and is taught from zero, including FastAPI and CI/CD. The earlier analysis survives only as *which worked example to use* — where shipped code exists, the example is CreatorClip or CFO Agent instead of a toy.
2. **Three depth bars added to every unit**, with a minute budget: `[A]` BUILD IT ~30m (implement cold + name the failure mode) · `[B]` EXPLAIN IT ~15m (the decision, not internals) · `[C]` NAME IT ~5m. Roughly 15 / 20 / 15 units.
3. **Sections broken into named chunks** (`1.A`, `4.C`, …) of ~20–30 min, each one teaching loop.
4. **A scoped `⏱ TRACK ADDENDUM` block added to `.claude/commands/learn.md`**, overriding Steps 5, 6, and 7.5 for the `api` track only: chunk loop instead of single delivery; inline checks per chunk instead of one end-of-unit explain-back; one worksheet per **section** (~9) instead of per unit (~60).
5. **A third check format added — spot-the-bug**: a 3–8 line snippet with exactly one real vulnerability, named before being told. Required at least once per security section.
6. **`concept_queue.md` re-tiered** with the same bars; `[C]` units deliberately excluded from the `/sharpen` queue.
7. **The retired "client one-liner" worksheet requirement removed from `learn.md` Step 7.5**, which still mandated it despite the decision to drop it.

**Why:**

- **Reese's call, and it's the right one:** *"assume I am learning everything from scratch… the pipeline is best spent understanding the 'what' and 'how deep'."* Revision 1 was a checklist of topics, which silently defers the depth decision to whatever comes next in the file. Under a 7-day clock that is how the peak window gets spent on the wrong thing.
- **The bars exist because the arithmetic doesn't work.** Taught from scratch, the 11 sections price at ~19h teaching + ~9h building = **~28 hours against ~21 available.** Rationing was going to happen either way; the only choice was whether it happened deliberately or by running out of days. Stated consequences: §1–§7 and §10 taught properly; **§8 HIPAA and §9 CI/CD capped at `[B]`/`[C]`** (the JD's *Desired* column, not its requirements); §11 story-drafting moved to evenings; **Issue 8 is the designated cut, never Issue 7.**
- **On chunking and inline checks:** the existing `/learn` teaches a full unit then runs one explain-back. For material this dense, that puts every check at the point of weakest recall. Chunk-level checks are the testing effect applied at the right granularity — and they're phone-friendly, which matters for an ADHD brain under time pressure.
- **On spot-the-bug:** short answer proves you can describe a concept; a snippet with `options={"verify_signature": False}` in it proves you'd catch it in a code review. The second is what a security interview actually tests, and the format didn't exist in the system yet.
- **On the addendum being scoped and dated:** rewriting the shared `/learn` skill a week before an interview would disturb the `ai`, `py`, and `soft` tracks for no benefit. The block is explicitly marked for deletion on 2026-08-18.

**Source / evidence:** Reese's direction (2026-08-10); an exploration pass over `career/lesson_assignments/2026-06-22_llm-call-anatomy.py` (the reference template), `2026-07-20_zero-few-shot-role-prompting.py` (including its in-file COACH NOTES grading convention), and `learn.md` Steps 4–9 / `sharpen.md` / `drill.md`, to confirm the new formats match the house style rather than replacing it. Confirmed the house question mold running through all three skills — *why THIS over THAT · when it matters · what breaks if you get it wrong* — and built every check format on it. Depth-bar system, inline-vs-worksheet placement, and one-project-per-section confirmed with Reese via AskUserQuestion.

**Follow-ups owed 08-18:** delete the `⏱ TRACK ADDENDUM` block and the peak-window-default bullet from `learn.md`. Keep the spot-the-bug format if it proved useful — it generalizes to the `ai` and `py` tracks.

**Date:** 2026-08-10

---

## 2026-08-10 — Seven-day interview sprint: a fourth `/learn` track added, the AI YouTube Editor paused, the job-pipeline pivot temporarily suspended

**What changed:**

1. **New track — `career/api-security-aws-prep/`**, reachable via `/learn api` (also `apisec`, `interview`). Eleven sections covering FastAPI at depth, REST/OpenAPI-as-contract, OAuth2/OIDC/Okta, JWT validation, mTLS, the AWS platform/edge stack, API testing, HIPAA/PHI, CI/CD, a system-design set-piece, and honest positioning. Registered in the Step 0 routing table of `.claude/commands/learn.md`, which now reads "four curated curricula" and gives this track the peak window by default through 08-17.
2. **New build repo — `career/lesson_assignments/secure-api-lab`**, driven by `/issue-workflow` over 8 dependency-ordered issues, ending in a real ECS/ALB/ACM/WAF/CloudWatch deployment.
3. **🏈 AI YouTube Editor paused 08-10 → 08-17.** It had outranked the Weekly and Monthly blocks since 08-04; the interview sprint now outranks it.
4. **⚡ The 07-25 job-pipeline pivot is suspended for the sprint**, and reinstated 08-18.
5. **Skills Tracker notes corrected** in `CAREER_LOG.md` — FastAPI, REST API design, CI/CD concepts, GitHub Actions. Levels moved Gap → Building as a *factual correction*, not a mastery bump.

**Why:**

- A screening cleared for a backend role whose JD is a single coherent thing — secure async FastAPI, IdP integration, AWS edge, HIPAA — with the next round ~08-17 covering verbal Q&A, live coding, *and* system design. Seven days, ~3hr/day available.
- **The gap analysis split in two, and conflating the halves was the main risk.** A full-repo grep returned **zero mentions** of mTLS, Okta, OIDC, SAML, ECS, ALB, Route 53, API Gateway, ACM, Private CA, WAF, Shield, CloudWatch, or Swagger — genuine acquisition-from-zero. But FastAPI (~37k LOC in CreatorClip + CFO Agent), async (defended cold), OAuth2 (shipped, YouTube publishing), testing (1,774 test functions), and CI/CD (5+ workflows, auto-deploy on main) were all already in production **and all self-rated "Gap."** Those need rehearsal, not teaching. Half the sprint's value is not wasting peak windows re-learning things he already does.
- **On the paused Editor:** `agenda.md` budgeted ~18 usable days to NFL Week 1 and the repo had already been dark 6 days. The interview is a larger and more time-bound lever than the Editor, and the sprint's content (secure APIs, AWS, auth) serves the Cognizant role regardless of outcome — so it doesn't violate the 07-25 pivot's *intent* (mastery over scattershot applications) even though it suspends its letter. Coupled obligation: **message the lead** rather than going silent.
- **On the tracker correction and why levels only moved to Building:** `CAREER_LOG.md` Active Struggles carries a standing rule from 2026-06-22 — *"Bump tracker levels only as concepts are actually defended, not from resume evidence alone."* That rule was honored. What was fixed is that two notes were **factually false** ("haven't built with it"; "no hands-on experience"), and "Gap" asserts something untrue. Cold defense is scheduled 08-16; any bump past Building is earned there. The risk being mitigated is real and specific: walking into an interview and under-selling production experience because your own file told you it was a gap.
- **On the floor:** `habits/tracker.md:105` documents six all-or-nothing collapses — *"a 10 and a 0, and no median day."* A 7×3hr plan is precisely that shape, so every sprint day carries a ~45-minute floor version that counts as a completed day.

**Source / evidence:** the job description (transcribed verbatim in the track's Interview Intel section); two parallel repo-exploration agents (2026-08-10) producing the skills inventory and the zero-footprint grep; live web research the same day verifying every Currency Watch claim — [FastAPI's python-jose→PyJWT migration](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/), [OAuth 2.1 still at draft-15](https://oauth.net/2.1/), [ALB native JWT verification shipped 2025-11-12](https://aws.amazon.com/about-aws/whats-new/2025/11/application-load-balancer-jwt-verification/), [ALB mTLS passthrough vs verify modes](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/configuring-mtls-with-elb.html), [AWS Private CA $400/mo vs $50/mo short-lived](https://aws.amazon.com/private-ca/pricing/), and [Okta client-credentials/custom-auth-server requirements](https://developer.okta.com/docs/guides/implement-grant-type/clientcreds/main/). Scope decisions (real AWS deploy vs paper, separate repo, full Editor pause) confirmed with Reese via AskUserQuestion.

**Follow-ups owed 08-18:** reinstate the weekend rule and the 07-25 pivot; delete the peak-window-default bullet from `learn.md` Step 0; resolve or update the Active Struggles entry with the interview outcome; re-scope the Editor with the lead.

**Date:** 2026-08-10

---

## 2026-08-04 — Coaching posture flipped: mentor generates insight, not therapist draws it out

**What changed:** New root file **`COACHING.md`** — the Mentor Doctrine — now the governing posture for every coaching session and for ordinary conversation in this repo. The core rule: **every session must leave a read on the table**; a session that only asked questions and mirrored him back is a *failed* session. Defines the four insight moves (cross-time read with dates · named call · reframe · the thing he didn't ask about), how to deliver a read ("here's what I see — does that track?"), and the only three cases where holding beats reading (raw grief · explicit "let me just talk" · genuine ambiguity in the record).

Files edited to match:
- `CLAUDE.md` — new "Coaching Posture" section at the top, pointing at `COACHING.md`
- `reflect.md` — Step 2 is now **form a read before speaking**; deleted *"your job is to draw things out of the user, not present things to them"*, *"lead with listening, not analysis... make them feel heard, not assessed"*, *"only challenge when they're clearly being dishonest with themselves"*, and *"if a contradiction exists, ask about it gently and let them see it themselves."* "Reflective listening" dropped from the toolkit; new **Insight toolkit** added above the (now demoted) Question toolkit; steps renumbered (the file had two "Step 5"s)
- `weekly-review.md` — *"let them arrive at it themselves, don't present it like a finding"* → **present patterns as findings with dates attached**; challenge whenever the record supports it, not only on self-dishonesty
- `monthly-review.md` — *"ask about it gently — let them arrive at the honest read themselves"* → **say it plainly with the evidence**; minimum deliverable is one month-spanning cross-time read + one named call
- `checkin.md` — unchanged in length; gains a hard-capped **one-sentence** optional read, explicitly outranked by the re-entry rule and forbidden when it would land as criticism at 10:40pm

**Why:** Reese's call, opening this session: *"I want Claude to be like a person who is able to generate insight now rather than just 'hearing me out.'"* The audit confirmed the gap was real and was in the *mechanics*, not the identity — every skill already declared "you are a mentor, not a therapist" in its Tone section while the step-by-step instructions enforced textbook Rogerian practice (withhold conclusions, let the client discover it). Net effect: `/brutally-honest` was the only skill in the system permitted to state a finding, so the only two settings were *validate* and *audit with receipts*, with nothing in between. The doctrine fills that middle. Tone is explicitly unchanged — process praise, "and" not "but", cue-level habit diagnosis, gaps-are-data — the only change is that the coach now shows up with something.

**Source / evidence:** Reese's request, 2026-08-04. Offending lines quoted above were pulled verbatim from the pre-change files. New file: `COACHING.md`. Related: memory `feedback_mentoring_tone.md` (2026-04, established the mentor *tone*) — this decision supplies the missing *mechanics*.

---

## 2026-07-07 — `/learn new`: an on-demand mode (Reese names the topic)

**What changed:** Added a fourth `/learn` mode — **`/learn new <topic>`** (aliases `adhoc`, `work`, `just-in-time`) — where Reese supplies the topic himself instead of it coming from a curated roadmap. New home: `career/on-demand-learning/` (`summary.md` is a *ledger/index* of what's been learned on demand, not a pre-planned unit list; + `reflection_log/`). Same `/learn` rigor (research-first → probe → teach → explain-back → build-before-bank). **Adaptive** on two axes: technical topic → writes a `.py` worksheet in `lesson_assignments/` and may enter `concept_queue.md` for `/sharpen`; conceptual topic → no worksheet, bank by using it (like `soft`). At persist, the "roadmap update" is appending a ledger row, not ticking a `[ ]`. When a cluster of related topics forms, the mode offers to **graduate** it into its own full track (the precedent: soft-skills, created earlier today). `.claude/commands/learn.md` updated: intro, Step 0 table + adaptation bullet, Step 1 (skip roadmap scan), Step 8 (ledger append).

**Why:** Reese's request — work regularly hands him something new he must learn *before* he can use or add it, and he wanted that just-in-time learning **banked here** rather than lost. The three existing tracks are all pre-curated roadmaps; none had a slot for emergent, work-driven topics. This closes that gap without polluting the curated tracks, and the graduation path means a recurring on-demand topic can become a real curriculum when it earns it.

**Source / evidence:** Reese's request during the 2026-07-07 `/learn soft` session, immediately after the three-track restructure. Files: `.claude/commands/learn.md`, new `career/on-demand-learning/`.

---

## 2026-07-07 — `/learn` goes from two tracks to three; mid-python repurposed; soft-skills added

**What changed (three linked decisions):**
1. **`/learn` now drives THREE parallel tracks, not two.** Step 0 of `.claude/commands/learn.md` updated: `ai` (AI Engineering — master track), `py` (Python Mastery), and new `soft` (Senior Engineering — Soft Skills). Track selected by token; ASK-ONCE fallback now names all three.
2. **The mid-python track was repurposed, not deleted.** The specific mid-level Python role that seeded `career/mid-python-developer-prep/` ($115k FastAPI weather-data shop) **closed before it was filled.** Rather than discard the work, its purpose was re-pointed from "demolish this one interview" → "Python mastery underpinning the AI-eng path." The FastAPI/weather intel is retained as realistic practice material, not *the* target job. Summary header reframed; `/learn` table updated.
3. **New `soft` track is worksheet-exempt and does NOT use `concept_queue.md`.** Soft skills have no code to green-light, so Step 7.5's `.py` worksheet is skipped for this track; the Step 7 "build" becomes a **real interaction** (interview answer, Slack/PR message, design doc). They're not defended cold in `/sharpen` either — soft skills are deployed under real conditions. Roadmap lives at `career/senior-engineering-soft-skills/summary.md` (6 units, Larson/Reilly/Fournier/Orosz as the resource pool).

**Why:** (1+2) Reese's mid-level dev job closed, but he explicitly chose to preserve the prep rather than let the loss collapse the work — Python mastery is genuinely foundational for AI engineering, so the content's value survives the job. (3) He asked to make senior/soft-skills a full track ("just as important as everything else"). At ~1yr in, aiming $120k+, the social/communication layer is the differentiator on top of technical skill — and unlike an API it has no runnable-test artifact, so the machinery was adapted honestly rather than faked.

**Source / evidence:** Reese's request during the 2026-07-07 `/learn` session (Unit 1 — Scope of Impact, the first soft-skills unit). Files touched: `.claude/commands/learn.md`, `career/mid-python-developer-prep/summary.md`, new `career/senior-engineering-soft-skills/`.

---

## 2026-06-22 — `/learn` now leaves a solo worksheet (lesson assignments)

**What changed:** Every `/learn` session now produces a self-contained, runnable **lesson assignment** at `career/lesson_assignments/YYYY-MM-DD_<kebab-unit>.py` — a struggle-first worksheet Reese can re-do alone. Added as **Step 7.5** in `.claude/commands/learn.md`. Three parts: (1) a short soliloquy on the target, (2) tiny isolated coding exercises with boilerplate pre-filled (concept/flow over syntax) and **Claude pre-writes the assert-based tests** for red/green solo feedback, (3) concept questions with a stated requirement + a gated answer key. Reference template: `career/lesson_assignments/2026-06-22_llm-call-anatomy.py`.

**Cross-skill guardrail:** `/sharpen` and `/drill` were updated with an "inspiration, not a crutch" note — they may borrow *angles* from a worksheet but must never read its prompts verbatim or surface the answer key before cold recall. Cold defense stays cold.

**Why:** Reese asked for it — a conversational `/learn` evaporates once the chat scrolls away; a runnable worksheet with pre-written tests turns the lesson into repeatable, phone-friendly homework with built-in feedback, and preserves the struggle-first principle when he works solo. The worksheet hits the *other* facets of the unit (not the Step-7 build he already did), widening coverage of the same primitive.

**Source / evidence:** Reese's request (2026-06-22) during the §1.1 `/learn` session. First worksheet (`2026-06-22_llm-call-anatomy.py`) shipped as the template; his `llm_cost.py` build confirmed the unit landed.

**Date:** 2026-06-22

---

## 2026-06-22 — Learning system: concept-driven engine replaces course-driven curriculum

**What changed:** The AI Engineering Master Guide was demoted from a course-completion curriculum ("complete in order, no skipping") to a **reference / source-of-truth**. The primary daily learning engine is now `/sharpen` + `career/concept_queue.md` — concept-driven, struggle-first, tied to Reese's own shipped code, logged to `CAREER_LOG.md`, maintained by `/drill`. Courses are reframed as **gap-fillers pulled on demand**, not a syllabus.

**Specifically:**
- Master Guide gained a "How to Use This Guide" section; Phase 1 retitled to a "Course Library — gap-fillers, pulled on demand"; Learning Philosophy rewritten around the sharpen→build→bank→drill loop.
- `concept_queue.md` Notes hardened with the rule: *concepts pull resources; resources don't push concepts.* Syllabi may be mined for candidate concepts, but they enter the pool **unprioritized** — never transcribed wholesale into a completion checklist.
- `CLAUDE.md` ADHD Learning Protocol reconciled: "One active course / Pre-commit a project / Build before next lesson" replaced with a concept-driven primary engine + a non-negotiable build anchor ("build before you bank") + course rules scoped to gap-filler mode only.
- **Capstone preserved as dedicated** (not folded into autoclip). The build mandate stays explicit so concept-grilling doesn't become passive consumption with extra steps.

**Why:** Structured courses don't survive the ADHD motivation system — Reese abandons them mid-way. The concept-queue loop delivers immediate reward, phone-friendly access (Claude Code mobile), and always-visible progress in `CAREER_LOG.md`, while directly producing the thing that matters for the AI-consultant target: defensible "why THIS over THAT" judgment, not passive exposure.

**Source / evidence:** Reese's own proposal (2026-06-22) + the `/sharpen` skill and `concept_queue.md` shipped the same day (commits `100600d`, `896c3b6`). The main tradeoff considered: a full deletion of the guide would have dropped the capstone build mandate and North Star context — rejected in favor of demote-to-reference + keep-dedicated-capstone.

**Date:** 2026-06-22

---

## 2026-06-22 — Technical learning moves fully in-catalog: `/learn` skill + live-researched curriculum replace online courses

**What changed:** Built a third learning skill, **`/learn`** (`.claude/commands/learn.md`), the *acquisition-from-zero* front of the pipeline: `/learn` (acquire, researched live) → `/sharpen` (defend cold) → `/drill` (retain). It walks a new technical curriculum at **`readings/ai-engineering-curriculum/summary.md`** — a sequenced, tiered **skeleton** of ~60 units across 8 sections (Foundations, LangChain Core, Agents, LangGraph, RAG, MCP, Evals/Observability, Async/Production) plus the Tier-2 periphery. Online technical courses are **no longer taken**; their content was mined into the curriculum and the actual teaching is generated **live against current docs** each session, so it never goes stale.

**Specifically:**
- Curriculum is a skeleton (objectives + tier + source + currency flags), not pre-written lessons — per the earlier 2026-06-22 decision that pre-baked content goes stale.
- Added a **⚠ Currency Watch** section capturing the breaking changes live research surfaced: LangChain v1 (`create_agent` over `AgentExecutor`, `langchain-classic`, `system_prompt`, TypedDict state), MCP 2025-11-25 (SSE-as-transport deprecated, structured output, elicitation, tasks, OAuth 2.1), RAGAS collections API + metric renames, LangGraph v1 (`interrupt()`, durability modes, supervisor/swarm split out), prompt-eng 2026 (prefilling removed, adaptive thinking, over-prompting backfires).
- Wired the three-stage pipeline into the Master Guide ("How to Use"), `concept_queue.md` (pipeline position), and `CLAUDE.md` ADHD Protocol.
- Two ledgers kept distinct: curriculum tracks *acquisition*; concept_queue tracks *defense*; CAREER_LOG tracks *mastery + cadence*.

**Why:** Online courses don't survive the ADHD motivation system AND go stale fast (a 2024 course teaches deprecated patterns). Learning in-catalog with live research solves both: immediate-reward + phone-friendly + always-tracked, AND always-current. Reese's own framing: "the technical things can be completely learned through here, as long as everything is backed and researched live (which is also helpful so the courses aren't outdated)."

**Source / evidence:** Reese's proposal (2026-06-22) + 5 parallel research subagents that pulled the current syllabi/docs for Eden Marco LangChain/LangGraph, MCP Masterclass + spec, RAG-evals + RAGAS, LangChain Academy + LangGraph/LangSmith, and Anthropic prompt-eng — each returning current topics plus a "potentially outdated" delta. Those deltas became the Currency Watch. Design forks confirmed via AskUserQuestion: new `/learn` skill (not folded into `/sharpen`), skeleton-map (not pre-written), research real syllabi live (not docs-only).

**Date:** 2026-06-22
