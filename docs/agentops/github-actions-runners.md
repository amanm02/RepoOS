# GitHub Actions Runners

RepoOS is configured to run GitHub Actions on a repository-level MacBook self-hosted runner.

## Required runner labels

The default workflow expects these labels:

```yaml
runs-on: [self-hosted, macOS, ARM64]
```

The runner should appear in GitHub under:

```text
Repository → Settings → Actions → Runners
```

## Why RepoOS uses a MacBook runner

RepoOS is intended to mirror local agent workflows as closely as possible. A MacBook self-hosted runner is useful when repo automation needs to validate the same environment used for local Codex, hooks, scripts, and developer workflows.

## Setup checklist

- [ ] Register a self-hosted runner at the repository level.
- [ ] Confirm the runner is online.
- [ ] Confirm labels include `self-hosted`, `macOS`, and `ARM64`.
- [ ] Keep the runner app/process active on the MacBook.
- [ ] Run the first PR workflow and confirm the job is picked up by the MacBook.

## Operational notes

- If the MacBook is asleep, offline, or the runner process is stopped, GitHub Actions jobs will queue.
- If a target repo should use GitHub-hosted runners instead, change `.github/workflows/agentops.yml` back to `ubuntu-latest` or the appropriate hosted runner.
- Keep runner-specific assumptions documented here and in `docs/verification.md`.

## Validation

After setup, run or trigger:

```bash
make agentops-pr
make hooks-smoke
make mcp-smoke
```

Then confirm the GitHub Actions job runs on the self-hosted MacBook runner.
