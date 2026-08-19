# CLAUDE.md — secure-api-lab

## What this is

A learning build covering secure async FastAPI, OAuth2/JWT/mTLS, Okta integration, and AWS
(ECS/ALB/Route 53/S3/API Gateway/ACM/WAF/CloudWatch) in a HIPAA-shaped environment.

*Started 2026-08-10 under a 7-day interview clock. **The clock was removed 2026-08-13** — that role closed on
years-of-experience before an interview happened. The build survived it: this is the security and
production-API layer under the AI capstone, and it's the only fully-specified project in the system.*

This repo is the *build* half. The *concept* half is the roadmap at
`~/workspace/life-log/career/secure-api-engineering/summary.md`, walked with `/learn`. Each issue in
`docs/issues.md` makes one roadmap section concrete — **a concept isn't banked until code using it exists.**
Each issue is also **PART 3 of that section's worksheet**: the top rung of the Ladder, where a taught
concept gets produced with no scaffolding under it.

Work it with `/issue-workflow <n>`.

## The bar

This is portfolio code, not throwaway. It should survive being read by a stranger.
It is **learning-first**: if a choice is between shipping faster and understanding deeper, understand deeper.
Without a deadline that tradeoff got easier, not harder — there is no longer any reason to cut a corner.

**Struggle-first (issue-workflow standing rule #0):** 10–20 minutes unaided before engaging AI on any issue.
Read the docs, form a hypothesis, sketch an approach. A wrong hypothesis is a great attempt; a blank page is not.

**Every issue ends with an out-loud explanation.** Each issue's acceptance criteria include a "can explain
out loud" item. That item is not optional — it is the actual deliverable. The code is how you earn it.

## Non-negotiable technical choices

- **PyJWT (`pyjwt[crypto]`), never python-jose.** The official FastAPI docs migrated; python-jose is
  effectively unmaintained. Most tutorials online are still wrong about this.
- **Pydantic v2 idioms** — `model_dump()`, `@field_validator`, `pydantic-settings`.
- **`lifespan`**, not `@app.on_event`. **`Annotated[X, Depends(...)]`**, not `= Depends(...)`.
- **Algorithms explicitly allow-listed** on every JWT decode. Never `verify=False`, never an unpinned `alg`.
- **No secrets in git.** `.env` and `certs/` are gitignored; `.env.example` is committed.
- Research live against current docs before implementing — the ecosystem moved recently and several
  patterns here changed within the last year (see the roadmap's Currency Watch).

## 💸 Cost guardrails — hard rules, not preferences

- **NEVER create an AWS Private CA.** ~$400/mo general-purpose, ~$50/mo short-lived; billed prorated from
  creation, and deleting it does not refund. mTLS is learned with a **local openssl CA** (Issue 5).
- **NEVER enable Shield Advanced.** ~$3,000/mo, 1-year commitment. Shield Standard is free and already on.
- **Set a $25 AWS Budget alert before creating any resource.**
- Tag every resource `project=secure-api-lab`. Keep `docs/TEARDOWN.md` current *as you build*.
- Target total spend: **under $20.**

## Layout

```
app/     FastAPI application
tests/   pytest — including the negative auth matrix (Issue 4)
certs/   generated locally by script, gitignored
docs/    issues.md · SOT.md · PROJECT_STATE.md · DECISIONS.md · TEARDOWN.md
```

## Git

Direct to `main`. Single owner, no PRs. Commit at each issue close-out.
