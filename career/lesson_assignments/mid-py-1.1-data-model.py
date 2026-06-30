"""
LESSON ASSIGNMENT — "Data Model & Idiomatic Python" (Mid-Python Prep §1.1, Tier 1)
Date taught: 2026-06-26  |  Source: job posting "strong Python proficiency"  |  Pair: /learn session

────────────────────────────────────────────────────────────────────────────
WHAT WE'RE TARGETING
────────────────────────────────────────────────────────────────────────────
Every "gotcha" question in a mid-level Python screen lives in the data model —
the rules for how objects have identity, value, and behavior. You write Python
daily; this worksheet is about defending the parts an interviewer pushes on
ONE step past the happy path, where fumbles happen.

Four facts to feel in your fingers, not just nod at:
  1. IDENTITY vs VALUE. `is` compares object identity (same object in memory);
     `==` compares value (calls __eq__). The ONLY safe use of `is` is the
     singletons: `x is None` (also True/False). Never `is` for ints/strings —
     CPython caches ints -5..256, so `is` LOOKS right then betrays you at 1000.
  2. DEFAULT ARGS ARE EVALUATED ONCE — at `def` time, not per call. So a
     mutable default (`bucket=[]`) is ONE shared object that leaks across
     calls. Fix = the `None` sentinel.
  3. DEFINING __eq__ NUKES __hash__ TO None. The object becomes unhashable
     (can't be a set member or dict key) until you also define __hash__. The
     invariant behind it: if a == b, then hash(a) must == hash(b).
  4. FUNCTIONS ARE FIRST-CLASS OBJECTS. A bare function name (no parens) IS a
     value you can store, put in a list, and pass to another function. That one
     fact is what makes decorators, sorted(key=...), and Depends() possible.

You already did the GridPoint build (the __eq__/__hash__ angle, live). This
worksheet drills the OTHER facets so the whole primitive is yours.

HOW TO USE THIS
  - PART 1: fill in each TODO. Boilerplate is pre-written so you focus on the
    CONCEPT and the FLOW, not syntax. Run `python mid-py-1.1-data-model.py`.
    The tests at the bottom tell you red/green. No AI until you've struggled.
  - PART 2: answer each concept question OUT LOUD or in writing BEFORE you
    scroll to the answer key. For each, also write the one-line "interviewer
    version" — the crisp answer you'd say across the table.
  - Done = all tests green AND you can say the Part 2 answers cold.
════════════════════════════════════════════════════════════════════════════
"""


# ─── EXERCISE 1 — The one safe use of `is` ──────────────────────────────────
# `None` is a singleton: there is exactly ONE None object in the whole program,
# so identity (`is`) is the correct, idiomatic test for it. Equality (`==`)
# would work too but can be fooled by a class that overrides __eq__.
#
# Implement is_missing: return True when `value` is the None singleton, using
# the IDENTITY operator (not ==). One line.
#
# Concept it burns in: `is None` is the canonical check; reach for `is` only
# for the singletons (None / True / False), `==` for everything value-related.

def is_missing(value) -> bool:
    # TODO: return whether `value` is the None singleton, using identity
    #       comparison rather than equality.
    if value is None:
        return True
    return False


# ─── EXERCISE 2 — Prove the small-int cache bites ───────────────────────────
# CPython pre-creates and caches every int in -5..256, so all copies of a
# small int are the SAME object; ints outside that range are fresh objects.
# This is exactly why `is` is unsafe for value comparison.
#
# Implement same_object: return the result of an IDENTITY comparison between
# two separate variables both assigned `n`. (Build the two variables yourself
# inside the function from the parameter, then compare them with `is`.)
#
# Concept it burns in: the answer flips at the cache boundary (256 -> ok,
# 257 -> not), which is the whole reason you never use `is` on numbers.

def same_object(n: int) -> bool:
    # TODO: bind `n` to two separate local variables, then return whether
    #       those two variables are the SAME object (identity comparison).
    var1 = int(str(n))
    var2 = int(str(n))
    if var1 is var2:
        return True
    return False


# ─── EXERCISE 3 — Kill the mutable-default bug ──────────────────────────────
# This buggy version shares ONE list across every call that omits `bucket`,
# because the default is evaluated once at def-time. Leave it as the cautionary
# example; write the FIXED version below it.
#
# Concept it burns in: default args evaluate once; for mutable defaults use the
# None-sentinel so each call that omits the arg gets a FRESH object.

def add_buggy(item, bucket=[]):          # <-- do NOT "fix" this one; it's the bug
    bucket.append(item)
    return bucket

def add_fixed(item, bucket=None):
    # TODO: if no bucket was passed in, create a fresh empty list for this call;
    #       otherwise use the one that was passed. Then append item and return
    #       the list. (Use the singleton check from Exercise 1.)
    if bucket is None:
        bucket = []
    bucket.append(item)
    return bucket


# ─── EXERCISE 4 — The __eq__ / __hash__ contract ────────────────────────────
# Two GridPoints with the same lat/lon should be "equal" AND usable as set
# members / dict keys. __eq__ is written for you. The moment it exists, Python
# sets __hash__ to None and instances become unhashable — so you must define
# __hash__ too, derived from the SAME fields __eq__ compares.
#
# Concept it burns in: a == b REQUIRES hash(a) == hash(b); hash the same data
# you compare on, or sets/dicts silently misbehave.

class GridPoint:
    def __init__(self, lat: float, lon: float):
        self.lat = lat
        self.lon = lon

    def __eq__(self, other) -> bool:
        return isinstance(other, GridPoint) and (self.lat, self.lon) == (other.lat, other.lon)

    def __hash__(self) -> int:
        # TODO: return a hash derived from the SAME fields __eq__ compares
        #       (lat and lon together), so equal points share a hash.
        return hash((self.lat,self.lon))


# ─── EXERCISE 5 — Functions are first-class objects ─────────────────────────
# A bare function name (no parens) IS a value: you can store it, list it, and
# pass it to another function that calls it for you later. This is the move
# under decorators, sorted(key=...), and FastAPI's Depends().
#
# Implement run_all: given a list of functions and one value, call EACH
# function on the value and return the list of results, in order.
#
# Concept it burns in: `fn` is the function object; `fn(value)` calls it. You
# can hand functions around like any other value.

def run_all(funcs: list, value) -> list:
    # TODO: for each function in funcs, call it on `value`, and collect the
    #       results into a list (same order). Return that list.
    final = []
    for func in funcs:
        final.append(func(value))
    return final


# ════════════════════════════════════════════════════════════════════════════
# PART 2 — CONCEPT QUESTIONS (answer cold, THEN check the key at the bottom)
# Requirement: for each, also write the ONE-LINE "interviewer version".
# ════════════════════════════════════════════════════════════════════════════
#
# Q1. `a = 100; b = 100; a is b` is True, but `a = 1000; b = 1000; a is b` is
#     False. Explain why — and state the rule it teaches you about `is`.

'''
your answer:
anything between -5 and 256 are stored in cache, and even if it's a different object, when you say a=5 and b=5, when it's cached, it's saved to the same number, once you are outside of that range, numbers like 1000 do get saved to different memory allocations, meaning a is b would then fail.

interviewer one-liner:
^^^
'''


# Q2. A teammate writes `def get_cache(key, store={}): ...` and reuses `store`
#     as a per-call scratch dict. Name what goes wrong, WHY (the timing word),
#     and the fix.

'''
your answer:
When you have a mutable default, then every time you don't pass a parameter to that variable, it uses that default, thus any information in there previously will leak into your other calls. The fix is having your parameter = None, and checking if var = None: (do something). This creates the parameter as immutable.

interviewer one-liner:
The variable is a mutable default and will leak into other calls, and using a mutable default like None will fix that.
'''


# Q3. You add `__eq__` to a class so two instances can be "equal." A colleague
#     says "now it won't work as a dict key." Are they right? What exactly
#     happened, and what's the invariant you must respect when you fix it?

'''
your answer:
Yes, because you didn't modify the __hash__() function as well. If you don't, then the hash will default to None, and thus things that aren't simply values will not be hashable or unpackable. To fix this, you must override the hash function and hash the values that are associated with __eq__()

interviewer one-liner:
^^^ one liner mine as well be that one above. It's sufficient.
'''


# Q4. What does it mean that "functions are first-class objects" in Python, and
#     name one real feature (decorator, sorted key, DI, ...) that this enables
#     and could not exist without it.

'''
your answer:
first class functions means functions can be assigned to variables, and have attributes just like other variables. This allows you to do something like decorators and iterators. For example, you pass a list of functions to a parameter with apply(funcs, value), and for func in funcs, you can do func(value) and append it to a new list. Without a first class function, you can't do this.

interviewer one-liner:
They are functions that can be applied as variables and passed as parameters, and thus creating the ability to be used as generators or be passed as a list and iterated over.
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
            name = f"{name}  [errored: {type(e).__name__}]"
        results.append((name, ok))
        print(f"  {'PASS' if ok else 'FAIL'} — {name}")

    print("Exercise 1 — `is None`:")
    check("None -> True", lambda: is_missing(None) is True)
    check("0 is NOT missing (truthiness trap)", lambda: is_missing(0) is False)
    check("empty string is NOT missing", lambda: is_missing("") is False)

    print("Exercise 2 — small-int cache:")
    check("256 is cached -> same object", lambda: same_object(256) is True)
    check("257 is past the cache -> different object", lambda: same_object(257) is False)

    print("Exercise 3 — mutable default:")
    check("fixed: first call returns [1]", lambda: add_fixed(1) == [1])
    check("fixed: second omitted-arg call does NOT leak -> [2], not [1, 2]",
          lambda: add_fixed(2) == [2])
    check("fixed: explicit bucket still works",
          lambda: add_fixed(9, [7]) == [7, 9])

    print("Exercise 4 — __eq__/__hash__ contract:")
    check("equal points dedupe in a set",
          lambda: len({GridPoint(40.0, -80.0), GridPoint(40.0, -80.0)}) == 1)
    check("usable as a dict key",
          lambda: {GridPoint(40.0, -80.0): "rain"}[GridPoint(40.0, -80.0)] == "rain")
    check("different points stay distinct",
          lambda: len({GridPoint(40.0, -80.0), GridPoint(41.0, -80.0)}) == 2)

    print("Exercise 5 — first-class functions:")
    check("runs each function on the value, in order",
          lambda: run_all([str.upper, str.strip], "  hi  ") == ["  HI  ", "hi"])
    check("works with lambdas too",
          lambda: run_all([lambda x: x + 1, lambda x: x * 2], 10) == [11, 20])

    passed = sum(1 for _, c in results if c)
    print(f"\n{passed}/{len(results)} green.",
          "All green — primitive owned." if passed == len(results) else "Keep going.")


if __name__ == "__main__":
    _run_tests()


# ════════════════════════════════════════════════════════════════════════════
# ANSWER KEY — no peeking until you've answered Part 2 cold.
# ════════════════════════════════════════════════════════════════════════════
#
# A1. CPython pre-creates and caches every integer from -5 to 256 at startup,
#     so every `100` in the program is literally the SAME cached object ->
#     `is` (identity) is True. 1000 is outside the cache, so each assignment
#     makes a fresh object -> different identities -> `is` is False. The values
#     are equal in BOTH cases (`==` is True for both). Rule: `is` tests object
#     identity, not value — never use it to compare numbers/strings; use `==`.
#     Reserve `is` for the singletons (None/True/False).
#     INTERVIEWER LINE: "Small ints are cached, so `is` accidentally works
#     under 257 then breaks above it — `is` is identity, `==` is value; I only
#     use `is` for None."
#
# A2. The default `{}` is evaluated ONCE, at function-definition time, so every
#     call that omits `store` shares the SAME dict — state leaks across calls
#     (and across unrelated callers). The timing word is "definition-time"
#     (a.k.a. "evaluated once"). Fix: default to None and build a fresh dict
#     inside when none was passed (`if store is None: store = {}`).
#     INTERVIEWER LINE: "Mutable defaults are evaluated once at def-time, so
#     they're shared across calls — I default to None and create the object
#     inside the function."
#
# A3. They're right — UNTIL you fix it. Defining `__eq__` without `__hash__`
#     makes Python implicitly set `__hash__` to None, so instances are
#     unhashable and raise TypeError as a set member or dict key. `__eq__`
#     itself still works fine. Fix: define `__hash__`, derived from the same
#     fields `__eq__` compares. Invariant you must respect: if a == b then
#     hash(a) == hash(b) (equal objects must hash equal, or hash collections
#     can't find them). Caveat: if the object is mutable, prefer leaving it
#     unhashable — a key whose hash changes corrupts the dict.
#     INTERVIEWER LINE: "Defining __eq__ nulls __hash__, so I define both and
#     hash the same fields I compare — because equal objects must hash equal."
#
# A4. Functions are values: a function object has an identity, a type, and can
#     be assigned, stored in containers, passed as an argument, and returned.
#     `name` (no parens) is the object; `name()` calls it. This enables
#     decorators (a function taking/returning a function), `sorted(key=fn)`
#     (you hand sorted the function), callbacks, and dependency injection like
#     FastAPI's `Depends(get_db)` (you hand over the function and the framework
#     calls it for you). None of these exist without first-class functions.
#     INTERVIEWER LINE: "Functions are first-class objects — passable values —
#     which is exactly what lets decorators and things like Depends() take a
#     function and call it for you."
