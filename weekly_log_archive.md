# Weekly Log Archive

*Archived weekly logs from python-learning-log.md. Newest at top.*

---

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

### Week of: [01/05/26 - 01/11/26]

**What I Actually Did:**
- 01/07 (Tue): Boot.dev RAG course — continuing modularity and code cleanliness patterns

---

### Week of: [12/29/25 - 01/04/26]

**What I Actually Did:**
- **Binary search problem (12/31):** Solved with hints after ~30-40 min of debugging
  - Descending order leaderboard with duplicate handling
  - Learned: `<=` loop condition, comparison direction for descending, why `low` is the answer
- **Two-pointer problem (12/31):** Solved solo in ~10 min, first try, all tests passed
  - Closest pair sum on sorted array
  - New DSA pattern — two pointers converging from ends
- **Find Suspicious Users (01/03):** Solved solo in ~2 min, all tests passed
  - Dictionary for O(n) counting, threshold detection
  - Pattern: `== threshold` instead of `>= threshold` for single-trigger events

**Attempted WITHOUT AI:**
- Initial binary search implementation — had right structure, wrong details
- Two-pointer implementation — 100% solo, clean first attempt
- Find Suspicious Users — 100% solo, 2 minutes flat

**Where I Froze / Needed Help:**
- Comparison direction (`>=` vs `<=`) for descending order
- Loop condition (`<` vs `<=`) — didn't realize `<` skips edge cases
- Why we return `low` instead of `mid`

**What Clicked:**
- `low` converges to insertion point by design — it tracks "earliest position that could be the answer"
- `while low <= high` ensures we check when pointers meet (single element remaining)
- For descending order: `>=` means "go right" (toward lower scores), `<` means "go left"
- **Two-pointer pattern:** Start at both ends, compare sum to target, move the pointer that helps you get closer. Sorted array = predictable movement.
- **Single-trigger pattern:** Use `==` not `>=` when you only care about the moment something crosses a threshold

**Weekly Reflection:**

- **Hours actually spent learning:** [FILL IN END OF WEEK]
- **Solo attempts vs AI-assisted ratio:** 2 solo, 1 with hints (67% solo)
- **Progress toward 3-month goal (honest 1-10):** [FILL IN END OF WEEK]
- **What went well:** Pushed through binary search debugging instead of giving up. Crushed two-pointer first try. Smashed 6/10 in 2 minutes on 01/03.
- **What I avoided or half-assed:** [FILL IN END OF WEEK]
- **One thing to do differently next week:** [FILL IN END OF WEEK]

---

### Week of: [12/22/25 - 12/28/25]

**What I Actually Did:**
- **Morning warmup session (12/22):** 3 problems solved solo in ~25 minutes total
  - Inventory Status Map (3/10) — dict transformation warmup
  - Summarize Purchases (5-6/10) — aggregation with nested dicts
  - **DFS Path Search (6/10)** — first algorithm from scratch, recursion + cycle prevention
- Implemented "foundational training period" idea from last week's reflection

**Attempted WITHOUT AI:**
- All three morning problems — 100% solo
- DFS algorithm with recursion and cycle prevention using a set

**Where I Froze / Needed Help:**
- None — clean sweep on all three problems

**What Clicked:**
- DFS mental model: base cases first, track visited nodes, recurse through neighbors, propagate True upward
- Debugging insight: `if has_path_dfs(...)` vs just calling it — need to check return value to propagate success
- Warmup reps on fundamentals → confidence boost before harder work

**Weekly Reflection:**

- **Hours actually spent learning:** ~5-6 hours
- **Solo attempts vs AI-assisted ratio:** 3/3 solo (100%)
- **Progress toward 3-month goal (honest 1-10):** 7/10
- **What went well:** Morning warmup system works. Proved fundamentals are solid. First DSA implementation solo.
- **What I avoided or half-assed:** Didn't push into harder territory after the wins
- **One thing to do differently next week:** Stack another DSA pattern (binary search or two-pointer)

-----

### Week of: [12/15/25 - 12/19/25]

**What I Actually Did:**

- **MAJOR WIN:** Solved 10/10 difficulty functional programming challenge (Boot.dev) completely solo in ~15 minutes - map_iter, filter_iter, compose, pipe
- Started Boot.dev RAG course on personal device
- Learned argparse CLI fundamentals — parser hierarchy, subcommands vs arguments, dest parameter, args namespace

**Attempted WITHOUT AI:**

- Functional Data Pipeline implementation (generators, higher-order functions, function composition)
- argparse CLI print statement (small but solo)

**Where I Froze / Needed Help:**

- None on the functional programming challenge - brief confusion on compose, but figured it out by breaking down requirements
- argparse boilerplate — needed line-by-line walkthrough to understand structure before implementing

**What Clicked:**

- Generators with `yield` - already understood the concept, just needed to apply it
- Right-to-left vs left-to-right execution (compose vs pipe) - caught the detail by reading carefully
- **Process that worked:** Read part A → implement function A → read part B → implement function B. One small problem at a time.
- **Key insight:** I can solve hard problems when I slow down and decompose them instead of panicking
- **argparse mental model:** `dest="command"` just names the slot where the chosen subcommand is stored — not magic. Subcommands (`search`, `index`) are separate from their arguments (`query`, `filepath`) so each command can have independent argument sets. `args` only contains user-provided values, not CLI structure.

**Weekly Reflection:**

- **Hours actually spent learning:** Roughly 4-5 hours
- **Solo attempts vs AI-assisted ratio:** roughly 50% of the things I did were solo, but nearly all of it were significantly easier
- **Progress toward 3-month goal (honest 1-10):** 8/10 - Crushed a 10/10 problem solo in 15 minutes, exactly what the goal is about
- **What went well:** Stayed focused on Python (Boot.dev RAG course), didn't drift to C or theory. Proved I can solve complex problems independently. Asked "why" questions on argparse before coding — building understanding first.
- **What I avoided or half-assed:** Architectural logic of the RAG course, needed to redo the file structure.
- **One thing to do differently next week:** Implement a foundational training period in the morning, to keep reps of the foundations (keep foundations strong, and build up the floor).

-----

### Week of: [12/8/25 - 12/12/25]

**What I Actually Did:**

- ~~with some help with Gemini, was able to build a tokenizer generator, with m length of words and n window size, yield the tokens of length n and then generate the next sequence until we hit the end of the list.~~ *[WORK ASSIGNMENT - MOVED TO SEPARATE NOTES]*
- ~~Implemented some core loop logic in C and started building some structs as well.~~ *[OFF-TRACK DIVERSION - ABANDONED C]*
- ~~Identified C structs and initializers. Got introduced to typedef. Introduced to the basics of a pointer.~~ *[OFF-TRACK DIVERSION - ABANDONED C]*
- ~~Understood the foundations of different major AI concepts, such as Prompt Engineering, XAI, evaluation, inferences, etc.~~ *[WORK ASSIGNMENT - MOVED TO SEPARATE NOTES]*

**Attempted WITHOUT AI:**

- ~~basic loops and structures, typedef, super basic pointer variables in C~~ *[OFF-TRACK - NOT PYTHON]*

**Where I Froze / Needed Help:**

- sliding n-grams, trying to find the right way to iterate over the windows if n was bigger than m (window bigger than length)

**What Clicked:**

- if you iterate, and you want to check a window, a good way to identify if the window is bigger than the length of the tokens is to iterate for range(len(tokens)-n + 1), then, if the window is bigger than the len of tokens, it'll be <0, and the iterator will never yield, thus giving us an empty list (a list in our case which is what we wanted)

**Weekly Reflection:**

- **Hours actually spent learning:** roughly 4-5
- **Solo attempts vs AI-assisted ratio:** most of my learning was purely theoretical, but the two things I did by myself was basically 50/50.
- **Progress toward 3-month goal (honest 1-10):** 3/10, could be better
- **What went well:** I was able to maintain good progression in the week despite my company laptop being down, continuing with boot.dev instead of the DS course. ~~I was able to implement basic C concepts without AI~~ *[Not relevant to Python goal]*
- **What I avoided or half-assed:** The actual learning part I avoided, I need to block more time next week. **Also drifted to C instead of staying focused on Python.**
- **One thing to do differently next week:** ~~Prepare the week fully before I go into the week.~~ **Stay focused on Python only - no C, no diversions. Boot.dev RAG course is the priority.**