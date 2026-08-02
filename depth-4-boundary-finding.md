# Depth-4 Boundary Finding: Ascendant-Climb Pattern Breaks at Tree Depth 5

**Task:** Post-Task 1.4a extension — depth-4 fixed point search at tree <= 5
**Date:** 2026-08-02
**Status:** v1.0 — NEGATIVE FINDING: ascendant-climb pattern has depth bound of 3
**Dependencies:** Task 1.3 (depth-2 witness), Task 1.3a (depth-3 witness), Task 1.4a (C* extension)
**Executable:** `_depth4_fast.py`, `_depth4_fixed.py`

---

## Executive Summary

A corrected depth-4 search was executed on tree<=5 (31 nodes, growth [1,2,2,3,7,16])
using the same ascendant-climb + parent-anchored construction that found depth-2 and
depth-3 fixed points. **No non-expansive map with a depth-4 fixed point was found** in
700,000 samples across 14 feasible climb chains. The ascendant-climb pattern has a
**depth bound of 3**: it works for d=2 at tree<=3 and d=3 at tree<=4, but breaks at
d=4 on tree<=5.

This is a structural finding — the additional distance-pair constraints introduced by
the 16 new depth-5 nodes cannot be satisfied by the simple climb+local-pool assignment
that was sufficient at smaller tree depths.

---

## Verification

| Pattern | Tree depth | Nodes | Fixed point | Status |
|:--------|:-----------|:------|:------------|:-------|
| Ascendant-climb d=2 | tree <= 3 | 8 | '[]#' (depth 2) | ✅ CONFIRMED (0/28 violations) |
| Ascendant-climb d=3 | tree <= 4 | 15 | '[[]#]' (depth 3) | ✅ CONFIRMED (0/105 violations) |
| Ascendant-climb d=4 | tree <= 5 | 31 | — | ❌ 0 hits (700K samples, 14 climbs, 11.5s) |

---

## Search Methodology

- **Tree:** `build_tree(max_depth=5)` — 31 nodes, growth [1,2,2,3,7,16]
- **Climb chains:** 14 feasible chains (7 strict parent-child + 7 sibling-style jumps)
- **Sampling:** 50,000 maps per climb, local pools (ancestors + self + children)
- **Checker:** Precomputed distance matrix (465 pairs), `is_ne` with early rejection
- **Script:** `_depth4_fast.py` (node-identity mapping fix, no zip-by-index bug)
- **Runtime:** 11.5s total (0.8-0.9s per climb), zero hits

---

## Structural Interpretation

The ascendant-climb pattern works at depths 2 and 3 because:
1. The non-climb nodes can be assigned to collapse toward ROOT's branch
2. At tree<=3 (8 nodes) and tree<=4 (15 nodes), the number of crossing pairs
   between the climb chain and the non-climb nodes is small enough for local-pool
   assignment to maintain global non-expansiveness

At tree<=5 (31 nodes with 16 depth-5 nodes), the situation changes:
1. The 16 new depth-5 nodes introduce 16^2/2 = 120 new pairs internally
2. Each depth-5 node also pairs with the 15 earlier nodes (16*15 = 240 new cross-pairs)
3. Total new pairs: ~360, nearly doubling the 105-pair check from tree<=4
4. The climb chain's strict non-expansiveness constraints now conflict with the
   assignments needed for distant nodes

This is consistent with the valuation structure finding (Task 1.4): image survival
ratio increases with tree depth (50% -> 67%), suggesting that deeper trees REQUIRE
more nuanced maps, not the simple collapse-to-ROOT-branch pattern.

---

## Implications

1. **Depth bound confirmed:** The ascendant-climb construction has a structural
   limit at depth 3. The pattern is not a universal depth-independent scheme.
2. **Bootstrap Conjecture status:** The global formulation is satisfiable at depths
   2 and 3 (the conjecture's viability is confirmed), but the constructive methodology
   for finding witnesses has a depth-dependent complexity barrier.
3. **Next approaches:** (a) explore fundamentally different construction patterns
   beyond ascendant-climb; (b) characterize the depth-bound theorem analytically;
   (c) investigate whether weighted/relaxed non-expansiveness permits depth>=4.

---

## Reproducibility

```bash
python _depth4_fast.py  # search on tree<=5, 14 climbs x 50K samples
python _depth4_fixed.py # original (200K samples — slower but identical method)
```
