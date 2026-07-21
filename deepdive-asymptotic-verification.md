# Deep-Dive Phase 2: Asymptotic Verification — Ratio Converging to ~2.0?

**Date:** 2026-07-21
**Status:** EXECUTED — tree built to depth 9 (789 nodes), branching ratio monotonically decreasing toward ~2.0
**Dependencies:** `deepdive-full-trajectory-space.md`, `_self_descriptive_system.py`

---

## §0. Key Finding

**The asymptotic branching ratio is NOT stabilizing at ~2.3 — it is monotonically DECREASING at every depth from 6 onward, trending toward ~2.0.** This was previously reported as "converging to ~2.3" based on depth-7 data. Depth 8 and 9 reveal the ratio is still in transient:

| Depth | Nodes | Branching Factor | Δ from prev |
|-------|-------|-----------------|-------------|
| 4 | 7 | 2.333 | — |
| 5 | 16 | 2.286 | -0.048 |
| 6 | 38 | 2.375 | +0.089 |
| 7 | 88 | 2.316 | -0.059 |
| 8 | 197 | 2.239 | -0.077 |
| 9 | 435 | 2.208 | -0.031 |

**Decreasing trend (depth 5→9):** 2.286 → 2.375 → 2.316 → 2.239 → 2.208

The reversal at depth 6 (2.375, up from 2.286) appears to be a transient spike. From depth 6 onward, the trend is monotonically decreasing: 2.375 → 2.316 → 2.239 → 2.208.

---

## §1. Physical Implication

If the ratio converges to **2.0**, the tree corresponds to a **p=1 trivial valuation** — the simplest possible ultrametric space. In p-adic terms:
- p=1: branching = 2 (binary tree)
- p=2: branching = 3 (dyadic, the standard p-adic connection)
- p=3: branching = 4

A p=1 (binary) limit would mean:
1. **The tree is NOT dyadic (p=2)** — the framework does NOT recover standard p-adic physics
2. **The tree is essentially binary at large scales** — each expression has ~2 children on average
3. **The framework's "p-adic" claim is weakened** — the formalism produces p=1, not p=2 or a nontrivial prime

### 1.1 What BINARY (p=1) Means

A binary branching tree at large depths means:
- Each expression distills into ~2 fundamentally different normal-form extensions
- The distinction/container primitives generate exactly 2 structural variants per depth level
- This matches the Laws of Form (Spencer-Brown) intuition: a distinction splits the void into 2 states

**The `#` vs `[]` split at depth 1 already suggests binary structure** — ROOT has exactly 2 children, `#` is terminal (0 further children), and `[]` is a container (~2 children). Binary branching at scale would mean this 2-child pattern persists at all depths.

---

## §2. Updated Research Implications

### 2.1 Previous Claims Requiring Revision

| Claim | Old Value | New Evidence |
|-------|-----------|-------------|
| Asymptotic branching | ~2.3 | Decreasing: 2.38→2.32→2.24→2.21 (toward ~2.0?) |
| "p=2 dyadic" connection | Implicit | No evidence — ratio trending toward 2 (p=1), not 3 (p=2) |
| "Universal constant ~4.7" (pre-G7) | 4.70 | FALSE — corrected to ~2.3, which is itself trending toward 2.0 |
| "~2.3 is universal" | Confirmed | Called into question — if ratio converges to 2.0, ~2.3 is a FINITE-DEPTH TRANSIENT |

### 2.2 What Holds

| Claim | Status |
|-------|--------|
| Trajectory-local reframe | ✅ Satisfiable |
| T* at depth ≥ 2 reachable | ✅ Confirmed (5 unique T*) |
| No T* subtree matches [1,2,2,3,7] | ✅ Proven (structural impossibility) |
| Calibration map selects vacuum branch | ✅ Confirmed |
| Branching at early depths is transient | 🔶 NEW: apparent from depth-9 data |

---

## §3. Next Steps

### 3.1 Immediate — Depth 10-11 Verification

Building the tree to depth 10-11 (~1200-2700 nodes) would give 2-3 more data points and distinguish:
- **Convergence to 2.0:** bf continues decreasing (2.21 → 2.19 → 2.17 → ...)
- **Convergence to ~2.2:** bf stabilizes (2.21 → 2.20 → 2.20 → ...)
- **Oscillation:** bf oscillates around some value

### 3.2 Analytical

- **Derive the asymptotic ratio from the rewrite rules** — can we prove analytically whether the ratio converges to 2.0, 2.2, or something else?
- **Compare to standard p-adic trees** — standard Bruhat-Tits trees for p=2 have branching factor p+1=3 at every node. Our tree has ~2.3 on average because many nodes are terminal or have few children.

### 3.3 Framework Implications

If the ratio converges to **2.0 (p=1)**:
- The framework is BINARY, not p-adic in the standard sense
- The "ultrametric" label is still correct (binary trees ARE ultrametric)
- The connection to p-adic numbers (Q_p) would need to be REVISED
- The trapped-ion experiment protocol (which assumes p-adic ultrametricity) may need revision

If the ratio converges to a non-integer **~2.1-2.3**:
- This would be a NON-STANDARD ultrametric space
- It would not correspond to any standard p-adic prime
- This could be a genuinely novel mathematical structure

---

## §4. Updated Gap Register (revision to G4)

| Gap | Old Status | New Status |
|-----|-----------|------------|
| **G4** | MODERATE — tractability confirmed, base ~2.3 | **HIGH** — asymptotic ratio NOT yet determined. Currently decreasing toward 2.0. Need depth 10-11 to confirm limit. p-adic correspondence uncertain if ratio settles at non-integer value. |

---

## §5. Data

### Raw Node Counts

```
Depth 0: 1
Depth 1: 2    (bf: 2.000)
Depth 2: 2    (bf: 1.000)
Depth 3: 3    (bf: 1.500)
Depth 4: 7    (bf: 2.333)
Depth 5: 16   (bf: 2.286)
Depth 6: 38   (bf: 2.375)
Depth 7: 88   (bf: 2.316)
Depth 8: 197  (bf: 2.239)
Depth 9: 435  (bf: 2.208)
Total: 789 nodes
```

### P-Adic Comparison

| p | p+1 | Distance from ~2.21 |
|---|-----|---------------------|
| 1 | 2   | 0.21 ← **closest** |
| 2 | 3   | 0.79 |
| 3 | 4   | 1.79 |
| 5 | 6   | 3.79 |
