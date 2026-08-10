# Secure API Engineering on AWS — interview sprint roadmap

> **Created 2026-08-10 under a 7-day clock.** Screening cleared for a backend role: FastAPI + OAuth2/JWT/mTLS + Okta + AWS (ECS/ALB/Route 53/ACM/WAF/CloudWatch) in a HIPAA environment. Next round ~**2026-08-17**, covering all three formats — verbal Q&A, live coding, and system design. This track outranks everything else in the system until then. See `DECISIONS.md` (2026-08-10).

**What this is:** A ground-up curriculum in secure API engineering — FastAPI at depth, OAuth2/OIDC/JWT, mTLS, and the AWS platform layer that actually fronts a production API. Built like the AI and Python curricula: each unit is learned in-catalog via `/learn api`, **researched live against current official docs**, then handed to `/sharpen` (defend cold) and `/drill` (retain). This roadmap is the *what to cover*; the teaching is generated fresh each session so it never goes stale.

**The framing — two different jobs, don't conflate them.** This track has an unusual shape because the gap analysis came back split:

- **§1, §2, §7, §9 are RECALIBRATION.** You already do these in production. `CAREER_LOG.md:52` rates FastAPI "Gap" while CreatorClip runs ~37k LOC of it with 1,774 test functions, and `CAREER_LOG.md:62` rates CI/CD "Gap" against 5+ live workflows and auto-deploy-on-main. The gap is not knowledge — it's **never having had to say it out loud.** Work these fast, out loud, anchored to your own code.
- **§3, §4, §5, §6, §8 are ACQUISITION FROM ZERO.** A full-repo grep on 2026-08-10 returned **zero mentions** of mTLS, Okta, OIDC, SAML, ECS, ALB, Route 53, API Gateway, ACM, Private CA, WAF, Shield, CloudWatch, or Swagger. Not as gaps, not as queue items — absent. These need real reps, and §6 needs a real deploy.

**Source of truth:** the job description (transcribed verbatim in Interview Intel below) and `career/helpful_notes_and_guides/AI Engineering Master Guide.md` for the mastery standard ("can I explain why THIS over THAT?").

**The pipeline:**
```
/learn          →   /sharpen        →   /drill
acquire (here)      defend cold         retain (spaced rep)
researched live     100% / tier bar     against forgetting curve
```

**Tiers** (interview-priority weighted, not generic importance):
- **Tier 1 — They WILL test this** → 100%, "can teach it." Mechanism + why-this-over-that + failure mode. These are the requirements stated explicitly in the posting.
- **Tier 2 — Likely probed / sets you apart** → Pareto 80/20, "explain the decision." The Desired Skills, and the depth that turns a pass into a "we want this person."

**Status keys:** `[ ]` not started · `[~]` in progress / needs another pass · `[x]` learned (date) → can defend cold → enters `/sharpen` then `/drill` rotation.

**How to use:** Work top-down within a section. Under a 7-day clock the day-map at the bottom overrides pure dependency order. Don't skip a `[ ]` because you "already know it" — the whole failure mode this track exists to fix is *knowing something you can't say*.

**The build is the spine.** Every Tier-1 section has a matching issue in `~/workspace/secure-api-lab/docs/issues.md`, driven by `/issue-workflow`. A concept isn't banked until the code exists — `concept_queue.md:93`, *"grilling without building is passive consumption with extra steps."* Worksheets, where a unit warrants one, land at `career/lesson_assignments/apisec-<section>-<kebab-unit>.py`.

---

## 🎯 Interview Intel — what they actually asked for

**Verbatim from the posting:**

> **API Development (Backend)** — Strong experience building REST APIs using Python, with FastAPI as the primary framework · Development of high-performance, secure, and asynchronous API services using FastAPI · API contract definition and maintenance using OpenAPI / Swagger · Experience exposing APIs that support integration with IDP (like Okta)
>
> **Security & Identity** — Implementation of OAuth2 authentication and authorization flows · Secure handling and validation of JWT tokens · Experience with mTLS (mutual TLS) for service-to-service communication · Strong understanding of API security protocols and secure communication standards
>
> **AWS Services for API & Security** — Hands-on experience with AWS services: ECS, ALB, Route 53, S3, API Gateway · Certificate management using AWS Certificate Manager (ACM) and AWS Private Certificate Authority · API protection using AWS WAF and AWS Shield · Monitoring, logging, and alerting using Amazon CloudWatch · Proven ability to deploy, secure, and operate APIs on AWS
>
> **API Testing & Validation** — Proficiency with API testing and validation · Ability to test authentication, authorization, headers, and request/response flows
>
> **Desired Skills** — *Compliance & Security Context:* Prior experience working in HIPAA-compliant environments · Secure handling of PHI, including access control, encryption, and audit logging. *DevOps & Source Control:* Familiarity with CI/CD pipelines for API and UI deployments.

**How to read it (the subtext):**

- **"high-performance, secure, and asynchronous"** — three words, three separate probes. *Asynchronous* means they will ask about the event loop and what happens when you block it. *High-performance* means workers, topology, pagination, streaming. *Secure* is the whole middle half of the posting. → **§1.**
- **"API contract definition and maintenance using OpenAPI/Swagger"** — the word **maintenance** is doing work here. They're not asking "does FastAPI generate a spec" (it does, for free). They're asking whether you've *versioned* a contract, detected a breaking change, and handed a spec to a consuming team. → **§2.**
- **"exposing APIs that support integration with IDP (like Okta)"** — this is the single most revealing line in the posting. "Exposing APIs that support integration with" means **your API is a Resource Server, not an authorization server.** You validate tokens Okta issued; you never issue them. If you get this backwards in the room, it's visible immediately. → **§3.**
- **"mTLS for service-to-service"** — note the qualifier. They're not doing mTLS for browsers; this is internal service auth. That tells you they have a service mesh or an internal PKI, and it's why AWS Private CA is in the very next bullet. → **§5.**
- **"ECS, ALB, Route 53, S3, API Gateway" + ACM/PCA + WAF/Shield + CloudWatch** — this is a complete, coherent request path, not a random service list. Learn it as **one diagram**, not eight facts. → **§6, §10.**
- **"Proven ability to deploy, secure, and operate APIs on AWS"** — *proven* and *operate*. This is the bullet you cannot talk your way past, and it's why Issue 7 of the build is a real deploy. → **§6.**
- **"test authentication, authorization, headers, and request/response flows"** — they are describing a **negative test matrix**, almost verbatim. Expired, wrong audience, bad signature, missing scope, missing header. → **§7.**
- **HIPAA / PHI** — listed as *Desired*, not required. That's your honest opening: study it genuinely, claim it accurately. → **§8, §11.**

**Where to spend the peak window:** §3, §4, §5, §6. That's ~70% of the posting and ~100% of your actual gap. §1/§2/§7/§9 are confirm-and-say-out-loud, not learn. §10 is the highest-leverage single hour of the week.

---

## ⚠ Currency Watch — verified live 2026-08-10; re-verify per unit

The ecosystem moved, and several of these are *recent enough that most candidates won't know them.* That's the differentiator.

- **`python-jose` is out; `PyJWT` is in.** The official FastAPI security tutorial migrated from python-jose to PyJWT — python-jose is effectively unmaintained. Half the FastAPI/JWT tutorials online still teach python-jose; using it dates you instantly. For RS256 (which is what you need with Okta) install **`pyjwt[crypto]`** — the `cryptography` extra is required for asymmetric algorithms. → [FastAPI OAuth2-JWT docs](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/)
- **OAuth 2.1 is still an Internet-Draft, not an RFC** — `draft-ietf-oauth-v2-1-15` as of March 2026. Say *"OAuth 2.1 is the de-facto 2026 baseline, though it's still a draft"* — the precision is a credibility marker, and claiming it's a finished RFC is a small, catchable error. What it changes: **implicit grant removed**, **resource-owner-password-credentials removed**, **PKCE required for every client including confidential ones**, exact-match redirect URI validation, refresh-token rotation strongly recommended. → [oauth.net/2.1](https://oauth.net/2.1/)
- **🔥 ALB can now verify JWTs itself — shipped 2025-11-12.** ALB supports client-credentials-flow JWT verification natively: you give the listener a JWKS endpoint and issuer, and it validates signature, expiry, and claims **before the request reaches your app**. HTTPS listeners only. This is nine months old and directly on-topic for this JD — most candidates will not know it exists. It reframes the §4 question "where do you validate the token?" into a real architectural tradeoff (edge vs in-app, and the defense-in-depth answer is *both*). → [AWS announcement](https://aws.amazon.com/about-aws/whats-new/2025/11/application-load-balancer-jwt-verification/)
- **ALB mTLS has two distinct modes** — don't blur them. **Passthrough**: ALB completes the handshake and forwards the whole client cert chain in the `X-Amzn-Mtls-Clientcert` header for your app to authorize on. **Verify**: you create a **trust store** resource, upload a CA bundle + CRLs, attach it to the listener, and ALB rejects bad certs itself. Related headers exist for granularity: `X-Amzn-Mtls-Clientcert-Subject`, `-Issuer`, `-Serial-Number`, `-Validity`. → [ALB mTLS docs](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/configuring-mtls-with-elb.html)
- **AWS Private CA has two pricing tiers, and the gap is the story.** General-purpose mode: **~$400/CA/month**. Short-lived-certificate mode: **~$50/CA/month + $0.058/cert**, max 7-day validity. The short-lived tier exists precisely because modern service-to-service mTLS wants frequently-rotated certs. Knowing both numbers *and why the cheap one is capped at 7 days* is a genuinely strong answer about internal PKI economics. **Neither gets created during this sprint** — see the cost guardrails. → [AWS Private CA pricing](https://aws.amazon.com/private-ca/pricing/)
- **Okta specifics that bite people:** you need a **custom authorization server** to protect your own API (the org default one won't mint custom scopes). The **client-credentials flow cannot request OpenID scopes** — no user context exists, so you must define a custom scope. A resource server must validate **both `aud` and `cid`**, not just `aud`. Cache the JWKS and only re-fetch when an unknown `kid` appears — don't fetch per request, and don't cache forever. → [Okta client credentials guide](https://developer.okta.com/docs/guides/implement-grant-type/clientcreds/main/)
- **Pydantic v2 / FastAPI current idioms** (carried over from the Python track, still load-bearing here): `model_dump()` not `.dict()`, `@field_validator` not `@validator`, `pydantic-settings` for `BaseSettings`, `lifespan` context manager not `@app.on_event`, and `Annotated[X, Depends(...)]` over the old `= Depends(...)` default-value form.
- **`httpx.ASGITransport`** is the current async test-client pattern; `TestClient` remains fine for sync tests.

---

## Section 1 — FastAPI at depth (Tier 1) · *recalibration*

*You have ~37k LOC of this in production across CreatorClip and CFO Agent. Nothing here is new information — it is the vocabulary for things you already do. Work it out loud, fast, and anchor every single answer to your own code.*

- [ ] **ASGI vs WSGI, and why FastAPI is async** — the concurrency model, why "high-performance" in the JD means the event loop, uvicorn/gunicorn worker topology. `T1`
- [ ] **`async def` vs `def` and the threadpool trap** — FastAPI runs plain `def` handlers in a threadpool; a blocking call inside an `async def` stalls the entire loop. *The single most likely "do you actually understand async" question in the room, and you already own the underlying concept cold (`CAREER_LOG.md:56`).* `T1`
- [ ] **`Depends()` and why auth belongs in a dependency** — DI as the composition point, sub-dependencies, caching, `dependency_overrides` as the testing seam. *This is the mechanism the entire §4 JWT design rests on.* `T1`
- [ ] **Pydantic v2 as the request/response contract** — validation at the boundary, `model_dump()`, why type params make the generated OpenAPI schema precise. `T1`
- [ ] **`response_model` as a PHI-leak control** — response filtering isn't cosmetic; it's how you enforce HIPAA minimum-necessary at the serialization layer. *Connects §1 to §8 — say this connection in the interview.* `T1`
- [ ] **Lifespan, exception handlers, and the error contract** — startup/shutdown resources, consistent error envelopes, never leaking internals in a 500. `T1`
- [ ] **Middleware vs dependency — when each** — cross-cutting (correlation IDs, logging, timing) vs per-route authorization. `T1`

## Section 2 — REST + OpenAPI/Swagger as a maintained contract (Tier 1) · *recalibration*

*Syllabus already existed at `mid-python-developer-prep/summary.md:79-89`, 100% unchecked. The JD's word is "maintenance" — aim there.*

- [ ] **Verbs, status codes, and the 401/403/422 distinction** — 401 = I don't know who you are; 403 = I know, you can't; 422 = I understood, the body is invalid. *Get this wrong and it's a visible tell.* `T1`
- [ ] **Statelessness, idempotency, and safe retries** — which verbs are idempotent, idempotency keys, why this matters behind a load balancer that retries. `T1`
- [ ] **Pagination, versioning, and breaking changes** — cursor vs offset; URL vs header versioning; what actually constitutes a breaking change to a consumer. `T1`
- [ ] **FastAPI's auto-generated OpenAPI + `securitySchemes`** — how the spec is produced, declaring OAuth2/bearer security in it, `/docs` vs `/redoc`, and locking the spec down in prod. `T1`
- [ ] **Contract-first vs code-first — the actual tradeoff** — when a consuming team forces contract-first; exporting the spec as a CI artifact and diffing it to catch breaking changes. *This is the "maintenance" answer.* `T1`

## Section 3 — OAuth2, OIDC, and integrating with Okta (Tier 1) · *from zero*

*Zero repo footprint on Okta, OIDC, or SAML. `CAREER_LOG.md:78` says you can't currently draw the authn/authz decision tree. You HAVE shipped OAuth2 (YouTube publishing in CreatorClip) and you have real earned judgment about it — you cut auto-upload from v1 over sensitive-scope review risk (`agenda.md:131`). Use that story; it's better than most candidates'.*

- [ ] **OAuth2 roles and the grant-type map** — resource owner / client / authorization server / **resource server**, and which grant for which situation. *Your API is the resource server. Internalize that framing before anything else.* `T1`
- [ ] **What OAuth 2.1 removed and why** — implicit and ROPC gone, PKCE now required for all clients, exact-match redirect URIs. Each removal traces to a specific attack. ⚠ *still a draft — say so* `T1`
- [ ] **Client credentials flow for service-to-service** — no user context, no OpenID scopes, custom scopes required. *This is the flow the JD's "service-to-service" bullet implies.* `T1`
- [ ] **Authorization code + PKCE for user flows** — the code interception attack PKCE closes, and why confidential clients need it too now. `T1`
- [ ] **OIDC vs OAuth2 = authentication vs authorization** — the ID token vs the access token, why you never authorize off an ID token, `/.well-known/openid-configuration` discovery. *The decision tree `CAREER_LOG.md:78` says you're missing.* `T1`
- [ ] **Okta concretely** — custom authorization server, issuer, audience, custom scopes and claims, the JWKS endpoint, and validating **both `aud` and `cid`**. `T1`
- [ ] **Scopes vs roles vs claims** — coarse API-level permission vs application RBAC, and where each is enforced. `T1`

## Section 4 — JWT validation done correctly (Tier 1) · *from zero*

*`concept_queue.md:67` has "JWT + API key patterns" as Tier 2, unchecked. It is not Tier 2 for this interview — the JD says "secure handling and validation of JWT tokens" explicitly.*

- [ ] **Anatomy: header, payload, signature** — base64url is encoding, not encryption; **anyone can read a JWT**; never put PHI in one. `T1`
- [ ] **RS256 vs HS256 and why asymmetric with an external IdP** — you hold no secret, Okta signs, you verify with a public key. `T1`
- [ ] **JWKS: fetch, `kid` selection, caching, rotation** — cache until an unknown `kid` appears; the failure mode of both over-fetching and never re-fetching. `T1`
- [ ] **The validation checklist, memorized cold** — signature · `iss` · `aud` · `exp` · `nbf`/`iat` · **algorithm allow-list**. *Be able to recite six items without hesitating.* `T1`
- [ ] **The attacks: `alg: none` and RS256→HS256 confusion** — why you pin algorithms explicitly, and why you never trust the payload before verifying the signature. *Naming these unprompted is a strong senior signal.* `T1`
- [ ] **Revocation — the honest hard problem** — JWTs are bearer tokens valid until expiry; the answers are short TTL + refresh rotation, introspection, or a denylist, each with a real cost. `T1`
- [ ] **Where to validate: edge vs app** — ALB JWT verification (⚠ new 2025-11) and API Gateway JWT authorizers vs in-app dependency; defense in depth says both, and know why. ⚠ *very recent — verify live* `T1`

## Section 5 — mTLS for service-to-service (Tier 1) · *from zero*

*Zero repo footprint. Learn it hands-on with a local openssl CA — see the cost guardrails on why NOT with AWS Private CA.*

- [ ] **TLS handshake, then what "mutual" adds** — server proves identity to client; mTLS makes the client prove identity back. `T1`
- [ ] **The client certificate as an identity** — extracting subject/SAN, mapping it to a service principal, why this authenticates the *workload* not the *user*. `T1`
- [ ] **mTLS vs JWT vs both** — mTLS authenticates the channel and the calling workload; the JWT carries the caller's authorization context. **Both, layered, is the zero-trust answer.** *If you can articulate only one thing from §5, make it this.* `T1`
- [ ] **Trust chains, CA hierarchy, revocation** — root vs intermediate, why you don't sign with the root, CRL vs OCSP and why revocation is genuinely hard. `T1`
- [ ] **Termination: ALB passthrough vs verify mode** — the `X-Amzn-Mtls-Clientcert` header family vs an ALB trust store with a CA bundle. ⚠ *two distinct modes, don't blur them* `T1`
- [ ] **Cert rotation and expiry — the #1 production failure mode** — automate or it will page you at 3am. Ties directly to why Private CA has a short-lived-cert tier. *Say this out loud in the room; it reads as operational experience.* `T1`

## Section 6 — The AWS API & security stack as one request path (Tier 1) · *from zero*

*The whole section is one diagram. Learn it as a path, not as eight services. Issue 7 of the build deploys it for real.*

- [ ] **The path, end to end** — Route 53 → ACM cert → WAF → ALB → ECS Fargate task → CloudWatch. *Draw it from memory in under 4 minutes. This is the §10 deliverable.* `T1`
- [ ] **ECS Fargate** — task definition vs service vs task; **task role vs execution role** (*execution role = what ECS needs to pull the image, write logs, inject secrets; task role = what your app code can call*) — a classic interview question; ECR; health checks; rolling deploys. `T1`
- [ ] **ALB** — listeners, rules, target groups, health checks, TLS termination; mTLS modes; and ⚠ native JWT verification (2025-11). `T1`
- [ ] **Route 53 + ACM** — alias records vs CNAME, health checks and failover; DNS-validated public certs and auto-renewal; why ACM public certs are free and can't be exported. `T1`
- [ ] **API Gateway vs ALB — when each** — HTTP API vs REST API, JWT authorizers, usage plans and throttling, request validation, VPC Link; and the honest cost/latency tradeoff vs an ALB. `T1`
- [ ] **WAF and Shield** — managed rule groups, rate-based rules, what a web ACL attaches to, count-mode before block-mode; Shield Standard (free, always on) vs Advanced (~$3k/mo — know the number, never enable it). `T1`
- [ ] **CloudWatch** — structured JSON logs, log groups and retention, metric filters, alarms, correlation IDs; what you alert on for an API (5xx rate, p99 latency, 401 spike as an attack signal). `T1`
- [ ] **S3 + KMS for an API** — Block Public Access, bucket policy vs IAM, SSE-KMS, presigned URLs and their expiry as an access-control decision. `T1`
- [ ] **IAM: roles over keys** — the assume-role model, least privilege, and why there should be no static access key anywhere in this architecture. `T1`

## Section 7 — API testing & validation (Tier 1) · *recalibration*

*You have 1,774 test functions in CreatorClip and 177 in CFO Agent. The JD is describing a negative test matrix — you just need to name what you already do.*

- [ ] **`TestClient` vs `httpx.ASGITransport`** — sync vs the current async pattern. ⚠ `T1`
- [ ] **`dependency_overrides` to swap auth in tests** — the reason §1's "auth belongs in a dependency" matters practically. `T1`
- [ ] **Minting test tokens** — a local RSA keypair + a fake JWKS endpoint so the auth path is tested for real, not mocked away. `T1`
- [ ] **The negative matrix** — expired · wrong `aud` · wrong `iss` · bad signature · `alg: none` · missing scope · missing/malformed header. *Seven cases. The JD asks for exactly this.* `T1`
- [ ] **Contract testing from the OpenAPI spec** — schemathesis / property-based testing against the generated schema; Postman/newman in CI. `T1`

## Section 8 — HIPAA & PHI for an API engineer (Tier 2) · *from zero*

*Listed as Desired, not required. Study it genuinely; claim it accurately. Your own prior guidance applies verbatim — `jobs/natera-sr-fwd-deployed/README.md:37`, "do not overclaim."*

- [ ] **The three rules at altitude** — Privacy, Security, Breach Notification; what "covered entity" and "business associate" mean and which one a vendor engineer is. `T2`
- [ ] **The Security Rule's technical safeguards, mapped to API surfaces** — access control → authn/authz; **audit controls** → who accessed which record when; integrity → tamper evidence; transmission security → TLS everywhere. `T2`
- [ ] **Audit logging without logging PHI** — log the subject, actor, action, and timestamp; never the payload. Redaction and structured-log discipline. *Directly implemented in Issue 6 of the build.* `T2`
- [ ] **Minimum necessary → `response_model`** — compliance enforced at the serialization layer, not by policy documents. `T2`
- [ ] **Encryption in transit and at rest** — TLS 1.2+ everywhere, KMS, key rotation, and what "addressable vs required" actually means in the Security Rule. `T2`
- [ ] **BAA + AWS shared responsibility + HIPAA-eligible services** — what AWS covers vs what stays yours. `T2`
- [ ] **De-identification** — Safe Harbor's 18 identifiers vs expert determination; why de-identified data leaves scope. `T2`

## Section 9 — CI/CD for API and UI (Tier 2) · *recalibration*

*Rated "Gap" at `CAREER_LOG.md:62-64` against 5+ real workflows and CI auto-deploy on push to main. Claim what you've built.*

- [ ] **The pipeline you can sketch on a whiteboard** — checkout → lint → test → security scan → build image → push ECR → deploy ECS. `T2`
- [ ] **GitHub Actions OIDC federation to an IAM role** — the modern answer: no long-lived AWS keys in CI, ever. *If they ask how you authenticate CI to AWS and you say "access keys in secrets," that's a miss.* `T2`
- [ ] **Deploy strategies** — rolling vs blue/green via CodeDeploy, health-check gating, rollback. `T2`
- [ ] **Migrations and secrets in a deploy** — where schema changes run; Secrets Manager / Parameter Store vs env vars. `T2`

## Section 10 — The system-design set-piece (Tier 1) · *synthesis*

*The highest-leverage hour of the sprint. One diagram containing every noun in the posting.*

- [ ] **"Design a secure, HIPAA-compliant API on AWS that authenticates against Okta"** — drawn cold, under 4 minutes, narrated: the request path, where the token is validated (and why possibly twice), where mTLS sits, what's logged and what isn't, what's encrypted, what you'd alarm on, and what you'd do differently at 100× scale. `T1`
- [ ] **The three follow-ups they will ask** — "what happens when Okta is down?" · "how do you revoke access immediately?" · "where could PHI leak in this design?" *Pre-build all three answers.* `T1`

## Section 11 — Honest positioning & the story bank (Tier 1)

*The section that keeps the other ten from backfiring.*

- [ ] **The have/haven't script** — one clean sentence separating what you've *operated* from what you've *studied*, for AWS ops, mTLS, and HIPAA. Base it on `jobs/natera-sr-fwd-deployed/README.md:37`, which already says it well. `T1`
- [ ] **6–8 STAR stories mapped to JD bullets** — CreatorClip multi-tenant RLS + OAuth publishing; CFO Agent threat model + encryption at rest + 177 tests; Cognizant MCP/agent work at enterprise scale; the Playwright-over-Cypress decision (`CAREER_LOG.md:103`); the sensitive-scope call that cut a feature (`agenda.md:131`). `T1`
- [ ] **Questions to ask them** — about their IdP topology, where they terminate mTLS, and how they handle token revocation. *Asking these proves §3–§5 better than answering does.* `T1`

---

## 🗓 The 7-day map

Peak block (90 min) = the `/learn api` unit · afternoon (60–90 min) = the build issue · evening (20 min) = `/drill` + log.
**Floor** = the ~45-min version that still counts the day. `habits/tracker.md:105` documents six all-or-nothing collapses — the floor exists so a bad day drops to it instead of to zero.

| Day | Peak — `/learn api` | Build issue | Floor |
|---|---|---|---|
| Sun 08-10 | §1 + §2 | Scaffold + Issue 1 | Skills recalibration; read the JD subtext aloud |
| Mon 08-11 | §3 | Issue 2 — Okta tenant, real token | §3 concepts only |
| Tue 08-12 | §4 | Issues 3 + 4 | The 6-item validation checklist, cold |
| Wed 08-13 | §5 | Issues 5 + 6 · **mock #1** | mTLS vs JWT: when each, why both |
| Thu 08-14 | §6 (the path) | Issue 7a — ECR → Fargate → ALB → ACM | Draw the request path from memory |
| Fri 08-15 | §6 (WAF/CloudWatch/API GW) | Issue 7b + Issue 8 | Finish the deploy |
| Sat 08-16 | §7 · §8 · §9 | **Teardown** + `/sharpen` §3–§6 | §8 HIPAA + the honest script |
| Sun 08-17 | §10 + §11 | **Full mock** | The one-page cheat sheet |

**Two mocks are mandatory.** Answering out loud is a different skill from knowing, and it's the one being graded.

---

## 💸 Cost & safety guardrails — non-negotiable

- **Never create an AWS Private CA.** General-purpose mode bills **~$400/month**, prorated from creation, and deleting it does not refund. Short-lived mode is ~$50/mo — still not worth it for a week. §5 uses a **local openssl CA**; you learn PCA's behavior and pricing from docs, and the pricing *is* the interview answer.
- **Never enable Shield Advanced.** ~$3,000/month with a 1-year commitment. Shield Standard is free and already on.
- **Run and tear down within ~2 days.** ALB ~$0.55/day · Fargate 0.25 vCPU ~$0.30/day · WAF $5/web ACL/mo + $1/rule/mo + $0.60/M requests · Route 53 hosted zone $0.50/mo · ACM public certs free. **Target: under $20 total.**
- Route 53 + a public ACM cert require **a domain you control** — confirm before Thursday.
- **Set a $25 AWS Budget alert on day one.** Tag everything `project=secure-api-lab`. Run `docs/TEARDOWN.md` on Saturday.

---

## Connections & Application

*(Populated as units land.)*

- **§1 → §8:** `response_model` is a compliance control. Response filtering enforces HIPAA minimum-necessary at the serialization layer — the same line of code answers a FastAPI question and a compliance question. Say the connection out loud; it's the kind of thing that separates a candidate who studied a list from one who understands a system.
- **§4 → §6:** "Where do you validate the JWT?" stopped being a settled question in November 2025 when ALB gained native JWT verification. Edge validation cuts latency and blocks bad traffic before it costs you compute; in-app validation survives an ALB misconfiguration and knows about business context. Defense in depth = both.
- **§5 → §3:** mTLS and OAuth2 are not alternatives and candidates constantly present them as such. mTLS authenticates the *workload*; the JWT authorizes the *call*. A service mesh doing mTLS still needs tokens for authorization.

## Honest Takeaways

*(Populated as the sprint runs.)*

- **2026-08-10 — the gap was narrower and more specific than the JD made it look.** A full-repo grep returned zero footprint on the entire AWS platform/edge/identity layer — but production FastAPI, async, OAuth2, testing at scale, and CI/CD were all already there and *self-rated as gaps.* Two different problems wearing the same label. Worth remembering the next time a posting looks overwhelming: separate "can't do" from "never had to say."

## Entry Log

*(Links added by `/learn api` at each session's persist step.)*
