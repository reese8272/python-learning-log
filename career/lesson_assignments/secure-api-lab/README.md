# secure-api-lab

A FastAPI service demonstrating enterprise API-security patterns end to end:

- **OAuth2 client-credentials** against Okta as an external IdP
- **JWT validation** against JWKS — algorithm pinning, `kid` rotation, the full claim checklist
- **Scope-based authorization** as a FastAPI dependency
- **mTLS** for service-to-service, with cert-as-identity
- **PHI-safe audit logging** — who accessed what, never the payload
- **Deployed on AWS**: ECS Fargate → ALB → ACM → Route 53, fronted by WAF, observed by CloudWatch
- **CI/CD** via GitHub Actions with OIDC federation — no long-lived AWS credentials

The service is a **resource server**: it validates tokens an external IdP issued, and never issues them.

## Status

Scaffolded 2026-08-10. See `docs/PROJECT_STATE.md` for live status and `docs/issues.md` for the build plan.

## Quickstart

*(added at Issue 1)*

## Docs

| File | What |
|---|---|
| `docs/issues.md` | The build plan, dependency-ordered |
| `docs/SOT.md` | Architecture and invariants |
| `docs/PROJECT_STATE.md` | Where the build actually is |
| `docs/DECISIONS.md` | Why the non-obvious choices were made |
| `docs/TEARDOWN.md` | AWS teardown checklist |
| `CLAUDE.md` | Working agreement, technical standards, cost guardrails |
