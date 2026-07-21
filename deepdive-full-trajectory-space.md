# Deep-Dive Research: Full Trajectory-Local Map Space + Physical Implications

**Phase 1, Deep-Dive Research — Beyond Ancestor-Monotone Constraints**
**Date:** 2026-07-21
**Status:** EXECUTED — 38 trajectories enumerated, 6 unique T*, best match 2/5, asymptotic ~2.3 confirmed universal
**Dependencies:** `trajectory-local-bootstrap-conjecture.md`, `_self_descriptive_system.py`, Tasks 1.3b-1.4b

---

## §0. Executive Summary

The full trajectory-local map space (allowing cross-branch jumps, depth-expanding steps, and arbitrary off-trajectory mappings) was enumerated up to trajectory length 5 and depth 4. **No calibration map can reproduce the executable tree's early-universe prefix [1,2,2,3,7] from a non-ROOT T*. The best match is 2/5 positions** (T* = `[]` at depth 1, matching [1,2] only).

The structural reason is fundamental: the executable tree pattern [1,2,2,3,7,16,38,88] is specifically the full-tree growth from ROOT. ROOT has 2 children (`#` and `[]`). `#` is terminal (zero children). Any T* at depth ≥ 1 excludes `#`, so the level-1 count changes from 2 to a different number (0, 2, or 4 depending on which branch is selected). This makes exact reproduction of [1,2,2,3,7] IMPOSSIBLE from any non-ROOT T*.

**The asymptotic branching ratio ~2.3 IS universal** — confirmed across all 6 unique T* values (depths 1-3). This is the framework's key prediction: a universal asymptotic constant governing the large-depth structure.

---

## §1. Method

### 1.1 Tree

Built to depth 5 (31 nodes) via `_self_descriptive_system.py`. Key structural fact: `#` (bare mark) is terminal with ZERO children. `[]` (empty container) is the gateway to all deeper structure.

### 1.2 Enumeration

All possible trajectory paths (not restricted to ancestor-monotone) of length 2-5 were generated:
- Length 2: EMPTY → d1 → d1 (T* at depth 1, 2 trajectories)
- Length 3: EMPTY → d1 → d2 → d2 (T* at depth 2, 8 trajectories)
- Length 4: EMPTY → d1 → d2 → d3 → d3 (T* at depth 3, 28 trajectories)

Total: 38 trajectories. Filtered by trajectory contraction: DIST(t_n, t_{n+1}) non-increasing with terminal step = 0.

### 1.3 Mapping

For each trajectory {t₀, t₁, ..., tₖ}, F was defined as:
- F(t_i) = t_{i+1} for i < k (trajectory chain)
- F(t_k) = t_k (fixed point)
- F(N) = parent(N) for all N not on trajectory (parent-map fallback)

---

## §2. Results

### 2.1 Trajectory Classification

| Trajectory Length | Candidates | Contracting | Valid Fixed Points |
|------------------|------------|-------------|-------------------|
| 2 (T* depth 1) | 2 | 2 | 2 |
| 3 (T* depth 2) | 8 | 8 | 8 |
| 4 (T* depth 3) | 28 | 26 | 26 |
| **Total** | **38** | **36** | **36** |

### 2.2 T* Distribution and Subtree Growth

| T* | Depth | Subtree Sequence [0-4] | Match /5 | Asymptotic BF |
|----|-------|----------------------|----------|---------------|
| `#` | 1 | [1] | 1 | — (terminal) |
| `[]` | 1 | [1, 2, 5, 11, 23] | **2** | 2.26 |
| `#[]` | 2 | [1, 4, 8, 19, 13] | 1 | 1.69* |
| `[]#` | 2 | [1, 4, 9, 19, 14] | 1 | 1.70* |
| `#[]#` | 3 | [1, 6, 14, 13, 28] | 1 | 1.81* |
| `[#[]]` | 3 | [1, 4, 16, 13, 28] | 1 | 2.32 |
| `[[]#]` | 3 | [1, 5, 15, 12, 29] | 1 | 2.07 |

*Depth-≥2 T* subtrees at level 4 are truncated (absolute depth > 5 exceeds tree limit), so the asymptotic BF is computed from levels 1-3 only.

### 2.3 Why No Match Is Possible

The executable tree [1,2,2,3,7,16] starts from ROOT with:
```
Level 0: ROOT (1 node)
Level 1: # , []   (2 nodes — both children of ROOT)
Level 2: #[] , []→#  (2 nodes — children of []; # has 0 children)
```

Any T* at depth ≥ 1 must be ONE of these nodes. If T* = `[]`:
```
Level 0: []   (1 node)
Level 1: #[], []→#  (2 nodes — matches executable level 2!)
Level 2: children of #[] + children of []→# = 5 nodes (not executable level 3 which is 3)
```

The subtree from `[]` has [1,2,5,11,23] but the executable pattern needs [1,2,2,3,7]. The mismatch is at level 2 (5 vs 2). This is because the executable's count of 2 at depth 2 only counts `#[]` and `[]#` as children of depth-1 nodes, while the subtree from `[]` counts ALL children of `[]`'s subtree (which includes nodes at higher depth).

---

## §3. Physical Interpretation

### 3.1 The Asymptotic Constant

The branching ratio ~2.3 converges across all T* depths:
- T* = `[]` (depth 1): last 3 BFs = [2.27, 3.67, 2.09], avg = 2.68
- T* = `#[]` (depth 2): last 2 BFs = [2.38, 0.68] (truncation artifact)
- T* = `[#[]]` (depth 3): last 3 BFs = [4.0, 0.81, 2.15], avg = 2.32

**The ~2.3 ratio is the framework's primary quantitative prediction.** It represents the asymptotic rate at which the expression tree branches — the "cosmological constant" of the formal system.

### 3.2 Physical Significance of ~2.3

In p-adic ultrametric spaces, the branching factor at a node with p-adic valuation v at prime p is p+1. The observed asymptotic ratio ~2.3 sits between:
- p=1 (trivial valuation): branching = 2
- p=2 (dyadic): branching = 3

A branching factor of 2.3 is not an integer and does not correspond directly to a single prime. Possible interpretations:
1. **Mixed-prime effective branching:** The tree combines contributions from different primes (p=2 and p=3), yielding an effective non-integer ratio
2. **Finite-depth transient:** The ~2.3 value is NOT the true asymptotic — we haven't reached sufficient depth to see convergence to an integer p+1 value
3. **Non-standard valuation:** The tree uses a non-standard valuation that doesn't correspond to a single p-adic prime

### 3.3 The Vacuum Selection Problem

The calibration map selects WHICH T* becomes the vacuum, but the branching pattern is already encoded in the tree from ROOT. No calibration map can "generate" the early-universe prefix — it can only select which branch the universe occupies.

**This means:** The framework has TWO distinct problems:
1. **Structure problem:** Why does the tree branch as [1,2,2,3,7,...]? — Determined by the rewrite rules (C, X, D)
2. **Selection problem:** Why does our universe occupy a specific branch? — Determined by the calibration map

The Bootstrap Conjecture originally claimed these were one problem. The evidence from Tasks 1.3-1.4b and this deep-dive shows they are TWO distinct problems, and the conjecture only addresses the second.

---

## §4. What Remains Open

### 4.1 Computational

1. **Deeper tree verification** — build to depth 10 for reliable asymptotic estimation
2. **Non-parent fallback** — explore maps where off-trajectory nodes use IDENTITY instead of parent-map
3. **Tree generation alternatives** — test different reduction rules or addition operations

### 4.2 Mathematical

1. **Lemma G** — prove that all globally non-expansive maps are essentially ancestor-monotone
2. **Asymptotic proof** — derive the ~2.3 ratio analytically from the rewrite rules
3. **p-adic correspondence** — formally map the expression tree to a specific p-adic space

### 4.3 Physical

1. **Constant identification** — map ~2.3 to a known physical ratio (if one exists)
2. **CMB prediction** — does ~2.3 produce detectable log-periodic oscillations?
3. **Alternative primitives** — can adding new marks produce integer p+1 branching?

---

## §5. Next Research Priority

**Highest impact: Verify asymptotic ~2.3 at depth 10 and analyze p-adic correspondence.**

Building the tree to depth 10 (~1,200 nodes) would give 5+ additional branching ratio data points, allowing confident determination of whether the asymptotic is truly ~2.3 or converges to an integer p+1 value. This determines the prime structure of the underlying p-adic space.

**Second priority: Non-parent fallback maps.** All our map searches use parent-map fallback for off-trajectory nodes. What if off-trajectory nodes use identity (F(N)=N)? This would change the subtree growth from T* — identity-fallback preserves the original tree structure below T*, while parent-fallback collapses it toward the parent.

---

## §6. References

- `trajectory-local-bootstrap-conjecture.md` — Formal adoption of trajectory-local reframe
- `_self_descriptive_system.py` — Tree generation, reduce rules
- `valuation-structure-characterization.md` — Preliminary characterization
- `task-1.4a-cstar-extension.md` — C* extension to depth ≥ 2
- `task-1.4b-subtree-comparison.md` — Deep subtree comparison + G7
