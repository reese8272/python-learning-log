#!/usr/bin/env python3
"""Gate for the /issue-workflow skill.

Two subcommands, both stdlib-only (Python >= 3.11):

  gate.py overlay <issue-workflow.toml>
      Validate a project overlay against the schema. Exit 0 if valid, 1 if not.

  gate.py run <run-record.md> [--overlay <toml>] [--verify] [--metrics] [--cwd <dir>]
      Validate a run record: phase stamps, evidence on every checked item,
      tier-mandatory sections, per-PR CI rule, per-environment deploy stamps.
      --verify re-executes every `cmd=` evidence and checks every `file=` path.
      --metrics derives lead time / reopens / CI reruns / deploy attempts from
      the stamps. Exit 0 only when every rule passes and all 8 phases are done.

The record grammar is documented in references/overlay-schema.md and
assets/run-record.md. Markers are HTML comments: <!-- kind: key=value ... -->.
"""
from __future__ import annotations

import argparse
import re
import shlex
import subprocess
import sys
import tomllib
from datetime import datetime, timezone
from pathlib import Path

PHASES = list(range(8))
TIERS = ("T0", "T1", "T2")
MODES = ("learn", "ship")

MARKER_RE = re.compile(r"<!--\s*(?P<kind>[a-z_]+):\s*(?P<body>.*?)\s*-->", re.S)
KV_RE = re.compile(r'(?P<k>[A-Za-z_][A-Za-z0-9_]*)=(?:"(?P<q>(?:[^"\\]|\\.)*)"|(?P<u>\S+))')
CHECKED_RE = re.compile(r"^\s*- \[x\]", re.I)
UNCHECKED_RE = re.compile(r"^\s*- \[ \]")
HEADING_RE = re.compile(r"^#{1,6}\s")

# --------------------------------------------------------------------------- overlay schema

SHIP_MODELS = ("pr-then-promote", "trunk-pr", "direct-push", "manual")

# key -> (type, required)
TOP_SCHEMA: dict[str, tuple[type | tuple[type, ...], bool]] = {
    "project": (str, True),
    "ship_model": (str, True),
    "repo_dir": (str, False),
    "base_branch": (str, True),
    "protected_branches": (list, False),
    "branch_pattern": (str, False),
    "commit_style": (str, False),
    "text_rules": (list, False),
    "state_doc": (str, False),
    "toolchain": (dict, False),
    "ci": (dict, False),
    "audit_cmds": (list, False),
    "migrations": (dict, False),
    "environments": (list, False),
    "tracker": (dict, False),
    "decision_logs": (dict, False),
    "handoff": (dict, False),
    "run_record": (dict, False),
    "forbidden": (list, False),
    "comms": (dict, False),
    "changelog": (str, False),
}
ENV_SCHEMA = {"name": (str, True), "deployed_by": (str, True), "verify": (list, True),
              "rollback": (str, False), "watch_minutes": (int, False)}
TRACKER_SCHEMA = {"kind": (str, True), "board": (str, False), "path": (str, False), "skill": (str, False),
                  "t2_design_review": (str, False), "secondary": (dict, False), "transitions": (dict, False),
                  "evidence_comment": (str, False), "id_format": (str, False)}
CI_SCHEMA = {"provider": (str, False), "local_chain": (list, True), "required_checks": (list, False),
             "review_bot": (dict, False)}
RUN_RECORD_SCHEMA = {"dir": (str, True), "commit": (bool, False)}


def _check_table(name: str, table: dict, schema: dict, errors: list[str], warnings: list[str]) -> None:
    for key in table:
        if key not in schema:
            errors.append(f"{name}: unknown key '{key}' (typo?)")
    for key, (typ, required) in schema.items():
        if key not in table:
            if required:
                errors.append(f"{name}: missing required key '{key}'")
            continue
        if not isinstance(table[key], typ):
            errors.append(f"{name}.{key}: expected {getattr(typ, '__name__', typ)}, got {type(table[key]).__name__}")


def validate_overlay(path: Path) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    try:
        data = tomllib.loads(path.read_text(encoding="utf-8"))
    except (OSError, tomllib.TOMLDecodeError) as exc:
        return [f"cannot parse {path}: {exc}"], []
    _check_table("overlay", data, TOP_SCHEMA, errors, warnings)
    model = data.get("ship_model")
    if model is not None and model not in SHIP_MODELS:
        errors.append(f"ship_model must be one of {SHIP_MODELS}, got '{model}'")
    for i, env in enumerate(data.get("environments", []) or []):
        if not isinstance(env, dict):
            errors.append(f"environments[{i}] must be a table")
            continue
        _check_table(f"environments[{i}]", env, ENV_SCHEMA, errors, warnings)
    if "tracker" in data and isinstance(data["tracker"], dict):
        _check_table("tracker", data["tracker"], TRACKER_SCHEMA, errors, warnings)
        t2 = data["tracker"].get("t2_design_review")
        if t2 is not None and t2 not in ("post-and-proceed", "wait"):
            errors.append("tracker.t2_design_review must be 'post-and-proceed' or 'wait'")
    if "ci" in data and isinstance(data["ci"], dict):
        _check_table("ci", data["ci"], CI_SCHEMA, errors, warnings)
    if "run_record" in data and isinstance(data["run_record"], dict):
        _check_table("run_record", data["run_record"], RUN_RECORD_SCHEMA, errors, warnings)
    if model in ("pr-then-promote", "trunk-pr"):
        if "ci" not in data:
            warnings.append(f"ship_model={model} but no [ci] table: phases 5/6 will have no CI gate")
        if not data.get("environments"):
            warnings.append(f"ship_model={model} but no [[environments]]: phase 6 collapses to 'confirm the merge landed'")
    if model == "direct-push" and data.get("environments"):
        warnings.append("ship_model=direct-push with environments: phase 6 will still require deploy stamps")
    for key in ("forbidden", "text_rules"):
        if key not in data:
            warnings.append(f"no '{key}' list; Phase 0 will have nothing to echo")
    return errors, warnings


# --------------------------------------------------------------------------- record parsing

def parse_kv(body: str) -> dict[str, str]:
    out: dict[str, str] = {}
    for m in KV_RE.finditer(body):
        val = m.group("q") if m.group("q") is not None else m.group("u")
        out[m.group("k")] = val.replace('\\"', '"') if val else ""
    return out


def parse_ts(value: str | None) -> datetime | None:
    if not value:
        return None
    try:
        dt = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt


class Record:
    def __init__(self, path: Path):
        self.path = path
        self.text = path.read_text(encoding="utf-8")
        self.lines = self.text.splitlines()
        self.markers: list[tuple[int, str, dict[str, str]]] = []  # (line_no, kind, kv)
        for i, line in enumerate(self.lines, 1):
            for m in MARKER_RE.finditer(line):
                kv = parse_kv(m.group("body"))
                bare = re.match(r"\s*(\d+)\b", m.group("body"))
                if m.group("kind") == "phase" and bare:
                    kv.setdefault("n", bare.group(1))
                self.markers.append((i, m.group("kind"), kv))
        self.run = next((kv for _, k, kv in self.markers if k == "run"), None)

    def of(self, kind: str) -> list[tuple[int, dict[str, str]]]:
        return [(ln, kv) for ln, k, kv in self.markers if k == kind]

    def sections(self) -> list[tuple[str, dict[str, str], int, int]]:
        """(name, kv, start_line, end_line) for every `section:` marker; a section runs to the next heading."""
        out = []
        secs = self.of("section")
        for ln, kv in secs:
            end = len(self.lines)
            for j in range(ln, len(self.lines)):
                if HEADING_RE.match(self.lines[j]):
                    end = j
                    break
            out.append((kv.get("name", "?"), kv, ln, end))
        return out


# --------------------------------------------------------------------------- rules

class Result:
    def __init__(self) -> None:
        self.rows: list[tuple[str, str, str]] = []  # (check, status, detail)
        self.ok = True

    def add(self, check: str, passed: bool | None, detail: str = "") -> None:
        status = "PASS" if passed else ("PENDING" if passed is None else "FAIL")
        if passed is False:
            self.ok = False
        if passed is None:
            self.ok = False
        self.rows.append((check, status, detail))

    def table(self) -> str:
        w = max((len(r[0]) for r in self.rows), default=10)
        lines = [f"{'check'.ljust(w)}  status   detail", f"{'-' * w}  -------  ------"]
        for check, status, detail in self.rows:
            lines.append(f"{check.ljust(w)}  {status.ljust(7)}  {detail}")
        return "\n".join(lines)


def phase_state(rec: Record, res: Result) -> set[int]:
    """Replay phase stamps in file order. Returns the set of phases currently done."""
    done: set[int] = set()
    order_ok = True
    for ln, kv in rec.of("phase"):
        try:
            n = int(kv.get("n", kv.get("phase", "")))
        except ValueError:
            res.add("phase stamps", False, f"line {ln}: phase marker without a valid n=")
            return done
        if n not in PHASES:
            res.add("phase stamps", False, f"line {ln}: phase {n} is not 0-7")
            return done
        if "reopened" in kv:
            done -= {p for p in done if p >= n}
            continue
        if "done" not in kv:
            res.add("phase stamps", False, f"line {ln}: phase {n} marker has neither done= nor reopened=")
            return done
        missing = [p for p in range(n) if p not in done]
        if missing:
            order_ok = False
            res.add("phase stamps", False, f"line {ln}: phase {n} done before phase(s) {missing}")
            return done
        done.add(n)
    if order_ok:
        pending = [p for p in PHASES if p not in done]
        if pending:
            res.add("phase stamps", None, f"done {sorted(done)}; pending {pending}")
        else:
            res.add("phase stamps", True, "phases 0-7 done in order")
    return done


def evidence_for_line(rec: Record, idx: int) -> list[dict[str, str]]:
    """Evidence markers on the checked line, or on the immediately following evidence-only line(s)."""
    found = [kv for ln, k, kv in rec.markers if k == "evidence" and ln == idx]
    j = idx + 1
    while j <= len(rec.lines):
        line = rec.lines[j - 1]
        stripped = line.strip()
        if not stripped or CHECKED_RE.match(line) or UNCHECKED_RE.match(line) or HEADING_RE.match(line):
            break
        if MARKER_RE.sub("", stripped).strip():
            break  # a real content line, not an evidence-only line
        found += [kv for ln, k, kv in rec.markers if k == "evidence" and ln == j]
        j += 1
    return found


def typed(ev: dict[str, str]) -> bool:
    return any(k in ev for k in ("cmd", "file", "url", "run"))


def check_evidence(rec: Record, res: Result, tier: str) -> None:
    missing: list[int] = []
    note_only_required: list[int] = []
    # note-only evidence is refused only inside sections required at T2 (threat, migration); a T1 rollback
    # section legitimately holds a prose answer
    required_sections = [(name, kv, s, e) for name, kv, s, e in rec.sections()
                         if kv.get("required") == "T2" and tier_at_least(tier, "T2")]
    for i, line in enumerate(rec.lines, 1):
        if not CHECKED_RE.match(line):
            continue
        evs = evidence_for_line(rec, i)
        if not evs:
            missing.append(i)
            continue
        in_required = any(s <= i <= e for _, _, s, e in required_sections)
        if in_required and not any(typed(ev) for ev in evs):
            note_only_required.append(i)
    if missing:
        res.add("evidence on [x]", False, f"no evidence marker on checked line(s) {missing}")
    else:
        n = sum(1 for l in rec.lines if CHECKED_RE.match(l))
        res.add("evidence on [x]", True, f"{n} checked item(s) carry evidence")
    if note_only_required:
        res.add("typed evidence in required sections", False,
                f"note-only evidence on line(s) {note_only_required} inside a T2-required section")
    elif required_sections:
        res.add("typed evidence in required sections", True, f"{len(required_sections)} required section(s)")


def tier_at_least(tier: str, needed: str) -> bool:
    return TIERS.index(tier) >= TIERS.index(needed) if tier in TIERS and needed in TIERS else False


def check_required_sections(rec: Record, res: Result, tier: str) -> None:
    secs = rec.sections()
    for name, kv, s, e in secs:
        need = kv.get("required")
        if not need or not tier_at_least(tier, need):
            continue
        body = rec.lines[s:e]
        checked = [l for l in body if CHECKED_RE.match(l)]
        if not checked:
            res.add(f"section '{name}' ({need}+)", False, f"required for tier {tier} but has no checked item")
        else:
            res.add(f"section '{name}' ({need}+)", True, f"{len(checked)} checked item(s)")


def check_prs(rec: Record, res: Result) -> None:
    prs = rec.of("pr")
    if not prs:
        res.add("pr markers", None, "no pr: marker yet")
        return
    latest: dict[str, tuple[int, dict[str, str]]] = {}
    for ln, kv in prs:
        latest[kv.get("n", f"line{ln}")] = (ln, kv)
    for n, (ln, kv) in latest.items():
        problems = []
        if kv.get("ci") != "success":
            problems.append(f"ci={kv.get('ci', '?')}")
        if kv.get("ci_head") and kv.get("head") and kv["ci_head"] != kv["head"]:
            problems.append(f"ci_head {kv['ci_head'][:9]} != head {kv['head'][:9]} (CI did not run on the final SHA)")
        if not kv.get("ci_head"):
            problems.append("no ci_head= (record the SHA the green run checked)")
        if not kv.get("merged"):
            res.add(f"PR #{n}", None, "open: " + ("; ".join(problems) if problems else "CI green on head, not merged yet"))
            continue
        res.add(f"PR #{n}", not problems, "; ".join(problems) if problems else f"ci green on {kv['head'][:9]}, merged {kv['merged'][:9]}")


def check_deploys(rec: Record, res: Result, overlay: dict | None) -> None:
    deploys = rec.of("deploy")
    handoffs = rec.of("handoff")
    pushes = rec.of("push")
    latest: dict[str, dict[str, str]] = {}
    for _, kv in deploys:
        env = kv.get("env", "?")
        if env not in latest or int(kv.get("attempt", "1")) >= int(latest[env].get("attempt", "1")):
            latest[env] = kv
    handed = {kv.get("env"): kv for _, kv in handoffs}
    envs = [e["name"] for e in (overlay or {}).get("environments", []) if isinstance(e, dict)] if overlay else list(latest)
    model = (overlay or {}).get("ship_model")
    if overlay is not None and not envs:
        if model == "direct-push":
            if pushes:
                kv = pushes[-1][1]
                res.add("push", bool(kv.get("confirmed")), f"{kv.get('branch', '?')}@{kv.get('sha', '?')[:9]} confirmed={kv.get('confirmed', 'no')}")
            else:
                res.add("push", None, "direct-push project: no push: marker yet")
        else:
            res.add("deploy", True, "overlay defines no environments")
        return
    merged_bases = {kv.get("base") for _, kv in rec.of("pr") if kv.get("merged")}
    by_name = {e["name"]: e for e in (overlay or {}).get("environments", []) if isinstance(e, dict)} if overlay else {}
    for env in envs:
        spec = by_name.get(env, {}).get("deployed_by", "")
        if ":" in spec and spec.split(":", 1)[0] in ("auto-on-merge-to", "promotion-pr"):
            base = spec.split(":", 1)[1]
            if base not in merged_bases:
                res.add(f"deploy {env}", False if env in latest else None,
                        f"deployed_by={spec} but no merged pr: marker with base={base}")
                continue
        if env in latest:
            kv = latest[env]
            v = kv.get("verify", "0/0")
            try:
                a, b = (int(x) for x in v.split("/"))
            except ValueError:
                a, b = 0, 1
            ok = a == b and b > 0
            res.add(f"deploy {env}", ok, f"run={kv.get('run', '?')} attempt={kv.get('attempt', '1')} verify={v}")
        elif env in handed:
            kv = handed[env]
            res.add(f"deploy {env}", bool(kv.get("to")), f"handed to {kv.get('to', '?')} at {kv.get('at', '?')}")
        else:
            res.add(f"deploy {env}", None, "no deploy: or handoff: stamp yet")


def verify_evidence(rec: Record, res: Result, cwd: Path) -> None:
    cmds = [(ln, kv) for ln, kv in rec.of("evidence") if "cmd" in kv]
    files = [(ln, kv) for ln, kv in rec.of("evidence") if "file" in kv]
    bad: list[str] = []
    for ln, kv in cmds:
        want = int(kv.get("exit", "0"))
        try:
            proc = subprocess.run(kv["cmd"], shell=True, cwd=cwd, capture_output=True, text=True, timeout=1800)
            got = proc.returncode
        except subprocess.TimeoutExpired:
            got = -1
        if got != want:
            bad.append(f"line {ln}: `{kv['cmd']}` exit {got} (recorded {want})")
    for ln, kv in files:
        p = kv["file"].split(":")[0]
        if not (cwd / p).exists() and not Path(p).exists():
            bad.append(f"line {ln}: file {p} does not exist")
    res.add("verify cmd/file evidence", not bad, "; ".join(bad) if bad else f"{len(cmds)} cmd + {len(files)} file evidence re-checked")


def metrics(rec: Record) -> str:
    out = []
    started = parse_ts((rec.run or {}).get("started"))
    phase_done: dict[int, datetime] = {}
    reopens = 0
    for _, kv in rec.of("phase"):
        if "reopened" in kv:
            reopens += 1
        elif "done" in kv:
            try:
                phase_done[int(kv.get("n", kv.get("phase", "-1")))] = parse_ts(kv["done"]) or datetime.min.replace(tzinfo=timezone.utc)
            except ValueError:
                pass
    deploy_ts = [parse_ts(kv.get("at")) for _, kv in rec.of("deploy")] + [parse_ts(kv.get("at")) for _, kv in rec.of("handoff")]
    deploy_ts = [t for t in deploy_ts if t]
    end = max([t for t in [phase_done.get(7)] + deploy_ts if t], default=None)
    if started and end:
        out.append(f"lead time (run start -> shipped): {end - started}")
    elif started:
        out.append("lead time: run not finished")
    if started and phase_done.get(4):
        out.append(f"time to build done: {phase_done[4] - started}")
    out.append(f"phase reopens: {reopens}")
    pr_counts: dict[str, int] = {}
    for _, kv in rec.of("pr"):
        pr_counts[kv.get("n", "?")] = pr_counts.get(kv.get("n", "?"), 0) + 1
    out.append(f"CI reruns: {sum(c - 1 for c in pr_counts.values())} across {len(pr_counts)} PR(s)")
    out.append(f"review rounds: {len(rec.of('review'))}")
    attempts: dict[str, int] = {}
    for _, kv in rec.of("deploy"):
        attempts[kv.get("env", '?')] = max(attempts.get(kv.get("env", '?'), 0), int(kv.get("attempt", "1")))
    out.append("deploy attempts: " + (", ".join(f"{e}={a}" for e, a in attempts.items()) or "none"))
    rolled = any(int(a) > 1 for a in attempts.values())
    out.append(f"rollback/redeploy occurred: {'yes' if rolled else 'no'}")
    return "\n".join(out)


# --------------------------------------------------------------------------- commands

def cmd_overlay(args: argparse.Namespace) -> int:
    errors, warnings = validate_overlay(Path(args.path))
    for w in warnings:
        print(f"WARN  {w}")
    for e in errors:
        print(f"ERROR {e}")
    print("overlay: " + ("PASS" if not errors else f"FAIL ({len(errors)} error(s))"))
    return 0 if not errors else 1


def cmd_run(args: argparse.Namespace) -> int:
    rec = Record(Path(args.record))
    res = Result()
    overlay = None
    if args.overlay:
        errs, _ = validate_overlay(Path(args.overlay))
        if errs:
            print("overlay invalid; run `gate.py overlay` first:\n  " + "\n  ".join(errs))
            return 1
        overlay = tomllib.loads(Path(args.overlay).read_text(encoding="utf-8"))
    if not rec.run:
        print("FAIL no <!-- run: id=... mode=... tier=... started=... --> marker")
        return 1
    tier = rec.run.get("tier", "")
    mode = rec.run.get("mode", "")
    res.add("run marker", tier in TIERS and mode in MODES and bool(parse_ts(rec.run.get("started"))),
            f"id={rec.run.get('id', '?')} mode={mode or '?'} tier={tier or '?'} started={rec.run.get('started', '?')}")
    if tier not in TIERS:
        tier = "T2"  # unknown tier: hold to the strictest requirements
    phase_state(rec, res)
    check_evidence(rec, res, tier)
    check_required_sections(rec, res, tier)
    check_prs(rec, res)
    check_deploys(rec, res, overlay)
    if args.verify:
        verify_evidence(rec, res, Path(args.cwd).resolve())
    print(res.table())
    if args.metrics:
        print("\nmetrics\n-------\n" + metrics(rec))
    verdict = "PASS" if res.ok else ("INCOMPLETE" if all(s != "FAIL" for _, s, _ in res.rows) else "FAIL")
    print(f"\ngate: {verdict}" + ("" if args.verify else "  (evidence not re-executed; add --verify for the final verdict)"))
    return 0 if res.ok else 1


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    po = sub.add_parser("overlay", help="validate an overlay TOML")
    po.add_argument("path")
    po.set_defaults(fn=cmd_overlay)
    pr = sub.add_parser("run", help="validate a run record")
    pr.add_argument("record")
    pr.add_argument("--overlay", help="overlay TOML; enables per-environment deploy checks")
    pr.add_argument("--verify", action="store_true", help="re-execute cmd= evidence and check file= paths")
    pr.add_argument("--metrics", action="store_true", help="print derived delivery metrics")
    pr.add_argument("--cwd", default=".", help="directory to run cmd= evidence from (default: cwd)")
    pr.set_defaults(fn=cmd_run)
    args = p.parse_args(argv)
    return args.fn(args)


if __name__ == "__main__":
    sys.exit(main())
