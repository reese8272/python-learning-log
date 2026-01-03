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
| Generators & yield | Can do independently | Built lazy iterators from scratch (map_iter, filter_iter) | 2025-12-13 |
| Higher-order functions | Can use with reference | Implemented compose and pipe functions; understand concept but need more practice | 2025-12-13 |
| argparse CLI basics | Can use with reference | Understand parser hierarchy (ArgumentParser → subparsers → arguments), dest parameter, args namespace | 2025-12-16 |
| Dict transformation & aggregation | Can do independently | Loop + conditionals + dict building, grouping/aggregation with nested dicts | 2025-12-22 |
| DSA (algorithms) | Can implement with reasoning | **LEVELED UP:** DFS from scratch — recursion, cycle prevention with set, base case handling | 2025-12-22 |
| Binary search | Can implement with reasoning | Descending order variant with duplicate handling. Key: `low` converges to insertion point, `<=` ensures convergence check | 2025-12-31 |
| Two-pointer technique | Can implement with reasoning | Closest pair sum on sorted array. Setup: low/high at ends, move based on sum vs target comparison | 2025-12-31 |
| Data structures (lists, dicts, sets) | Can do independently | **LEVELED UP:** Instinctively reached for dict for O(n) counting; understand when dict > list for lookups/counting | 2026-01-03 |
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

| Pattern | When to Use | Key Insight |
|---------|-------------|-------------|
| `== threshold` vs `>= threshold` | Single-trigger events (e.g., "first time X reaches N") | `==` fires exactly once when threshold is crossed; `>=` fires every time after, requiring extra tracking to prevent duplicates |
| `dict.get(key, default)` | Counting/accumulating in dicts | Cleaner than `if key not in dict` — one line instead of four |

-----

## CURRENT WEEK

*At end of week: move this section to weekly_log_archive.md and start fresh.*

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

-----

## CURRENT MONTH

*At end of month: move this section to monthly_log_archive.md and start fresh.*

### Month: January 2026

**DS Course Progress:**

- Modules completed: [UPDATE]
- Current module: [UPDATE]

**Boot.dev Progress:**

- Find Suspicious Users completed solo, 2 minutes (01/03/26)

**Independence Growth:**

- Problems solved solo this month: 1 (Find Suspicious Users 6/10)
- Problems solved with hints: 0
- Hardest thing I did without AI: Find Suspicious Users (6/10) — 2 minutes, correct data structure instinct

**Am I closer to the 3-month goal?**
Strong start to January. 6/10 in 2 minutes shows the reps are compounding. Data structure selection is becoming instinctive.

**Am I bouncing between systems or staying focused?**
[UPDATE END OF MONTH]

**Honest assessment - what needs to change?**
[UPDATE END OF MONTH]