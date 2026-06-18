# Verification

Use these commands before reporting completion.

```bash
make agentops-pr
make hooks-smoke
make mcp-smoke
make test
```

## GitHub Actions runner

RepoOS GitHub Actions are configured to run on a repository-level MacBook self-hosted runner:

```yaml
runs-on: [self-hosted, macOS, ARM64]
```

Before relying on CI, confirm the runner is online in GitHub:

```text
Repository → Settings → Actions → Runners
```

If the MacBook runner is offline, asleep, or the runner process is stopped, Actions jobs may remain queued. See `docs/agentops/github-actions-runners.md`.

## Verification summary format

```text
Validation:
- make agentops-pr: pass / did not pass / not run
- make hooks-smoke: pass / did not pass / not run
- make mcp-smoke: pass / did not pass / not run
- make test: pass / did not pass / not run
- GitHub Actions self-hosted runner: online / offline / not checked

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
- runner labels if different from `self-hosted`, `macOS`, `ARM64`
