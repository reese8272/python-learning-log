# AI Engineering Master Guide

**Target:** AI Engineer → AI Consultant (Enterprise Automation & Orchestration)  
**Domain:** Enterprise IT automation — agentic systems that replace manual handoffs with coordinated agent teams  
**Mastery standard:** Can I explain why THIS over THAT? If I can break down the decision, I own it.

---

## Learning Philosophy

Understand enough to build → build → understand more deeply through building → design → lead.

Building is what converts knowledge into judgment. Move through the checklist at your own pace — no dates, no weekly blocks. Finish an item, check it off, move to the next. Skip nothing.

---

## Phase 1 — Core Stack

*Learn the tools. Work every lab. No skipping.*

### Courses (complete in order)

- [ ] **Eden Marco — LangChain: Develop AI Agents with LangChain & LangGraph**
  - [udemy.com/course/langchain](https://www.udemy.com/course/langchain/) | ~20 hrs | Paid | ⭐ 4.6
  - Covers: LangChain core, LangGraph, prompt engineering (CoT, ReAct, Few-Shot), agents, tool calling, RAG intro, MCP intro, LangSmith basics
  - GitHub: [github.com/emarco177/langchain-course](https://github.com/emarco177/langchain-course)

- [ ] **Anthropic — Prompt Engineering Interactive Tutorial**
  - [github.com/anthropics/prompt-eng-interactive-tutorial](https://github.com/anthropics/prompt-eng-interactive-tutorial) | ~8-10 hrs | Free
  - Covers: Prompt structure, XML tagging, chain-of-thought, role prompting, few-shot, evidence-before-conclusions
  - Do alongside or right after Eden Marco's prompt sections

- [ ] **LangChain Academy — Intro to LangSmith**
  - [academy.langchain.com/courses/intro-to-langsmith](https://academy.langchain.com/courses/intro-to-langsmith) | ~3-4 hrs | Free
  - Covers: Experiment tracking, dataset management, annotation queues, agent observability, evaluations

- [ ] **LangChain Academy — Intro to LangGraph**
  - [academy.langchain.com/courses/intro-to-langgraph](https://academy.langchain.com/courses/intro-to-langgraph) | ~4-5 hrs | Free
  - Covers: Short/long-term memory, state management, persistence, multi-agent systems

- [ ] **MCP Masterclass — Complete Guide to MCP in Python**
  - [udemy.com/course/learn-mcp-model-context-protocol-complete-guide](https://www.udemy.com/course/learn-mcp-model-context-protocol-complete-guide/) | ~8 hrs | Paid | ⭐ 4.7
  - Covers: MCP architecture, tools/resources/prompts, transport (STDIO, Streamable HTTP), building MCP servers & clients

- [ ] **RAG-LLM Evals & Test Automation for Beginners**
  - [udemy.com/course/rag-llm-evaluation-ai-test](https://www.udemy.com/course/rag-llm-evaluation-ai-test/) | ~8.5 hrs | Paid | ⭐ 4.6
  - Covers: RAGAS framework, 7 core LLM metrics, pytest assertions, single/multi-turn evaluation, test data generation

- [ ] **Anthropic — Real World Prompting + Prompt Evaluations**
  - [github.com/anthropics/courses](https://github.com/anthropics/courses) | ~3-4 hrs | Free
  - Covers: Production prompts, prompt evals, measuring prompt quality

- [ ] **LangChain Academy — Deep Research with LangGraph**
  - [academy.langchain.com/courses/deep-research-with-langgraph](https://academy.langchain.com/courses/deep-research-with-langgraph) | ~3-4 hrs | Free
  - Covers: Multi-agent deep research system, LangGraph coordination, LangSmith evals
  - Do this last — ties together LangGraph + LangSmith + evals as a Phase 1 capstone

### Concepts to Cover Alongside

*Not standalone courses — concepts to understand while working through the courses above. Read the linked reference, take notes, move on.*

- [ ] **REST API Design** — HTTP methods, status codes, request/response cycle, what makes an API RESTful → [System Design Primer](https://github.com/donnemartin/system-design-primer)
- [ ] **Git workflows** — branching, meaningful commit messages, PRs, rebasing → [Conventional Commits](https://www.conventionalcommits.org/) | [Git Flight Rules](https://github.com/k88hudson/git-flight-rules)
- [ ] **Docker fundamentals** — containers vs VMs, writing a Dockerfile, building and running an image → [Docker Docs](https://docs.docker.com/get-started/)
- [ ] **Docker Compose** — multi-container apps, service networking, volumes, `.env` files → [Docker Compose Reference](https://docs.docker.com/compose/compose-file/)
- [ ] **Python packaging** — `pyproject.toml`, `uv`, virtual environments → [uv docs](https://docs.astral.sh/uv/)
- [ ] **Async & Event-Driven Architecture** — `async/await` at the architecture level, message queues conceptually (Kafka/RabbitMQ), when async vs sync
- [ ] **Authentication & Authorization** — JWT (issue, sign, verify), API key patterns, OAuth2 overview, authn vs authz → [JWT.io](https://jwt.io/introduction)
- [ ] **OWASP Top 10** — read once, all 10 items, one sitting → [OWASP Top 10](https://owasp.org/www-project-top-ten/) | [OWASP API Security](https://owasp.org/www-project-api-security/)
- [ ] **Databases** — SQL vs NoSQL, when to use PostgreSQL vs vector DB vs Redis, indexing conceptually
- [ ] **Caching** — LRU eviction, write-through vs write-back, cache invalidation
- [ ] **Secrets & production security** — `.env` files, never committing API keys, secrets management → [python-dotenv](https://pypi.org/project/python-dotenv/)

---

## Must-Read AI Papers

*These explain how the models you're building on actually work — the difference between using LLMs and understanding them. Read them alongside or between phases, one at a time. Your mentor's recommended list.*

- [ ] **Llama-3** — The Llama 3 Herd of Models (Meta, 2024)
  - [arxiv.org/abs/2407.21783](https://arxiv.org/abs/2407.21783)
  - How a leading open-weight model family is designed, trained, and deployed at scale. The benchmark for open-source frontier models.

- [ ] **MoE** — Mixtral of Experts (Mistral AI, 2024)
  - [arxiv.org/abs/2401.04088](https://arxiv.org/abs/2401.04088)
  - Sparse mixture-of-experts architecture: only a subset of parameters activate per token. Large model capacity at lower inference cost. Explains the MoE routing logic now used across many frontier models.

- [ ] **Gemma** — Gemma: Open Models Based on Gemini Research (Google, 2024)
  - [arxiv.org/abs/2403.08295](https://arxiv.org/abs/2403.08295)
  - How Google's frontier research translates into deployable open models. Lightweight, responsible, high-performing.

- [ ] **VisionMamba** — Vision Mamba (2024)
  - [arxiv.org/abs/2401.09417](https://arxiv.org/abs/2401.09417)
  - Efficient visual representation using bidirectional state space models (SSMs) as an alternative to vision transformers. Relevant for multimodal agent systems.

- [ ] **Gemini 1.5** — Gemini 1.5: Unlocking Multimodal Understanding Across Millions of Tokens (Google, 2024)
  - [arxiv.org/abs/2403.05530](https://arxiv.org/abs/2403.05530)
  - How million-token context windows are achieved. Directly relevant for long-context RAG and agentic memory.

- [ ] **Phi-3** — Phi-3 Technical Report (Microsoft, 2024)
  - [arxiv.org/abs/2404.14219](https://arxiv.org/abs/2404.14219)
  - A small model that rivals much larger ones through better training data. The core argument: data quality beats model size.

- [ ] **Qwen-2** — Qwen2 Technical Report (Alibaba, 2024)
  - [arxiv.org/abs/2407.10671](https://arxiv.org/abs/2407.10671)
  - Leading open-weight model with strong multilingual and coding capabilities. Expands your mental model of what the frontier looks like beyond OpenAI/Anthropic/Google.

- [ ] **KAN** — KAN: Kolmogorov-Arnold Networks (2024)
  - [arxiv.org/abs/2404.19756](https://arxiv.org/abs/2404.19756)
  - A new neural network architecture replacing fixed activation functions with learnable ones on edges rather than nodes. Challenges the MLP paradigm — worth understanding even if MLPs still dominate.

- [ ] **LLM Survey** — Large Language Models: A Survey (2024)
  - [arxiv.org/abs/2402.06196](https://arxiv.org/abs/2402.06196)
  - Comprehensive map of the LLM landscape — development, capabilities, evaluation, limitations. Good for building the full mental model of where everything fits.

- [ ] **DeepSeek-Coder** — DeepSeek-Coder: When the Large Language Model Meets Programming (2024)
  - [arxiv.org/abs/2401.14196](https://arxiv.org/abs/2401.14196)
  - How code-focused LLMs are trained and what makes them effective. Directly relevant for agentic systems that write, analyze, or migrate code.

---

## Phase 2 — Build: Capstone Project

*No new course content in this phase. If you hit a wall on something specific, that's your learning item for the day. Struggle first, then reach for help.*

### Design First

*Do all of this before writing any code.*

- [ ] Write the architecture doc — all endpoints, all data models (Pydantic schemas), agent flow map, what triggers what, what returns what
- [ ] Define the agent team — which agents, what each one owns, how state flows between them
- [ ] Draw the system design diagram (ASCII is fine)
- [ ] Save the architecture doc to `career/reflection_log/` before writing a single line of code

### Infrastructure

- [ ] Docker Compose running: FastAPI + PostgreSQL (with pgvector) + Redis
- [ ] FastAPI app running and reachable
- [ ] PostgreSQL connection established, pgvector extension enabled
- [ ] Redis connection established
- [ ] `.env` file handling for all secrets — nothing hardcoded
- [ ] Basic health check endpoint working

### Agent Layer

- [ ] State schema defined (`TypedDict`)
- [ ] Agent nodes implemented (Analyzer, Processor, Validator, Reviewer — adapt to your domain)
- [ ] `StateGraph` wired — nodes connected, edges defined
- [ ] LangSmith connected — traces visible in dashboard
- [ ] Basic end-to-end flow working (rough is fine — polish comes later)
- [ ] Human-in-the-loop checkpoint on Reviewer node

### RAG Pipeline

- [ ] Document ingestion — chunk, embed, store in pgvector
- [ ] Retrieval working — query → relevant chunks → passed to agent context
- [ ] RAG integrated into the relevant agent node

### MCP Integration

- [ ] MCP server defined with at least one real tool
- [ ] MCP tools wired into the agent system
- [ ] Error handling on tool failures

### AWS Bedrock

- [ ] LLM provider abstracted — configurable via env var (Anthropic API locally, Bedrock in production mode)
- [ ] Bedrock connection working with at least one model

### Production Readiness

- [ ] API key authentication on FastAPI endpoints (`Depends()` auth middleware)
- [ ] RAGAS eval pass on RAG pipeline — at least 3 metrics measured
- [ ] Redis caching integrated where it makes sense
- [ ] Structured logging added (JSON format, request IDs, agent step logging) → [structlog](https://www.structlog.org/en/stable/)
- [ ] pytest coverage on critical paths — endpoint tests, agent unit tests → [pytest docs](https://docs.pytest.org/en/stable/how-to/)
- [ ] OWASP checklist pass — go through your notes and check each item against your code
- [ ] No bare `except Exception` anywhere — error handling is explicit
- [ ] README written — what it is, how to run it, architecture overview → [Make a README](https://www.makeareadme.com/)
- [ ] Architecture diagram finalized

---

## Phase 3 — AWS & Cloud

*After shipping the project. Now the hands-on means something because you have context.*

- [ ] **AWS Bedrock hands-on** — connect your project to a real Bedrock endpoint, not just local Anthropic API
- [ ] **AWS IAM** — roles, policies, least privilege — understand it well enough to set up your project's permissions correctly
- [ ] **AWS Lambda** — understand what it is, when you'd use it over FastAPI, basic deployment
- [ ] **AWS SageMaker** — understand the service landscape: when SageMaker vs Bedrock vs roll your own
- [ ] **Distributed Systems & CAP Theorem** — consistency vs availability tradeoffs → [System Design Primer](https://github.com/donnemartin/system-design-primer)
- [ ] **Observability** — logging vs metrics vs tracing, OpenTelemetry conceptually → [OpenTelemetry for Python](https://opentelemetry.io/docs/languages/python/)
- [ ] **Scalability Patterns** — horizontal vs vertical scaling, stateless service design, connection pooling
- [ ] **Twelve-Factor App** — read once → [12factor.net](https://12factor.net/)

---

## Phase 4 — Certifications

*After shipping the project and completing Phase 3. The cert validates what you've built, not the other way around.*

- [ ] **AWS AIF-C01 — AI Practitioner** ← take this first
- [ ] **AWS MLA-C01 — ML Associate** ← after AIF-C01

---

## Capstone Project Spec

**Concept:** A multi-agent orchestration system that automates a complex enterprise workflow — takes a real input, routes it through a team of specialized agents, produces a validated output with human-in-the-loop checkpoints.

**Inspired by:** The legacy → modern framework migration pattern. Each agent owns one concern; the graph coordinates the pipeline.

**Agent team (adapt to your chosen workflow):**

| Agent | Responsibility |
|---|---|
| Analyzer | Ingests input, builds a semantic map or structured understanding of what it's working with |
| Processor | Does the primary transformation or generation work |
| Validator | Checks output against rules, runs tests, verifies correctness |
| Reviewer | Flags ambiguous or low-confidence outputs for human review |

**Tech stack:**

| Layer | Tool |
|---|---|
| Orchestration | LangGraph |
| Observability | LangSmith |
| Tool integration | MCP |
| RAG + vector DB | pgvector (PostgreSQL extension) |
| Evals | RAGAS |
| API layer | FastAPI |
| Infrastructure | Docker Compose |
| Cache | Redis |
| LLM | Anthropic API (local) / AWS Bedrock (production-configurable) |
| Auth | API key via FastAPI `Depends()` |
| Logging | structlog |
| Testing | pytest |

**What done looks like:**
- Running, Dockerized system that accepts a real input and produces a validated output through the agent team
- LangSmith traces visible for every agent run
- RAG pipeline with RAGAS eval scores
- OWASP-checked, API-key-protected, structured-logged
- README + architecture diagram you could put in front of a client

---

## Domain Focus

**Enterprise IT automation and orchestration** — AI systems that replace manual, human-in-the-loop enterprise workflows with coordinated agent teams.

**Primary vertical:** Enterprise IT / internal operations automation  
**Secondary vertical (penciled in — update when you have a lean):**

| Option | Why it fits |
|---|---|
| Financial services (BFSI) | Document processing, compliance, risk assessment — RAG is a natural fit; heavily regulated = high consulting value |
| Legal / compliance | Contract analysis, regulatory document search, policy Q&A — RAG is almost perfectly suited |
| Healthcare | Clinical documentation, prior auth, knowledge retrieval |

---

## Resource Reference

### Courses & Tutorials

| Resource | Type | Link |
|---|---|---|
| Eden Marco — LangChain & LangGraph | Udemy (~20 hrs) | [link](https://www.udemy.com/course/langchain/) |
| Anthropic Prompt Engineering Tutorial | Free Notebooks (~8-10 hrs) | [link](https://github.com/anthropics/prompt-eng-interactive-tutorial) |
| LangChain Academy — Intro to LangSmith | Free (~3-4 hrs) | [link](https://academy.langchain.com/courses/intro-to-langsmith) |
| LangChain Academy — Intro to LangGraph | Free (~4-5 hrs) | [link](https://academy.langchain.com/courses/intro-to-langgraph) |
| MCP Masterclass | Udemy (~8 hrs) | [link](https://www.udemy.com/course/learn-mcp-model-context-protocol-complete-guide/) |
| RAG-LLM Evals & Test Automation | Udemy (~8.5 hrs) | [link](https://www.udemy.com/course/rag-llm-evaluation-ai-test/) |
| Anthropic — Real World Prompting + Evals | Free Notebooks (~3-4 hrs) | [link](https://github.com/anthropics/courses) |
| LangChain Academy — Deep Research with LangGraph | Free (~3-4 hrs) | [link](https://academy.langchain.com/courses/deep-research-with-langgraph) |

### Security & Standards

| Resource | Link |
|---|---|
| OWASP Top 10 | [link](https://owasp.org/www-project-top-ten/) |
| OWASP API Security Top 10 | [link](https://owasp.org/www-project-api-security/) |
| JWT.io | [link](https://jwt.io/introduction) |

### System Design

| Resource | Link |
|---|---|
| System Design Primer | [link](https://github.com/donnemartin/system-design-primer) |
| Twelve-Factor App | [link](https://12factor.net/) |
| High Scalability Blog | [link](http://highscalability.com/) |

### Code Quality

| Resource | Link |
|---|---|
| PEP 8 | [link](https://peps.python.org/pep-0008/) |
| Ruff (Python linter) | [link](https://docs.astral.sh/ruff/) |
| Google Python Style Guide | [link](https://google.github.io/styleguide/pyguide.html) |

### Infrastructure

| Resource | Link |
|---|---|
| Docker Compose Reference | [link](https://docs.docker.com/compose/compose-file/) |
| Redis Data Types | [link](https://redis.io/docs/latest/develop/data-types/) |
| FastAPI Official Tutorial | [link](https://fastapi.tiangolo.com/tutorial/) |

### Git & Workflow

| Resource | Link |
|---|---|
| Conventional Commits | [link](https://www.conventionalcommits.org/) |
| Git Flight Rules | [link](https://github.com/k88hudson/git-flight-rules) |
| Make a README | [link](https://www.makeareadme.com/) |

### Testing & Observability

| Resource | Link |
|---|---|
| pytest How-To Guides | [link](https://docs.pytest.org/en/stable/how-to/) |
| structlog | [link](https://www.structlog.org/en/stable/) |
| OpenTelemetry for Python | [link](https://opentelemetry.io/docs/languages/python/) |

### Environment & Secrets

| Resource | Link |
|---|---|
| python-dotenv | [link](https://pypi.org/project/python-dotenv/) |
| uv — Python Package Manager | [link](https://docs.astral.sh/uv/) |
| gitignore.io | [link](https://www.toptal.com/developers/gitignore) |

### Inference & Explainability (Do When Ready)

*Deeper specializations — come back when a project demands it.*

| Resource | Link |
|---|---|
| Nebius — Serving LLMs with vLLM | [link](https://nebius.com/blog/posts/serving-llms-with-vllm-practical-guide) |
| Aleksa Gordić — Inside vLLM | [link](https://www.aleksagordic.com/blog/vllm) |
| vLLM Official Docs — Optimization | [link](https://docs.vllm.ai/en/latest/configuration/optimization/) |
| SHAP Tutorial — Explainable AI | [link](https://shap.readthedocs.io/en/latest/example_notebooks/overviews/An%20introduction%20to%20explainable%20AI%20with%20Shapley%20values.html) |
| Christoph Molnar — Interpretable ML (LIME chapter) | [link](https://christophm.github.io/interpretable-ml-book/lime.html) |
