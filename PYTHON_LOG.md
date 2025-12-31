# Reese's Python Learning Log

**Started:** 2025-12-09  
**Primary Focus (while waiting on company laptop):**

- Boot.dev RAG course (personal device)
- Krish Naik DS Course video review + prep notes (when accessible)

**Primary Focus (when company laptop returns):**

- DS Course hands-on implementation (Krish Naik)
- Boot.dev Python fundamentals
- neetcode problem-solving practice

**What Gets Logged:** Only direct Python coding practice and problem-solving attempts  
**What Doesn't:** Work assignments, theory without practice, language diversions

**3-Month Goal:** Solve 5-6/10 Python problems from scratch in 30-60 min, explaining reasoning throughout

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
| Generators & yield | Can do independently | Built lazy iterators from scratch (map_iter, filter_iter) | 2025-12-13 |
| Higher-order functions | Can use with reference | Implemented compose and pipe functions; understand concept but need more practice | 2025-12-13 |
| argparse CLI basics | Can use with reference | Understand parser hierarchy (ArgumentParser → subparsers → arguments), dest parameter, args namespace | 2025-12-16 |
| Dict transformation & aggregation | Can do independently | Loop + conditionals + dict building, grouping/aggregation with nested dicts | 2025-12-22 |
| DSA (algorithms) | Can implement with reasoning | **LEVELED UP:** DFS from scratch — recursion, cycle prevention with set, base case handling | 2025-12-22 |
| Binary search | Can implement with reasoning | Descending order variant with duplicate handling. Key: `low` converges to insertion point, `<=` ensures convergence check | 2025-12-31 |
| Two-pointer technique | Can implement with reasoning | Closest pair sum on sorted array. Setup: low/high at ends, move based on sum vs target comparison | 2025-12-31 |
| pandas | Exposed | Used in work, need AI help | - |
| numpy | Exposed | Used in work, need AI help | - |
| Data structures (lists, dicts) | Can use | Don't know when to pick which | - |
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

## WEEKLY LOG

*Newest week at top. Add a new section each week.*

-----

### Week of: [12/29/25 - 01/04/26]

**What I Actually Did:**
- **Binary search problem (12/31):** Solved with hints after ~30-40 min of debugging
  - Descending order leaderboard with duplicate handling
  - Learned: `<=` loop condition, comparison direction for descending, why `low` is the answer
- **Two-pointer problem (12/31):** Solved solo in ~10 min, first try, all tests passed
  - Closest pair sum on sorted array
  - New DSA pattern — two pointers converging from ends

**Attempted WITHOUT AI:**
- Initial binary search implementation — had right structure, wrong details
- Two-pointer implementation — 100% solo, clean first attempt

**Where I Froze / Needed Help:**
- Comparison direction (`>=` vs `<=`) for descending order
- Loop condition (`<` vs `<=`) — didn't realize `<` skips edge cases
- Why we return `low` instead of `mid`

**What Clicked:**
- `low` converges to insertion point by design — it tracks "earliest position that could be the answer"
- `while low <= high` ensures we check when pointers meet (single element remaining)
- For descending order: `>=` means "go right" (toward lower scores), `<` means "go left"
- **Two-pointer pattern:** Start at both ends, compare sum to target, move the pointer that helps you get closer. Sorted array = predictable movement.

**Weekly Reflection:**

- **Hours actually spent learning:** [FILL IN END OF WEEK]
- **Solo attempts vs AI-assisted ratio:** [FILL IN END OF WEEK]
- **Progress toward 3-month goal (honest 1-10):** [FILL IN END OF WEEK]
- **What went well:** Pushed through binary search debugging instead of giving up
- **What I avoided or half-assed:** [FILL IN END OF WEEK]
- **One thing to do differently next week:** [FILL IN END OF WEEK]

-----

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

- **Hours actually spent learning:** [FILL IN END OF WEEK]
- **Solo attempts vs AI-assisted ratio:** 3/3 solo so far (100%)
- **Progress toward 3-month goal (honest 1-10):** [FILL IN END OF WEEK]
- **What went well:** Morning warmup system works. Proved fundamentals are solid. First DSA implementation solo.
- **What I avoided or half-assed:** [FILL IN END OF WEEK]
- **One thing to do differently next week:** [FILL IN END OF WEEK]

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

-----

## MONTHLY CHECK-IN

*Newest month at top. Add a new section each month.*

-----

### Month: December 2025

**DS Course Progress:**

- Modules completed: None yet (waiting on company laptop)
- Current module: Watching videos when accessible, taking prep notes

**Boot.dev Progress:**

- RAG course started (12/13/25)
- Functional programming challenge completed solo (10/10 difficulty, 15 minutes)
- argparse CLI basics learned (12/16/25)
- Morning warmup session established (12/22/25) — 3 problems solo
- Binary search (descending order) completed with hints (12/31/25)
- Two-pointer (closest pair sum) completed solo, first try (12/31/25)

**Independence Growth:**

- Problems solved solo this month: 5 (Functional Data Pipeline 10/10, Inventory Status 3/10, Summarize Purchases 5-6/10, DFS Path Search 6/10, Two-Pointer Closest Pair 5/10)
- Problems solved with hints: 2 (argparse CLI 4/10, Binary Search 6/10)
- Hardest thing I did without AI: **Functional Data Pipeline** (10/10) and **DFS Path Search** (6/10 — first algorithm from scratch)

**Am I closer to the 3-month goal?**
YES. Went from freezing on 5/10 problems to crushing 10/10 solo in 15 minutes. Now also implementing algorithms (DFS, binary search, two-pointer) from scratch. Two-pointer was first try, 10 minutes, all passes — stacking DSA patterns fast. The gap is closing fast.

**Am I bouncing between systems or staying focused?**
Was bouncing (C diversion week 1), but corrected course. Now locked on Boot.dev RAG + Python only. Morning warmup system established.

**Honest assessment - what needs to change?**
Keep doing what I did on 12/13 and 12/22 - attempt problems solo first, don't reach for AI, slow down and read carefully, solve one piece at a time. The neurons DO connect when I force them to. Morning warmup reps are working — keep this habit.