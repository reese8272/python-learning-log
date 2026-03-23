Agent Stack

Planner — Reads the current codebase state and produces a structured implementation plan before any code is written. Everything else runs downstream of its output.

Architect — Traverses the repo to evaluate proposed designs against your actual stack and constraints, producing a validated 30k view of the system.

Reviewer — Autonomously reads changed files, checks for correctness, security issues, and stack-specific anti-patterns, then surfaces or fixes findings directly.

Test Writer — Reads the implementation, writes tests following Pareto coverage (20% of tests covering 80-95% of behavior), then runs them to verify.
Debugger — Takes a failing test or traceback, traces through the relevant files, produces a hypothesis, and attempts a fix.

Documenter — Reads completed code and writes docstrings, changelog entries, and README updates to bring documentation to production quality.

Orchestrator — Spawns the above agents as parallel sub-agents via the Task tool and synthesizes their output into a unified result.

CLAUDE.md Composer — Takes the Architect's validated output and generates the initial CLAUDE.md, so it reflects reality rather than assumptions.

Explain It Back — After shipping something, asks you to explain the code, evaluates your explanation, and surfaces genuine comprehension gaps tied to your actual work.

--------

CLAUDE.md Updater Command
markdown# CLAUDE.md Updater

Review the conversation history from this session and determine whether anything 
materially changes what is documented in CLAUDE.md.

Only update if one or more of the following is true:
- A milestone was completed or its status changed
- An architectural decision was made or reversed
- A new hard rule emerged (from a bug, production issue, or explicit decision)
- The stack changed (new tool, removed dependency, new pattern adopted)
- The current task or focus shifted significantly

If nothing in this session meets that bar, respond with:
"No updates warranted." and stop. Do not add, reword, or reformat anything.

If an update is warranted:
- Make the smallest possible change that captures the new truth
- Do not expand sections that don't need expanding
- Do not rewrite things that are still accurate
- Update the "Current State" date and content if the project state changed

Noise is worse than silence. When in doubt, do not update.