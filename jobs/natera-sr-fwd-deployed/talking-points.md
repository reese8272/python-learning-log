# Talking Points — Natera Sr Forward Deployed AI Solutions Engineer

## "Why THIS over THAT" Decision Points
Anchored to the JD: embed in a domain, find a workflow, build an agent/integration, deploy and run it.

### 1. LangGraph (stateful graph) over raw function-calling loops — for multi-step agents
- **THAT (raw loop):** a while-loop around a model with tools is fine for a single tool call or two.
- **THIS (LangGraph):** the moment a workflow has branches, retries, human-in-the-loop checkpoints, or needs to resume after failure, you want explicit state and a graph you can inspect. In CFO Agent I used LangGraph so the agent's reasoning steps over financial data were persistent and re-entrant, not a black-box loop.
- **Forward-deployed relevance:** embedded systems have to *keep running* and be debuggable in production. A graph you can trace beats a loop you have to guess about.

### 2. An agent + integration over a plain script — for a 10–100x workflow
- **THAT (script):** if the workflow is deterministic, high-volume, and never varies, a script or cron job is cheaper and more reliable. Don't reach for an agent to do a regex's job.
- **THIS (agent):** reach for an agent when the workflow needs judgment on messy/unstructured input, branches based on content, or spans several tools/systems. CreatorClip needs an agent because "what makes a good clip for *this* creator" is a judgment call, not a rule.
- **The honest tell:** I ask "would a junior teammate need to think, or just follow steps?" Thinking → agent. Steps → script. This restraint is itself a forward-deployed skill: shipping the boring solution when it wins.

### 3. pgvector over a hosted vector DB (Pinecone/Weaviate) — for embedded/early systems
- **THAT (hosted):** worth it at very large scale, or when you need managed sharding/replication and don't already run Postgres.
- **THIS (pgvector):** if the data already lives in Postgres — as it does in CreatorClip and CFO Agent — pgvector keeps embeddings *next to* the relational data, one backup story, one connection, no extra vendor and no cross-store consistency problem. For a forward-deployed system embedded in one domain's data, fewer moving parts wins.

### 4. MCP over bespoke per-tool APIs — for giving agents tool access
- **THAT (bespoke):** hand-rolling a tool wrapper is fine for one-off, single-agent tools.
- **THIS (MCP/FastMCP):** MCP gives a standard interface so tools are reusable across agents/clients and don't get re-glued every time. I deployed FastMCP servers at Cognizant so enterprise tools plugged into agents in a modular way instead of bespoke integrations per project. For an org standing up many embedded workflows, a standard tool layer compounds.

## Likely Interview Questions + Answer Skeletons

### Q1: "Walk me through a time you deployed something into production and had to keep it running."
- **Skeleton:** Pick CreatorClip. (1) The workflow it replaces (manual clip editing). (2) The architecture and the *hard* part — async orchestration with Celery so a long WhisperX transcription doesn't block, plus real YouTube OAuth. (3) What broke in production and how I handled it (failure/retry in the pipeline). (4) That it's live at autoclip.studio. End on: "It's not a demo — it runs."

### Q2: "You'd be embedding in a domain like Clinical or Lab Ops with no healthcare background. How do you ramp?"
- **Skeleton:** Name it honestly — no healthcare yet. Then: my whole track record is ramping into domains I didn't start in (WorldCovers = philatelic cataloging I knew nothing about, shipped features fast by sitting with stakeholders). Method: shadow the humans doing the workflow, find the highest-friction repetitive step, ship a thin automation, iterate with them. I've handled sensitive data (financial, in CFO Agent), so regulated-data discipline transfers; the domain is what I'd learn, and learning someone else's domain fast is the job.

### Q3: "How do you decide a workflow is worth automating vs. leaving alone?"
- **Skeleton:** Frequency × pain × variability. High-frequency + painful + *some* judgment = the sweet spot for an agent. Pure-deterministic → script. Low-frequency → probably leave it. I'd spend the first week measuring, not building — the forward-deployed mistake is automating the wrong thing beautifully.

## The ONE Project To Demo
**Demo CreatorClip (autoclip.studio).** Justification:
- It's **live and running** — the single strongest proof of "build, deploy, AND run," which is exactly this role's bar.
- It's **integration- and automation-heavy** (Celery, WhisperX, pgvector, YouTube OAuth) — it *looks like* the kind of embedded workflow-automation this role builds.
- It's **his own end-to-end system** — no ambiguity about what he personally did.
- Keep **CFO Agent as the backup demo** if the interviewer leans toward agent reasoning / sensitive-data handling (its encrypted vault + CSV/OFX import + sensitive financial data is the better story for the healthcare-data conversation). Frame it honestly as in active development — a production-complexity build he's standing up 0→1 — not a deployed system.

## 30-Second Positioning Pitch (for THIS role)
> "I'm an AI engineer whose whole thing is building agent systems and actually running them in production — not prototypes. My clearest proof is CreatorClip, a live async pipeline at autoclip.studio that automates short-form video from long-form content. I'm also standing up CFO Agent 0→1 — a LangGraph finance agent with an encrypted data vault and CSV/OFX import, a production-complexity build in active development. At Cognizant I deploy MCP servers and multi-agent LangGraph systems, and as a freelance contractor I deliver client-facing work under tight timelines with non-technical stakeholders. That last part is really what this role is — embed in a domain, find the workflow that could run 10–100x more often, and build and run the thing that does it. I'm applying at Senior because I lead with running systems, not tenure."
