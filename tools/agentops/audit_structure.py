from tools.agentops.common import main_check, require_file, require_any

checks = [
    require_file("docs/agentops/folder-structure-map.md"),
    require_any([".codex/config.toml"], "Codex config"),
    require_any([".agents/skills/doc-gardening/SKILL.md"], "repo skills"),
]
raise SystemExit(main_check("audit_structure", checks))
