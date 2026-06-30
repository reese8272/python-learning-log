# Mid-Level Python Developer — Interview Prep Roadmap

**What this is:** A ground-up technical curriculum to walk into a specific interview — **mid-level Python developer, $115k, building high-performance FastAPI services that serve weather datasets (Radar, Satellite, Numerical Weather Models)** — and demolish it. Built the same way as the AI curriculum: each unit is learned in-catalog via `/learn` (researched live against current docs), then handed to `/sharpen` (defend cold) and `/drill` (retain). This roadmap is the *what to cover*; the teaching is generated fresh each session so it never goes stale.

**The framing — build UP from zero.** Assume nothing is owned. Every item starts at `[ ]`, even ones you ship at work today, because the goal isn't *exposure* — it's being able to **defend every rung cold at the mid-level bar.** A thing you use daily but can't explain *why this over that* is a thing you'll fumble when the interviewer pushes one level past the happy path. Re-derive it. Sections are ordered bottom-up: each rung rests on the one below it.

**Source of truth:** the job posting itself (responsibilities + requirements, transcribed in Interview Intel below) and `career/helpful_notes_and_guides/AI Engineering Master Guide.md` for the mastery standard ("can I explain why THIS over THAT?").

**The pipeline:**
```
/learn          →   /sharpen        →   /drill
acquire (here)      defend cold         retain (spaced rep)
researched live     100% / tier bar     against forgetting curve
```

**Tiers** (interview-priority weighted, not generic importance):
- **Tier 1 — They WILL test this** → 100%, "can teach it." Mechanism + why-this-over-that + failure mode. These are the requirements stated explicitly in the posting.
- **Tier 2 — Likely probed / sets you apart** → Pareto 80/20, "explain the decision." Nice-to-haves and depth that turns a pass into a "we want this person."

**Status keys:** `[ ]` not started · `[~]` in progress / needs another pass · `[x]` learned (date) → can defend cold → enters `/sharpen` then `/drill` rotation.

**How to use:** Work top-down within a section; sections are ordered by dependency. Don't skip a `[ ]` because you "already know it" — if you can't pass the explain-back at the tier bar, it isn't owned yet. When `/learn` finishes a unit, it logs to `reflection_log/`, marks it here, and (optionally) drops it into `career/concept_queue.md` for a defense pass.

**Every unit leaves a worksheet.** Same as the AI curriculum: each `/learn` unit produces a self-contained, runnable lesson-assignment at `career/lesson_assignments/YYYY-MM-DD_<unit>.py` (template: `2026-06-22_llm-call-anatomy.py`). Shape is fixed — targeting soliloquy → Part 1 coding exercises (boilerplate pre-filled, **TODOs state intent, never the solution line**) → Part 2 concept questions answered cold + a one-line "interviewer version" of each → a red/green test runner → a gated answer key. A unit isn't banked until its worksheet runs green **and** you can say the concepts cold.

---

## 🎯 Interview Intel — what they actually asked for

**Verbatim from the posting:**

> **Responsibilities:** Design and develop high-performance Python FastAPIs · Enable seamless access to datasets such as Radar, Satellite, and Numerical Weather Models · Collaborate in an Agile environment · Contribute to enterprise-grade data solutions.
>
> **Requirements:** 2 yrs professional experience or equivalent CS degree · Strong Python + hands-on FastAPI · RESTful web services + Git · Build automation (Jenkins/Hudson) · Agile.
>
> **Nice to have:** Agile experience · JIRA.

**How to read it (the subtext):**
- **"high-performance FastAPI"** → they care about async, the event loop, not blocking it, pagination/streaming for big payloads, and worker/deployment topology. Not just "can you write an endpoint." → **§3, §4.**
- **"Radar, Satellite, Numerical Weather Models"** → this is a **geospatial / scientific-data shop.** The data is huge gridded arrays in formats most web devs have never touched (GRIB2, NetCDF, HDF5, Zarr). Knowing this domain even at altitude is the single biggest *wow* lever — most candidates won't. → **§5.**
- **"enterprise-grade data solutions"** → reliability, versioned APIs, contracts, auth, observability. → **§4, §9.**
- **"Jenkins or Hudson"** → the one stated requirement that's a genuine cold gap for you. Hudson is literally Jenkins' ancestor (Oracle fork → renamed). Learn Jenkins; you've covered both. → **§7.**
- **Agile / JIRA** → low-stakes, mostly vocabulary + stories from real work. Don't over-invest. → **§8.**

**Where to spend the peak window:** §3 (FastAPI depth) and §5 (weather data) — that's where the interview is won or lost. §7 (Jenkins) is a focused half-day to close the one real gap. Everything else is confirm-and-defend.

---

## ⚠ Currency Watch — research these live, don't teach from memory

The ecosystem moved; teach the *current* pattern.
- **Pydantic v2** is the world now — `pydantic-core` is Rust, ~5–50× faster than v1. `@validator`→`@field_validator`, `@root_validator`→`@model_validator`, `.dict()`→`.model_dump()`, `BaseSettings` moved to **`pydantic-settings`**, `Config` class → `model_config = ConfigDict(...)`. FastAPI is fully v2-native. If you teach v1 syntax in the interview you date yourself instantly.
- **FastAPI `lifespan`** (async context manager) replaced the deprecated `@app.on_event("startup"/"shutdown")`.
- **`Annotated[...]` dependency style** (`Annotated[Item, Depends(get_item)]`) is the current idiom over the old `= Depends(...)` default-value form.
- **NumWeatherModel data on the cloud** has shifted from "download the GRIB file" toward **Zarr / Cloud-Optimized GeoTIFF + STAC catalogs + range-request subsetting** (NODD, AWS Open Data, Pangeo). Know both the legacy file formats and the cloud-native access pattern.
- **HTTPX + `httpx.ASGITransport`** is the current async test client pattern; `starlette.testclient.TestClient` still works for sync.

Re-verify per unit.

---

## Section 1 — Python Core, at the depth a mid-level interview probes (Tier 1)

*The floor. You write Python daily — this section is about defending the parts an interviewer pushes on past the happy path. If you can't explain the GIL or why a generator saves memory, the rest doesn't matter.*

- [x] **Data model & idiomatic Python** (2026-06-29) — mutability, identity vs equality (`is` vs `==`), truthiness, `__dunder__` methods, why everything's an object. `T1` *(2026-06-26 — taught: `is`/`==` + small-int cache −5..256, mutable-default evaluated-once + None sentinel, `__eq__` nulls `__hash__` + the hash invariant, first-class functions → decorators/Depends. Worksheet: lesson_assignments/mid-py-1.1-data-model.py. 2026-06-29 — worksheet 13/13 green; all 4 explain-backs cold (Q2 mutable-vs-immutable-sentinel + Q4 "generators" slips corrected). BUILD BANKED: lesson_assignments/mid-py-1.1-grid-cache.py — GridCell value object as a weather-cache key; wrote `__eq__`/`__hash__` cold, caught two own bugs after coaching (`__hash__` must return `hash(tuple)` not the tuple; `__eq__` needs `isinstance` guard to stay total). 5/5 green. → enters /sharpen. Idiom drilled: `return <bool expr>`.)*
- [~] **Type hints in earnest** — `typing` module, `Optional`/`Union`/`|`, generics, `Protocol`, why hints matter for FastAPI (they ARE the API contract). `T1` *(2026-06-30 — taught: hints inert at runtime (`__annotations__`), nullable≠required two-axis (`| None` = type, default = required), Pydantic v2 makes `x: int|None` REQUIRED → 422 (v1's implicit-None default removed — staleness flag), builtin generics `list[str]`/`dict[str,float]`, `Protocol` structural typing for vendor-SDK shapes + `@runtime_checkable`. All 3 explain-backs cold. Worksheet: lesson_assignments/mid-py-1.2-type-hints.py. BUILD PENDING: ForecastQuery four-corner truth-table model. → mark `[x]` once build + worksheet run green.)*
- [ ] **Generators & iterators** — `yield`, lazy evaluation, when a generator saves memory vs a list; the streaming-large-dataset connection. `T1`
- [ ] **Decorators & closures** — what `@something` actually does, writing one, why FastAPI/pytest lean on them. `T1`
- [ ] **Context managers** — `with`, `__enter__/__exit__`, `contextlib`, why they matter for files/connections/sessions. `T1`
- [ ] **The GIL, threading vs multiprocessing vs asyncio** — what the GIL is, I/O-bound vs CPU-bound, which concurrency model for which, why FastAPI is async. *The single most likely "do you actually understand it" question.* `T1`
- [ ] **`async`/`await` & the event loop** — coroutines, the loop, `await` as a yield point, what blocks the loop and why that kills a server. *Prereq for everything in §3.* `T1`
- [ ] **Exceptions & error design** — custom exception classes, EAFP vs LBYL, where to catch, exception chaining. `T2`
- [ ] **Testing with pytest** — fixtures, parametrize, mocking, what's worth testing (Pareto). `T1`
- [ ] **Packaging & environments** — `venv`/`uv`/`poetry`, `pyproject.toml`, dependency pinning, why reproducible builds matter for CI. `T2`

## Section 2 — HTTP & RESTful Web Services (Tier 1)

*The conceptual layer under FastAPI. The posting names "RESTful web services" as a requirement — you need the principles, not just the framework that implements them.*

- [ ] **HTTP fundamentals** — request/response, methods (GET/POST/PUT/PATCH/DELETE), status codes (and which to return when), headers, content negotiation. `T1`
- [ ] **REST principles** — resources & URIs, statelessness, representations, why REST and not RPC; Richardson Maturity Model at altitude. `T1`
- [ ] **Idempotency & safety** — which verbs are idempotent/safe and why it matters for retries and reliability. `T1`
- [ ] **API design: pagination, filtering, sorting** — offset vs cursor pagination, why cursor for large/changing datasets (directly relevant to serving big weather data). `T1`
- [ ] **API versioning** — URL vs header vs media-type versioning; why you version at all; enterprise contract stability. `T1`
- [ ] **Error contracts** — consistent error envelopes, problem+json, not leaking internals. `T2`
- [ ] **REST vs GraphQL vs gRPC** — the judgment call: when each, why REST is the right default for a public data API. `T2`

## Section 3 — FastAPI to the "high-performance" bar (Tier 1 — the headline)

*The #1 stated requirement. You ship FastAPI already — this section is about being able to defend every design choice and the performance story cold. Build a tiny throwaway API per unit; don't just read.*

- [ ] **The ASGI mental model** — what ASGI is vs WSGI, why async servers (uvicorn) beat sync (gunicorn/WSGI) for I/O-bound APIs, where Starlette fits under FastAPI. `T1`
- [ ] **Path / query / body params & request parsing** — how FastAPI maps a request to typed function args; automatic validation. `T1`
- [ ] **Pydantic v2 models** — `BaseModel`, field types, validators (`@field_validator`/`@model_validator`), serialization (`model_dump`), why pydantic-core (Rust) is fast. *The validation layer is half of FastAPI's value.* `T1`
- [ ] **Response models & `response_model`** — shaping output, excluding fields, separate input/output schemas, status codes. `T1`
- [ ] **Dependency Injection (`Depends`)** — the killer feature: shared logic, `yield` dependencies (setup/teardown for DB sessions), sub-dependencies, dependency overrides in tests. *Interviewers love asking how DI works here.* `T1`
- [ ] **`async def` vs `def` path operations** — when FastAPI runs your handler in the threadpool vs the loop, why a blocking call in an `async def` handler is a bug, `run_in_threadpool`. *The "high-performance" question lives here.* `T1`
- [ ] **Error handling** — `HTTPException`, custom exception handlers, validation error responses. `T1`
- [ ] **Streaming & large responses** — `StreamingResponse`, generators as response bodies, serving large arrays without loading them all into memory. *Direct line to serving big weather datasets.* `T1`
- [ ] **Background tasks vs Celery vs async** — FastAPI `BackgroundTasks` for light work, when you need a real queue (Celery) instead, why. `T1`
- [ ] **Middleware, CORS, lifespan** — request/response middleware, the `lifespan` async context manager (replaces `on_event`), startup DB pools. `T2`
- [ ] **Auth in FastAPI** — `OAuth2PasswordBearer`, API-key dependencies, JWT validation as a dependency. `T1`
- [ ] **Testing FastAPI** — `TestClient` / async `httpx.ASGITransport`, dependency overrides, fixture-based DB setup. `T1`
- [ ] **Performance & deployment topology** — uvicorn workers, gunicorn+uvicorn-worker, connection pooling, when async actually helps vs hurts, profiling an endpoint. *Be able to tell the "I made this endpoint faster by X" story.* `T1`
- [ ] **Auto OpenAPI / docs** — how the schema is generated, why typed code = free docs = enterprise-friendly. `T2`

## Section 4 — Data Access Layer for an API (Tier 1)

*"Enable seamless access to datasets" + "enterprise-grade data solutions." How the API actually talks to storage, performantly and safely.*

- [ ] **SQLAlchemy 2.0 + async** — the ORM, async sessions, the session-per-request pattern via `Depends`, why a yield-dependency. `T1`
- [ ] **Connection pooling** — what a pool is, why it matters under load, pool sizing, the #1 silent performance killer. `T1`
- [ ] **N+1 queries & query performance** — spotting it, eager loading, why it tanks a data API. `T1`
- [ ] **Pagination & streaming from the DB** — server-side cursors, not loading a million rows into memory. `T1`
- [ ] **Caching layer** — Redis as a read cache, cache invalidation, when caching a weather query is safe (and when stale data is dangerous). `T2`
- [ ] **SQL vs NoSQL vs object storage for big data** — why gridded weather data lives in object storage (S3) + a catalog, not a relational row. `T2`

## Section 5 — Serving Weather Data: Radar, Satellite & Numerical Weather Models (Tier 1 — the wow factor)

*The domain edge. Most candidates for a generic "Python dev" role know nothing here — showing up fluent in GRIB/NetCDF/xarray and the cloud-native access pattern is what turns "qualified" into "we need this person." Learn it at altitude; you don't need to be a meteorologist, you need to speak the data fluently.*

- [ ] **What Numerical Weather Models ARE** — gridded forecasts (GFS, HRRR, ECMWF, NAM), what a "model run" / cycle / forecast hour is, dimensions (lat × lon × level × time × variable). The mental model under all of it. `T1`
- [ ] **Radar & Satellite data** — NEXRAD Level II/III (radar), GOES (satellite) at altitude: what they measure, why they're huge, why they need specialized access. `T1`
- [ ] **The file formats** — **GRIB2** (weather model standard), **NetCDF** (scientific arrays + metadata), **HDF5** (hierarchical), and why these exist instead of CSV/JSON. `T1`
- [ ] **The scientific Python stack** — **xarray** (labeled N-D arrays — the central tool), NumPy under it, `cfgrib`/`netCDF4`/`h5py` engines, Dask for out-of-memory arrays. *If you can talk xarray confidently you've already won this round.* `T1`
- [ ] **Cloud-native access** — **Zarr** (chunked array storage for the cloud), **Cloud-Optimized GeoTIFF (COG)**, **STAC** catalogs, range-request subsetting; why "download the whole GRIB" is the old way. ⚠ research live — this is moving fast. `T1`
- [ ] **Serving it through an API** — subsetting (give me this variable, this bbox, this time), why you never load the full array, streaming/tiling responses, the connection back to §3 StreamingResponse. *This is the literal job.* `T1`
- [ ] **Geospatial standards & coordinates** — OGC APIs (WMS/WCS/Features), CRS/projections at altitude, bounding boxes. `T2`
- [ ] **Where the data lives** — NOAA Open Data Dissemination (NODD), AWS/GCP open weather buckets, the Pangeo ecosystem. Shows you know the real-world supply chain. `T2`

## Section 6 — Git & Source Control (Tier 2 — confirm and defend)

*Stated requirement, but table-stakes. Goal: zero fumbles on the workflow questions, not deep internals.*

- [ ] **Core model** — commits, branches, the index/staging area, what a commit actually is (snapshot + parent). `T2`
- [ ] **Branching & collaboration** — feature branches, PRs, code review flow, why a team uses them. `T2`
- [ ] **Merge vs rebase** — what each does to history, when to use which, why rebase a feature branch but never shared history. `T2`
- [ ] **Resolving conflicts** — the mechanics, calmly. `T2`
- [ ] **Git in a CI context** — webhooks/triggers, what the build server pulls, tags & artifacts. `T2` *(bridges to §7)*

## Section 7 — Build Automation & CI/CD: Jenkins / Hudson (Tier 1 — the real gap)

*The one explicit requirement that isn't in your daily stack. Hudson = Jenkins' direct ancestor (same lineage after the Oracle/Sun fork), so learning Jenkins covers both — say exactly that if asked. Close this gap deliberately; it's small but it's named in the requirements.*

- [ ] **What CI/CD actually is** — continuous integration vs continuous delivery vs deployment, why automated build/test/deploy, the value to an enterprise team. `T1`
- [ ] **What Jenkins is (and Hudson's relation)** — the automation server, master/agent (controller/node) model, the plugin ecosystem, the Hudson→Jenkins history in one sentence. `T1`
- [ ] **The Jenkins pipeline** — the **Jenkinsfile**, declarative vs scripted, `stages`/`steps`/`agent`, pipeline-as-code in the repo. `T1`
- [ ] **A real pipeline for a Python API** — checkout → install deps → lint → pytest → build (Docker image) → deploy; what each stage does. *Be able to sketch this on a whiteboard.* `T1`
- [ ] **Triggers, artifacts, credentials** — webhook/poll triggers, archiving build artifacts, secrets/credentials management. `T2`
- [ ] **Jenkins vs GitHub Actions / GitLab CI** — the judgment call: when each, why an enterprise might run self-hosted Jenkins. `T2`

## Section 8 — Agile & JIRA (Tier 2 — vocabulary + stories)

*Nice-to-haves. You already work in Agile per your resume — this is about naming the ceremonies correctly and having a clean "how I work in a sprint" story. Don't over-invest; an afternoon, tops.*

- [ ] **Scrum vs Kanban** — the two frames, sprints vs continuous flow, when each. `T2`
- [ ] **Scrum ceremonies & roles** — sprint planning, daily standup, review, retro; PO vs Scrum Master vs dev; story points & velocity at altitude. `T2`
- [ ] **JIRA mechanics** — epics/stories/tasks/subtasks, the board, workflow states, linking a branch/PR to a ticket. `T2`
- [ ] **Your Agile story** — a crisp 60-second answer to "tell me how you work in an Agile team," drawn from real Cognizant work. `T2`

## Section 9 — Production & System Design (Tier 2 — the senior signal)

*"Enterprise-grade" and "high-performance" are senior words. You won't be asked to architect a distributed system at mid-level, but signaling you think about this stuff separates you from the pack.*

- [ ] **12-factor app** — config in env, stateless processes, why it matters for scaling an API. `T2`
- [ ] **Docker for a Python API** — Dockerfile, multi-stage builds, why containers for reproducible deploys; ties to §7. `T2`
- [ ] **Observability** — structured logging, request IDs, health checks, metrics; how you'd debug a slow endpoint in prod. `T2`
- [ ] **Scaling a read-heavy data API** — horizontal scaling, caching, CDN/edge for static data, where the bottleneck is. `T2`
- [ ] **Reliability basics** — timeouts, retries, graceful degradation, rate limiting. `T2`

---

## Connections & Application

- **The interview is won in §3 and §5.** FastAPI depth proves you meet the bar; weather-data fluency proves you're *the* candidate. Everything else is removing reasons to say no.
- **Build before you bank** (CLAUDE.md): the strongest possible prep is a tiny real artifact — a throwaway FastAPI service that subsets a real GRIB/NetCDF file with xarray and streams the result. That one project would touch §1 (async), §2 (REST), §3 (FastAPI/streaming), §4 (data access), and §5 (the whole domain) at once, and gives you a concrete "here's something I built that does exactly your job" story. *Strongly consider making this the capstone of this prep.*
- **Defense, not exposure.** Each `[x]` should mean you passed an explain-back at the tier bar — feed landed units into `/sharpen` and run a mock interview against §3/§5/§7 before the real thing.
- **The honest gap is §7.** Be deliberate about Jenkins; it's the only named requirement you can't currently tell a story about. A half-day and a sketched pipeline closes it.

## Honest Takeaways

*(fill as units land — what prep is paying off, where the interview pressure actually is, what surprised you)*

## Entry Log

- [2026-06-26](reflection_log/2026-06-26.md) — §1.1 "Data model & idiomatic Python" (Tier 1): `is`/`==` + small-int cache, mutable-default evaluated-once, `__eq__`/`__hash__` contract, first-class functions. 3/4 explain-back cold; build + worksheet assigned.
- 2026-06-29 — §1.1 **banked `[x]`**: worksheet 13/13 green, all 4 explain-backs cold (Q2 + Q4 slips corrected), and build banked (mid-py-1.1-grid-cache.py — GridCell value object as a weather-cache key, written cold, two self-caught bugs). Enters `/sharpen`. Next: §1.2 type hints.
- [2026-06-30](reflection_log/2026-06-30.md) — §1.2 "Type hints in earnest" (Tier 1) `[~]`: nullable≠required two-axis, Pydantic v2 `Optional` no longer implies a default (422 staleness flag), builtin generics, `Protocol` structural typing. All 3 explain-backs cold; build (four-corner ForecastQuery) + worksheet assigned. Mark `[x]` once green. Next: §1.3 Generators & iterators.
