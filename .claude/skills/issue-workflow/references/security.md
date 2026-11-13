# Security and supply chain, per change

Read at Phase 2 for tier T2, and at Phase 4 whenever the diff adds or upgrades a dependency, touches a manifest or
lockfile, or adds an input, endpoint, or permission.

## Threat model in four questions (every T2 change)

1. What are we working on? Name the new input, endpoint, field, job, or permission in one line.
2. What can go wrong? Walk STRIDE once: spoofing (who can pretend to be whom), tampering (what can be altered in
   transit or at rest), repudiation (what action leaves no trace), information disclosure (what the caller can now
   read that they could not), denial of service (what unbounded work a caller can trigger), elevation (what the
   caller can now do that they could not).
3. What will we do about it? One mitigation per real threat; "accepted, because ..." is allowed and logged.
4. Did we do enough? The Phase 4 security items and the fresh-context `/security-review` answer this.

## Pick-list from ASVS L2 for common change types

- **New endpoint or action:** permission class named; object-level check present; typed serializer validates every
  field; string lengths bounded; the unauthenticated and the wrong-role caller both get the same safe error.
- **New stored field:** does it leak through any existing public serializer or list endpoint? Grep the serializers
  before adding the field, not after a report.
- **File upload or path from input:** extension and size bounded; never joined into a filesystem path without
  normalisation; served with a safe content type.
- **Auth or session change:** expiry and rotation stated; same error for unknown user and wrong password; no secret
  in a URL or log.
- **Config, CORS, CSRF, headers:** the allowed origins are exact; credentials flags justified; HSTS, nosniff,
  frame-options, CSP, referrer policy unchanged or tightened.

## Dependencies and supply chain

- No new dependency without a line in the brief naming the maintained alternative that lost and the lockfile change.
- Run every `audit_cmds` entry when a manifest or lockfile changed and record the exit as `cmd=` evidence. Run
  `npm audit` after the build, not before it (ISSUES_LOG 2026-08-03-02).
- Lockfiles are committed and reviewed as part of the diff; pins are exact.
- Before the first build of a repository you did not write, run the config-file malware scan the project provides
  (`tools/fingerprint.sh` in WorldCovers) and read its output (ISSUES_LOG 2026-09-28-01; the BeaverTail loader lived
  in `postcss.config.js`).
- Realistic target for a small team: SLSA Build L2 (hosted CI builds the artifact; provenance is the run). Secret
  scanning and push protection are repository settings, not custom tooling; check they are on when a T2 change
  touches CI.

## Secrets

- Grep the diff for literal keys, tokens, passwords, and `.env` content before committing.
- Never print a secret value in chat, the run record, a PR body, a commit, or a log line. Refer to secrets by name.
- A new config value goes in the committed env example with a description and no value.

Sources: OWASP Threat Modeling Cheat Sheet (https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html);
OWASP ASVS (https://owasp.org/www-project-application-security-verification-standard/, https://github.com/OWASP/ASVS);
NIST SSDF PW/RV practices (https://csrc.nist.gov/pubs/sp/800/218/final); SLSA levels (https://slsa.dev/spec/v1.0/levels);
GitHub secret scanning (https://docs.github.com/en/code-security/getting-started/understanding-github-secret-types).
