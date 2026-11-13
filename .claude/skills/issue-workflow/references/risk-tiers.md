# Risk tiers

Classify by what the change touches, never by diff size. A ten-line change to a permission class is T2; a
four-hundred-line copy edit is T0. When in doubt, pick the higher tier; it can only come down with a logged decision.

| Tier | Touches | Examples |
|---|---|---|
| **T0** | Docs, copy, styling, comments, non-executed config; no behaviour change | README fix, CSS spacing, help text, changelog |
| **T1** | Logic or UI behaviour without a new trust boundary, schema change, or irreversible step | a new filter on a list page, a bug fix in a serializer, a new component, a refactor with unchanged tests |
| **T2** | Any of: authentication or permissions; schema or data migrations, backfills, or deletes; money or payments; secrets, env, CORS, CSRF, or security headers; CI, deploy, or infrastructure; the public API's shape; third-party dependencies added or upgraded; a step that cannot be undone | new endpoint, new field with migration, a dependency bump, a deploy script change, a bulk recode of existing rows |

## What each tier switches on

| Gate | T0 | T1 | T2 |
|---|---|---|---|
| Brief with fetched documentation (Rule 2) | yes, may be short | yes | yes |
| Rollback field in the brief | yes | yes | yes |
| Scale field (data volume, N+1 risk) | no | yes | yes |
| Threat model (STRIDE-lite, `references/security.md`) | no | only if the Explore pass found a new input | **yes, typed evidence** |
| Migration checklist | no | no | **yes** (or the typed "no migration in this diff" item) |
| Per-unit build checklist with evidence | yes, abbreviated | yes | yes |
| Local CI chain under the CI toolchain | yes | yes | yes |
| Dependency audit (`audit_cmds`) | when a manifest or lockfile changed | same | same |
| Accessibility mini-check | when a UI file changed | same | same |
| Review-bot triage | yes | yes | yes |
| Fresh-context `/code-review` + `/security-review` | no | yes | yes |
| T2 brief posted to the tracker before building | no | no | yes, when an acceptor is named |
| Post-deploy watch window | no | yes | yes |
| Decision-log entry | only if alternatives existed | yes | yes |

## Tier changes mid-run

Raise the tier the moment the diff touches a T2 item you did not expect (a migration appeared, a dependency was
needed). Write a `note=` line in the run record's Phase 0 section with the reason, update the `run:` marker's
`tier=`, and run the gates the new tier adds before continuing. Lowering a tier needs the user's explicit agreement
and a decision-log line.

Sources: NIST SSDF PW.1 risk-based design (https://csrc.nist.gov/pubs/sp/800/218/final); OWASP ASVS levels
(https://owasp.org/www-project-application-security-verification-standard/).
