# Folder Structure Map

```text
.
├── AGENTS.md
├── MEMORY.md
├── .codex/
│   ├── config.toml
│   ├── hooks.json
│   ├── rules/
│   └── agents/
├── .agents/skills/
├── docs/
│   ├── agentops/
│   ├── decisions/
│   ├── evals/
│   ├── implementation-plans/
│   ├── retrospectives/
│   └── specs/
├── tools/agentops/
└── .github/
```

## Placement rules

- Stable agent guidance: `AGENTS.md`.
- Durable repo facts: `MEMORY.md`.
- Detailed agent operations: `docs/agentops/`.
- Project-specific specs: `docs/specs/`.
- Implementation plans: `docs/implementation-plans/`.
- Post-failure reviews: `docs/retrospectives/`.
- Audit scripts: `tools/agentops/`.
- Reusable skills: `.agents/skills/`.
- Codex config, rules, hooks, subagents: `.codex/`.
