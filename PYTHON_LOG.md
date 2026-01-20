# Reese's Python Learning Log

**Started:** 2025-12-09  
**Primary Focus:**

- Boot.dev backend path + RAG course
- Krish Naik DS/NLP Course (Udemy)
- neetcode problem-solving practice

**All resources now on personal device** — no work laptop dependencies.

**What Gets Logged:** Only direct Python coding practice and problem-solving attempts  
**What Doesn't:** Work assignments, theory without practice, language diversions

**3-Month Goal:** Solve 5-6/10 Python problems from scratch in 30-60 min, explaining reasoning throughout

**Archive Files:**
- `weekly_log_archive.md` — Past weekly logs
- `monthly_log_archive.md` — Past monthly check-ins

-----

## WHO I AM

**Role:** Junior Python Developer at Cognizant  
**Day Job:** Data Science, ML, and Data Analytics pipelines  
**Learning Window:** 2-3 hours during 9-5 workday  
**Target:** Senior Python Engineer at Cognizant (specialization flexible)

**My Honest Baseline (as of 2025-12-09):**

- I know Python basics: loops, functions, classes, types, lists, dicts
- I can read and modify existing code
- I cannot build from scratch independently - I freeze at "thought to paper"
- Everything I've built has been with AI or external help
- The gap: neurons don't connect because AI fills in before I have to think

**What I've Been Exposed To (with help):**

- Multi-agent software team (dev, tester, security lead, team lead)
- MCP servers for file/directory read-write
- Customer data pipelines for insights on repeat callers and workflows

-----

## WEEKLY SCHEDULE

*Established: 2025-12-21*

**Philosophy:** Weekdays for lessons and guided learning. Weekends for deep work and harder challenges.

| Day | Learning Focus | Time | Notes |
|-----|----------------|------|-------|
| Mon | Boot.dev | ~2-3 hrs (work) | Lessons, concepts, guided exercises |
| Tue | Boot.dev | ~2-3 hrs (work) | Lessons, concepts, guided exercises |
| Wed | Krish Naik NLP/DS course | ~2-3 hrs (work) | Lessons, concepts, guided exercises |
| Thu | Krish Naik NLP/DS course | ~2-3 hrs (work) | Lessons, concepts, guided exercises |
| Fri | Neetcode + weekly reflection | ~2-3 hrs (work) | Problem-solving practice, update this log |
| Sat | Boot.dev (deep work) | 6-8 AM (2 hrs) | Harder challenges, uninterrupted thinking |
| Sun | NLP course (deep work) | 6-8 AM (2 hrs) | Harder challenges, uninterrupted thinking |

**Weekly total:** ~16-19 hours of intentional learning

**Daily rhythm (weekdays):**

- 5:00 AM - Wake
- 5:30-7:00 AM - Gym
- 7:00-8:00 AM - Bible study & journaling
- 8:00-9:00 AM - Kids to sitter
- 9:00-5:30 PM - Work (includes 2-3 hrs learning)
- 5:30-8:00 PM - Kids
- 8:00-9:00 PM - Decompress / passive prep for next day
- 9:00 PM - Bed

**Weekend rhythm:**

- 5:00 AM - Wake
- 6:00-8:00 AM - Deep learning work (at-home workout before or after)
- 8:00 AM onward - Family time

-----

## SKILLS TRACKER

*Update when something genuinely levels up. Be honest.*

| Skill | Level | Notes | Last Practiced |
|-------|-------|-------|----------------|
| Python basics (loops, functions, classes) | Can do independently | **LEVELED UP:** Implemented functional programming patterns solo (generators, higher-order functions, composition) | 2025-12-13 |
| Generators & yield | Can do independently | Built lazy iterators from scratch (map_iter, filter_iter); infinite Fibonacci with `while True: yield` | 2026-01-19 |
| Higher-order functions | Can do independently | **LEVELED UP:** Filter + map composition, callbacks, functions returning functions | 2026-01-19 |
| Decorators | Can do independently | Timer wrapper pattern — capture start/end, call inner func, return result | 2026-01-19 |
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
| RAG fundamentals | In progress | Learning through Boot.dev RAG course — modularity, code cleanliness, retrieval patterns | 2026-01-07 |
| pandas | Exposed | Used in work, need AI help | - |
| numpy | Exposed | Used in work, need AI help | - |
| Stats/Probability | Gap | Need to learn | - |
| NLP techniques | Gap | Target skill from DS Course | - |

**Level definitions:**

- **Gap:** Haven't learned yet
- **Exposed:** Seen it, used it with help, can't do it alone
- **Can use with reference:** Can do it if I look things up
- **Can do independently:** No AI, no docs, I got this

-----

## INDEPENDENCE TRACKER

*The whole point: proving you can do things WITHOUT AI*

| Date | Problem/Task | Difficulty | Solo Attempt Time | Result | Notes |
|------|--------------|------------|-------------------|--------|-------|
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

**No active struggles logged.** Update as they come up during RAG course.

-----

## PATTERNS & MENTAL MODELS

*Reusable insights worth remembering*

### Data Structure Selection
| Pattern | When to Use | Key Insight |
|---------|-------------|-------------|
| Dict for O(n) counting | Need to count occurrences, check membership, or aggregate | Dict lookup is O(1); nested loops scanning a list is O(n²) |
| `dict.get(key, default)` | Counting/accumulating in dicts | `count[x] = count.get(x, 0) + 1` — one line instead of if/else block |
| Set for cycle prevention | Graph traversal, avoiding revisits | O(1) membership check; add before recursing, check before exploring |

### Threshold & Trigger Logic
| Pattern | When to Use | Key Insight |
|---------|-------------|-------------|
| `== threshold` vs `>= threshold` | Single-trigger events (e.g., "first time X reaches N") | `==` fires exactly once when crossed; `>=` requires extra tracking to prevent duplicates |

### Two-Pointer Technique
| Pattern | When to Use | Key Insight |
|---------|-------------|-------------|
| Converging pointers | Sorted array, find pair matching condition (sum, diff, etc.) | `low = 0`, `high = len-1`. Move the pointer that gets you closer to target. Sorted = predictable movement. |
| Early return on exact match | Target found mid-search | `if condition_met: return result` — don't keep searching once you've won |

### Binary Search
| Pattern | When to Use | Key Insight |
|---------|-------------|-------------|
| `while low <= high` | Standard binary search loop | `<=` ensures you check when pointers meet (single element remaining); `<` skips edge cases |
| Return `low` not `mid` | Finding insertion point | `low` converges to answer by design; `mid` is just a temp calculation each iteration |
| Descending order search | Sorted descending (leaderboards, rankings) | Logic inverts: `>=` goes right (toward lower values), `<` goes left |

### Recursion & DFS
| Pattern | When to Use | Key Insight |
|---------|-------------|-------------|
| Self-similar structure recognition | Nested dicts, trees, subtasks, file systems | If the part looks like the whole, recursion is the natural fit. Handle one level, delegate the rest. |
| Boolean propagation | DFS/tree search returning True/False | `if recursive_call(...): return True` — must explicitly bubble up success, don't just call and ignore |
| Base case first | Any recursive function | Check termination conditions before recursive calls; prevents infinite loops and handles edge cases |
| Visited set | Graph traversal with cycles | Add node to visited *before* recursing into neighbors; check membership *before* exploring |

### BFS
| Pattern | When to Use | Key Insight |
|---------|-------------|-------------|
| Depth tracking | Shortest path problems | `depth` is where we came from; `depth + 1` is where we are now. Return `depth + 1` when goal found. |
| BFS vs DFS selection | Shortest path = BFS, exhaustive search = DFS | BFS guarantees shortest path in unweighted graphs; DFS explores depth-first (not shortest) |

### Function Patterns
| Pattern | When to Use | Key Insight |
|---------|-------------|-------------|
| Decorator structure | Timing, logging, auth wrappers | `def decorator(func): def wrapper(*args, **kwargs): ... return wrapper` |
| Memoization | Expensive recursive calls (Fibonacci, etc.) | Check cache first, compute + store if missing, return cached |
| Currying | Partial application, config builders | Each function returns the next function until all args collected |
| Mutable default for state | Function call counting, accumulators | `def f(x, state=[0])` — list persists across calls |
| Function composition | Chaining transformations | `f(g(x))` — inner closure captures outer functions |

### Sliding Window
| Pattern | When to Use | Key Insight |
|---------|-------------|-------------|
| Window range formula | Fixed-size window over sequence | `range(len(seq) - window_size + 1)` — auto-returns empty if window > sequence |

### Problem-Solving Meta-Strategies
| Pattern | When to Use | Key Insight |
|---------|-------------|-------------|
| Solve incrementally | Complex multi-part problems | Break into pieces, solve one function at a time, test as you go |
| Read twice, code once | Before starting any problem | Almost missed "right-to-left" in compose — slow down, catch details before writing |

-----

## SYSTEM IMPROVEMENTS LOG

*Meta-level changes that make learning more consistent*

| Date | Change | Impact |
|------|--------|--------|
| 01/07/26 | Purchased Udemy DS course on personal device ($15) | Eliminated work laptop dependency. All three learning pillars now accessible regardless of IT issues. |

-----

## CURRENT WEEK

*At end of week: move this section to weekly_log_archive.md and start fresh.*

### Week of: [01/19/26 - 01/25/26]

**What I Actually Did:**

- 01/20: Boot.dev — Sum Task Durations Recursively (7/10) — solved independently in ~10 min
- 01/19: Boot.dev — Fix Shortest Social Connection (BFS) — solved independently in ~1 min
- 01/19: Krish Naik DS Course — Completed Advanced Functions module (15 exercises)

**Attempted WITHOUT AI:**

| Date | Problem/Task | Difficulty | Solo Attempt Time | Result | Notes |
|------|--------------|------------|-------------------|--------|-------|
| 01/20/26 | Sum Task Durations Recursively | 7/10 | ~10 min | Solved solo | Nested task structure with optional subtasks. Self-similar data structure = recursion. Articulated WHY it works: "the structure of the subtasks is the same structure as the parent tasks." |
| 01/19/26 | Fix Shortest Social Connection (BFS) | 5/10 | ~1 min | Solved solo | Recognized DFS vs BFS issue immediately. Key insight: `depth` is where we came from, `+1` is where we are now — return `depth + 1` when neighbor equals goal. |
| 01/19/26 | Advanced Functions Module (15 exercises) | 4-6/10 | ~45-60 min total | Completed | Memoization, **kwargs filtering, callbacks, decorators (timer wrapper), higher-order functions (filter + map composition), function composition, partial application, generators (infinite Fibonacci), currying, context managers, type separation, mutable default state. All working code. |

**Where I Froze / Needed Help:**

- None logged yet this week

**What Clicked:**

- BFS vs DFS recognition is becoming automatic
- Decorator pattern (wrapper function capturing timing) feels natural now
- Currying with nested closures — `height(2)(3)(4)` pattern understood and implemented
- Recursion on nested structures — can now articulate WHY it guarantees full traversal

**Weekly Reflection:**

- **Hours actually spent learning:** [FILL IN END OF WEEK]
- **Solo attempts vs AI-assisted ratio:** [FILL IN END OF WEEK]
- **Progress toward 3-month goal (honest 1-10):** [FILL IN END OF WEEK]
- **What went well:** [FILL IN END OF WEEK]
- **What I avoided or half-assed:** [FILL IN END OF WEEK]
- **One thing to do differently next week:** [FILL IN END OF WEEK]

-----

## CURRENT MONTH

*At end of month: move this section to monthly_log_archive.md and start fresh.*

### Month: January 2026

**DS Course Progress:**

- Modules completed: Advanced Functions (01/19/26)
- Current module: [UPDATE]

**Boot.dev Progress:**

- Find Suspicious Users completed solo, 2 minutes (01/03/26)
- RAG course in progress — learning modularity patterns (01/07/26)
- Fix Shortest Social Connection (BFS) completed solo, 1 minute (01/19/26)
- Sum Task Durations Recursively (7/10) completed solo, 10 minutes (01/20/26)

**Independence Growth:**

- Problems solved solo this month: 3 (Find Suspicious Users 6/10, BFS fix 5/10, Sum Task Durations 7/10)
- Problems solved with hints: 0
- Module exercises completed: 15 (Advanced Functions)
- Hardest thing I did without AI: Sum Task Durations (7/10) — 10 minutes, recursive nested structure traversal

**Running total of independent solves:**

1. 10/10 functional programming (15 min) — Dec
2. 6/10 Find Suspicious Users (2 min) — Jan
3. 5/10 BFS shortest path (1 min) — Jan
4. 15x Advanced Functions exercises (~45-60 min total) — Jan
5. 7/10 Sum Task Durations recursion (10 min) — Jan

**Am I closer to the 3-month goal?**
Strong start to January. 7/10 in 10 minutes — ahead of the 5-6/10 in 30-60 min target. Data structure selection is becoming instinctive. BFS/DFS distinction now automatic. Recursion on nested structures now understood at the "can explain why it works" level, not just "can write working code" level. The Advanced Functions module reinforces patterns you already had (generators, composition) while adding new tools (decorators, currying, partial).

**Am I bouncing between systems or staying focused?**
[UPDATE END OF MONTH]

**Honest assessment - what needs to change?**
[UPDATE END OF MONTH]