# Engineering Roadmap
**Target:** Senior-level AI Engineer (Agentic Systems)  
**Daily commitment:** 2 hrs main session + 30 min morning cherry-pick  
**Weekly commitment:** 45 min Sunday system design + 10-15 min mid-week recap  

---

## How Every Week Works

| Block | Time | What It Is |
|---|---|---|
| Morning cherry-pick | 30 min, daily | Boot.dev concept or a generated coding problem. Logged in Python log. |
| Main session | 2 hrs, daily | Course content, labs, or project (phase-dependent) |
| System design Sunday | 45 min | Study one system design concept. Take notes. |
| System design recap | 10-15 min, 2x/week | Re-read your notes. No new content. Just solidifying. |

**Python log rule:** Every week has a log entry. Concept summaries, code snippets, questions that came up, and the system design notes all go there. If you can't write it in your own words, you don't own it yet.

---

## Phase Overview

```
Weeks 1–6  │  LangChain / LangGraph / MCP Course
Weeks 7–8  │  Capstone Prep (Redis + FastAPI cherry-picks, architecture design)
Weeks 9–12 │  Portfolio Project (capstone only)
```

---

## PHASE 1: LangChain / LangGraph / MCP (Weeks 1–6)

> **Rule for this phase:** Learn the concept in the course first. Then immediately apply it in whatever lab or mini-project is built into the course. No skipping labs. The project waits until you've earned it.

---

### Week 1 — LangChain Foundations

**Main session (2 hrs/day):**  
LangChain core — models, prompt templates, chains, LCEL (LangChain Expression Language). Understand what a "chain" actually is. Work all built-in labs.

**Morning cherry-pick (30 min, daily):**  
Git workflows. Branching strategy, meaningful commit messages, pull requests, rebasing basics. This is professional hygiene — it will matter in code reviews.

**System design this week:**  
**REST API Design** — HTTP methods (GET/POST/PUT/DELETE), status codes, request/response cycle, what makes an API RESTful. This is the backbone of FastAPI later.

**Python log entry should include:**  
- What LCEL actually does under the hood (in your own words)
- A chain you built and what each piece does
- REST API design notes

---

### Week 2 — LangChain Tools, Memory & RAG

**Main session:**  
LangChain tools and tool-calling. Memory types (buffer, summary, vector). Basic RAG pipeline — retriever + chain. Work all labs.

**Morning cherry-pick:**  
Python advanced patterns — decorators, context managers (`with` statements), generators, and `async/await` basics. These will show up constantly in LangGraph and FastAPI.

**System design this week:**  
**Databases — SQL vs NoSQL** — When do you use PostgreSQL vs a vector DB vs Redis? What does "schema" mean and why does it matter? How does indexing work conceptually?

**Python log entry should include:**  
- The RAG pattern drawn out (retriever → context → LLM → response)
- What tool-calling actually does at the API level
- SQL vs NoSQL decision framework (when to use which)

---

### Week 3 — LangGraph Foundations

**Main session:**  
LangGraph — state, nodes, edges, `StateGraph`. Build your first graph from scratch. Understand what "state" means in a graph vs in a regular function. Work all labs.

**Morning cherry-pick:**  
Docker fundamentals. What is a container vs a VM? Writing a Dockerfile. Building and running an image. This directly applies to your portfolio project infrastructure.

**System design this week:**  
**Caching** — What it is, LRU eviction, write-through vs write-back, cache invalidation. This is a preview of Redis. Pay attention — you'll use this in Weeks 7 and 9+.

**Python log entry should include:**  
- LangGraph state machine mental model (draw it out, even if rough)
- A node you built and what it does
- Caching patterns reference (cache hit, cache miss, invalidation)

---

### Week 4 — LangGraph Multi-Agent Systems

**Main session:**  
LangGraph multi-agent — supervisor patterns, subagent nodes, tool nodes, human-in-the-loop flows. This is where things get real. Go slower here if you need to. Work all labs.

**Morning cherry-pick:**  
Docker Compose — multi-container apps, service networking, volumes, `.env` files. You will write a `docker-compose.yml` in Week 9. Don't let it be your first time seeing it.

**System design this week:**  
**Authentication & Authorization** — JWT (what it is, how it works), API key patterns, OAuth2 overview, the difference between authn and authz. Directly applicable to your job.

**Python log entry should include:**  
- Supervisor pattern diagram (even sketched is fine)
- How human-in-the-loop actually pauses and resumes a graph
- JWT flow: how a token is issued, signed, and verified

---

### Week 5 — MCP Foundations

**Main session:**  
MCP — protocol overview, server/client architecture, how tools are defined and called, how MCP connects to LangGraph. Work all labs.

**Morning cherry-pick:**  
HTTP and networking concepts — TCP/IP, DNS, TLS/HTTPS, what happens when you make an API call at the network level. Boot.dev teaches this well even in the Go track — use the concept, not the Go implementation.

**System design this week:**  
**Rate Limiting & API Security** — Token bucket vs leaky bucket algorithms, why rate limiting matters, DDoS basics. Read OWASP Top 10 this week. All 10 items. It's ~2 hours total and it's the professional literacy baseline.

**Python log entry should include:**  
- MCP mental model: server exposes tools → client calls them → LLM uses them
- OWASP Top 10 — one sentence each on what the vulnerability is and how to guard against it
- Rate limiting patterns

---

### Week 6 — MCP Advanced + Full Integration Labs

**Main session:**  
MCP advanced — multi-MCP orchestration, complex tool definitions, error handling in tools, any remaining built-in course labs and projects. This is your Phase 1 capstone week. Don't rush it.

**Morning cherry-pick:**  
Python packaging and environment management — `pyproject.toml`, `poetry` or `uv`, virtual environments, managing dependencies. You'll need this when your portfolio project has 15 dependencies.

**System design this week:**  
**Async Patterns & Event-Driven Architecture** — `async/await` at the architecture level, what a message queue is (Kafka, RabbitMQ conceptually), when you'd use async vs sync. This is increasingly relevant for agentic systems.

**Python log entry should include:**  
- End-to-end integration: how a user request flows from FastAPI → LangGraph agent → MCP tool → back
- Full architecture sketch (even rough)
- Async patterns reference

---

## PHASE 2: Capstone Prep (Weeks 7–8)

> **What changes:** Morning cherry-picks are no longer Boot.dev topics. They are now **Redis** and **FastAPI exclusively.** The main session shifts from course consumption to review, consolidation, and architecture design. No new course content. You are getting ready to build.

---

### Week 7 — Redis Deep Dive

**Main session (2 hrs/day):**  
Review Phase 1 notes. Write a self-assessment: what do you fully own? What's fuzzy? Fill the gaps. Start reading the FastAPI official docs (not a tutorial — the actual docs). Understand the structure before you use it.

**Morning cherry-pick — Redis (all week):**  
- Day 1: Data structures — strings, lists, hashes, sets, sorted sets. What each is for.  
- Day 2: TTL and expiration. How caching with Redis actually works in code.  
- Day 3: Pub/Sub pattern. How Redis can act as a message broker.  
- Day 4: Redis in Python — `redis-py` basics. Connect, set, get, expire.  
- Day 5: Redis + Docker — running Redis in a container, connecting from your app.

**System design this week:**  
**Distributed Systems Basics** — CAP theorem (Consistency, Availability, Partition tolerance — pick 2). What "eventual consistency" means. Why distributed systems fail. This will inform how you think about your project's architecture.

**Python log entry should include:**  
- Redis data structure cheat sheet (what to use when)
- Code snippets: connect to Redis, cache a result, set TTL, pub/sub example
- CAP theorem in your own words with a real example

---

### Week 8 — FastAPI Deep Dive + Architecture Design

**Main session (2 hrs/day):**  
**Design the project on paper before writing a single line of code.**  
- Define all endpoints (method, path, request body, response body)  
- Define all data models (Pydantic schemas)  
- Map the agent flow (what triggers what, what returns what)  
- Write the full architecture doc and save it to your Python log  
- Draw the system design diagram (even in ASCII or on paper)  

This document becomes your spec. You build against it in Weeks 9–12.

**Morning cherry-pick — FastAPI (all week):**  
- Day 1: Routing, path/query parameters, response models  
- Day 2: Pydantic models — validation, nested models, optional fields  
- Day 3: Dependency injection — `Depends()`, what it's for, how to use it  
- Day 4: Async endpoints — `async def` in FastAPI, background tasks  
- Day 5: Middleware and error handling — global exception handlers, logging middleware

**System design this week:**  
**Observability** — Logging vs metrics vs tracing. Structured logging (JSON logs). What you'd add to a production system so you can debug it when it breaks. You will implement basic logging in Week 12.

**Python log entry should include:**  
- FastAPI reference sheet (routing, Pydantic, DI, async — one example each)  
- **Project architecture document** (this is the main deliverable of Week 8)  
- Observability notes: what you'll log and where

---

## PHASE 3: Portfolio Project / Capstone (Weeks 9–12)

> **Rule for this phase:** No new course content. Cherry-picks are now **project-driven** — if you hit a wall on something specific, that's your cherry-pick that day. System design continues on the same schedule.

> **"Struggle first, AI second" applies here without exception.** Before reaching for Claude Code on any implementation, spend at least 20 minutes attempting it yourself. Document what you tried and where you got stuck. Then bring that context to the AI session.

---

### Week 9 — Infrastructure First (No Agents Yet)

**Main session goal:**  
Get the skeleton standing. No agent logic this week.

- Docker Compose up with all services: FastAPI, PostgreSQL, Redis  
- FastAPI app running and reachable  
- Database connection established, basic health check endpoint working  
- Redis connection established  
- `.env` file handling for secrets (never hardcoded)  
- Basic project structure following your architecture doc  

**Cherry-pick this week:**  
Whatever you hit a wall on. Common candidates: Docker networking between services, SQLAlchemy setup with PostgreSQL, environment variable handling.

**System design this week:**  
**Secrets & Security in Production** — `.env` files, never committing API keys, secrets management patterns, how production systems handle credentials.

---

### Week 10 — Agent Layer

**Main session goal:**  
Wire up the LangGraph agent system against the running infrastructure.

- Planner, Researcher, Synthesizer nodes implemented  
- State schema defined and working  
- Agents connected to FastAPI via an endpoint  
- Basic end-to-end flow working (even if slow or rough)  
- Error handling on agent failures (what happens if a node throws?)

**Cherry-pick this week:**  
Project-driven. Likely candidates: LangGraph state debugging, async agent invocation from FastAPI.

**System design this week:**  
**Scalability Patterns** — Horizontal vs vertical scaling, stateless service design (why your FastAPI app should be stateless), connection pooling for databases.

---

### Week 11 — MCP Integration + Authentication

**Main session goal:**  
Production-readiness pass.

- MCP tools wired into the agent system  
- API key authentication on FastAPI endpoints (`Depends()` auth middleware)  
- OWASP checklist pass — go through your Top 10 notes and check each item against your code  
- Redis caching integrated where it makes sense (e.g., caching repeated research queries)

**Cherry-pick this week:**  
Project-driven. Likely candidates: MCP tool error handling, JWT vs API key implementation decision.

**System design this week:**  
Free pick — review whichever previous concept you feel weakest on.

---

### Week 12 — Polish, Testing & Documentation

**Main session goal:**  
Ship something you'd put in front of a hiring manager.

- Structured logging added (JSON format, request IDs, agent step logging)  
- Basic pytest coverage on critical paths (endpoint tests, agent unit tests)  
- Error handling is explicit everywhere — no bare `except Exception`  
- README written: what it is, how to run it, architecture overview  
- Architecture diagram added (even a clean ASCII version works)  
- Final Python log entry: what you built, what you learned, what you'd do differently

**Cherry-pick this week:**  
pytest — fixtures, mocking external calls, testing async functions.

**System design this week:**  
**System Design Review** — Pick the design that is most directly reflected in what you just built. Write a short comparison: how does your project align with the pattern? Where did you deviate and why?

---

## Reference: System Design Schedule (Full 12 Weeks)

| Week | Topic | Why It Matters Now |
|---|---|---|
| 1 | REST API Design | Foundation for FastAPI |
| 2 | Databases: SQL vs NoSQL | PostgreSQL + vector DB decisions |
| 3 | Caching | Redis preview |
| 4 | Authentication & Authorization | Job requirement, Week 11 implementation |
| 5 | Rate Limiting & API Security + OWASP | Direct job requirement |
| 6 | Async & Event-Driven Architecture | LangGraph + FastAPI async |
| 7 | Distributed Systems & CAP Theorem | Multi-service architecture awareness |
| 8 | Observability | Week 12 logging implementation |
| 9 | Secrets & Production Security | Week 9 implementation |
| 10 | Scalability Patterns | Production thinking |
| 11 | Free pick (weakest topic) | Gap closure |
| 12 | Review: your project's architecture | Synthesize what you built |

---

## Reference: Cherry-Pick Schedule

| Weeks | Topic | Source |
|---|---|---|
| 1 | Git workflows | Boot.dev |
| 2 | Python advanced (decorators, generators, async) | Boot.dev |
| 3 | Docker fundamentals | Boot.dev |
| 4 | Docker Compose | Boot.dev |
| 5 | HTTP & networking concepts | Boot.dev |
| 6 | Python packaging & env management | Boot.dev |
| 7 | Redis (all week, systematic) | Official docs + redis-py |
| 8 | FastAPI (all week, systematic) | Official FastAPI docs |
| 9–12 | Project-driven (whatever you hit a wall on) | Whatever is blocking you |

---

## What "Done" Looks Like at Week 12

- A running, Dockerized AI research assistant with a FastAPI interface, LangGraph multi-agent system, MCP tool integration, PostgreSQL persistence, Redis caching, API key auth, structured logging, and basic test coverage.
- A Python log with 12 weeks of documented learning, system design notes, and architecture decisions.
- The ability to explain every line of that project — what it does, why it's there, and what you'd change.
- A resume entry that reflects real system design thinking, not "used LangGraph to build a chatbot."

---

---

## Resources

These are the non-course references that support the roadmap. Official sources only — no tutorials, no YouTube, no aggregators.

---

### Security & Standards

| Resource | What It Is | Link |
|---|---|---|
| OWASP Top 10 | The 10 most critical web application security risks. Read once in Week 5, reference on every build. | https://owasp.org/www-project-top-ten/ |
| OWASP API Security Top 10 | API-specific version of OWASP. More directly applicable to FastAPI work than the general list. | https://owasp.org/www-project-api-security/ |
| JWT.io | Interactive JWT decoder + full spec explanation. Use this any time you're implementing auth. | https://jwt.io/introduction |

---

### Code Quality

| Resource | What It Is | Link |
|---|---|---|
| PEP 8 — Python Style Guide | The official Python style standard. Naming conventions, spacing, imports — the rules that make code readable. | https://peps.python.org/pep-0008/ |
| Ruff — Python Linter | A fast linter that enforces PEP 8 and catches bugs automatically. Should be in every Python project from day one. | https://docs.astral.sh/ruff/ |
| Google Python Style Guide | How Google writes Python at scale. Good complement to PEP 8 — covers docstrings, comments, and project structure. | https://google.github.io/styleguide/pyguide.html |

---

### System Design & Architecture

| Resource | What It Is | Link |
|---|---|---|
| System Design Primer | The most thorough free system design reference on the internet. Use it to go deeper on any weekly system design topic. | https://github.com/donnemartin/system-design-primer |
| Twelve-Factor App | The 12 principles behind building maintainable, scalable web apps. Directly relevant to your Docker + FastAPI setup. | https://12factor.net/ |
| High Scalability Blog | Real-world architecture teardowns of companies like YouTube, Twitter, and Slack. Makes system design feel concrete. | http://highscalability.com/ |

---

### Infrastructure

| Resource | What It Is | Link |
|---|---|---|
| Docker Compose File Reference | Dockerfile reference, Compose spec, networking — the authoritative source. Bookmark the Compose file reference specifically. | https://docs.docker.com/compose/compose-file/ |
| Redis — Introduction to Data Types | Commands reference, data structures, TTL, pub/sub. Start here before Week 7 cherry-picks. | https://redis.io/docs/latest/develop/data-types/ |
| FastAPI Official Tutorial | The best framework docs in Python. Start with Tutorial → User Guide, then read Advanced User Guide before Phase 3. | https://fastapi.tiangolo.com/tutorial/ |

---

### Git & Workflow

| Resource | What It Is | Link |
|---|---|---|
| Conventional Commits | A spec for writing consistent, readable commit messages. Makes PRs and changelogs dramatically cleaner. | https://www.conventionalcommits.org/ |
| Git Flight Rules | An exhaustive guide to "what do I do when..." scenarios in Git. Bookmarkable — you'll come back to this repeatedly. | https://github.com/k88hudson/git-flight-rules |
| Make a README | A template-based guide to writing project READMEs. Your portfolio project README is a first impression — read before Week 12. | https://www.makeareadme.com/ |

---

### Testing & Observability

| Resource | What It Is | Link |
|---|---|---|
| pytest — How-To Guides | Fixtures, mocking, parametrize — all of it. Read "How to use fixtures" before Week 12 cherry-picks begin. | https://docs.pytest.org/en/stable/how-to/ |
| structlog | Turns Python log lines into JSON objects your future self can actually search and read. Use this instead of the built-in logging module. | https://www.structlog.org/en/stable/ |
| OpenTelemetry for Python | The industry standard for distributed tracing. You won't implement this on day one, but knowing it exists matters. | https://opentelemetry.io/docs/languages/python/ |

---

### Environment & Secrets

| Resource | What It Is | Link |
|---|---|---|
| python-dotenv | Load .env files into environment variables. The baseline approach for secrets management in every project. | https://pypi.org/project/python-dotenv/ |
| uv — Python Package Manager | The new standard for Python dependency management. Faster than pip, replaces virtualenv. Use this from Week 6 onward. | https://docs.astral.sh/uv/ |
| gitignore.io | Generates a .gitignore for any stack instantly. Run "python, fastapi, docker" before your first commit. | https://www.toptal.com/developers/gitignore |

---

*Last updated: March 2026*