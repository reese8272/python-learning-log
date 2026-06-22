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

**Course-version context** (from Reese's actual enrolled syllabi):
- **Eden Marco is the re-recorded v1.0 version** and is *partly* currency-aware: lec 97 "Building Modern LLM Agents: From History to LangGraph v1.0" and lec 143 "Stop Writing Deprecated Code: LangChain's Official MCP Server" address the migrations directly. BUT it still teaches `AgentExecutor` *first* (lec 90 "Implementing ReAct AgentExecutor with LangGraph") before the v1.0 lecture — so learn `create_agent` as the real target and treat the AgentExecutor lectures as the "history" they're framed as.
- **MCP Masterclass [2025]** already covers Streamable HTTP and FastMCP-vs-lowlevel (matches current spec), so the SSE-transport worry is *less* applicable here — but it predates and omits **elicitation, tasks, structured tool output, and OAuth 2.1 auth**; pull those from the current spec.

Re-verify before each unit — these move fast.

---

## Section 1 — Foundations & Prompt/Context Engineering (Tier 1)

*Eden Marco lec 67–75 + Anthropic tutorials. The course teaches prompting late (after building); learn it first — everything downstream rests on it.*

- [ ] **What an LLM call actually is** — tokens, completions, context window; reason about cost/latency/failure modes. `T1` · src: Eden Marco lec 67 ("GIST of LLMs")
- [ ] **Anatomy of a prompt** — system/user/assistant turns, prompt composition, `max_tokens`. `T1` · src: Eden Marco lec 68, Anthropic Ch.1
- [ ] **Zero-shot, few-shot, role prompting** — steering by examples and persona; clear-and-direct. `T1` · src: Eden Marco lec 69–70, Anthropic
- [ ] **XML tagging & output-format control** — separate data from instructions; tell it what TO do. `T1` · src: Anthropic Ch.4–5
- [ ] **Chain-of-thought & ReAct prompting** — reason-then-answer; evidence-before-conclusions/quote-grounding. `T1` · src: Eden Marco lec 71–72, Anthropic ⚠ adaptive thinking now preferred over manual CoT
- [ ] **Context engineering** — curating the window deliberately; context-engineer a system prompt. `T1` · src: Eden Marco lec 74–75 (the 2026 framing)
- [ ] **Avoiding hallucinations** — give an "out", ground in sources, investigate-before-answering. `T1` · src: Anthropic Ch.8
- [ ] **Prompt patterns that changed in 2026** — prefill removed, structured outputs, adaptive thinking/effort, over-prompting backfire. `T1` · src: live docs ⚠ entirely post-dates the tutorials

## Section 2 — LangChain Core (Tier 1)

*Eden Marco lec 9–14, 158–164.*

- [ ] **Prompt templates, ChatModels, chains** — `ChatPromptTemplate`, `init_chat_model`; build a summarize chain. `T1` · src: Eden Marco lec 9–10
- [ ] **LCEL** — the pipe (`|`) composition: prompt → model → parser. `T1` · src: Eden Marco lec 9 ⚠ LCEL for pipelines, `create_agent` for agents
- [ ] **The messages model** — `System/Human/AIMessage`, `content_blocks`. `T1` · src: Eden Marco lec 159
- [ ] **Output parsers & structured output** — `StrOutputParser`, Pydantic parsing; typed results. `T1` · src: Eden Marco lec 22–23
- [ ] **Document loaders & text splitters** — ingest to `Document`; `RecursiveCharacterTextSplitter`, chunk size/overlap. `T1` · src: Eden Marco lec 160–161
- [ ] **Local & swappable models** — Ollama (open-weights) + provider switching (Groq); open-source vs. managed (Deepseek). `T2` · src: Eden Marco lec 12, 81, coding ex 1
- [ ] **Token-limit handling strategies** — trimming/summarization/co-reference resolution when context overflows. `T2` · src: Eden Marco lec 162–163
- [ ] **Legacy vs. v1 surface** — what moved to `langchain-classic`, why LCEL/`create_agent` replaced old chains. `T2` · src: live docs ⚠ the v1 migration itself

## Section 3 — Agents, From Scratch to `create_agent` (Tier 1)

*Eden Marco lec 15–41 — the course's strongest sequence: build agents WITHOUT abstractions first, then use the framework. Do it in that order; it's why you'll actually understand them.*

- [ ] **What an AI agent is + ReAct theory** — the gist of reason→act→observe. `T1` · src: Eden Marco lec 15, 26
- [ ] **First framework agent** — tools + LLM + Tavily search; how query→answer flows. `T1` · src: Eden Marco lec 19–21
- [ ] **Tool / function calling** — `@tool`, schemas, docstrings/type-hints as the agent-facing interface; tool binding & defensive prompting. `T1` · src: Eden Marco lec 28–30
- [ ] **Manual JSON schemas vs. the tool abstraction** — what the `@tool` decorator does for you. `T1` · src: Eden Marco lec 32
- [ ] **ReAct loop with the raw SDK** — build the loop against raw Ollama, no LangChain; demystifies "agent". `T1` · src: Eden Marco lec 33
- [ ] **Function calling from scratch** — dynamic tool descriptions, the ReAct prompt, manual tool calling without function-calling APIs. `T1` · src: Eden Marco lec 35–39
- [ ] **`create_agent` (v1)** — the current one-line agent on LangGraph: durable execution, streaming, checkpointing; `system_prompt`, middleware. `T1` · src: live docs ⚠ replaces the `AgentExecutor` the course teaches first (lec 90)
- [ ] **ReAct failure modes** — skips steps, declares done early, loops; how to constrain. `T1` · src: all agent work

## Section 4 — LangGraph (Tier 1)

*Eden Marco lec 85–124 + LangChain Academy.*

- [ ] **Why a graph over a ReAct loop** — guaranteed execution & control surface vs. an uncontrollable loop; flow engineering. `T1` · src: Eden Marco lec 86–88 *(already owned — 2026-06-22; deepen)*
- [ ] **`StateGraph`, state schema, reducers** — `TypedDict` channels, `Annotated` reducers, `add_messages`/`MessagesState`. `T1` · src: LangChain Academy ⚠ reducers are the most-misunderstood concept; `MessageGraph` removed
- [ ] **Nodes & edges** — node = partial-state update; deterministic vs. conditional edges; `START`/`END`. `T1` · src: Eden Marco lec 89, 94–95
- [ ] **The ReAct agent as a graph** — building the loop in LangGraph; AgentExecutor→v1.0 history. `T1` · src: Eden Marco lec 90–97 ⚠ lec 97 covers the v1.0 migration directly
- [ ] **Checkpointers & persistence** — save state per step under a thread; `InMemory`/`Sqlite`/`Postgres` savers; durability modes. `T1` · src: LangChain Academy ⚠ durability flag; shallow savers deprecated
- [ ] **Short- vs. long-term memory** — per-thread checkpointer vs. cross-thread `Store`; trimming/summarization. `T1` · src: Eden Marco lec 164, LangChain Academy
- [ ] **Human-in-the-loop** — `interrupt()` + `Command(resume=...)`; edit-state/approve patterns; time travel. `T1` · src: LangChain Academy ⚠ over static breakpoints/`NodeInterrupt`
- [ ] **Streaming modes** — `values`/`updates`/`messages`/custom for responsive UIs. `T2` · src: LangChain Academy
- [ ] **Parallelism & composition** — fan-out/fan-in, subgraphs, map-reduce via `Send`. `T1` · src: LangChain Academy
- [ ] **Reflection & Reflexion patterns** — generate→critique→revise; actor/revisor; learning from past attempts. `T1` · src: Eden Marco lec 98–110
- [ ] **Multi-agent topologies** — supervisor vs. swarm vs. single ReAct; handoff tools; when each. `T1` · src: LangChain Academy ⚠ supervisor/swarm are separate packages
- [ ] **LangGraph deployment** — Platform/Server, assistants, threads/runs, double-texting. `T2` · src: LangChain Academy

## Section 5 — RAG & Retrieval (Tier 1)

*Eden Marco lec 42–66, 111–124 + RAG-evals (reconstructed — no enrolled list available).*

- [ ] **What an embedding actually is** — vector space, dimensionality, similarity; same model indexes & queries. `T1` · src: Eden Marco lec 41, autoclip/CFO Agent
- [ ] **Embedding model choice** — why Voyage AI over OpenAI embeddings in autoclip. `T1` · src: autoclip
- [ ] **The RAG pipeline (naive → 2-step)** — TextLoader/Splitter/Embeddings/Pinecone; ingestion then retrieval; 2-step RAG. `T1` · src: Eden Marco lec 42–49
- [ ] **Chunking strategy** — fixed/recursive/semantic; size/overlap; metadata; makes-or-breaks retrieval. `T1` · src: Eden Marco lec 60, RAG-evals
- [ ] **Vector stores & similarity search** — Pinecone/FAISS/Chroma/pgvector; managed vs. local; batch indexing; top-k. `T1` · src: Eden Marco lec 45, 61
- [ ] **pgvector vs. dedicated vector DB** — when each, why pgvector for his builds. `T1` · src: autoclip, CFO Agent
- [ ] **Production RAG app** — crawling (Tavily Map/Extract), retrieval agent, Streamlit UI, going to production. `T2` · src: Eden Marco lec 51–65
- [ ] **Hybrid search & re-ranking** — dense+sparse/BM25; cross-encoder second pass; lifts precision. `T1` · src: RAG-evals
- [ ] **Agentic / advanced RAG** — Corrective (CRAG), Self-RAG, Adaptive RAG; relevance-grading node; web fallback. `T1` · src: Eden Marco lec 111–124

## Section 6 — MCP (Tier 1)

*MCP Masterclass (full enrolled list) + Eden Marco lec 125–146 + current spec.*

- [ ] **Why MCP exists** — the M×N → M+N integration problem; vs. function-calling/plugins. `T1` · src: MCP Masterclass, Eden Marco lec 125
- [ ] **MCP architecture** — host/client/server triad; data layer (JSON-RPC) vs. transport layer; how tool calling rides it. `T1` · src: MCP Masterclass, Eden Marco lec 127–128
- [ ] **Lifecycle & capability negotiation** — `initialize` handshake, version negotiation, stateful sessions. `T1` · src: current spec
- [ ] **Server primitives** — tools (model-controlled), resources (app-controlled GET, w/ inputs), prompts (user-controlled). `T1` · src: MCP Masterclass ("deep dives")
- [ ] **FastMCP vs. low-level server** — when each; `@mcp.tool/resource/prompt`, the `Context` object. `T1` · src: MCP Masterclass, FastMCP docs
- [ ] **Building servers** — simple servers, local files, API calls, complex inputs; build projects (memory tracker, chess stats). `T1` · src: MCP Masterclass
- [ ] **Building clients** — `ClientSession` lifecycle, list/call tools-resources-prompts, wire LLM↔servers, multi-server. `T1` · src: MCP Masterclass
- [ ] **Transports & deployment** — STDIO vs. Streamable HTTP; package & host a remote server (VM), connect via Inspector/client. `T1` · src: MCP Masterclass ⚠ standalone SSE deprecated; batching removed (course is current on Streamable HTTP)
- [ ] **LangChain MCP integration** — MCP adapter, the official LangChain MCP server. `T1` · src: Eden Marco lec 139, 143 (lec 143 = "stop writing deprecated code")
- [ ] **MCP client primitives** — sampling, elicitation, roots, logging. `T2` · src: current spec ⚠ elicitation + sampling-with-tools post-date the [2025] course
- [ ] **MCP auth & security** — OAuth 2.1 Resource Server, Resource Indicators, confused-deputy/token-passthrough. `T2` · src: current spec ⚠ not in the course; moved fast across 2025-06→11
- [ ] **Tasks (durable execution)** — long-running tool ops with status polling. `T2` · src: current spec ⚠ 2025-11-25 addition, not in course
- [ ] **MCP server vs. inline tools** — why a FastMCP server over in-process tools. `T1` · src: Cognizant FastMCP work

## Section 7 — Deep Agents & Agent Skills (Tier 1 — cutting-edge, 2026)

*Eden Marco lec 147–157. None of this was in the reconstructed curriculum — it's the newest, most consulting-relevant material, and it maps directly onto how this very catalog's skills work.*

- [ ] **Agent taxonomy** — shallow vs. deep vs. coding agents; what makes an agent "deep". `T1` · src: Eden Marco lec 148
- [ ] **Dynamic to-do lists** — how deep agents decompose and track complex tasks. `T1` · src: Eden Marco lec 149
- [ ] **Sub-agents & hierarchical delegation** — spawning sub-agents, how context flows to/from them. `T1` · src: Eden Marco lec 150–151
- [ ] **Agent file systems** — giving an agent a workspace; why it matters for long tasks. `T1` · src: Eden Marco lec 152
- [ ] **Agent Skills — the 3 layers** — usage → middleware → source; progressive disclosure (`skills.py`). `T1` · src: Eden Marco lec 153–157 *(meta: this is how `/learn`, `/sharpen` etc. work)*

## Section 8 — Evals & Observability (Tier 1 — genuine gap, high value)

*RAG-evals (reconstructed) + LangChain Academy LangSmith + Eden Marco lec 167.*

- [ ] **Why eval AI differs from QA** — non-deterministic outputs → assert on thresholds, not equality. `T1` · src: RAG-evals
- [ ] **LLM-as-judge** — when reliable (stronger judge), cost/opacity/verbosity bias; temp=0. `T1` · src: RAG-evals
- [ ] **Why eval before a model swap** — silent regressions; tool-calling differs across providers. `T1` · src: Judgment Log — deepen
- [ ] **RAGAS core metrics** — faithfulness, answer/response relevancy, context precision/recall; what each measures & diagnoses. `T1` · src: RAG-evals ⚠ collections API + renames
- [ ] **Golden datasets & synthetic test data** — curated eval sets; RAGAS `TestsetGenerator` (knowledge-graph based). `T2` · src: RAG-evals
- [ ] **Eval automation with pytest** — `assert score >= threshold`, fixtures, parametrize, CI gates. `T2` · src: RAG-evals
- [ ] **Lean AI feedback loop** — building the eval/feedback loop into a real app. `T2` · src: Eden Marco lec 167
- [ ] **LangSmith tracing** — `@traceable`, run types, threads; what observability gives you. `T1` · src: LangChain Academy, Eden Marco lec 13, 102 ⚠ `LANGSMITH_*` env vars
- [ ] **LangSmith evaluation** — datasets/examples, evaluators, `evaluate()`/`aevaluate()`, experiments, online eval. `T2` · src: LangChain Academy
- [ ] **Eval framework landscape** — RAGAS vs. DeepEval vs. TruLens; when each. `T2` · src: RAG-evals

## Section 9 — LLM Application Security (Tier 1 — distinct from generic OWASP)

*Eden Marco lec 169–178. This is agent-specific security — where AI-generated code reliably fails — and it's high consulting value. Promoted to Tier 1 from the old generic periphery.*

- [ ] **What is LLM AppSec** — the threat surface of LLM/agent apps vs. traditional apps. `T1` · src: Eden Marco lec 172
- [ ] **Where AI coding agents fail** — RBAC, business logic, SSRF, rate limiting, CSRF (and why they're fine at SQLi/XSS). `T1` · src: Eden Marco lec 174–177
- [ ] **"Prompt engineering won't fix insecure code"** — why guardrails ≠ secure code; the real fix. `T1` · src: Eden Marco lec 178
- [ ] **Prompt-injection defense** — pre/post hooks as guardrails. `T2` · src: autoclip hooks (partly owned)
- [ ] **Agents in CTF / offensive context** — how agents are used in security competitions. `T2` · src: Eden Marco lec 169

## Section 10 — Production Reliability & Harness Engineering (Tier 1/2)

*Eden Marco lec 165–171 + autoclip/capstone.*

- [ ] **Core architecture of production-grade AI** — what separates a demo from a deployed system. `T1` · src: Eden Marco lec 165
- [ ] **Managing variance & hallucinations in production** — making outputs reliable enough to ship. `T1` · src: Eden Marco lec 171
- [ ] **Harness engineering** — the scaffolding around the model that makes agents work. `T1` · src: Eden Marco lec 170
- [ ] **Making users trust AI agents** — UX/transparency patterns for adoption. `T2` · src: Eden Marco lec 166
- [ ] **Celery vs. FastAPI background tasks vs. asyncio** — why Celery for autoclip's pipeline. `T1` · src: autoclip
- [ ] **Structured logging & API-key auth** — JSON logs/request IDs (structlog); FastAPI `Depends()` auth. `T2` · src: capstone

## Section 11 — Engineering Judgment & Decision Frameworks (Tier 1 — the consultant's edge)

*Not taught well by any single course — which is the whole reason to build it here, researched live. These are the THIS-over-THAT calls that separate an engineer who can build from a consultant who can advise. Directly serves the mastery standard: "can I explain why THIS over THAT?"*

- [ ] **Workflow vs. agent — do you even need an agent?** — deterministic chains/workflows vs. autonomous agents; the cost of agency (latency, unpredictability, debugging). Default to the simplest thing that works. `T1` · src: Anthropic "Building Effective Agents" + live research
- [ ] **Prompt vs. RAG vs. fine-tune vs. agentic** — the capability decision tree: which lever for which problem, and why fine-tuning is rarely the first answer. `T1` · src: live research
- [ ] **Model & provider selection** — which model/provider for which job; cost/latency/capability tradeoffs; when local vs. managed. `T1` · src: Eden Marco lec 25, 81 + live research
- [ ] **Build vs. buy & framework selection** — LangGraph vs. alternatives vs. rolling your own; when a framework earns its complexity. `T1` · src: Eden Marco lec 86, 146 + live research

## Section 12 — How LLMs Actually Work (Tier 2 — awareness)

*Awareness-level only — enough to reason about why models behave, cost, and break the way they do, and to sound credible with a technical client. NOT deep ML theory. Maps to the Master Guide's "Must-Read AI Papers" — `/learn` can teach a paper's core idea without you reading the whole thing. Pull these between build sections, one at a time.*

- [ ] **Transformer & attention, at altitude** — next-token prediction, what "attention" buys you, why context is the unit of work. The mental model under everything. `T2` · src: live research (foundational)
- [ ] **Mixture of Experts (MoE)** — sparse activation: big capacity, cheaper inference; why frontier models use it. `T2` · src: Mixtral paper
- [ ] **Long-context mechanics** — how million-token windows are achieved; what degrades at length (lost-in-the-middle). Directly informs RAG vs. long-context calls. `T2` · src: Gemini 1.5 paper
- [ ] **Data quality > model size** — why a small, well-trained model can rival a big one. Informs model selection. `T2` · src: Phi-3 paper
- [ ] **The open-weight landscape** — Llama 3 / Qwen2 / Gemma / DeepSeek-Coder: what the frontier looks like beyond Anthropic/OpenAI; when open-weights make sense. `T2` · src: those papers + live research
- [ ] **Post-transformer architectures (awareness)** — state-space models (Mamba) and KANs as challengers; know they exist, not the math. `T2` · src: Vision Mamba / KAN papers
- [ ] **Why models hallucinate & vary** — the mechanistic "why" behind the reliability work in §10; connects internals to production behavior. `T2` · src: live research

---

## Tier 2 — Periphery (pulled when a build needs them)

Decision-level (80/20), not internals. Security moved up to Section 9 (it earned Tier 1).

- [ ] **Cloud/AWS** — Bedrock vs. SageMaker vs. roll-your-own · Lambda vs. FastAPI · IAM least privilege · S3 basics. `T2`
- [ ] **Auth & secrets** — authn vs. authz · JWT + API keys · OWASP Top 10 (one sitting) · secrets mgmt. `T2`
- [ ] **Infra & systems** — Docker / Compose · CI/CD · SQL vs. NoSQL vs. vector vs. Redis · caching · REST design · CAP/12-factor/scalability. `T2`
- [ ] **Ecosystem judgment** — LangChain vs. LlamaIndex · Generative UI (CopilotKit) · LLM privacy & data retention. `T2` · src: Eden Marco lec 78–79, 146

---

## Connections & Application

- The curriculum is the **acquisition** funnel; `concept_queue.md` is the **defense** funnel. A unit learned here becomes a concept to grill there. They share the CAREER_LOG as the mastery ledger.
- **Build before you bank** (CLAUDE.md): a unit isn't owned until code using it exists — work, autoclip, the dedicated capstone, or a throwaway script. The capstone (Master Guide Phase 2) is where these units compound into a portfolio piece.
- The Currency Watch is the live edge — re-research per unit; the whole point of in-house learning is never shipping a deprecated pattern.

## Honest Takeaways

*(fill as units land — what the live-research format gets right, where it falls short vs. a structured course)*

## Entry Log

*(links to `reflection_log/YYYY-MM-DD.md` per `/learn` session)*
