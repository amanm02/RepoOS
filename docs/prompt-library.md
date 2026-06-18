# Prompt Library

Keep prompts generic, reusable, and short. Do not add project-specific product content to this template.

## Set up AgentOps

```text
Set up a Continuous AgentOps System for this repository.

Goal:
Create a recurring improvement loop for documentation, repo structure, code quality, tool/function calls, hooks, MCPs, skills, subagents, evals, and harness engineering.

Read first:
- AGENTS.md
- MEMORY.md if present
- docs/verification.md if present
- docs/issue-map.md if present
- .codex/config.toml if present
- .codex/hooks.json if present
- .agents/skills if present

Rules:
- Keep AGENTS.md short and map-like.
- Keep MEMORY.md durable, not conversational.
- Do not duplicate guidance across files.
- Prefer small, mechanical checks over vague instructions.
- Treat repeated agent mistakes as missing guardrails.
- Ralph-style loops must be bounded, sandboxed, and test-gated.

Validation:
- Run make agentops-pr if available.
- Run make hooks-smoke if hooks exist.
- Run make mcp-smoke if MCPs exist.
- Run existing test/lint/typecheck commands if available.

Final response:
1. Summary
2. Files changed
3. New recurring checks
4. Risks
5. Follow-up issues
6. Validation results
```

## One bounded improvement loop

```text
Run one bounded AgentOps improvement loop.

Read:
- docs/agentops/improvement-backlog.md
- docs/agentops/harness-scorecard.md
- docs/verification.md
- MEMORY.md

Rules:
- Select exactly one high-leverage improvement.
- Keep the diff small.
- Do not touch secrets, env files, production configs, or generated files.
- Run relevant verification.
- Update docs only if the change affects workflow, structure, or conventions.
- Append progress to docs/agentops/improvement-backlog.md.
- Commit only if verification passes.
- Stop after one logical change.
```
