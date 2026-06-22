# AI Engineering Curriculum — self-taught, live-researched

**What this is:** The technical learning path that replaces taking online courses. Each unit is learned in-catalog via `/learn` — researched live against current official docs, taught at its tier, then handed to `/sharpen` (defend cold) and `/drill` (retain). The course syllabi (Eden Marco, MCP Masterclass, RAG-evals, LangChain Academy, Anthropic prompt-eng) were mined for *what to cover*; the actual teaching is generated fresh each session so it never goes stale.

**Source of truth:** `career/helpful_notes_and_guides/AI Engineering Master Guide.md` (North Star, capstone, salary ladder, resource pool). This file is the *technical curriculum* derived from it.

**The pipeline:**
```
/learn          →   /sharpen        →   /drill
acquire (here)      defend cold         retain (spaced rep)
researched live     100% / tier bar     against forgetting curve
```

**Tiers** (same as `career/concept_queue.md`):
- **Tier 1 — Foundational / agentic core** → 100%, "can teach it." Mechanism + why-this-over-that + failure mode.
- **Tier 2 — Periphery** → Pareto 80/20, "explain the decision."

**Status keys:** `[ ]` not started · `[~]` in progress / needs another pass · `[x]` learned (date) → enters `/sharpen` then `/drill` rotation.

**How to use:** Work top-down within a section; sections are roughly ordered by dependency. A live project need always jumps the line — that's the best learning. When `/learn` finishes a unit, it logs the session to `reflection_log/`, marks it here, and drops the concept into `career/concept_queue.md` for a later defense pass.

---

## ⚠ Currency Watch — what the courses teach that's now WRONG (2026)

These are the breaking changes live research surfaced. `/learn` must teach the **current** pattern, not the course's. This list is the single biggest reason to learn in-house.

- **LangChain v1 is a breaking release.** `AgentExecutor`, `initialize_agent`, `create_react_agent` → **`langchain.agents.create_agent`** (built on LangGraph). Legacy chains (`LLMChain`, `RetrievalQA`, `ConversationChain`) moved to **`langchain-classic`**. Agent param `prompt` → **`system_prompt`** (string, not `SystemMessage`). Pre/post hooks → **middleware**. Agent state must be **`TypedDict`** (no Pydantic). Memory → **LangGraph persistence (checkpointers)**. LCEL is *not* deprecated (use it for pipelines; `create_agent`/LangGraph for agents). *(Note: `create_agent` import path churned across v1.0→1.1.x — verify against the installed version.)*
- **MCP spec is now 2025-11-25.** Standalone **SSE transport is deprecated** — only STDIO + Streamable HTTP exist (SSE is a sub-mode of Streamable HTTP). **JSON-RPC batching removed.** Added: structured tool output (`outputSchema`/`structuredContent`), **elicitation**, **tasks** (durable execution), sampling-with-tools, OAuth 2.1 Resource Server model + Resource Indicators. FastMCP 2.x is the maintained standalone.
- **RAGAS API is mid-migration.** Legacy lowercase metrics (`faithfulness`, `answer_relevancy`, `context_recall`) → class API (`Faithfulness`, `ResponseRelevancy`, `LLMContextRecall`) → newer **collections API** (`from ragas.metrics.collections import AnswerRelevancy`). Build dataset via `SingleTurnSample` → `EvaluationDataset`; wrap judge with `LangchainLLMWrapper`. Testset gen is now **knowledge-graph based** (`TestsetGenerator` + `default_transforms()`), not the old "evolutions" API. Pin your version.
- **LangGraph v1.** HITL: **`interrupt()` + `Command(resume=...)`** over static breakpoints/`NodeInterrupt`. Checkpointer **durability modes** (`durability='exit'|'async'|'sync'`). `MessageGraph` removed → `StateGraph` with a messages key. Supervisor/swarm are **separate packages** (`langgraph-supervisor`, `langgraph-swarm`). Docs moved to `docs.langchain.com/oss/python/langgraph`. Env vars `LANGSMITH_*` (legacy `LANGCHAIN_*`).
- **Prompt engineering 2026.** **Prefilling the assistant turn is removed** (400 error on Claude 4.6+) → use Structured Outputs + system-prompt instructions. **Adaptive thinking** (`effort` param) replaces manual CoT and `budget_tokens`. Aggressive "you MUST" / anti-laziness prompting now **backfires** (over-triggers). Models are more concise by default; you now prompt to *add* summaries / suppress LaTeX. Per-model prompting guidance now matters.

Re-verify before each unit — these move fast.

---

## Section 1 — Foundations (Tier 1)

- [ ] **What an LLM call actually is** — tokens, completions, context window; reason about cost/latency/failure modes. `T1` · src: Eden Marco Ch.1
- [ ] **Prompt vs. context engineering** — deliberate structuring; context window as the real bottleneck (2026 framing). `T1` · src: Eden Marco, Anthropic
- [ ] **Core prompt patterns** — clear-and-direct, role, XML tagging, few-shot/multishot, output-format control. `T1` · src: Anthropic tutorial
- [ ] **Chain-of-thought & evidence-before-conclusions** — reason-then-answer; quote-grounding for long docs. `T1` · src: Anthropic ⚠ adaptive thinking now preferred over manual CoT
- [ ] **Avoiding hallucinations** — give an "out", ground in sources, investigate-before-answering. `T1` · src: Anthropic
- [ ] **Prompt patterns that changed in 2026** — prefill removed, structured outputs, adaptive thinking/effort, over-prompting backfire. `T1` · src: live docs ⚠ entirely post-dates the tutorial

## Section 2 — LangChain Core (Tier 1)

- [ ] **`init_chat_model` & the messages model** — provider-agnostic LLM instantiation; `System/Human/AIMessage`, `content_blocks`. `T1` · src: Eden Marco
- [ ] **Prompt templates & LCEL** — `ChatPromptTemplate`, the pipe (`|`) composition: prompt → model → parser. `T1` · src: Eden Marco ⚠ LCEL for pipelines, `create_agent` for agents
- [ ] **Output parsers & structured output** — `StrOutputParser`, Pydantic/structured parsing; typed results. `T1` · src: Eden Marco
- [ ] **Document loaders & text splitters** — ingest to `Document`; `RecursiveCharacterTextSplitter`, chunk size/overlap. `T1` · src: Eden Marco
- [ ] **Legacy vs. v1 surface** — what moved to `langchain-classic`, why LCEL/`create_agent` replaced old chains. `T2` · src: live docs ⚠ the v1 migration itself

## Section 3 — Agents (Tier 1)

- [ ] **The ReAct loop from scratch** — think→act→observe, the scratchpad; build it manually before abstractions. `T1` · src: Eden Marco "agents under the hood"
- [ ] **Tool / function calling** — `@tool`, schemas, docstrings/type-hints as the agent-facing interface; how a call is emitted and routed. `T1` · src: Eden Marco
- [ ] **`create_agent` (v1)** — the current one-line agent on LangGraph: durable execution, streaming, checkpointing; `system_prompt`, middleware. `T1` · src: live docs ⚠ replaces `AgentExecutor`/`create_react_agent`
- [ ] **ReAct failure modes** — skips steps, declares done early, loops; how to constrain. `T1` · src: all agent work
- [ ] **Code-execution / multi-tool agents** — Python REPL tool, sandboxing, multi-tool routing. `T2` · src: Eden Marco

## Section 4 — LangGraph (Tier 1)

- [ ] **Why a graph over a ReAct loop** — guaranteed execution & control surface vs. an uncontrollable loop. `T1` · src: Eden Marco *(already owned — 2026-06-22; deepen)*
- [ ] **`StateGraph`, state schema, reducers** — `TypedDict` channels, `Annotated` reducers, `add_messages`/`MessagesState`. `T1` · src: LangChain Academy ⚠ reducers are the most-misunderstood concept; `MessageGraph` removed
- [ ] **Nodes & edges** — node = partial-state update; deterministic vs. conditional edges; `START`/`END`. `T1` · src: LangChain Academy
- [ ] **Cyclic graphs & the agent loop in LangGraph** — LLM node ↔ tool node via conditional edge. `T1` · src: Eden Marco
- [ ] **Checkpointers & persistence** — save state per step under a thread; `InMemory`/`Sqlite`/`Postgres` savers; durability modes. `T1` · src: LangChain Academy ⚠ durability flag; shallow savers deprecated
- [ ] **Short- vs. long-term memory** — per-thread checkpointer vs. cross-thread `Store`; trimming/summarization. `T1` · src: LangChain Academy
- [ ] **Human-in-the-loop** — `interrupt()` + `Command(resume=...)`; edit-state/approve patterns; time travel. `T1` · src: LangChain Academy ⚠ over static breakpoints/`NodeInterrupt`
- [ ] **Streaming modes** — `values`/`updates`/`messages`/custom for responsive UIs. `T2` · src: LangChain Academy
- [ ] **Parallelism & composition** — fan-out/fan-in, subgraphs, map-reduce via `Send`. `T1` · src: LangChain Academy
- [ ] **Multi-agent topologies** — supervisor vs. swarm vs. single ReAct; handoff tools; when each. `T1` · src: Eden Marco, LangChain Academy ⚠ supervisor/swarm are separate packages
- [ ] **Reflection & Reflexion patterns** — self-critique→revise; learning from past attempts. `T2` · src: Eden Marco
- [ ] **LangGraph deployment** — Platform/Server, assistants, threads/runs, double-texting. `T2` · src: LangChain Academy

## Section 5 — RAG & Retrieval (Tier 1)

- [ ] **What an embedding actually is** — vector space, dimensionality, similarity; same model indexes & queries. `T1` · src: Eden Marco, autoclip/CFO Agent
- [ ] **Embedding model choice** — why Voyage AI over OpenAI embeddings in autoclip. `T1` · src: autoclip
- [ ] **Chunking strategy** — fixed/recursive/semantic/sentence-window; size/overlap; metadata; makes-or-breaks retrieval. `T1` · src: Eden Marco, RAG-evals
- [ ] **Vector stores & similarity search** — Pinecone/FAISS/Chroma/pgvector; managed vs. local; top-k. `T1` · src: Eden Marco
- [ ] **pgvector vs. dedicated vector DB** — when each, why pgvector for his builds. `T1` · src: autoclip, CFO Agent
- [ ] **The RAG pipeline** — chunk→embed→search→(re-rank)→generate; which metric diagnoses which stage. `T1` · src: RAG-evals
- [ ] **Hybrid search & re-ranking** — dense+sparse/BM25; cross-encoder second pass; lifts precision. `T1` · src: RAG-evals
- [ ] **Query transformation** — multi-query, HyDE, decomposition for poor queries. `T2` · src: RAG-evals
- [ ] **Agentic / advanced RAG** — Corrective (CRAG), Self-RAG, Adaptive RAG; doc-relevance grading; web fallback. `T2` · src: Eden Marco

## Section 6 — MCP (Tier 1)

- [ ] **Why MCP exists** — the M×N → M+N integration problem; vs. function-calling/plugins. `T1` · src: MCP Masterclass
- [ ] **Host / client / server triad + two-layer model** — data layer (JSON-RPC) vs. transport layer; local vs. remote. `T1` · src: MCP spec
- [ ] **Lifecycle & capability negotiation** — `initialize` handshake, version negotiation, stateful sessions. `T1` · src: MCP spec
- [ ] **Server primitives** — tools (model-controlled), resources (app-controlled GET), prompts (user-controlled); schemas, annotations, `listChanged`. `T1` · src: MCP spec
- [ ] **Client primitives** — sampling, elicitation, roots, logging. `T2` · src: MCP spec ⚠ elicitation + sampling-with-tools are new
- [ ] **Transports** — STDIO vs. Streamable HTTP; session mgmt; security (Origin validation). `T1` · src: MCP spec ⚠ standalone SSE deprecated; batching removed
- [ ] **Building servers with FastMCP** — `@mcp.tool/resource/prompt`, the `Context` object, low-level vs. FastMCP. `T1` · src: MCP Masterclass, FastMCP docs
- [ ] **Building clients** — `ClientSession` lifecycle, discovery, wiring an LLM to MCP tools. `T1` · src: MCP Masterclass
- [ ] **MCP auth & security** — OAuth 2.1 Resource Server, Resource Indicators, confused-deputy/token-passthrough risks. `T2` · src: MCP spec ⚠ moved fast across 2025-06→11
- [ ] **MCP server vs. inline tools** — why a FastMCP server over in-process tools. `T1` · src: Cognizant FastMCP work

## Section 7 — Evals & Observability (Tier 1 — genuine gap, high value)

- [ ] **Why eval AI differs from QA** — non-deterministic outputs → assert on thresholds, not equality. `T1` · src: RAG-evals
- [ ] **LLM-as-judge** — when reliable (stronger judge), cost/opacity/verbosity bias; temp=0. `T1` · src: RAG-evals
- [ ] **Why eval before a model swap** — silent regressions; tool-calling differs across providers. `T1` · src: Judgment Log — deepen
- [ ] **RAGAS core metrics** — faithfulness, answer/response relevancy, context precision/recall; what each measures & diagnoses. `T1` · src: RAG-evals ⚠ collections API + renames
- [ ] **Golden datasets & synthetic test data** — curated eval sets; RAGAS `TestsetGenerator` (knowledge-graph based). `T2` · src: RAG-evals
- [ ] **Eval automation with pytest** — `assert score >= threshold`, fixtures, parametrize, CI gates. `T2` · src: RAG-evals
- [ ] **LangSmith tracing** — `@traceable`, run types, threads; what observability gives you. `T1` · src: LangChain Academy ⚠ `LANGSMITH_*` env vars
- [ ] **LangSmith evaluation** — datasets/examples, evaluators, `evaluate()`/`aevaluate()`, experiments, online eval. `T2` · src: LangChain Academy
- [ ] **Eval framework landscape** — RAGAS vs. DeepEval vs. TruLens; when each. `T2` · src: RAG-evals

## Section 8 — Async & Production Architecture (Tier 1/2)

- [ ] **Celery vs. FastAPI background tasks vs. asyncio** — why Celery for autoclip's pipeline. `T1` · src: autoclip
- [ ] **Structured logging** — JSON logs, request IDs, agent-step logging (structlog). `T2` · src: capstone
- [ ] **API-key auth on FastAPI** — `Depends()` middleware. `T2` · src: capstone

---

## Tier 2 — Periphery (pulled when a build needs them)

These mirror `career/concept_queue.md` Tier 2 — learn at decision-level (80/20), not internals.

- [ ] **Cloud/AWS** — Bedrock vs. SageMaker vs. roll-your-own · Lambda vs. FastAPI · IAM least privilege · S3 basics. `T2`
- [ ] **Security** — authn vs. authz · JWT + API keys · OWASP Top 10 (one sitting) · secrets mgmt · prompt-injection defense. `T2`
- [ ] **Infra & systems** — Docker / Compose · CI/CD · SQL vs. NoSQL vs. vector vs. Redis · caching · REST design · CAP/12-factor/scalability. `T2`

---

## Connections & Application

- The curriculum is the **acquisition** funnel; `concept_queue.md` is the **defense** funnel. A unit learned here becomes a concept to grill there. They share the CAREER_LOG as the mastery ledger.
- **Build before you bank** (CLAUDE.md): a unit isn't owned until code using it exists — work, autoclip, the dedicated capstone, or a throwaway script. The capstone (Master Guide Phase 2) is where these units compound into a portfolio piece.
- The Currency Watch is the live edge — re-research per unit; the whole point of in-house learning is never shipping a deprecated pattern.

## Honest Takeaways

*(fill as units land — what the live-research format gets right, where it falls short vs. a structured course)*

## Entry Log

*(links to `reflection_log/YYYY-MM-DD.md` per `/learn` session)*
