# AgentOps

AgentOps is the continuous improvement layer for repository agents.

## Goal

Make the repository more agent-legible, verifiable, safe, and self-improving over time.

## Operating loop

```text
Run work
→ collect trace, terminal log, PR diff, or test result
→ score behavior
→ identify failure pattern
→ choose fix surface
→ open small PR
→ verify
→ update docs, memory, skills, hooks, or schemas
→ add regression case
→ repeat
```

## Fix surface decision table

| Failure pattern | Fix type |
|---|---|
| Agent forgets repo conventions | Update `AGENTS.md` or a scoped `AGENTS.md` |
| Agent follows stale instructions | Update `MEMORY.md`, stale-doc log, or delete old docs |
| Agent calls wrong tool | Update tool registry, MCP instructions, or tool schema |
| Agent skips verification | Add hook, PR checklist, or CI gate |
| Agent creates bloated docs | Add doc linter and max-size thresholds |
| Agent edits wrong files | Add rule, hook, or forbidden-path check |
| Agent repeats a bug | Add regression test and eval case |
| Agent overuses context | Split docs and add context-budget checks |

## Key files

- `agent-legibility-scorecard.md`
- `harness-scorecard.md`
- `folder-structure-map.md`
- `hook-registry.md`
- `mcp-registry.md`
- `tool-registry.md`
- `function-call-registry.md`
- `ralph-loop-protocol.md`
- `improvement-backlog.md`
