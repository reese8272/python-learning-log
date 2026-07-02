# LinkedIn + GitHub — Make the Differentiators Visible

The whole resume strategy leans on "I ship production agent systems." Right now that's invisible online. This file closes that gap. Copy/paste the entries below.

**Honesty guardrail (same as the resumes):**
- **CreatorClip / autoclip.studio** = ✅ LIVE production SaaS. Describe it as live.
- **CFO Agent** = 🚧 in active development. Do NOT call it live/deployed. No Plaid (not built).

---

## 1. GitHub — do this first (5 min)
Both repos now have a README committed. Make sure each repo is **public** and the README renders:
- CreatorClip → https://github.com/reese8272/creatorclip
- CFO Agent → https://github.com/reese8272/CFO-Agent

Then **pin both** on your GitHub profile (Profile → Customize your pins → select these two).

> 60-second win after that: record a Loom of each running and paste the link at the top of each README (there's a `<!-- TODO: add demo GIF -->` placeholder in the CreatorClip one).

---

## 2. LinkedIn "Featured" section (most visible — do this)
Profile → Add profile section → Featured → Add a link. Add both:

### Featured link 1 — CreatorClip (lead with this; it's live)
- **Link:** https://autoclip.studio
- **Title:** `CreatorClip — AI video auto-clipper (live SaaS)`
- **Description:**
> A production SaaS I built end-to-end: turns long-form YouTube content into short-form clips, learning each creator's style via a custom "DNA" module. FastAPI + async Celery pipeline (WhisperX → Voyage AI/pgvector embeddings → ffmpeg), React/TypeScript frontend, Stripe billing, YouTube OAuth. Live at autoclip.studio.

### Featured link 2 — CFO Agent
- **Link:** https://github.com/reese8272/CFO-Agent
- **Title:** `CFO Agent — personal-finance AI agent (LangGraph)`
- **Description:**
> An agentic personal-finance assistant (in active development): an 11-node LangGraph reasoning agent on FastAPI with PostgreSQL persistence, Redis caching, an encrypted data vault, CSV/OFX import, and a scenario engine. Backed by 159 tests + an eval harness.

---

## 3. LinkedIn "Projects" section
Profile → Add profile section → Additional → Projects. Add both.

### Project 1
- **Project name:** `CreatorClip / autoclip.studio`
- **Dates:** 2025 – Present
- **Project URL:** https://autoclip.studio
- **Description:**
> Production AI SaaS that auto-generates short-form clips from long-form YouTube video, learning a creator's channel style via a custom "DNA" module. Architecture: React/TypeScript frontend + FastAPI backend; async Celery pipeline (WhisperX transcription → Voyage AI + pgvector semantic embeddings → ffmpeg rendering); YouTube OAuth; Stripe billing with a credit ledger; per-creator PostgreSQL row-level security; staging/prod Docker compose with CI auto-deploy; Prometheus/Sentry/OpenTelemetry observability; ~79% test coverage. Live at autoclip.studio.
- **Skills to tag:** Python, FastAPI, Celery, LangChain, pgvector, PostgreSQL, Redis, React, TypeScript, Docker, CI/CD, Stripe

### Project 2
- **Project name:** `CFO Agent`
- **Dates:** 2025 – Present
- **Project URL:** https://github.com/reese8272/CFO-Agent
- **Description:**
> Agentic personal-finance platform (in active development). An 11-node LangGraph reasoning agent (retrieval → analysis → specialist → coach → tracker → alert → synthesis → persist) on a FastAPI backend, with PostgreSQL persistence, Redis caching, Anthropic prompt caching, a Fernet-encrypted data "vault," CSV/OFX import, and a financial-scenario engine. Architected multi-tenant; 159 tests plus an evaluation harness.
- **Skills to tag:** Python, FastAPI, LangGraph, LangChain, PostgreSQL, Redis, Anthropic API, AI Agents

---

## 4. Optional but high-ROI — headline / About tweak
- **Headline idea:** `AI Engineer — LangGraph agents, MCP servers, RAG · Python/FastAPI · shipped a live AI SaaS (autoclip.studio)`
- **About opener idea:** "I build and ship agentic AI systems. I run a live production SaaS (autoclip.studio) and build multi-agent LangGraph systems + MCP servers professionally at Cognizant." — then point to Featured.

## Order of operations
1. Make both repos public + confirm READMEs render → pin them.
2. Add both Featured links (autoclip first).
3. Add both Projects entries.
4. Record two Looms; paste into READMEs + Featured.
5. Update headline/About.
