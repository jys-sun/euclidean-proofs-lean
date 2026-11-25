import EuclideanProof.Basic

namespace EuclideanProof

/-- A segment's midpoint does not depend on which endpoint is named first. -/
theorem midpoint_symmetry (A B : Point) : midpoint A B = midpoint B A := by
  -- Unfold our definition, then use commutativity of addition in each coordinate.
  simp only [midpoint, add_comm]

end EuclideanProof
