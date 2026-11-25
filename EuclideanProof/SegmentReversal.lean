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
