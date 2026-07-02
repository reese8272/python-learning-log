# Talking Points — Genesys Sr. SWE, Full Stack (Agentic AI)

Framing for every answer: **CX / experience orchestration**. Genesys connects people, systems, data, and AI in real customer conversations. Tie agent-design decisions back to *the customer experience surface*, not just the model.

---

## "Why THIS over THAT" — the decisions that show judgment

### 1. Streaming vs. request/response for agent UX
- **THAT (request/response):** simplest — user waits, full answer returns. Fine for a batch tool.
- **THIS (streaming, for CX):** in a contact-center flow the agent's latency is *felt* by a live customer or a live human agent. Token streaming (SSE / WebSocket) keeps the experience responsive and lets a human interrupt or redirect mid-turn. For experience orchestration, perceived latency IS the product — stream by default, fall back to request/response only for internal/batch calls.
- **Why it matters here:** Genesys's whole value is the live experience. I'd argue streaming isn't a nice-to-have, it's a UX correctness requirement.

### 2. LangGraph state machine vs. ad-hoc orchestration for multi-turn CX flows
- **THAT (ad-hoc / prompt-chaining):** fast to prototype, but state lives implicitly in prompt history; hard to resume, branch, or audit. Breaks down when a conversation forks (escalate to human? route to billing? retry a tool?).
- **THIS (LangGraph explicit state machine):** nodes + edges + typed state make multi-turn CX flows inspectable and resumable. You can checkpoint a conversation, hand off to a human, and resume — which is exactly what contact-center escalation needs. Guardrails and routing become graph edges, not buried if-statements.
- **This is my real experience:** I built a multi-agent LangGraph system (codegen/testing/security/supervision) — the same supervisor + specialized-node pattern maps onto CX routing.

### 3. Where agent logic lives — frontend vs. backend
- **Frontend (React/TS):** rendering, streaming display, optimistic UI, capturing user intent. Keep it thin on logic.
- **Backend (FastAPI/Django):** the agent loop, tool calls, secrets, orchestration state, persistence. **All decision logic and tool access stays server-side** — never expose model keys or tool routing to the browser.
- **THIS over THAT:** put the *state machine* in the backend, the *experience* in the frontend, and a streaming contract between them. I've built exactly this split (React/TS front end + FastAPI/Django backend) — most AI candidates only have one side.

### 4. How MCP standardizes tool access across an orchestration platform
- **THAT (bespoke integrations):** every agent re-implements its own connectors to CRM, telephony, knowledge base — N agents × M systems glue code, brittle and duplicated.
- **THIS (MCP as the tool contract):** each system exposes one MCP server; any agent speaks the same protocol. On a platform connecting thousands of orgs' systems, MCP turns M×N into M+N and makes tool access governable and swappable.
- **My real work:** built custom FastMCP servers and integrated external MCP services with AWS for dynamic agent tool access — this is the standardization argument in practice.

---

## Likely interview questions + answer skeletons

**Q1: "This is a Sr role and you're ~1 year in. Make the case."**
- Don't argue years. Argue **surface area owned end-to-end**: shipped MCP servers into live client workflows, a full React+Django+PostgreSQL platform to a paying client, multi-agent LangGraph in enterprise R&D.
- "I've already operated across the whole stack a Genesys agent lives in — UI, API, orchestration, tools. The seniority gap I'd close fastest is domain and scale; the breadth is already here."
- Be honest, then pivot to the rare combination.

**Q2: "How would you design an agent that helps a live contact-center rep during a call?"**
- Clarify: real-time, human-in-the-loop, latency-sensitive.
- **Frontend:** streaming suggestions surfaced beside the call UI, non-blocking, rep stays in control.
- **Backend:** LangGraph flow — transcribe (WhisperX-style) → retrieve relevant KB/CRM context (RAG + pgvector) → propose next-best-action → log. Tools reached via MCP (CRM, KB, telephony).
- **State/ops:** checkpoint conversation state for resume/handoff; Redis for hot context; Postgres for persistence and audit.
- Close on tradeoffs: stream for perceived latency, keep the human as the decision-maker, keep the agent advisory in v1.

**Q3: "How do you keep a multi-agent system reliable / debuggable in production?"**
- Explicit state machine (LangGraph) so every transition is inspectable; typed state.
- Guardrails as graph edges (validation, human-escalation nodes), not scattered conditionals.
- Observability: log each node's input/output; checkpoint state; evaluate with a fixed test set (I've done prompt-eng + model evaluation).
- MCP contract isolates tool failures from agent logic.

---

## The ONE demo — recommend **CFO Agent**

**Pick CFO Agent over CreatorClip** for this role, because:
- It's the cleanest **full-stack + agent** story in a *conversational, multi-turn, live-data* shape — closest analog to a CX orchestration agent.
- FastAPI + **LangGraph** orchestration + **PostgreSQL persistence** + **Redis** hot context + **CSV/OFX import into an encrypted vault** for real external data + **multi-tenant-ready** — mirrors exactly the concerns a Genesys agent has (state, persistence, real system integration, multi-org). (It's in active development, a production-complexity build he's standing up 0→1 — frame it that way, not as deployed.)
- It lets you narrate every "why THIS over THAT" above with real code: where state lives, backend vs frontend split, streaming, tool access.
- *(CreatorClip is a stronger pure-pipeline/async-scale demo — hold it in reserve if they push on high-throughput data processing.)*

Have ready: the LangGraph state graph, the persistence/caching split, and how you'd expose the data layer (CSV/OFX import + encrypted vault) through an MCP-standardized tool layer.

---

## 30-second pitch
> I'm a full-stack engineer who builds agentic AI end-to-end — from a React/TypeScript UI, through a FastAPI or Django REST backend, down to LangGraph orchestration and the MCP tool layer agents call. At Cognizant I ship LangGraph multi-agent systems and production MCP integrations; freelance, I delivered a full React + Django + PostgreSQL platform to a live client. The reason this Genesys role fits is that it wants both halves — the agent depth and the full-stack build — and I own the whole surface an agent lives in, not just the model. That's the rare part, and it's exactly what experience orchestration needs.
