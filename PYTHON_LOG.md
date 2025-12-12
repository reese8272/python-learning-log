# Reese's Python Learning Log

**Started:** 2025-12-09  
**Primary Focus:** DS Course (Krish Naik - Complete Data Science, ML, DL, NLP Bootcamp)  
**3-Month Goal:** Solve 5-6/10 Python problems from scratch in 30-60 min, explaining reasoning throughout

---

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

---

## SKILLS TRACKER

*Update when something genuinely levels up. Be honest.*

| Skill | Level | Notes | Last Practiced |
|-------|-------|-------|----------------|
| Python basics (loops, functions, classes) | Can use with reference | Cannot write from scratch confidently | 2025-12-09 |
| pandas | Exposed | Used in work, need AI help | - |
| numpy | Exposed | Used in work, need AI help | - |
| Data structures (lists, dicts) | Can use | Don't know when to pick which | - |
| DSA (algorithms) | Concept only | Can't implement | - |
| Stats/Probability | Gap | Need to learn | - |
| NLP techniques | Gap | Target skill from DS Course | - |
| C Basics | Can do independently | learning super basic C to understand lower level code | 2025-12-11 |

**Level definitions:**
- **Gap:** Haven't learned yet
- **Exposed:** Seen it, used it with help, can't do it alone
- **Can use with reference:** Can do it if I look things up
- **Can do independently:** No AI, no docs, I got this

---

## INDEPENDENCE TRACKER

*The whole point: proving you can do things WITHOUT AI*

| Date | Problem/Task | Difficulty | Solo Attempt Time | Result | Notes |
|------|--------------|------------|-------------------|--------|-------|
| 12/09/25 | sliding n-grams window | 5/10 | ~15 minutes | Needed AI | was sort of unsure of the question, and then gemini helped me understand that in a window problem, you can do for range(len(what you're sliding over) - <window size> + 1 to catch the last bit of the window), because then if the window size is larger than the thing were sliding, it'll auto detect it and return nothing (empty list or empty string more likely) |
| 12/09/25 | basic loops in C | 3/10 | ~15 minutes | Solved solo | Super basic stuff with C so far, and it's my second passing, but I was able to solve everything 100% by myself (which is nice bause it's a more hardware language and it's implementing the basics without ANY help)
| 12/11/25 | Implementing structs and initializers, getting introduced to pointers | 2/10 | ~30 minutes | Solved solo | learning some really cool basics with C, and getting down structs, types, typedef, and the introduction to pointers.


**Result options:** Solved solo, Solved with hints, Needed AI, Gave up

---

## ACTIVE STRUGGLES

*What's blocking you RIGHT NOW. When resolved, delete and update Skills Tracker.*

### [Struggle Name] - Added: [DATE]

**What's happening:**


**What I've tried:**


**Current theory:**


---

## WEEKLY LOG

*Newest week at top. Add a new section each week.*

---

### Week of: [12/8/25 - 12/12/25]

**What I Actually Did:**
- with some help with Gemini, was able to build a tokenizer generator, with m length of words and n window size, yield the tokens of length n and then generate the next sequence until we hit the end of the list.
- Implemented some core loop logic in C and started building some structs as well.
- Identified C structs and initializers. Got introduced to typedef. Introduced to the basics of a pointer.

**Attempted WITHOUT AI:**
- basic loops and structures, typedef, super basic pointer variables in C

**Where I Froze / Needed Help:**
- sliding n-grams, trying to find the right way to iterate over the windows if n was bigger than m (window bigger than length)

**What Clicked:**
- if you iterate, and you want to check a window, a good way to identify if the window is bigger than the length of the tokens is to iterate for range(len(tokens)-n + 1), then, if the window is bigger than the len of tokens, it'll be <0, and the iterator will never yield, thus giving us an empty list (a list in our case which is what we wanted)
- second go around with pointer and struct logic. Lot cleaner the second go around and taking notes.

**Weekly Reflection:**

- **Hours actually spent learning:** 
- **Solo attempts vs AI-assisted ratio:** 
- **Progress toward 3-month goal (honest 1-10):**
- **What went well:** I was able to maintain good progression in the week despite my company laptop being down, continuing with boot.dev instead of the DS course. I was able to implement basic C concepts without AI
- **What I avoided or half-assed:**
- **One thing to do differently next week:**

---

## MONTHLY CHECK-IN

*Newest month at top. Add a new section each month.*

---

### Month: [MONTH YEAR]

**DS Course Progress:**
- Modules completed:
- Current module:

**Independence Growth:**
- Problems solved solo this month:
- Hardest thing I did without AI:

**Am I closer to the 3-month goal?**


**Am I bouncing between systems or staying focused?**


**Honest assessment - what needs to change?**