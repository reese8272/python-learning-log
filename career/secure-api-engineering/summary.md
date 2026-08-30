# Secure API Engineering on AWS — roadmap

> ## ⏸ PAUSED — 2026-08-27 (Phase 3)
>
> **This track is formally paused, not abandoned and not deleted.** All four curriculum tracks were paused together in the Phase 3 rewrite. The honest number that drove it: **4 banked units out of 233 across all four roadmaps since April — one `[x]` apiece.** Every track launched and stalled at unit 2. That's not a pace problem; it's a signature.
>
> **What this file is now:** a **reference catalog**, not a backlog. Nothing here is owed. There is no ACTIVE track and no track menu. Look things up here freely; do not "resume the roadmap."
>
> **What replaced it:** work generates the curriculum now. Craft reps (the Cognizant project) and Business reps (client work) throw off things that couldn't be explained — those get captured, and `/drill` and `/sharpen` walk the captures. `/learn new <topic>` handles on-demand acquisition when a capture needs real teaching.
>
> **The material is good and it was never the problem.** The one time learning visibly converted to career movement (07-28 → 07-29, the work quiz then the boss call) it was a **defense** rep under real stakes, not an acquisition rep. Phase 3 stops manufacturing stakes and uses the real ones.
>
> Un-pausing is an `/audit` decision, not a mid-session one. See `SYSTEM.md` Layer 2 and `DECISIONS.md` (2026-08-27).


> **⏸ PAUSED 2026-08-27 (was ACTIVE).** Created 2026-08-10 as a 7-day interview sprint; **de-timeboxed 2026-08-13** when that role closed on years-of-experience before an interview happened. The clock is gone. The curriculum stayed, because it's the production-API and security layer under everything else being built — the capstone spec is FastAPI + `Depends()` auth + Docker + AWS, and `secure-api-lab` is the only fully-specified project in the system. See `DECISIONS.md` (2026-08-13).

**What this is:** A ground-up curriculum in secure API engineering, taught in-catalog via `/learn`, **researched live against current official docs**, then handed to `/sharpen` (defend cold) and `/drill` (retain). This roadmap is the *what to cover and how deep*; the teaching is generated fresh each session so it never goes stale.

**The framing — build UP from zero.** Assume nothing is owned. Every unit starts at `[ ]`, **including things you ship at work today**, because the goal isn't *exposure* — it's being able to produce it cold. A thing you use daily but can't explain *why this over that* is the thing that falls apart one level past the happy path.

The one place your existing work is used: **as the worked example.** Where you have shipped code, the teaching anchors to CreatorClip or CFO Agent instead of a toy app. That's salience, not a shortcut — the unit still gets taught from the mechanism up. **And check first whether he's already operated it** *(standing instruction, 2026-08-11)*: in §1 the gap turned out to be vocabulary, not understanding — CPU-bound work leaving the request path is exactly what Celery does in CreatorClip. Teach the name onto the thing he already built rather than teaching the thing.

**Source of truth:** current official docs (live-researched every session), `career/helpful_notes_and_guides/AI Engineering Master Guide.md` for the mastery standard ("can I explain why THIS over THAT?"), and `career/helpful_notes_and_guides/Learning Science Protocol.md` for how the sessions are shaped.

---

## 📏 Depth bars

Every unit carries a bar. The bar says how long to spend and what "done" means, and it **binds in both directions** — don't over-teach a `[C]`. Full definitions live in `/learn`; the table is here for reading the roadmap.

| Bar | Means | Done sounds like | Budget |
|---|---|---|---|
| **`[A]` BUILD IT** | Implement from scratch cold; name the failure mode | *"I can write it, say why this over that, and what breaks if I'm wrong."* | ~30 min |
| **`[B]` EXPLAIN IT** | Defend the decision, not the internals | *"I know when to reach for it and the one-line why."* | ~15 min |
| **`[C]` NAME IT** | One sentence — enough to not be blindsided | *"I know what that is and where it shows up."* | ~5 min |

**Where the `[A]`s cluster:** on what you'd have to *produce* cold — the JWT validation path, the OAuth2 flow map, async/DI, `response_model`, the AWS request path, and the negative test matrix. **§8 (HIPAA) and §9 (CI/CD) stay capped at `[B]`/`[C]`** — context, not craft. **§5 (mTLS) was mostly re-barred `[A]`→`[B]` on 2026-08-13**, since those `[A]`s existed because one specific posting named mTLS as a hard requirement.

**Status keys:** `[ ]` not started · `[~]` taught, not yet banked · `[x]` banked (date) → enters `/sharpen` then `/drill` rotation.

> ⚠️ **`[~]` → `[x]` is not a teaching session's call.** Banking requires the section worksheet running green **or** a clean cold re-ask at Step 1.5 of a later session. See `Learning Science Protocol.md` #5.

---

## 🔁 How a session runs

The session protocol — the chunk loop, the Ladder, the three in-session check formats, and the Learning notes convention — **is now evergreen and lives in `/learn`** (`.claude/commands/learn.md`). It was invented here during the sprint and promoted out on 2026-08-13 so every track gets it. Nothing about it is track-specific anymore.

The two things still specific to this track:
- **Chunks are predeclared** per section below (`1.A`, `4.C`, …), so a session can stop cleanly mid-section.
- **Worksheets are one per SECTION**, at `career/lesson_assignments/apisec-<section>-<kebab-name>.py`, and **PART 3 of each is that section's real issue** in `career/lesson_assignments/secure-api-lab/docs/issues.md`.

## 🎯 Section → project map

One project per section — the already-written issues in `career/lesson_assignments/secure-api-lab/docs/issues.md`. This is the top rung of the Ladder: the place where a taught unit becomes code with no scaffolding under it.

| Section | Project |
|---|---|
| §1 + §2 | **Issue 1** — FastAPI skeleton + OpenAPI contract |
| §3 | **Issue 2** — Okta tenant issuing real tokens |
| §4 + §7 | **Issues 3 + 4** — validation dependency + negative test matrix |
| §5 | **Issue 5** — mTLS with a local CA |
| §8 | **Issue 6** — audit logging with PHI redaction |
| §6 | **Issue 7** — the AWS deploy *(load-bearing)* |
| §9 | **Issue 8** — CI/CD with OIDC federation |

---

## 📌 Why these units — evidence from a real posting

*This curriculum wasn't assembled from a syllabus. It was reverse-engineered from a live 2026 job description for a secure-API role (FastAPI + OAuth2/JWT/mTLS + Okta + AWS, HIPAA environment). That role closed on years-of-experience, but **the posting remains good evidence of what this skill set is actually worth in the market** — which is why the section list survived the role. Kept as market evidence; the interview framing is gone.*

- **"high-performance, secure, and asynchronous"** — three words, three separate probes. *Asynchronous* means the event loop and what happens when you block it. *High-performance* means workers, topology, pagination. *Secure* is a whole half of the job. → **§1**
- **"contract definition and maintenance"** — **maintenance** is the tell. Not "does FastAPI generate a spec" (it does, free) but: have you *versioned* one, caught a breaking change, handed a spec to a consuming team? → **§2**
- **"exposing APIs that support integration with IDP (like Okta)"** — the most revealing line. It means **your API is a Resource Server, not an authorization server.** You validate tokens Okta issued; you never issue them. Getting this backwards is visible immediately. → **§3**
- **"mTLS for service-to-service"** — note the qualifier. Not browsers; internal service auth. That implies a mesh or internal PKI, and it's why Private CA is the very next bullet. → **§5**
- **"ECS, ALB, Route 53, S3, API Gateway" + ACM/PCA + WAF/Shield + CloudWatch** — a complete request path, not a random list. Learn it as **one diagram**. → **§6**
- **"Proven ability to deploy, secure, and operate"** — *proven* and *operate*. The bullet you cannot talk past; it's why Issue 7 is a real deploy. → **§6**
- **"test authentication, authorization, headers, and request/response flows"** — a **negative test matrix**, described nearly verbatim. → **§7**
- **HIPAA / PHI, CI/CD** — listed as *Desired*, not required. Hence the `[C]` cap. → **§8, §9**

---

## ⚠ Currency Watch — verified live 2026-08-10 · **stale since then — re-verify per unit before teaching**

Several of these are recent enough that most people working in this space don't know them yet. **The dates below are the point:** anything more than a few months old here should be re-checked live, not trusted. That's Rule 1.

- **`python-jose` is out; `PyJWT` is in.** The official FastAPI security tutorial migrated; python-jose is effectively unmaintained. Half the tutorials online still teach it. For RS256 (what Okta uses) install **`pyjwt[crypto]`**. → [FastAPI docs](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/)
- **OAuth 2.1 is still an Internet-Draft, not an RFC** — `draft-ietf-oauth-v2-1-15` as of March 2026. Say *"the de-facto 2026 baseline, though still a draft"* — the precision is a credibility marker. Changes: implicit removed, ROPC removed, **PKCE required for every client including confidential ones**, exact-match redirect URIs, refresh-token rotation. → [oauth.net/2.1](https://oauth.net/2.1/)
- **🔥 ALB can verify JWTs itself — shipped 2025-11-12.** Give the listener a JWKS endpoint and issuer; it validates signature, expiry, and claims before the request reaches your app. HTTPS listeners only, supports client-credentials. Nine months old and directly on-topic. → [AWS announcement](https://aws.amazon.com/about-aws/whats-new/2025/11/application-load-balancer-jwt-verification/)
- **ALB mTLS has two distinct modes.** **Passthrough**: ALB forwards the cert chain in `X-Amzn-Mtls-Clientcert` for your app to authorize on. **Verify**: a **trust store** resource with a CA bundle + CRLs, and ALB rejects bad certs itself. Related headers: `-Subject`, `-Issuer`, `-Serial-Number`, `-Validity`. → [ALB mTLS docs](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/configuring-mtls-with-elb.html)
- **AWS Private CA has two tiers and the gap is the story.** General-purpose **~$400/CA/month**; short-lived-certificate mode **~$50/CA/month + $0.058/cert**, max 7-day validity. The cheap tier exists *because* modern service-to-service mTLS wants frequently-rotated certs. → [pricing](https://aws.amazon.com/private-ca/pricing/)
- **Okta specifics that bite people:** you need a **custom authorization server** to protect your own API. **Client-credentials cannot request OpenID scopes** — no user exists, so define a custom scope. Validate **both `aud` and `cid`**. Cache JWKS; re-fetch only on an unknown `kid`. → [Okta guide](https://developer.okta.com/docs/guides/implement-grant-type/clientcreds/main/)
- **Pydantic v2 / FastAPI idioms:** `model_dump()` not `.dict()`, `@field_validator` not `@validator`, `pydantic-settings` for `BaseSettings`, `lifespan` not `@app.on_event`, `Annotated[X, Depends(...)]` not `= Depends(...)`.
- **`httpx.ASGITransport`** is the current async test-client pattern; `TestClient` is fine for sync.

---

## Section 1 — FastAPI at depth
**Chunks:** 1.A the event loop → 1.B dependency injection → 1.C contracts & response shaping → 1.D lifecycle & errors
**Project:** Issue 1 · **Budget:** ~150 min teaching + ~60 build

### 1.A — The event loop
- [x] **1.1 ASGI vs WSGI** `[B] ~15m` *(2026-08-11)* — the concurrency model; why "high-performance" in this JD means the loop; uvicorn/gunicorn worker topology.
- [~] **1.2 `async def` vs `def`, and the threadpool trap** `[A] ~30m` *(chunk 1.2a taught 2026-08-18; **1.2b pending**; build assigned, not run)* — FastAPI runs plain `def` handlers in a threadpool; a blocking call inside an `async def` stalls **every** request on that worker. Covers `run_in_executor` and how to spot a blocking call in a library you didn't write. *The single most likely "do you actually understand async" question.* **Breaks if wrong:** one sync DB driver in an async handler and your p99 goes to seconds under any concurrency.

### 1.B — Dependency injection
- [ ] **1.3 `Depends()` and why auth belongs in a dependency** `[A] ~30m` — DI as the composition point; sub-dependencies; per-request caching; `dependency_overrides` as the testing seam. *The mechanism §4's entire JWT design rests on.* **Breaks if wrong:** auth-in-a-decorator can't be overridden in tests, so the auth path ships untested.
- [ ] **1.4 The `Annotated` idiom** `[C] ~5m` — current form vs the old default-value style.

### 1.C — Contracts & response shaping
- [ ] **1.5 Pydantic v2 as the request contract** `[B] ~15m` — validation at the boundary; `model_dump()`; why precise type params make the generated OpenAPI schema precise.
- [ ] **1.6 `response_model` as a PHI-leak control** `[A] ~30m` — response filtering isn't cosmetic; it's how HIPAA minimum-necessary gets enforced at the serialization layer. *Say this §1→§8 connection in the room — it's what separates studying a list from understanding a system.* **Breaks if wrong:** you return the ORM object, and every column ships — including the ones the caller has no right to.

### 1.D — Lifecycle & errors
- [ ] **1.7 `lifespan`** `[C] ~5m` — startup/shutdown resources; replaced the deprecated `@app.on_event`.
- [ ] **1.8 Exception handlers and the error contract** `[B] ~15m` — consistent envelopes; never leaking internals or stack traces in a 500.
- [ ] **1.9 Middleware vs dependency — when each** `[C] ~5m` — cross-cutting (correlation IDs, timing) vs per-route authorization.

### 📝 Learning notes — Section 1

*(In progress — 1.1 taught 2026-08-11; 1.2a taught 2026-08-18. Append as the remaining chunks land.)*

**Asked** *(2026-08-11, chunk 1.A)*
- Do I need the acronyms? Is "contract" the agreed format between two things?
- What are ongoing channels / WebSockets?
- **"If both send the same data, how does ASGI cost less?"** — the best question of the session; it's the mechanism of the whole unit, and he found it himself rather than accepting the table.
- How is a connection physically established, and how does an idle process know to stay open vs. close? (Answered: `epoll`/`kqueue` — the kernel wakes the process; it never polls.)
- Are WSGI/ASGI just standards rather than frameworks or packages?
- Is uvicorn the same thing as FastAPI?

**Asked** *(2026-08-18, chunk 1.2a)*
- Does `timeout=10` mean the request waits 10 seconds and then fails — and is that a 502? *(Answered: it's a **ceiling, not a duration**; if it fired → `ReadTimeout` → unhandled → **500** from the app. 502 is what a **proxy** returns — an ALB in front of a dead task.)*
- **"What is `async with`? Is it like `with open(file) as f` — automatic open and close?"** — exactly right, and he got there from the analogy unprompted. The `async` prefix means `__aenter__`/`__aexit__` are coroutines, so setup/teardown can themselves await (closing pooled sockets is I/O).

**Landed**
- ASGI wins on I/O-bound waiting, buys nothing on CPU-bound work. ✅ cold, first try.
- **WSGI/ASGI are specifications, not packages** — he arrived at this unprompted and stated it cleanly.
- uvicorn = server / FastAPI = framework, correctly separated.
- Heap = the pool for objects that must outlive the call that created them.
- One uvicorn process per container on ECS (had the answer before the reason).

**Landed** *(2026-08-18, chunk 1.2a)*
- `await` = **suspend point**, and `asyncio.gather` is what makes three 1s calls take 1s. ✅ cold — **clears an 08-11 Tripped item.**
- Fill-in-the-blank: `def` → **threadpool** → **40** slots; `async def` + a blocking call → effective concurrency **1**. ✅ cold, all three.
- `ceil(N / pool) × duration` as the threadpool throughput formula — **method produced cold** (arithmetic slipped, see Tripped).
- **His own sentence, better than the one I gave him:** *"unless we write our own await logic too, we are not only not guaranteed concurrency, but we are explicitly not helped from our own blockage, whereas `def` will help us."* **`async def` is opting *out* of the safety net.** This is the one to say out loud.
- `async with` = context manager, arrived at via his own `open(file) as f` analogy.

**Tripped** → *(the pre-built drill list)*
- **"WSGI is better for CPU-bound work"** → ❌ Neither helps. CPU work is core-bound; both scale it with processes. The asymmetry is that WSGI *degrades* (one thread burns) while ASGI *stalls* (the only thread burns).
- **"ASGI becomes WSGI if you handle async badly"** → ❌ It becomes **strictly worse** than WSGI — WSGI still has N other threads; a blocked loop has nothing.
- **"The ASGI connection stays open for the app's lifetime"** → ❌ Two sockets, not one tunnel: the **listening** socket is app-lifetime; a **connection** socket is client-lifetime, and ASGI is invoked once *per connection*.
- ~~**`await` groups coroutines**~~ → ✅ **cleared 2026-08-18**, re-asked cold and correct (`asyncio.gather` / `TaskGroup`).
- **Heap = "stack-like with fast lookups"** → ❌ conflated with a hash map / the heap data structure.
- One-worker-per-container *reason* → had the rule, not the why. Correct why: **nested process managers — ECS can't observe or restart a worker inside a task, so a hung worker looks healthy.** *(⚠ re-asked 2026-08-18 and **still missed** — answered "work goes to the other 3," which is the mechanism of the danger, not what ECS observes. Re-ask again in the reason form: **ECS sees a HEALTHY task** — PID 1 alive, health check passes ~75% of the time, silent 75% capacity forever, no alarm, no restart.)*
- ~~**Listening vs connection socket**~~ → ✅ **cleared 2026-08-18 (`/drill`, 3rd ask)** — but read the caveat. Cold count was **3, not 4**: the connection sockets and their client-lifetime came out clean (new — both prior attempts were nowhere near), the **listening** socket was dropped entirely. It then came out cleanly *under a probe*: "close the listening socket mid-request" → **"the 3 tabs finish fine, the 4th gets connection refused."** That's the mechanism, not the label, so it clears — **but it has never been produced cold.** Moves to the `/drill` rotation, **re-ask in ~1 week** in the cold count form.

**Tripped** *(2026-08-18, chunk 1.2a)*
- **"`async def` means all 50 requests finish in ~2 seconds"** → ❌ ~**100s**. He computed 100s first, then talked himself out of it. `async def` is a *promise to the loop*, not a capability from it — `requests.get` has no `await` in front of it, so there is no suspend point and the loop is held for the full 2s, fifty times.
- **Plain `def` version of the same handler = 100s** → ❌ ~**4s**. The *less* async-looking version is **25× faster**, because FastAPI ships `def` handlers to the 40-wide threadpool.
- **Throughput formula = `N × duration`** → ❌ `ceil(N / pool) × duration`.
- **`200 / 40 = 50`** → ❌ **= 5**. Method was right, arithmetic slipped 10× (**25s**, not 250s). Worth catching: 25s vs 250s is the difference between "degraded" and "the ALB health check timed out and ECS is cycling your tasks."
- **"WSGI can pawn off CPU-bound work to other threads"** → ❌ No handoff exists; the request *arrives* on its own thread. **WSGI degrades to 39/40 capacity; ASGI goes to zero.**
- **Idle CPU + 8s p99 → "no await was established"** → ⚠️ true but not an answer to *why those symptoms discriminate*. All three candidates give high latency. **Undersized instance → CPU pegged, not idle. Slow DB → slow even at concurrency 1. Blocked loop → a single request is *fast*; latency is pure queue depth, linear in request rate, CPU flat.** The test is one sentence: **"send one request to an idle box."**

**Watch**
- **States the rule, not the reason.** Twice (workers-per-container, ASGI-vs-WSGI) he produced the correct answer and then restated it instead of justifying it. This is exactly the failure mode the interview probes with "why?" — grade the *second* sentence, not the first.
- **Vocabulary gap, not a knowledge gap.** He self-described the work as "vibe coded — I know what I want, the plumbing may as well be foreign." That's accurate about the plumbing and *understated* about the judgment: he had the Celery-off-the-request-path answer available and didn't recognize it as a Section 1 answer. Pattern for the rest of the sprint: **before teaching a unit from zero, check whether he has already operated it and just lacks the words.**
- Asks precisely and pushes past the analogy to the mechanism. Let him — the questions have been higher-yield than the checks.

**Watch** *(added 2026-08-18 evening, `/drill`)*
- **Reads code for syntax when the question is about policy.** Handed a 5-line snippet with both guardrails on the wrong side — and told the topic was *guardrail placement* — he answered with two (incorrect) async-mechanics observations: "we're not in an `async with`" and "the return doesn't have an `await`." Neither is a defect. **The recognition mode fired on a question that wanted reasoning**, roughly 60 seconds after a clean mechanism win on sockets. Same boundary the 08-18 coaching session named; this is the first instance caught *in the act*.
  - Contributing factor worth separating out: **interference from the prior drill item.** Item ① was pure async/socket mechanics. Item ② arrived and he answered it in the previous item's vocabulary. That is a known cost of interleaving and not, by itself, a knowledge gap — but the fact that the *topic label* didn't override it is the finding.
- **He said "explain that simpler, I might be missing something" instead of bluffing.** Worth logging on the positive side: the 08-11 failure mode was four misconceptions banked behind *confident* answers. Asking for the simpler version is the calibration working.
- **He closed the session on "my brain is a little fried."** Correct call, correctly timed — evening, non-peak, after a full peak-window `/learn` earlier the same day. Stopping on an honest signal is the behavior the floor rule exists to protect.

**Watch** *(updated 2026-08-18 — the 08-11 pattern escalated to a named call)*
- **"States the rule, not the reason" is now at four occurrences and it is the section's headline finding.** 08-11: workers-per-container, ASGI-vs-WSGI. 08-18: what ECS *sees* (Step 1.5 ④) and the idle-CPU differential (check ②). **The call, delivered and accepted: recall is genuinely good; justification is the actual gap.** Not knowledge, not aptitude — he retrieves the correct fact and, asked *why*, paraphrases the fact louder. That is exactly what fails at the **second** question in any technical conversation: the first checks whether you read it, the second checks whether you understand it.
  - **Mechanical fix, in force from 2026-08-18:** when asked "why," **the first sentence may not contain the thing being explained.** If the answer to *"why is the loop the problem?"* opens with *"because the loop…"*, scrap it and restart from what someone **observes**. Grade the restart, not the reflex.
- **He argues himself out of correct first instincts.** Pretest A: wrote ~100s, then appended *"but because it's an async, all 50 should be done in about 2 seconds right?"* The first answer was right and the override was the textbook misconception. Pattern to test deliberately — ask for a first answer, then ask him to defend it *before* offering a revision.
- **Arithmetic slips under conceptual load.** `200/40 = 50`. The concept was fully owned; the division wasn't. Not a math gap — a bandwidth symptom. Worth watching whether it recurs specifically on the checks that come *after* a hard reframe.
- **The "already operated it" check came back NO for the first time, and the reason is the finding.** *"Everything is done in prod."* This trap is **invisible at concurrency 1**, which is how he develops and smoke-tests. Whole categories of production behavior are unavailable to him not through inexperience but because **he has no local concurrency harness.** That's a fixable tooling gap with outsized returns — hence the build.

---

## Section 2 — REST + OpenAPI as a maintained contract
**Chunks:** 2.A semantics → 2.B the contract
**Project:** Issue 1 (shared with §1) · **Budget:** ~85 min

### 2.A — Semantics
- [ ] **2.1 Verbs, and the 401 / 403 / 422 distinction** `[A] ~30m` — 401 = I don't know who you are · 403 = I know, and you can't · 422 = I understood, the body is invalid. Plus 200 vs 201 vs 204. *Getting this wrong is a visible tell, and §4 depends on it: a valid token missing a scope is **403**, not 401.* **Breaks if wrong:** clients build retry logic against the wrong signal and hammer you on an error that will never resolve.
- [ ] **2.2 Statelessness, idempotency, and safe retries** `[B] ~15m` — which verbs are idempotent, idempotency keys, why it matters behind a load balancer that retries.
- [ ] **2.3 Pagination** `[C] ~5m` — cursor vs offset, and when offset breaks.

### 2.B — The contract
- [ ] **2.4 Versioning and breaking changes** `[B] ~15m` — URL vs header versioning; what actually constitutes a breaking change to a consumer.
- [ ] **2.5 FastAPI's generated OpenAPI + `securitySchemes`** `[B] ~15m` — how the spec is produced, declaring OAuth2/bearer security in it, `/docs` vs `/redoc`, locking it down in prod.
- [ ] **2.6 Contract-first vs code-first** `[C] ~5m` — when a consuming team forces contract-first; exporting the spec as a CI artifact and diffing it. *This is the "maintenance" answer.*

---

## Section 3 — OAuth2, OIDC, and integrating with Okta
**Chunks:** 3.A the roles → 3.B the flows → 3.C OIDC vs OAuth2 → 3.D Okta concretely
**Project:** Issue 2 · **Budget:** ~170 min teaching + ~45 build *(3.7–3.8 spill to evening if needed)*

### 3.A — The roles
- [ ] **3.1 The four roles, and which one you are** `[A] ~30m` — resource owner / client / authorization server / **resource server**. Your API validates; it never issues. *Internalize this framing before anything else in the section — the JD's Okta bullet is entirely about it.* **Breaks if wrong:** you design token issuance into a service that should only verify, and the whole architecture answer collapses.

### 3.B — The flows
- [ ] **3.2 The grant-type map, and what OAuth 2.1 removed** `[A] ~30m` — implicit and ROPC gone, PKCE now required for confidential clients too, exact-match redirect URIs. Each removal traces to a specific attack — know which. ⚠ *still a draft; say so precisely* **Breaks if wrong:** recommending implicit flow in 2026 dates you a decade.
- [ ] **3.3 Client credentials, for service-to-service** `[A] ~30m` — no user context, no OpenID scopes, custom scopes required, client authentication methods. *This is the flow the JD's service-to-service bullet implies, and the one Issue 2 uses.* **Breaks if wrong:** you try to request `openid` in a machine flow and spend an hour on a confusing error.
- [ ] **3.4 Authorization code + PKCE** `[B] ~15m` — the code-interception attack PKCE closes, and why confidential clients need it now too.

### 3.C — OIDC vs OAuth2
- [ ] **3.5 OIDC vs OAuth2 = authentication vs authorization** `[A] ~30m` — ID token vs access token, why you **never** authorize off an ID token, the `/.well-known/openid-configuration` discovery document. *The decision tree `CAREER_LOG.md` currently records as missing.* **Breaks if wrong:** you accept an ID token as an API credential — a real and common vulnerability, not a theoretical one.

### 3.D — Okta concretely
- [ ] **3.6 Okta's model** `[B] ~15m` — custom authorization server vs the org default, issuer, audience, custom scopes and claims, the JWKS endpoint, validating **both `aud` and `cid`**.
- [ ] **3.7 Scopes vs roles vs claims** `[B] ~15m` — coarse API permission vs application RBAC, and where each is enforced.
- [ ] **3.8 SAML** `[C] ~5m` — what it is, why enterprises still have it, why it isn't in your path.

---

## Section 4 — JWT validation done correctly
**Chunks:** 4.A anatomy & signing → 4.B the checklist → 4.C JWKS & rotation → 4.D the attacks
**Project:** Issues 3 + 4 · **Budget:** ~140 min teaching + ~90 build
*The highest-density section in the sprint. If a day gets sacrificed, it is never this one.*

### 4.A — Anatomy & signing
- [ ] **4.1 Header, payload, signature** `[A] ~30m` — base64url is **encoding, not encryption**; anyone can read a JWT; therefore **never put PHI in one**. Claim vocabulary: `iss` `sub` `aud` `exp` `nbf` `iat` `jti` `scp` `cid` `kid`. **Breaks if wrong:** you store something sensitive in a token and hand it to the client.
- [ ] **4.2 RS256 vs HS256** `[B] ~15m` — symmetric vs asymmetric; with an external IdP you hold no secret, Okta signs, you verify with a public key.

### 4.B — The checklist
- [ ] **4.3 The six-item validation checklist, memorized** `[A] ~30m` — signature · `iss` · `aud` · `exp` · `nbf`/`iat` · **algorithm allow-list**, plus Okta's `cid`. *Recite six items without hesitating; this is the most likely single question in the interview.* **Breaks if wrong:** skip `aud` and you accept a token minted for a completely different service — a full auth bypass.

### 4.C — JWKS & rotation
- [ ] **4.4 JWKS: fetch, `kid` selection, caching, rotation** `[A] ~30m` — cache until an unknown `kid` appears; the failure mode of fetching per-request (latency + a DoS on your IdP) *and* of caching forever (rotation breaks you at 3am). **Breaks if wrong:** the IdP rotates keys and every request 401s until someone redeploys.

### 4.D — The attacks
- [ ] **4.5 `alg: none` and RS256→HS256 confusion** `[A] ~30m` — the two classic JWT attacks. Confusion: sign with the *public* key as an HMAC secret, and a naive verifier accepts it. The fix in both cases is one line: pin the algorithm. *Naming these unprompted is a strong senior signal.* **Breaks if wrong:** anyone who can read your public key can mint valid tokens.
- [ ] **4.6 Revocation — the honest hard problem** `[C] ~5m` — bearer tokens are valid until expiry; short TTL + refresh rotation vs introspection vs denylist, each with a real cost.

---

## Section 5 — mTLS for service-to-service
**Chunks:** 5.A TLS → mutual → 5.B cert as identity → 5.C mTLS vs JWT → 5.D termination & rotation
**Project:** Issue 5 · **Budget:** ~95 min teaching + ~60 build
*Re-barred `[A]`→`[B]` on 2026-08-13: 5.2 and 5.3 were `[A]` because one JD named mTLS as a hard requirement. Absent that, this is decision-level. **5.3 is the exception — it stays `[A]`**, because "mTLS vs JWT" is a genuine architecture decision you'll make on your own systems, not a posting artifact.*

### 5.A — TLS → mutual
- [ ] **5.1 The handshake, then what "mutual" adds** `[B] ~15m` — server proves identity to client; mTLS makes the client prove identity back.

### 5.B — Cert as identity
- [ ] **5.2 The client certificate as an identity** `[B] ~15m` — extracting subject/SAN, mapping it to a service principal, why this authenticates the **workload** rather than a user.

### 5.C — mTLS vs JWT
- [ ] **5.3 mTLS vs JWT vs both** `[A] ~30m` — mTLS authenticates the channel and calling workload; the JWT carries the caller's authorization context. **Both, layered, is the zero-trust answer.** *If only one thing survives from §5, make it this — these get presented as alternatives constantly, and they aren't.* **Breaks if wrong:** you build a mesh with mTLS and skip tokens, and you have authentication with no authorization — every service can call every endpoint.

### 5.D — Termination & rotation
- [ ] **5.4 Trust chains and CA hierarchy** `[B] ~15m` — root vs intermediate, why you never sign leaf certs with the root.
- [ ] **5.5 ALB termination: passthrough vs verify** `[B] ~15m` — the `X-Amzn-Mtls-Clientcert` header family vs a trust store with a CA bundle. ⚠ *two distinct modes, don't blur them*
- [ ] **5.6 Rotation and expiry — the #1 production failure mode** `[B] ~15m` — automate or get paged. Ties to why Private CA has a 7-day short-lived tier. *Saying this out loud reads as operational experience.*
- [ ] **5.7 CRL vs OCSP** `[C] ~5m` — why revocation is genuinely hard in PKI too.

---

## Section 6 — The AWS API & security stack as one request path
**Chunks:** 6.A the path → 6.B compute → 6.C edge & identity → 6.D observability
**Project:** Issue 7 *(load-bearing)* · **Budget:** ~185 min, split Thu + Fri

### 6.A — The path
- [ ] **6.1 The request path, end to end** `[A] ~30m` — Route 53 → ACM → WAF → ALB → ECS Fargate → CloudWatch. *Learn the section as this one diagram; every other unit hangs off it, and it's what the standing set-piece drill asks you to draw cold.* **Breaks if wrong:** you can't reason about where anything belongs — which layer terminates TLS, which one you'd alarm on, where a change at 100× actually lands.

### 6.B — Compute
- [ ] **6.2 ECS Fargate** `[B] ~15m` — task definition vs service vs task; ECR; health checks; rolling deploys.
- [ ] **6.3 Task role vs execution role** `[A] ~30m` — **execution role** = what ECS needs (pull the image, write logs, inject secrets); **task role** = what your application code can call. *A classic interview question with a crisp answer.* **Breaks if wrong:** you grant the app the execution role's permissions and blow least-privilege wide open.

### 6.C — Edge & identity
- [ ] **6.4 ALB** `[B] ~15m` — listeners, rules, target groups, health checks, TLS termination; plus ⚠ native JWT verification (2025-11).
- [ ] **6.5 Route 53 + ACM** `[B] ~15m` — alias vs CNAME, health checks; DNS-validated public certs, auto-renewal, why ACM public certs are free and non-exportable.
- [ ] **6.6 API Gateway vs ALB — when each** `[B] ~15m` — HTTP API vs REST API, JWT authorizers, usage plans, request validation, VPC Link; the honest cost/latency tradeoff.
- [ ] **6.7 Where to validate the token: edge vs app** `[B] ~15m` — ALB/API Gateway authorizers vs an in-app dependency. Defense in depth says both; know why each alone is insufficient. ⚠ *very recent — verify live*
- [ ] **6.8 WAF and Shield** `[B] ~15m` — managed rule groups, rate-based rules, what a web ACL attaches to, **count mode before block mode**; Shield Standard (free, on) vs Advanced (~$3k/mo — know the number, never enable it).
- [ ] **6.9 IAM: roles over keys** `[B] ~15m` — the assume-role model, least privilege, why no static access key should exist in this architecture.

### 6.D — Observability
- [ ] **6.10 CloudWatch** `[B] ~15m` — structured JSON logs, log groups and retention, metric filters, alarms, correlation IDs. What you actually alert on for an API: 5xx rate, p99 latency, and **a 401 spike as an attack signal**.
- [ ] **6.11 S3 + KMS for an API** `[C] ~5m` — Block Public Access, bucket policy vs IAM, SSE-KMS, presigned URLs and expiry as an access-control decision.

---

## Section 7 — API testing & validation
**Chunks:** 7.A the harness → 7.B the matrix
**Project:** Issue 4 (shared with §4) · **Budget:** ~85 min

- [ ] **7.1 `TestClient` vs `httpx.ASGITransport`** `[C] ~5m` — sync vs the current async pattern.
- [ ] **7.2 `dependency_overrides` to swap auth** `[B] ~15m` — the practical payoff of §1.3.
- [ ] **7.3 Minting test tokens against a fake JWKS** `[A] ~30m` — a local RSA keypair so the auth path is tested **for real** rather than mocked away. **Breaks if wrong:** you mock the validator, and the one function that matters most ships with zero real coverage.
- [ ] **7.4 The negative matrix** `[A] ~30m` — expired · wrong `aud` · wrong `iss` · bad signature · `alg: none` · missing scope (403) · missing/malformed header (401). *Seven cases; the JD asks for exactly this.* **Breaks if wrong:** you can only prove the happy path, which proves nothing about security.
- [ ] **7.5 Contract testing from the spec** `[C] ~5m` — schemathesis against the generated OpenAPI; Postman/newman in CI.

---

## Section 8 — HIPAA & PHI for an API engineer `[B]/[C] only`
**Project:** Issue 6 · **Budget:** ~65 min
*Context, not craft — capped at `[B]`/`[C]` by design. Study it genuinely; claim it accurately. **Never overclaim HIPAA experience** — a caught overclaim on a compliance topic is worse than an honest gap, every time.*

- [ ] **8.1 The three rules** `[C] ~5m` — Privacy, Security, Breach Notification; covered entity vs business associate, and which one a vendor engineer is.
- [ ] **8.2 The Security Rule's technical safeguards, mapped to API surfaces** `[B] ~15m` — access control → authn/authz · **audit controls** → who accessed what, when · integrity → tamper evidence · transmission security → TLS everywhere.
- [ ] **8.3 Audit logging without logging PHI** `[B] ~15m` — log the actor, action, resource **reference**, timestamp, outcome. Never the payload. Redaction and structured-log discipline. *Directly implemented in Issue 6.*
- [ ] **8.4 Minimum necessary → `response_model`** `[B] ~15m` — compliance enforced at the serialization layer rather than in a policy document. *The §1.6 connection, from the other direction.*
- [ ] **8.5 Encryption in transit and at rest** `[C] ~5m` — TLS 1.2+, KMS, rotation; "addressable vs required" in the Security Rule.
- [ ] **8.6 BAA + AWS shared responsibility** `[C] ~5m` — what AWS covers vs what stays yours; HIPAA-eligible services.
- [ ] **8.7 De-identification** `[C] ~5m` — Safe Harbor's 18 identifiers vs expert determination.

---

## Section 9 — CI/CD for API and UI `[B]/[C] only`
**Project:** Issue 8 *(the designated cut if the week compresses)* · **Budget:** ~40 min

- [ ] **9.1 The pipeline you can sketch on a whiteboard** `[B] ~15m` — checkout → lint → test → security scan → build image → push ECR → deploy ECS.
- [ ] **9.2 GitHub Actions OIDC federation to an IAM role** `[B] ~15m` — no long-lived AWS keys in CI, ever. *If asked how CI authenticates to AWS and you answer "access keys in secrets," that's a miss.*
- [ ] **9.3 Deploy strategies** `[C] ~5m` — rolling vs blue/green via CodeDeploy, health-check gating, rollback.
- [ ] **9.4 Migrations and secrets in a deploy** `[C] ~5m` — where schema changes run; Secrets Manager / Parameter Store vs env vars.

---

## 🎨 The standing set-piece — a `/drill` exercise, not a section

*Was §10. Demoted 2026-08-13: it isn't material to learn, it's a **rehearsal of everything else**, so it belongs in the retention loop rather than the acquisition roadmap. Once §6 is banked, this becomes a recurring `/drill` item — pull it every few weeks, cold, timed.*

> **"Design a secure, HIPAA-compliant API on AWS that authenticates against Okta."**
> Drawn cold in under 4 minutes and narrated: the request path, where the token is validated (and why possibly twice), where mTLS sits, what's logged and what isn't, what's encrypted, what you'd alarm on, what changes at 100×.

**The three follow-ups, pre-built:** *"What happens when Okta is down?"* · *"How do you revoke access immediately?"* · *"Where could PHI leak in this design?"* A strong diagram undone by the first probe past it is the actual failure mode — the follow-ups are the exercise, not a bonus round.

*(Deleted 2026-08-13: §11, "Honest positioning & the story bank." It was interview drafting — a have/haven't script, STAR stories, questions to ask them. Nothing to learn, and it was tied to one posting. If an interview appears, rebuild it then from `CAREER_LOG.md`, which is where the raw material lives anyway.)*

---

## 💸 Cost & safety guardrails — non-negotiable

*The clock is gone, so there is no reason to rush a deploy or eat cost. Everything here still stands — these are guardrails against an expensive mistake, not against a deadline.*

- **Never create an AWS Private CA.** ~$400/mo general-purpose (~$50/mo short-lived), prorated from creation, no refund on delete. §5 uses a **local openssl CA**; PCA's behavior and pricing are learned from docs.
- **Never enable Shield Advanced.** ~$3,000/month, 1-year commitment. Shield Standard is free and already on.
- **Stand up and tear down inside one sitting.** ALB ~$0.55/day · Fargate 0.25 vCPU ~$0.30/day · WAF $5/web ACL/mo + $1/rule/mo · Route 53 zone $0.50/mo · ACM public certs free. Issue 7 is the only unit that costs anything; **target under $20 for the whole track.**
- Route 53 + a public ACM cert require **a domain you control** — confirm before starting Issue 7.
- **Set a $25 AWS Budget alert before the first `terraform apply`.** Tag everything `project=secure-api-lab`. Run `docs/TEARDOWN.md` the same day you deploy.

---

## Connections & Application

- **§1.6 ↔ §8.4 — `response_model` is a compliance control.** The same line of code answers a FastAPI question and a HIPAA question. Say the connection out loud; it distinguishes someone who studied a list from someone who understands a system.
- **§4 ↔ §6.7 — "where do you validate the JWT?" stopped being settled in November 2025.** Edge validation cuts latency and blocks bad traffic before it costs compute; in-app validation survives an ALB misconfiguration and knows business context. Defense in depth = both.
- **§5.3 ↔ §3 — mTLS and OAuth2 are not alternatives.** mTLS authenticates the *workload*; the JWT authorizes the *call*. A mesh doing mTLS still needs tokens.
- **§2.1 ↔ §4.3 — status codes are an auth design decision.** A valid token missing a scope is 403, not 401. Getting it right requires having thought about both sections at once.

## Honest Takeaways

- **2026-08-10 — the real constraint is hours, not aptitude.** From scratch, the material priced out at ~28 hours against ~21 available. Naming the depth bar per unit is what made that survivable; without it the peak window goes to whatever is next in the file rather than what actually matters. The `[C]` bar is the honest part — some things are worth exactly five minutes.
- **2026-08-13 — the format outlived the deadline, and that's the finding.** The role closed on years-of-experience before an interview happened. What the seven days actually produced wasn't interview readiness — it was the depth bars, the chunk loop, the three check formats, and the Learning notes block, all of which are now evergreen across every track. **The uncomfortable half:** those inventions came out of a week with a real external date on it, and the date is gone. Nothing here replaces it yet. Worth deciding what does — a cert exam, a demo to John, a public repo milestone — because the record is clear that this system runs hot against a deadline and cold without one.

## Entry Log

*(Links added by `/learn` at each session's persist step.)*

- [2026-08-11](reflection_log/2026-08-11.md) — §1 chunk 1.A (partial): **1.1 ASGI vs WSGI `[x]`**. Schedule call: §1 run today instead of §2, since §1's three `[A]`s underpin §3–§4. Live-verified the current worker guidance (gunicorn recipe is gone from the docs; one uvicorn process per container on ECS). Six foundational questions answered off-script — sockets, `epoll`, stack vs heap, `await` vs `gather`. Four misconceptions corrected. Notes-page convention added. **Stopped at 1.2.**
- [2026-08-18](reflection_log/2026-08-18.md) — §1 chunk **1.2a**: **1.2 `async def` vs `def` `[~]`** (1.2b pending). First rep after a 6-day gap. Delayed re-ask scored 1 clean / 2 partial / 1 miss; `await`-vs-`gather` cleared, sockets missed a second time. **Pretest 0 for 3** — predicted `async def` would be *faster* than `def` on a blocking call; it's **25× slower** (~100s vs ~4s). Taught the **three-way routing rule** and the shared 40-token anyio limiter, with the §1.3/§4 tie-in (a sync JWKS fetch in the auth dependency silently caps the whole API at 40). Live-confirmed the FastAPI async page still carries **neither** the blocking-in-`async-def` warning **nor** the threadpool size. **The read: "states the rule, not the reason" hit four occurrences and was escalated to a named call.** **Stopped at 1.2b.**
