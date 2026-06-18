# Recurring Audits

RepoOS CI is expected to run on a repository-level MacBook self-hosted runner with labels `self-hosted`, `macOS`, and `ARM64`. Include runner health in audit reviews.

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
- The MacBook self-hosted runner is online before relying on GitHub Actions status.

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
- Self-hosted runner is online and has expected labels

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
- Whether the MacBook runner is still the right default for this repo or template target
