# Career Log — Reese

**Role target:** AI Consultant / AI Systems Engineer  
**Current context:** AI Consultant & SME role offered at Cognizant (2026-04-03)  
**Focus:** Agentic engineering, cloud AI (AWS), production systems, security  
**Mastery standard:** Can I explain why THIS over THAT? If I can break down the decision — not just the syntax — I own it.

**Reference:**
- `patterns.md` — Reusable patterns and mental models; add when a pattern proves reliable
- Weekly / monthly reflection → handled by `/weekly-review` and `/monthly-review`

---

## SKILLS TRACKER

*Update when understanding genuinely deepens. The bar is explanation, not execution.*

**Last Reviewed** = the date you last actively recalled this skill cold — explained it out loud, passed a practice question on it, or had it tested in real work. Not the date you re-read the notes. During `/weekly-review`, scan for anything not reviewed in 2+ weeks and flag it for a quick self-test.

**Levels:**
- **Gap** — haven't touched it
- **Exposed** — seen it in context, can't explain it independently yet
- **Building** — actively learning, reps in progress
- **Can explain the what** — understand what it does and how to use it
- **Can explain the why** — understand the decision rationale; can say why THIS over THAT
- **Can teach it** — explained it to someone else and it held up under questions

---

### Agentic Engineering
| Skill | Level | Notes | Last Updated | Last Reviewed |
|-------|-------|-------|--------------|---------------|
| LangChain | Building | Actively working through Eden Marco course. Understands ReACT loop, State = messages array, LangChain vs raw API decision rationale, system prompt as control surface | 2026-05-04 | - |
| LangGraph | Can explain the why | Explained cold (2026-06-22): the graph is a *control surface* over an otherwise-uncontrollable ReAct loop — guarantees a step runs regardless of the model's decision; shared `StateGraph` state + conditional vs deterministic edges; reach for it on need for control/state/durability, **not** agent count (a single agent still uses it for persistence / HITL / resume). Resume shows production multi-agent builds (Cognizant code-gen/test/review team, autoclip). | 2026-06-22 | 2026-06-22 |
| LangSmith | Gap | - | - | - |
| MCP (Model Context Protocol) | Exposed | Aware of it through work context | 2026-04-01 | - |
| Agent orchestration | Exposed | Working with agents at Cognizant | 2026-04-01 | - |
| Tool use / function calling | Building | Understands docstrings + type hints as agent-facing interface; LangChain schema authoring vs raw JSON tradeoff; MAX_ITERATIONS as production guard | 2026-05-04 | - |

### LLM Systems
| Skill | Level | Notes | Last Updated | Last Reviewed |
|-------|-------|-------|--------------|---------------|
| RAG fundamentals | Building | Modularity, retrieval patterns, code cleanliness — reps in progress | 2026-01-07 | - |
| Hooks / guardrails | Can explain the why | Pre-hook = gate before LLM call; post-hook = sanitize before returning. Can explain the decision rationale and order. | 2026-04-01 | - |
| Prompt engineering | Can explain the why | Evaluate-before-delegate principle understood. + Prompt anatomy **defended cold in /sharpen (2026-07-22)** — first cold defense: render order tools→system→messages = cacheable byte-prefix (system top-level, not messages[0]); assistant turns = re-sent prior outputs = the "memory" (stateless API, history re-billed every call); max_tokens = 200 + stop_reason (never raises) vs context window = 400 BadRequestError (raises — different retry paths); prefill removed 4.6+ (400) → output_config.format *enforces* shape vs prefill *nudge*, shape ≠ quality. Taught in-session, drill it: silent cache invalidators (dynamic bytes in prefix; verify via usage.cache_read_input_tokens). + Steering ladder acquired (2026-07-20): instructions → few-shot (3–5, tagged, diverse) → schema; role prompting = cacheable-prefix prior-shift; aggressive "MUST" prompting overtriggers on 4.5/4.6+ — still to defend cold. "Can teach it" waits on the §1.3 defense. | 2026-07-22 | 2026-07-22 |
| Output evaluation | Can explain the what | Run similar prompts, compare key info surfaces, refine if missing | 2026-04-01 | - |
| LLM evals / benchmarking | Gap | - | - | - |

### System Design
| Skill | Level | Notes | Last Updated | Last Reviewed |
|-------|-------|-------|--------------|---------------|
| FastAPI | Building | ⚠ **Note corrected 2026-08-10 — the old note ("haven't built with it") was factually false.** ~37k LOC of FastAPI in CreatorClip (1,774 test functions) + CFO Agent (177 tests, Redis-backed LangGraph checkpointing). Level held deliberately low per the standing rule in Active Struggles — production LOC is not a mastery claim. Cold defense scheduled 08-16 (`/sharpen`); bump only then. | 2026-08-10 | - |
| REST API design | Building | ⚠ Note corrected 2026-08-10. Has shipped REST surfaces — Django REST over a 14-table Postgres schema (WorldCovers), FastAPI endpoints across both flagship projects. The untested part is *design rationale from scratch* (status-code semantics, idempotency, versioning), not exposure. Roadmap: `secure-api-engineering` §2. | 2026-08-10 | - |
| Service decomposition | Gap | - | - | - |
| Data flow design | Gap | - | - | - |
| Async patterns (asyncio) | Can explain the why | asyncio for I/O-bound, gather for overlapping waits, run_in_executor for blocking calls — can explain why each | 2026-04-01 | - |

### Production Infrastructure
| Skill | Level | Notes | Last Updated | Last Reviewed |
|-------|-------|-------|--------------|---------------|
| Docker | Exposed | Know what it does, can't build Dockerfiles independently | - | - |
| CI/CD concepts | Building | ⚠ **Note corrected 2026-08-10 — "no hands-on experience" was factually false.** CFO Agent runs 5+ CI workflows with auto-deploy to prod on push to main; CreatorClip has staging/prod Docker-compose with CI auto-deploy. Gap is the *vocabulary and the whiteboard sketch*, not the doing. Roadmap: §9. | 2026-08-10 | - |
| GitHub Actions | Building | ⚠ Note corrected 2026-08-10 — authored the workflows above. Untested: OIDC federation to an IAM role (the current no-static-keys pattern) — §9. | 2026-08-10 | - |
| GitLab CI | Gap | - | - | - |

### Cloud — AWS for AI
| Skill | Level | Notes | Last Updated | Last Reviewed |
|-------|-------|-------|--------------|---------------|
| AWS Bedrock | Gap | - | - | - |
| AWS SageMaker | Gap | - | - | - |
| AWS Lambda | Gap | - | - | - |
| AWS IAM | Gap | - | - | - |
| AWS S3 | Gap | - | - | - |

### Cloud — AWS platform & edge *(added 2026-08-10 for the secure-API interview track)*
*The prior AWS section covers only the **AI** services. The platform/edge layer below is what actually fronts a production API, and a full-repo grep on 2026-08-10 returned **zero mentions** of every row here. Honest baseline — the point is a visible before/after as `secure-api-engineering` §6 lands.*

| Skill | Level | Notes | Last Updated | Last Reviewed |
|-------|-------|-------|--------------|---------------|
| ECS / Fargate | Gap | Task def vs service vs task; **task role vs execution role**. Build: secure-api-lab Issue 7 | 2026-08-10 | - |
| ALB | Gap | Listeners/rules/target groups; mTLS passthrough vs verify; native JWT verification (new 2025-11) | 2026-08-10 | - |
| Route 53 | Gap | Alias records, health checks, failover | 2026-08-10 | - |
| ACM / Private CA | Gap | DNS-validated public certs + auto-renewal; PCA general-purpose $400/mo vs short-lived $50/mo (7-day max) | 2026-08-10 | - |
| API Gateway | Gap | HTTP vs REST API, JWT authorizers, usage plans; the when-vs-ALB decision | 2026-08-10 | - |
| AWS WAF / Shield | Gap | Managed rule groups, rate-based rules, count-before-block; Shield Standard vs Advanced (~$3k/mo) | 2026-08-10 | - |
| CloudWatch | Gap | Structured JSON logs, metric filters, alarms; what to alert on for an API | 2026-08-10 | - |

### Security
| Skill | Level | Notes | Last Updated | Last Reviewed |
|-------|-------|-------|--------------|---------------|
| Authentication vs Authorization | Gap | Know the words, can't explain the decision tree. ⏱ Now Tier 1 — the posting names it. Roadmap §3 | 2026-08-10 | - |
| OAuth2 flows | Exposed | **Shipped** YouTube OAuth publishing in CreatorClip, and made a real judgment call on it (cut auto-upload from v1 over sensitive-scope review risk). Never defended cold; grant-type map and OAuth 2.1 changes are genuinely new. Roadmap §3 | 2026-08-10 | - |
| OIDC / IdP integration (Okta) | Gap | Zero repo footprint. Resource-server framing, custom auth server, custom scopes, `aud` + `cid`. Build: Issue 2 | 2026-08-10 | - |
| JWT validation | Gap | Zero repo footprint. The 6-item checklist, JWKS/`kid`/rotation, `alg:none` + RS256→HS256 confusion, revocation. Build: Issues 3–4 | 2026-08-10 | - |
| mTLS | Gap | Zero repo footprint. Cert-as-identity, trust chains, ALB termination modes, rotation as the #1 failure mode. Build: Issue 5 (local openssl CA) | 2026-08-10 | - |
| HIPAA / PHI handling | Gap | Zero operating experience — **do not overclaim** (own prior guidance: `jobs/natera-sr-fwd-deployed/README.md:37`). Studying the technical safeguards + audit-logging discipline. Roadmap §8 | 2026-08-10 | - |
| Credential management | Gap | - | - | - |
| OWASP basics | Gap | - | - | - |
| Cryptography fundamentals | Gap | - | - | - |
| Prompt injection defense | Exposed | Aware through hooks/guardrails context | 2026-04-01 | - |

### Python Core *(locked — reference only)*
| Skill | Level | Notes | Last Reviewed |
|-------|-------|-------|---------------|
| Python fundamentals | Can teach it | Loops, functions, classes, generators, decorators — solid | - |
| Async / asyncio | Can explain the why | See System Design section | - |
| Data structures | Can teach it | Lists, dicts, sets, stacks, queues — can explain selection rationale cold | - |
| DSA | Can explain the why | DFS, BFS, binary search, two-pointer, sorting — logic is solid | - |
| Decorators | Can teach it | @property, @staticmethod, @classmethod, @cache, @dataclass — design intent understood | - |

---

## JUDGMENT LOG

*The bar: can I explain why THIS over THAT? Log moments where the decision — not just the answer — clicked.*

| Date | Concept / Decision | Why THIS over THAT | Context | Can Teach | Last Reviewed |
|------|-------------------|--------------------|---------|-----------|---------------|
| 2026-07-22 | Why output tokens cost ~5× input | Input is processed in **one parallel prefill pass** — the whole prompt at once. Output is **autoregressive**: generated one token at a time, and each new token requires a full forward pass over everything generated so far. Serial generation vs parallel reading is the mechanical reason for the price asymmetry ($5/$25 per MTok on current Opus) — and why long outputs, not long inputs, dominate latency. | /sharpen cold defense of §1.1 (learned 06-22); defended unaided a month later | Yes | 2026-07-22 |
| 2026-07-22 | Anatomy of a prompt — system as top-level param, memory, token walls, prefill→structured outputs | System is top-level (not messages[0]) because the API renders **tools → system → messages** and caching is a byte-prefix match — fixed order makes static instructions a stable, cacheable prefix (reads ~0.1×; one dynamic byte in the prefix and everything after misses). "Memory" = re-sent assistant turns on a stateless API — context management is a *cost* problem. max_tokens = 200 you inspect (`stop_reason`) vs context-window-exceeded = 400 that raises — different retry code paths; treating them the same retries an unfixable request. Prefill (nudge) removed on 4.6+ → `output_config.format` (enforce); shape ≠ quality either way. | First /sharpen cold defense; from the 07-08 /learn §1.2 extraction-assembler build; verified vs current Claude API reference (caching, stop-reason, migration docs) | Yes — invalidator facet taught this session, drill it | 2026-07-22 |
| 2026-07-07 | Playwright + Claude Code for UI/UX test generation (over manual testing / Cypress / Selenium) | Manual UI/UX testing was slow, tedious, and leaked visual regressions between releases. Chose **Claude Code** because Claude is the company's proprietary in-house LLM. Chose **Playwright over Cypress/Selenium** because it's more LLM-friendly to *generate* against (auto-waiting, role-based locators, cleaner/consistent API → less flaky LLM-written code). Outcome (rung-3): devs ship UI changes faster without hand-testing every build; clients see visual upgrades reach users sooner. | Cognizant work; surfaced in `/learn soft` Unit 1 (senior-frame communication) | Partial — articulated in `/learn`; defend cold in `/sharpen` (esp. the *why* behind "more LLM-friendly") | 2026-07-07 |
| 2026-06-22 | LangGraph vs plain ReAct agent (`AgentExecutor`) | A ReAct agent is dynamic but *unconstrained* — the LLM controls the whole flow, so you can't guarantee any step runs. LangGraph wires the flow as a graph: a deterministic edge **guarantees execution regardless of the previous agent's decision**. You move must-happen steps (validation, security review, human checkpoints) out of the probabilistic loop and into the structure. So you reach for LangGraph not for *more* dynamism (ReAct is already dynamic) but to *buy back control* over it. | Cognizant code-gen/test/review multi-agent team; verified vs LangGraph docs | Yes | 2026-06-22 |
| 2026-06-22 | When NOT to use LangGraph | Don't decide by agent *count* — decide by whether you need enforced **control, shared/persistent state, or durability**. Multiple independent agents with no shared state → no graph (just run them). A *single* agent that must survive a restart, resume after interrupt, or pause for human approval → still LangGraph. (LangChain's own agents are now built on top of LangGraph for exactly this.) The special thing is the shared `StateGraph` state flowing node→node. | Sharpen session; verified vs LangChain/LangGraph docs | Yes | 2026-06-22 |
| 2026-05-07 | @tool vs @traceable | Completely separate concerns — different layers, different jobs. @tool is LangChain: wraps a function into a tool object (schema gen, result parsing). @traceable is LangSmith: instruments for observability. Drop to raw Ollama → lose @tool (you left LangChain); @traceable is provider-agnostic and stays. Confusing them means misdiagnosing what breaks when you switch providers. | Eden Marco course | Yes | 2026-07-06 (partial — had the what + layers, missed the provider-swap failure mode) |
| 2026-05-07 | Ollama schema generation modes | Two modes: (1) manual JSON — write the schema yourself, docstrings irrelevant; (2) auto-schema — pass functions directly, Ollama generates schema, but requires Google-style docstrings. Choosing wrong means either unnecessary boilerplate (writing JSON when auto would work) or broken schema generation (using auto without the right docstring format). | Eden Marco course | Yes | - |
| 2026-05-04 | LangChain vs raw API | LangChain removes three pain points — schema authoring, provider lock-in, result parsing. Drop to raw only when you need behavior LangChain hides (e.g., streaming edge cases, custom retry logic). The abstraction costs you visibility in exchange for speed. | Eden Marco course, Session 1 | Yes | - |
| 2026-05-04 | Model swap = benchmarked decision | Swapping models is not a config change — tool-calling behavior differs between providers and versions in non-obvious ways. Two checks before swapping: (1) does the model support tool calling? (2) does it eval correctly on your actual use case? Without evals, regressions are silent. | Eden Marco course, Session 1 | Yes | - |
| 2026-04-01 | Pre-hook vs post-hook | Pre-hook gates input before it reaches the model — catches injection, validates, logs. Post-hook sanitizes output before it reaches the caller — scans for credentials, checks policy. Order matters: bad input should never touch the model; bad output should never reach the user. | Claude 101 + Cognizant work | Yes | - |
| 2026-04-01 | asyncio.gather vs sequential awaits | Sequential awaits stack wait times (5 x 2s = 10s). gather overlaps them (5 x 2s ≈ 2s). Use gather when calls are independent and I/O-bound. Using it with synchronous blocking functions doesn't help — use run_in_executor to offload those to a thread pool instead. | Career reflection | Yes | - |
| 2026-03-19 | @classmethod vs @staticmethod vs module function | @classmethod: needs class context, inherits correctly (use cls not ClassName). @staticmethod: utility grouped with the class but needs no instance or class state. Module function: fully standalone. Choose by what context the function actually needs — don't reach for classmethod when there's no class state involved. | Decorators session | Yes | - |
| 2026-01-19 | Queue vs Stack (FIFO vs LIFO) | Queue = first in, first out — use when order of arrival matters (BFS, task scheduling). Stack = last in, first out — use when you need to process the most recent item first (undo, DFS, call stacks). Both are lists under the hood; the difference is which end you pop from. | DSA practice | Yes | 2026-07-28 (solid — sharpened the failure mode: swap the frontier and BFS silently becomes DFS, shortest-path guarantee gone) |
| 2026-01-19 | BFS vs DFS | BFS = level by level, guarantees shortest path in unweighted graphs. DFS = goes deep first, exhaustive search. If you need the shortest route, BFS. If you need to find if a path exists at all, DFS. | DSA practice | Yes | - |
| 2026-01-03 | Dict vs List for counting | List lookup is O(n) — you scan every element. Dict lookup is O(1) — hash table, direct access. When you're counting occurrences or checking membership repeatedly, dict is the right tool. Nested loops + list = O(n²) for no reason. | Boot.dev exercise | Yes | 2026-07-05 (partial — had the what, missed O(1)-vs-O(n) rationale) |

---

## CONSULTING LOG

*Capturing moments where I explained, led, or taught. This is career data.*

| Date | Context | What I explained or led | How it landed |
|------|---------|------------------------|---------------|
| 2026-04-03 | AI Consultant & SME role offered at Cognizant | — | Role offered based on demonstrated AI expertise and ability to lead teams |

---

## ACTIVE STRUGGLES

*Current blockers. Delete when resolved, update Skills Tracker.*

- **System design instincts:** Know the vocabulary (Docker, K8s, FastAPI, CI/CD) but don't yet have the judgment for *when* to reach for each. Gap is "knowing when," not "knowing what." Next: concept tour — map the territory before building.
- **Security fundamentals:** Auth/authz, credential management, cryptography — exposed at best. These matter for production AI systems and the consultant role.
- **Cloud / AWS for AI:** Zero hands-on. SageMaker, Bedrock, Lambda, IAM — need to build something real in AWS, not just read about it.
- **Agentic frameworks:** Actively working through Eden Marco LangChain course. Layer 1 (agent loop, function calling) done. LangGraph why-over-ReAct now explained cold (2026-06-22). LangSmith/evals still genuine gaps; MCP shipped in production (FastMCP at Cognizant) but the *why* not yet defended cold.
- **Independent execution under observation (2026-07-25, from John's mid-year notes):** The review's core critique — "prove you can perform without AI" + accountability/comms gaps under stress (Verizon merge conflicts, marketing engagement). Not a learning-system gap; a *performance-visibility* gap: unassisted capability was never trained as its own rep and never made visible at work. Counter-system: `helpful_notes_and_guides/Independence Protocol.md` (learning ladder, weekly Cold Bench, own-every-line + comms floor, artifact scoreboard through Jan 2027). **Day-2 data point (07-28): target state reached from the inside** — work quiz passed via self-invented fading-scaffold protocol (support faded to zero), "I can defend myself" on the work pipeline (files, contracts, configs, his code's place in it); day 2 cost less and paid more than day 1. Boss call 07-29 from a position of knowledge = first visible payoff. Resolve when the year-end package ships.
- **The secure-API gap (opened 2026-08-10, sprint ended 2026-08-13):** The role that triggered this closed on years-of-experience before an interview happened, so there's no interview outcome to record. **The gap analysis is what survived, and it still holds** — it split cleanly in two: **recalibration** (FastAPI, async, OAuth2, testing, CI/CD: already in production, never said out loud) vs **acquisition from zero** (the entire AWS platform/edge layer, mTLS, Okta/OIDC, HIPAA — zero repo footprint on a full grep). Roadmap: `career/secure-api-engineering/summary.md`, build: `~/workspace/secure-api-lab`. **Resolve when §6 is banked and Issue 7 has actually deployed** — that's the point where the "acquisition from zero" half stops being a gap.
- **No deadline currently drives the learning (opened 2026-08-13).** The seven-day sprint produced more structured learning than any comparable stretch in the record — the depth bars, the chunk loop, the check formats, the Learning notes block all came out of it. That week had a hard external date on it. It's gone, and nothing has replaced it. The open question is what does: a cert exam date (AIF-C01 is already the Master Guide's Phase 4 opener), a demo to John, or a public milestone on `secure-api-lab`. **Resolve by naming one.**
- **Tracker undersells the resume (2026-06-22):** *(2026-08-10 addendum — acted on, partially. The FastAPI / REST / CI-CD / GitHub Actions **notes** were factually wrong, not merely conservative: "haven't built with it" against ~37k LOC, "no hands-on experience" against 5+ live workflows. Notes corrected and levels moved Gap→Building as a **factual correction**, not a mastery claim; "Gap" asserts something untrue. The standing rule below still holds — no bump past Building without a cold defense, scheduled 08-16.)* The Skills Tracker is calibrated below reality — it marked LangGraph/FastAPI/MCP/Bedrock as Gap/Exposed while the resume shows production builds of all of them (CFO Agent, autoclip/CreatorClip, Cognizant multi-agent team). The real gap isn't building capacity — it's *defending the decisions cold* (consultant-grade articulation). The fix is the new `/sharpen` loop + `career/concept_queue.md`: grill each concept against his own shipped code until the level reflects demonstrated explanation, not exposure. Bump tracker levels only as concepts are actually defended, not from resume evidence alone.
