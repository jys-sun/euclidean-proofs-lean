"""Read and check the actual Lean files used by the notebooks (Python 3.10+)."""
from pathlib import Path
import shutil
import subprocess


def find_project_root(start: str | Path | None = None) -> Path:
    """Find the Lake project from the current directory or an explicit start."""
    location = Path.cwd() if start is None else Path(start)
    location = location.resolve()
    if location.is_file():
        location = location.parent
    for candidate in (location, *location.parents):
        if (candidate / "lean-toolchain").is_file() and (candidate / "lakefile.toml").is_file():
            return candidate
    raise FileNotFoundError("Cannot find project root; start inside euclidean-proof.")


def read_lean(relative_path: str | Path, root: str | Path | None = None) -> str:
    """Read a practice, resolving its path relative to the Lake project."""
    return (find_project_root(root) / relative_path).read_text(encoding="utf-8")


def check_lean(
    relative_path: str | Path, root: str | Path | None = None, timeout: int = 120
) -> subprocess.CompletedProcess:
    """Run Lean, show diagnostics, and raise on an invalid proof or setup failure.

    Run `lake build` first so local imports have compiled .olean files.
    This checks the saved file on disk, including any edits made by the learner.
    """
    project = find_project_root(root)
    source = (project / relative_path).resolve()
    if not source.is_file():
        raise FileNotFoundError(source)
    lake = shutil.which("lake")
    if lake is None:
        raise RuntimeError("Lake is missing from PATH. Install elan, then restart Jupyter; see README.md.")
    command = [lake, "env", "lean", str(source.relative_to(project))]
    try:
        result = subprocess.run(
            command, cwd=project, capture_output=True, text=True, timeout=timeout, check=False
        )
    except subprocess.TimeoutExpired as exc:
        raise RuntimeError(
            "Lean timed out. Run `lake build` in a terminal first, or increase timeout."
        ) from exc
    for output in (result.stdout, result.stderr):
        if output:
            print(output, end="" if output.endswith("\n") else "\n")
    if result.returncode:
        raise subprocess.CalledProcessError(
            result.returncode, command, output=result.stdout, stderr=result.stderr
        )
    print(f"PASS: {source.relative_to(project)}")
    return result
