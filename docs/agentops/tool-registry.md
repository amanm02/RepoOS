# Tool Registry

Every tool should have one focused job and a predictable contract.

| Tool | Purpose | Access | Inputs | Outputs | Smoke test | Status |
|---|---|---|---|---|---|---|
| _template_ | Describe the job | read/write | schema | schema | command | proposed |

## Tool standard

A tool is allowed only if:

- It does one job.
- Its name is action-oriented.
- Its inputs are explicit.
- Its outputs are predictable.
- It documents whether it reads or writes.
- Write actions use confirmation or a safe approval path.
- Problem modes are documented.
- A smoke test exists.
