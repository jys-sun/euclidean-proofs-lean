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
