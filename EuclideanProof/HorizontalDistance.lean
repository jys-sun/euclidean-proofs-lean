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
