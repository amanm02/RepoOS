.PHONY: agentops-pr agentops-weekly agentops-monthly hooks-smoke mcp-smoke test

agentops-pr:
	python tools/agentops/audit_docs.py
	python tools/agentops/audit_memory.py
	python tools/agentops/audit_structure.py
	python tools/agentops/audit_tools.py
	python tools/agentops/audit_hooks.py

agentops-weekly:
	python tools/agentops/find_stale_docs.py
	python tools/agentops/check_context_budget.py
	python tools/agentops/score_harness.py

agentops-monthly:
	python tools/agentops/generate_improvement_backlog.py
	python tools/agentops/audit_mcp.py
	python tools/agentops/audit_function_schemas.py

hooks-smoke:
	python tools/agentops/audit_hooks.py --smoke

mcp-smoke:
	python tools/agentops/audit_mcp.py --smoke

test: agentops-pr hooks-smoke mcp-smoke
