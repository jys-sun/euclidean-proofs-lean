"""Runner contracts; Lean proof correctness is checked by Lean itself."""
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch

from scripts.lean_runner import check_lean, find_project_root, read_lean


class RunnerTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        # macOS maps /var to /private/var; compare canonical paths.
        self.root = Path(self.temp.name).resolve()
        (self.root / "lean-toolchain").write_text("leanprover/lean4:v4.24.0\n")
        (self.root / "lakefile.toml").write_text('name = "test"\n')
        (self.root / "notebooks").mkdir()
        (self.root / "Practice.lean").write_text("example : 1 = 1 := rfl\n")

    def test_root_from_notebook_directory(self):
        self.assertEqual(find_project_root(self.root / "notebooks"), self.root)

    def test_no_project_has_helpful_error(self):
        with tempfile.TemporaryDirectory() as other:
            with self.assertRaisesRegex(FileNotFoundError, "project root"):
                find_project_root(other)

    def test_reads_source_and_rejects_missing_file(self):
        self.assertIn("rfl", read_lean("Practice.lean", self.root))
        with self.assertRaises(FileNotFoundError):
            check_lean("Absent.lean", self.root)

    @patch("scripts.lean_runner.shutil.which", return_value=None)
    def test_missing_lake_explains_installation(self, _which):
        with self.assertRaisesRegex(RuntimeError, "elan"):
            check_lean("Practice.lean", self.root)

    @patch("scripts.lean_runner.shutil.which", return_value="/tools/lake")
    @patch("scripts.lean_runner.subprocess.run")
    def test_success_uses_project_cwd(self, run, _which):
        run.return_value = subprocess.CompletedProcess([], 0, "", "")
        with redirect_stdout(StringIO()) as out:
            result = check_lean("Practice.lean", self.root)
        self.assertEqual(result.returncode, 0)
        args, kwargs = run.call_args
        self.assertEqual(args[0], ["/tools/lake", "env", "lean", "Practice.lean"])
        self.assertEqual(kwargs["cwd"], self.root)
        self.assertIn("PASS", out.getvalue())

    @patch("scripts.lean_runner.shutil.which", return_value="/tools/lake")
    @patch("scripts.lean_runner.subprocess.run")
    def test_bad_proof_prints_diagnostics_and_raises(self, run, _which):
        run.return_value = subprocess.CompletedProcess([], 1, "unsolved goals", "detail")
        with redirect_stdout(StringIO()) as out:
            with self.assertRaises(subprocess.CalledProcessError):
                check_lean("Practice.lean", self.root)
        self.assertIn("unsolved goals", out.getvalue())
        self.assertIn("detail", out.getvalue())
        self.assertNotIn("PASS", out.getvalue())

    @patch("scripts.lean_runner.shutil.which", return_value="/tools/lake")
    @patch("scripts.lean_runner.subprocess.run")
    def test_timeout_has_actionable_message(self, run, _which):
        run.side_effect = subprocess.TimeoutExpired("lake", 1)
        with self.assertRaisesRegex(RuntimeError, "lake build"):
            check_lean("Practice.lean", self.root, timeout=1)


if __name__ == "__main__":
    unittest.main()
