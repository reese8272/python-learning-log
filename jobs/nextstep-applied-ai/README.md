# Next Step Systems — Applied AI Engineer (+ AI Backend Engineer)

## Job Snapshot

- **Roles:** Applied AI Engineer (PRIMARY) and AI Backend Engineer — sibling roles at the same firm, same recruiter. **One tailored resume serves both.** Apply to BOTH.
- **Company:** Next Step Systems — a technical recruiting firm. End client is undisclosed. Fully remote.
- **Comp:** $140,000 – $200,000 (both variants same band).
- **Apply direct (their real ATS — SmartRecruiters, NOT Dice easy-apply):**
  - Applied AI Engineer: https://jobs.smartrecruiters.com/NextStepSystems/744000135482821-applied-ai-engineer-work-from-home
  - AI Backend Engineer: https://jobs.smartrecruiters.com/NextStepSystems/744000135478267-ai-backend-engineer-work-from-home
- **Contact:** Mike Stapinski, President & Founder — jobs@nextstepsystems.com — 630-428-0600. Free to job seekers. LinkedIn (verify — a few profiles exist): https://www.linkedin.com/in/mikestapinski/ ; bio: https://www.nextstepsystems.com/it-recruiters-president-mike-stapinski/

### JD essence
- **Applied AI:** turn model capabilities into real product behavior — AI that interacts with users, supports decisions, and powers automation.
- **AI Backend:** the systems powering AI-driven decisioning, automation, and orchestration — where latency, correctness, reliability, and **cost** directly impact production.

---

## Why He Fits (clean match, not a stretch)

This is the best level-fit of the recruiter-tier roles. The JD asks for exactly what he's already built:
- **Production LLM / agent apps** — CFO Agent (LangGraph + FastAPI), Agentic Software Development Team (multi-agent LangGraph on Bedrock), MCP server integrations at Cognizant.
- **Orchestration + async backends** — CreatorClip's Celery pipeline, LangGraph agent graphs.
- **Model evaluation** — prompt engineering and model evaluation from the GenAI contractor role.
- **Cost / latency awareness** — Redis caching (CFO Agent) and off-request async workers (CreatorClip) are real cost- and latency-aware design decisions, not buzzwords.

The JD's own framing (latency, correctness, reliability, cost) maps almost one-to-one onto his project decisions.

---

## What Changed & Why

- **Summary rewritten** for an applied-AI / backend engineer who "turns models into reliable production behavior with attention to latency and cost." Directly mirrors the JD language.
- **Projects lead the resume** (before Experience) because the strongest evidence for this role is what he's built. CreatorClip and CFO Agent are placed first.
- **Latency/cost framing added** to CreatorClip (async off-request pipeline) and CFO Agent (Redis caching) — truthful re-wording of existing architecture to surface the cost/latency angle the JD cares about.
- **Skills regrouped** to put AI/Agentic and Backend/Infra (FastAPI, Celery, Redis, LangGraph) up top.

## How It's Tailored

Re-emphasis and reordering only. Every fact is from the source resume. Nothing invented: no new employers, dates, metrics, or skills. Tailoring = lead with projects, surface the orchestration/cost/latency story, and align vocabulary with the JD.

---

## Gaps To Frame

- **Hard scale/latency-at-volume metrics.** He has the architecture (async Celery, Redis caching, decoupled model steps) but light on published throughput/latency numbers. **Frame:** talk about the *design decisions* and why they exist — "heavy steps run off the request path so the API stays responsive; caching cuts repeat token cost" — rather than claiming volume he can't back. If asked for numbers, be honest and pivot to the reasoning.
- **~1 year tenure.** These roles don't read senior-only, and the recruiter tier is right for his level. Don't over-apologize; let the shipped production work carry it.

---

## Fit Verdict

**High.** Cleanest level-fit of the recruiter-tier roles. Apply to **BOTH** Applied AI and AI Backend via SmartRecruiters, then message Mike. Estimated interview-conversation probability: high, given the recruiter is incentivized to place and the skill overlap is direct.
