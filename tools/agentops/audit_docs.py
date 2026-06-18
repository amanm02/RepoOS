from tools.agentops.common import main_check, require_file, warn_if_large

checks = [
    require_file("AGENTS.md"),
    require_file("MEMORY.md"),
    require_file("docs/agentops/README.md"),
    require_file("docs/verification.md"),
    warn_if_large("AGENTS.md", 120),
    warn_if_large("MEMORY.md", 200),
]
raise SystemExit(main_check("audit_docs", checks))
