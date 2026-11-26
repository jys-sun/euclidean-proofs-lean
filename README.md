# Euclidean proofs with Lean 4

Small coordinate geometry practice problems, with mathematical proofs beside
Lean code and explanations of how the steps connect. Basic algebra is enough
to get started. We use squared distance to keep the calculations simple.

## Quick start

Install Git and [Lean via elan](https://lean-lang.org/install/), then run
from the repository root:

```bash
lake update
lake exe cache get
lake build
```

The project pins Lean and mathlib to **4.24.0**. Setup needs internet access;
after editing a `.lean` file, run `lake build` again.

## Practice

Each page includes the question, mathematical proof, Lean code, and something to try.

1. [Segment reversal](data/01_segment_reversal.md)
2. [Midpoint symmetry](data/02_midpoint_symmetry.md)
3. [Squared-distance symmetry](data/03_distance_symmetry.md)
4. [Horizontal segments](data/04_horizontal_distance.md)
5. [Pythagorean identity](data/05_pythagorean.md)
6. [Nonnegative distance and a false stronger claim](data/06_nonnegative_distance.md)

The `.lean` files in [EuclideanProof/](EuclideanProof/) are the executable
solutions. Practice 6 also includes a [deliberately invalid proof](examples/expected_failure/StrictDistance.lean):
it fails as expected and is excluded from the normal build.

## Demonstration notebook

The [single notebook](notebooks/lean_geometry_demo.ipynb) shows all six proofs,
Lean checker calls, and saved results, including the expected failure.
To rerun it, use Python 3.10+ after completing the Lean setup:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m jupyterlab
```

Open the notebook and run its cells in order. On Windows PowerShell, activate
with `.venv\Scripts\Activate.ps1`. Python is only needed for the notebook.

## Learning resources

- [Theorem Proving in Lean 4](https://lean-lang.org/theorem_proving_in_lean4/)
- [Mathematics in Lean](https://leanprover-community.github.io/mathematics_in_lean/)
