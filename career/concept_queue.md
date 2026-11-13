# Concept Queue — the Sharpen backlog

The prioritized list of concepts to grill with `/sharpen`. Seeded from Reese's own shipped code (the richest curriculum — defend what you already built) and the genuine gaps on the AI Engineering Master Guide path.

> **⚠️ Phase 3 (2026-08-27) — the source changed.** The four curricula are **paused** (4 banked of 233). This queue is now seeded by **real work**: 💼 Craft reps on the Cognizant project and 🛠 Business reps on Ian's client work. The selection rule is unchanged and still the best one in the system — **pick the slice you feel you *should* already be able to explain and quietly can't.** That flinch is the targeting system.
>
> `/sharpen` is also now the highest-value command in the Depth lane: the one time learning visibly converted to career movement (07-28 → 07-29) it was a **defense** rep under real stakes, against a lifetime ratio of 17 learn : 2 sharpen : 2 drill.

**Where this sits in the pipeline:** real work (Craft / Business) → a capture → **`/sharpen` (this queue — defend cold)** → `/drill` (retain). `/learn new <topic>` feeds in when a capture needs real teaching. A unit learned via `/learn` lands here to be defended. Concepts from his own shipped code start here directly (already built, just need defending). Two ledgers: this file tracks *acquisition/defense*; `CAREER_LOG.md` tracks *mastery + review cadence*.

**Depth bars** (see `.claude/commands/sharpen.md`), which replaced Tier 1/Tier 2 on 2026-08-13:
- **`[A]` BUILD IT** → mechanism + why-this-over-that + failure mode, cold and unaided. **95% is a miss.**
- **`[B]` EXPLAIN IT** → the decision only. "When I'd reach for it and the one-line why" is a complete pass; don't grade internals.
- **`[C]` NAME IT** → **deliberately not in this queue.** Defending "what Shield Standard is" cold is ceremony.

*Legacy notation: the section headings below still read **Tier 1** / **Tier 2**. Map **T1 ≈ `[A]`/`[B]`**, **T2 ≈ `[C]`/`[B]`**, and re-bar a row when you touch it — no bulk rewrite.*

`[ ]` = not yet owned · `[~]` = needs another rep · `[x]` = owned (date) — moves to `/drill` rotation.

Work top-down. Higher bars before lower unless a real project need jumps the line.

---

## 🎯 The AI Engineer list — top of the queue (seeded 2026-11-13)

*Twenty-two units in four passes. Seeded from three things: AI features shipped for a client (the code exists; the defense doesn't), an AI Engineer interview where two questions about how models are trained and measured went unanswered, and a check against what 2026 AI Engineer postings ask for. Ordered by one test: **does this rep pay off both in the client work and in an outside interview?***

**How a unit runs — the existing rules, nothing new:**
- **One unit, named before you sit down.** Re-ask last time's Tripped items cold → guess before being taught → 8-minute chunks with 2–4 checks each → a 5-minute build → write the Tripped list → one "Stopped at / Next step" line. `[A]` ≈ 30 min · `[B]` ≈ 15 min.
- **A session may only mark `[~]`.** `[x]` needs a clean cold re-ask in a *later* session, or running code. Every `[A]` needs a `Breaks if wrong:` line **you** wrote.
- **The "this over that" on each row is a question, not an answer.** Answer it cold first; the anchors and the grading key live in a private companion file kept with the client work (not in this repo — this repo is public).
- **Passes are an order, not walls.** A live work need jumps the line, the flinch rule still picks within a pass, and `/drill` mixes across passes. Worst day: recall one unit's "this over that" out loud, three minutes. That's a rep.

**Lookup key:** `§N` = that section of the paused catalog at `readings/ai-engineering-curriculum/summary.md` (a shelf, not a backlog). `§13` is new there as of today — the topics the catalog never had.

### Pass 1 — Defend what you shipped *(run with `/sharpen`; the code already exists)*

- [ ] `[A]` **1 · The model reads, code decides** — the model turns words into structured details; code checks them, decides what's missing and builds the answer; a person confirms. **This over that:** a reader with no tools vs an agent that acts on its own. *(lookup: §11, §3 · asked for: agents, human approval)*
- [ ] `[A]` **2 · Structured output, checked twice** — a schema constrains the shape; code still checks ranges and whether the thing named exists. **This over that:** schema-enforced output vs "ask for JSON and parse it"; reject the whole output vs filter out the bad part. *(lookup: §2)*
- [ ] `[A]` **3 · User text is data** — the prompt-injection posture: delimit it, sanitize it, send less, check the result in code, and test with hostile input. **This over that:** code-side checks vs instructing the model to behave. *(lookup: §9 · asked for: guardrails)*
- [ ] `[B]` **4 · The model has no memory** — the whole conversation is re-sent every turn; state lives in code and merges without letting a blank erase a known value. **This over that:** state kept in code vs state kept on the model's side. *(lookup: §1 — also clears the fuzzy token face on "What an LLM call actually is")*
- [ ] `[A]` **5 · Confirmation bound to what the person saw** — the confirm button carries the identity of the exact proposal on screen. **This over that:** "confirm this card" vs "confirm the latest". *(lookup: §4 human-in-the-loop)*
- [ ] `[B]` **6 · When the model call fails** — timeout, retry, refusal, cut-off output, a non-AI fallback; and where the slow call sits relative to the database transaction. **This over that:** call outside the transaction with an edit counter vs holding the lock while the model thinks. *(lookup: §10)*
- [ ] `[B]` **7 · Send the model as little as possible** — what goes into the prompt, what is deliberately left out, and where that data physically goes. **This over that:** let the model point at a record by number vs copy the record's values into the prompt. *(lookup: §9, Tier 2 privacy)*

### Pass 2 — Measure it *(the biggest gap in the shipped code, and the skill postings ask for most)*

- [ ] `[A]` **8 · Precision, recall, F-beta, the PR curve, the threshold** — **Build:** hand-label the correct answers for one partner in the field-matching scorer; compute precision and recall per confidence band; pick the review threshold off the curve. **This over that:** move the threshold vs change the scorer; which error costs more here, a wrong match accepted or a right one sent to review? *(lookup: §13 · the first interview question)*
- [ ] `[B]` **9 · Calibration** — does a 0.95 mean right 95% of the time? **Build:** a reliability table from the same answer key. **This over that:** a score you can read as a probability vs a score that only ranks. *(lookup: §13)*
- [ ] `[A]` **10 · A golden set and an eval harness for an LLM feature** — **Build:** 30 real phrasings run against the real model, with threshold assertions in the test runner. **This over that:** tests with a scripted fake model vs evals against the real one — what each can and cannot prove. *(lookup: §8 · asked for: evaluation, 56% of postings in one count)*
- [ ] `[B]` **11 · LLM-as-judge** — when to trust a model grading a model. **Build:** grade one slice of unit 10 three ways (code check, judge model, you) and compare. **This over that:** judge model vs exact checks vs human labels. *(lookup: §8)*
- [ ] `[B]` **12 · Tracing and cost per call** — **Build:** log tokens, latency, model and outcome for every call in one feature. **This over that:** a row in your own table vs a tracing product. *(lookup: §8 · asked for: observability)*
- [ ] `[B]` **13 · Evaluate before a model swap** — a large model at low effort vs a small model for the same extraction job, decided by unit 10's numbers and unit 12's costs. **This over that:** swap on a hunch vs swap on an eval; which metric must not get worse? *(lookup: §8, §11)*

### Pass 3 — How models learn *(the interview; one small public project — a query-complexity router)*

- [ ] `[A]` **14 · Train a classifier end to end** — loss function, gradient descent, train / validation / test, overfitting. **Build:** router v0 — embeddings plus a linear head that labels a query simple / medium / hard. **This over that:** the loss the model is trained on vs the metric you judge it by (the exact blur from the interview). *(lookup: §13)*
- [ ] `[A]` **15 · Class imbalance** — stratified splits, class weights, focal loss, resampling; judged per class, never on accuracy. **Build:** shrink one class to 3%, watch it vanish, then fix it three ways and compare per-class recall. **This over that:** reweight the loss vs resample the data vs move the threshold. *(lookup: §13 · the second interview question)*
- [ ] `[B]` **16 · What an embedding is** — text as a vector, cosine similarity, why similar text lands close. **Build:** inspect nearest neighbours in the router's data and find one that surprises you. **This over that:** embeddings plus a small head vs fine-tuning a whole model vs asking an LLM to classify. *(lookup: §5)*
- [ ] `[B]` **17 · Model routing** — by task type, cost and latency; measured figures vs advertised ones; what to do before there is any data. **Build:** route with the router and report cost saved against quality lost. **This over that:** route on measured results vs route on the model card. *(lookup: §13, §11 · asked for: multi-model use, routing by task type)*
- [ ] `[B]` **18 · Prompt vs retrieval vs fine-tuning, and what LoRA changes** — **Build:** a one-page decision note for the router: which lever, and why not the other two. **This over that:** teach the model a behaviour vs hand it the facts. *(lookup: §13, §11 · asked for: fine-tuning)*

### Pass 4 — Breadth *(pulled when the work needs it)*

- [ ] `[B]` **19 · Retrieval: when exact match beats embeddings** — the RAG pipeline, chunking and hybrid search at decision level. **This over that:** an exact-match query vs nearest-neighbour similarity. *(lookup: §5 · asked for: RAG, vector databases)*
- [ ] `[B]` **20 · Tool calling and MCP** — what to expose to outside agents and what to keep behind a screen. **This over that:** an MCP tool vs a web-only operation. *(lookup: §3, §6 — shipped before, never defended)*
- [ ] `[B]` **21 · Open-weight and small models, quantization** — what you trade away, and when local beats hosted. **This over that:** a hosted frontier model vs a small model you run yourself. *(lookup: §12, §13)*
- [ ] `[B]` **22 · LLM system design, out loud** — design one system end to end with token cost, latency, the human fallback and the guardrails made explicit. **This over that:** the simplest thing that works vs the architecture that sounds senior. *(lookup: §10, §11)*

### Coverage — what postings ask for, and where it sits

*Checked 2026-11-13 against six sources (keys below). Most of them sell courses or tools and their percentages disagree, so read the numbers as direction, not measurement.*

| Skill area | Evidence | Where it sits |
|---|---|---|
| Python | 71% [D] [E] | Owned (`CAREER_LOG.md`: can teach it) |
| LLM APIs | 66% [D] | Units 2, 4 · §1 (one `[x]`, two `[~]`) |
| Evaluation of LLM systems | 56% [K] · 52% run offline evals [L] | Units 8–11, 13 |
| Agents | 50% [K] | Units 1, 5, 20 · §3, §4, §7 |
| Retrieval (RAG) | 13.6–40% [E] [K] [D] | Unit 19 · §5 |
| Classical machine learning | 38% [D] | Units 8, 9, 14, 15 · §13 |
| Cloud (AWS first) | 37% [D] | **Deferred on purpose** · Tier 2 catalog, the paused secure-API track |
| Deep learning frameworks (PyTorch) | 23–38% [D] [E] | Used inside units 14–15; framework depth **deferred** |
| Observability and tracing | 19% [D] · 89% in use [L] | Unit 12 |
| Vector databases and embeddings | 12–18% [D] | Units 16, 19 |
| SQL and data pipelines | 17–19% [D] [E] | **Deferred** · used daily in client work |
| Docker, Kubernetes, CI/CD | 16–24% [D] [E] | **Deferred** · Tier 2 catalog |
| Fine-tuning | 14.8% [E] · 57% of teams don't [L] | Unit 18 |
| TypeScript | 13% [D] | Practised in the client work; no unit |
| Prompt and context engineering | 7–9% [K] [E] | Owned / partial · §1 |
| Model routing and cost control | 44% route by task type [A] | Units 13, 17 |
| Guardrails and security | human approval is the top guardrail [A] | Units 3, 5, 7 · §9 |
| Open-weight models, quantization | about half use open weights [A]; asked in interviews [X] | Unit 21 |
| LLM system design | interview round [X] | Unit 22 |
| Frameworks (LangChain, LangGraph) | 25% [D] | **Deferred** · §2, §4 (LangGraph-vs-ReAct already `[x]`) |
| Inference serving (batching, GPUs) | interview round [X] | **Deferred** · named in §13 |

`[K]` kdnuggets.com/the-ai-skills-that-actually-show-up-in-job-postings-right-now · `[D]` dev.to/gnana_6392e836fd500a957dc/ai-engineer-skills-companies-want-in-2026-3449-posting-analysis-5f9l · `[E]` 365datascience.com/career-advice/career-guides/ai-engineer-job-outlook-2025/ · `[A]` amplifypartners.com/blog-posts/the-2026-ai-engineering-report · `[L]` langchain.com/state-of-agent-engineering · `[X]` aced.io/blog/ai-engineer-interview-questions

**One limit, written down:** none of these sources shows interviewers asking classification-metric questions. The evidence for Pass 3 is the interview itself, the 38% figure and one posting asking for LoRA. That is why it is third and not first.

---

## Tier 1 — Foundational / agentic core (100% / teach-it)

### Agents & orchestration
- [x] **LangGraph vs plain ReAct agent** — why the graph over an `AgentExecutor` loop *(2026-06-22 — landed: graph guarantees execution regardless of the model's decision; control surface over an uncontrollable loop; reach for it on need for control/state/durability, not agent count)*
- [ ] **Supervisor vs swarm vs single ReAct agent** — when each multi-agent topology, and why *(source: Cognizant code-gen/test/review team, autoclip)*
- [ ] **ReAct loop mechanics** — think→act→observe, the scratchpad, and its failure modes (skips steps, declares done early) *(source: all agent work)*
- [ ] **LangGraph shared state** — `StateGraph` / `TypedDict`, how state flows node→node, conditional vs deterministic edges *(source: Cognizant)*
- [ ] **Checkpointers / persistence / HITL** — durable execution, resume-after-interrupt, human-in-the-loop pause *(source: path gap; partially touched)*

### RAG & retrieval
- [ ] **What an embedding actually is** — vector space, dimensionality, similarity *(source: autoclip, CFO Agent)*
- [ ] **Embedding model choice** — why Voyage AI over OpenAI embeddings in autoclip *(source: autoclip)*
- [ ] **Chunking strategy** — size/overlap tradeoffs, why it makes or breaks retrieval *(source: RAG pipelines)*
- [ ] **pgvector vs dedicated vector DB** (Pinecone/Weaviate) — when each, why pgvector for his builds *(source: autoclip, CFO Agent)*
- [ ] **Retrieval patterns** — pure similarity vs hybrid/keyword, re-ranking *(source: Cognizant RAG)*

### LLM fundamentals
- [~] **What an LLM call actually is** — stateless re-send model, tokens, context window (hard-reject vs lost-in-middle), cost asymmetry (output ~5× input & why) *(2026-07-22 — /sharpen: 3 of 4 faces owned cold: statelessness ✓, hard-reject vs lost-in-the-middle ✓, cost asymmetry mechanism ✓ (parallel prefill vs serial autoregressive generation). Fuzzy: tokens — ratio inverted (token ≈ ¾ word, word ≈ 1.33 tokens), tokens are learned subword vocab not fixed-size, why-tokens = atomic unit of compute. One more rep on the token face.)*
- [x] **Anatomy of a prompt** — system as top-level param (not messages[0]) & why (render order tools→system→messages = cacheable byte-prefix); assistant turns = re-sent prior outputs = "memory"; max_tokens = 200 + stop_reason (never raises) vs context window = 400 BadRequestError (raises); ⚠ assistant-prefill removed on Claude 4.6+ (400) → Structured Outputs (output_config.format) enforce vs prefill nudge *(2026-07-22 — defended cold, first /sharpen defense. All four faces produced under push. Taught in-session → drill: silent cache invalidators (dynamic bytes in prefix — timestamps/UUIDs/unsorted JSON/varying tools; verify via usage.cache_read_input_tokens). In /drill rotation.)*

### Tools, MCP, prompting
- [ ] **The steering ladder (zero-shot → few-shot → structured outputs) + role prompting** — escalate only when the job demands it: clear instructions default, examples (3–5, tagged, DIVERSE) for fuzzy steering, schema for guaranteed shape (shape ≠ quality); role = system-param prior-shift (tone + scope/judgment, not knowledge, cacheable prefix); ⚠ aggressive "you MUST" prompting now overtriggers on 4.5/4.6+ *(learned 2026-07-20 via /learn §1.3; build pending — triage-call worksheet. Defend cold once built.)*
- [ ] **MCP: server vs inline tools** — what MCP is, why a FastMCP server over defining tools in-process, transport (STDIO vs HTTP) *(source: Cognizant FastMCP work)*
- [ ] **Tool/function calling internals** — schema authoring, docstrings/type-hints as the agent-facing interface *(partially in Judgment Log)*
- [ ] **Prompt engineering patterns** — CoT, ReAct, few-shot, structured/JSON output — when each *(source: Cognizant prompt work)*

### Evals & observability  *(genuine gap — highest learning value)*
- [ ] **Why eval before model swap** — silent regressions, tool-calling differs across providers *(partially in Judgment Log — deepen)*
- [ ] **RAGAS + core LLM metrics** — faithfulness, relevancy, etc.; what they measure *(source: path gap)*
- [ ] **LangSmith tracing/observability** — what it gives you, @traceable vs @tool *(source: path gap; @tool/@traceable partly in Judgment Log)*

### Async architecture
- [ ] **Celery workers vs FastAPI background tasks vs asyncio** — why Celery for autoclip's pipeline *(source: autoclip)*

### Mid-Python Dev interview prep *(roadmap: `career/mid-python-developer-prep/`)*
- [ ] **Python data model** — `is` vs `==` + small-int cache, mutable-default evaluated-once, `__eq__`/`__hash__` contract + invariant, first-class functions *(acquired 2026-06-26 via /learn §1.1; build banked 2026-06-29 — GridCell value object. Ready to defend cold in /sharpen.)*
- [ ] **Type hints in earnest** — hints inert at runtime; nullable (`| None`, the type) vs required (the default) as independent axes; Pydantic v2 makes `x: int|None` required → 422 (v1 implicit-None default removed); builtin generics `list[str]`/`dict[str,float]`; `Protocol` structural typing for shapes you don't own + `@runtime_checkable` gotcha *(acquired 2026-06-30 via /learn §1.2; build pending — four-corner ForecastQuery model. Defend cold once built.)*

### Secure API on AWS *(roadmap: `career/secure-api-engineering/`)* — ⏸ **paused 2026-08-27** *(was the active track; label repaired 2026-11-13)*

*Seeded 2026-08-10 from a real posting's requirements; **de-timeboxed 2026-08-13** when that role closed. The clock is gone, the queue isn't — this is the production-API and security layer under the capstone. Build: `career/lesson_assignments/secure-api-lab`.*

**Depth bars carry over from the roadmap, and they define what "Owned" means in `/sharpen`:**
- **`[A]`** — the `/sharpen` bar is full: mechanism + why-this-over-that + failure mode, cold. 95% is a miss.
- **`[B]`** — decision-level only. "When I'd reach for it and the one-line why" is a complete pass; don't grade internals.
- **`[C]`** units are deliberately **not in this queue.** Defending "what Shield Standard is" cold is ceremony — they're taught, noted, and left alone.

- [ ] `[A]` **Resource server vs authorization server** — your API validates tokens Okta issued; it never issues them. The framing the whole Okta bullet rests on *(source: JD "exposing APIs that support integration with IDP")*
- [ ] `[A]` **OAuth2 grant-type map + what 2.1 removed** — implicit and ROPC gone, PKCE now required for confidential clients too; each removal traces to a specific attack. Still an Internet-Draft, not an RFC — say so precisely *(source: JD; verified live 2026-08-10)*
- [ ] `[A]` **Client credentials flow** — no user context; why it can't request OpenID scopes and needs a custom scope. The flow Issue 2 actually uses
- [ ] `[A]` **OIDC vs OAuth2 = authn vs authz** — ID token vs access token, why you never authorize off an ID token *(the decision tree `CAREER_LOG.md` Security section records as missing)*
- [ ] `[A]` **JWT anatomy** — encoding not encryption; anyone can read it; therefore never put PHI in one
- [ ] `[A]` **The JWT validation checklist, cold** — signature · `iss` · `aud` · `exp` · `nbf` · algorithm allow-list; plus `cid` for Okta. Six items, recited without hesitating
- [ ] `[A]` **`alg: none` and RS256→HS256 confusion** — why you pin algorithms and never read the payload before verifying. Naming these unprompted is a senior signal
- [ ] `[A]` **JWKS fetch, `kid` selection, caching, rotation** — cache until an unknown `kid` appears; the failure modes of both over-fetching and never re-fetching
- [ ] `[A]` **Client cert as an identity** — extracting subject/SAN → service principal; authenticates the *workload*, not a user
- [ ] `[A]` **mTLS vs JWT vs both** — mTLS authenticates the *workload/channel*, the JWT authorizes the *call*. Layered is the zero-trust answer. *The single highest-value one-liner in §5*
- [ ] `[A]` **The AWS request path as one diagram** — Route 53 → ACM → WAF → ALB → ECS Fargate → CloudWatch. Drawn cold in under 4 minutes
- [ ] `[A]` **ECS task role vs task execution role** — execution role = what ECS needs (pull image, write logs, inject secrets); task role = what your app code can call. Classic interview question
- [ ] `[A]` **The negative test matrix** — expired · wrong aud · wrong iss · bad signature · `alg:none` · missing scope (403) · missing header (401). Seven cases
- [~] `[A]` **`async def` vs `def` and the threadpool trap** — it's a **three-way** routing decision, not two: `async def` + only awaitables → runs on the loop, unbounded · plain `def` → Starlette `run_in_threadpool` → `anyio.to_thread.run_sync`, capped at **40** (`current_default_thread_limiter().total_tokens`) · `async def` + a blocking call → runs on the loop and **stops** it, effective concurrency **1**. Row three is not a slower row one, it's a **worse row two** — `async def` opts *out* of the safety net. Throughput for `def`: `ceil(N / pool) × duration`. The 40 is **one shared pool per process** — `def` *dependencies* draw from it too, so a sync JWKS fetch in the auth dependency caps the entire API at 40. Diagnostic: idle CPU + high p99 + **a single request to an idle box is fast** = blocked loop (a slow DB is slow at concurrency 1; an undersized box pegs CPU). **Breaks if wrong:** one sync driver in an `async def` and p99 goes to seconds with no error and an idle-looking CPU graph. *(acquired 2026-08-18 via `/learn` §1.2a — **1.2b pending** (spotting blocking calls in third-party libs, the escape hatches); build assigned not run. Defend cold once complete.)*
- [ ] `[A]` **`Depends()` and why auth belongs in a dependency** — the composition point, and the `dependency_overrides` testing seam
- [ ] `[A]` **`response_model` as a PHI-leak control** — minimum-necessary enforced at the serialization layer, not in a policy doc
- [ ] `[A]` **401 vs 403 vs 422** — and why a valid token missing a scope is 403
- [ ] `[B]` **ASGI vs WSGI — the concurrency model** — both are *specifications*, not packages. WSGI's unit of concurrency is an OS thread (~8 MB stack + scheduler entry); ASGI's is a heap-allocated coroutine, so *waiting* is nearly free. Wins on I/O-bound work, buys nothing on CPU-bound, and done wrong is **strictly worse** than WSGI. Plus the container rule: one uvicorn process per ECS task, because nested process managers make a hung worker invisible to ECS *(acquired 2026-08-11 via `/learn` §1.1 — defend cold)*
- [ ] `[B]` **JWT revocation** — bearer tokens are valid until expiry; short TTL + rotation vs introspection vs denylist, and what each costs
- [ ] `[B]` **Where to validate the token: edge vs app** — ALB native JWT verification (new 2025-11) and API Gateway authorizers vs an in-app dependency; defense in depth says both
- [ ] `[B]` **ALB mTLS: passthrough vs verify mode** — `X-Amzn-Mtls-Clientcert` header family vs a trust store with a CA bundle + CRLs. Two distinct modes, don't blur them
- [ ] `[B]` **Cert rotation/expiry as the #1 mTLS production failure** — and why AWS Private CA has a $50/mo short-lived tier (7-day max) next to the $400/mo general-purpose one
- [ ] `[B]` **API Gateway vs ALB — when each** — HTTP vs REST API, JWT authorizers, usage plans, and the honest cost/latency tradeoff
- [ ] `[B]` **HIPAA technical safeguards mapped to API surfaces** — access control, **audit controls** (log actor/action/resource-reference/time, never the payload), integrity, transmission security
- [ ] `[B]` **GitHub Actions OIDC federation to an IAM role** — no long-lived AWS keys in CI, ever. "Access keys in secrets" is a miss

---

## Tier 2 — Periphery (80/20 / explain-the-decision)

### Cloud / AWS
- [ ] **Bedrock vs SageMaker vs roll-your-own** — the service-selection decision *(source: Cognizant Bedrock work)*
- [ ] **Lambda vs FastAPI** — when serverless over a running service
- [ ] **IAM least privilege** — roles/policies, enough to secure his own project
- [ ] **S3 basics** — when/why

### Security
> **Promoted to Tier 1 permanently (2026-08-13).** The first two rows below now live in the "Secure API on AWS" block above. They were promoted for a posting; they stay promoted because they're foundational to anything that authenticates a caller. Work them there.

- [ ] **authn vs authz** — the decision tree, not just the words *(→ promoted, see the Secure API block)*
- [ ] **JWT + API key patterns** — issue/sign/verify, when each *(→ promoted, see the Secure API block)*
- [ ] **OWASP Top 10** — read once, all ten, one sitting
- [ ] **Secrets management** — .env, never committing keys, prod patterns
- [ ] **Prompt injection defense** — pre/post hooks as guardrails *(partly owned via hooks)*

### Infra & systems
- [ ] **Docker** — containers vs VMs, what a Dockerfile does *(currently "Exposed" — resume shows usage; sharpen the why)*
- [ ] **Docker Compose** — multi-service networking, volumes
- [ ] **CI/CD concepts** — pipeline stages, when it matters
- [ ] **SQL vs NoSQL vs vector vs Redis** — pick-the-store decision; indexing basics
- [ ] **Caching** — write-through vs write-back, LRU eviction, invalidation
- [ ] **REST API design** — methods, status codes, what makes it RESTful
- [ ] **CAP theorem / 12-factor / scalability patterns** — vocab-level, decision-level

### Study targets (not grill concepts — courses/certs)
- AWS AIF-C01 → then MLA-C01
- Targeted course fillers *only* for named gaps: RAG-LLM Evals, MCP Masterclass, LangChain Academy (LangSmith/LangGraph)

---

## Notes
- The queue is seeded; reprioritize freely. A live project need always jumps the line — that's the best learning.
- When a concept lands, it's logged to the CAREER_LOG Judgment Log and enters `/drill` rotation. This file tracks acquisition; CAREER_LOG tracks mastery + review cadence.
- **This queue is the primary learning engine** (see `career/helpful_notes_and_guides/AI Engineering Master Guide.md`, now demoted to reference). The Master Guide's course list is a *resource pool*, not a syllabus.
- **Concepts pull resources; resources don't push concepts.** Mine course syllabi (Eden Marco, etc.) for *candidate* concepts — but they enter this pool **unprioritized**. Don't transcribe a whole syllabus into a completion checklist; that recreates the course-abandonment trap. Projects decide the order.
- **Courses are gap-fillers, pulled on demand.** When `/sharpen` hits a true *Gap* (never encountered, can't struggle-first), pull the matching course section, learn just that, then return to the queue.
- The build still matters: the dedicated capstone project (Master Guide Phase 2) is where grilled concepts become real judgment. Grilling without building is passive consumption with extra steps.
