# Reese’s Python Learning Log

**Started:** 2025-12-09  
**Primary Focus (while waiting on company laptop):**

- Boot.dev RAG course (personal device)
- Krish Naik DS Course video review + prep notes (when accessible)

**Primary Focus (when company laptop returns):**

- DS Course hands-on implementation (Krish Naik)
- Boot.dev Python fundamentals
- neetcode problem-solving practice

**What Gets Logged:** Only direct Python coding practice and problem-solving attempts  
**What Doesn’t:** Work assignments, theory without practice, language diversions

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
- I cannot build from scratch independently - I freeze at “thought to paper”
- Everything I’ve built has been with AI or external help
- The gap: neurons don’t connect because AI fills in before I have to think

**What I’ve Been Exposed To (with help):**

- Multi-agent software team (dev, tester, security lead, team lead)
- MCP servers for file/directory read-write
- Customer data pipelines for insights on repeat callers and workflows

-----

## WEEKLY SCHEDULE

*Established: 2025-12-21*

**Philosophy:** Weekdays for lessons and guided learning. Weekends for deep work and harder challenges.

|Day|Learning Focus              |Time           |Notes                                    |
|---|----------------------------|---------------|-----------------------------------------|
|Mon|Boot.dev                    |~2-3 hrs (work)|Lessons, concepts, guided exercises      |
|Tue|Boot.dev                    |~2-3 hrs (work)|Lessons, concepts, guided exercises      |
|Wed|Krish Naik NLP/DS course    |~2-3 hrs (work)|Lessons, concepts, guided exercises      |
|Thu|Krish Naik NLP/DS course    |~2-3 hrs (work)|Lessons, concepts, guided exercises      |
|Fri|Neetcode + weekly reflection|~2-3 hrs (work)|Problem-solving practice, update this log|
|Sat|Boot.dev (deep work)        |6-8 AM (2 hrs) |Harder challenges, uninterrupted thinking|
|Sun|NLP course (deep work)      |6-8 AM (2 hrs) |Harder challenges, uninterrupted thinking|

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

|Skill                                    |Level                 |Notes                                                                                                             |Last Practiced|
|-----------------------------------------|----------------------|------------------------------------------------------------------------------------------------------------------|--------------|
|Python basics (loops, functions, classes)|Can do independently  |**LEVELED UP:** Implemented functional programming patterns solo (generators, higher-order functions, composition)|2025-12-13    |
|Generators & yield                       |Can do independently  |Built lazy iterators from scratch (map_iter, filter_iter)                                                         |2025-12-13    |
|Higher-order functions                   |Can use with reference|Implemented compose and pipe functions; understand concept but need more practice                                 |2025-12-13    |
|argparse CLI basics                      |Can use with reference|Understand parser hierarchy (ArgumentParser → subparsers → arguments), dest parameter, args namespace             |2025-12-16    |
|pandas                                   |Exposed               |Used in work, need AI help                                                                                        |-             |
|numpy                                    |Exposed               |Used in work, need AI help                                                                                        |-             |
|Data structures (lists, dicts)           |Can use               |Don’t know when to pick which                                                                                     |-             |
|DSA (algorithms)                         |Concept only          |Can’t implement                                                                                                   |-             |
|Stats/Probability                        |Gap                   |Need to learn                                                                                                     |-             |
|NLP techniques                           |Gap                   |Target skill from DS Course                                                                                       |-             |

**Level definitions:**

- **Gap:** Haven’t learned yet
- **Exposed:** Seen it, used it with help, can’t do it alone
- **Can use with reference:** Can do it if I look things up
- **Can do independently:** No AI, no docs, I got this

-----

## INDEPENDENCE TRACKER

*The whole point: proving you can do things WITHOUT AI*

|Date    |Problem/Task                                                       |Difficulty|Solo Attempt Time|Result           |Notes                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|--------|-------------------------------------------------------------------|----------|-----------------|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|12/09/25|sliding n-grams window                                             |5/10      |~15 minutes      |Needed AI        |was sort of unsure of the question, and then gemini helped me understand that in a window problem, you can do for range(len(what you’re sliding over) - <window size> + 1 to catch the last bit of the window), because then if the window size is larger than the thing were sliding, it’ll auto detect it and return nothing (empty list or empty string more likely)                                                                                                           |
|12/13/25|**Functional Data Pipeline (map_iter, filter_iter, compose, pipe)**|**10/10** |~15 minutes      |**Solved solo**  |**BREAKTHROUGH:** Built lazy iterators with yield, implemented right-to-left function composition, threaded values through pipe. First 10/10 problem solved completely independently. Strategy: broke problem into pieces, tackled one function at a time. Almost missed “right-to-left” detail in compose but caught it. Minor edge case bug (returned tuple instead of function when len==1) but passed all tests. Key learning: slow down, read carefully, solve incrementally.|
|12/16/25|argparse CLI implementation                                        |4/10      |~5 minutes       |Solved with hints|Needed walkthrough of boilerplate to understand the parser hierarchy, but wrote the implementation (`print(f"Searching for: {args.query}")`) solo. Asked good “why” questions before coding — understood the system instead of just copy/pasting.                                                                                                                                                                                                                                 |

**Result options:** Solved solo, Solved with hints, Needed AI, Gave up

-----

## ACTIVE STRUGGLES

*What’s blocking you RIGHT NOW. When resolved, delete and update Skills Tracker.*

**No active struggles logged.** Update as they come up during RAG course.

-----

## WEEKLY LOG

*Newest week at top. Add a new section each week.*

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

- **Hours actually spent learning:** [FILL IN END OF WEEK]
- **Solo attempts vs AI-assisted ratio:** [FILL IN END OF WEEK]
- **Progress toward 3-month goal (honest 1-10):** 8/10 - Crushed a 10/10 problem solo in 15 minutes, exactly what the goal is about
- **What went well:** Stayed focused on Python (Boot.dev RAG course), didn’t drift to C or theory. Proved I can solve complex problems independently. Asked “why” questions on argparse before coding — building understanding first.
- **What I avoided or half-assed:** [FILL IN END OF WEEK]
- **One thing to do differently next week:** [FILL IN END OF WEEK]

-----

### Week of: [12/8/25 - 12/12/25]

**What I Actually Did:**

- ~with some help with Gemini, was able to build a tokenizer generator, with m length of words and n window size, yield the tokens of length n and then generate the next sequence until we hit the end of the list.~ *[WORK ASSIGNMENT - MOVED TO SEPARATE NOTES]*
- ~Implemented some core loop logic in C and started building some structs as well.~ *[OFF-TRACK DIVERSION - ABANDONED C]*
- ~Identified C structs and initializers. Got introduced to typedef. Introduced to the basics of a pointer.~ *[OFF-TRACK DIVERSION - ABANDONED C]*
- ~Understood the foundations of different major AI concepts, such as Prompt Engineering, XAI, evaluation, inferences, etc.~ *[WORK ASSIGNMENT - MOVED TO SEPARATE NOTES]*

**Attempted WITHOUT AI:**

- ~basic loops and structures, typedef, super basic pointer variables in C~ *[OFF-TRACK - NOT PYTHON]*

**Where I Froze / Needed Help:**

- sliding n-grams, trying to find the right way to iterate over the windows if n was bigger than m (window bigger than length)

**What Clicked:**

- if you iterate, and you want to check a window, a good way to identify if the window is bigger than the length of the tokens is to iterate for range(len(tokens)-n + 1), then, if the window is bigger than the len of tokens, it’ll be <0, and the iterator will never yield, thus giving us an empty list (a list in our case which is what we wanted)

**Weekly Reflection:**

- **Hours actually spent learning:** roughly 4-5
- **Solo attempts vs AI-assisted ratio:** most of my learning was purely theoretical, but the two things I did by myself was basically 50/50.
- **Progress toward 3-month goal (honest 1-10):** 3/10, could be better
- **What went well:** I was able to maintain good progression in the week despite my company laptop being down, continuing with boot.dev instead of the DS course. ~I was able to implement basic C concepts without AI~ *[Not relevant to Python goal]*
- **What I avoided or half-assed:** The actual learning part I avoided, I need to block more time next week. **Also drifted to C instead of staying focused on Python.**
- **One thing to do differently next week:** ~Prepare the week fully before I go into the week.~ **Stay focused on Python only - no C, no diversions. Boot.dev RAG course is the priority.**

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

**Independence Growth:**

- Problems solved solo this month: 1 (Functional Data Pipeline - 10/10)
- Problems solved with hints: 1 (argparse CLI - 4/10)
- Hardest thing I did without AI: **Functional Data Pipeline** - generators, higher-order functions, composition - all from scratch in 15 minutes

**Am I closer to the 3-month goal?**
YES. Went from freezing on 5/10 problems to crushing 10/10 solo in 15 minutes. The gap is closing fast.

**Am I bouncing between systems or staying focused?**
Was bouncing (C diversion week 1), but corrected course. Now locked on Boot.dev RAG + Python only.

**Honest assessment - what needs to change?**
Keep doing what I did on 12/13 - attempt problems solo first, don’t reach for AI, slow down and read carefully, solve one piece at a time. The neurons DO connect when I force them to.