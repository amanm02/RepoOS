# Verification

Use these commands before reporting completion.

```bash
make agentops-pr
make hooks-smoke
make mcp-smoke
make test
```

## Verification summary format

```text
Validation:
- make agentops-pr: pass / did not pass / not run
- make hooks-smoke: pass / did not pass / not run
- make mcp-smoke: pass / did not pass / not run
- make test: pass / did not pass / not run

Notes:
- <anything skipped and why>
```

## Target repo customization

When RepoOS is copied into another repository, add that repo's real commands here:

- lint
- typecheck
- unit tests
- integration tests
- build
- docs checks
