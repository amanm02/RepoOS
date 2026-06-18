---
name: tool-call-audit
description: Use when reviewing tools, function calls, schemas, or repeated invocation failures.
---

# Tool Call Audit Skill

## Goal

Make every tool and function call predictable, narrow, testable, and safe.

## Checks

- One job per tool.
- Explicit input schema.
- Predictable output shape.
- Read/write classification.
- Example calls.
- Known failure modes.
- Smoke test.
- Registry entry in `docs/agentops/tool-registry.md` or `docs/agentops/function-call-registry.md`.

## Output

- Schema gaps
- Wrong-tool patterns
- Suggested schema changes
- Suggested smoke tests
