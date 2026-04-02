# AI/ML Engineering Learning Roadmap

**Goal:** LangChain, LangGraph, LangSmith, MCP, Prompt/Context Engineering, RAG, Validation/Evals, Inference, Explainability  
**Total Time:** ~65-70 hours | 3 Paid Courses + 7 Free Resources  
**Estimated Coverage:** 95%+ across all target topics

---

## Stage 1: Foundation

### 1. Eden Marco — LangChain: Develop AI Agents with LangChain & LangGraph
- **Link:** [udemy.com/course/langchain](https://www.udemy.com/course/langchain/)
- **Type:** Udemy | ~20 hours | ⭐ 4.6 (45k+ ratings)
- **Covers:** LangChain core, LangGraph, prompt engineering (CoT, ReAct, Few-Shot), agents, tool calling, RAG intro, MCP intro, LangSmith basics
- **Why first:** Everything else builds on this. Mental models for LangChain abstractions, agent patterns, and LangGraph state management are hardest to learn from docs alone.
- **GitHub repo:** [github.com/emarco177/langchain-course](https://github.com/emarco177/langchain-course)

### 1b. Anthropic — Prompt Engineering Interactive Tutorial
- **Link:** [github.com/anthropics/prompt-eng-interactive-tutorial](https://github.com/anthropics/prompt-eng-interactive-tutorial)
- **Type:** Free | Jupyter Notebooks | ~8-10 hours
- **Covers:** 9 chapters — prompt structure, XML tagging, chain-of-thought, role prompting, few-shot learning, evidence-before-conclusions, advanced techniques
- **Why here:** Eden Marco teaches prompt theory. This gives you hands-on reps against a real model. Do alongside or right after Eden Marco's prompt sections.

---

## Stage 2: LangSmith & LangGraph Depth

### 2. LangChain Academy — Intro to LangSmith
- **Link:** [academy.langchain.com/courses/intro-to-langsmith](https://academy.langchain.com/courses/intro-to-langsmith)
- **Type:** Free | ~3-4 hours
- **Covers:** Experiment tracking, dataset management, annotation queues, agent observability, evaluations
- **Why here:** Eden Marco only touches LangSmith basics. This fills the depth gap on the tooling you'll use daily for debugging and eval workflows.

### 3. LangChain Academy — Foundation: Intro to LangGraph (Python)
- **Link:** [academy.langchain.com/courses/intro-to-langgraph](https://academy.langchain.com/courses/intro-to-langgraph)
- **Type:** Free | ~4-5 hours
- **Covers:** Short vs long-term memory, state management, persistence, multi-agent systems, agentic workflows
- **Why here:** Deepens LangGraph beyond what Eden Marco covers. Official source built by the LangGraph team. Do this after finishing Eden Marco's LangGraph sections.

---

## Stage 3: MCP

### 4. MCP Masterclass — Complete Guide to MCP in Python
- **Link:** [udemy.com/course/learn-mcp-model-context-protocol-complete-guide](https://www.udemy.com/course/learn-mcp-model-context-protocol-complete-guide/)
- **Type:** Udemy | ~8 hours | ⭐ 4.7
- **Covers:** MCP architecture, protocol theory, tools/resources/prompts, transport (STDIO, Streamable HTTP), building MCP servers & clients, publishing/deploying, LLM integration
- **Why here:** Zero overlap with previous courses. Python-focused. Directly relevant to Informatica MCP server work. Nothing else covers MCP with sufficient depth.

---

## Stage 4: Evals & Production Prompting

### 5. RAG-LLM Evals & Test Automation for Beginners
- **Link:** [udemy.com/course/rag-llm-evaluation-ai-test](https://www.udemy.com/course/rag-llm-evaluation-ai-test/)
- **Type:** Udemy | ~8.5 hours | ⭐ 4.6
- **Covers:** RAGAS framework, 7 core LLM metrics, pytest assertions for metric benchmarking, single/multi-turn evaluation, test data generation, evaluation dashboard
- **Why here:** You need to build things before you can evaluate them. This gives you the automation framework for testing RAG/LLM systems.

### 5b. Anthropic — Real World Prompting + Prompt Evaluations
- **Link:** [github.com/anthropics/courses](https://github.com/anthropics/courses)
  - Real World Prompting: `real_world_prompting/` directory
  - Prompt Evaluations: `prompt_evaluations/` directory
- **Type:** Free | Jupyter Notebooks | ~3-4 hours combined
- **Covers:** Incorporating techniques into complex production prompts, writing production-grade prompt evals, measuring prompt quality
- **Why here:** Bridges prompt engineering into evals. Directly complements the RAGAS course with Anthropic's approach to eval methodology.

---

## Stage 5: Capstone Project

### 6. LangChain Academy — Deep Research with LangGraph
- **Link:** [academy.langchain.com/courses/deep-research-with-langgraph](https://academy.langchain.com/courses/deep-research-with-langgraph)
- **Type:** Free | ~3-4 hours
- **Covers:** Build a multi-agent deep research system, LangGraph multi-agent coordination, LangSmith evaluation of agent performance
- **Why here:** Ties together LangGraph + LangSmith + evals in one capstone project. Do this after evals to test everything you've learned.

---

## Stage 6: Inference & Explainability (Do When Ready)

> These can wait until after you've shipped real projects with Stages 1-5. Come back to these when the work demands it.

### 7a. Nebius — "Serving LLMs with vLLM: A Practical Guide"
- **Link:** [nebius.com/blog/posts/serving-llms-with-vllm-practical-guide](https://nebius.com/blog/posts/serving-llms-with-vllm-practical-guide)
- **Type:** Free | Written guide | ~2-3 hours
- **Covers:** Transformer fundamentals → PagedAttention → continuous batching → quantization (INT8/INT4/FP8) → tensor parallelism → deployment
- **Why:** Single best written resource on production LLM inference. Start-to-finish, practical.

### 7b. Aleksa Gordić — "Inside vLLM: Anatomy of a High-Throughput LLM Inference System"
- **Link:** [aleksagordic.com/blog/vllm](https://www.aleksagordic.com/blog/vllm)
- **Type:** Free | Blog post series | ~1-2 hours
- **Covers:** Deep technical breakdown — scheduling, paged attention, continuous batching, speculative decoding, chunked prefill, multi-GPU execution
- **Why:** Builds the mental model for how inference engines actually work under the hood.

### 7c. vLLM Official Docs — Optimization & Tuning
- **Link:** [docs.vllm.ai/en/latest/configuration/optimization](https://docs.vllm.ai/en/latest/configuration/optimization/)
- **Type:** Free | Reference docs
- **Covers:** Parallelism strategies, memory management, attention backends, API server scale-out
- **Why:** Reference when you're actually deploying and tuning.

### 8a. SHAP Official Tutorial — Introduction to Explainable AI with Shapley Values
- **Link:** [shap.readthedocs.io — Intro to Explainable AI](https://shap.readthedocs.io/en/latest/example_notebooks/overviews/An%20introduction%20to%20explainable%20AI%20with%20Shapley%20values.html)
- **Type:** Free | Interactive Jupyter Notebooks | ~2-3 hours
- **Covers:** Linear regression → tree models → deep learning explanations using the `shap` Python package
- **Why:** Hands-on, progressive, uses the actual library you'd use in production.

### 8b. 1littlecoder — "What is Interpretable Machine Learning"
- **Link:** [YouTube — ML Explainability with Python LIME & SHAP Tutorial](https://www.classcentral.com/course/youtube-what-is-interpretable-machine-learning-ml-explainability-with-python-lime-shap-tutorial-126501)
- **Type:** Free | YouTube | ~1 hour
- **Covers:** LIME and SHAP overview, advantages/disadvantages, Python demos
- **Why:** Good visual overview before diving into the SHAP docs. Watch this first, then do 8a.

### 8c. Christoph Molnar — Interpretable Machine Learning Book (LIME Chapter)
- **Link:** [christophm.github.io/interpretable-ml-book/lime.html](https://christophm.github.io/interpretable-ml-book/lime.html)
- **Type:** Free | Online book | ~1 hour for LIME chapter
- **Covers:** LIME theory in depth — the gold standard reference for ML interpretability
- **Why:** When you need the deeper "why" behind LIME beyond the code demos.

---

## Quick Reference: Coverage by Topic

| Topic | Primary Source | Supplement | Est. Coverage |
|---|---|---|---|
| **LangChain** | Eden Marco | LangChain Academy (LangChain Foundation) | 95% |
| **LangGraph** | Eden Marco | LangChain Academy (Intro to LangGraph + Deep Research) | 95% |
| **LangSmith** | Eden Marco (basics) | LangChain Academy (Intro to LangSmith) | 90% |
| **MCP** | MCP Masterclass | — | 90% |
| **Prompt/Context Eng** | Eden Marco (theory) | Anthropic Tutorial + Real World Prompting | 92% |
| **RAG** | Eden Marco + Boot.dev | — | 90% |
| **Validation/Evals** | RAG-LLM Evals | Anthropic Prompt Evals + LangSmith Academy | 88% |
| **Inference** | — | Nebius guide + Gordić blog + vLLM docs | 80% |
| **Explainability** | — | SHAP tutorial + 1littlecoder + Molnar book | 78% |

---

## Notes

- **Stages 1-5 are the priority.** ~55-60 hours. This is where 90% of the job-relevant skill comes from.
- **Stage 6 is "when you need it."** Inference and explainability are deeper specializations — learn them when a project demands it.
- **Boot.dev RAG course** (already in progress) supplements Eden Marco's RAG coverage. No additional RAG course needed.
- **Note-taking approach:** Concept (2-3 sentences), Code Pattern (actual syntax), Lab Prompt (challenge question for yourself).