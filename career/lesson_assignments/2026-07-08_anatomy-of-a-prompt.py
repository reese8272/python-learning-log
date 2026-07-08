"""
LESSON ASSIGNMENT — "Anatomy of a Prompt" (Curriculum §1.2, Tier 1)
Date taught: 2026-07-08  |  Source: Eden Marco lec 68 + Anthropic Ch.1  |  Pair: /learn session
Researched live against the current Anthropic Messages API (claude-api skill, 2026-07-08).

────────────────────────────────────────────────────────────────────────────
WHAT WE'RE TARGETING
────────────────────────────────────────────────────────────────────────────
§1.1 said the LLM call is a STATELESS re-send of tokens. This unit is: what
are those tokens STRUCTURED as? Get the anatomy wrong and everything built on
top of it — tool calling, RAG context assembly, agent scratchpads — is built
on sand.

Three facts to feel in your fingers, not just nod at:
  1. `system` is a SEPARATE TOP-LEVEL parameter — NOT an entry in `messages`.
     `messages` holds ONLY user/assistant turns. This isn't pedantry: the
     render order is tools -> system -> messages, so a frozen system prompt
     is a CACHEABLE PREFIX. Mis-file it as messages[0] and you lose the mental
     model for where the prompt cache boundary sits.
  2. The `assistant` turns you re-send ARE the model's own prior outputs. That
     — nothing hidden server-side — is the entire mechanism of "memory." You
     send the transcript; it re-reads the transcript.
  3. Two limits, two DIFFERENT failures. `max_tokens` caps OUTPUT and truncates
     SOFTLY (stop_reason="max_tokens", maybe mid-sentence, no error). The
     context window caps input+output and REJECTS HARD
     (stop_reason="model_context_window_exceeded"). Always check stop_reason.

⚠ CURRENCY LANDMINE (why we learn live, not from a 2024 course):
  Prefilling the assistant turn — writing a partial final assistant message to
  force a format — is REMOVED on Claude 4.6+ (400 error). The current
  replacement is Structured Outputs: output_config={"format":{"type":
  "json_schema","schema":{...}}}. It ENFORCES/validates the shape; prefill only
  nudged. Ship the old trick against claude-opus-4-8 and it's a hard 400.

HOW TO USE THIS
  - PART 1: answer the concept questions COLD, out loud or in writing, BEFORE
    scrolling to the answer key. Write the one-line "client version" for each.
  - PART 2 + PART 3: fill in each TODO. Boilerplate is pre-written so you focus
    on the CONCEPT and the FLOW, not syntax. The TODOs tell you WHAT to do, not
    the line to type. Run `python 2026-07-08_anatomy-of-a-prompt.py` — the tests
    at the bottom give red/green. No AI until you've struggled 10+ min.
  - Done = all tests green AND you can say the Part 1 answers cold.
════════════════════════════════════════════════════════════════════════════
"""


# ════════════════════════════════════════════════════════════════════════════
# PART 1 — CONCEPT QUESTIONS (answer cold, THEN check the key at the bottom)
# For each, also write the ONE-LINE version you'd say to a client.
# ════════════════════════════════════════════════════════════════════════════
#
# Q1. In an Anthropic Messages API call, WHERE does the system prompt live, and
#     what goes in the `messages` array? Then: why does that separation matter
#     for cost? (Name the render order.)

'''
your answer here
'''

# Q2. It's turn 5 of a chat. Write out what the `messages` array looks like
#     (roles, in order). What is actually IN the assistant entries, and why is
#     that the complete explanation for how the model "remembers" turn 1?

'''
your answer here
'''

# Q3. `max_tokens` vs the context window: which one truncates, which one
#     rejects, and what single field do you check on the response to tell which
#     (if either) happened? Name the two stop_reason strings.

'''
your answer here
'''

# Q4. A pre-2026 course teaches you to force JSON by prefilling the assistant
#     turn with `{"role":"assistant","content":"{\\"name\\": \\""}`. What
#     happens if you ship that against claude-opus-4-8, and what is the current
#     replacement — and why is the replacement BETTER, not just "not broken"?

'''
your answer here
'''


# ════════════════════════════════════════════════════════════════════════════
# PART 2 — CODING EXERCISES (drill the facets; boilerplate pre-filled)
# ════════════════════════════════════════════════════════════════════════════

# ─── EXERCISE 1 — Roles go in the right place ───────────────────────────────
# Build the SHAPE of an Anthropic call. `system` is a top-level key; `messages`
# holds ONLY user/assistant turns.
#
# Concept it burns in: system is architecturally separate from the transcript.

def build_call_shape(system_prompt: str, turns: list[dict]) -> dict:
    # TODO: return a dict with exactly two keys — one holding the system prompt
    #       string at the top level, and one holding the turns list. Do NOT put
    #       the system prompt inside the turns list.
    #       (Match the key names the API uses.)
    raise NotImplementedError


# ─── EXERCISE 2 — Reconstruct the "memory" the model reads ──────────────────
# The model has no memory; the messages list IS the memory, and you rebuild it
# every turn. Given the prior transcript (user/assistant turns already
# exchanged) and the new user message, return the messages list to send THIS
# turn.
#
# Concept it burns in: you re-send the whole prior transcript, and the assistant
# entries in it are the model's own past replies — that's the "memory."

def next_messages(prior_transcript: list[dict], new_user_msg: str) -> list[dict]:
    # TODO: return a NEW list = every prior turn, in order, followed by the new
    #       user message as its own {"role": ..., "content": ...} entry.
    #       Don't mutate prior_transcript; don't prepend a system entry (system
    #       lives at the top level, per Exercise 1).
    raise NotImplementedError


# ─── EXERCISE 3 — Read the stop_reason like an engineer ─────────────────────
# Every response carries a stop_reason. It tells you whether you got a whole
# answer, a truncated one, or a rejection. Map it to a plain-English diagnosis.
#
# Concept it burns in: max_tokens = SOFT truncation; context overflow = HARD
# reject; end_turn = clean finish. Unchecked, a truncated answer looks like a
# model failure when it's really an unread flag.

def diagnose(stop_reason: str) -> str:
    # TODO: return "complete" when the model finished naturally,
    #       "truncated_output" when it hit the output cap,
    #       "context_overflow" when the whole conversation exceeded the window.
    #       (You need the exact stop_reason strings the API uses — recall them,
    #       don't guess loosely.)
    raise NotImplementedError


# ─── EXERCISE 4 — The prefill replacement: build a structured-output config ──
# Prefilling the assistant turn is dead on 4.6+. To force a shape now you pass
# an output_config with a json_schema. Build that config given the field names
# the client must return.
#
# Concept it burns in: the CURRENT way to guarantee output shape is a validated
# schema, not a prompt hack.

def structured_output_config(required_fields: list[str]) -> dict:
    # TODO: return the output_config dict the current API expects:
    #       a "format" whose type marks it as a json schema, carrying a JSON
    #       Schema for an object that REQUIRES every name in required_fields
    #       (each typed as a string). Shape to match:
    #         {"format": {"type": <the json-schema marker>,
    #                     "schema": {"type": "object",
    #                                "properties": {<field>: {"type": "string"}, ...},
    #                                "required": [<every field>]}}}
    raise NotImplementedError


# ════════════════════════════════════════════════════════════════════════════
# PART 3 — PROJECT (the bank-gate build)
# Assemble the FULL kwargs for a real extraction call. This is prompt_anatomy.py
# distilled to its testable core: it wires all four facets together — top-level
# system, a user turn, a structured-output config (the prefill replacement), and
# an explicit max_tokens. `_live_demo()` at the very bottom actually fires it.
# ════════════════════════════════════════════════════════════════════════════

EXTRACTION_SYSTEM = (
    "You are a financial-data extractor. Return ONLY the requested fields, "
    "grounded strictly in the provided text. Do not infer missing values."
)

def build_extraction_call(text: str, model: str = "claude-opus-4-8") -> dict:
    """Return the kwargs dict you'd splat into client.messages.create(**kwargs)
    to extract {company, q3_revenue, prior_revenue} from `text`."""
    fields = ["company", "q3_revenue", "prior_revenue"]
    # TODO: build and return a dict with these keys:
    #   - "model": the model arg
    #   - "max_tokens": a sane explicit cap (a few hundred is plenty here)
    #   - "system": the top-level system prompt (use EXTRACTION_SYSTEM)
    #   - "messages": a one-entry list — a user turn whose content asks to
    #                 extract the fields from `text`
    #   - "output_config": reuse structured_output_config(fields) so the shape
    #                      is schema-enforced (NOT prefilled)
    raise NotImplementedError


# ════════════════════════════════════════════════════════════════════════════
# TEST RUNNER — run this file; green means the flow is right. (Offline — no API.)
# ════════════════════════════════════════════════════════════════════════════
def _run_tests():
    results = []

    def check(name, cond_fn):
        try:
            ok = bool(cond_fn())
        except Exception as e:
            ok = False
            name = f"{name}  [errored: {type(e).__name__}]"
        results.append((name, ok))
        print(f"  {'PASS' if ok else 'FAIL'} — {name}")

    print("Exercise 1 — roles in the right place:")
    shape = lambda: build_call_shape("be terse", [{"role": "user", "content": "hi"}])
    check("system is a top-level key (string)",
          lambda: shape()["system"] == "be terse")
    check("messages holds only the turns (no system entry)",
          lambda: shape()["messages"] == [{"role": "user", "content": "hi"}])
    check("no role=='system' leaked into messages",
          lambda: all(m["role"] != "system" for m in shape()["messages"]))

    print("Exercise 2 — reconstruct the transcript:")
    PRIOR = [
        {"role": "user", "content": "hello"},
        {"role": "assistant", "content": "hi!"},
    ]
    check("new user msg appended after the whole prior transcript",
          lambda: next_messages(PRIOR, "again") == [
              {"role": "user", "content": "hello"},
              {"role": "assistant", "content": "hi!"},
              {"role": "user", "content": "again"},
          ])
    check("prior transcript is NOT mutated",
          lambda: (next_messages(PRIOR, "again"), len(PRIOR) == 2)[1])
    check("first turn = just the new user msg",
          lambda: next_messages([], "start") == [{"role": "user", "content": "start"}])

    print("Exercise 3 — stop_reason diagnosis:")
    check("end_turn -> complete", lambda: diagnose("end_turn") == "complete")
    check("max_tokens -> truncated_output", lambda: diagnose("max_tokens") == "truncated_output")
    check("model_context_window_exceeded -> context_overflow",
          lambda: diagnose("model_context_window_exceeded") == "context_overflow")

    print("Exercise 4 — structured-output config (prefill replacement):")
    cfg = lambda: structured_output_config(["name", "amount"])
    check("format.type marks a json schema",
          lambda: cfg()["format"]["type"] == "json_schema")
    check("schema requires every field",
          lambda: sorted(cfg()["format"]["schema"]["required"]) == ["amount", "name"])
    check("each field typed as string",
          lambda: all(p == {"type": "string"}
                      for p in cfg()["format"]["schema"]["properties"].values()))

    print("Part 3 — extraction call assembly:")
    kw = lambda: build_extraction_call("Acme posted Q3 revenue of $4.2M, up from $3.8M.")
    check("system rides at the top level (not in messages)",
          lambda: kw()["system"] == EXTRACTION_SYSTEM
                  and all(m["role"] != "system" for m in kw()["messages"]))
    check("exactly one user turn, and the source text is in it",
          lambda: len(kw()["messages"]) == 1
                  and kw()["messages"][0]["role"] == "user"
                  and "Acme" in kw()["messages"][0]["content"])
    check("output_config enforces the three fields (schema, not prefill)",
          lambda: sorted(kw()["output_config"]["format"]["schema"]["required"])
                  == ["company", "prior_revenue", "q3_revenue"])
    check("max_tokens is set and sane",
          lambda: isinstance(kw()["max_tokens"], int) and kw()["max_tokens"] > 0)

    passed = sum(1 for _, c in results if c)
    print(f"\n{passed}/{len(results)} green.",
          "All green — anatomy owned." if passed == len(results) else "Keep going.")


def _live_demo():
    """The actual 5-min bank-gate call. Requires `pip install anthropic` and
    ANTHROPIC_API_KEY set. Run with:  python 2026-07-08_anatomy-of-a-prompt.py --live
    Prints the extracted JSON and the stop_reason (prove you checked it)."""
    import anthropic
    client = anthropic.Anthropic()
    kwargs = build_extraction_call("Acme Corp posted Q3 revenue of $4.2M, up from $3.8M.")
    resp = client.messages.create(**kwargs)
    text = next((b.text for b in resp.content if b.type == "text"), "")
    print("EXTRACTED:", text)
    print("STOP_REASON:", resp.stop_reason)   # want "end_turn" — anything else means read the flag


if __name__ == "__main__":
    import sys
    if "--live" in sys.argv:
        _live_demo()
    else:
        _run_tests()


# ════════════════════════════════════════════════════════════════════════════
# ANSWER KEY — no peeking until you've answered Part 1 cold.
# ════════════════════════════════════════════════════════════════════════════
#
# A1. `system` is a SEPARATE TOP-LEVEL parameter on messages.create(...). The
#     `messages` array holds ONLY user and assistant turns. Render order is
#     tools -> system -> messages, so a frozen system prompt (+ frozen tools)
#     forms a stable, CACHEABLE PREFIX; only the volatile user turns fall after
#     the cache line. File system as messages[0] and you lose the model for
#     where the prompt cache boundary lives.
#     CLIENT LINE: "The instructions live in their own slot, above the chat —
#     that's what lets us cache them and only pay for the new turn each time."
#
# A2. messages = [user, assistant, user, assistant, user]. The assistant entries
#     are the model's OWN prior replies, fed back in. The API is stateless, so
#     the ONLY reason it 'remembers' turn 1 is that turn 1's assistant reply is
#     physically in the array you re-send. No server-side memory — you send the
#     transcript, it re-reads the transcript.
#     CLIENT LINE: "It doesn't remember — we hand it the whole conversation
#     every call, so memory is something we send, not something it stores."
#
# A3. max_tokens caps OUTPUT and truncates SOFTLY — it stops mid-generation,
#     possibly mid-sentence, no error, with stop_reason="max_tokens". The
#     context window caps input+output combined and REJECTS HARD, with
#     stop_reason="model_context_window_exceeded". You check `stop_reason` on the
#     response every time; "end_turn" is the clean finish.
#     CLIENT LINE: "One limit cuts the answer short but tells you it did; the
#     other refuses the request outright — we check the stop flag to know which."
#
# A4. Shipping the prefill against claude-opus-4-8 returns a 400 — trailing
#     assistant-turn prefills are removed on Claude 4.6+. Replacement: Structured
#     Outputs, output_config={"format":{"type":"json_schema","schema":{...}}}.
#     Better because it ENFORCES the schema server-side (validated conforming
#     JSON), where prefill only NUDGED the model and could still drift.
#     CLIENT LINE: "We don't trick it into a format anymore — we hand it a schema
#     it's guaranteed to match, so the output is validated, not just hoped for."
