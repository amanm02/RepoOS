# Recurring Audits

## Every PR

Run:

```bash
make agentops-pr
```

Checks:

- `AGENTS.md` stays short.
- `MEMORY.md` remains durable.
- Changed files are reflected in folder map if needed.
- New tools/functions have registries and tests.
- Hooks pass smoke checks.
- MCP registry is updated if MCP config changed.
- Docs are updated when behavior changed.

## Weekly

Run:

```bash
make agentops-weekly
```

Checks:

- Stale docs
- Orphan docs
- Duplicate instructions
- Folder sprawl
- Prompt-library bloat
- Unused hooks, skills, or subagents

## Monthly

Run:

```bash
make agentops-monthly
```

Checks:

- Agent legibility score
- Harness health score
- MCP necessity
- Hook noise
- Top repeated agent defects
