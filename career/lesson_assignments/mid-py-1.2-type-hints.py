"""
LESSON ASSIGNMENT — "Type Hints in Earnest" (Mid-Python Prep §1.2, Tier 1)
Date taught: 2026-06-30  |  Source: job posting "strong Python + hands-on FastAPI"  |  Pair: /learn session

────────────────────────────────────────────────────────────────────────────
WHAT WE'RE TARGETING
────────────────────────────────────────────────────────────────────────────
In a plain script, type hints are decoration — CPython ignores them. In
FastAPI/Pydantic, the SAME hints become executable contract: they decide what
gets parsed, validated, coerced, documented, and rejected with a 422. The
interview question "how does FastAPI know a field is required / how does it
return a 422?" is really "do you understand your hints became the contract?"
This worksheet makes that reflex-fast.

Four facts to feel in your fingers, not just nod at:
  1. HINTS ARE NOT ENFORCED AT RUNTIME by CPython. They live in
     __annotations__; mypy/Pyright/ruff and runtime frameworks (Pydantic,
     FastAPI) are what READ and act on them. `def f(x: int)` then `f("hi")`
     raises only if some line inside trips on the wrong type — not because of
     the hint.
  2. NULLABLE != REQUIRED — two independent axes.
       nullable  = the TYPE     -> `int | None`     (value may be None)
       required  = the DEFAULT  -> no default = required; `= None` = optional
     `x: int | None`        -> REQUIRED, may be None
     `x: int | None = None` -> OPTIONAL, defaults to None
     Optional[int] means EXACTLY `int | None` — it does NOT mean "optional arg."
  3. CURRENT SYNTAX (3.9/3.10+): builtins + `|`, no typing imports for the
     common cases. `list[str]`, `dict[str, float]`, `int | None`.
     STALE: `List[str]`, `Dict[...]`, `Optional[int]`, `Union[int, str]`.
     PYDANTIC v1 quirk now GONE in v2: v1 made `Optional[x]` default to None
     implicitly (treated nullable as optional). v2 does NOT — `x: int | None`
     is a REQUIRED field. Carrying the v1 instinct into v2 is a real bug source.
  4. PROTOCOL = structural typing ("static duck typing"). A class satisfies a
     Protocol by HAVING the right methods/shape — no inheritance, no import, no
     registration. It's how you type "anything with a .read()" across classes
     you don't own (stdlib, boto3, vendor SDKs). isinstance() against a Protocol
     needs @runtime_checkable, and even then only checks the method EXISTS.

HOW TO USE THIS
  - PART 1: fill in each TODO. Boilerplate is pre-written so you focus on the
    CONCEPT and the FLOW, not syntax. Run `python mid-py-1.2-type-hints.py`.
    The tests at the bottom tell you red/green. No AI until you've struggled.
  - PART 2: answer each concept question OUT LOUD or in writing BEFORE you
    scroll to the answer key. For each, also write the one-line "interviewer
    version" — the crisp answer you'd say across the table.
  - Done = all tests green AND you can say the Part 2 answers cold.

  NOTE: requires Python 3.10+ (uses `X | None`) and `pip install pydantic>=2`.
════════════════════════════════════════════════════════════════════════════
"""

from typing import Protocol, runtime_checkable
from pydantic import BaseModel, ValidationError


# ─── EXERCISE 1 — Hints don't run; __annotations__ proves it ────────────────
# Type hints are stored as data on the function, not enforced. This exercise
# makes you READ that data so the "hints are inert at runtime" fact is concrete.
#
# Implement declared_types: return the function's annotation mapping (the dict
# Python stored from the hints). It already exists on every function — you just
# have to return the right attribute. Do NOT build the dict by hand.
#
# Concept it burns in: the hint is metadata in __annotations__; nothing checks
# it unless a tool or framework chooses to read it.

def declared_types(func) -> dict:
    # TODO: return the attribute where Python stores a function's type hints
    #       (the annotation mapping). One line, no manual dict construction.
    ...


# ─── EXERCISE 2 — The four-corner truth table, as Pydantic fields ───────────
# Build a model whose four fields are exactly the four combinations of
# {required, optional} x {not-nullable, nullable}. The field NAMES tell you
# which corner each one is. Choose the annotation + default for each so the
# tests (which probe required-vs-optional and null-vs-not) pass.
#
#   required_solid    -> required, NOT nullable   (must pass; can't be None)
#   required_nullable -> required, nullable        (MUST pass; may be None)
#   optional_solid    -> optional, NOT nullable    (may omit; defaults to "json")
#   optional_nullable -> optional, nullable        (may omit; defaults to None)
#
# Concept it burns in: nullable is the TYPE (`| None`), required is the DEFAULT
# (absence of one). They're independent — set each axis deliberately.

class ForecastQuery(BaseModel):
    # TODO: declare the four fields below with the right TYPE and DEFAULT so each
    #       lands in its named corner of the table. Use modern `str | None`
    #       syntax. Default the optional_solid field to the string "json".
    ...


# ─── EXERCISE 3 — Generics make validation DEEP ─────────────────────────────
# A bare `list` says "a list of something." A generic says "of what" — and that
# is what lets a framework validate each element. Annotate this function with
# CURRENT generic syntax: it takes a list of (lat, lon) float pairs and returns
# a mapping from a string key to a float.
#
# Implement to_lookup: build a dict mapping "lat,lon" (formatted string) -> the
# product lat*lon, for each pair. The point is the ANNOTATION as much as the
# body — use builtins + brackets, not typing.List/Dict/Tuple.
#
# Concept it burns in: `list[tuple[float, float]]` / `dict[str, float]` — the
# type PARAMETER is what makes validation and OpenAPI schemas precise.

def to_lookup(pairs):  # TODO: annotate the parameter and the return type
    # TODO: for each (lat, lon) pair, add an entry keyed by the string
    #       f"{lat},{lon}" whose value is lat * lon. Return the dict.
    ...


# ─── EXERCISE 4 — Protocol: type by shape, not lineage ──────────────────────
# You want a function that accepts "anything with a .read() returning bytes,"
# including classes you don't own. Define the Protocol that captures that shape,
# then a function typed against it. NEITHER concrete class below inherits the
# Protocol — they satisfy it structurally, which is the whole point.
#
# Concept it burns in: structural typing — having the method IS satisfying the
# interface. No inheritance/registration. @runtime_checkable is what lets the
# isinstance() test in the runner work (and it only checks the method exists).

@runtime_checkable
class Readable(Protocol):
    # TODO: declare the required shape — a `read` method taking no args and
    #       returning bytes. Use `...` as the body (it's a structural stub).
    ...


def read_all(source) -> bytes:  # TODO: annotate `source` with the Protocol type
    # TODO: call the source's read() method and return its bytes.
    ...


# These two satisfy Readable WITHOUT inheriting it — do not change them.
class FileLike:
    def read(self) -> bytes:
        return b"grib-bytes"

class NotReadable:
    def open(self) -> bytes:
        return b"nope"


# ════════════════════════════════════════════════════════════════════════════
# PART 2 — CONCEPT QUESTIONS (answer cold, THEN check the key at the bottom)
# Requirement: for each, also write the ONE-LINE "interviewer version".
# ════════════════════════════════════════════════════════════════════════════
#
# Q1. A teammate says "I added `Optional[int]` to that Pydantic field, so now
#     the client can leave it out." In Pydantic v2, are they right? Explain what
#     `Optional[int]` actually controls, and what they'd ACTUALLY need to change
#     to make the field omittable.

'''
your answer:


interviewer one-liner:

'''


# Q2. You see `from typing import List, Dict, Optional, Union` at the top of a
#     2021 file, and `def f(x: Optional[int]) -> List[str]:`. Rewrite that
#     signature in current (3.10+) idiom, and name which import(s) you no longer
#     need. Why does the old form "date you" in an interview?

'''
your answer:


interviewer one-liner:

'''


# Q3. You need a function to accept "any object with a `.connect()` method,"
#     including a class from a vendor SDK you can't edit. What typing tool, and
#     WHY does it beat (a) a shared base class / ABC and (b) no hint at all?
#     What's the gotcha if you want to `isinstance()` against it?

'''
your answer:


interviewer one-liner:

'''


# Q4. True or false, with reasoning: "If I write `def f(x: int): ...` and call
#     `f('hello')`, Python raises a TypeError because of the type hint." If
#     false, when (if ever) does an error actually occur, and what's the hint
#     doing in the meantime?

'''
your answer:


interviewer one-liner:

'''


# ════════════════════════════════════════════════════════════════════════════
# TEST RUNNER — run this file; green means the flow is right.
# ════════════════════════════════════════════════════════════════════════════
def _run_tests():
    results = []

    def check(name, cond_fn):
        try:
            ok = bool(cond_fn())
        except Exception as e:
            ok = False
            name = f"{name}  [errored: {type(e).__name__}: {e}]"
        results.append((name, ok))
        print(f"  {'PASS' if ok else 'FAIL'} — {name}")

    print("Exercise 1 — hints live in __annotations__:")
    def _sample(x: int, y: str) -> bool: ...
    check("returns the annotation mapping",
          lambda: declared_types(_sample) == {"x": int, "y": str, "return": bool})

    print("Exercise 2 — required vs nullable corners:")
    # required_solid + required_nullable must be provided; the two optionals may be omitted.
    base = dict(required_solid="t2m", required_nullable=None)
    check("omitting an optional field is fine (defaults apply)",
          lambda: ForecastQuery(**base).optional_solid == "json")
    check("optional_nullable defaults to None",
          lambda: ForecastQuery(**base).optional_nullable is None)
    check("required_nullable accepts an explicit None",
          lambda: ForecastQuery(**base).required_nullable is None)
    def _missing_required():
        try:
            ForecastQuery(required_nullable=None)  # omit required_solid
            return False
        except ValidationError:
            return True
    check("omitting a REQUIRED field raises ValidationError", _missing_required)
    check("required_nullable is required even though it's nullable",
          lambda: (lambda: ForecastQuery(required_solid="t2m"))() and False
          if False else _req_nullable_required())

    print("Exercise 3 — generics:")
    check("builds the lat,lon -> product lookup",
          lambda: to_lookup([(2.0, 3.0), (4.0, 5.0)]) == {"2.0,3.0": 6.0, "4.0,5.0": 20.0})

    print("Exercise 4 — Protocol structural typing:")
    check("a class WITH read() satisfies it (no inheritance)",
          lambda: read_all(FileLike()) == b"grib-bytes")
    check("isinstance works via @runtime_checkable",
          lambda: isinstance(FileLike(), Readable) is True)
    check("a class WITHOUT read() does NOT satisfy it",
          lambda: isinstance(NotReadable(), Readable) is False)

    passed = sum(1 for _, c in results if c)
    print(f"\n{passed}/{len(results)} green.",
          "All green — primitive owned." if passed == len(results) else "Keep going.")


def _req_nullable_required() -> bool:
    # required_nullable has NO default -> omitting it must raise, proving
    # nullable != optional.
    try:
        ForecastQuery(required_solid="t2m")
        return False
    except ValidationError:
        return True


if __name__ == "__main__":
    _run_tests()


# ════════════════════════════════════════════════════════════════════════════
# ANSWER KEY — no peeking until you've answered Part 2 cold.
# ════════════════════════════════════════════════════════════════════════════
#
# A1. They're WRONG in Pydantic v2. `Optional[int]` means exactly `int | None`
#     — it controls the VALUE's type (may be an int or None), not whether the
#     field is required. A field is omittable only if it has a DEFAULT. So
#     `x: int | None` is still REQUIRED (client omitting it -> 422). To make it
#     omittable they must add a default: `x: int | None = None`. (In Pydantic
#     v1 Optional implicitly defaulted to None — that magic was removed in v2,
#     which is exactly why their instinct is stale.)
#     INTERVIEWER LINE: "Optional just means the value can be None; in v2 it's
#     still required unless you give it a default — nullable and required are
#     different axes."
#
# A2. Current: `def f(x: int | None) -> list[str]:`. You no longer need ANY of
#     those typing imports — `int | None` replaces Optional/Union, and the
#     builtin `list[...]` replaces `List`. (Keep `typing` only for things with
#     no builtin form, e.g. Protocol, Callable, TypeVar.) The old form dates you
#     because 3.9 brought builtin generics and 3.10 brought `X | None`; writing
#     `List`/`Optional` signals you learned on a pre-2021 codebase — same smell
#     as Pydantic v1 `.dict()`.
#     INTERVIEWER LINE: "I'd write `int | None` and `list[str]` — builtins plus
#     the union operator; the typing.List/Optional forms are pre-3.10."
#
# A3. Use a `Protocol` (structural typing). Define `class HasConnect(Protocol):
#     def connect(self) -> ...: ...` and type the param `HasConnect`.
#     (a) Beats an ABC because an ABC requires the class to INHERIT it — you
#     can't make a vendor SDK class subclass your base, but Protocol matches by
#     SHAPE, so the vendor class satisfies it for free. (b) Beats no-hint
#     duck-typing because you keep the flexibility AND get static checking —
#     mypy flags a caller passing something without `.connect()` before runtime.
#     Gotcha: a plain Protocol can't be used with isinstance() — you must add
#     `@runtime_checkable`, and even then it only checks the method EXISTS, not
#     its signature/return type.
#     INTERVIEWER LINE: "A Protocol — it types by shape, so a class I can't edit
#     satisfies it without inheriting; I add @runtime_checkable only if I need
#     isinstance, and that only checks the method exists."
#
# A4. FALSE. CPython does not check type hints at runtime — `f('hello')` does
#     NOT raise because of the hint. The hint just sits in `f.__annotations__`.
#     An error occurs only if/when a line INSIDE the function performs an
#     operation the string can't support (e.g. `x + 1` -> TypeError on str+int);
#     if the body never does anything int-specific, it runs clean. Enforcement
#     comes from mypy/Pyright/ruff statically, or a framework that opts in to
#     reading the hints (Pydantic/FastAPI) — never from the interpreter itself.
#     INTERVIEWER LINE: "Hints aren't enforced at runtime — they're metadata;
#     an error only happens if the body does something the actual type can't do,
#     and static checkers or Pydantic are what enforce the contract."
