# Practice 1: Reversing a segment

Reversing a segment is familiar on a drawing: the arrow points the other way. Here we'll write that observation in coordinates and see how Lean checks the two coordinates separately.

## Question

Let $A=(a_x,a_y)$ and $B=(b_x,b_y)$ be arbitrary points in $\mathbb{R}^2$.
Prove that reversing the segment negates its displacement:

$$
B-A=-(A-B).
$$

## Assumptions and model

Points are pairs of real numbers: `Point := ℝ × ℝ`. The notation `A.1`
means the x-coordinate and `A.2` means the y-coordinate. Squared distance is
an explicitly defined algebraic function; it avoids square roots. Any additional
hypotheses appear in the question and in the Lean theorem's parameters.

## A concrete example

Try the coordinates A = (1, 2), B = (4, 6). The forward displacement is (3, 4); the reverse displacement is (−3, −4).

## Hints

1. Write the two scalar equalities on paper.
2. Split equality of pairs with `apply Prod.ext`.
3. Use `ring` for each coordinate.

## Mathematical proof

For the first coordinate, expand the negation:

$$
-(a_x-b_x)=-a_x+b_x=b_x-a_x.
$$
Likewise, for the second coordinate,

$$
-(a_y-b_y)=b_y-a_y.
$$
Therefore the two coordinate pairs agree:

$$
\begin{aligned}
B-A&=(b_x-a_x,\,b_y-a_y)\\
&=\bigl(-(a_x-b_x),\,-(a_y-b_y)\bigr)\\
&=-(A-B).
\end{aligned}
$$

## Lean proof code

Here is the matching [Lean source](../EuclideanProof/SegmentReversal.lean).
`Point`, `midpoint`, and `sqDist` are defined in [Basic.lean](../EuclideanProof/Basic.lean).

```lean
import EuclideanProof.Basic

namespace EuclideanProof

/-- Reversing a segment negates each coordinate displacement. -/
theorem segment_reversal (A B : Point) :
    (B.1 - A.1, B.2 - A.2) = (-(A.1 - B.1), -(A.2 - B.2)) := by
  -- Equality of pairs reduces to equality of their two coordinates.
  apply Prod.ext
  · -- First goal: B.x - A.x = -(A.x - B.x).
    ring
  · -- Second goal: the same calculation for y.
    ring

end EuclideanProof
```

## How the proofs correspond

| Mathematical reasoning | Lean code and its role |
| --- | --- |
| Let A and B be arbitrary real coordinate pairs. | `(A B : Point)` |
| To show two pairs are equal, compare their x- and y-coordinates. | `apply Prod.ext` |
| For x: B.x − A.x = −(A.x − B.x), by expanding the minus sign. | First `·` goal, solved by `ring` |
| For y: B.y − A.y = −(A.y − B.y), by the same calculation. | Second `·` goal, solved by `ring` |

## Reading the Lean proof

`(A B : Point)` means the result holds for every pair of points. `:= by` starts a tactic proof. `apply Prod.ext` turns one equality of pairs into two coordinate goals. Each `·` starts a bullet for one goal. `ring` proves a polynomial identity over the real numbers.

- [Lean solution](../EuclideanProof/SegmentReversal.lean)
- [Shared demonstration notebook](../notebooks/lean_geometry_demo.ipynb)
- [Shared definitions](../EuclideanProof/Basic.lean)

## Something to try

In the Lean file, delete one `ring` line and rerun the check. Read the remaining goal in the error. Restore the line and check again.

When you want to try a change, save it to `EuclideanProof/SegmentReversal.lean` and run this from the
repository root:

```bash
lake build
lake env lean EuclideanProof/SegmentReversal.lean
```

`lake build` refreshes imported definitions too. The second command checks this
individual saved practice. You can run both commands directly in a terminal.
The Markdown code block shows the supplied solution; it will not change
automatically when you experiment with the `.lean` file.
