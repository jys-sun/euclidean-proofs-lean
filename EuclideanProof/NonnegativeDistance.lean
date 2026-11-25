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
