"""
LESSON ASSIGNMENT — "What an LLM call actually is" (Curriculum §1.1, Tier 1)
Date taught: 2026-06-22  |  Source: Eden Marco lec 67  |  Pair: /learn session

────────────────────────────────────────────────────────────────────────────
WHAT WE'RE TARGETING
────────────────────────────────────────────────────────────────────────────
Every architecture decision you'll make as a consultant — memory, cost,
why a long agent loop gets expensive, when to RAG vs stuff the window —
traces back to ONE primitive: what actually happens in a single LLM call.

Three facts to feel in your fingers, not just nod at:
  1. The call is STATELESS. The model remembers nothing. The "conversation"
     is an illusion YOU maintain by re-sending the whole transcript every turn.
  2. The context window is a HARD CEILING (input + output combined). Over it =
     the API rejects you with a 400. That's different from the SOFT failure
     (lost-in-the-middle degradation) that happens *within* a legal-but-huge
     context.
  3. Output costs ~5x input because input is one parallel forward pass, but
     output is generated one token at a time (serial, can't parallelize).

You already built llm_cost.py (the cost angle). This worksheet drills the
OTHER three facets so the whole primitive is yours.

HOW TO USE THIS
  - PART 1: fill in each TODO. Boilerplate is pre-written so you focus on the
    CONCEPT and the FLOW, not syntax. Run `python 2026-06-22_llm-call-anatomy.py`.
    The tests at the bottom tell you red/green. No AI until you've struggled.
  - PART 2: answer the concept questions OUT LOUD or in writing BEFORE you
    scroll to the answer key. For each, also write the one-line "client version."
  - Done = all 4 tests green AND you can say the 4 concept answers cold.
════════════════════════════════════════════════════════════════════════════
"""

# Pre-filled: per-MTok (input, output) pricing, verified 2026-06-22 (Anthropic docs)
PRICING = {
    "haiku-4.5":  (1, 5),
    "sonnet-4.6": (3, 15),
    "opus-4.8":   (5, 25),
}


# ─── EXERCISE 1 — Statelessness: you re-send EVERYTHING, every turn ──────────
# A "conversation" is just a growing list of messages you resend each call.
# Implement build_request: given the prior history and a new user message,
# return the FULL list the API receives this turn = system prompt, then all
# prior history, then the new user message appended on the end.
#
# Concept it burns in: the model has no memory — the payload IS the memory,
# and it grows every turn (which is why long loops cost more each step).

SYSTEM_PROMPT = {"role": "system", "content": "You are a helpful assistant."}

def build_request(history: list[dict], new_user_msg: str) -> list[dict]:
    # TODO: return [system, *history, {"role": "user", "content": new_user_msg}]
    ...


# ─── EXERCISE 2 — Tokens: estimate from raw text ────────────────────────────
# Rule of thumb: ~0.75 words per token  ->  tokens ≈ words * 1.33
# Implement estimate_tokens: count the words in `text`, return the integer
# token estimate (round down with int()).
#
# Concept it burns in: tokens are the unit of billing AND the unit of the
# context window — you reason in tokens, not characters or words.

def estimate_tokens(text: str) -> int:
    # TODO: words = text.split(); return int(len(words) * 1.33)
    ...


# ─── EXERCISE 3 — The hard ceiling: input + output must fit the window ───────
# The window caps input + reserved output COMBINED. If they don't fit, the API
# rejects the request up front (a 400) — it does NOT silently truncate or
# hallucinate. Implement call_status: return "ok" if the call fits, else
# "rejected".
#
# Concept it burns in: over-limit is a HARD reject (fix = chunk/RAG), which is
# a different failure from in-window degradation (fix = better retrieval).

def call_status(input_tokens: int, reserved_output: int, window: int) -> str:
    # TODO: return "ok" if input_tokens + reserved_output <= window else "rejected"
    ...


# ─── EXERCISE 4 — Prove the output asymmetry numerically ────────────────────
# A client wants to cut cost. They can trim N words off the INPUT or N words
# off the OUTPUT. Implement cheaper_to_trim: compute the dollars saved by each
# option and return the string "input" or "output" — whichever saves MORE.
#
# Concept it burns in: because output is ~5x the price, trimming output beats
# trimming the same number of words off input — every time.

def cheaper_to_trim(words: int, model: str) -> str:
    p_in, p_out = PRICING[model]
    tokens = words * 1.33
    # TODO: saved_input  = (tokens / 1e6) * p_in
    #       saved_output = (tokens / 1e6) * p_out
    #       return "output" if saved_output > saved_input else "input"
    ...


# ════════════════════════════════════════════════════════════════════════════
# PART 2 — CONCEPT QUESTIONS (answer cold, THEN check the key at the bottom)
# ════════════════════════════════════════════════════════════════════════════
#
# Q1. "The LLM remembers our conversation" is wrong. Why — and what does that
#     fact force YOU to build into any multi-turn app?
#
# Q2. A client says "we'll just dump our 300-page knowledge base into the
#     context window on every query." Name the TWO distinct things that go
#     wrong — the HARD failure and the SOFT failure — and give the different
#     fix for each.
#
# Q3. Output tokens cost ~5x input tokens. Give the MECHANISTIC reason (what is
#     the model physically doing differently for output vs input?).
#
# Q4. What does capping `max_tokens` actually guard, what does it NOT fix, and
#     what breaks if you set it too low?
#
# Requirement: for each, also write the ONE-LINE version you'd say to a client.


# ════════════════════════════════════════════════════════════════════════════
# TEST RUNNER — run this file; green means the flow is right.
# ════════════════════════════════════════════════════════════════════════════
def _run_tests():
    results = []

    def check(name, cond_fn):
        # cond_fn is a lambda so an unfinished stub fails cleanly instead of
        # crashing the whole runner — you see every exercise's status.
        try:
            ok = bool(cond_fn())
        except Exception as e:
            ok = False
            name = f"{name}  [errored: {type(e).__name__}]"
        results.append((name, ok))
        print(f"  {'PASS' if ok else 'FAIL'} — {name}")

    # `history` = the prior turns WITHOUT the system prompt; build_request
    # always re-prepends system. (That's the point — system rides every call.)
    PRIOR = [
        {"role": "user", "content": "hello"},
        {"role": "assistant", "content": "hi!"},
    ]

    print("Exercise 1 — statelessness / re-send:")
    check("first turn = system + 1 user msg",
          lambda: build_request([], "hello") == [SYSTEM_PROMPT, {"role": "user", "content": "hello"}])
    check("second turn re-sends system + WHOLE prior transcript + new msg",
          lambda: build_request(PRIOR, "again") == [
              SYSTEM_PROMPT,
              {"role": "user", "content": "hello"},
              {"role": "assistant", "content": "hi!"},
              {"role": "user", "content": "again"},
          ])
    check("payload grows every turn (4 msgs by turn 2)",
          lambda: len(build_request(PRIOR, "again")) == 4)

    print("Exercise 2 — token estimate:")
    check("10 words ≈ 13 tokens",
          lambda: estimate_tokens("one two three four five six seven eight nine ten") == 13)
    check("empty string = 0 tokens", lambda: estimate_tokens("") == 0)

    print("Exercise 3 — hard ceiling:")
    check("fits -> ok", lambda: call_status(150_000, 20_000, 200_000) == "ok")
    check("over window -> rejected", lambda: call_status(190_000, 20_000, 200_000) == "rejected")
    check("exactly at the limit -> ok", lambda: call_status(180_000, 20_000, 200_000) == "ok")

    print("Exercise 4 — output asymmetry:")
    check("trimming output saves more than input", lambda: cheaper_to_trim(500, "haiku-4.5") == "output")
    check("holds on opus too", lambda: cheaper_to_trim(500, "opus-4.8") == "output")

    passed = sum(1 for _, c in results if c)
    print(f"\n{passed}/{len(results)} green.", "All green — flow owned." if passed == len(results) else "Keep going.")


if __name__ == "__main__":
    _run_tests()


# ════════════════════════════════════════════════════════════════════════════
# ANSWER KEY — no peeking until you've answered Part 2 cold.
# ════════════════════════════════════════════════════════════════════════════
#
# A1. The API is stateless — the model has zero memory between calls. Each turn
#     you re-send the entire transcript (system + all history + new msg), which
#     is flattened to one token string; the model just predicts the next token.
#     What you must build: a way to persist + re-send state (and later, trim or
#     summarize it so the growing transcript stays cheap and under the window).
#     CLIENT LINE: "The model doesn't remember — we re-send the conversation
#     every call, so 'memory' is something we engineer, not something it has."
#
# A2. HARD failure: input over the window -> API 400 rejection. Fix = chunk the
#     KB and retrieve only relevant pieces (RAG), don't send it all.
#     SOFT failure: even if it fits, "lost in the middle" — the model
#     under-attends to info buried in a huge context, so answers degrade. Fix =
#     better retrieval + ordering (put what matters at the edges), not more
#     context. (Degradation ≠ hallucination — it's attention, not invention.)
#     CLIENT LINE: "Stuffing it all in either gets rejected outright or quietly
#     degrades quality — retrieval beats brute force on both counts."
#
# A3. Input is processed in ONE parallel forward pass (cheap, fast). Output is
#     autoregressive — generated one token at a time, each token a full forward
#     pass, and you can't parallelize because token N+1 depends on token N.
#     You're paying for serial GPU work.
#     CLIENT LINE: "Reading the prompt is one parallel pass; writing the answer
#     is serial, token by token — that's why output is the expensive side."
#
# A4. max_tokens caps the OUTPUT length only -> guards cost + runaway rambling.
#     It does NOT fix input-side degradation or lost-in-the-middle (those come
#     from the input). Too low -> the answer is truncated mid-sentence with
#     stop_reason = "max_tokens".
#     CLIENT LINE: "max_tokens is a cost/runaway guard on the answer length —
#     not a quality knob, and set it too tight and you cut the answer off."
