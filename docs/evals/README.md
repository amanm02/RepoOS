# Evals

Use this directory to define repeatable checks for agent workflow behavior.

## Recommended regression cases

- Agent reports completion without verification.
- Agent edits a forbidden path.
- Agent uses stale documentation.
- Agent calls the wrong tool.
- Agent creates duplicate docs.
- Agent fails to update `MEMORY.md` for durable conventions.
- Agent overloads `AGENTS.md` instead of linking deeper docs.

## Case format

```yaml
id: example-case
task: "Describe the task."
expected_behavior:
  - "Expected behavior."
observed_problem_signals:
  - "Problem signal."
fix_surfaces:
  - "hook"
  - "doc"
grader_notes: "How to evaluate behavior."
```
