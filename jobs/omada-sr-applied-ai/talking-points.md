# Talking Points — Omada, Senior Applied AI Engineer

## "Why THIS over THAT" — applied AI at scale

**RAG vs. fine-tuning for a care-guidance use case**
Default to RAG. Care guidance changes (new protocols, updated clinical content) and must be traceable to a source — RAG lets you swap the knowledge base without retraining and cite what the model used, which matters in a health context. Fine-tuning bakes knowledge into weights: expensive to update, hard to audit, and a compliance liability when guidance shifts. Reserve fine-tuning for *behavior/format* shaping (tone, structured output), not for facts. THIS (retrieval) over THAT (fine-tuning) = freshness + auditability + lower change cost.

**Managed vs. self-hosted embeddings**
Start managed (e.g. Voyage, as in CreatorClip) — you get quality and zero ops while validating the product. Move to self-hosted only when volume makes per-call cost dominate, or when data-residency/PHI rules forbid sending text to a third party. In a health company the residency question can force self-hosting earlier than cost would — so the real decision driver is often compliance, not price. Name that tradeoff explicitly; it signals you think past the happy path.

**Latency / cost tradeoffs at scale**
Lever order: (1) cache aggressively — Redis for repeated context, as in CFO Agent; (2) right-size the model per step — small/cheap model for routing and extraction, large model only for the reasoning that needs it; (3) batch and go async — Celery workers so user-facing latency isn't tied to pipeline depth (the CreatorClip pattern). "Use the biggest model everywhere" is the naive default; tiered routing is the scale answer.

**Eval strategy for LLM outputs in a regulated / health context**
Layered: (1) offline eval set of representative inputs with expected properties, run on every prompt/model change; (2) LLM-as-judge for fuzzy quality at volume, but calibrated against human-labeled samples so you trust the judge; (3) hard guardrails/assertions for anything safety-critical (never emit clinical advice outside approved bounds); (4) human-in-the-loop review for high-stakes paths. Point: in health you can't ship on vibes — you need a regression harness and a bright line between "quality" checks and "safety" checks.

---

## Likely interview questions + skeletons

**Q1: "You're early in your career — why are you a fit for a Senior role?" (the seniority gap)**
Skeleton: Acknowledge it head-on — don't dodge. "I'm ~1 year in, so I'm applying above my tenure on purpose. What I'd point to is scope: I've shipped applied-AI systems end-to-end and to real clients — autoclip.studio as a running product, MCP servers and RAG in production at Cognizant. I'd rather be judged on what I've shipped than on the calendar. And I'm genuinely open to a mid-level seat if that's the right level — I want to do this work at Omada more than I need the title." Confident, honest, leaves the down-level door open.

**Q2: "Walk me through deploying an AI application you built."**
Skeleton: Use CreatorClip. Problem → architecture (FastAPI ingress, Celery async workers, WhisperX → Voyage/pgvector retrieval → ffmpeg render) → why each choice → what broke and how you handled it → how you'd know it's working (eval/monitoring). Show the whole lifecycle, not just the model call.

**Q3: "How would you make an LLM feature safe to put in front of patients?"**
Skeleton: Retrieval over approved content only (citable, updatable); guardrails on output bounds; layered eval (offline set + judge + human review on high-stakes paths); log everything for auditability; fail closed — if confidence/retrieval is weak, defer to a human rather than guess. Be honest that healthcare is a new domain for you and that you'd ramp on the specific regulatory constraints fast; pair the humility with the systems instinct.

---

## The ONE demo project: **CreatorClip / autoclip.studio**
Recommend leading with this over CFO Agent. Why:
- **It's the most complete applied-AI pipeline** — transcription, embeddings, retrieval, agentic processing, rendering, OAuth publishing — which maps directly to "targeted AI applications delivered at scale."
- **It's live and clickable** (autoclip.studio) — a running product beats a repo for someone deciding whether to look past ~1 year of tenure.
- **It shows production instincts** — async Celery, pgvector at scale, managed embeddings, a real render path — the engineering maturity that offsets the seniority question.
- Keep CFO Agent as the "and I'm also standing up a production-complexity agent that does agentic reasoning over real financial data (CSV/OFX import into an encrypted vault)" follow-up — frame it as in active development, not deployed.

## 30-second pitch
"I'm an applied-AI engineer — I take state-of-the-art LLM and agent tooling and turn it into software that actually ships. My main proof is autoclip.studio: an async AI pipeline that transcribes, embeds, retrieves, and renders video end-to-end, running as a real product. On top of that I build RAG pipelines, multi-agent LangGraph systems, and MCP servers in production at Cognizant, including client work. I'm about a year in, so I'm reaching for this role on the strength of what I've shipped rather than years — and I'm genuinely excited about applied AI for care at scale, which is exactly the kind of problem I want to be solving."
