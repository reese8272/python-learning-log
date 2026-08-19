# TEARDOWN.md

**Run this Saturday 2026-08-16.** Written as resources are created, not after — a teardown checklist
authored from memory is how a billing surprise happens.

Every resource is tagged `project=secure-api-lab`.

## Before anything

- [ ] Screenshot the working deployment (the 200 with a real token, the CloudWatch alarm, the WAF console).
      **You cannot re-create these after teardown, and they are the interview evidence.**
- [ ] Save the ECS task definition JSON and the ALB listener config into `docs/` — cheap to keep, useful to show.

## Teardown order (dependencies matter)

- [ ] **ECS service** → set desired count to 0, then delete the service
- [ ] **ECS cluster** → delete
- [ ] **ECS task definitions** → deregister (free, but keeps the console honest)
- [ ] **ALB** → delete the listener, then the load balancer  *(~$0.55/day — the largest recurring line)*
- [ ] **Target groups** → delete
- [ ] **WAF web ACL** → disassociate from the ALB first, then delete  *($5/mo + $1/rule/mo)*
- [ ] **ACM certificate** → delete (free, but it blocks nothing once the ALB is gone)
- [ ] **Route 53 record** → delete the alias record. **Decide on the hosted zone** ($0.50/mo — keep it if
      the domain is staying, delete if it was registered only for this)
- [ ] **ECR repository** → delete images, then the repo *(storage is cheap but nonzero)*
- [ ] **CloudWatch log groups** → delete, or set retention to 1 day
- [ ] **Secrets Manager secrets** → delete with `--force-delete-without-recovery` (otherwise they linger
      billed for the 30-day recovery window)
- [ ] **IAM roles** (task role, execution role, GitHub OIDC role) → delete. Free, but leaving an assumable
      role attached to a public OIDC trust policy is a real security loose end, not just clutter
- [ ] **Security groups / VPC resources** created for this
- [ ] **NAT Gateway** — if one was created, this is the sneaky expensive one (~$1/day + data). Verify it's gone.

## Verify

- [ ] `aws resourcegroupstaggingapi get-resources --tag-filters Key=project,Values=secure-api-lab` returns empty
- [ ] Billing console → Cost Explorer shows the run and the drop-off
- [ ] The $25 Budget alert never fired
- [ ] Update `docs/PROJECT_STATE.md` → "AWS resources currently live: **None**"

## Never created in the first place

- ❌ AWS Private CA (~$400/mo general-purpose · ~$50/mo short-lived — prorated from creation, no refund)
- ❌ Shield Advanced (~$3,000/mo, 1-year commitment)

If either of these somehow exists, that is the emergency, and it comes before everything else on this list.
