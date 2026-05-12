# LangChain: Develop AI Agents with LangChain & LangGraph
*Eden Marco — Udemy*

**Status:** In progress
**Format:** Video course (~20 hrs) | [Course repo](https://github.com/emarco177/langchain-course)
**Paired Project:** Career skills quizzer agent — reads `CAREER_LOG.md`, picks a skill or judgment log entry, and drills active recall cold. "Explain why LangChain over raw API. Go." Evolves naturally as the course progresses: tool calling (session 1–2), state management (LangGraph), RAG over the full career log (later). Solves a real problem in this system and uses your own career data as the content.

---

## Build Log

*Tracks what's been built in the paired project and what's queued next. Updated each session.*

| Session | What was covered | What was built | Status |
|---------|-----------------|----------------|--------|
| 1 | Agent loop, ReACT pattern, tool calling, LangChain vs raw API | *(not yet built)* | Queued |
| 2 | @tool vs @traceable, Ollama schema generation modes (manual JSON vs auto-schema) | *(not yet built)* | Queued |

**Next build task:** Wire a basic LangChain agent with a single tool that reads `CAREER_LOG.md` and returns a random Judgment Log entry. No quiz logic yet — just get the agent calling the tool and returning an entry. That's the foundation everything else builds on.

---

## What kind of course this is

A hands-on survey of the full LangChain/LangGraph/LangSmith stack. The goal isn't to memorize the API — it's to build decision-making muscle about *when* to use each layer and *why*. Every lab is an opportunity to see the framework making tradeoffs on your behalf. The right question after each section: "What does this layer hide from me, and when would I want to drop below it?"

---

## Session Notes

### Session 1 — Agent Loop + Function Calling

**Main Idea:** Every agent framework is a variant of the ReACT loop. LangChain abstracts away the plumbing (schema authoring, provider lock-in, result parsing) so you can focus on the loop itself — but you need to understand what it hides to know when to go raw.

- ReACT loop: Thought → Action → Observation → Thought, exit on Answer. This is the skeleton underneath LangGraph, MCP, and every other agent framework.
- State = the messages array. No memory abstraction at this layer — history is the growing list passed back into the LLM each turn. (This is why LangGraph introduces explicit state.)
- LangChain vs raw API: LangChain removes three pain points — schema authoring, provider lock-in, result parsing. Drop to raw only when you need behavior LangChain hides.
- Model swaps are benchmarked decisions, not config changes. Two failure modes to check: (1) does the model support tool calling? (2) does it eval correctly against your actual use case? Swapping without evals risks silent regression — tool-calling behavior changes between providers and versions in non-obvious ways.
- System prompt is a control surface. Strict rules ("never calculate your own math, use the tools") steer tool-call behavior without code changes. Prompt engineering = agent steering.
- Docstrings + type hints are part of the prompt the model reads when picking a tool. They are not human-only documentation — treat them as agent-facing interface.
- Always set a MAX_ITERATIONS guard. Runaway loops are a real failure mode, not an edge case.
- Tracing is non-negotiable. Without it, non-deterministic loops are undebuggable.
- Known simplification: single tool call per iteration. Real LLMs return parallel tool calls — LangGraph's tool nodes handle this. Watch for it.

> **Connection:** The State = messages array insight directly explains why LangGraph exists. When you get there, come back to this — it will click differently.

### Session 2 — LangGraph: Why It Exists

**Main Idea:** The basic agent loop is a straight line with one fork. LangGraph is a map with many paths — and the difference isn't cosmetic, it's what makes agents production-safe.

- The `while True` loop has two production-killing flaws: state lives in RAM (no recovery if process dies) and there's only one decision point (tool or done). Neither is acceptable for real systems.
- Silent bug in the basic loop: only `tool_calls[0]` is handled. Real LLMs return parallel tool calls — the rest are silently dropped. LangGraph's tool nodes handle all of them.
- LangGraph's three concepts: **State** (typed object persisted to DB after every node), **Nodes** (functions that take state, do work, return updated state), **Edges** (connections between nodes — fixed or conditional).
- Conditional edges are how routing works. The LLM sets a field in state (e.g. `state["next"]`). The edge function reads it and returns the next node name. Decision logic lives in the graph structure, not buried in loop conditionals.
- Persistent checkpointing is the core production unlock. State written to SQLite/Redis/Postgres after every node. Process can die and resume from the last checkpoint.
- The messages array unpacked: `SystemMessage` (your system prompt) → `HumanMessage` (user input) → `AIMessage` (LLM response, may contain tool_calls) → `ToolMessage` (tool result) → `AIMessage` (final answer). The full history is passed back each turn — history IS state.

> **Connection:** "A while loop is a straight line with one fork. LangGraph is a map with many paths." The State = messages array note from Session 1 now has a concrete answer: LangGraph exists because that list in RAM isn't enough for anything serious.

---

## Connections & Application

- The ReACT loop being the common ancestor of all agent frameworks means mental models transfer. Learn it once here, apply it everywhere.
- System prompt as control surface + docstrings as agent-facing interface = prompt engineering is not separate from engineering. It is engineering.
- LangSmith tracing and MAX_ITERATIONS are the two non-negotiables for production. Build the habit of adding them from session one, not retrofitting them later.

---

## Honest Takeaways

*(Update as course progresses. Complete when finished.)*

---

## Entry Log

- [2026-05-04](reflection_log/2026-05-04.md) — Session 1: Agent loop, ReACT pattern, function calling, LangChain vs raw API
- [2026-05-12](reflection_log/2026-05-12.md) — Session 2: LangGraph — why it exists, State/Nodes/Edges, persistent checkpointing, conditional routing
