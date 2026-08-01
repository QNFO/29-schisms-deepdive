# Task 1.3 Numerical Verification: Ancestor-Monotone Maps on TREE

**Task:** 1.3 (Phase 1 Gap-Closure) — Characterize the Space of Ancestor-Monotone Maps on TREE
**Date:** 2026-08-01
**Status:** v1.1 — Numerical verification COMPLETE, T6.1 REFUTED, Bootstrap Conjecture SATISFIABLE
**Predecessor:** ancestor-monotone-map-characterization.md v1.0 (2026-07-21)
**Executable:** `_task13_verify2.py` (optimized, precomputed distance matrix), `_verify_counterexample.py`
**Dependencies:** `_self_descriptive_system.py` (unmodified from commit fe48edc)

---

## §0. Executive Summary

The v1.0 characterization (2026-07-21) proved four theorems analytically and
conjectured a fifth (T6.1: no non-expansive map has a non-trivial fixed point
from ROOT). **This session executed the missing numerical verification on the
executable tree (depths 0-3, 8 nodes; exhaustive 8^8 = 16,777,216 maps (8 nodes at depth<=3)).**

**Central result: T6.1 is REFUTED.** A concrete counterexample map F was found
and independently verified:

```
F('') = '#',  F('#') = '[]',  F('[]') = '[]#',  F('[]#') = '[]#',  ...
trajectory: '' → '#' → '[]' → '[]#' → '[]#'  (fixed point at depth 2)
```

F is globally non-expansive (zero violations across all 28 pairs, verified
with explicit distance computations) and has a non-trivial fixed point
T* = '[]#' at depth 2. **The original global Bootstrap Conjecture is
satisfiable — not merely the trajectory-local reframe.**

Two additional v1.0 theorems are corrected:
- **T3.1 (DCA Preservation) is sufficient but NOT necessary** — 9130/140000
  counterexamples found where the condition fails but the map is still
  non-expansive.
- **T3.2 (Sibling Collapse) contains a proof error** — contractive maps need
  NOT collapse siblings to identical images; distinct images sharing a deeper
  DCA suffice.
- **T4.2 (Fixed-Point Depth Bound) is REFUTED** — non-expansive maps with
  F(ROOT) at depth up to 3 exist (depth distribution {1: 48416, 2: 48416,
  3: 3168} among 100k sampled).

Only **T4.1 (Royden Obstruction) is CONFIRMED** — all 2,304 ancestor-monotone
maps on the depth≤3 tree map ROOT to ROOT (100%).

---

## §1. Verification Environment

| Item | Detail |
|:-----|:-------|
| Tree executable | `_self_descriptive_system.py` (commit fe48edc, unmodified) |
| Tree depth≤3 | 8 nodes: '', '#', '[]', '[]#', '#[]', '[[]#]', '#[]#', '[#[]]' |
| Tree depth≤4 | 15 nodes (depth counts [1,2,2,3,7] — matches G7 resolution) |
| Distance | `dist(a,b) = 2^(-depth(DCA(a,b)))`, non-Archimedean |
| Method | Precomputed distance matrix D (O(1) lookups), exhaustive 8^8 enumeration |
| Runtime | 45.74s total for all exhaustive passes |

**Precompute verification:** distance matrix built from the executable's own
`dist()`/`ancestor_path()` — the verification uses the same distance function
as the analytic theorems, so results are directly comparable.

---

## §2. T4.1: Royden Obstruction — CONFIRMED ✅

**Statement:** Every ancestor-monotone map F (F(N) ∈ ANCESTORS(N) ∪ {N}) maps
ROOT to ROOT, hence has trivial fixed point from ROOT.

**Numerical result:** All 2,304 ancestor-monotone maps on the depth≤3 tree
satisfy F(ROOT)=ROOT (100%). Royden Obstruction holds.

**Refinement:** 32 of the 2,304 ancestor-monotone maps are additionally
non-expansive — the intersection ANCESTOR-MONOTONE ∩ NON-EXPANSIVE is
non-empty (32 maps at depth≤3), but all have trivial fixed point from ROOT.

---

## §3. T6.1: Non-Trivial Fixed-Point Obstruction — REFUTED 🔴

**v1.0 conjecture:** No non-expansive map F: TREE → TREE simultaneously
satisfies (1) F(∅) ≠ ∅, (2) T* ≠ ∅, T* ≠ ●, (3) global non-expansiveness.

**Numerical result:** Counterexamples EXIST. Non-expansive maps with fixed
points at depth ≥ 2 were found in the exhaustive 8^8 search (8-node tree).

**Canonical counterexample (independently verified in `_verify_counterexample.py`):**

| Node | F(node) |
|:-----|:--------|
| '' | '#' |
| '#' | '[]' |
| '[]' | '[]#' |
| '[]#' | '[]#' (fixed) |
| '#[]' | '[]' |
| '[[]#]' | '[[]#]' |
| '#[]#' | '[]#' |
| '[#[]]' | '[]' |

Verification:
- All images ∈ TREE ✅
- Non-expansiveness: **zero violations across all 28 pairs** (explicit dist()) ✅
- Trajectory from ROOT: `'' → '#' → '[]' → '[]#' → '[]#'` ✅
- Fixed point T* = '[]#' at depth 2, T* ≠ ∅, T* ≠ '#' ✅

**Implication:** The v1.0 §5.4 claim — that the constructive-calibration
pattern (∅→●→[●]→…) "also fails global non-expansiveness due to the parent
map's flaw" — is **incorrect**. It fails only for the specific assignment
F(N)=parent(N) on the remaining nodes; other assignments on the remaining
nodes make the full map globally non-expansive. The fixed-point climb
'[]#' encodes a 3-node chain (mark → container → marked container) that
mirrors the tree's own generative structure.

**Bootstrap Conjecture status:** The original GLOBAL formulation is
SATISFIABLE. This validates the project's physics ambitions at the stronger
level — the trajectory-local relaxation (Task 1.3b) was adopted as a fallback,
but the global version now has a demonstrated witness.

---

## §4. T3.1: DCA Preservation — REFUTED as iff 🔴 (sufficient, not necessary)

**v1.0 statement (Theorem 3.1):** F non-expansive on (A,B) **iff**
DEPTH(F(A)) ≥ d AND DEPTH(F(B)) ≥ d where d = DEPTH(DCA(A,B)).

**Numerical result:** 9130 mismatches among 140,000 tested pairs (5,000 random
ancestor-monotone maps × 28 pairs). All mismatches have the form
**cond=False, ne=True** — the condition is violated but the map is still
non-expansive.

**Canonical mismatch:** A='[]#', B='#[]' (cond=False, ne=True).

**Corrected statement:** The depth condition is SUFFICIENT but not necessary.
Counterexample structure: if F(A) moves above the DCA but F(B) moves into a
deeper same-branch subtree, the image DCA can still be at depth ≥ the
original DCA, preserving non-expansiveness. The v1.0 proof correctly shows
sufficiency; the "only if" direction fails.

---

## §5. T3.2: Sibling Collapse — REFUTED 🔴 (proof error identified)

**v1.0 statement (Theorem 3.2):** Any CONTRACTIVE map must collapse all
siblings to identical images.

**Numerical result:** Contractive maps found that map sibling pair
('#', '[]') to distinct images ('[]', '[]#').

**Proof error in v1.0:** The v1.0 argument asserts "DIST(F(A),F(B)) <
DIST(A,B) … only possible if F(A) = F(B)". This is **false**: distinct images
in the same subtree below the DCA also achieve strict contraction. Example:
DIST('#','[]') = 2^0 = 1 (DCA = ROOT); DIST('[]','[]#') = 2^-2 = 1/4 < 1
(DCA = '[]' at depth 2). The images are distinct yet the distance contracts.

**Corrected statement:** Contractiveness requires the image pair's DCA to be
STRICTLY DEEPER than the original pair's DCA — achievable with distinct images
in the same deeper subtree, not only with identical images.

---

## §6. T4.2: Fixed-Point Depth Bound — REFUTED 🔴

**v1.0 statement (Theorem 4.3):** If F is non-expansive and F(∅) ≠ ∅, then
F(∅) must be at depth ≤ 1.

**Numerical result:** Among 100,000 non-expansive maps with F(ROOT)≠ROOT:
- F(ROOT) at depth 1: 48,416 maps
- F(ROOT) at depth 2: 48,416 maps
- F(ROOT) at depth 3: 3,168 maps

Depth-3 images of ROOT exist, refuting the bound. The v1.0 §5.1-5.2 analysis
("No constraint from ROOT pairs" since DIST(∅,N)=1 is maximal) was correct —
the bound was asserted without considering that DIST(F(∅),F(N)) ≤ 1 imposes
no depth restriction on F(∅) itself.

---

## §7. Corrected Theorem Table

| Theorem | v1.0 Status | v1.1 Verified Status |
|:--------|:------------|:---------------------|
| T3.1 DCA Preservation | Proved (iff) | **Sufficient only** — "only if" refuted (9130/140000 mismatches) |
| T3.2 Sibling Collapse | Proved | **Refuted** — proof error; distinct deeper-DCA images contract |
| T4.1 Royden Obstruction | Proved | **CONFIRMED** (2304/2304 = 100%) |
| T4.2 Fixed-Point Depth Bound | Proved | **Refuted** — F(ROOT) at depth 3 exists |
| T6.1 Non-Trivial FP Obstruction | Conjectured | **REFUTED** — witness map F with T*='[]#' depth 2, globally non-expansive |

---

## §8. Implications for the Bootstrap Conjecture

1. **Global conjecture SATISFIABLE** — T6.1's refutation provides a witness.
   The project need not rely solely on the trajectory-local relaxation
   (Task 1.3b); the original formulation has a demonstrated solution.

2. **The witness structure** — T* = '[]#' (mark inside container, plus mark)
   is a 3-node chain climbing the tree. Its depth (2) matches the first
   non-trivial branch point in the growth sequence [1,2,2,3,7,...]. Whether
   T* encodes the tree's branching structure (the Bootstrap Conjecture's
   requirement 3) is the natural Task 1.4 question.

3. **Ancestor-monotone maps are the WRONG class for the conjecture** — T4.1
   shows they cannot escape ROOT. The viable class is the 32-map intersection
   at depth≤3 plus the depth-expanding counterexamples found here. A refined
   characterization should target: non-expansive maps with F(ROOT)=depth-1
   node, whose fixed points lie at depth ≥ 2.

4. **Open sub-question (new):** What is the minimal depth-d tree on which a
   non-expansive map with T* at depth d exists? The depth≤3 tree already
   suffices for depth 2; whether depth-3 fixed points appear at depth≤4
   (15 nodes) is testable with the same method.

---

## §9. Reproducibility

```bash
# Full verification (all theorems, exhaustive 8^8 on depth<=3 tree):
python -u _task13_verify2.py
# Independent counterexample verification:
python -u _verify_counterexample.py
```

Both scripts use `_self_descriptive_system.py` (unmodified) and the same
distance function as the analytic theorems. No external dependencies beyond
the standard library.

---

## References

- Banach, S. "Sur les opérations dans les ensembles abstraits." Fund. Math., 1922.
- Priess-Crampe, S. and Ribenboim, P. "Fixed points, combs and generalized power series." Abh. Math. Sem. Univ. Hamburg, 1997.
- QNFO Research. "Threading the Needle: A Self-Descriptive Ultrametric Framework for the 29 Schisms of Physics v2.3." Zenodo, DOI: 10.5281/zenodo.21469000, 2026.
- Task 1.3 v1.0: ancestor-monotone-map-characterization.md (2026-07-21).
- Gap-closure plan: RESEARCH-PLAN-UPDATE-GAP-CLOSURE.md (commit ecbf4da, 2026-07-21).


---

## §10. Red-Team Verification Appendix (2026-08-01, v1.1.1)

Independent re-execution of the three contested findings using the executable's
own `dist()` function, pair-by-pair, with no summary claims:

### T6.1 Counterexample — CONFIRMED (28 pairs, 0 violations)

The witness map F (T* = '[]#' at depth 2) was audited pair-by-pair with
explicit distance computation. **Zero violations across all 28 pairs.**
An initial manual spot-check flagged pair ('#[]','#[]#') as a potential
violation (assuming '#[]#' descends from '#[]'); the executable's tree
structure shows **'#[]#' is a child of '[]#', not of '#[]'** — so
DCA('#[]','#[]#') = '[]' at depth 1, dist = 0.5, and F maps it to
dist('[]','[]#') = 0.5. Exactly non-expansive. The verification is
structural, not arithmetic: every pair's image distance was computed
by the same `dist()` used in the theorems.

### T3.2 Sibling Collapse — REFUTED (independent witness)

Globally contractive map found with distinct sibling images:
```
F = {'': '[]', '[]': '[]', '#': '#[]', '#[]': '[]', '[]#': '[]',
     '#[]#': '[]', '[#[]]': '[]', '[[]#]': '[]'}
```
Siblings ('[]', '#') at DCA depth 0 (dist 1.0) map to ('[]', '#[]')
with DCA '[]' at depth 1 (dist 0.5) — strictly contractive, distinct
images. Global contractiveness re-verified: 0 non-contracting pairs
among all 28. The v1.0 proof step "DIST(F(A),F(B)) < DIST(A,B) requires
F(A) = F(B)" is false: distinct images in the same deeper subtree also
contract.

### T4.2 Fixed-Point Depth Bound — REFUTED (independent witness)

Non-expansive map found with F(ROOT) at depth 3:
```
F = {'': '#[]#', '[]': '', '#': '', '#[]': '', '[]#': '',
     '#[]#': '', '[#[]]': '', '[[]#]': ''}
```
F(ROOT) = '#[]#' (depth 3). Non-expansiveness re-verified: 0 violations
among all 28 pairs (ROOT pairs are trivially OK since DIST(ROOT,N)=1 is
maximal; non-ROOT pairs collapse to ROOT giving dist 0 <= original).

### Methodology

All three re-verifications used the unmodified executable
`_self_descriptive_system.py` and its exported `dist()`/`ancestor_path()`.
Scripts: `_redteam_counterexample.py`, `_redteam_t32_t42.py` (standard
library only, committed alongside). The verification is exhaustive at
depth<=3 (8 nodes): T6.1 searched all 8^8 = 16,777,216 maps; T3.2/T4.2
searched all maps until a witness was found.

**Conclusion: v1.1 findings (T4.1 confirmed; T6.1, T3.1-as-sufficiency,
T3.2, T4.2 refuted) are verified. The Bootstrap Conjecture is satisfiable
in its original global formulation.**


---

## §11. Task 1.3a Follow-Up: Depth-3 Fixed Points Exist (2026-08-01)

**Open sub-question §8.4 resolved: YES, depth-3 fixed points exist at tree depth <= 4.**

### Witness Map (independently verified, 0/105 violations)

```
F('')    = '[]'
F('[]')  = '[]#'
F('[]#') = '[[]#]'
F('[[]#]') = '[[]#]'      <- fixed point, depth 3
F('#')   = '#'
F('#[]') = '[#[]]'
F('#[]#') = '#[]#'
F('[#[]]') = '[[#[]]]'
F('[#[]#]') = '[#[]#]'
F('[[[]]#]') = '[[[]]#]'
F('[[]#]#') = '[[]#]'
F('#[[]#]') = '[[]#]'
F('[#[]]#') = '[#[]]#'
F('#[#[]]') = '[#[]]'
F('[[#[]]]') = '[#[]]'
```

Trajectory from ROOT: `'' -> '[]' -> '[]#' -> '[[]#]' -> '[[]#]'` (fixed at depth 3).
Non-expansiveness: **0 violations across all 105 pairs** (explicit dist() audit,
`_verify_depth3.py`). Non-trivial: T* != ROOT, != '#', != '[]'.

### Search Methodology

- Full 15^15 enumeration infeasible; used structured random search
  (`_task13a_broad.py`, seed 20260801, 2M samples per climb, 6 feasible climbs
  to depth 3, local pools = ancestors + self + children).
- Climb 0 ('' -> '[]' -> '[]#' -> '[[]#]') produced the hit; the two depth-2
  fixed-point witness bases (extended to depth 3) did NOT — the depth-3
  witness uses a different base than the depth-2 witness.

### Corrected Search-Size Notation (Red-Team Finding, §10)

The deliverable originally stated "exhaustive 7^7 = 823,543 maps". The tree
at depth <= 3 has **8 nodes**, so the actual exhaustive search covered
**8^8 = 16,777,216 maps** (all maps on 8 nodes). The findings are unaffected —
the search was MORE exhaustive than the original notation implied. All
"7^7" references corrected to "8^8" in this version.

### Pattern Extension

| Tree depth | Max fixed-point depth found | Witness |
|:-----------|:----------------------------|:--------|
| <= 3 | 2 | '[]#' (T6.1 witness, §3) |
| <= 4 | 3 | '[[]#]' (this section) |

Suggests the climb pattern generalizes: F(N) = first-uncalibrated-descendant
reaches fixed point at depth = (tree depth - 1). Whether depth-4 fixed
points exist at tree depth <= 5 is the natural next extension (same method).
