from __future__ import annotations

import argparse


def session_start() -> int:
    print("RepoOS hook: read AGENTS.md, MEMORY.md, and docs/agentops/README.md.")
    return 0


def prompt_scope() -> int:
    print("RepoOS hook: keep work bounded; use implementation plans for large changes.")
    return 0


def pre_tool() -> int:
    print("RepoOS hook: use explicit approval for sensitive files or irreversible actions.")
    return 0


def post_tool() -> int:
    print("RepoOS hook: record repeated tool problems in docs/agentops/improvement-backlog.md.")
    return 0


def stop() -> int:
    print("RepoOS hook: include validation results before reporting completion.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("event", choices=["session-start", "prompt-scope", "pre-tool", "post-tool", "stop"])
    args = parser.parse_args()
    return {
        "session-start": session_start,
        "prompt-scope": prompt_scope,
        "pre-tool": pre_tool,
        "post-tool": post_tool,
        "stop": stop,
    }[args.event]()


if __name__ == "__main__":
    raise SystemExit(main())
