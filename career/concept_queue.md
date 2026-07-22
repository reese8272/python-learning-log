# Concept Queue — the Sharpen backlog

The prioritized list of concepts to grill with `/sharpen`. Seeded from Reese's own shipped code (the richest curriculum — defend what you already built) and the genuine gaps on the AI Engineering Master Guide path.

**Where this sits in the pipeline:** `/learn` (acquire from zero, via `readings/ai-engineering-curriculum/`) → **`/sharpen` (this queue — defend cold)** → `/drill` (retain). A unit learned via `/learn` lands here to be defended. Concepts from his own shipped code start here directly (already built, just need defending). Two ledgers: this file tracks *acquisition/defense*; `CAREER_LOG.md` tracks *mastery + review cadence*.

**Two tiers** (see `.claude/commands/sharpen.md`):
- **Tier 1 — Foundational / agentic core** → 100%, "can teach it." Mechanism + why-this-over-that + failure mode. Defend cold.
- **Tier 2 — Periphery** → Pareto 80/20, "explain the decision." Enough to make the call, not teach the internals.

`[ ]` = not yet owned · `[~]` = needs another rep · `[x]` = owned (date) — moves to `/drill` spaced-repetition rotation.

Work top-down within each tier. Tier 1 before Tier 2 unless a real project need jumps the line.

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
- [ ] **What an LLM call actually is** — stateless re-send model, tokens, context window (hard-reject vs lost-in-middle), cost asymmetry (output ~5× input & why) *(learned 2026-06-22 via /learn; defend cold)*
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

---

## Tier 2 — Periphery (80/20 / explain-the-decision)

### Cloud / AWS
- [ ] **Bedrock vs SageMaker vs roll-your-own** — the service-selection decision *(source: Cognizant Bedrock work)*
- [ ] **Lambda vs FastAPI** — when serverless over a running service
- [ ] **IAM least privilege** — roles/policies, enough to secure his own project
- [ ] **S3 basics** — when/why

### Security
- [ ] **authn vs authz** — the decision tree, not just the words
- [ ] **JWT + API key patterns** — issue/sign/verify, when each
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
