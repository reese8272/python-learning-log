# ~~Reese's Python Learning Log~~ — ARCHIVED

> **This file is superseded by `CAREER_LOG.md`.** Do not update this file. It is kept for historical reference only.

---

**Started:** 2025-12-09  
**Primary Focus:**

- Boot.dev backend path + RAG course
- Krish Naik DS/NLP Course (Udemy)
- neetcode problem-solving practice

**All resources now on personal device** — no work laptop dependencies.

**What Gets Logged:** Only direct Python coding practice and problem-solving attempts  
**What Doesn't:** Work assignments, theory without practice, language diversions

**3-Month Goal:** Solve 5-6/10 Python problems from scratch in 30-60 min, explaining reasoning throughout

**Reference:**
- `patterns.md` — Patterns & mental models (add a row when something proves reliable)
- Weekly / monthly reflection → handled by `/weekly-review` and `/monthly-review`

-----

## SKILLS TRACKER

*Update when something genuinely levels up. Be honest.*

| Skill | Level | Notes | Last Practiced |
|-------|-------|-------|----------------|
| Python basics (loops, functions, classes) | Can do independently | **LEVELED UP:** Implemented functional programming patterns solo (generators, higher-order functions, composition) | 2026-02-18 |
| Generators & yield | Can do independently | Built lazy iterators from scratch (map_iter, filter_iter); infinite Fibonacci with `while True: yield` | 2026-01-19 |
| Higher-order functions | Can do independently | **LEVELED UP:** Filter + map composition, callbacks, functions returning functions | 2026-01-19 |
| Decorators | Can do independently | **LEVELED UP:** @property (encapsulation, `_variable` convention), @staticmethod (class-namespaced utilities), @classmethod (alternative constructors — use `cls` not class name for inheritance), @cache (automated memoization), @dataclass (data containers, Value Object pattern). Previously: timer wrapper pattern. | 2026-03-19 |
| Memoization | Can do independently | Dict cache with `if n in memo` check, store before return | 2026-01-19 |
| Currying | Can use with reference | Nested closures returning functions — `f(a)(b)(c)` pattern | 2026-01-19 |
| functools.partial | Can use with reference | Pre-fill arguments: `partial(multiply, y=2)` creates doubler | 2026-01-19 |
| Function composition | Can do independently | `f(g(x))` pattern — inner function closure capturing outer functions | 2026-01-19 |
| Context managers | Can use with reference | `with open()` pattern with try/except error handling | 2026-01-19 |
| argparse CLI basics | Can use with reference | Understand parser hierarchy (ArgumentParser → subparsers → arguments), dest parameter, args namespace | 2025-12-16 |
| Dict transformation & aggregation | Can do independently | Loop + conditionals + dict building, grouping/aggregation with nested dicts | 2025-12-22 |
| DSA (algorithms) | Can implement with reasoning | **LEVELED UP:** DFS from scratch — recursion, cycle prevention with set, base case handling | 2025-12-22 |
| Recursion on nested structures | Can do independently | **LEVELED UP:** Tree/nested dict traversal. Key insight: self-similar structures — the part looks like the whole, so the function handles one level and delegates the rest to itself. | 2026-01-20 |
| BFS shortest path | Can do independently | Queue-based traversal, return depth+1 when goal found | 2026-01-19 |
| Binary search | Can implement with reasoning | Descending order variant with duplicate handling. Key: `low` converges to insertion point, `<=` ensures convergence check | 2025-12-31 |
| Two-pointer technique | Can implement with reasoning | Closest pair sum on sorted array. Setup: low/high at ends, move based on sum vs target comparison | 2025-12-31 |
| Data structures (lists, dicts, sets) | Can do independently | **LEVELED UP:** Instinctively reached for dict for O(n) counting; understand when dict > list for lookups/counting | 2026-01-03 |
| Stacks & Queues | Can do independently | Time complexity diagnosis without hesitation — O(n) insertion, deletion, etc. | 2026-02-11 |
| Linked Lists | Can implement with reasoning | Implemented `__iter__` with generator. Tripped on using generator within own class — resolved with `self` (see Patterns). | 2026-02-11 |
| RAG fundamentals | In progress | Learning through Boot.dev RAG course — modularity, code cleanliness, retrieval patterns | 2026-01-07 |
| Big O notation | Can do independently | Time/space complexity for common sorting algorithms — can explain cold | 2026-02-09 |
| Bubble sort | Can do independently | Implemented from scratch, no friction | 2026-02-09 |
| Insertion sort | Can do independently | Implemented from scratch, no friction | 2026-02-09 |
| Merge sort | Can implement with reasoning | Logic is understood — recursive split/merge. Tripped on syntax (bare `return` instead of `return arr` in base case), not on the algorithm itself. | 2026-02-09 |
| Quick sort | Can implement with reasoning | Partitioning logic is understood. Needed clarification on tracking pivot/i/j indices during partition, but conceptual understanding was there. | 2026-02-09 |
| pandas | Exposed | Used in work, need AI help | - |
| numpy | Exposed | Used in work, need AI help | - |
| Stats/Probability | Gap | Need to learn | - |
| NLP techniques | Gap | Target skill from DS Course | - |

**Level definitions:**

- **Gap:** Haven't learned yet
- **Exposed:** Seen it, used it with help, can't do it alone
- **In progress:** Actively learning, not enough reps to assess level yet
- **Can use with reference:** Can do it if I look things up
- **Can implement with reasoning:** Understand the logic, may need syntax help
- **Can do independently:** No AI, no docs, I got this

-----

## INDEPENDENCE TRACKER

*The whole point: proving you can do things WITHOUT AI*

| Date | Problem/Task | Difficulty | Solo Attempt Time | Result | Notes |
|------|--------------|------------|-------------------|--------|-------|
| 03/19/26 | **Python Decorators — deducing design intent** (@property, @staticmethod, @classmethod, @cache, @dataclass) | **4-5/10** | Session | **Independently deduced key patterns** | Constructed @classmethod car dealership example (`Car.from_string(...)`) before being told. Mapped @cache to manual dict memoization immediately. ID'd @staticmethod vs module tradeoff. Identified @dataclass as data container signal. Design rationale deduced through questioning, not recitation. |
| 02/18/26 | **Fix Collect Top Scores (Boot.dev)** | **3-4/10** | ~5 min | **Solved solo** | Control flow with break/continue/sentinel. Filter by min_score, stop at -1 sentinel, enforce max_scores limit. No hesitation — loop + conditionals pattern is locked in. |
| 02/11/26 | **Stacks, Queues & Linked Lists (Boot.dev DSA)** | **4-6/10** | Full session | **Stacks/Queues: Solved solo. Linked Lists: Solved with hints** | Stacks and queues — diagnosed all time complexities without hesitation. Linked lists: implemented `__iter__` generator successfully, only tripped on how to call the generator within the class itself (answer: use `self`). |
| 02/09/26 | **Sorting Algorithms from Scratch (merge, quick, bubble, insertion) + Big O Refresher** | **5-7/10** | Full session | **Mostly solo (syntax help only)** | Refresher after ~3 week gap. Bubble and insertion came naturally. Merge and quick sort were logically correct — issues were syntax-level: bare `return` instead of `return arr` on merge sort base case, and index tracking clarification on quick sort pivot/i/j. Big O analysis solid across all four without reference. |
| 01/20/26 | **Sum Task Durations Recursively** | **7/10** | ~10 min | **Solved solo** | Nested task structure with optional subtasks. Base case: empty list returns 0. Recursive case: iterate tasks, add duration, recurse on subtasks if present. **Key insight articulated:** "the structure of the subtasks is the same structure as the parent tasks" — self-similar data = recursion is the natural fit. |
| 01/19/26 | **Advanced Functions Module (15 exercises)** | **4-6/10** | ~45-60 min total | **Completed** | Memoization, **kwargs filtering, callbacks, decorators (timer wrapper), higher-order functions (filter + map composition), function composition, partial application, generators (infinite Fibonacci), currying, context managers, type separation, mutable default state. All working code. |
| 01/19/26 | **Fix Shortest Social Connection (BFS)** | **5/10** | ~1 min | **Solved solo** | Recognized DFS vs BFS issue immediately. Key insight: `depth` is where we came from, `+1` is where we are now — return `depth + 1` when neighbor equals goal. |
| 01/03/26 | **Find Suspicious Users (Pick Right Data Structure)** | **6/10** | ~2 min | **Solved solo** | Dictionary for O(n) counting. Used second dict for duplicate tracking (worked but unnecessary). **Pattern learned:** Use `== threshold` instead of `>= threshold` for single-trigger events — fires exactly once when crossed, no extra tracking needed. |
| 12/31/25 | **Two-Pointer - Closest Pair Sum** | **5/10** | ~10 min | **Solved solo** | **First two-pointer problem!** New DSA pattern, first try, all tests passed. Setup: `low = 0`, `high = len(nums) - 1`. Logic: sum too big → high down, sum too small → low up. Early return on exact match. Tracked best diff and final pair. Clean implementation. Could simplify diff calc with `abs()` but code works. |
| 12/31/25 | **Binary Search - Find Player Rank (descending order, insert after duplicates)** | **6/10** | ~30-40 min | **Solved with hints** | Tricky because descending order inverts standard binary search logic. Key learnings: (1) `while low <= high` is standard — ensures we check when pointers converge, (2) For descending + "insert after duplicates": `>=` moves `low` right, `<` moves `high` left, (3) Return `low` not `mid` — `low` converges to insertion point by design, `mid` is just a temp calculation, (4) `+1` for 1-based ranking. Debugged through multiple iterations — comparison direction and loop condition were the bugs. |
| 12/22/25 | **Depth-First Path Search (DFS with recursion)** | **6/10** | ~15-20 min | **Solved solo** | **First algorithm implementation from scratch.** Handled cycle prevention with set, base cases, recursive exploration. Key debugging insight: needed `if has_path_dfs(...)` to propagate True upward. Had correct `==` and `return False` initially, changed during debugging, forgot to revert. |
| 12/22/25 | Summarize Purchases by Category (grouping/aggregation) | 5-6/10 | ~3-4 min | Solved solo | Aggregation pattern with nested dicts. No hesitation on "check if key exists → initialize or update" logic. Minor note: explicit empty check was redundant but harmless. |
| 12/22/25 | Build Inventory Status Map (dict transformation) | 3/10 | ~2 minutes | Solved solo | Warmup rep. Loop + conditionals + dict building — no hesitation. Minor cleanup: removed unnecessary `continue` statements. |
| 12/16/25 | argparse CLI implementation | 4/10 | ~5 minutes | Solved with hints | Needed walkthrough of boilerplate to understand the parser hierarchy, but wrote the implementation (`print(f"Searching for: {args.query}")`) solo. Asked good "why" questions before coding — understood the system instead of just copy/pasting. |
| 12/13/25 | **Functional Data Pipeline (map_iter, filter_iter, compose, pipe)** | **10/10** | ~15 minutes | **Solved solo** | **BREAKTHROUGH:** Built lazy iterators with yield, implemented right-to-left function composition, threaded values through pipe. First 10/10 problem solved completely independently. Strategy: broke problem into pieces, tackled one function at a time. Almost missed "right-to-left" detail in compose but caught it. Minor edge case bug (returned tuple instead of function when len==1) but passed all tests. Key learning: slow down, read carefully, solve incrementally. |
| 12/09/25 | sliding n-grams window | 5/10 | ~15 minutes | Needed AI | was sort of unsure of the question, and then gemini helped me understand that in a window problem, you can do for range(len(what you're sliding over) - <window size> + 1 to catch the last bit of the window), because then if the window size is larger than the thing were sliding, it'll auto detect it and return nothing (empty list or empty string more likely) |

**Result options:** Solved solo, Solved with hints, Needed AI, Gave up

-----

## ACTIVE STRUGGLES

*What's blocking you RIGHT NOW. When resolved, delete and update Skills Tracker.*

- **Merge sort base case syntax:** Logic was correct but wrote bare `return` instead of `return arr` when array length is 1. Kept getting `None` as results. The algorithm worked — the Python syntax didn't. Need to internalize: in Python, bare `return` always returns `None`. If your base case IS a value, return that value.
- **Quick sort index tracking:** Understood the partitioning concept (pick pivot, smaller left, larger right) but got turned around tracking pivot, i, and j positions during the partition step. Was a clarification question, not a conceptual gap. Need more reps to make the index dance automatic.

