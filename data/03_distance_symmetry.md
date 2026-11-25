# Practice 3: Squared distance is symmetric

Swapping two points changes the signs of their coordinate differences, but it doesn't change their distance. Let's follow what happens when we square those differences, then compare the algebra with Lean's proof.

## Question

For $A=(a_x,a_y)$ and $B=(b_x,b_y)$, define squared distance by

$$
D(A,B)=(b_x-a_x)^2+(b_y-a_y)^2.
$$
Prove that $D(A,B)=D(B,A)$. The function $D$ is named `sqDist` in Lean.

## Assumptions and model

Points are pairs of real numbers: `Point := ℝ × ℝ`. The notation `A.1`
means the x-coordinate and `A.2` means the y-coordinate. Squared distance is
an explicitly defined algebraic function; it avoids square roots. Any additional
hypotheses appear in the question and in the Lean theorem's parameters.

## A concrete example

The squared distance between (1, 2) and (4, 6) is 3² + 4² = 25 in either order. Ordinary distance is 5.

## Hints

1. Expand the definition of sqDist.
2. Notice that reversing subtraction changes only its sign.
3. Use `dsimp [sqDist]` followed by `ring`.

## Mathematical proof

Each coordinate difference changes sign when the endpoints are reversed:

$$
b_x-a_x=-(a_x-b_x),\qquad b_y-a_y=-(a_y-b_y).
$$
Since $(-t)^2=t^2$ for every real number $t$,

$$
\begin{aligned}
D(A,B)
&=(b_x-a_x)^2+(b_y-a_y)^2\\
&=\bigl(-(a_x-b_x)\bigr)^2+\bigl(-(a_y-b_y)\bigr)^2\\
&=(a_x-b_x)^2+(a_y-b_y)^2\\
&=D(B,A).
\end{aligned}
$$

## Lean proof code

Here is the matching [Lean source](../EuclideanProof/DistanceSymmetry.lean).
`Point`, `midpoint`, and `sqDist` are defined in [Basic.lean](../EuclideanProof/Basic.lean).

```lean
import EuclideanProof.Basic

namespace EuclideanProof

/-- Squaring removes the sign change from reversing a segment. -/
theorem sqDist_symmetry (A B : Point) : sqDist A B = sqDist B A := by
  -- `dsimp` unfolds the definition, exposing a polynomial identity.
  dsimp [sqDist]
  -- `ring` checks equality by putting both polynomials in a normal form.
  ring

end EuclideanProof
```

## How the proofs correspond

| Mathematical reasoning | Lean code and its role |
| --- | --- |
| Expand both squared distances into sums of squared coordinate differences. | `dsimp [sqDist]` |
| Reversing each subtraction changes its sign; squaring removes that sign. | `ring` checks this algebraic identity for both coordinates. |
| The two sums of squared differences are equal. | The same `ring` closes the equality goal; it does not call the segment-reversal theorem. |

## Reading the Lean proof

`dsimp [sqDist]` unfolds our definition. It leaves a polynomial equality. `ring` normalizes each side and proves that they agree. This proof checks the same algebra as the informal argument, without invoking the earlier segment theorem.

- [Lean solution](../EuclideanProof/DistanceSymmetry.lean)
- [Shared demonstration notebook](../notebooks/lean_geometry_demo.ipynb)
- [Shared definitions](../EuclideanProof/Basic.lean)

## Something to try

Temporarily change just the first exponent in the definition of sqDist from 2 to 1. Run `lake build`: symmetry should fail. Restore the definition and rebuild before continuing.

When you want to try a change, save it to `EuclideanProof/DistanceSymmetry.lean` and run this from the
repository root:

```bash
lake build
lake env lean EuclideanProof/DistanceSymmetry.lean
```

`lake build` refreshes imported definitions too. The second command checks this
individual saved practice. You can run both commands directly in a terminal.
The Markdown code block shows the supplied solution; it will not change
automatically when you experiment with the `.lean` file.
