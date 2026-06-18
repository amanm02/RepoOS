---
name: mcp-audit
description: Use when adding, reviewing, or pruning MCP servers and MCP instructions.
---

# MCP Audit Skill

## Goal

Ensure MCP access is necessary, safe, documented, and tested.

## Checks

- Purpose is clear.
- Read/write behavior is documented.
- Auth requirements are explicit.
- Server instructions include constraints and workflows.
- Smoke test exists.
- Retirement criteria are defined.
- Registry entry exists in `docs/agentops/mcp-registry.md`.

## Output

- MCP inventory
- Missing registry fields
- Safety risks
- Smoke test recommendations
