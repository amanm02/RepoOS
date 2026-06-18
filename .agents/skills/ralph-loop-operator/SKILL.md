---
name: ralph-loop-operator
description: Use only for bounded, testable, low-risk iterative repository improvement loops.
---

# Ralph Loop Operator Skill

## Goal

Run exactly one bounded improvement iteration.

## Required inputs

- Plan file
- Progress file
- Verification commands
- Max iteration count
- Forbidden paths
- Rollback instructions

## Loop steps

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
- No large rewrites without explicit plan.
