# dynamo-log-report-fixed

Repository for Project Dynamo work.

## Structure
- `assessment/` — assessment exercises, one numbered folder per assessment:
  - `assessment 0001/` — "Fix the broken Terminal-Bench task": a repaired TB2 (Harbor) task that parses an access log into a JSON report.
- Real task folders live at the repo root (outside `assessment/`), each in its own folder named by task.

## assessment 0001 — log-report (repaired TB2 task)
Parse an Apache-style access log into a small JSON summary report.

### Layout (under `assessment/assessment 0001/`)
- `task.toml` — Harbor manifest; declares `artifacts = ["/app/report.json"]`.
- `instruction.md` — the prompt the agent sees; numbered criteria consistent with the verifier.
- `environment/Dockerfile` — single task image (agent + verifier); pinned, allowlisted base; bakes pinned test deps.
- `environment/access.log` — seed input, copied to `/app/access.log`.
- `solution/solve.sh`, `solution/solve.py` — reference (oracle) solution.
- `tests/test.sh`, `tests/test_outputs.py` — verifier; writes reward to `/logs/verifier/reward.txt` + `ctrf.json`.

### Calibration
- `harbor run -p . --agent oracle` → reward 1.0
- `harbor run -p . --agent nop`   → reward < 1.0

Expected report: `{"total_requests": 6, "unique_ips": 3, "top_path": "/index.html"}`

### What was repaired from the broken version
1. `task.toml`: `artifacts` was a string pointing at `/app/out.json`; now a top-level array `["/app/report.json"]` matching the real output.
2. `environment/Dockerfile`: `FROM python:latest` → allowlisted, digest-pinned base image; removed the leaked `solution_hint.py` from the build context.
3. Verifier only checked that the file existed; now asserts the exact values (one test per success criterion, each with a docstring).
4. `tests/test.sh` wrote the reward to `/app/reward.txt` with no CTRF; now writes `/logs/verifier/reward.txt` and emits `/logs/verifier/ctrf.json`.
5. `instruction.md` rewritten: absolute `/app` paths, named output file + exact JSON schema, numbered criteria, and the required timeout line.
