import EuclideanProof.Basic

namespace EuclideanProof

/-- Squaring removes the sign change from reversing a segment. -/
theorem sqDist_symmetry (A B : Point) : sqDist A B = sqDist B A := by
  -- `dsimp` unfolds the definition, exposing a polynomial identity.
  dsimp [sqDist]
  -- `ring` checks equality by putting both polynomials in a normal form.
  ring

end EuclideanProof
