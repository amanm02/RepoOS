# MCP Registry

Every MCP entry should document purpose, access, constraints, and smoke tests.

| MCP | Purpose | Read/write | Auth required | Smoke test | Status |
|---|---|---|---|---|---|
| _template_ | Describe the MCP | read/write/none | yes/no | command | proposed |

## Required fields

For each MCP, document:

- Name
- Purpose
- Read/write classification
- Authentication requirements
- Safe use cases
- Forbidden use cases
- Input and output expectations
- Failure modes
- Smoke test
- Owner
- Retirement criteria

## Default policy

Do not add MCPs because they are available. Add them only when they make the repo workflow safer, faster, or more reliable.
