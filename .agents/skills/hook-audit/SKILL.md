---
name: hook-audit
description: Use when adding, reviewing, testing, or pruning Codex hooks.
---

# Hook Audit Skill

## Goal

Keep hooks deterministic, useful, low-noise, and testable.

## Checks

- Hook has one purpose.
- Hook is classified as blocking or warning.
- Hook does not duplicate CI unnecessarily.
- Hook has a smoke test.
- Hook failure message is actionable.
- Hook is registered in `docs/agentops/hook-registry.md`.

## Output

- Hook inventory
- Missing tests
- False positive risks
- False negative risks
- Recommended changes
