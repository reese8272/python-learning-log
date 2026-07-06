# Portfolio Interview Prep — CFO Agent & CreatorClip

Distilled from an independent audit of the two flagship résumé projects (code integrity, availability, accuracy, positioning). Read this before any technical screen. The full audit is retired; the load-bearing parts live here.

**Core message:** neither project is simple or fragile — both are live, production-grade systems. The real interview risk is **ownership depth** ("did *you* build this or did Claude?"), not "is it real?" Prep = defending decisions, not adding features.

---

## Verified proof points (use as talking points)

**CFO Agent** — `github.com/reese8272/CFO-Agent` · deployed to prod (Oracle VM + Cloudflare tunnel, CI/CD)
- ~9,937 LOC app · ~3,683 LOC tests · repo reports **177 passing / 4 skipped** · 74 commits · first commit May 26 2026 → ~6 weeks.
- Real multi-node **LangGraph** topology: retrieval → analyzer → strategist / career / income-optimizer / tax-optimizer → coach → tracker → alert → synthesizer → persist.
- **Redis-backed LangGraph checkpointing**, **encryption at rest** (encrypted transaction amounts), Alembic migrations (7 revisions), `slowapi` rate limiting, Sentry, a written threat model, 5+ CI workflows, self-graded production-assessment log.

**CreatorClip / autoclip.studio** — `github.com/reese8272/creatorclip` · live (302 + healthy `/health`: postgres/redis/storage ok)
- ~37,195 LOC app · ~54,841 LOC tests · **1,774 test functions** · real React/TS frontend · 230 commits · ~10 days.
- **Deployed multi-tenant SaaS** with **Stripe billing/subscriptions**; Celery + Redis + RedBeat async pipeline; Voyage AI (`voyage-3.5`) embeddings in pgvector; ffmpeg render (two-pass loudness norm, libass captions); real YouTube OAuth.
- Undocumented extras: MediaPipe active-speaker reframing, Sentry + OpenTelemetry, per-creator recency-decayed preference model, an agentic Pro chat assistant.

---

## Accuracy fixes — status

- [x] **CFO Agent Plaid overclaim** — *fixed.* Plaid is NOT integrated (code defers it: "Phase 2 / Plaid — deferred, do not wire yet"; only a config placeholder + nullable `plaid_account_id`). Real aggregation = **CSV/OFX import (`ofxtools`) + market-data APIs (yfinance / RentCast)**. Master résumé now says CSV/OFX + encrypted vault. **If asked about Plaid: it's roadmap, not built.**
- [x] **CreatorClip transcription** — *fixed in master.* Default backend is **Deepgram nova-3**, not WhisperX (WhisperX is a config-selectable self-host option). Lead with "Deepgram (WhisperX/AssemblyAI selectable)."
- [ ] **Same WhisperX→Deepgram + Plaid wording still present in the 7 tailored `jobs/*/resume.md`** and in LinkedIn copy — fix before sending those.
- [x] **CreatorClip undersold** — master now surfaces SaaS / Stripe billing / multi-tenant / React-TS frontend.
- [ ] Both projects are **2026** projects (first commits May/Jun 2026), not "2025–2026" — correct any date lines.
- [ ] CFO Agent README badge drift: "in active development / 159 tests" → live / 177 tests.

---

## Ownership-depth questions to rehearse (answer cold)

~130k lines across two prod systems in ~6 weeks with "AI-augmented engineering (Claude Code)" on the résumé → a sharp interviewer probes *why*, not *whether*:
- Why Celery over a native async task queue? Why RedBeat specifically?
- Why encrypt transaction amounts but not [X]?
- Where does your LangGraph state get corrupted under concurrent turns?
- Walk me through a bug you found and fixed.

Answer these well and the scale is a weapon; fumble them and it's a red flag.

---

## Interview ammo — bug/tradeoff stories (from CFO Agent's own SEV2 backlog)

Each is a clean 60-sec narrative (what it was → how I caught it → how I'd fix it → what I learned). Shows you audit your own work.
- **Money source-of-truth drift** — tax constants re-hardcoded in `wealth_position.py` instead of imported from `principles.py`; silent divergence at the 2027 rollover.
- **Duplicated expense-sum logic** across three files that diverged → empty expense table reported `savings_rate = 100%`.
- **`float()` casts on money** inside `analysis_jsonb`, violating a no-float-money rule — and it's the exact payload the LLM reasons over.
- **Token accounting gap** — only the synthesizer's tokens were logged; other nodes undercounted usage.
- **`StopIteration → 500`** when the model truncates at `max_tokens` in five nodes (coach guarded it; others didn't).
- **N+1 in CSV/OFX import** — a select + flush + audit insert per row.
- **Missing rate limits** on endpoints that fan out to paid external APIs.
