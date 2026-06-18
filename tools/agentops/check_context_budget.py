from tools.agentops.common import main_check, warn_if_large

checks = [
    warn_if_large("AGENTS.md", 120),
    warn_if_large("MEMORY.md", 200),
    warn_if_large("docs/prompt-library.md", 250),
]
raise SystemExit(main_check("check_context_budget", checks))
