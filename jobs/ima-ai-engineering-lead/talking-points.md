# Talking Points — IMA AI Engineering Lead (Founding AI Engineer)

## "Why THIS over THAT" — decisions a founding eng in an MS shop will actually face

### LangGraph vs. Azure AI Foundry / Semantic Kernel — what transfers
- **What's the same:** the hard part of agent work is *architecture* — state, control flow, tool boundaries, when to loop vs. terminate, how to persist and recover. That's stack-agnostic. A LangGraph state machine maps conceptually onto Semantic Kernel planners/agents and Foundry's orchestration; the graph-of-nodes mental model carries over.
- **Why LangGraph today:** explicit, inspectable control flow and state — I can reason about exactly where an agent is and why. That transparency is what let me debug and harden CFO Agent (the production-complexity finance agent I'm standing up 0→1) and the multi-agent dev team.
- **Honest framing for IMA:** initial solutions are Microsoft-ecosystem, so I'd lead with Semantic Kernel / Azure AI Foundry + Azure OpenAI for the first capabilities to stay in the org's supported stack. My LangGraph experience means I already think in the primitives those tools expose — the ramp is API surface, not concepts.

### When a copilot vs. an autonomous agent
- **Copilot (human in the loop):** default for high-stakes or low-tolerance-for-error work — anything touching financials, compliance, client-facing output. The human stays the decision-maker; AI drafts, retrieves, suggests. Right first move for an insurance/finance org building trust in AI.
- **Autonomous agent (acts without approval per step):** justified only when the task is well-bounded, reversible or low-blast-radius, and the cost of a wrong action is low. My multi-agent dev team is autonomous because generated code is reviewable and cheap to throw away.
- **Rule of thumb I'd bring:** start copilots, earn autonomy with evidence. Ship the human-in-the-loop version first, measure, then remove the human only where the data says it's safe.

### Build vs. buy for a *first* AI capability
- **Buy / adopt the platform layer:** model hosting (Azure OpenAI), vector store, eval tooling, observability. No moat in rebuilding these; buying gets to value faster and keeps a solo founder from drowning in infra.
- **Build the org-specific glue:** the RAG over IMA's own data, the domain agents, the tool integrations (MCP-style connectors) to internal systems. That's where the differentiated value and the defensibility live — and it's exactly the MCP/RAG work I've done.
- **Why this split:** as a founding eng, my scarcest resource is my own time; spend it on what only an insider can build, buy everything commoditized.

### First 90 days as founding engineer (sequencing)
- **Days 0–30 — listen & land one win.** Map the real workflows, find the highest-pain / lowest-risk use case, ship one narrow copilot end-to-end on the sanctioned Azure stack. Prove the loop, build trust.
- **Days 30–60 — establish the platform spine.** Stand up the repeatable pieces: RAG over internal data, eval harness, observability, security/data-boundary guardrails. Make the second use case cheap.
- **Days 60–90 — templatize and show the roadmap.** Turn the spine into a pattern others can reuse, document how AI gets built/delivered here, and present a prioritized roadmap. This is where "founding builder" starts becoming "how the org does AI" — the earliest seed of the Lead mandate.

---

## Likely interview questions

### Q: "You're ~1 year in — why you as the Lead?"
**Honest answer skeleton:**
- Name it directly: "On tenure, I'm early — I won't pretend otherwise. So let me answer on what this role actually needs on day one."
- Pivot to scope: "What a founding role rewards is someone who can take an AI capability from zero without a template to copy. I've done that repeatedly and solo — CreatorClip, live in production; CFO Agent, a production-complexity finance agent I'm actively standing up 0→1; the multi-agent LangGraph dev team; custom MCP servers — owning the whole slice from architecture through to shipping and running it."
- Address the leadership piece honestly: "Founding is builder-first — the team comes after the first capability exists and proves value. I'm ready to be the person who builds that first thing and defines how it's done; I'd grow into people-leadership as the function grows, and I'd be straight with you about that arc."
- Close on trajectory: "The bet you'd be making is on demonstrated 0→1 velocity over years-on-paper. My track record is exactly that bet."

### Q: "Most of your agent work is Anthropic/AWS/LangGraph — how do you handle a Microsoft/Azure-first mandate?"
- AZ-900 certified, so the Azure fundamentals are in place.
- The agent architecture is stack-agnostic — I already think in the primitives Semantic Kernel and Azure AI Foundry expose; the delta is API surface, not concepts.
- Plan: lead first capabilities with Azure OpenAI + Semantic Kernel to stay in the supported stack, ramp depth on the job. Don't oversell — be explicit it's a fast ramp, not existing production depth.

### Q: "Walk me through a system you took from nothing to production."
- For a *shipped-and-running* system, lead with **CreatorClip / autoclip.studio** (live in production). For agent-architecture depth, use **CFO Agent** — the production-complexity finance agent I'm standing up 0→1 (in active development): the problem, why LangGraph for explicit state, the hybrid context architecture (auto aggregation + manual encrypted "vault"), why Redis caching + PostgreSQL persistence, and the multi-tenant productization decision. Show the *why* behind each choice, not just the stack list — and be clear which is deployed vs. in active development.

---

## The ONE project to demo: CFO Agent
- **Why this one:** it's a *0→1, productizable* agent in active development — the exact shape of a founding role's first deliverable. It shows full-stack agent ownership (LangGraph orchestration, FastAPI backend, PostgreSQL/Redis, an encrypted data vault with CSV/OFX import), real architectural judgment (hybrid context, multi-tenant design), and it's in the finance domain — directly relevant to an insurance/financial-services employer.
- **Why not the others:** the multi-agent dev team is impressive but R&D-flavored and less business-legible; autoclip is a great agentic-pipeline story but consumer/creator-domain and further from IMA's world. CFO Agent lands the founding-builder + finance-relevance message in one artifact.

---

## 30-second pitch for THIS role
> "I build production AI agents from zero — solo, end to end. I've shipped CreatorClip live to production, and I'm actively standing up a personal-finance agent on LangGraph 0→1; I've also built a multi-agent software-dev team on Bedrock and custom MCP servers that give agents live tool access — owning architecture through to shipping each time. This founding role is exactly that shape: build the first AI capabilities from the ground up and define how AI gets delivered across IMA. I'm early-career, so I'll be straight that the Lead title is a stretch on tenure — but founding roles reward demonstrated 0→1, and that's my whole track record. I'm AZ-900 certified and my agent architecture is stack-agnostic, so ramping into the Azure/Microsoft ecosystem is fast. I'd start with one high-value copilot, prove the loop, then build the platform spine behind it."
