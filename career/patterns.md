# Patterns & Mental Models

*Reusable insights extracted from practice. Add a row when a pattern proves reliable across multiple problems.*

-----

### Data Structure Selection
| Pattern | When to Use | Key Insight |
|---------|-------------|-------------|
| Dict for O(n) counting | Need to count occurrences, check membership, or aggregate | Dict lookup is O(1); nested loops scanning a list is O(n²) |
| `dict.get(key, default)` | Counting/accumulating in dicts | `count[x] = count.get(x, 0) + 1` — one line instead of if/else block |
| Set for cycle prevention | Graph traversal, avoiding revisits | O(1) membership check; add before recursing, check before exploring |
| Stack (LIFO) | Undo operations, expression parsing, DFS | Push/pop from top only. O(1) push/pop. Think "last in, first out" — most recent item is always what you grab next. |
| Queue (FIFO) | BFS, task scheduling, order preservation | Enqueue at back, dequeue from front. O(1) enqueue/dequeue (with deque). Think "first in, first out" — process in arrival order. |

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

### Linked Lists & Iterators
| Pattern | When to Use | Key Insight |
|---------|-------------|-------------|
| `__iter__` as generator | Making a linked list (or any custom collection) iterable with `for` loops | Define `__iter__` using `yield` to walk nodes. This makes the class a generator-based iterator — `for item in my_list` just works. |
| Using own iterator inside the class | Need to loop over the collection's elements within another method of the same class | Use `for item in self` — calling `self` in a `for` loop triggers `__iter__` on the current instance. The class IS the iterable, so `self` is how you access it from inside. |

### Function Patterns
| Pattern | When to Use | Key Insight |
|---------|-------------|-------------|
| Decorator structure | Timing, logging, auth wrappers | `def decorator(func): def wrapper(*args, **kwargs): ... return wrapper` |
| Memoization | Expensive recursive calls (Fibonacci, etc.) | Check cache first, compute + store if missing, return cached |
| Currying | Partial application, config builders | Each function returns the next function until all args collected |
| Mutable default for state | Function call counting, accumulators | `def f(x, state=[0])` — list persists across calls |
| Function composition | Chaining transformations | `f(g(x))` — inner closure captures outer functions |

### Class Design Patterns
| Pattern | When to Use | Key Insight |
|---------|-------------|-------------|
| `@property` (encapsulation) | Control how class attributes are read/written; enforce validation rules | Store real value in `_variable`, expose via property method. Without setter = read-only. With setter = enforce rules before allowing change. |
| `_variable` convention | Any attribute that should be accessed via property, not directly | Single underscore = "internal, use the interface." Convention only — not enforced by Python — but widely respected. |
| `@staticmethod` | Utility function logically related to a class but needing no instance or class state | Can be called on the class directly without instantiating. When multiple related classes exist (USD/GBP/YEN), grouping utilities with their class beats a flat module. |
| `@classmethod` as alternative constructor | Different way to instantiate without being restricted to `__init__` signature | Receives `cls` instead of `self`. Use `cls(...)` not `ClassName(...)` — works correctly with inheritance; subclass gets back an instance of *itself*, not the parent. |
| `@cache` (automated memoization) | Expensive recursive functions; any pure function called repeatedly with same inputs | Same as manual dict memoization — stores result on first call, returns it on repeat calls. Arguments must be hashable. Changes recursive from exponential to linear time. |
| `@dataclass` (data container) | Class whose only job is holding structured data | Auto-generates `__init__`, `__repr__`, `__eq__`. Signals "data container, not behavior." Two instances with same field values are equal (Value Object pattern). |
| `@dataclass` vs Pydantic `BaseModel` | Choosing between internal data holders and boundary validators | `@dataclass`: no runtime type enforcement, no validation, no serialization. Pydantic: enforces types at runtime, validates, serializes. Use dataclass for internal containers you control. Use Pydantic when data crosses a boundary (API input, agent state, external data) — bad types can silently break things downstream. |

### Sorting Algorithms
| Pattern | When to Use | Key Insight |
|---------|-------------|-------------|
| Bubble sort | Simple/educational; nearly sorted data | Nested loops, swap adjacent. O(n²) time, O(1) space. Early exit optimization if no swaps in a pass. |
| Insertion sort | Small datasets, nearly sorted data | Build sorted portion left-to-right, shift elements to insert. O(n²) time, O(1) space. Best case O(n) on sorted input. |
| Merge sort | Need guaranteed O(n log n), stability matters | Divide in half, recurse, merge sorted halves. O(n log n) time, O(n) space. The merge step is the hard part: two pointers comparing heads of sorted subarrays. |
| Quick sort | General-purpose, good average case | Pick pivot, partition (smaller left, larger right), recurse on halves. O(n log n) avg / O(n²) worst, O(log n) space. Partition logic is the tricky part. |

### Big O Quick Reference
| Pattern | When to Use | Key Insight |
|---------|-------------|-------------|
| O(n²) vs O(n log n) | Choosing a sorting approach | Bubble/insertion are simple but slow on large data. Merge/quick scale — the "log n" comes from halving the problem each step. |
| Space complexity tradeoff | Merge sort vs quick sort | Merge needs O(n) extra space for merging. Quick sorts in-place with O(log n) stack space. Trade memory for guaranteed performance. |

### Sliding Window
| Pattern | When to Use | Key Insight |
|---------|-------------|-------------|
| Window range formula | Fixed-size window over sequence | `range(len(seq) - window_size + 1)` — auto-returns empty if window > sequence |

### asyncio & Concurrency
| Pattern | When to Use | Key Insight |
|---------|-------------|-------------|
| `asyncio` for I/O-bound work | Network calls, DB queries, LLM API calls — anything where the CPU sits idle waiting | Not parallelism — cooperative concurrency. The event loop exploits the gaps between `await` points. Two things never run at the exact same time, but wait times overlap. |
| `asyncio.gather` | Fire multiple async tasks simultaneously | All wait periods overlap instead of stacking. 5 x 2s calls = ~2s total, not ~10s. |
| Blocking the event loop | Calling a synchronous blocking function inside async code without `await` | Silent bug — no error, just destroys concurrency. `time.sleep(3)` inside a coroutine freezes everything. Always ask: *"What is the event loop actually doing at this line?"* |
| `run_in_executor` | Must call a blocking sync function inside async code | Ships the blocking call to a thread pool, frees the event loop. `await loop.run_in_executor(None, fn)` — `None` = default ThreadPoolExecutor. |
| asyncio vs threading vs multiprocessing | Choosing the right concurrency tool | I/O-bound + async → `asyncio`. Blocking I/O you can't rewrite → `threading`. CPU-bound → `multiprocessing`. |

### LLM System Design
| Pattern | When to Use | Key Insight |
|---------|-------------|-------------|
| Pre-hook (LLM middleware) | Before the LLM call — security checks, prompt injection detection, logging, input validation | Can short-circuit the call entirely if input fails checks. Acts as a gate. Think: input validation at the boundary. |
| Post-hook (LLM middleware) | After the LLM response — scan for credentials, malicious output, policy violations, logging | Runs before the response is returned to the caller. Think: output sanitization at the boundary. |
| Evaluate before you delegate | Before trusting an LLM to own a task | Run the task yourself (or with close oversight) first. Then use your output as a benchmark — have the LLM do it and compare. Refine the prompt until the outputs match on the things that matter. |
| Output evaluation via comparison | Validating LLM prompt quality | Run similar prompts, check that all key information surfaces across outputs. If key info is missing, refine the prompt. A report you've already produced is a perfect benchmark. |

### Agentic System Design
| Pattern | When to Use | Key Insight |
|---------|-------------|-------------|
| Agent + tool use | LLM needs to take actions in the world (search, run code, call APIs) | The LLM decides *when* to call a tool; the tool does the actual work. Keep tools small and single-purpose — easier to reason about and debug. |
| LangChain for orchestration | Building chains of LLM calls, prompt templates, tool use, memory | Abstracts the plumbing. Use it when you need reusable components. Don't use it when a simple direct API call is cleaner. |
| LangGraph for stateful agents | Multi-step agents that need to loop, branch, or revisit steps | Models agent execution as a graph — nodes are steps, edges are transitions. Use when agent behavior is too complex for a linear chain. |
| LangSmith for observability | Debugging and evaluating LLM pipelines in production | Traces every LLM call, tool invocation, and token. Essential for knowing *why* an agent did what it did. |
| MCP (Model Context Protocol) | Standardizing how LLMs connect to external tools and data sources | Separates the tool interface from the model. Any MCP-compliant client can use any MCP-compliant server — plug and play. |

### Production Infrastructure
| Pattern | When to Use | Key Insight |
|---------|-------------|-------------|
| Docker container | Packaging an app so it runs the same everywhere | Bundles the app + its dependencies + its environment into one image. Eliminates "works on my machine." Think: a portable, self-contained box. |
| CI/CD pipeline | Automating test → build → deploy on every code push | Continuous Integration: automatically test and build. Continuous Deployment: automatically ship if tests pass. Removes manual deployment steps and catches breaks before they reach production. |
| GitHub Actions trigger | Automating workflows in response to git events | Runs on push, PR, schedule, etc. Define jobs in `.github/workflows/`. Each job = a series of steps that run in sequence. |

### Security
| Pattern | When to Use | Key Insight |
|---------|-------------|-------------|
| Authentication vs Authorization | Any system with users and protected resources | AuthN = "who are you?" (identity). AuthZ = "what are you allowed to do?" (permissions). AuthN always comes first — you can't authorize an unknown identity. |
| Credential management | Any secrets (API keys, DB passwords, tokens) in code or pipelines | Never hardcode credentials. Use environment variables locally, secrets managers (AWS Secrets Manager, GitHub Secrets) in production. Leaked creds are the #1 avoidable breach vector. |
| Prompt injection defense | Any LLM app accepting user input | User input that manipulates the prompt to hijack the LLM's behavior. Mitigate with: input validation (pre-hook), privilege separation (LLM shouldn't have access to what it doesn't need), output validation (post-hook). |

### Cloud — AWS for AI
| Pattern | When to Use | Key Insight |
|---------|-------------|-------------|
| *(Growing — add as learned)* | | |

### Problem-Solving Meta-Strategies
| Pattern | When to Use | Key Insight |
|---------|-------------|-------------|
| Solve incrementally | Complex multi-part problems | Break into pieces, solve one function at a time, test as you go |
| Read twice, code once | Before starting any problem | Almost missed "right-to-left" in compose — slow down, catch details before writing |
| Bare `return` = `None` | Any Python function returning a value | If your base case IS a value, you must return that value explicitly. `return` by itself always returns `None`. |
