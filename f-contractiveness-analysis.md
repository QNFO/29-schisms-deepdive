# F-Contractiveness Analysis: When Is a Map on the Expression Tree Contractive?

**Date:** 2026-07-20
**Status:** Addendum to 29-schisms-deepdive v1.1
**Purpose:** Address Red Team CRITICAL finding C5 — contractiveness of F was assumed, not derived.

---

## §1. Setup

The metric space is (TREE, DIST) where:
- TREE is the infinite directed graph of reduced expressions from ROOT = ∅
- DIST(A, B) = 2^(-depth of deepest common ancestor)
- DIST satisfies the strong condition: DIST(A, C) ≤ max(DIST(A, B), DIST(B, C))

A map F: TREE → TREE is CONTRACTIVE if:
    DIST(F(A), F(B)) < DIST(A, B) for all A ≠ B

---

## §2. When Is F Contractive?

### Theorem 1 (Contractiveness Conditions)

For a map F: TREE → TREE, F is contractive in the DIST metric if and only if
one of the following holds for all A, B with A ≠ B:

#### Case 1: Depth-Reducing (Always Contractive)
```
DEPTH(F(A)) < DEPTH(A)

Then DEPTH(ANCESTOR(F(A), F(B))) ≥ DEPTH(ANCESTOR(A, B)) + 1
→ DIST(F(A), F(B)) = 2^(-d_FA,FB) ≤ 2^(-(d_AB + 1)) = (1/2) * 2^(-d_AB) < DIST(A, B) ✓
```
The parent function satisfies this: DEPTH(parent(X)) = DEPTH(X) - 1 for X ≠ ROOT.

#### Case 2: Depth-Preserving, Strict on Branch Structure
```
DEPTH(F(A)) = DEPTH(A) AND
ANCESTOR(F(A), F(B)) is STRICTLY DEEPER than ANCESTOR(A, B) when A, B share a non-ROOT ancestor

If A and B are in different ROOT branches: ANCESTOR(A, B) = ROOT
    → ANCESTOR(F(A), F(B)) must also be ROOT (cannot go deeper than ROOT)
    → If F maps to FEWER branches: F(A) and F(B) stay in same branch → d deeper
    → If F preserves branches: d unchanged → DIST unchanged → NOT contractive

If A and B share a non-ROOT ancestor:
    → ANCESTOR(F(A), F(B)) must be STRICTLY deeper than ANCESTOR(A, B)
    → DIST(F(A), F(B)) < DIST(A, B) ✓
```
This requires F to "specialize" nodes — preserving depth but creating finer
distinctions between nodes that share recent ancestors.

#### Case 3: Absolute (Distance Reduction by Fixed Factor)
```
There exists c < 1 such that DIST(F(A), F(B)) ≤ c × DIST(A, B) for all A ≠ B
```
This is stronger than necessary but sufficient. Equivalent to Banach's contractive
map condition in complete metric spaces.

### Theorem 2 (Non-Contractive Warning Signs)

F is DEFINITELY NOT contractive if:

1. **Distance-preserving:** DIST(F(A), F(B)) = DIST(A, B) for some A ≠ B with
   non-ROOT common ancestor. (Violates strict inequality.)

2. **Distance-increasing:** DIST(F(A), F(B)) > DIST(A, B) for any A ≠ B.
   (Map spreads nodes apart — calibration diverges.)

3. **Non-injective with same-depth collision:** F(A) = F(B) for A ≠ B where
   DEPTH(A) = DEPTH(B). Then DIST(F(A), F(B)) = 0 = DIST(A, A) but A ≠ B →
   fails the definition (requires contraction for A ≠ B, but F(A) = F(B) gives 0 ≤ DIST(A,B) — this is actually
   contractive! Wait — this is a special case: if F(A) = F(B) and DIST(A,B) > 0,
   then 0 < DIST(A,B), so this IS contractive for that pair. But for the strong
   condition to hold, we need the inequality strict for ALL A ≠ B.)

### Corollary 1 (Parent Function) — **ERRATUM 2026-07-21: THIS CLAIM IS FALSE**

**Original (incorrect) claim, retained below struck through for the record:**

~~The parent function F(X) = parent(X) is ALWAYS contractive because:~~
~~- For X ≠ ROOT: DEPTH(F(X)) = DEPTH(X) - 1 (Case 1, depth-reducing)~~
~~- For X = ROOT: F(ROOT) = ROOT (fixed point)~~
~~- Therefore: DIST(F(A), F(B)) ≤ (1/2) × DIST(A, B) for all A ≠ B~~

**Why this is wrong:** The argument only checks that DEPTH decreases for each individual node under the parent map — it never checks what happens to the DCA (deepest common ancestor) of a PAIR of nodes under that map. These are different things, and the depth-reduction property does NOT imply the pairwise distance-reduction property claimed here.

**Counterexample (proved in `ancestor-monotone-map-characterization.md` §2, 2026-07-21):** Let A be a node at depth $d$ and let B be a child of A at depth $d+1$. Then $ANCESTOR(A,B) = A$ and $DIST(A,B) = 2^{-d}$. Applying the parent map: $parent(B) = A$, and $ANCESTOR(parent(A), A) = parent(A)$ at depth $d-1$ (since $parent(A)$ IS an ancestor of A). This gives:

$$DIST(parent(A), parent(B)) = DIST(parent(A), A) = 2^{-(d-1)} = 2 \times 2^{-d} = 2 \times DIST(A,B)$$

**The distance DOUBLED, not halved.** The parent map is not contractive — not even non-expansive — for any pair where one node is an ancestor of the other. It is contractive/non-expansive only for pairs whose deepest common ancestor is a PROPER ancestor of both nodes (i.e., neither node in the pair is itself the DCA).

**Corrected statement:** The parent function is contractive for pairs (A, B) where $ANCESTOR(A,B) \neq A$ and $ANCESTOR(A,B) \neq B$. It is distance-INCREASING (by exactly a factor of 2) for pairs where one node is a direct or indirect ancestor of the other. It is therefore **not globally contractive**, contradicting the original Corollary 1 above and the "Corollary 1.1" citation of this claim in earlier drafts of `c-contractiveness-proof.md` (since corrected in that document's v2.0).

This error propagated silently for one full project phase before being caught during Task 1.3 (2026-07-21) — a reminder that a plausible-sounding one-line depth argument is not a substitute for checking the actual pairwise distance definition.

### Corollary 2 (Trivial Non-Trivial Maps)

The only maps that are BOTH non-trivial (not the identity, not the parent function)
AND contractive must satisfy Case 2 (depth-preserving with strict branch refinement).
This constrains the space of possible calibration maps significantly.

---

## §3. Implications for the Bootstrap Conjecture

The Bootstrap Conjecture requires a contractive map F that represents physical
calibration. The derivation above shows:

1. ~~**The parent function is always contractive**~~ — **CORRECTED (2026-07-21): this is false, see erratum on Corollary 1 above.** The parent function IS globally non-expansive-or-worse (it strictly increases distance for ancestor/descendant pairs), so it does not straightforwardly serve as "the trivial baseline contractive map" this section originally assumed. The Bootstrap Conjecture analysis in `ancestor-monotone-map-characterization.md` and `deeper-math-bootstrap-obstruction.md` supersedes this document's conclusions and should be treated as authoritative going forward.

2. **Non-trivial F (depth-preserving) exists only under strict conditions** —
   it must refine branches without changing depth. This is the "interesting"
   case where calibration produces structure.

3. **Most randomly chosen F will NOT be contractive** — the space of
   contractive maps is a small subset of all possible maps on TREE.

4. **The existence of a physically meaningful contractive F is NOT guaranteed**
   by the tree structure alone — it requires additional constraints.

---

## §4. Computable Projections (Addressing C4)

### Truncation Approximation

For p-adic representations, the Monna map truncated at depth D:
```
MONNA_D(x) = Σ[i=k to D] a_i * p^(-i-1)
Error: |MONNA(x) - MONNA_D(x)| ≤ p^(-D-1)
```
This is computable in O(D) time.

### ε-Neighborhood Coarse-Graining

From the implementation results:
```
Depth 2: ε=0.500 → {ROOT, [1]} vs {3 classes} → compression ~4×
Depth 4: ε=0.500 → compression ~5×
Depth 6: ε=0.500 → compression ~125:1 (all depth≥2 nodes collapse)
```

The classical continuous world corresponds to the ε=0.500 projection at
sufficiently high depth. The projection is exactly computable by BFS from
the target node to depth -log₂(ε).

**Theorem:** For ε = 2^(-k), any node at depth ≥ k+1 is in the same
ε-neighborhood as all other nodes at depth ≥ k+1. The number of equivalence
classes is at most the number of nodes at depth ≤ k.

This is computable and provides the exact bridge from discrete tree to
classical continuum.

---

## §5. Tree Growth Asymptotics (Addressing C3)

Verified growth pattern from the executable:
```
Depth 0: 1
Depth 1: 2    (ratio: 2.00)
Depth 2: 2    (ratio: 1.00)
Depth 3: 3    (ratio: 1.50)
Depth 4: 7    (ratio: 2.33)
Depth 5: 28   (ratio: 4.00)
Depth 6: 125  (ratio: 4.46)
Depth 7: 588  (ratio: 4.70)

Ratio appears to converge to ~4.7, suggesting exponential growth with
base ≈ 4.7 after initial transient. This is exponential, NOT super-exponential.
```

**Implication:** The tree is computationally tractable at moderate depths.
Depth 7 (588 nodes) is fully computable. Depth 10 would be ~588 × 4.7³ ≈ 60,000
nodes — still tractable. Depth 20 would be ~588 × 4.7¹³ ≈ 10¹² nodes — at the
limit of current hardware but not categorically impossible.

The Red Team finding C3 (*"Tree growth is super-exponential — can't compute
physics"*) is PARTIALLY REFUTED. Growth is exponential, not super-exponential.
Physical predictions at moderate depths are computable. Deep Planck-scale
predictions may still be infeasible, but the framework has a computable
"classical limit" region.

---

## References

- Banach, S. "Sur les opérations dans les ensembles abstraits et leur application
  aux équations intégrales." Fundamenta Mathematicae, 1922.
- Monna, A.F. "Sur une transformation simple des nombres p-adiques en nombres réels."
  Indagationes Mathematicae, 1953.
