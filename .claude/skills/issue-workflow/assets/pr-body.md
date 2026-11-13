## Summary

Tracker: <id and link, e.g. Trello [T87](url) / tracker #190>. <One line: the user-visible goal.>

- <what changed, grouped Backend / Frontend when both change>
- <rules recorded in the decision log(s), by heading>

## Risk tier

<T0 | T1 | T2> - <one line why; for T2 name the boundary touched: auth / migration / data / secrets / infra / public API>

## Test plan

- [x] <test file>: <what it asserts> (<N> new / changed)
- [x] full suite: <command> -> <count> OK
- [x] local CI chain under the CI toolchain (<node/python versions>): lint, typecheck, unit, build
- [x] <migration check command> clean (when backend changed)
- [ ] After merge on <first environment>: <the one manual check a human does>

## Rollback

<revert this PR | feature flag <name> | expand/contract step N of M | not reversible: <why, and the backup taken>>

## Verify after merge

- <environment>: <verify command or probe>, expected <result>

<attribution footer: "Generated with Claude Code (https://claude.com/claude-code)". Use the plain-ASCII form whenever
the overlay's text_rules forbid non-ASCII in PR bodies; otherwise the standard emoji form is fine.>
