# MEMORY.md

This file stores durable repo memory for agents. It is not a diary and should not contain transient task notes.

## Current repo facts

- This repository is a generic Continuous AgentOps template.
- The template is designed to be copied into other repositories.
- Project-specific content should live in the target repository after installation, not in the reusable template.

## Known constraints

- Keep `AGENTS.md` short and map-like.
- Keep `.codex/`, `.agents/skills/`, and `docs/agentops/` reusable by default.
- Do not store secrets, credentials, tokens, or private customer data.
- Do not create unbounded autonomous loops.
- Write actions must be reviewable and test-gated.

## Repeated agent mistakes

Use this format when a mistake repeats:

```md
### Mistake: <name>
- Observed behavior:
- Correct behavior:
- Prevention mechanism:
- Related files:
```

## Recently changed conventions

Use this format:

```md
### <YYYY-MM-DD> — <change>
- Change:
- Reason:
- Files affected:
```

## Deprecated guidance

Use this format:

```md
### Deprecated: <guidance>
- Replacement:
- Removal date:
- Cleanup issue:
```
