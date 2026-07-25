# The Independence Protocol — the 6-month answer to the mid-year review

**Created:** 2026-07-25, in response to John's six GoPerform notes (primary source: `career/reflection_log/2026-07-25.md`).
**Horizon:** Aug 2026 → Jan 2027 (year-end review).
**One-line thesis:** Use AI to *learn faster than anyone*, and prove capability *without* it — visibly, on a scoreboard John himself wrote.

---

## The reframe that makes this workable

Reese's tension: *"I know I'm using AI to learn — but that's the point."* Correct — and John agrees: the one appreciation note on Credentials praises the training pace. The distinction that resolves it:

- **AI as tutor** — every interaction *increases* what you can do without it. (Fine. Encouraged. Keep.)
- **AI as prosthetic** — AI substitutes for performance; remove it and output collapses. (This is what John saw under stress.)

The existing pipeline (`/learn` → `/sharpen` → `/drill`, struggle-first, build-before-bank) is already tutor-mode by design. What it's missing is not discipline — it's two layers it never had:

1. **An unassisted-performance rep** — nothing in the system currently makes you produce *without* AI, on a clock, the way work does.
2. **A visibility layer** — John can't see the catalog. He sees standups, commits, PRs, and how you behave when a codebase is on fire.

The protocol adds both. Nothing existing is removed.

---

## Layer 1 — The learning ladder (how to learn *anything*: docs, tutorials, new domains)

This is the upgraded struggle-first rule. For any new concept, tool, or domain (agile ceremonies, AWS service, systems design pattern — the ladder is domain-agnostic):

1. **Recall first (2 min).** Before opening anything: what do I already know? Write three lines from memory. (Primes retrieval; exposes the real gap.)
2. **Primary source next (15–20 min minimum).** Official docs, spec, or source code — *not* AI, not a blog. Keep a one-line **docs log**: what I looked up, where the answer lived. This trains the exact skill John calls "core analytical ability": navigating primary sources under your own power. Tutorials are allowed here; AI is not.
3. **Build by hand.** The attempt is typed by you, no AI in the editor. Wrong is fine — wrong is data.
4. **AI as examiner, never author.** Only after the attempt: share what you tried, where you're stuck, and ask it to help you *see* what you're missing — grade the attempt, name the gap, point back to the doc section. The artifact stays yours.
5. **Bank it.** Curriculum checkbox → concept queue → CAREER_LOG, exactly as now.

**The rule that changed:** the old rule limited *when* AI enters (10–20 min). The new rule also limits *what AI is allowed to do* when it enters: examine, not author. For learning reps this is absolute.

## Layer 2 — The Cold Bench (the missing rep — build the muscle John says is absent)

Once a week, peak window, 60–90 minutes, timer running:

- Pick a **work-shaped task** at or slightly above the tier bar. Sources: curriculum sections, capstone checklist, or a real work ticket reshaped. Examples: wire a `StateGraph` with a conditional edge from a blank file; write the Dockerfile + compose for a two-service app; design and defend an API for a feature; debug a deliberately-planted failure; write an ADR for a real decision.
- **Docs allowed. AI forbidden. Until the timer ends.** This is stress inoculation — the precise condition ("high-stress, complex codebase, no help coming") the review says you fail in, rehearsed weekly at safe stakes.
- **Post-mortem with AI as grader:** what would have failed in production, what took longest, which gap goes into the concept queue next.
- **Log it** in the ledger below. The ledger *is* the evidence base — by January it's six months of dated, unassisted output.

### Cold Bench ledger

| Date | Task | Time | Unassisted result | Gap found → queued |
|---|---|---|---|---|
| | | | | |

## Layer 2.5 — The Ownership Audit (know your own systems end-to-end)

The concept queue was always seeded from "his own shipped code — the richest curriculum." This layer makes that a *practice*: the 12:00 weekday block (the retired pipeline slot, now the **🧭 Ownership block**) is spent auditing and documenting his own projects until he can walk any of them end-to-end, cold.

**The rep (one slice per sitting, ~25 min):**
1. Pick ONE module from the queue below — never "the project," always a slice.
2. Read it like a reviewer who didn't write it.
3. Document it *in that project's repo*: what it does, **why this over that**, the data flow, the failure modes. ADR-style where a real decision lives.
4. Anything you can't explain cold → a row in `career/concept_queue.md`. That's the audit finding — the gap goes into the `/sharpen` funnel.
5. Tick the slice below with the date.

**Why this matters for the review:** "true mastery of your craft" = walking your own architecture without notes. These audits are also the raw material for ADRs #1–2, the tech talk, and design-review credibility — the scoreboard artifacts write themselves out of this block.

**Audit queue (seed — reorder freely, add slices as discovered):**

*autoclip:*
- [ ] Pipeline architecture end-to-end — ingestion → processing → output; why Celery over FastAPI background tasks
- [ ] Embedding + retrieval layer — why Voyage AI, why pgvector; chunking choices
- [ ] Hooks/guardrails — pre/post structure, what each gate catches
- [ ] Deployment + config surface — env, secrets, what breaks first under load

*CFO Agent:*
- [ ] Agent graph — nodes, state schema, edges; why this topology
- [ ] Retrieval path — pgvector integration, query shaping
- [ ] Auth + API surface — login flow, endpoint contract
- [ ] Prod posture — what Gate 2 verified, health checks, PG+Redis wiring

**Worst-day minimum (this is Floor #2 now):** one doc line or one audit note on your own code. Two minutes counts.

## Layer 3 — The work-visible layer (what John actually sees)

The catalog is invisible to him. These four behaviors are the review's own prescriptions, made operational:

- **Own every line.** Never commit a line you can't explain cold. If AI produced it, rewrite it or work it until you can defend the *why* at a whiteboard. (This is the mastery standard — "why THIS over THAT" — applied at commit time. It converts every workday into `/sharpen` reps.)
- **First hour AI-free.** On any hard ticket: read the code, read the docs, write a 5-line plan *before* any AI involvement. Then, if used, AI pressure-tests the plan instead of replacing it. Independence that starts the task is independence colleagues can see.
- **The comms floor (daily, non-negotiable at work):** honest standup — yesterday / today / *blockers stated early and specifically* (his phrase was "honest standups"); risk surfaced the same day you smell it, in writing; pull/rebase daily, small commits, announce before touching shared files (kills the Verizon merge-conflict pattern at the root).
- **Keep the composure asset in front.** The appreciation note is proof it's working. Collected-and-constant under stress is now a named strength — it's the trait to lead with in the exact high-stress moments the other notes are about.

## Layer 4 — The scoreboard (blow them out of the water, using their own rubric)

Every "Measured by" line in the review goals is an artifact. Artifacts are dated, visible, and undeniable — reviews built on them can't be vibes. The campaign:

| When | Artifact | Review goal it lands on |
|---|---|---|
| Aug | Cold Bench running weekly + comms floor live daily | Technical Mastery, Project Leadership |
| Aug–Sep | AWS cert study in the peak window → **sit the exam** | Credentials (Q2 line, delivered late > never) |
| Sep | **ADR #1** on a real work decision | Technical Mastery Q3 ("2+ ADRs") |
| Sep–Oct | **Mentor one person** formally (Orion mentorship already forming — name it, cadence it) + one cross-team initiative | Mentorship Q3 |
| Oct | **ADR #2** + peer design review participation | Technical Mastery Q3 |
| Oct–Nov | Capstone: architecture doc → working skeleton (the build that makes the ADRs and design-review credibility real) | Technical Mastery, EA Modernization |
| Nov | **Tech talk or presentation** (candidate topic: what the modernization pipeline taught about agentic migration — you own this material) | Mentorship Q4 |
| Nov–Dec | **Lead a design review**; KB article published | Technical Mastery Q4, Credentials Q4 |
| Dec–Jan | **One full project lifecycle owned** — scoping to delivery, with the comms floor as the trail of accountability | Project Leadership Q4 |
| Jan | Year-end package: the ledger, the ADRs, the talk, the cert, the mentorship record — assembled and handed over | The whole review |

## Cadence (folds into the existing engine — nothing new to remember daily)

> **The daily version of this protocol is the time-anchored checklist at the top of `agenda.md` ("The Daily Protocol").** That table is the single source of truth for the day; this section is the summary.

- **Daily:** the Floor as-is · comms floor at work · one `/drill` (non-peak).
- **Peak blocks:** unchanged engine (`/learn` / `/sharpen`, one concept to the bar) — now under the Layer-1 ladder; **one block per week is the Cold Bench.**
- **Weekly (`/weekly-review`):** check the ledger got a row, the comms floor held, one artifact moved.
- **Monthly (`/monthly-review`):** scoreboard row check — on pace for January?

## Failure modes to watch (name them now, catch them early)

- **All-or-nothing collapse** (the documented #1 risk): a missed Cold Bench week is data, never debt. Re-entry is `/checkin`, same as everything else.
- **Stealth prosthetic:** "AI as examiner" quietly becoming "AI writes it and I read it." The tell: you can't reproduce the artifact the next day. The ledger catches this — unassisted results don't lie.
- **Invisible progress:** doing all of this and never letting John see it. Counter: the artifacts are *at work, in work systems* — ADRs in the repo, updates in the channel, the talk on the calendar. The catalog stays the engine; the evidence lives where he looks.
