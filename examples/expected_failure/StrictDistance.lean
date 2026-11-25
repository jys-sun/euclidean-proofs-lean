import EuclideanProof.NonnegativeDistance

open EuclideanProof

-- DELIBERATELY INVALID: nonnegative does not imply strictly positive.
-- This file is checked explicitly by the demonstration notebook and is
-- not imported by the library, so `lake build` remains successful.
example (A B : Point) : 0 < sqDist A B := by
  -- This theorem proves 0 ≤ sqDist A B, which does not meet the goal 0 < ... .
  exact sqDist_nonneg A B
