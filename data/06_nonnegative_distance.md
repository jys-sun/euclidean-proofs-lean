# Practice 6: A true inequality and a false stronger claim

A small change from “at least zero” to “greater than zero” makes a real difference. Let's prove the first claim, try the stronger one, and look at why Lean asks us for more.

## Question

Let $A=(a_x,a_y)$ and $B=(b_x,b_y)$ be arbitrary points in $\mathbb{R}^2$.
With squared distance defined by

$$
D(A,B)=(b_x-a_x)^2+(b_y-a_y)^2,
$$
prove the inequality $D(A,B)\ge 0$. Can we strengthen it to $D(A,B)>0$
without adding an assumption?

## Assumptions and model

Points are arbitrary real coordinate pairs, including coincident points.
`D` in the mathematical notation is `sqDist` in Lean. No distinctness assumption
is present. `≤` means nonnegative here; `<` means strictly positive.

## Mathematical proof

Every real square is nonnegative:

$$
(b_x-a_x)^2\ge 0,\qquad (b_y-a_y)^2\ge 0.
$$
Adding these inequalities yields

$$
D(A,B)=(b_x-a_x)^2+(b_y-a_y)^2\ge 0+0=0.
$$
In Lean, we write this conclusion as `0 ≤ sqDist A B`. Unlike `ring`, which
checks polynomial equalities, this proof uses order lemmas: `sq_nonneg` and
`add_nonneg`. `exact` supplies a proof whose type must match the current goal.

## Lean proof code

Here is the matching [Lean source](../EuclideanProof/NonnegativeDistance.lean).

```lean
import EuclideanProof.Basic

namespace EuclideanProof

/-- Squared distance is a sum of two nonnegative squares. -/
theorem sqDist_nonneg (A B : Point) : 0 ≤ sqDist A B := by
  unfold sqDist
  -- `sq_nonneg t` proves 0 ≤ t²; `add_nonneg` adds two such inequalities.
  exact add_nonneg (sq_nonneg (B.1 - A.1)) (sq_nonneg (B.2 - A.2))

/-- Coincident endpoints give a counterexample to unconditional positivity. -/
theorem sqDist_self (A : Point) : sqDist A A = 0 := by
  simp [sqDist]

/-- Formally refute the assertion that every squared distance is positive. -/
theorem not_always_sqDist_pos : ¬ (∀ A B : Point, 0 < sqDist A B) := by
  -- Suppose the universal strict inequality were true.
  intro h
  -- It would hold for the origin paired with itself.
  have impossible := h (0, 0) (0, 0)
  -- But its squared distance is zero, so this would assert 0 < 0.
  simp [sqDist] at impossible

end EuclideanProof
```

## How the proofs correspond

| Mathematical reasoning | Lean code and its role |
| --- | --- |
| Expand the squared-distance formula. | `unfold sqDist` |
| Each real square is nonnegative. | `sq_nonneg (B.1 - A.1)` and `sq_nonneg (B.2 - A.2)` |
| A sum of two nonnegative quantities is nonnegative. | `add_nonneg` combines the two proofs; `exact` closes the goal. |
| Coincident points have squared distance zero. | `simp [sqDist]` proves `sqDist_self`. |
| A universal strict inequality would apply to the origin paired with itself. | `intro h` followed by `h (0, 0) (0, 0)` |
| The resulting claim that zero is strictly less than zero is impossible. | `simp [sqDist] at impossible` proves the negation. |

## Counterexample to strict positivity

The stronger claim $D(A,B)>0$ for **all** $A,B$ is false.
A single case where a claim fails is enough to disprove it; this is called a
**counterexample**. We can find one without leaving the origin.
Take $A=B=(0,0)$. Then

$$
D(A,A)=(0-0)^2+(0-0)^2=0,
$$
so the proposed conclusion would be $0>0$, a contradiction.
Thus

$$
\neg\bigl(\forall A,B\in\mathbb{R}^2,\;D(A,B)>0\bigr).
$$
The Lean theorem `sqDist_self` proves the zero-distance calculation, and
`not_always_sqDist_pos` formally proves this negation. `intro h` assumes the
universal claim; applying `h` to the origin twice gives the contradiction.
A strictly positive result needs a further assumption, such as $A\ne B$.

## A deliberately failed Lean proof

The invalid attempt below passes a proof of $0\le D(A,B)$ to a goal
requiring $0<D(A,B)$. Lean reports a **type mismatch**: the weak inequality
is not a proof of the strict inequality.

It's worth keeping two things separate here. Lean rejecting an argument
doesn't, by itself, mean the statement is false. We might just need a different
proof of a true statement. Here the separate
counterexample above, also checked in Lean, establishes that the universal
strict inequality is false.

The invalid file is intentionally outside the library imports, so normal
`lake build` checks the valid practice problems and succeeds. The notebook checks this
file separately, displays the compiler diagnostics, and catches the expected
failure. It still raises if the invalid file unexpectedly passes or if the
failure is unrelated to this proof mismatch.

[Expected-failure source](../examples/expected_failure/StrictDistance.lean):

```lean
import EuclideanProof.NonnegativeDistance

open EuclideanProof

-- DELIBERATELY INVALID: nonnegative does not imply strictly positive.
-- This file is checked explicitly by the demonstration notebook and is
-- not imported by the library, so `lake build` remains successful.
example (A B : Point) : 0 < sqDist A B := by
  -- This theorem proves 0 ≤ sqDist A B, which does not meet the goal 0 < ... .
  exact sqDist_nonneg A B
```

## Run the examples

From the repository root:

```bash
lake build
lake env lean EuclideanProof/NonnegativeDistance.lean
# This command is supposed to fail with a type mismatch and a nonzero exit code:
lake env lean examples/expected_failure/StrictDistance.lean
```

The [shared demonstration notebook](../notebooks/lean_geometry_demo.ipynb)
includes saved outputs for both the successful inequality proof and the expected
failure, together with the explanation and formal counterexample.

## Something to try

Prove that $A
e B$ implies $0<D(A,B)$. Explain which step requires the
new assumption and why `sq_nonneg` alone cannot prove strict positivity.
Keep your working theorem in a separate Lean file until it is complete.
