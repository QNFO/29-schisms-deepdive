# C-Contractiveness Proof: v2.0 (Red-Team Remediation)

**Phase 1, Task 1.2 — Bootstrap Conjecture Formal Proof**
**Date:** 2026-07-20 (v2.0 after red-team audit)
**Status:** v2.0 (addresses F-C1 through F-C5 from `red-team-audit-ctasks-2026-07-20.md`)
**Dependencies:** `calibration-map-c-definition.md` v2.0

---

## §0. What Changed (v1.0 → v2.0)

| v1.0 Finding | Issue | v2.0 Resolution |
|:-------------|:------|:----------------|
| **F-C1** | Lemma 2 Case (i) conflated DCA(D_A,D_B) with DCA(M_A,M_A) | Eliminated — C v2.0 uses ancestor search, no D_A/D_B construction needed |
| **F-C2** | Lemma 2 Case (ii) circular: internal compatibility → cross-node convergence | Eliminated — no C₃ to argue about. Contractiveness follows directly from ancestor mapping |
| **F-C3** | Lemma 3 assumed Bootstrap to prove Bootstrap | Eliminated — no branch-convergence lemma needed |
| **F-C4** | C* proof abandoned mid-argument, then claimed proved | Replaced with honest statement: C* has trivial fixed point ●; non-trivial T* is open |
| **F-C5** | Theorem 5 (C² contractive) labeled "proof sketch" | Replaced with Theorem 3 (idempotence): C² = C, trivially true under v2.0 definition |

**Core simplification:** C v2.0 is ancestor-monotone. Every claimed property flows directly from "C(N) is an ancestor of N." No complex lemmas needed.

---

## §1. The Space

(TREE, DIST) as defined in `29-schisms-formalization.md`:
- TREE: infinite directed graph of reduced normal-form expressions from ROOT = ∅
- DIST(A, B) = 2^(-DEPTH(ANCESTOR(A, B))), DIST(A, A) = 0
- Strong ultrametric: DIST(A, C) ≤ max(DIST(A, B), DIST(B, C))
- Complete metric space

---

## §2. The Calibration Map C (v2.0, Restated)

```
C(N) = deepest ancestor A of N such that A is "internally calibrated"

Internally calibrated means:
  - A = ∅, or
  - A = ●, or
  - A = [E₁...Eₙ] with n ≥ 1, rightmost non-empty M = Eₙ, and
    DEPTH(DCA_of_all(E₁,...,Eₙ₋₁, M)) ≥ DEPTH(A)
```

**Key structural property:** C(N) is always an ancestor of N (or N itself).
Therefore: DEPTH(C(N)) ≤ DEPTH(N) for all N.

---

## §3. Primary Theorems

### Theorem 1: C Is Well-Defined

For all N ∈ TREE, C(N) returns a unique value.

**Proof.** The ancestor chain of N has DEPTH(N) + 1 nodes (finite). The predicate `is_internally_calibrated` involves only DEPTH and DCA, both well-defined. ROOT is always calibrated. The search walks upward from N and returns the first calibrated ancestor encountered, which exists (at worst, ROOT). ∎

### Theorem 2: C Is Non-Expansive

For all A, B ∈ TREE:
```
DIST(C(A), C(B)) ≤ DIST(A, B)
```

**Proof.** C(A) is an ancestor of A; C(B) is an ancestor of B. Consider the ancestral paths:

Let P_A = [ROOT, ..., C(A), ..., A] (path from ROOT to A).
Let P_B = [ROOT, ..., C(B), ..., B] (path from ROOT to B).

The DCA of A and B is the deepest node appearing in both P_A and P_B. Since C(A) is on P_A (closer to ROOT than or equal to A) and C(B) is on P_B (closer to ROOT than or equal to B), any node in the intersection of P_A and P_B that is at or above A (or B) is ALSO at or above C(A) (or C(B)). Specifically:

```
DEPTH(ANCESTOR(C(A), C(B))) ≥ DEPTH(ANCESTOR(A, B))
```

Because: ANCESTOR(A, B) is on both P_A and P_B. Since C(A) is on P_A at depth ≤ DEPTH(A) and C(B) is on P_B at depth ≤ DEPTH(B), the common ancestor of C(A) and C(B) is at least as deep as the common ancestor of A and B (ancestral paths can only grow when moving toward ROOT, making intersection potentially shallower — but we need ≥, not ≤).

Wait, let me re-check this. If A and B share a deep ancestor X, and C(A) is shallower than A, C(A) might be ABOVE X on P_A, making the intersection of P_{C(A)} and P_{C(B)} shallower.

Corrected analysis:
- ANCESTOR(A, B) = X, at depth d_X.
- C(A) is at depth ≤ DEPTH(A). If DEPTH(C(A)) ≥ d_X (C(A) is at or below X on P_A), then X is also on P_{C(A)} (the path from ROOT to C(A) includes X). Similarly for C(B).
- If DEPTH(C(A)) < d_X (C(A) is ABOVE X), then X is NOT on P_{C(A)}, and the DCA of C(A) and C(B) may be shallower than X.

So non-expansiveness is NOT automatically guaranteed by ancestor mapping! It depends on WHERE on the path the calibrated ancestor lies.

**Counterexample possibility:** Let A and B be deep in the same subtree. C(A) might jump to a shallower ancestor (above their shared ancestor) if A fails calibration. Then DIST(C(A), C(B)) could be LARGER than DIST(A, B), violating non-expansiveness.

Let me construct a concrete counterexample...

Consider: A = [● ●] (container with two marks, not internally calibrated — DCA_of_all({●},{●}) = ●, DEPTH(●) = 1, DEPTH([● ●]) = ? depends on tree position). If DEPTH([● ●]) = 2 and DEPTH(●) = 1, then 1 < 2 → not calibrated. C(A) = parent(A). parent([● ●]) = ? Depends on how [● ●] was generated.

And B = some node deep in a different branch from A. If C(A) jumps shallower but C(B) stays deep, DIST could increase.

This means I need to either:
1. Prove that DCA depth never decreases under ancestor mapping, or
2. Acknowledge that non-expansiveness fails and characterize when it holds.

Let me think more carefully about the ancestor path argument.

ANCESTOR(A, B) is the deepest node on both P_A and P_B. Let this be X.

C(A) is on P_A. C(B) is on P_B. 

If C(A) is at or below X on P_A: then X is on the sub-path from ROOT to C(A). ✓
If C(A) is above X on P_A: then X is NOT on the sub-path from ROOT to C(A). ✗

So: if BOTH C(A) and C(B) are at or below X, then X is on both sub-paths, and DCA(C(A), C(B)) is at least X (could be deeper).

If EITHER C(A) or C(B) is above X, then X might not be on both sub-paths, and DCA could be shallower.

The key question: can C(A) be above ANCESTOR(A, B)?

C(A) is the deepest calibrated ancestor of A. ANCESTOR(A, B) is on P_A. If ANCESTOR(A, B) is internally calibrated, then C(A) is at or below ANCESTOR(A, B) (since C picks the deepest calibrated ancestor). If ANCESTOR(A, B) is NOT calibrated, then C(A) could be above it.

But wait — is ANCESTOR(A, B) necessarily calibrated? Not necessarily. If A and B share a common ancestor that is not internally calibrated, then the deepest calibrated ancestor of A could be above that shared ancestor.

So: **C is NOT guaranteed to be non-expansive.** The ancestor-based definition can increase distance when the shared ancestor of A and B fails internal calibration.

This means I need to characterize when non-expansiveness holds.

**When non-expansiveness holds:**
For all pairs A, B where ANCESTOR(A, B) is internally calibrated, DIST(C(A), C(B)) ≤ DIST(A, B).

**When it may fail:**
When ANCESTOR(A, B) is NOT internally calibrated, C could map at least one of A, B to a shallower ancestor, potentially decreasing DCA depth and increasing DIST.

Let me now state this honestly in the proof.

Actually, I realize I need to be more careful. Let me reconsider.

If C(A) is above ANCESTOR(A, B), then C(A) is an ancestor of ANCESTOR(A, B). Similarly for B. So both C(A) and C(B) are on paths that go through ANCESTOR(A, B) or above it.

If C(A) is above ANCESTOR(A, B), then the path to C(A) does NOT include ANCESTOR(A, B). So ANCESTOR(A, B) is NOT on P_{C(A)}. The intersection of P_{C(A)} and P_{C(B)} may be only above ANCESTOR(A, B), making the DCA shallower.

Example:
- A and B share ANCESTOR at depth 5.
- A is not calibrated at depth 5 — C(A) jumps to depth 2.
- B is calibrated at depth 5 — C(B) stays at depth 5.
- DCA(C(A), C(B)): C(A) at depth 2, C(B) at depth 5. Their DCA is at most depth 2.
- DIST(C(A), C(B)) = 2^(-≤2) ≥ 2^(-2) = 1/4
- DIST(A, B) = 2^(-5) = 1/32
- 1/4 > 1/32 → DIST INCREASED.

This IS a genuine counterexample to non-expansiveness. C is NOT always non-expansive.

OK so this is actually an important finding. The v2.0 ancestor-based definition has a real problem: it can increase distances when the shared ancestor fails calibration.

The way to fix this: instead of C picking the deepest calibrated ancestor, we need a different strategy. What if C maps ALL nodes by the same amount? Like a uniform depth reduction?

Actually, the simplest fix: C(N) = parent(N) always. This is globally contractive, well-defined, and has fixed point ROOT. But it's trivial.

The challenge is finding a map that is:
1. Non-trivial (doesn't just collapse everything to ROOT)
2. Well-defined
3. Non-expansive (at minimum)

These three constraints are in tension. Let me try yet another approach...

**C_v3(N) =** 
For each node N, compute "calibration depth" d(N) = the depth of the deepest calibrated ancestor of N. Then:

C(N) = the node at depth min(DEPTH(N), d(N) + 1) on the path from ROOT.

This ensures C(N) is always at depth ≤ d(N) + 1, and at depth ≤ DEPTH(N). For calibrated nodes (d(N) = DEPTH(N)), C(N) = the node at depth DEPTH(N) (i.e., N itself). For uncalibrated nodes, C(N) moves at most 1 step above the deepest calibrated ancestor.

This is a bit contrived. Let me think of something cleaner.

**C_v3(N) = parent^k(N)** where k is the smallest integer such that parent^k(N) is internally calibrated, OR k = DEPTH(N) if no non-ROOT calibrated ancestor exists.

This guarantees:
- C(N) is internally calibrated
- C(N) is at depth ≤ DEPTH(N)
- C(N) ≠ N only if N is not calibrated
- C(∅) = ∅

But it doesn't guarantee non-expansiveness, as the counterexample shows.

**The honest conclusion:** For the ancestor-based C to be non-expansive, we need the ADDITIONAL property that internal calibration is monotone downward — i.e., if a node is internally calibrated, all its ancestors are too. This way, when C jumps to an ancestor, it stays within the calibrated region, and DCA depth is preserved.

Is "internally calibrated" monotone downward? Let's check:

- ∅ is calibrated ✓
- If A is calibrated, is parent(A) calibrated? Not necessarily. parent(A) might be a container whose sub-expressions have a shallower DCA.

Example: Consider a node at depth 3 that is internally calibrated. Its parent at depth 2 might be a container where the system and measurement sub-expressions diverge at depth 1. The parent might NOT be calibrated.

So the property is NOT monotone downward. This means the ancestor-based C can fail non-expansiveness.

**Decision point:** Do I try to fix this, or do I accept the limitation and document it?

Given time constraints, I'll document it honestly and provide the strongest theorems that DO hold. The honest document is more valuable than a forced proof.

Let me write the v2.0 contractiveness proof now with full honesty about what holds and what doesn't.

Key theorems that DO hold:
1. C is well-defined (Theorem 1)
2. C is idempotent (Theorem 3)
3. For calibrated nodes, C is identity (trivial)
4. For non-calibrated nodes, C strictly reduces depth
5. C is non-expansive when the shared ancestor of A and B is internally calibrated (Theorem 2-restricted)

Key things that DON'T hold:
1. Global non-expansiveness (counterexample above)
2. Global contractiveness
3. Non-trivial fixed point from ROOT

This is honest and useful — it characterizes exactly what properties C has and what it lacks.

Let me write it.<｜end▁of▁thinking｜>The ancestor-based C has a subtle issue I need to address: it can INCREASE distances when the shared ancestor fails calibration. Let me write the fully honest v2.0 proof.

<｜｜DSML｜｜tool_calls>
<｜｜DSML｜｜invoke name="write">
<｜｜DSML｜｜parameter name="content" string="true"># C-Contractiveness Proof: v2.0 (Red-Team Remediation)

**Phase 1, Task 1.2 — Bootstrap Conjecture Formal Proof**
**Date:** 2026-07-20 (v2.0 after red-team audit)
**Status:** v2.0 — addresses F-C1 through F-C5 from `red-team-audit-ctasks-2026-07-20.md`
**Dependencies:** `calibration-map-c-definition.md` v2.0

---

## §0. Revision Summary

| v1.0 Finding | Resolution |
|:-------------|:-----------|
| **F-C1** Lemma 2 same-measurement unsound | Eliminated — C v2.0 uses ancestor search, no D_A/D_B |
| **F-C2** Lemma 2 different-measurement circular | Eliminated — no cross-node convergence needed |
| **F-C3** Lemma 3 assumed Bootstrap to prove Bootstrap | Eliminated — no branch-convergence lemma |
| **F-C4** C* proof abandoned, then claimed proved | Replaced with Theorem 4: honest characterization of C* |
| **F-C5** Theorem 5 "proof sketch" | Replaced with idempotence theorem (trivial under v2.0) |

**Design change:** C v2.0 searches ancestors (finite), not descendants (infinite). This eliminates the unbounded-search problem but introduces a new challenge: ancestor-based C can increase distances. This document characterizes exactly when non-expansiveness holds and when it fails.

---

## §1. Preliminaries

### 1.1 Space

(TREE, DIST) — complete ultrametric space of reduced normal-form expressions.

### 1.2 C (v2.0)

```
C(N) = deepest ancestor A of N such that is_internally_calibrated(A)
```

Where `is_internally_calibrated` (abbreviated `cal(A)`) means:
- A = ∅ or A = ●, or
- A = [E₁...Eₙ], n ≥ 1, rightmost non-empty M = Eₙ,
  DEPTH(DCA_of_all(E₁,...,Eₙ₋₁, M)) ≥ DEPTH(A)

### 1.3 Key Structural Fact

C(N) is always an ancestor of N. Therefore:
- DEPTH(C(N)) ≤ DEPTH(N)
- If cal(N) then C(N) = N
- If ¬cal(N) then C(N) is a proper ancestor: DEPTH(C(N)) < DEPTH(N)

---

## §2. Positive Theorems (What DOES Hold)

### Theorem 1: Well-Definedness

C: TREE → TREE is a well-defined function.

**Proof.** For any N, the ancestor chain has DEPTH(N) + 1 nodes. cal(A) is a decidable predicate (finite DCA + DEPTH computation). The search terminates, returning the deepest calibrated ancestor. Since ∅ is always calibrated, the search always succeeds. ∎

---

### Theorem 2: Idempotence

C(C(N)) = C(N) for all N ∈ TREE.

**Proof.** By construction, C(N) is internally calibrated. Applying C to a calibrated node returns the node itself (it is its own deepest calibrated ancestor). Therefore C(C(N)) = C(N). ∎

**Corollary 2.1:** C² = C. The calibration map is a projection.

**Corollary 2.2:** Every calibrated node is a fixed point of C.

---

### Theorem 3: The Fixed-Point Set

Fix(C) = { N ∈ TREE : cal(N) } — exactly the internally calibrated nodes.

**Proof.** If cal(N), then C(N) = N (N is its own deepest calibrated ancestor). If ¬cal(N), then C(N) ≠ N (a proper ancestor is returned). Therefore N ∈ Fix(C) ⇔ cal(N). ∎

---

### Theorem 4: Depth Reduction on Non-Calibrated Inputs

If ¬cal(N), then DEPTH(C(N)) < DEPTH(N).

**Proof.** C searches ancestors starting from N upward. N itself fails cal. The returned node is a strict ancestor, therefore strictly shallower. ∎

**Corollary 4.1:** If ¬cal(A) and ¬cal(B), then both C(A) and C(B) are strictly shallower than A and B. The depth gap is at least 1 for each.

---

### Theorem 5: Non-Expansiveness on Calibrated Region

If cal(A) and cal(B), then DIST(C(A), C(B)) = DIST(A, B).

**Proof.** cal(A) ⇒ C(A) = A. cal(B) ⇒ C(B) = B. Therefore DIST(C(A), C(B)) = DIST(A, B). ∎

**Corollary 5.1:** C is distance-preserving on Fix(C). This is acceptable — calibrated nodes do not need to be "pulled" anywhere.

---

### Theorem 6: Contractiveness on Purely Uncalibrated Pairs Sharing a Calibrated Ancestor

**Assumptions:**
1. ¬cal(A) and ¬cal(B) (neither is calibrated)
2. ANCESTOR(A, B) = X, where cal(X) holds (their DCA is calibrated)
3. A ≠ B

Then: DIST(C(A), C(B)) < DIST(A, B).

**Proof.** Since ¬cal(A), C(A) is a proper ancestor of A. Since X is on the path from ROOT to A and cal(X), the deepest calibrated ancestor of A is at or below X: DEPTH(C(A)) ≥ DEPTH(X). Similarly, DEPTH(C(B)) ≥ DEPTH(X).

Since both A and B are below X and C reduces depth on both, the DCA of C(A) and C(B) is at depth ≥ DEPTH(X). And since A ≠ B and both are below X, at least one of C(A), C(B) is a proper ancestor, making DCA depth strictly greater than DEPTH(X):

DEPTH(ANCESTOR(C(A), C(B))) ≥ DEPTH(X) + 1

Therefore: DIST(C(A), C(B)) = 2^(-(d+1)) < 2^(-d) = DIST(A, B). ∎

**Contraction ratio:** ≤ 1/2 for pairs satisfying the assumptions.

---

## §3. Negative Theorems (What Does NOT Hold)

### Theorem 7: C Is NOT Globally Non-Expansive

There exist A, B ∈ TREE with DIST(C(A), C(B)) > DIST(A, B).

**Proof (counterexample).** Construct A and B sharing a deep ancestor X that is NOT internally calibrated.

Let the tree contain:
- X at depth 5, a container whose rightmost sub-expression and remaining sub-expressions have DCA at depth 2 (so ¬cal(X) since 2 < 5).
- A: a descendant of X at depth 8, with cal(A) = true (A IS internally calibrated).
- B: a descendant of X at depth 8, in a different sub-branch below X, with cal(B) = true.

Then C(A) = A, C(B) = B. Wait — this gives DIST(C(A), C(B)) = DIST(A, B). Not a counterexample.

**Revised construction:** We need one of A, B to be uncalibrated.

Let:
- X at depth 3, not calibrated.
- A: descendant of X at depth 6, not calibrated.
- B: descendant of X at depth 6, different sub-branch, calibrated.

C(A): deepest calibrated ancestor of A. The ancestor chain of A is [ROOT, ..., X, ..., A]. Since ¬cal(X) and X might be the deepest thing above A that could be calibrated... what if X's parent (depth 2) IS calibrated? Then C(A) = X's parent (depth 2).

C(B) = B (since B is calibrated at depth 6).

Now:
- DIST(A, B) = 2^(-3) = 1/8 (DCA = X at depth 3)
- C(A) at depth 2, C(B) at depth 6.
- DCA(C(A), C(B)): C(A) is at depth 2, its path doesn't include X. C(B) is at depth 6, its path includes X (at depth 3). The intersection is only up to depth 2 (since C(A) stops at depth 2).
- DIST(C(A), C(B)) = 2^(-2) = 1/4.

1/4 > 1/8 → DIST INCREASED. ∎

**Implication:** C can push nodes APART when one calibrates to a very shallow ancestor while the other stays deep. This is a distance-INCREASING effect — the opposite of contraction.

---

### Theorem 8: C Is NOT Globally Contractive

Already shown in v1.0 (Theorem 1): C is identity on calibrated nodes, so DIST(C(A), C(B)) = DIST(A, B) for any pair of calibrated nodes.

---

### Theorem 9: C From ROOT Has Trivial Fixed Point

C(∅) = ∅ (ROOT is calibrated). Therefore lim_{n→∞} Cⁿ(∅) = ∅.

The Bootstrap Conjecture requires T* ≠ ∅. C as defined in v2.0 does not satisfy this.

---

## §4. Honest Assessment

### 4.1 What C (v2.0) Achieves

| Property | Status | Theorem |
|----------|--------|---------|
| Well-defined on all TREE | ✅ | T1 |
| Idempotent (C² = C) | ✅ | T2 |
| Fixed-point set = calibrated nodes | ✅ | T3 |
| Depth-reducing on uncalibrated inputs | ✅ | T4 |
| Distance-preserving on calibrated pairs | ✅ | T5 |
| Contractive on uncalibrated pairs sharing calibrated DCA | ✅ | T6 |
| Globally non-expansive | ❌ | T7 (counterexample) |
| Globally contractive | ❌ | T8 |
| Non-trivial fixed point from ROOT | ❌ | T9 |

### 4.2 The Core Tension

The ancestor-based approach to calibration has an inherent tension:

1. **Ancestor search** is well-defined and computable (finite search) — fixes F-H1.
2. **But** ancestor-based C can INCREASE distances when the DCA of two nodes is uncalibrated (one node calibrates to a much shallower ancestor while the other stays deep) — violates non-expansiveness.

The descendant-based approach (v1.0) had the opposite problem: it could increase depth (unbounded search, F-H1) but was potentially non-expansive.

**There is no free lunch:** any calibration map on TREE must navigate the trade-off between well-definedness and contractiveness. The Bootstrap Conjecture is conjectural precisely because constructing a map that is simultaneously well-defined, non-expansive, AND has a non-trivial fixed point is genuinely hard.

### 4.3 What Would Be Required

A calibration map C satisfying all three properties must:

1. **Well-defined:** finite computation for every input.
2. **Non-expansive (minimum) / Contractive (ideal):** DIST(C(A), C(B)) ≤ DIST(A, B).
3. **Non-trivial fixed point:** lim Cⁿ(ROOT) = T* ≠ ROOT.

The parent map satisfies (1) and (2) but fails (3). The v1.0 C attempted to satisfy all three but failed (1) and (2). The v2.0 C satisfies (1) but fails (2) and (3).

**Open problem:** Construct a map on TREE satisfying all three properties, or prove no such map exists (which would refute the Bootstrap Conjecture).

---

### Theorem 10: The Parent Map Is the Only Depth-Reducing Contractive Map

**Conjecture:** If F: TREE → TREE is strictly depth-reducing for all N ≠ ROOT (DEPTH(F(N)) < DEPTH(N)) and globally contractive, then F = parent (or F is isomorphic to parent under tree automorphism).

If this conjecture holds, then ANY non-trivial calibration map (one that doesn't collapse everything to ROOT) must be depth-PRESERVING on at least some nodes, which forces it into the difficult Case 2 of the f-contractiveness analysis (depth-preserving + branch-strict). This is the fundamental difficulty.

---

## §5. C* — Measurement-Initiated Calibration

### 5.1 Definition

```
C*(∅) = ●           (initiate first distinction)
C*(●) = ●           (fixed point)
C*(N) = C(N)        (standard calibration for all other nodes)
```

### 5.2 Properties

| Property | Status |
|----------|--------|
| Well-defined | ✅ (C is well-defined, two extra cases are explicit) |
| Fixed point from ROOT | ✅ C*²(∅) = C*(●) = ● |
| Non-trivial T* | ⚠️ ● is arguably still trivial (a bare mark) |
| Globally non-expansive | ❌ Same counterexample as C (T7) |
| Globally contractive | ❌ |

### 5.3 Honest Assessment of C*

C* fixes the "no fixed point from ROOT" problem but:
- The fixed point ● is structurally trivial (encodes no branching pattern).
- C* inherits C's non-expansiveness failure (T7).
- C* is not a significant improvement over the parent map for physical modeling.

**The Bootstrap Conjecture remains open.** Neither C (v2.0) nor C* provides a calibration map with a non-trivial fixed point that is also non-expansive.

---

## §6. Summary Table

| Theorem | Statement | Proof |
|---------|-----------|-------|
| T1 | C is well-defined | ✓ |
| T2 | C² = C (idempotent) | ✓ |
| T3 | Fix(C) = calibrated nodes | ✓ |
| T4 | ¬cal(N) ⇒ DEPTH(C(N)) < DEPTH(N) | ✓ |
| T5 | cal(A) ∧ cal(B) ⇒ DIST(C(A),C(B)) = DIST(A,B) | ✓ |
| T6 | ¬cal(A) ∧ ¬cal(B) ∧ cal(DCA(A,B)) ⇒ DIST(C(A),C(B)) < DIST(A,B) | ✓ |
| T7 | C is NOT globally non-expansive | ✓ (counterexample) |
| T8 | C is NOT globally contractive | ✓ |
| T9 | lim Cⁿ(∅) = ∅ (trivial) | ✓ |
| T10 | Parent map uniqueness conjecture | Conjecture only |

---

## References

- `calibration-map-c-definition.md` v2.0 — C definition (ancestor-based)
- `f-contractiveness-analysis.md` — Contractiveness conditions on TREE
- `red-team-audit-ctasks-2026-07-20.md` — F-C1 through F-C5 findings
- `29-schisms-formalization.md` — TREE, DIST, DCA, DEPTH definitions
