# Python `asyncio` — Learning Log

**Date:** 2026-03-30
**Track:** AI-Augmented Dev / Python Foundations
**Format:** Socratic / Challenge-based

-----

## Core Concept: Cooperative Concurrency

`asyncio` is **not parallelism** — it is **cooperative concurrency** on a single thread.

- A single **event loop** acts as a scheduler inside one thread
- When a coroutine hits `await`, it yields control back to the event loop
- The event loop resumes another coroutine that is ready to make progress
- Two things are **never running at the exact same time** — but wait times overlap

**Key distinction:**

|Type                        |Tool             |Use Case                                  |
|----------------------------|-----------------|------------------------------------------|
|Cooperative concurrency     |`asyncio`        |I/O-bound work (network calls, DB queries)|
|True parallelism (threads)  |`threading`      |Blocking I/O you can’t rewrite            |
|True parallelism (processes)|`multiprocessing`|CPU-bound / heavy computation             |

-----

## Why asyncio Works for LLM API Calls

Each LLM API call involves sending a request and **waiting** on the network — the CPU is idle during that wait. `asyncio` exploits those idle gaps:

- Fire 5 API calls nearly simultaneously with `asyncio.gather`
- All 5 wait periods **overlap** instead of stacking
- Result: ~2 seconds instead of ~10 seconds for 5 x 2-second calls

> The event loop doesn’t make each call faster — it stops wasting the gaps between them.

**Why asyncio gives zero benefit for matrix multiplication:**
CPU-bound work never yields. There’s no `await` gap for the event loop to exploit. The coroutine just runs and runs without ever giving control back — so concurrency never kicks in.

-----

## Blocking the Event Loop — The Silent Bug

If you call a **synchronous blocking function** inside an async context without `await`, you freeze the entire event loop. Every other coroutine is paused until it finishes.

### Example of the bug:

```python
import asyncio
import time

async def agent_node():
    print("Starting agent")
    time.sleep(3)  # ← BLOCKS THE EVENT LOOP
    print("Agent done")

async def main():
    await asyncio.gather(
        agent_node(),
        agent_node(),
        agent_node()
    )

asyncio.run(main())
```

**What actually happens:** Runs sequentially — ~9 seconds total. `gather` gives you nothing because `time.sleep` never yields.

**Why it’s dangerous:** No error is raised. Everything works — just silently slower.

-----

## The Fix: `run_in_executor`

When you **must** call a synchronous blocking function inside async code, ship it to a thread pool so the event loop stays free.

```python
import asyncio
import time

def slow_sync_call():
    time.sleep(3)  # blocking, but now running in a thread

async def agent_node():
    print("Starting agent")
    loop = asyncio.get_event_loop()
    await loop.run_in_executor(None, slow_sync_call)  # None = default ThreadPoolExecutor
    print("Agent done")

async def main():
    await asyncio.gather(
        agent_node(),
        agent_node(),
        agent_node()
    )

asyncio.run(main())
```

**What actually happens now:** All 3 sleep in parallel threads — ~3 seconds total.

### How `run_in_executor` works mechanically:

1. Ships the blocking function to a worker thread
1. Immediately `await`s a future that resolves when the thread finishes
1. Event loop is free to run other coroutines while the thread works
1. When the thread completes, your coroutine resumes with the result

-----

## Decision Guide

|Situation                                |Solution                                             |
|-----------------------------------------|-----------------------------------------------------|
|Async I/O (network, DB with async driver)|`await` natively                                     |
|Blocking I/O you can’t rewrite           |`run_in_executor(None, fn)` — ThreadPoolExecutor     |
|Heavy CPU-bound work                     |`run_in_executor(executor, fn)` — ProcessPoolExecutor|

-----

## Key Takeaways

1. `asyncio` exploits I/O wait gaps — it does not create true parallelism
1. Blocking the event loop is silent — it won’t crash, it just destroys concurrency
1. `run_in_executor` is the bridge between async code and synchronous blocking libraries
1. Always ask: *“What is the event loop actually doing at this line?”*

-----

## Next Concepts to Explore

- `asyncio.gather` vs `asyncio.wait` vs `TaskGroup`
- `asyncio.Lock` and managing shared state in concurrent coroutines
- How FastAPI handles the event loop under the hood

---

i wanna start listening to think and grow rich on youtube
build this repo with a more life-oriented style with directories about my life
track this stuff with my habits and ideas
i wanna start listening to certain videos every day, like mini habit building videos to literally brainwash myself to being awesome 
create alarms to build habits
when learning, i want to be cloud, ai native, i beleive i already know version control, but SYSTEM DESIGNS OMG
habits i heard that felt necessary - new experiences, family and relationships over all, walk to clear mind, will write more down as i live
