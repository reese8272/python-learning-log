# SOT.md — Source of Truth

Facts about this system that must not drift. Updated at every issue close-out.

## Purpose

A secure FastAPI service demonstrating enterprise API-security patterns end to end: OAuth2 client-credentials
against Okta, JWT validation against JWKS, scope-based authorization, mTLS for service-to-service, PHI-safe
audit logging, and a real AWS deployment behind an ALB with WAF and CloudWatch.

## Architecture — the target request path

```
Client
  │  (mTLS: client cert, Issue 5)
  │  (Authorization: Bearer <Okta JWT>)
  ▼
Route 53  →  ACM cert  →  WAF  →  ALB (HTTPS listener)
                                    │
                                    ▼
                             ECS Fargate task
                             ├─ require_token   (JWKS, 6-check validation)
                             ├─ require_scope   (403 on insufficient scope)
                             ├─ response_model  (minimum-necessary filtering)
                             └─ audit log       (actor/action/resource/time, no PHI)
                                    │
                                    ▼
                               CloudWatch Logs → metric filter → alarm
```

**Token issuance is external.** This service is a **resource server**: it validates tokens Okta issued and
never issues them. That framing is load-bearing — it is what the JD's "exposing APIs that support
integration with IDP" actually means.

## Invariants

- Signature verification happens **before** any claim is read or trusted.
- JWT decode always pins `algorithms=["RS256"]`. No exceptions, no config that can widen it.
- `401` = unauthenticated (no/invalid token). `403` = authenticated but insufficient scope. These never blur.
- PHI never enters a log line, a JWT, or a URL.
- No static AWS access keys exist anywhere — roles and OIDC federation only.
- `certs/` and `.env` are never committed.

## Key coordinates

| Thing | Where |
|---|---|
| Concept roadmap | `~/workspace/life-log/career/secure-api-engineering/summary.md` |
| Issue list | `docs/issues.md` |
| Okta issuer / audience | `.env` (see `.env.example`) |
| AWS region | *(set at Issue 7)* |
| Domain | *(confirm before Issue 7)* |

## Open questions

- Domain for the ACM cert — owned already, or register one? Blocks Issue 7.
- ALB native JWT verification (shipped 2025-11) — demo it *in addition to* in-app validation if Thursday
  has room. It's a strong differentiator; it is not a substitute for Issue 3.
