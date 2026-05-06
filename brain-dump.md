# Brain Dump

Everything goes here first. Don't filter, don't organize — just get it out. `/organize-brain-dump` will route it when ready.

---

## Habit Checklist

*Check off what hit today. Leave blank what didn't. No judgment — just data.*

- [X] Wake at 6am (7:30 but better than previous days, working towards 6am and this is a win for me)
- [X] Sunlight within 30 min of waking
- [ ] Must-listen playlist
- [X] Morning shake
- [X] Morning deep work block
- [ ] 15-min creativity block
- [X] Gym
- [ ] Daily walk
- [ ] Nonfiction reading
- [ ] Dedicated learning block
- [ ] 3 things grateful for
- [ ] Mental load dump

---

Eden marco langchain course cont.
Decisions / "why this over that" (cont.)
- @tool vs @traceable: completely separate concerns. @tool is LangChain's
  decorator — wraps a function into a LangChain tool object (schema gen,
  result parsing). @traceable is LangSmith's decorator — instruments a
  function for observability. Dropping to raw ollama means dropping @tool
  (you're off LangChain); @traceable stays regardless of provider.
- Ollama schema generation has two modes: (1) manual JSON — you write the
  schema yourself, docstrings irrelevant to ollama; (2) auto-schema — pass
  functions directly as tools, ollama generates the schema, but requires
  Google-style docstrings. Today's code used mode 1.