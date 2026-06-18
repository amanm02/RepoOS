from tools.agentops.common import main_check, require_file

checks = [
    require_file("docs/agentops/tool-registry.md"),
    require_file("docs/agentops/function-call-registry.md"),
]
raise SystemExit(main_check("audit_registries", checks))
