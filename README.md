# Euclidean proofs with Lean 4

A proof on paper can feel clear while still leaving a few steps unstated.
Lean asks us to make those steps explicit. These practice problems are a way
to explore that difference with small, familiar coordinate geometry questions.

Each practice page puts the mathematical argument next to the Lean code, with
a table explaining how they connect. You can start with the math, take a guess
at what the code is doing, and then ask Lean to check it. There's no need to
know Lean already; basic algebra is enough to begin.

The points are pairs of real numbers, written `Point := ℝ × ℝ` in Lean.
We work with **squared distance**—the sum of the squared coordinate
differences—so we can focus on the argument without introducing square roots.

You can read the pages in `data/` and check the `.lean` files with `lake build`.
If you'd like to see the calls and their results together, the single
[demonstration notebook](notebooks/lean_geometry_demo.ipynb) runs all six
practice problems. It also keeps the output from an attempt that should fail,
which gives us something useful to read and work through.

## Set up Lean

You need Git and [elan](https://github.com/leanprover/elan), which provides the
`lean` compiler and `lake` build tool. Python 3.10 or newer is needed only for
the demonstration notebook. Lean and mathlib are not Python packages.

On macOS or Linux, install elan using the
[official Lean installation instructions](https://lean-lang.org/install/).
For example, download the installer, inspect it, then run it:

```bash
curl -fsSL https://raw.githubusercontent.com/leanprover/elan/master/elan-init.sh -o /tmp/elan-init.sh
sh /tmp/elan-init.sh --default-toolchain none
```

Open a new terminal afterward, or run `source "$HOME/.elan/env"`. On Windows,
follow the official installation instructions (or use WSL and the commands above).

From this repository's root, run:

```bash
lake --version
lake update
lake exe cache get
lake build
```

`lean-toolchain` selects **Lean 4.24.0**; `lakefile.toml` selects the matching
**mathlib v4.24.0**. Elan downloads the toolchain automatically. This stable
pair is deliberate; there is no need to upgrade to follow the practice problems. The
mathlib tag's [toolchain file](https://github.com/leanprover-community/mathlib4/blob/v4.24.0/lean-toolchain)
records the matching version. The included `lake-manifest.json` pins the resolved
dependency commits; keep it in version control. `lake update` refreshes that
dependency graph and may also start the cache download automatically.

The first setup needs internet access and several GB of free disk space.
`lake exe cache get` downloads compiled mathlib files rather than building the
library from source. `lake build` then compiles our definitions and all six
proofs. See mathlib's [dependency setup guide](https://github.com/leanprover-community/mathlib4/wiki/Using-mathlib4-as-a-dependency).

## Practice

| Practice | Math proof and Lean comparison | Lean source | Demonstration |
| --- | --- | --- | --- |
| 1. Segment reversal | [Question](data/01_segment_reversal.md) | [Solution](EuclideanProof/SegmentReversal.lean) | [Run](notebooks/lean_geometry_demo.ipynb) |
| 2. Midpoint symmetry | [Question](data/02_midpoint_symmetry.md) | [Solution](EuclideanProof/MidpointSymmetry.lean) | [Run](notebooks/lean_geometry_demo.ipynb) |
| 3. Squared-distance symmetry | [Question](data/03_distance_symmetry.md) | [Solution](EuclideanProof/DistanceSymmetry.lean) | [Run](notebooks/lean_geometry_demo.ipynb) |
| 4. Horizontal segments | [Question](data/04_horizontal_distance.md) | [Solution](EuclideanProof/HorizontalDistance.lean) | [Run](notebooks/lean_geometry_demo.ipynb) |
| 5. Pythagorean identity | [Question](data/05_pythagorean.md) | [Solution](EuclideanProof/Pythagorean.lean) | [Run](notebooks/lean_geometry_demo.ipynb) |
| 6. Nonnegative distance and a false strict inequality | [Question](data/06_nonnegative_distance.md) | [Solution](EuclideanProof/NonnegativeDistance.lean) | [Run](notebooks/lean_geometry_demo.ipynb) |

[Practice 1](data/01_segment_reversal.md) is a gentle starting point. Here's one
way to work through a question:

1. Try a few lines on paper first, then compare them with the mathematical proof.
2. Read the Lean code alongside the table. Notice what each step needs to know.
3. If you feel like experimenting, open the linked `.lean` file and try the suggestion at the end.
4. Save your edits and run `lake build` to check them.

Each practice includes a complete proof, so you have something to compare with
your own attempt. The suggestions at the end leave a little room to explore.
The code blocks in Markdown reproduce the supplied solutions for convenient
reading. The `.lean` files are the executable source of truth; if you change a
solution permanently, update its Markdown code block and explanation as well.

For example, in the horizontal-segment practice:

| Mathematical proof step | Lean proof step |
| --- | --- |
| Expand the squared-distance formula. | `unfold sqDist` |
| Use the assumption A.y = B.y. | `rw [h]` |
| The vertical contribution is zero, leaving (B.x − A.x)². | `simp` |

One Lean tactic can perform several elementary algebra steps. The correspondence
table explains the connection; it does not imply a word-for-word translation.

## When a stronger claim goes too far

[Practice 6](data/06_nonnegative_distance.md) proves $D(A,B)≥ 0$ by adding
nonnegative squares. It then considers the false stronger claim $D(A,B)>0$
for every pair of points: coincident points give $D(A,A)=0$.
The valid Lean module proves both nonnegativity and the negation of the
unconditional strict claim.

The [deliberately invalid proof](examples/expected_failure/StrictDistance.lean)
tries to use a proof of `0 ≤ sqDist A B` where `0 < sqDist A B` is required.
The notebook displays the real type mismatch and records **EXPECTED FAILURE**.
A failed attempt doesn't tell us everything: a true statement can still have
an incorrect proof. Here, the coincident points show why the stronger claim
itself fails, and Lean checks that counterexample too. This invalid file is excluded from the library imports,
so `lake build` still succeeds. To reproduce its failure directly:

```bash
lake env lean examples/expected_failure/StrictDistance.lean
```

## A first Lean proof

```lean
import EuclideanProof.Basic

open EuclideanProof

example (A B : Point) (h : A.2 = B.2) :
    sqDist A B = (B.1 - A.1) ^ 2 := by
  unfold sqDist
  rw [h]
  simp
```

`(A B : Point)` introduces arbitrary points; `(h : A.2 = B.2)` supplies a named
assumption. The colon before `sqDist` introduces the proposition to prove.
`by` begins a tactic proof. `unfold` expands a definition, `rw` substitutes an
equality, and `simp` discharges routine simplifications. The result says:
**for every A and B with equal y-coordinates**, this squared-distance identity holds.

A **goal** is a statement Lean still needs proved; the context contains the
variables and hypotheses currently available. `apply Prod.ext` splits an equality
of pairs into two goals, one for each coordinate. `ring` checks polynomial
identities. `dsimp` expands specified definitions and performs basic computation.
If you write a theorem as `P → Q`, `intro h` moves the assumption `P` into the
context under the name `h`; our practice problems usually introduce hypotheses directly
as theorem parameters instead.

The midpoint definition is marked `noncomputable` because division on arbitrary
real numbers is noncomputable in Lean. It remains fully usable in proofs; these
practice problems concern mathematical identities rather than executable numerical code.

Save edits in the `.lean` files and run `lake build`. A successful build means
Lean accepted the proofs; an invalid proof produces diagnostics and a failed
build. Lean accepts incomplete proofs marked `sorry` with a warning, so **do not use
`sorry` in a completed solution**; none of the supplied solutions use it.

For an interactive view of goals, open the project in VS Code with the
[Lean 4 extension](https://lean-lang.org/install/). The notebook provides batch
checking; it does not embed the editor's live proof-state panel.

## Check proofs

```bash
# Compile every practice, including imported local modules.
lake build

# Check an individual saved practice file after the build.
lake env lean EuclideanProof/HorizontalDistance.lean

# Check the Python runner (no Lean installation needed for these unit tests).
python3 -m unittest discover -s tests -v
```

## Demonstration notebook

One notebook demonstrates all six mathematical proofs, matching Lean sources,
and real checker calls. Its Markdown uses `$...$` for inline formulas and
`$$...$$` for displayed equations, as do the practice problems in `data/`. Saved outputs
show each call and exit code, followed by a summary table. Rerun the notebook
to check your current files.
From the repository root, after setting up Lean and running `lake build`:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m jupyterlab
```

On Windows PowerShell, activate with `.venv\Scripts\Activate.ps1`.
Use the **Python 3 (ipykernel)** kernel. Start with
[lean_geometry_demo.ipynb](notebooks/lean_geometry_demo.ipynb) and run its cells
from top to bottom. The notebook uses Python to run `lake env lean` on the
saved `.lean` files. It requires no custom Lean kernel or language model API key.
After editing a proof, rerun its source-display and check cells. Invalid proofs
print diagnostics and raise a Python exception.

To validate and execute the demonstration notebook after building Lean:

```bash
python - <<'PY'
from pathlib import Path
import nbformat
from nbclient import NotebookClient

root = Path.cwd().resolve()
for path in sorted((root / "notebooks").glob("*.ipynb")):
    notebook = nbformat.read(path, as_version=4)
    nbformat.validate(notebook)
    NotebookClient(notebook, timeout=180, kernel_name="python3",
                   resources={"metadata": {"path": str(path.parent)}}).execute()
    print(f"PASS: {path.name}")
PY
```

## Project map

```text
data/                       Questions, math proofs, Lean code, and comparisons
notebooks/lean_geometry_demo.ipynb  One executed demonstration of all six practice problems
EuclideanProof/Basic.lean   Points, midpoint, and squared distance
EuclideanProof/*.lean       Commented proofs
EuclideanProof.lean         Imports all practice problems for lake build
scripts/lean_runner.py      Shared source reader and Lean subprocess runner
examples/expected_failure/  Deliberately invalid proof checked separately
tests/                      Python runner checks
lakefile.toml               Lake library and mathlib dependency
lean-toolchain              Pinned Lean version
requirements.txt            Optional Python notebook dependencies
```

## Add a practice problem

1. Write `data/07_your_question.md`: state assumptions, question, mathematical
   proof, Lean code, a step correspondence table, hints, and an exercise.
   Specify whether your result concerns squared distance or ordinary distance.
2. Create `EuclideanProof/YourQuestion.lean`, import `EuclideanProof.Basic`, and
   put your theorem inside `namespace EuclideanProof` / `end EuclideanProof`.
3. Add `import EuclideanProof.YourQuestion` to `EuclideanProof.lean`.
4. Run `lake build` and ensure the Markdown code block matches the `.lean` file.
   Add the practice to the table above.
5. To demonstrate the new question, add a section to the shared notebook with
   the mathematical proof, source display, and checker call. Update the expected
   practice count in its summary cell, then rerun the notebook to refresh outputs.

## If something gets stuck

- **`lake: command not found`:** install elan and ensure its `bin` directory is
  on `PATH`. Restart Jupyter after changing your shell environment.
- **An imported `.olean` file is missing:** run `lake exe cache get` followed by
  `lake build` from the repository root.
- **Changes to an imported definition seem ignored:** rerun `lake build`.
  Standalone `lake env lean` checks do not rebuild imported modules.
- **Lean times out in a notebook:** complete setup and `lake build` in a terminal
  first. If necessary, call `check_lean(LEAN_FILE, ROOT, timeout=300)`.
- **Network or download failures:** check access to GitHub, Lean releases, and
  mathlib's cache; retry the failed setup command. No API key is required.
- **macOS reports `tar: Failed to set default locale`:** in the same terminal,
  run `export LANG=C LC_ALL=C`, then retry `lake exe cache get` and `lake build`.
- **A proof fails after an edit:** inspect the goal and hypotheses in the
  diagnostics. Undo your experiment or complete the missing argument.

For more practice, see [Mathematics in Lean](https://leanprover-community.github.io/mathematics_in_lean/).
