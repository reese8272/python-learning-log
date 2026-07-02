# Talking Points — Senior AI/ML Engineer (MCP)

Everything here is anchored to the three JD pillars: **MCP tooling**, **creative understanding**, and **evaluation**. Frame answers as "why THIS over THAT" — decision rationale is the bar.

---

## Why THIS over THAT (decision anchors)

### MCP server vs. a bespoke REST tool API for exposing capabilities
- **Why MCP:** the JD wants capabilities exposed to **both internal and external services**. An MCP server gives you one standardized, self-describing tool interface that any MCP-aware agent/client can discover and call — you publish the capability once instead of hand-rolling a REST contract, client SDKs, and glue per consumer.
- **When a plain REST API still wins:** deterministic, high-throughput service-to-service calls where no LLM/agent is in the loop and you don't need dynamic discovery. MCP earns its keep specifically when *agents* need dynamic tool access — which is the whole point of a "creative understanding" capability layer.
- **Proof:** built FastMCP servers + external MCP integrations at Cognizant to give agents exactly this kind of dynamic tool access.

### Designing an eval harness for a *subjective* signal ("creative quality")
This is the honest stretch area — answer it as a design, not a claim of a finished platform:
- **Ground truth first:** you can't score "quality" in the abstract. Anchor it to a measurable proxy — actual creative *performance data* (engagement/conversion) and/or human-labeled preference sets. That converts a subjective signal into a supervised target.
- **Datasets:** curate a held-out, versioned dataset of creatives + outcomes; keep a golden set that never changes so scores are comparable over time.
- **Scoring:** separate *capability metrics* (does the model extract the right creative attributes?) from *outcome correlation* (do our scores predict performance?). Report both.
- **Regression tests:** every model/prompt change runs against the golden set; alert on metric drift beyond a threshold. Treat prompt/model changes like code changes.
- **Dashboards:** track score distributions, correlation-to-performance, and per-segment breakdowns so stakeholders see quality trends, not just point numbers.
- **Honest framing:** "I've built model-evaluation and scoring loops and a semantic-clustering insights engine with executive reporting; I'd formalize the regression-suite + dashboard layer here — that's the piece I'd be building up, and I know the shape of it."

### Embeddings for multimodal creative data — Voyage AI + pgvector vs. alternatives
- **Why Voyage:** strong retrieval quality without running your own embedding infra; already validated it in CreatorClip.
- **Why pgvector over a dedicated vector DB (Pinecone/Weaviate):** if the data already lives in Postgres, pgvector keeps embeddings *next to* the relational creative/performance metadata — you can filter by campaign, brand, or performance metric and do vector search in one query, one system to operate. Reach for a dedicated vector store only at a scale/latency where Postgres genuinely strains.
- **Multimodal note:** transcript/text embeddings capture a lot of creative signal cheaply; you layer in visual/frame features when the question demands it. Start with the cheap signal that already correlates.

### Agentic workflow design over footage + performance data
- **Why an agentic/LangGraph workflow over a single monolithic prompt:** the task is multi-step and heterogeneous — ingest footage, transcribe, extract creative attributes, join to performance data, reason about *why* it worked. Modeling that as explicit graph nodes gives you inspectable state, retries per stage, and the ability to swap/evaluate one node without rerunning everything. A single mega-prompt is a black box you can't evaluate stage-by-stage.
- **Proof:** LangGraph multi-agent systems with dedicated evaluation/security nodes (Cognizant R&D), CFO Agent's hybrid-context LangGraph service.

### The CreatorClip "DNA" module as a creative-scoring analog
- It learns a creator's channel style from their existing content and **scores new segments against that learned style** — i.e. it already answers "does this fit / how strong is this creative signal?" That is the same problem shape as scoring why an ad creative works; the target changes (performance instead of channel-fit), the machinery is the same.

---

## Likely interview questions + skeletons

**Q1 — "Walk me through building and owning an MCP server for a creative-understanding capability."**
- Skeleton: capability boundary (what tool(s) to expose) → schema/tool definitions so any MCP client can discover them → auth/tenancy for internal vs external consumers → the underlying pipeline (embed + score) behind the tool → versioning + observability so you can *own* it over time. Ground it in the FastMCP work at Cognizant.

**Q2 — "How would you build an evaluation system to know our creative-quality scores are actually good?"** *(his lighter area — answer honestly + credibly)*
- Skeleton: use the design above (ground truth via performance data + human labels → versioned golden dataset → capability vs. outcome-correlation metrics → regression on every change → dashboards). Lead with what he's done (model eval, Call-Data insights engine, evaluation agents), be explicit about what he'd be *building up* (formal regression/dashboard tooling). Confidence + honesty beats bluffing here.

**Q3 — "You're ~1yr in for a senior role — why you?"**
- Skeleton: don't argue the title, argue the artifacts. "Two things most candidates at any level haven't shipped: production MCP servers, and a from-scratch video-understanding-and-scoring pipeline. Both are the core of this role. I've done the exact work, not adjacent work." Then point at autoclip.studio + the MCP work.

---

## The ONE demo — CreatorClip / autoclip.studio
- **Why this one:** it's a single artifact that hits *three* JD pillars at once — footage ingestion + creative understanding (WhisperX → embeddings), a learned **scoring** module ("DNA"), and a real async production pipeline (Celery/FastAPI/pgvector). Nothing else in the portfolio maps as directly to a creative-data company's product.
- **How to show it:** live at https://autoclip.studio, code at https://github.com/reese8272. Walk the flow footage → transcript → embeddings (Voyage/pgvector) → DNA scoring → render, then say one sentence connecting each stage to the JD.

---

## 30-second pitch (tuned to a creative-data company)
> "I'm an AI engineer who does two rare things: I build and own production MCP servers, and I've shipped a video-understanding pipeline that turns footage into embeddings and a learned scoring module. At Cognizant I built FastMCP servers and external MCP integrations on AWS to give agents dynamic tool access; on my own I built autoclip.studio, which transcribes video, embeds it with Voyage AI and pgvector, and scores content against a creator's learned style. That's basically your job description — expose creative-understanding capabilities through MCP, score them, and wrap them in agentic workflows. I'd love to do it on real creative-performance data."
