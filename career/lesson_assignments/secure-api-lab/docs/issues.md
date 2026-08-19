# Issues — secure-api-lab

Driven by `/issue-workflow <n>`. Dependency-ordered. Each issue closes a section of the roadmap at
`~/workspace/life-log/career/secure-api-engineering/summary.md`.

**No clock** *(removed 2026-08-13 — the role that set it closed before an interview)*. Issue 7 is still the
load-bearing one: it converts *"proven ability to deploy, secure, and operate APIs on AWS"* from a no into a
yes, and it's the only issue that costs money. Everything else can be worked at any pace.

**Struggle-first applies** (issue-workflow standing rule #0): attempt each issue unaided for 10–20 minutes
before engaging. A wrong hypothesis is a great attempt; a blank page is not.

---

**Issue 1: FastAPI skeleton with a real OpenAPI contract**
**Depends on**: none

**What**: A running FastAPI app with a mock patient-records resource, Pydantic v2 request/response models,
and a curated OpenAPI spec that declares its `securitySchemes`.
**Why**: Establishes the surface everything else attaches to, and closes roadmap §1–§2. The PHI-shaped
resource is deliberate — it makes `response_model` filtering a compliance control from the first commit.

**Acceptance criteria**:
- [ ] `uvicorn` serves the app; `/docs` renders
- [ ] At least one `GET` (list, paginated) and one `POST`, both with explicit `response_model`
- [ ] A response model that **deliberately omits fields present on the DB model** — the minimum-necessary demo
- [ ] `lifespan` context manager used (not `@app.on_event`), `Annotated[...]` dependency style throughout
- [ ] `securitySchemes` present in the generated OpenAPI JSON
- [ ] `scripts/export_openapi.py` writes `openapi.json` to disk — the artifact CI will diff later
- [ ] Can explain out loud: 401 vs 403 vs 422, and which of the two endpoints is idempotent

---

**Issue 2: Okta tenant issuing real tokens**
**Depends on**: none (do in parallel with 1 if blocked)

**What**: An Okta developer tenant with a custom authorization server, a custom scope, and a
machine-to-machine app; obtain a real access token via client-credentials and decode it.
**Why**: Closes roadmap §3. Every JWT concept downstream is abstract until a real Okta token is in hand.

**Acceptance criteria**:
- [ ] Free Okta developer tenant created
- [ ] **Custom** authorization server (not the org default) with a custom scope, e.g. `records.read`
- [ ] Service (machine-to-machine) app configured for client credentials
- [ ] `curl` against `/oauth2/<id>/v1/token` returns an access token
- [ ] Token pasted into jwt.io — can name every claim, and identify `iss`, `aud`, `cid`, `scp`, `exp`, `kid`
- [ ] The JWKS endpoint fetched and the `kid` matched to the token header
- [ ] Credentials in `.env` only; `.env` gitignored; `.env.example` committed
- [ ] Can explain out loud: why client-credentials cannot request OpenID scopes

---

**Issue 3: JWT validation + scope authorization as dependencies**
**Depends on**: Issues 1, 2

**What**: A `require_token` dependency validating Okta-issued JWTs against JWKS, plus a `require_scope(...)`
dependency for authorization. **PyJWT, not python-jose.**
**Why**: The core of the whole interview. Closes roadmap §4 and makes §1's "auth belongs in a dependency" real.

**Acceptance criteria**:
- [ ] `pyjwt[crypto]` used; RS256; **algorithms explicitly allow-listed**
- [ ] JWKS fetched and cached; re-fetch triggered only by an unknown `kid`
- [ ] All six checks enforced: signature · `iss` · `aud` · `exp` · `nbf` · algorithm — plus Okta's `cid`
- [ ] `require_scope("records.read")` returns **403** on a valid token missing the scope (not 401)
- [ ] Validation failures log the reason server-side but return a generic client error — no oracle
- [ ] A real Okta token gets 200 against the protected endpoint
- [ ] Can explain out loud: why signature verification precedes reading any claim

---

**Issue 4: The negative test matrix**
**Depends on**: Issue 3

**What**: A pytest suite that mints its own tokens from a local RSA keypair against a fake JWKS, and proves
every rejection path.
**Why**: The JD describes this almost verbatim — "test authentication, authorization, headers, and
request/response flows." Closes roadmap §7.

**Acceptance criteria**:
- [ ] Local RSA keypair + fake JWKS fixture; tests never call the real Okta
- [ ] `dependency_overrides` used to swap the JWKS source
- [ ] Seven cases, each asserting the **correct** status: expired · wrong `aud` · wrong `iss` · bad signature ·
      **`alg: none`** · missing scope (403) · missing/malformed Authorization header (401)
- [ ] One happy-path test asserting 200
- [ ] `httpx.ASGITransport` for the async client
- [ ] Full suite green
- [ ] Can explain out loud: how the RS256→HS256 confusion attack works and which line of code stops it

---

**Issue 5: mTLS with a local private CA**
**Depends on**: Issue 1

**What**: An openssl-generated CA, server cert, and client cert; a TLS listener requiring client certs;
the service extracting the client's subject as an identity.
**Why**: Closes roadmap §5. **Do not use AWS Private CA** — see the cost guardrails.

**Acceptance criteria**:
- [ ] `certs/` generated by a committed, re-runnable script; **`certs/` gitignored**
- [ ] Root CA → server cert and client cert, both signed by it
- [ ] Server requires and verifies client certs against the CA
- [ ] `openssl s_client` **succeeds with** a client cert and **fails without** one — both captured
- [ ] The app reads the client cert subject and maps it to a service principal
- [ ] A code path reading `X-Amzn-Mtls-Clientcert` for the ALB-passthrough case (even if unexercised locally)
- [ ] Can explain out loud: mTLS vs JWT vs both, and why cert rotation is the #1 production failure mode

---

**Issue 6: Structured audit logging with PHI redaction**
**Depends on**: Issues 1, 3

**What**: JSON logging with correlation IDs and an audit trail recording who accessed which record when —
without ever logging the record contents.
**Why**: Closes roadmap §8's most concrete piece. The distinction between *audit logging* and *logging the
data* is the whole HIPAA answer.

**Acceptance criteria**:
- [ ] JSON-structured logs; correlation ID via middleware, propagated to every log line
- [ ] An audit event per protected-resource access: actor (from token `sub`/`cid`), action, resource id, timestamp, outcome
- [ ] A redaction filter; a test asserting a known PHI string **never** appears in captured log output
- [ ] Auth failures logged with reason; tokens themselves never logged
- [ ] Can explain out loud: why the audit log records the *reference* and not the *payload*

---

**Issue 7: Deploy to AWS — ECS Fargate behind an ALB, protected**
**Depends on**: Issues 1, 3, 6

**What**: Containerize, push to ECR, run on Fargate behind an ALB with an ACM cert and a Route 53 record,
fronted by WAF, logging to CloudWatch with an alarm.
**Why**: **The bullet that can't be talked past.** Closes roadmap §6 and makes the §10 diagram something
lived rather than read.

**💸 Guardrails — read before touching the console:**
- **Never create an AWS Private CA** (~$400/mo general-purpose, ~$50/mo short-lived; prorated from creation, no refund)
- **Never enable Shield Advanced** (~$3k/mo, 1-year commitment). Shield Standard is free and already on.
- **Set a $25 Budget alert first.** Tag everything `project=secure-api-lab`. Target under $20 total.
- Requires a domain you control for the ACM cert — confirm before starting.

**Acceptance criteria**:
- [ ] Budget alert set **before** any resource is created
- [ ] Multi-stage Dockerfile, non-root user; image in ECR
- [ ] ECS Fargate task definition with **task role and execution role as separate roles** — can explain the difference
- [ ] Secrets injected via Secrets Manager / SSM, **not** environment literals
- [ ] ALB with an HTTPS listener, ACM DNS-validated cert, health check passing
- [ ] Route 53 alias record resolving to the ALB
- [ ] WAF web ACL with a managed rule group + a rate-based rule, attached — start in **count** mode, then block
- [ ] CloudWatch log group receiving the structured logs; a metric filter on 5xx; one alarm
- [ ] **End-to-end proof**: a real Okta token gets 200 over public HTTPS; a tampered token gets 401
- [ ] No static AWS access keys anywhere in the repo
- [ ] `docs/TEARDOWN.md` written **as this is built**, not after

---

**Issue 8: CI/CD via GitHub Actions with OIDC federation**
**Depends on**: Issue 7

**What**: A pipeline that lints, tests, builds, pushes to ECR, and deploys to ECS — authenticating to AWS
via OIDC federation with no long-lived credentials.
**Why**: Closes roadmap §9. "Access keys in GitHub secrets" is the wrong answer in 2026; this is the right one.

**Acceptance criteria**:
- [ ] Workflow: checkout → ruff → pytest → build → push ECR → update ECS service
- [ ] **GitHub OIDC provider + an assumable IAM role** — zero static AWS keys in secrets
- [ ] IAM role scoped to this repo (and ideally this branch) in its trust policy
- [ ] The OpenAPI spec exported as a build artifact and diffed against the committed one
- [ ] A green run on `main`
- [ ] Can explain out loud: how OIDC federation actually establishes trust, and why it beats a rotated key

---

## Implementation order

1 → 2 (parallel) → 3 → 4 → 5 → 6 → 7 → 8. Issues 1 and 2 are independent; start 2 first if Okta signup
needs to bake. **Issue 7 is the load-bearing one** — if the week compresses, cut Issue 8 before Issue 7.
