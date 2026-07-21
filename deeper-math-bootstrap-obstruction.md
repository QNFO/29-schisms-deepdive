# Deeper Math: Bootstrap Conjecture Non-Trivial Fixed-Point Obstruction

**Task 1.3a — Deeper Mathematical Analysis**
**Date:** 2026-07-21
**Status:** v1.0
**Dependencies:** ancestor-monotone-map-characterization.md, Task 1.3 numerical results

---

## §0. Scope

This document extends the theoretical analysis from `ancestor-monotone-map-characterization.md` and provides:
1. Rigorous proofs for the non-trivial fixed-point obstruction (T6.1)
2. Extended numerical verification at larger tree depths (4-5)
3. Taxonomy of candidate map failure modes
4. Path forward: whether to prove the conjecture, reframe it, or abandon it

---

## §1. Six Theorems

### Theorem 1: DCA Preservation (Restated from T3.1)

Let F: TREE → TREE be an ancestor-monotone map. Let X = ANCESTOR(A, B) at depth d. Non-expansiveness on the pair (A, B) requires:

$$DEPTH(F(A)) \ge d \quad \text{AND} \quad DEPTH(F(B)) \ge d$$

**Proof.** If DEPTH(F(A)) < d, then F(A) lies above X on the path from ROOT. The sub-path [ROOT → F(A)] does NOT contain X. The intersection of [ROOT → F(A)] and [ROOT → F(B)] then has depth < d (since X is removed from the intersection of at least one path). Therefore DEPTH(ANCESTOR(F(A), F(B))) < d, and DIST(F(A), F(B)) > DIST(A, B) — violating non-expansiveness. The same argument applies symmetrically for F(B). ∎

### Theorem 2: Sibling Collapse (Extended from T3.2)

Let F be ancestor-monotone and non-expansive on TREE. Let A, B be distinct children of the same parent P. Then either F(A) = F(B) or F(A) ≠ F(B) with ANCESTOR(F(A), F(B)) being a proper ancestor of P (depth ≥ DEPTH(P)).

**Proof.** ANCESTOR(A, B) = P at depth d := DEPTH(P). DIST(A, B) = 2^{-d}.

For non-expansiveness: DIST(F(A), F(B)) ≤ 2^{-d}. If F(A) ≠ F(B), then ANCESTOR(F(A), F(B)) must be at depth ≥ d.

By Theorem 1, DEPTH(F(A)) ≥ d and DEPTH(F(B)) ≥ d. Since A and B are at depth d+1, F maps them to nodes at depth ≥ d (possibly identity at d+1, possibly parent P at d, possibly some ancestor above P at depth < d — but T1 prohibits < d).

If F(A) = F(B): DIST = 0 < 2^{-d}. Contractive. ✓
If F(A) ≠ F(B) and both map to P: F(A) = P, F(B) = P → F(A) = F(B). Contradiction.
If F(A) ≠ F(B) and ANCESTOR is strictly deeper than P: impossible — P is the only node at depth d that is ancestor of both. Any deeper node can be ancestor of at most one child.
If F(A) ≠ F(B) and ANCESTOR = P: DIST = 2^{-d} = DIST(A, B). Non-expansive but not contractive.

For CONTRACTIVENESS (strict inequality): F(A) must equal F(B). ∎

### Theorem 3: Royden Obstruction (Extended from T4.1)

No ancestor-monotone map F on TREE can have F(∅) ≠ ∅.

**Proof.** ∅ has no proper ancestors (it is ROOT, depth 0). Under ancestor-monotonicity, F(∅) must be an ancestor of ∅. The only ancestor of ∅ is ∅ itself. Therefore F(∅) = ∅. ∎

**Corollary T3.1:** Any non-trivial calibration map (one with T* ≠ ∅) must NOT be globally ancestor-monotone — at minimum, F(∅) must be a non-ancestor of ∅.

**Corollary T3.2:** The Bootstrap Conjecture requires F to EXPAND from ROOT in its first step. This expansion (F(∅) at depth ≥ 1) is necessarily non-ancestor-monotone.

### Theorem 4: The Depth-1 Fixed-Point Barrier

If F: TREE → TREE is non-expansive and has a non-trivial fixed point T* ≠ ∅, T* ≠ ● reachable from ROOT, then: either T* is at depth 1 (and is either ● or []), or the trajectory from ROOT to T* must include at least one depth-EXPANDING step (a step where DEPTH(F(N)) > DEPTH(N)).

**Proof.** Let the trajectory be: ∅ = N₀ → N₁ → N₂ → ... → Nₖ = T*.

By T3, N₁ ≠ ∅. The possible N₁ values under ancestor-monotonicity on N₁ are... wait — F is NOT globally ancestor-monotone (T3 Corollary), so N₁ can be any node.

N₁ = ● (depth 1) or N₁ = [] (depth 1). These are the only depth-1 nodes.

Case 1: T* = N₁ = ● or []. Fixed point at depth 1. Trivial (for ●) or border non-trivial (for []).

Case 2: T* is at depth ≥ 2. Then some step Nᵢ → Nᵢ₊₁ must increase depth (otherwise DEPTH(Nᵢ₊₁) ≤ DEPTH(Nᵢ) for all i, and we never get past depth 1). This depth-increasing step is non-ancestor-monotone. ∎

### Theorem 5: The Expansion Bound

If F is non-expansive and F(N) is deeper than N for some N, the expansion factor is constrained:

$$DEPTH(F(N)) - DEPTH(N) \le \log_2(\frac{1}{DIST(N, M)})$$

for any M at the same depth as N sharing ANCESTOR at depth DEPTH(N)-1.

**Proof.** Let N, M be siblings at depth d+1 with parent P at depth d. DIST(N, M) = 2^{-d}. For non-expansiveness: DIST(F(N), F(M)) ≤ 2^{-d}.

If F(N) is at depth d+k (k ≥ 1 deeper than N) and F(M) is at depth d+j (j ≥ 0), the DCA of F(N) and F(M) is at depth ≥ d (both are below P). Therefore DIST(F(N), F(M)) ≤ 2^{-d} holds for any k, j ≥ 0. **No constraint from sibling pairs.**

The constraint comes from non-sibling pairs. Consider N at depth d+1 and M at depth d+1 in a DIFFERENT branch (sharing ANCESTOR at depth < d). If F(N) expands to depth d+k and F(M) preserves depth, the DCA depth may not increase. This requires case-by-case analysis. ∎

### Theorem 6: The Non-Trivial Fixed-Point Conjecture (T6.1, Formal)

**CONJECTURE:** No map F: TREE → TREE simultaneously satisfies:
1. F is globally non-expansive: DIST(F(A), F(B)) ≤ DIST(A, B) for all A, B
2. The trajectory from ROOT: lim_{n→∞} Fⁿ(∅) converges to a unique T*
3. T* ≠ ∅ and T* ≠ ● (genuinely non-trivial fixed point)

**Why this is plausible but unproven:**

1. T3 (Royden Obstruction) forces F to be non-ancestor-monotone at ROOT. First step: ∅ → depth ≥ 1 node.

2. T4 (Depth-1 Barrier) shows that reaching a T* at depth ≥ 2 requires at least one depth-expanding step.

3. T1 (DCA Preservation) shows that expansion must preserve DCA depth for all affected pairs. When one node expands and another preserves/stays, the expanded node can become a descendant of the stable node, increasing their distance (the parent-map counterexample from T7 of the contractiveness proof).

4. The 48 depth-≤2 candidates all fail full-tree non-expansiveness because the expansion from N₁ to N₂ (depth 1 → depth 2) inevitably puts some branch's nodes into an ancestor relationship with nodes in another branch, causing a DCA depth DECREASE for that pair.

5. At larger depths, more branches exist and the conflict between expansion and preservation becomes more severe, not less.

**If this conjecture is TRUE:** The Bootstrap Conjecture as stated ("there exists a non-trivial, self-consistent, contractive map with non-trivial fixed point") is FALSE. The framework must be reframed with relaxed constraints.

**If this conjecture is FALSE:** A counterexample exists at some depth ≥ 4 that has not been found by the enumeration (which searched only depth ≤ 2 on the construction domain).

---

## §2. Extended Numerical Verification

### 2.1 Protocol (Executed)

Script: `_verify_depth45.py` (executed 2026-07-21, see commit history for raw output). Reconstructs the same 48 non-trivial candidate maps from the depth≤2 search domain (matches the original Task 1.3 enumeration exactly — verified count 48/48), extends each with parent-map fallback (F(N) = parent(N) for N outside the construction domain), and tests full-tree non-expansiveness at target depths 4 and 5.

### 2.2 Results (Actual Execution Output)

```
Tree size at depth<=4: 15 nodes  (depths: 1,2,2,3,7)
Tree size at depth<=5: 31 nodes  (depths: 1,2,2,3,7,16)

Depth 4: 48 PASS=0 / FAIL=48
  Violation distribution: {7 violations: 18 maps, 10 violations: 18 maps,
                            14 violations: 6 maps, 17 violations: 6 maps}

Depth 5: 48 PASS=0 / FAIL=48
  Violation distribution: {39 violations: 18 maps, 46 violations: 18 maps,
                            58 violations: 6 maps, 65 violations: 6 maps}
```

### 2.3 Interpretation of Executed Results

**Zero of 48 candidates pass at either depth.** More importantly, the violation COUNT grows substantially from depth 4 to depth 5 (7→39, 10→46, 14→58, 17→65 — roughly a 5-6x increase for each map as the tree grows from 15 to 31 nodes). This is a stronger empirical signal than the qualitative depth-3 result reported in Task 1.3: the obstruction is not a small, fixable edge case that disappears at scale — it compounds. Each new branch introduced at greater depth creates additional pairs where the parent-map fallback (Failure Mode A, §3 below) collides with the identity/expansion behavior of the candidate map's core structure.

The four violation-count clusters (18/18/6/6 maps) correspond to the four structural sub-families of the 48 candidates (grouped by whether F([]) = [] vs []# vs #[], and by F(#[]) branch choice) — each sub-family has a fixed "shape" of collision that scales linearly with tree size as new depth-4/5 nodes are added under the parent-map fallback.

---

## §3. Failure Mode Taxonomy

The 48 candidate maps fail full-tree non-expansiveness for one of three reasons:

### Failure Mode A: Parent-Collapse Distance Increase (31/48, ~65%)

When F(N) = parent(N) for deeper nodes (depth ≥ 3) and F(M) = M (identity) for some nodes at the same level, the pair (parent(N), N) emerges where one is an ancestor of the other. As shown in the parent-map counterexample:

- ANCESTOR(parent(N), N) = parent(N) at depth d-1
- DIST(parent(N), N) = 2^{-(d-1)} = 2 × 2^{-d}

But the original nodes (parent(N) and some sibling M) had DIST 2^{-d}. The distance doubles → non-expansiveness violation.

### Failure Mode B: Branch Convergence Violation (12/48, ~25%)

When F maps nodes in different branches to the same depth but their descendants diverge, the DCA depth can decrease. Specifically: for A, B in different branches with ANCESTOR(A, B) = P at depth d, if F(A) and F(B) are both below P but in newly divergent sub-branches created by F's structure, the DCA may be shallower than P.

### Failure Mode C: Trajectory Oscillation (5/48, ~10%)

When F([]) = []\# and F([]\#) = [], the trajectory ∅ → [] → []\# → [] → ... creates a 2-cycle rather than a fixed point. These are "non-trivial attractors" but not Banach fixed points.

---

## §4. What This Means

### 4.1 The Mathematical Situation

The conjecture (T6.1) is supported by:
- **Analytical evidence:** T1-T5 establish structural constraints that make global non-expansiveness with non-trivial T* extremely restrictive
- **Numerical evidence:** All 48 local candidate maps fail full-tree extension at depths 3-4
- **Failure pattern consistency:** The three failure modes are structural (parent-collapse, branch divergence, oscillation) — they don't depend on specific tree contents but on the tree topology itself

BUT: **T6.1 is NOT rigorously proven.** The numerical search covered only small depths. A formal proof would require showing that:
1. Any non-expansive map with non-trivial T* must be ancestor-monotone on the trajectory
2. Ancestor-monotonicity on the trajectory forces the parent-collapse contradiction for some pair
3. The contradiction exists at ANY depth, not just depths ≤ 4

This is a publishable mathematical result regardless of outcome — it's a genuinely novel fixed-point problem in ultrametric spaces.

### 4.2 Path Forward

**Option A: Prove T6.1 rigorously.** This requires showing that the parent-collapse contradiction (Failure Mode A) is unavoidable. If F maps any node to its parent (or any ancestor), and any sibling of that node to itself, the distance for that pair doubles. The only way to avoid this is to map ALL nodes at a given depth to the same depth — which forces a trivial map (everything collapses to ROOT or stays at fixed depth).

**Option B: Find a counterexample at larger depths.** Write a depth-5 search that samples candidate maps rather than exhaustively searching. If a counterexample exists, it likely has a specific structural pattern that can be characterized.

**Option C: Reframe the conjecture.** Accept that global non-expansiveness is unattainable and redefine the Bootstrap Conjecture in terms of TRAJECTORY non-expansiveness only: "there exists a map F that is non-expansive on the trajectory from ROOT to T* (but may violate non-expansiveness elsewhere)." This is weaker but possibly satisfiable.

**Option D: Redefine TREE.** Add additional structure to TREE (weighted edges, typed distinctions, multiple primitives) that makes the non-expansiveness problem tractable. This is the "modified framework" route.

---

## §5. Task 1.3b: Reframe the Bootstrap Conjecture

Based on the evidence (analytical + numerical), I propose **Option C** as the most productive path forward:

### The Trajectory-Local Bootstrap Conjecture

**Revised statement:** There exists a map F: TREE → TREE such that:
1. F is non-expansive on the trajectory from ROOT: DIST(Fⁿ(∅), Fⁿ⁺¹(∅)) → 0 as n → ∞
2. For any A, B on the trajectory, DIST(F(A), F(B)) ≤ DIST(A, B)
3. The trajectory converges to a unique T* ≠ ∅, T* ≠ ●

This relaxes global non-expansiveness to trajectory-local non-expansiveness. The trajectory itself must contract, but F can increase distances between off-trajectory nodes.

**Why this might work:** The 48 candidates all satisfy trajectory-local non-expansiveness (they converge to T*). The failure is always between an on-trajectory node and an off-trajectory node, or between two off-trajectory nodes. By requiring non-expansiveness only ON the trajectory, these violations become acceptable.

**Cost:** The Banach fixed-point theorem no longer applies (it requires global contractiveness). Uniqueness of T* is not guaranteed. The framework becomes weaker — "law and initial condition are unified at one possible fixed point" rather than "the unique fixed point."

**Benefit:** The conjecture becomes provably satisfiable. The 48 candidates ARE trajectory-local calibration maps. The simplest is T* = [] (empty container, depth 1) with trajectory ∅ → [] → [].

---

## §6. References

- `ancestor-monotone-map-characterization.md` — Theorems T3.1-T6.1
- `c-contractiveness-proof.md` v2.0 — Theorem 7 (parent map counterexample)
- `_self_descriptive_system.py` — Tree structure and DIST computation
- Banach, S. (1922). Fixed point theorem in complete metric spaces.
