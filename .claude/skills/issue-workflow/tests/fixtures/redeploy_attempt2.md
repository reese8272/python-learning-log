# Run record: 12
<!-- run: id=12 mode=ship tier=T1 started=2026-10-20T10:00Z -->
## 0. Ground
<!-- section: name=ground -->
- [x] acceptance criteria exist <!-- evidence: file=tests/fixtures/trunk.toml:1 -->
<!-- phase: 0 done=2026-10-20T10:10Z -->
## 1. Understand
<!-- phase: 1 done=2026-10-20T10:20Z -->
## 2. Check
### Rollback
<!-- section: name=rollback required=T1 -->
- [x] revert PR <!-- evidence: note="single commit, revert is clean" -->
<!-- phase: 2 done=2026-10-20T10:30Z -->
<!-- phase: 3 done=2026-10-20T10:35Z -->
## 4. Build
- [x] lint clean <!-- evidence: cmd="true" exit=0 -->
- [x] tests green
  <!-- evidence: cmd="true" exit=0 -->
<!-- phase: 4 done=2026-10-20T11:00Z -->
## 5. PR
<!-- pr: n=7 base=main head=aaaaaaaaa ci_run=100 ci_head=aaaaaaaaa ci=success merged=bbbbbbbbb -->
<!-- review: source=bot findings=2 fixed=1 dismissed=1 -->
<!-- phase: 5 done=2026-10-20T11:30Z -->
## 6. Deploy
<!-- deploy: env=prod run=101 attempt=1 verify=1/2 at=2026-10-20T11:45Z -->
<!-- deploy: env=prod run=102 attempt=2 verify=2/2 at=2026-10-20T11:55Z -->
<!-- phase: 6 done=2026-10-20T12:00Z -->
## 7. Close
- [x] docs updated <!-- evidence: file=tests/fixtures/trunk.toml:2 -->
<!-- phase: 7 done=2026-10-20T12:10Z -->
