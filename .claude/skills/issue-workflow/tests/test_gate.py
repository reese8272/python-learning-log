"""Pareto tests for gate.py: one happy path per shape, the load-bearing failure rules, and --verify."""
import io
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "scripts"))
import gate  # noqa: E402

FX = HERE / "fixtures"


def run(*argv):
    buf = io.StringIO()
    with redirect_stdout(buf):
        code = gate.main(list(argv))
    return code, buf.getvalue()


class OverlayTests(unittest.TestCase):
    def test_valid_overlays_pass(self):
        for name in ("trunk.toml", "two_stage.toml"):
            code, out = run("overlay", str(FX / name))
            self.assertEqual(code, 0, out)

    def test_invalid_overlay_names_each_problem(self):
        code, out = run("overlay", str(FX / "invalid.toml"))
        self.assertEqual(code, 1)
        for needle in ("unknown key 'shipmodel'", "ship_model must be one of", "missing required key 'verify'"):
            self.assertIn(needle, out)


class RecordTests(unittest.TestCase):
    def test_single_stage_passes_with_verify_and_metrics(self):
        code, out = run("run", str(FX / "single_stage_pass.md"), "--overlay", str(FX / "trunk.toml"),
                        "--verify", "--metrics", "--cwd", str(HERE.parent))
        self.assertEqual(code, 0, out)
        self.assertIn("gate: PASS", out)
        self.assertIn("lead time (run start -> shipped): 2:10:00", out)

    def test_two_stage_promotion_passes(self):
        code, out = run("run", str(FX / "two_stage_pass.md"), "--overlay", str(FX / "two_stage.toml"), "--metrics")
        self.assertEqual(code, 0, out)
        self.assertIn("deploy hellowoco.app", out)

    def test_two_stage_fails_without_promotion_pr(self):
        text = (FX / "two_stage_pass.md").read_text()
        text = "\n".join(l for l in text.splitlines() if "n=192" not in l)
        with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False) as f:
            f.write(text)
        code, out = run("run", f.name, "--overlay", str(FX / "two_stage.toml"))
        self.assertEqual(code, 1)
        self.assertIn("no merged pr: marker with base=main", out)

    def test_reopened_phase_passes(self):
        code, out = run("run", str(FX / "reopened_pass.md"), "--overlay", str(FX / "trunk.toml"), "--metrics")
        self.assertEqual(code, 0, out)
        self.assertIn("phase reopens: 1", out)
        self.assertIn("CI reruns: 1", out)

    def test_missing_evidence_fails(self):
        code, out = run("run", str(FX / "missing_evidence.md"), "--overlay", str(FX / "trunk.toml"))
        self.assertEqual(code, 1)
        self.assertIn("no evidence marker on checked line", out)

    def test_t2_note_only_evidence_fails(self):
        code, out = run("run", str(FX / "t2_note_only.md"), "--overlay", str(FX / "two_stage.toml"))
        self.assertEqual(code, 1)
        self.assertIn("note-only evidence", out)

    def test_ci_head_mismatch_fails(self):
        code, out = run("run", str(FX / "ci_head_mismatch.md"), "--overlay", str(FX / "trunk.toml"))
        self.assertEqual(code, 1)
        self.assertIn("CI did not run on the final SHA", out)

    def test_redeploy_attempt2_passes_and_reports_rollback(self):
        code, out = run("run", str(FX / "redeploy_attempt2.md"), "--overlay", str(FX / "trunk.toml"), "--metrics")
        self.assertEqual(code, 0, out)
        self.assertIn("rollback/redeploy occurred: yes", out)

    def test_verify_catches_lying_cmd_evidence(self):
        text = (FX / "single_stage_pass.md").read_text().replace('cmd="true" exit=0', 'cmd="false" exit=0', 1)
        with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False) as f:
            f.write(text)
        code, out = run("run", f.name, "--overlay", str(FX / "trunk.toml"), "--verify", "--cwd", str(HERE.parent))
        self.assertEqual(code, 1)
        self.assertIn("`false` exit 1 (recorded 0)", out)

    def test_incomplete_record_is_pending_not_fail(self):
        text = "\n".join((FX / "single_stage_pass.md").read_text().splitlines()[:7])
        with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False) as f:
            f.write(text)
        code, out = run("run", f.name, "--overlay", str(FX / "trunk.toml"))
        self.assertEqual(code, 1)
        self.assertIn("gate: INCOMPLETE", out)
        self.assertIn("pending [1, 2, 3, 4, 5, 6, 7]", out)


if __name__ == "__main__":
    unittest.main()
