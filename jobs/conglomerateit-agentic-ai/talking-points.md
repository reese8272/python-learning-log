# Talking Points — ConglomerateIT Agentic AI Engineer

Anchored to **production agent engineering** and the "why THIS over THAT" bar. Every point below traces to real shipped work.

---

## "Why THIS over THAT" — core defenses

**LangGraph state machine vs. a ReAct-only loop.**
A bare ReAct loop reasons and acts in one undifferentiated stream — fine for a demo, brittle in production because you can't inspect or constrain where it is. A LangGraph state machine makes the agent's steps explicit nodes with typed state and controlled transitions, so you can gate a step, retry a single node, add a supervision checkpoint, and reason about failure. That's exactly how the multi-agent build system routes between codegen / testing / security / supervision agents. THIS over THAT when reliability and multi-step control matter more than raw speed of prototyping.

**Agent memory: Redis vs. a vector store — short vs. long term.**
Two different jobs. **Redis** holds short-term working state — the current run's context, recent tool results, session scratch — fast, ephemeral, cheap to read every step. That's the CFO Agent's Redis layer. **Durable/structured state** (transactions, entities, tenant data) lives in **PostgreSQL** for correctness and queryability. A **vector store (pgvector)** is for semantic recall over large unstructured history — used in autoclip's embedding retrieval, not for hot per-step state. Rule of thumb: Redis for "what just happened," Postgres for "what's true," vector store for "what's relevant." Don't reach for a vector DB when a key-value cache is the right tool.

**Tool/function calling via MCP vs. hardcoded tools.**
Hardcoding tools into the agent couples the agent to every integration and means a redeploy per tool change. **MCP servers** expose tools over a standard protocol, so agents get *dynamic* tool access at runtime and tools are reusable across agents and clients. On a consulting bench that's decisive — you add a client's tool surface without rewriting the agent. That's the FastMCP + external-MCP work at Cognizant.

**Guardrails / supervision in production.**
A supervision agent reviews or gates other agents' output before it's committed — in the build system, that's the layer catching bad codegen or security issues before they land. In production it's the difference between "agent did something" and "agent did something *we allowed*." Pair it with structured output validation and step-level checkpoints.

**Agent failure / retries.**
Because steps are discrete LangGraph nodes, a failed tool call retries at the node — with backoff and a capped attempt count — rather than restarting the whole reasoning chain. Idempotent tool design + persisted state means a mid-run failure resumes instead of redoing side effects. This is a production concern a prototype never has to answer, and it's a strong differentiator to raise unprompted.

---

## Likely interview questions + skeletons

**Q1. "Tell me about an agent you shipped to production — what made it production, not a prototype?"**
CFO Agent — a production-complexity agent I'm standing up 0→1 (in active development, not yet deployed). Full agent loop on FastAPI + LangGraph. What makes it production-*grade* by design rather than a prototype: durable state in PostgreSQL (survives restarts), Redis for hot working memory, real imported data via CSV/OFX import into an encrypted vault, multi-tenant-ready design, and failure handling at the node level. A prototype answers the happy path; this is built to answer persistence, tenancy, and recovery. (For a system that's actually *shipped and running*, I point to CreatorClip / autoclip.studio, live in production.)

**Q2. "How do you keep a multi-step agent reliable when any step can fail or hallucinate?"**
Explicit state machine (LangGraph) so steps are inspectable and independently retryable → structured/validated tool outputs → a supervision checkpoint before consequential actions → capped retries with backoff on idempotent tools → persisted state so a failure resumes rather than restarts. Cite the supervision agent in the build system as the concrete guardrail.

**Q3. "How do you design agent memory?"**
Split by job: short-term working state in Redis, durable/structured truth in PostgreSQL, semantic recall via pgvector when history is large and unstructured. Match store to access pattern and lifetime; don't default to a vector DB for everything. Point to CFO Agent's hybrid-context architecture.

---

## The ONE demo — recommendation

**Lead with the Agentic Software Development Team (multi-agent LangGraph).**
It's the strongest single showcase of the exact JD language: planning loops, multi-step reasoning, tool-calling, and — uniquely — a **supervision** agent, which is what separates "shipped to production" from "ran once." It shows agent *orchestration*, which is the bench's whole value proposition.

**Have CFO Agent as the backup / second demo** — it's the cleaner story for *agent memory* and *owning the full loop end to end*. If the interviewer probes persistence/state, pivot to CFO Agent. Between them you cover orchestration + memory, the two things this role cares about most.

---

## Client-adaptability note (consulting bench)

The end client is unknown, so lead with *how fast you ramp*, not domain depth. Concrete framing: "I've delivered cross-functionally at Cognizant and directly for a freelance client (WorldCovers) on compressed timelines — I'm used to scoping into an unfamiliar domain and shipping. MCP-based tool access is literally built for this: I plug a client's tools into the agent without rewriting it." That turns the bench's ambiguity into a strength.

---

## 30-second pitch

"I'm an agentic AI engineer who ships agents to production and owns the loop end to end. In the last year I've built a multi-agent LangGraph system with a supervision agent that automates the software build lifecycle, production MCP servers that give agents dynamic tool access, a live agent product — CreatorClip / autoclip.studio — running in production, and CFO Agent, a production-complexity finance agent I'm standing up 0→1 with real short- and long-term memory. I think in state machines and guardrails, not one-off ReAct loops, and I'm equally comfortable on full-time or contract. I'm exactly the profile you're building the bench with."
