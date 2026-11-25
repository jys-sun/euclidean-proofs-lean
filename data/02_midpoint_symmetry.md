# Practice 2: The midpoint is independent of endpoint order

A midpoint shouldn't depend on which endpoint we name first. This is a small example, but it's a useful place to see how an ordinary fact about addition becomes a Lean proof.

## Question

For $A=(a_x,a_y)$ and $B=(b_x,b_y)$, define their midpoint by

$$
M(A,B)=\left(\frac{a_x+b_x}{2},\frac{a_y+b_y}{2}\right).
$$
Prove that $M(A,B)=M(B,A)$.

## Assumptions and model

Points are pairs of real numbers: `Point := ℝ × ℝ`. The notation `A.1`
means the x-coordinate and `A.2` means the y-coordinate. Squared distance is
an explicitly defined algebraic function; it avoids square roots. Any additional
hypotheses appear in the question and in the Lean theorem's parameters.

## A concrete example

A = (0, 2) and B = (4, 6) have midpoint (2, 4), whichever endpoint is first.

## Hints

1. Open Basic.lean and read the definition of midpoint.
2. Both coordinates differ only in the order of addition.
3. Use `simp only [midpoint, add_comm]`.

## Mathematical proof

By commutativity of real addition,

$$
a_x+b_x=b_x+a_x,\qquad a_y+b_y=b_y+a_y.
$$
Substituting these equalities in the midpoint formula gives

$$
\begin{aligned}
M(A,B)
&=\left(\frac{a_x+b_x}{2},\frac{a_y+b_y}{2}\right)\\
&=\left(\frac{b_x+a_x}{2},\frac{b_y+a_y}{2}\right)\\
&=M(B,A).
\end{aligned}
$$

## Lean proof code

Here is the matching [Lean source](../EuclideanProof/MidpointSymmetry.lean).
`Point`, `midpoint`, and `sqDist` are defined in [Basic.lean](../EuclideanProof/Basic.lean).

```lean
import EuclideanProof.Basic

namespace EuclideanProof

/-- A segment's midpoint does not depend on which endpoint is named first. -/
theorem midpoint_symmetry (A B : Point) : midpoint A B = midpoint B A := by
  -- Unfold our definition, then use commutativity of addition in each coordinate.
  simp only [midpoint, add_comm]

end EuclideanProof
```

## How the proofs correspond

| Mathematical reasoning | Lean code and its role |
| --- | --- |
| Write each midpoint as the pair of coordinate averages. | `midpoint` in `simp only [midpoint, add_comm]` unfolds the definition. |
| Use A.x + B.x = B.x + A.x, and likewise for y. | `add_comm` supplies commutativity of addition. |
| The equal coordinate averages give equal midpoint pairs. | `simp only` completes both coordinate simplifications and the pair equality. |

## Reading the Lean proof

`midpoint` is a definition in Basic.lean. `simp only [midpoint, add_comm]` unfolds that definition and simplifies with the commutativity law for addition. The word `only` limits the simplification rules to the ones listed (plus basic computation). `simp` handles the pair components too.

- [Lean solution](../EuclideanProof/MidpointSymmetry.lean)
- [Shared demonstration notebook](../notebooks/lean_geometry_demo.ipynb)
- [Shared definitions](../EuclideanProof/Basic.lean)

## Something to try

Replace the proof with `unfold midpoint`, then `apply Prod.ext` and a `ring` bullet for each coordinate. Check this alternative proof.

When you want to try a change, save it to `EuclideanProof/MidpointSymmetry.lean` and run this from the
repository root:

```bash
lake build
lake env lean EuclideanProof/MidpointSymmetry.lean
```

`lake build` refreshes imported definitions too. The second command checks this
individual saved practice. You can run both commands directly in a terminal.
The Markdown code block shows the supplied solution; it will not change
automatically when you experiment with the `.lean` file.
