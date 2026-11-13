# Run record: T47
<!-- run: id=T47 mode=ship tier=T2 started=2026-10-20T08:00Z -->
<!-- section: name=ground -->
- [x] AC present <!-- evidence: file=docs/issues.md:5481 -->
<!-- phase: 0 done=2026-10-20T08:10Z -->
<!-- phase: 1 done=2026-10-20T08:20Z -->
### Threat model
<!-- section: name=threat required=T2 -->
- [x] new endpoint listed <!-- evidence: note="looked fine" -->
### Rollback
<!-- section: name=rollback required=T1 -->
- [x] revert PR <!-- evidence: note="choices-only migration, reversible" -->
### Migration safety
<!-- section: name=migration required=T2 -->
- [x] makemigrations --check clean <!-- evidence: cmd="true" exit=0 -->
- [x] backward compatible <!-- evidence: file=backend/common/migrations/0021.py:1 -->
<!-- phase: 2 done=2026-10-20T08:40Z -->
<!-- phase: 3 done=2026-10-20T08:45Z -->
- [x] suite green <!-- evidence: cmd="true" exit=0 -->
<!-- phase: 4 done=2026-10-20T10:00Z -->
<!-- pr: n=193 base=staging head=111111111 ci_run=900 ci_head=111111111 ci=success merged=222222222 -->
<!-- review: source=code-review findings=1 fixed=1 dismissed=0 -->
<!-- phase: 5 done=2026-10-20T10:30Z -->
<!-- deploy: env=woco.dev run=901 attempt=1 verify=3/3 at=2026-10-20T10:45Z -->
<!-- phase: 6 done=2026-10-20T11:00Z -->
<!-- phase: 5 reopened=2026-10-21T09:00Z reason="promotion PR" -->
<!-- pr: n=192 base=main head=333333333 ci_run=950 ci_head=333333333 ci=success merged=444444444 -->
<!-- phase: 5 done=2026-10-21T09:30Z -->
<!-- deploy: env=hellowoco.app run=951 attempt=1 verify=3/3 at=2026-10-21T10:00Z -->
<!-- phase: 6 done=2026-10-21T10:05Z -->
- [x] evidence posted to card <!-- evidence: url=https://trello.com/c/x -->
<!-- phase: 7 done=2026-10-21T10:15Z -->
