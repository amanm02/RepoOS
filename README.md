# RepoOS

RepoOS is a reusable Continuous AgentOps template for making repositories more agent-legible, testable, and self-improving.

Operating principle:

> Every repeated agent mistake becomes either a test, a hook, a skill, a doc update, a subagent role, a schema constraint, or a repo-structure change.

## What this template provides

- Short, map-like `AGENTS.md` for agent onboarding.
- Durable `MEMORY.md` for stable repo facts and repeated failure patterns.
- AgentOps documentation for docs, folder structure, hooks, MCPs, tools, function calls, evals, and harness engineering.
- Codex configuration, rules, subagents, hooks, and reusable skills.
- Lightweight audit scripts and Makefile targets.
- GitHub Actions, issue templates, and PR checklist gates.
- A bounded Ralph Wiggum loop protocol for safe iterative improvement.

## Runner requirement

RepoOS GitHub Actions are configured for a repository-level MacBook self-hosted runner with these labels:

```yaml
runs-on: [self-hosted, macOS, ARM64]
```

See `docs/agentops/github-actions-runners.md` before copying this template into a target repository. If a target repo should use GitHub-hosted runners instead, update `.github/workflows/agentops.yml` accordingly.

## Install into another repo

Copy the template files into the target repository, then run:

```bash
make agentops-pr
make hooks-smoke
make mcp-smoke
```

Then customize only the project-specific documents:

- `README.md`
- `docs/ROADMAP.md`
- `docs/verification.md`
- `docs/issue-map.md`
- `docs/specs/`
- `docs/agentops/github-actions-runners.md` if the target repo uses different runner labels

Keep `.codex/`, `.agents/skills/`, and `docs/agentops/` generic unless the target repo needs a repo-specific override.

## Core rules

1. `AGENTS.md` is a map, not a manual.
2. `MEMORY.md` stores durable repo facts, not notes.
3. Every repeated mistake becomes a guardrail.
4. Every guardrail must be testable.
5. Every tool must have a contract.
6. Every MCP must have a registry entry and smoke test.
7. Every hook must be deterministic and low-noise.
8. Every large workflow must have a plan.
9. Every completed plan must be archived.
10. Every stale doc must be updated, moved, or deleted.
11. Every agent loop must be bounded.
12. Every claim of completion must include verification.
