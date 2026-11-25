# Practice 4: Squared distance along a horizontal line

When two points have the same height, the vertical part of their distance disappears. The interesting part here is seeing exactly where Lean uses that assumption.

## Question

Let $A=(a_x,a_y)$ and $B=(b_x,b_y)$ satisfy $a_y=b_y$.
Using the squared-distance formula

$$
D(A,B)=(b_x-a_x)^2+(b_y-a_y)^2,
$$
prove that $D(A,B)=(b_x-a_x)^2$. The function $D$ is named `sqDist` in Lean.

## Assumptions and model

Points are pairs of real numbers: `Point := ℝ × ℝ`. The notation `A.1`
means the x-coordinate and `A.2` means the y-coordinate. Squared distance is
an explicitly defined algebraic function; it avoids square roots. Any additional
hypotheses appear in the question and in the Lean theorem's parameters.

## A concrete example

For A = (1, 3), B = (5, 3), the squared distance is (5 − 1)² = 16. Distinct endpoints are not required.

## Hints

1. Expand sqDist.
2. Rewrite with the hypothesis h.
3. Simplify the zero vertical contribution.

## Mathematical proof

The hypothesis $a_y=b_y$ implies

$$
b_y-a_y=b_y-b_y=0.
$$
Substitute this into the squared-distance formula:

$$
\begin{aligned}
D(A,B)
&=(b_x-a_x)^2+(b_y-a_y)^2\\
&=(b_x-a_x)^2+(b_y-b_y)^2\\
&=(b_x-a_x)^2+0^2\\
&=(b_x-a_x)^2.
\end{aligned}
$$
The assumption is used in the second line; the remaining steps are algebra.

## Lean proof code

Here is the matching [Lean source](../EuclideanProof/HorizontalDistance.lean).
`Point`, `midpoint`, and `sqDist` are defined in [Basic.lean](../EuclideanProof/Basic.lean).

```lean
import EuclideanProof.Basic

namespace EuclideanProof

/-- Equal y-coordinates make the vertical contribution to squared distance zero. -/
theorem horizontal_sqDist (A B : Point) (h : A.2 = B.2) :
    sqDist A B = (B.1 - A.1) ^ 2 := by
  -- The named hypothesis `h` is a premise, not something we prove here.
  unfold sqDist
  -- Replace A.y with B.y using h.
  rw [h]
  -- B.y - B.y = 0, 0² = 0, and t + 0 = t.
  simp

end EuclideanProof
```

## How the proofs correspond

| Mathematical reasoning | Lean code and its role |
| --- | --- |
| Assume the two y-coordinates are equal. | `(h : A.2 = B.2)` |
| Write sqDist(A,B) = (B.x − A.x)² + (B.y − A.y)². | `unfold sqDist` |
| Substitute B.y for A.y using the assumption. | `rw [h]` |
| Since B.y − B.y = 0, its square vanishes and adding zero changes nothing. | `simp` |

## Reading the Lean proof

`(h : A.2 = B.2)` names the hypothesis h. `unfold sqDist` exposes its formula. `rw [h]` rewrites A.y as B.y. `simp` uses elementary rules such as t − t = 0, 0² = 0, and t + 0 = t. A proof establishes the conclusion under its stated assumptions; it does not establish the assumptions themselves.

- [Lean solution](../EuclideanProof/HorizontalDistance.lean)
- [Shared demonstration notebook](../notebooks/lean_geometry_demo.ipynb)
- [Shared definitions](../EuclideanProof/Basic.lean)

## Something to try

Write a new example with the hypothesis `h : A.1 = B.1`. Prove that a vertical segment has squared distance `(B.2 - A.2) ^ 2`, using the same pattern.

When you want to try a change, save it to `EuclideanProof/HorizontalDistance.lean` and run this from the
repository root:

```bash
lake build
lake env lean EuclideanProof/HorizontalDistance.lean
```

`lake build` refreshes imported definitions too. The second command checks this
individual saved practice. You can run both commands directly in a terminal.
The Markdown code block shows the supplied solution; it will not change
automatically when you experiment with the `.lean` file.
