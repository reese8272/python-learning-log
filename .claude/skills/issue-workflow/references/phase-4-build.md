# Phase 4 - Build: quality is enforced while building

Phase 7 is a judge, not a bug hunt, because the bugs get caught and fixed here, at the moment they appear.

## Build discipline

- Follow the project's `CLAUDE.md` coding principles and the decision logs' standing rules.
- Write tests alongside the code, not after. For a bug fix write the failing test first and watch it fail.
- Map every acceptance criterion to at least one test or one named manual check; write the map in the run record.
- Test to the Pareto rule: the core happy path per module, the load-bearing boundary values, and error handling at
  system boundaries. Not every permutation, not implementation details, not what the language already guarantees.
- Pyramid, not crab: many unit tests, fewer integration tests, fewest end-to-end. A flaky test is quarantined in the
  same PR with a follow-up note, never deleted silently and never left red.
- Learn mode: run the Phase 4 loop as `/tdd` describes it (red, green, refactor; one behaviour per loop).

## The per-unit checklist (binary, with evidence)

After every meaningful unit of work (a function, a module, a commit-sized chunk, never more), copy this list into
the run record under a `### Unit N` heading and tick each item **with an evidence marker**: `cmd="..." exit=0` for
anything a tool checked, `file=path:line` for anything you read, `note="..."` only for reasoning. Tools first,
judgment second: run the project's formatter, linter, type checker, and the relevant tests at every unit and read
the actual output.

**Syntax and types**
- [ ] formatter and linter clean on the changed files
- [ ] type checker clean (or the project has none; say so)

**Bugs and logic**
- [ ] the new or changed tests fail before the change and pass after it (bug fixes), or cover each AC (features)
- [ ] boundaries checked by hand: empty input, max length, off-by-one at range edges, None/null, the unauthenticated caller
- [ ] no inverted condition or unreachable branch (read the diff once more, slowly)

**Smells**
- [ ] no logic duplicated from an existing function; the closest sibling pattern was reused
- [ ] no magic values; no misleading names; functions stay readable (roughly under 30 lines)
- [ ] no dead code, no commented-out blocks, no TODO without an owner, no debug prints

**Compliance**
- [ ] follows the project's own conventions (the pattern the Explore pass named) and the decision logs' rules
- [ ] obeys `text_rules`; new config values are in the committed env example with a description

**Performance**
- [ ] no per-row query in a loop; list endpoints that touch a new relation carry a query-count assertion
- [ ] no unbounded loop over user-controlled input; no client or connection constructed per request

**Formatting**
- [ ] matches the project formatter's output; no mixed styles in the diff

**Security**
- [ ] boundary input is validated with a typed schema or serializer; string lengths are bounded
- [ ] no SQL, shell, or path built from unvalidated input; no secret value in code, log, record, or chat
- [ ] every new endpoint or action names its permission class and object-level check
- [ ] `references/security.md` items run when a dependency, manifest, or lockfile changed

**Accessibility (when a UI file changed)**
- [ ] every control has a label; focus order follows reading order; the change works by keyboard; contrast is not
      reduced; status changes are announced (WCAG 2.2 AA quick reference)

Any unticked item means stop, fix, re-tick. Do not bank a known gap for later.

## Migration safety (tier T2, or whenever a migration file exists in the diff)

- [ ] the overlay's `migrations.check_cmd` is clean (no missing migration)
- [ ] the schema change is backward-compatible with the code currently running in production (expand first: add
      nullable or defaulted columns; contract in a later change after the code stops reading the old shape)
- [ ] every data migration has a reverse, or its irreversibility is written in the brief and the PR body
- [ ] a backup is named (tool and tag from `migrations.backup_tool`) before the production migrate; if the overlay's
      `migrations.rollback` is `none`, say so in the PR body
- [ ] the deploy's migration step cannot be surprised: no untracked migration files, no renamed migration

## Before leaving the phase

1. Run every command in the overlay's `ci.local_chain`, in order, under the `toolchain` versions, and record each
   as `cmd=` evidence. Then run the full test suite once more on the finished state.
2. Optional: `/simplify` on the diff for reuse and altitude cleanups (quality only; it is not a bug hunt).
3. Stamp `<!-- phase: 4 done=<ts> -->`.

Gate: every unit's checklist fully ticked with evidence · local CI chain green under the CI toolchain · full suite
green · migration list done when applicable.

Sources: test pyramid and alternatives (https://web.dev/articles/ta-strategies); flaky-test quarantine
(https://martinfowler.com/articles/nonDeterminism.html); Django migrations (https://docs.djangoproject.com/en/5.2/topics/migrations/);
`assertNumQueries` (https://docs.djangoproject.com/en/5.2/topics/testing/tools/#django.test.TransactionTestCase.assertNumQueries);
WCAG 2.2 quick reference (https://www.w3.org/WAI/WCAG22/quickref/); Core Web Vitals thresholds (https://web.dev/articles/vitals).
