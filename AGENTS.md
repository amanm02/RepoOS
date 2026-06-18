# AGENTS.md

This file is the entry map for agents. Keep it short. Prefer links to deeper docs.

## Read first

- `README.md`
- `MEMORY.md`
- `docs/agentops/README.md`
- `docs/agentops/folder-structure-map.md`
- `docs/agentops/harness-scorecard.md`
- `docs/agentops/tool-registry.md`
- `docs/agentops/mcp-registry.md`
- `docs/agentops/hook-registry.md`
- `docs/verification.md`

## Working rules

- Start from the linked source of truth.
- Do not rely on stale chat context.
- Prefer small, reviewable diffs.
- Run verification before claiming completion.
- Update docs when behavior, structure, commands, tools, hooks, MCPs, or workflows change.
- Convert repeated mistakes into tests, hooks, skills, evals, schema constraints, or documentation.
- Keep this file map-like. Put detailed guidance in `docs/agentops/`.

## Source-of-truth hierarchy

1. Code and tests
2. Generated schemas and typed contracts
3. `docs/architecture/` or `docs/specs/`
4. `docs/agentops/` registries
5. `MEMORY.md`
6. `AGENTS.md`
7. Prompt library
8. Old plans or chat context

If two sources conflict, update or delete the lower-priority source.

## Done means

- Code changed if needed.
- Tests, lint, typecheck, or documented verification passed.
- Docs updated if behavior or structure changed.
- `MEMORY.md` updated only for durable repo facts.
- New repeated failures added to `docs/agentops/improvement-backlog.md`.
- Changes are committed, pushed, and a PR is opened unless explicitly told otherwise.
