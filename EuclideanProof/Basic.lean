import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Ring

/-!
# Our coordinate plane

An ordered pair of real numbers is a point. `P.1` is its x-coordinate;
`P.2` is its y-coordinate. We use squared distance to avoid square roots.
These are coordinate definitions, not a synthetic geometry axiom system.
-/
namespace EuclideanProof

abbrev Point := ℝ × ℝ

-- Division on arbitrary reals is noncomputable: this is a mathematical
-- definition for proofs, not an executable numerical approximation.
noncomputable def midpoint (A B : Point) : Point :=
  ((A.1 + B.1) / 2, (A.2 + B.2) / 2)

def sqDist (A B : Point) : ℝ :=
  (B.1 - A.1) ^ 2 + (B.2 - A.2) ^ 2

end EuclideanProof
