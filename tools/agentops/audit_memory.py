from tools.agentops.common import main_check, require_file, warn_if_large

checks = [
    require_file("MEMORY.md"),
    warn_if_large("MEMORY.md", 200),
]
raise SystemExit(main_check("audit_memory", checks))
