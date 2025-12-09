# Python Learning Log

Last Updated: 2025-12-08

---

## 1. CURRENT FOCUS

### Week of 2025-12-08

**Platform:** Boot.dev + Coursera NLP & DS + neetcode planning

**Topic:** Course structure planning and AI dependency awareness

**Time Invested:** Planning phase

**What I Built/Practiced:**
- Structured weekly learning schedule (Mon/Tue: Boot.dev, Wed/Thurs: Coursera, Fri: neetcode integration)
- Identified integration pattern: using Friday for system design reflection on Mon-Thurs work

**What Clicked:**
- Recognition that context-switching between platforms daily is inefficient
- System design should be a lens for reviewing work, not isolated study
- Need to capture "architectural questions" during learning sessions for Friday review

**What's Still Fuzzy:**
- How to effectively log daily without overhead
- Best way to capture struggles in real-time vs retrospectively

**Architectural Question This Raises:**
- How do I structure logs themselves for queryability by AI assistants?
- What's the minimum viable logging to get maximum AI assistance benefit?

---

## 2. KNOWLEDGE INVENTORY

### Langchain and Langgraph

**Status:** Comfortable

**Last Practiced:** 2025-12-08 (ongoing in work projects)

**Can Do:**
- Build agent structures using `create_react_agent()` functions
- Construct langgraph agents and connections between agents
- Add tools to agents and create use cases
- Work with agent structures at intermediate level

**Still Working On:**
- Advanced patterns and optimizations
- Edge cases in multi-agent coordination
- Performance tuning for production

**Used In:**
- Work projects involving LLM agents and tool integration

**Skill Level:** 5/10 (very familiar, but still a lot to learn)

---

### Model Context Protocol (MCP)

**Status:** Learning

**Last Practiced:** 2025-12-08 (recent experimentation)

**Can Do:**
- Instantiate local MCP servers using npx
- Run servers as tools for agents
- Set up fileservermcp for file system access (read, write, modify files/directories in specific folders)

**Still Working On:**
- Creating custom MCP servers
- Understanding full protocol capabilities
- Integration patterns beyond basic examples

**Used In:**
- Local experimentation with LLM file system access

**Skill Level:** 3/10

---

### Python Syntax (Basic & Intermediate)

**Status:** Solid

**Last Practiced:** Daily

**Can Do:**
- All basic syntax (for loops, while loops, conditionals, etc.)
- Classes, functions, and package structures
- Understand `__init__` in packages
- Work with common packages: numpy, pandas, os, and misc packages
- Understand their general use cases

**Still Working On:**
- Advanced class patterns and metaclasses
- Advanced package architecture
- More complex numpy/pandas operations

**Used In:**
- Daily work and all learning platforms

**Skill Level:** 7.5/10 (on Beginner/Intermediate level, not Advanced)

---

### Data Structures & Algorithms (Basic)

**Status:** Comfortable

**Last Practiced:** 2025-12-08 (ongoing in Boot.dev)

**Can Do:**
- Understand concepts: stack, queue, lists
- Know what binary trees, binary search, linked lists are and basic use cases
- Understand Big O notation and optimization importance (keeping close to O(1))
- Recognize when operations can become exponential if not handled properly

**Still Working On:**
- Advanced structures: A*, Dijkstra's, Binary Search Trees (BST)
- Knowing WHEN to implement specific structures
- Hard-coding implementations from memory
- Pattern recognition for which structure fits which problem

**Used In:**
- Boot.dev exercises
- Work problems occasionally

---

### Recursion & Memoization

**Status:** Comfortable

**Last Practiced:** 2025-12-08 (recent breakthrough)

**Can Do:**
- Break problems down to base cases
- Address problems at smaller scale working toward base case
- Implement memoization with dictionaries/lists
- Understand space-time tradeoffs
- Know when recursion depth becomes a problem (RecursionError)
- Understand LRU cache strategy and cache thrashing

**Key Understanding:**
- Recursion = the calculation process (breaking down the problem)
- Memoization = storing results (the "Post-it note") to avoid recalculation
- Transforms brute force to lookup: saves Time (CPU), costs Space (Memory)
- When cache is too small for working set → cache thrashing → 0% hit rate
- When recursion depth exceeds limits (~1000 in Python) → switch to iteration

**Still Working On:**
- More complex recursive patterns
- Optimal cache sizing decisions
- When to choose recursion vs iteration upfront

**Used In:**
- Boot.dev grid traversal problems
- Path-finding exercises

---

### Python Best Practices

**Status:** Comfortable

**Last Practiced:** 2025-12-08

**Can Do:**
- Avoid mutable defaults in functions
- Use `None` as default, then initialize inside function
- Understand why `def append(item, target=[])` is problematic (same list reused)
- Know that `None` is a singleton

**Key Pattern:**
```python
def append(item, target=None):
    if target is None:
        target = []
    # ... rest of function
```

**Used In:**
- All Python code writing

---

## 3. ACTIVE STRUGGLES

### Advanced Data Structures - When to Use Which - Added: 2025-12-08

**Context:**
Encountered in Boot.dev and work projects where optimal structure choice matters

**The Problem:**
I know OF advanced structures (A*, Dijkstra's, BST) but they aren't "hard coded in my brain." When I encounter a problem that needs them:
- I'm not sure I'd recognize it needs that specific structure
- I wouldn't know how to implement it from scratch
- I can't distinguish when to pick one over another

**What I've Tried:**
- Learning about them conceptually
- Understanding what they do
- Haven't practiced implementing them enough to internalize

**Current Understanding:**
- Understand the concepts and general use cases
- Missing: pattern recognition for real problems
- Missing: muscle memory for implementation
- Missing: decision framework for structure selection

---

### System Design Fundamentals - Added: 2025-12-08

**Context:**
Work situations where system design knowledge would be directly beneficial

**The Problem:**
Complete gap in knowledge:
- Don't know what system designs are
- Don't know how to pick appropriate patterns
- Don't know when to use them
- Missing fundamental understanding of the field

**What I've Tried:**
- Recognized the need
- Haven't started learning yet

**Current Understanding:**
- Zero baseline
- Need structured introduction to field
- Should be addressed through neetcode system design section
- Will use Friday integration sessions to apply to Mon-Thurs learning

---

### AI Dependency - Added: 2025-12-08

**Context:**
Learning coding in the age of AI has created problematic reliance

**The Problem:**
I rely on AI WAY too much:
- Don't connect dots well between problem and solution
- Struggle to solve relatively easy problems independently
- Pattern: Ask AI what I want → Give constraints → Might know a few structures → AI solves it
- Not building independent problem-solving muscles

**What I've Tried:**
- Recognition of the problem
- Awareness that this stems from learning in AI era

**Current Understanding:**
- This is blocking real growth
- Need accountability mechanisms
- Need to force more independent attempts before AI assistance
- Theoretical understanding is strong; implementation without AI is weak

**Potential Solutions to Try:**
- Time-box independent attempts before AI help
- Use AI in Socratic mode (questions, not answers)
- Track problems solved independently vs with AI help
- Challenge mode: solve problem, then check AI solution
- Build up from easier problems where AI isn't needed

---

## 4. INTEGRATION LOG

### 2025-12-08

**Concepts Reviewed This Week:**
- Learning structure and schedule planning
- AI dependency recognition
- Log architecture for AI assistant integration

**System Design Thinking:**
- How to structure learning logs for queryability
- Balancing detail vs maintenance overhead
- Integration patterns between three learning platforms

**Connections Made:**
- Boot.dev (infrastructure) + Coursera (data/ML) + neetcode (architecture) = complete production system thinking
- Friday system design reviews can tie together disparate concepts from earlier in week
- Learning logs themselves are a system design problem

**Questions for Next Week:**
- What's the right logging frequency to maintain without overhead?
- How to capture architectural questions in the moment during learning?
- Best practices for version controlling learning progress?

---

## 5. PLATFORM-SPECIFIC NOTES

### Boot.dev Progress

**Current Status:** Active user, Python course with Go language path

**Focus Areas:**
- Backend development fundamentals
- Python → C → Go → Kubernetes → Git → Docker progression
- DSA integrated into curriculum
- Recently completed: RAG architecture module

**Key Strengths from Platform:**
- Gamification keeps engagement high
- Integrated learning path for backend dev
- Has "training grounds" feature for practice

**What I Need from Boot.dev:**
- Foundation in backend thinking
- DSA practice in context
- Infrastructure concepts

---

### Coursera NLP & DS Progress

**Current Status:** Enrolled in Krish's NLP and Data Science course

**Focus Areas:**
- Data science libraries: numpy, pandas
- Statistics and probability
- ML techniques: K-nearest neighbors, etc.
- NLP techniques and sentence transformers
- Basic → Intermediate → Advanced Python coverage

**Key Strengths from Platform:**
- In-depth coverage of data science ecosystem
- Strong ML/NLP focus (my target niche)
- Comprehensive library training

**What I Need from Coursera:**
- Path toward data science/ML/AI specialization
- Production-level data manipulation skills
- NLP implementation knowledge

---

### neetcode Progress

**Current Status:** Planning to use for system design integration

**Focus Areas:**
- DSA (overlaps with Boot.dev, good for reiteration)
- System design (unique to this platform, critical gap)
- Pattern recognition for implementation

**Key Strengths from Platform:**
- System design curriculum
- Real interview/production patterns
- Structured problem sets

**What I Need from neetcode:**
- System design fundamentals
- Architectural thinking patterns
- DSA reinforcement and pattern recognition

**Friday Review Strategy:**
- Review Mon-Thurs work through system design lens
- Use neetcode frameworks to analyze scalability
- Identify patterns in what I built
- Document architectural decisions and tradeoffs

---

## LEARNING METHODOLOGY NOTES

### Current Weekly Structure (As of 2025-12-08)

**Work Hours:** 9am - 5:30pm
- Flexible time: 4-5 hours for personal/learning during work day
- Strategy: Integrate learning directly with work tasks

**Monday/Tuesday:** Boot.dev
- Full day focus on backend fundamentals
- Build something concrete
- Note architectural questions for Friday

**Wednesday/Thursday:** Coursera NLP & DS
- Full day focus on data science/ML
- Practice with real data manipulation
- Note architectural questions for Friday

**Friday:** neetcode + Integration
- System design lens on week's work
- Review architectural questions from Mon-Thurs
- Tie together concepts across platforms
- NOT a separate study day, but a reflection/integration day

**Post-5:15pm:** Kids home, minimal learning time
- Focus on family
- Learning happens during work hours

### Integration Philosophy

Learning isn't separate from work - it's the methodology:
- Hit a data manipulation task at work → Coursera moment
- System design question → neetcode moment
- Backend architecture decision → Boot.dev moment

Shift from "completing courses" to "solving problems with these resources"

### Anti-Patterns to Avoid

- ❌ 30-30-30 minute rotations (context switching hell)
- ❌ Treating learning as separate from work
- ❌ Trying to "complete" platforms linearly
- ❌ Logging so detailed it becomes a chore
- ❌ Using AI before attempting independently

### Success Patterns

- ✅ Full-day focus on one platform
- ✅ Learning through application to real problems
- ✅ Friday integration to tie concepts together
- ✅ Minimal but consistent logging
- ✅ Forcing independent attempts before AI help

---

## PERSONAL CONTEXT

**Work:** Junior Python developer at company
- Balance between company work and skill development during work hours
- Applied to production-level projects needing system design knowledge

**Education:** Social work student (SOWK 311)
- Balancing technical career with academic pursuits
- Diverse interests: technology and human services

**Family:** Kids home by 5:15pm daily
- Learning window: primarily during work hours
- Need efficient use of 4-5 flexible hours daily

**Learning Goals:**
- Path toward data science/ML/AI specialization
- Break AI dependency for coding
- Build production-level system design knowledge
- Strengthen advanced DSA implementation

