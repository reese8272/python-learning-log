#!/usr/bin/env python3
"""Create a run record for one issue from assets/run-record.md, the project overlay, and the git baseline.

  new_run.py --id T87 --mode ship --tier T1 [--overlay PATH] [--project-dir DIR] [--tracker-ref TEXT]

Refuses to overwrite an existing record. Prints the path it wrote.
"""
from __future__ import annotations

import argparse
import os
import subprocess
import sys
import tomllib
from datetime import datetime, timezone
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parent.parent
TEMPLATE = SKILL_DIR / "assets" / "run-record.md"


def git(repo: Path, *args: str) -> str:
    try:
        return subprocess.run(["git", "-C", str(repo), *args], capture_output=True, text=True, timeout=30).stdout.strip()
    except (OSError, subprocess.TimeoutExpired):
        return ""


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--id", required=True, help="tracker id, e.g. T87, IT-12, 42")
    p.add_argument("--mode", required=True, choices=("learn", "ship"))
    p.add_argument("--tier", required=True, choices=("T0", "T1", "T2"))
    p.add_argument("--overlay", help="overlay TOML (default: <project-dir>/.claude/issue-workflow.toml)")
    p.add_argument("--project-dir", default=os.environ.get("CLAUDE_PROJECT_DIR") or os.getcwd())
    p.add_argument("--tracker-ref", default="", help="card/issue URL or path to paste into the record")
    args = p.parse_args(argv)

    project_dir = Path(args.project_dir).resolve()
    overlay_path = Path(args.overlay) if args.overlay else project_dir / ".claude" / "issue-workflow.toml"
    overlay: dict = {}
    if overlay_path.exists():
        overlay = tomllib.loads(overlay_path.read_text(encoding="utf-8"))
    else:
        print(f"note: no overlay at {overlay_path}; using generic defaults", file=sys.stderr)

    repo_dir = project_dir / overlay.get("repo_dir", ".")
    run_dir = project_dir / (overlay.get("run_record", {}).get("dir") or "docs/issue-runs")
    safe_id = "".join(c if c.isalnum() or c in "-_" else "-" for c in args.id)
    target = run_dir / f"{safe_id}.md"
    if target.exists():
        print(f"refusing to overwrite existing record: {target}", file=sys.stderr)
        return 1

    branch = git(repo_dir, "rev-parse", "--abbrev-ref", "HEAD") or "?"
    head = git(repo_dir, "rev-parse", "--short=9", "HEAD") or "?"
    dirty = len([l for l in git(repo_dir, "status", "--porcelain").splitlines() if l.strip()])
    upstream = git(repo_dir, "rev-parse", "--abbrev-ref", "@{u}") or "none"

    text = TEMPLATE.read_text(encoding="utf-8").format(
        id=args.id,
        project=overlay.get("project", project_dir.name),
        mode=args.mode,
        tier=args.tier,
        started=datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%MZ"),
        overlay=str(overlay_path) if overlay_path.exists() else "none",
        repo_dir=str(repo_dir),
        branch=branch,
        head=head,
        dirty=dirty,
        upstream=upstream,
        tracker_ref=args.tracker_ref or "(fill in)",
    )
    run_dir.mkdir(parents=True, exist_ok=True)
    target.write_text(text, encoding="utf-8")
    print(target)
    return 0


if __name__ == "__main__":
    sys.exit(main())
