# DECISIONS.md — secure-api-lab

Design decisions that deviate from the obvious default. Newest first.

---

## 2026-08-10 — PyJWT over python-jose

**Decision:** Use `pyjwt[crypto]` for all JWT work.
**Why:** The official FastAPI security tutorial migrated from python-jose to PyJWT; python-jose is
effectively unmaintained. A large share of FastAPI/JWT tutorials still teach python-jose, so using it
signals a stale mental model. The `[crypto]` extra is required for RS256, which is mandatory here because
Okta signs asymmetrically.
**Source:** https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/ (verified 2026-08-10)

---

## 2026-08-10 — mTLS learned with a local openssl CA, not AWS Private CA

**Decision:** Issue 5 generates its own CA with openssl. AWS Private CA is studied from docs only.
**Why:** AWS Private CA bills ~$400/mo in general-purpose mode (~$50/mo short-lived), prorated from
creation with no refund on delete. For a 7-day learning sprint that is indefensible, and the mTLS concepts
— trust chains, cert-as-identity, client-cert verification, rotation — are fully learnable locally.
The pricing itself is retained as an interview answer about why organizations centralize internal PKI and
why the short-lived tier is capped at 7-day certs.
**Source:** https://aws.amazon.com/private-ca/pricing/ (verified 2026-08-10)

---

## 2026-08-10 — In-app JWT validation is the deliverable; ALB JWT verification is a bonus

**Decision:** Issue 3 implements validation in the application. ALB's native JWT verification is
demonstrated only if Issue 7 finishes early.
**Why:** ALB gained client-credentials JWT verification on 2025-11-12 — genuinely new and a strong thing to
know. But offloading validation to the edge would skip the exact mechanism the interview will probe
(JWKS, `kid` rotation, algorithm pinning, the claim checklist). Build it in-app to learn it; know the edge
option to discuss the tradeoff. The correct production answer is defense in depth — both.
**Source:** https://aws.amazon.com/about-aws/whats-new/2025/11/application-load-balancer-jwt-verification/
(verified 2026-08-10)

---

## 2026-08-10 — The mock resource is PHI-shaped on purpose

**Decision:** The demo resource is patient records rather than a generic `Item`.
**Why:** It makes `response_model` field-filtering a *compliance control* (HIPAA minimum-necessary) rather
than a style choice, and it forces the audit-logging problem in Issue 6 to be real: log who accessed which
record, never the record itself. The JD lists HIPAA/PHI as desired; this is how the build earns a genuine
answer instead of a memorized one.
