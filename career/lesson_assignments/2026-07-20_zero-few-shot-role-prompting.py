"""
LESSON ASSIGNMENT — "Zero-shot, few-shot, role prompting" (Curriculum §1.3, Tier 1)
Date taught: 2026-07-20  |  Source: Eden Marco lec 69-70 + Anthropic prompting docs  |  Pair: /learn session
Researched live against platform.claude.com "Prompting best practices" (2026-07-20).
Note: the old per-technique tutorial pages are GONE — merged into one page with
per-model guidance first. Prompting advice is now model-versioned.

────────────────────────────────────────────────────────────────────────────
WHAT WE'RE TARGETING
────────────────────────────────────────────────────────────────────────────
§1.1: a call is stateless re-sent tokens. §1.2: how those tokens are
structured. §1.3 is the first STEERING unit: making the model behave.
The unit is not "zero vs few shot" — it's the 2026 STEERING LADDER:

  1. ZERO-SHOT + clear, direct instructions — the DEFAULT. Current models are
     strong enough that the docs say try direct instruction first. Cheapest
     rung (fewest tokens). 2026 addition: give the WHY behind a rule
     ("read aloud by TTS, so no ellipses") — the model generalizes from
     motivation better than from bare commands.
  2. FEW-SHOT EXAMPLES — for FUZZY steering: tone, judgment boundaries,
     edge-case handling. Spec: 3-5 examples, wrapped in <example>/<examples>
     tags, and DIVERSE — examples teach everything they contain, including
     accidental patterns (all-positive labels, uniform length).
  3. STRUCTURED OUTPUTS — when the shape must be GUARANTEED. Schema enforces;
     examples only nudge. Guarantees SHAPE, not content quality.

  ROLE PROMPTING (orthogonal to the ladder): a one-sentence prior-shift in the
  top-level `system` param — changes tone, vocabulary, scope, judgment
  defaults. Does NOT add knowledge or accuracy. Lives in system → part of the
  cacheable prefix (render order tools -> system -> messages, from §1.2), so
  you write it once and it steers every turn ~free.

⚠ CURRENCY LANDMINE (why we learn live, not from a 2024 course):
  Aggressive prompting — "CRITICAL: You MUST...", "If in doubt, always..." —
  now BACKFIRES. Claude 4.5/4.6+ follow the system prompt much more closely,
  so language written to overpower a 2023 model's reluctance causes
  OVERTRIGGERING today. Current fix: plain sentences ("Use this tool
  when..."). A course recording teaches the aggressive style as a technique;
  it's now an anti-pattern.

HOW TO USE THIS
  - PART 1: answer the concept questions COLD, before scrolling to the key.
  - PART 2 + PART 3: fill in each TODO. Boilerplate is pre-written so you
    focus on the CONCEPT and the FLOW, not syntax. The TODOs tell you WHAT to
    do, not the line to type. Run
    `python 2026-07-20_zero-few-shot-role-prompting.py` — red/green at the
    bottom. No AI until you've struggled 10+ min.
  - Done = all tests green AND you can say the Part 1 answers cold.
════════════════════════════════════════════════════════════════════════════
"""


# ════════════════════════════════════════════════════════════════════════════
# PART 1 — CONCEPT QUESTIONS (answer cold, THEN check the key at the bottom)
# ════════════════════════════════════════════════════════════════════════════
#
# Q1. Walk the steering ladder: the three rungs, what kind of job makes you
#     step UP a rung, and the one-line cost logic for why you don't start at
#     the top.

'''
your answer here
'''

# Q2. The current few-shot spec: how many examples, how are they formatted in
#     the prompt, and what is the one PROPERTY of an example set that stops it
#     from silently teaching the wrong thing? Give a concrete way an example
#     set goes wrong without that property.

'''
your answer here
'''

# Q3. Role prompting: name two things it genuinely changes, the one thing
#     people wrongly expect it to change, and WHERE the role lives in the API
#     call — plus why that placement makes it nearly free (name the render
#     order).

'''
your answer here
'''

# Q4. A pre-2026 course teaches "CRITICAL: You MUST use the search tool for
#     every question." What goes wrong shipping that against a current model,
#     why did the failure mode flip, and what does the current fix look like?

'''
your answer here
'''


# ════════════════════════════════════════════════════════════════════════════
# PART 2 — CODING EXERCISES (drill the facets; boilerplate pre-filled)
# ════════════════════════════════════════════════════════════════════════════

# ─── EXERCISE 1 — Choose the rung ───────────────────────────────────────────
# Given a description of the steering job, pick the cheapest rung that can do
# it. This is the decision, distilled.
#
# Concept it burns in: escalate only when the job demands it — instructions
# first, examples for fuzz, schema for guarantees.

def choose_rung(job: dict) -> str:
    """job has two boolean flags:
         needs_guaranteed_schema — output MUST parse against a fixed shape
         fuzzy_style_or_judgment — steering tone/edge-cases/judgment calls
       Return one of: "zero_shot", "few_shot", "structured_output".
    """
    # TODO: pick the rung. A guaranteed schema outranks everything (it's the
    #       only rung that ENFORCES). Otherwise fuzzy steering needs examples.
    #       Otherwise plain clear instructions are enough — that's the default.
    ...


# ─── EXERCISE 2 — Format the examples block ─────────────────────────────────
# Build the current-spec examples block from (input, output) pairs.
#
# Concept it burns in: examples are STRUCTURED (tags separate them from
# instructions) and live as one stable block you can park in the cacheable
# prefix.

def wrap_examples(pairs: list[tuple[str, str]]) -> str:
    """Return a single string:
       <examples>
         one <example> block per pair, each containing the input line then the
         output line
       </examples>
    """
    # TODO: for each (inp, out) pair build
    #         <example>\n<input>...</input>\n<output>...</output>\n</example>
    #       then join them all inside one <examples>...</examples> wrapper,
    #       newline-separated.
    ...


# ─── EXERCISE 3 — Catch the silent bias ─────────────────────────────────────
# Your example set teaches everything it contains — including patterns you
# didn't intend. Lint a set of example labels for the most common failure:
# uniformity.
#
# Concept it burns in: DIVERSE is the load-bearing word in the few-shot spec.
# All-same-label examples teach "always answer that label."

def examples_are_diverse(labels: list[str]) -> bool:
    """Return True only when the example set is usable: at least 2 examples
    AND more than one distinct label represented."""
    # TODO: implement exactly that rule.
    ...


# ─── EXERCISE 4 — 2026 prompt lint: flag aggressive language ────────────────
# Old-style "overpowering" prompt language now causes overtriggering on
# current models. Write the lint that flags it.
#
# Concept it burns in: the failure mode FLIPPED — models now follow the system
# prompt closely, so shouting produces over-eager behavior, not compliance.

AGGRESSIVE_MARKERS = ["CRITICAL", "YOU MUST", "ALWAYS", "IF IN DOUBT"]

def lint_for_overtriggering(instruction: str) -> list[str]:
    """Return the list of AGGRESSIVE_MARKERS present in `instruction`
    (case-insensitive match), in AGGRESSIVE_MARKERS order. Empty list = safe."""
    # TODO: check each marker against an upper-cased copy of the instruction;
    #       collect the ones found.
    ...


# ════════════════════════════════════════════════════════════════════════════
# PART 3 — PROJECT (the bank-gate build)
# A Cognizant-flavored code-review triage call that pulls all three levers ON
# PURPOSE, each doing the one job it's best at:
#   - ROLE (system): shifts judgment defaults toward a senior reviewer
#   - FEW-SHOT (system, inside the cacheable prefix): teaches the fuzzy
#     blocking/non-blocking boundary by example
#   - STRUCTURED OUTPUT: guarantees the label parses every time
# `_live_demo()` at the bottom fires it for real.
# ════════════════════════════════════════════════════════════════════════════

REVIEWER_ROLE = (
    "You are a senior code reviewer on an enterprise consulting team. "
    "Judge review comments by whether they block a merge."
)

# The fuzzy boundary few-shot exists to teach: severity is about IMPACT, not
# tone. Note the labels are deliberately MIXED — that's Exercise 3 in action.
TRIAGE_EXAMPLES = [
    ("SQL query concatenates raw user input", "blocking"),
    ("variable name `tmp2` is unclear", "non_blocking"),
    ("missing await on the payment call — result is a coroutine", "blocking"),
    ("prefer f-string over .format() here", "non_blocking"),
]

def build_triage_call(review_comment: str, model: str = "claude-opus-4-8") -> dict:
    """Return the kwargs dict you'd splat into client.messages.create(**kwargs)
    to classify `review_comment` as blocking / non_blocking with a reason."""
    # TODO: build and return a dict with these keys:
    #   - "model": the model arg
    #   - "max_tokens": a sane explicit cap (a few hundred)
    #   - "system": ONE string = the role sentence (REVIEWER_ROLE) followed by
    #               the examples block — build it with wrap_examples(TRIAGE_EXAMPLES).
    #               Both are STABLE, so both belong in the system prefix.
    #   - "messages": a one-entry list — a user turn asking to triage
    #                 `review_comment` (the volatile part goes LAST).
    #   - "output_config": a format dict marking a json schema, whose schema is
    #                 an object REQUIRING "severity" and "reason" — severity a
    #                 string constrained by an enum of the two valid labels,
    #                 reason a plain string. (Recall the shape from §1.2's
    #                 worksheet; add the enum constraint yourself.)
    ...


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

    print("Exercise 1 — choose the rung:")
    check("schema guarantee -> structured_output (even when also fuzzy)",
          lambda: choose_rung({"needs_guaranteed_schema": True,
                               "fuzzy_style_or_judgment": True}) == "structured_output")
    check("fuzzy tone/judgment -> few_shot",
          lambda: choose_rung({"needs_guaranteed_schema": False,
                               "fuzzy_style_or_judgment": True}) == "few_shot")
    check("plain job -> zero_shot (the default rung)",
          lambda: choose_rung({"needs_guaranteed_schema": False,
                               "fuzzy_style_or_judgment": False}) == "zero_shot")

    print("Exercise 2 — examples block:")
    blk = lambda: wrap_examples([("in1", "out1"), ("in2", "out2")])
    check("wrapped in one <examples> envelope",
          lambda: blk().strip().startswith("<examples>")
                  and blk().strip().endswith("</examples>"))
    check("one <example> tag per pair",
          lambda: blk().count("<example>") == 2 and blk().count("</example>") == 2)
    check("inputs and outputs both present and tagged",
          lambda: "<input>in1</input>" in blk() and "<output>out2</output>" in blk())

    print("Exercise 3 — diversity lint:")
    check("mixed labels pass",
          lambda: examples_are_diverse(["blocking", "non_blocking", "blocking"]) is True)
    check("uniform labels fail (silent bias)",
          lambda: examples_are_diverse(["blocking", "blocking", "blocking"]) is False)
    check("a single example is not a set",
          lambda: examples_are_diverse(["blocking"]) is False)

    print("Exercise 4 — overtriggering lint:")
    check("flags CRITICAL and YOU MUST",
          lambda: lint_for_overtriggering(
              "CRITICAL: you must use the search tool") == ["CRITICAL", "YOU MUST"])
    check("flags IF IN DOUBT",
          lambda: lint_for_overtriggering("If in doubt, call the tool") == ["IF IN DOUBT"])
    check("plain 2026-style instruction is clean",
          lambda: lint_for_overtriggering(
              "Use the search tool when the answer depends on current info") == [])

    print("Part 3 — triage call assembly:")
    kw = lambda: build_triage_call("hardcoded API key in settings.py")
    check("role sentence leads the system prompt",
          lambda: kw()["system"].startswith(REVIEWER_ROLE))
    check("examples ride in the system prefix (stable content), tagged",
          lambda: "<examples>" in kw()["system"]
                  and "<example>" in kw()["system"])
    check("example labels are diverse (both labels taught)",
          lambda: "blocking" in kw()["system"] and "non_blocking" in kw()["system"])
    check("exactly one user turn carrying the volatile comment",
          lambda: len(kw()["messages"]) == 1
                  and kw()["messages"][0]["role"] == "user"
                  and "hardcoded API key" in kw()["messages"][0]["content"])
    check("schema requires severity + reason",
          lambda: sorted(kw()["output_config"]["format"]["schema"]["required"])
                  == ["reason", "severity"])
    check("severity is enum-constrained to the two labels",
          lambda: sorted(kw()["output_config"]["format"]["schema"]["properties"]
                         ["severity"]["enum"]) == ["blocking", "non_blocking"])
    check("max_tokens is set and sane",
          lambda: isinstance(kw()["max_tokens"], int) and kw()["max_tokens"] > 0)

    passed = sum(1 for _, c in results if c)
    print(f"\n{passed}/{len(results)} green.",
          "All green — steering ladder owned." if passed == len(results) else "Keep going.")


def _live_demo():
    """The actual 5-min bank-gate call. Requires `pip install anthropic` and
    ANTHROPIC_API_KEY set. Run: python 2026-07-20_zero-few-shot-role-prompting.py --live
    Prints the schema-enforced triage JSON and the stop_reason."""
    import anthropic
    client = anthropic.Anthropic()
    kwargs = build_triage_call("test asserts on a hardcoded timestamp — flaky after midnight")
    resp = client.messages.create(**kwargs)
    text = next((b.text for b in resp.content if b.type == "text"), "")
    print("TRIAGE:", text)
    print("STOP_REASON:", resp.stop_reason)


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
# A1. Rung 1: zero-shot + clear direct instructions — the default; current
#     models usually don't need more, and it's the fewest tokens (the prompt is
#     re-sent every call, §1.1). Step up to rung 2 (few-shot) when the thing
#     you're steering is FUZZY — tone, judgment boundaries, edge cases —
#     because instructions can't fully specify "what a good one looks like."
#     Step up to rung 3 (structured outputs) when the shape must be
#     GUARANTEED: schema ENFORCES, examples only NUDGE. You don't start at the
#     top because every rung above zero-shot costs tokens on every call — and
#     you never spend examples on a job schema enforcement does for free.
#
# A2. 3-5 examples, wrapped in <example> tags inside an <examples> envelope so
#     the model can tell examples from instructions. The load-bearing property
#     is DIVERSITY: examples teach every pattern they contain, including
#     accidental ones. Concrete failure: a sentiment classifier whose examples
#     are all "positive" quietly teaches "always answer positive" — the
#     uniform pattern IS the lesson the model takes.
#
# A3. Genuinely changes: tone/vocabulary/register, AND scope/judgment defaults
#     (a Python-specialist role answers in Python unasked; a security-reviewer
#     role flags what a generic assistant waves through). Wrongly expected:
#     knowledge/accuracy — "you are a senior Rust engineer" doesn't make it
#     better at Rust, it shifts register and priorities, not capability. The
#     role lives in the top-level `system` param; render order is
#     tools -> system -> messages, so the role sits in the stable cacheable
#     prefix — written once, cached, steering every turn nearly free.
#
# A4. On current models (4.5/4.6+) that instruction OVERTRIGGERS — the tool
#     fires on questions that don't need it. The failure flipped because the
#     aggressive style was invented to overpower older models' reluctance;
#     current models follow the system prompt closely, so shouting now
#     produces over-eager literal compliance. Current fix: plain scoped
#     sentences — "Use the search tool when the answer depends on current
#     information" — and give the WHY so the model generalizes the boundary.
