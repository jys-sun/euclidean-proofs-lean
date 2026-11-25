# Practice 5: A coordinate Pythagorean identity

The familiar Pythagorean identity is a good place to compare a short calculation with a short Lean proof. We'll use a triangle whose legs follow the coordinate axes, so we can see every term directly.

## Question

Let $O=(0,0)$, $H=(x,0)$, and $P=(x,y)$, where $x,y\in\mathbb{R}$.
With $D$ denoting squared distance (`sqDist` in Lean), prove

$$
D(O,P)=D(O,H)+D(H,P).
$$

## Assumptions and model

Points are pairs of real numbers: `Point := ℝ × ℝ`. The notation `A.1`
means the x-coordinate and `A.2` means the y-coordinate. Squared distance is
an explicitly defined algebraic function; it avoids square roots. Any additional
hypotheses appear in the question and in the Lean theorem's parameters.

## A concrete example

With x = 3 and y = 4, the identity becomes 25 = 9 + 16. We prove the axis-aligned squared-distance identity, not the general theorem about all right triangles.

## Hints

1. Draw the three points and label the horizontal and vertical legs.
2. Expand the three instances of sqDist.
3. Simplify the resulting polynomial with `ring`.

## Mathematical proof

Compute the three squared distances directly:

$$
\begin{aligned}
D(O,P)&=(x-0)^2+(y-0)^2=x^2+y^2,\\
D(O,H)&=(x-0)^2+(0-0)^2=x^2,\\
D(H,P)&=(x-x)^2+(y-0)^2=y^2.
\end{aligned}
$$
Consequently,

$$
D(O,P)=x^2+y^2=D(O,H)+D(H,P).
$$
The legs are parallel to the coordinate axes. This proves the identity for
these coordinates; it also holds when $x=0$ or $y=0$, when the triangle is degenerate.

## Lean proof code

Here is the matching [Lean source](../EuclideanProof/Pythagorean.lean).
`Point`, `midpoint`, and `sqDist` are defined in [Basic.lean](../EuclideanProof/Basic.lean).

```lean
import EuclideanProof.Basic

namespace EuclideanProof

/-- A right triangle with legs parallel to the coordinate axes. -/
theorem pythagorean_axis_aligned (x y : ℝ) :
    sqDist (0, 0) (x, y) =
      sqDist (0, 0) (x, 0) + sqDist (x, 0) (x, y) := by
  -- Expand squared distances and evaluate pair coordinates.
  dsimp [sqDist]
  -- The resulting identity is x² + y² = x² + y².
  ring

end EuclideanProof
```

## How the proofs correspond

| Mathematical reasoning | Lean code and its role |
| --- | --- |
| Let x and y be arbitrary real numbers, with O=(0,0), H=(x,0), P=(x,y). | `(x y : ℝ)` and the explicit coordinate pairs in the statement |
| Expand OP², OH², and HP² using the squared-distance formula. | `dsimp [sqDist]` |
| Compute OP²=x²+y², OH²=x², HP²=y²; hence OP²=OH²+HP². | `ring` simplifies the coordinate differences and verifies the resulting identity. |

## Reading the Lean proof

`(x y : ℝ)` universally quantifies over two real coordinates. `dsimp [sqDist]` unfolds the formula and computes the coordinates of the explicitly given pairs. `ring` finishes the algebra. Negative coordinates work too. If x or y is zero, this is a degenerate triangle; the identity remains true.

- [Lean solution](../EuclideanProof/Pythagorean.lean)
- [Shared demonstration notebook](../notebooks/lean_geometry_demo.ipynb)
- [Shared definitions](../EuclideanProof/Basic.lean)

## Something to try

Generalize the points to O=(a,b), H=(a+x,b), P=(a+x,b+y). State and prove the same squared-distance identity; unfolding and `ring` still work.

When you want to try a change, save it to `EuclideanProof/Pythagorean.lean` and run this from the
repository root:

```bash
lake build
lake env lean EuclideanProof/Pythagorean.lean
```

`lake build` refreshes imported definitions too. The second command checks this
individual saved practice. You can run both commands directly in a terminal.
The Markdown code block shows the supplied solution; it will not change
automatically when you experiment with the `.lean` file.
