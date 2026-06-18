# Ralph Loop Protocol

Use Ralph-style loops only for bounded, testable, low-risk improvement work.

## Allowed use cases

- Improve documentation structure.
- Fix lint or type issues.
- Add missing smoke tests.
- Update stale registries.
- Prune unused skills or subagents.
- Improve test coverage in a narrow area.

## Required inputs

- Plan file
- Progress file
- Verification commands
- Maximum iterations
- Forbidden paths
- Rollback instructions

## Required behavior per loop

1. Read the plan.
2. Read progress.
3. Choose one small task.
4. Implement one logical change.
5. Run verification.
6. Commit only if checks pass.
7. Append concise progress.
8. Stop if complete or blocked.

## Hard limits

- No unbounded loops.
- No production credentials.
- No destructive commands.
- No schema migrations without review.
- No large rewrites without explicit plan.
