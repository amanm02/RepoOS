# Hook Registry

Hooks should be deterministic, low-noise, and testable.

| Hook | Event | Purpose | Blocks? | Test command |
|---|---|---|---:|---|
| load-agent-map | SessionStart | Surface key repo guidance | No | `make hooks-smoke` |
| prompt-scope-check | UserPromptSubmit | Warn about ambiguous or risky scope | No | `make hooks-smoke` |
| dangerous-action-guard | PreToolUse | Guard destructive or secret-touching actions | Yes | `make hooks-smoke` |
| tool-result-audit | PostToolUse | Capture tool result anomalies | No | `make hooks-smoke` |
| verification-reminder | Stop | Remind agent to report verification | No | `make hooks-smoke` |

## Hook standard

A hook is allowed only if:

- It has one purpose.
- It is deterministic.
- It has an actionable message.
- It is classified as blocking or warning.
- It has a smoke test.
- It does not duplicate CI without a reason.
