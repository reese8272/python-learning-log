# Talking Points — Applied AI / AI Backend Engineer

> The end client is undisclosed (recruiter-fronted), so prep is **generic-but-solid**: know the production LLM-backend fundamentals cold and anchor every answer in your own shipped work.

---

## "Why THIS over THAT" — the decision rationale (the bar)

### Async (Celery) over synchronous request handling for LLM/media work
- **Why:** LLM inference, transcription, and embedding are slow and variable. Running them inline blocks the request thread and blows up p95 latency. Pushing them to Celery workers keeps the API responsive and lets heavy steps scale independently.
- **Your evidence:** CreatorClip's entire pipeline is Celery-backed and off the request path.
- **The tradeoff:** async adds complexity (queue, workers, result polling/webhooks, eventual consistency). Worth it when work is long-running or bursty; overkill for a sub-second call you can just await.

### Redis caching to cut token cost and latency
- **Why:** LLM calls cost money and time per token. Caching deterministic or repeat results (embeddings, prior agent context, repeated prompts) avoids paying twice for the same answer.
- **Your evidence:** CFO Agent uses Redis on the agent's hot paths.
- **The tradeoff:** caching only helps where inputs repeat and staleness is acceptable. Cache key design and TTL matter; don't cache user-specific or fast-changing data blindly.

### When to stream vs. return whole
- **Stream** when a human is watching output land (chat, generated prose) — it cuts *perceived* latency dramatically even if total time is unchanged.
- **Don't stream** when the consumer is another system that needs the whole structured result (tool output, JSON you'll parse, a downstream automation step) — streaming just adds parsing headaches.

### Model routing for cost
- **Why:** not every call needs the biggest model. Route simple classification/extraction to a cheaper/faster model and reserve the expensive one for hard reasoning. Cost and latency drop without hurting quality where it matters.
- **The tradeoff:** routing adds a decision layer and a failure mode (mis-routing). Start simple; add routing when a cost or latency ceiling forces it.

### Reliability patterns for flaky LLM calls
- **Retries with backoff** for transient errors/rate limits.
- **Timeouts** so one hung call doesn't stall the pipeline.
- **Fallbacks** — degrade to a smaller model, a cached answer, or a graceful error rather than failing hard.
- **Idempotency** on retried work so you don't double-charge tokens or double-process.

---

## Likely interview questions + skeletons

**Q1. "How do you keep an LLM-backed API responsive under load?"**
- Skeleton: move slow/variable work off the request path (Celery workers) → return fast with a job handle → deliver results via polling/webhook/stream. Cache repeat results in Redis. Set timeouts so no single call stalls the system. Anchor in CreatorClip.

**Q2. "How do you control cost in a production LLM system?"**
- Skeleton: three levers — (1) don't recompute (Redis caching of embeddings/repeat results), (2) don't over-spend per call (model routing: cheap model for easy tasks, expensive for hard), (3) don't waste tokens (tight prompts, trimmed context, the hybrid context arch in CFO Agent). Measure cost per request before optimizing.

**Q3. "How do you make agent/LLM behavior reliable when the model is non-deterministic and calls can fail?"**
- Skeleton: retries+backoff and timeouts at the call boundary; fallbacks (smaller model / cached / graceful error); validate structured output before trusting it; idempotent retried steps. In a multi-agent LangGraph system, a supervision node catches and re-routes failures — cite the Agentic Software Development Team's supervision agent.

---

## The ONE demo — CreatorClip / autoclip.studio

**Why this one:** it's the tightest match to the JD's "latency, correctness, reliability, and cost" framing. It's a real, end-to-end async pipeline (Celery) with genuine cost/latency-aware design (heavy model + media steps decoupled and queued), plus retrieval (Voyage + pgvector) and a real integration (YouTube OAuth). It shows you can turn model capability into product behavior at the system level — exactly the role. CFO Agent is the strong backup (orchestration + Redis caching + multi-tenant) if they lean more "backend/decisioning."

---

## 30-second pitch

"I'm an applied-AI / backend engineer — I build the systems that turn a model into reliable product behavior. At Cognizant I ship GenAI and agentic systems with LangGraph and custom MCP servers. On my own projects, CreatorClip is an async Celery AI video pipeline where the heavy transcription and embedding work runs off the request path so the API stays fast, and my CFO Agent uses LangGraph orchestration with Redis caching to keep token cost and latency down. I care about the unglamorous production parts — latency, cost, and making flaky LLM calls dependable with retries, timeouts, and fallbacks. That's the whole job in these two postings, which is why I applied to both."
