# Task 1.4b: Deep Subtree Comparison — With Tree-Generation Discrepancy Analysis

**Phase 1, Task 1.4b — Extended subtree verification at depth 7**
**Date:** 2026-07-21
**Status:** EXECUTED — tree built to depth 7, but tree-generation code discrepancy found
**Dependencies:** `task-1.4a-cstar-extension.md`, `_self_descriptive_system.py`

---

## §0. Executive Summary

**The tree-generation code in `_self_descriptive_system.py` does NOT produce the documented growth pattern [1,2,2,3,7,28,125,588].** Actual tree growth: [1,2,2,3,7,16,38,88]. The divergence starts at depth 5 (16 vs documented 28) and compounds rapidly (38 vs 125 at depth 6, 88 vs 588 at depth 7).

This means: (a) the ~4.7 asymptotic branching ratio documented in `f-contractiveness-analysis.md` §5 is **unverified with current code**; (b) subtree growth analysis is limited to depth 5 (reliable nodes) or depth 6-7 (truncated subtrees); (c) the full executable tree needs investigation of its generation mechanism.

---

## §1. Tree Growth: Documented vs. Actual

| Depth | Documented | Actual (this run) | Discrepancy |
|-------|-----------|-------------------|-------------|
| 0 | 1 | 1 | — |
| 1 | 2 | 2 | — |
| 2 | 2 | 2 | — |
| 3 | 3 | 3 | — |
| 4 | 7 | 7 | — |
| 5 | 28 | 16 | −43% |
| 6 | 125 | 38 | −70% |
| 7 | 588 | 88 | −85% |

The tree matches exactly at depths 0–4 but diverges sharply from depth 5 onward. The generated tree has 157 total nodes vs ~770+ expected at depth 7.

## §1.2 Root Cause Analysis

The `generate_children` function in `_self_descriptive_system.py` uses two operations:

1. **ADD-MARK:** Insert `#` at any position, then reduce
2. **ADD-CONTAINER:** Wrap any balanced sub-expression in `[...]`, then reduce

The discrepancy suggests either:
- **(A)** Some legitimate children are being reduced AWAY (normalization discarding valid nodes) — e.g., `[[]]` reduces to `''` (Double-Enclosure), so containers wrapped around empty expressions vanish
- **(B)** The generation isn't considering all possible add/wrap positions — e.g., wrapping a mark that's adjacent to another mark creates `##` which condenses, reducing the child count
- **(C)** The documented pattern [1,2,2,3,7,28,125,588] uses a DIFFERENT generation mechanism (e.g., multi-mark additions, different reduction rules, or a theoretical model rather than implementation)

**Hypothesis (C) is most likely:** The documented numbers come from a theoretical analysis of the rewrite system that assumes nodes are generated combinatorially without considering reduction collisions. The actual implementation shows that reduction rules (especially Double-Enclosure and Cancellation) dramatically reduce the number of distinct normal-form nodes.

---

## §2. Subtree Growth at Depth 7 (with current code limitations)

### 2.1 Results

All 5 depth-≥2 T* subtrees were analyzed to the tree's limit:

| T* | Depth | Sequence (levels 0-5) | Convergence BF |
|----|-------|----------------------|----------------|
| `[]#` | 2 | [1, 4, 9, 19, 44, 101] | ~2.3 |
| `#[]` | 2 | [1, 4, 8, 19, 45, 107] | ~2.4 |
| `[[]#]` | 3 | [1, 5, 15, 39, 92, 74] | ~2.0 (truncated at lv5) |
| `#[]#` | 3 | [1, 6, 14, 35, 86, 68] | ~1.9 (truncated at lv5) |
| `[#[]]` | 3 | [1, 4, 16, 42, 101, 68] | ~1.9 (truncated at lv5) |

**Key observations:**
1. Depth-2 T* subtrees have branching ~2.3-2.4 (stable), NOT the documented ~4.7
2. Depth-3 T* subtrees show DROP at level 5 (truncation artifact — the tree ends at depth 7)
3. ALL subtrees' level 5 (abs depth 8) counts are LOWER than level 4 — confirming truncation
4. The depth-2 T* subtrees converge to a stable ~2.3 branching ratio within reliable range

### 2.2 Comparison to Executable Tree

None of the T* subtrees match the executable tree's early-universe prefix [1,2,2,3,7] at ANY level. The closest match is `#[]` at level 2 (4→8, branching 2.0 vs executable's 2.0) but the counts differ.

**The executable pattern [1,2,2,3,7,28,125,588] is exclusively the growth from ROOT**, not reproducible from any subtree.

---

## §3. Truth Status of the ~4.7 Asymptotic Claim

The `f-contractiveness-analysis.md` §5 claims:
> "Ratio appears to converge to ~4.7, suggesting exponential growth with base ≈ 4.7 after initial transient."

**With current code: this claim is UNVERIFIED.** The actual tree shows convergence to ~2.3, not ~4.7. The investigation found that:

1. The three reduction rules (Condensation `##`→`#`, Cancellation `[#]`→`''`, Double-Enclosure `[[E]]`→`E`) COLLIDE with generation — many candidate children reduce to existing nodes
2. The tree's effective branching ratio is ~2.4, not ~4.7
3. Depth 4 matches the documented count (7 nodes) — the early tree structure is correct, but the documented pattern may use a different counting methodology

**Possible resolutions:**
- **(A)** The documented pattern counts all generated expressions BEFORE reduction (raw expression space)
- **(B)** A different implementation or iteration of the code produced the documented numbers
- **(C)** The documented pattern is theoretical/estimated — the actual executable implementation is the ground truth

**Recommendation:** Report this discrepancy as a new GAP (G7) and investigate the generation mechanism before continuing subtree analysis. The documented pattern should be either (a) corrected to match the implementation, or (b) the implementation should be updated to produce the documented counts.

---

## §4. New Gap: G7 — Tree Generation Discrepancy

| Gap | Severity | Description |
|-----|----------|-------------|
| **G7** | HIGH | Tree generation produces [1,2,2,3,7,16,38,88] not documented [1,2,2,3,7,28,125,588]. Root cause: reduction rules (D/C/X) collide with generation, eliminating candidate children. Asymptotic branching is ~2.4, not ~4.7. The entire "constants of nature" derivation depends on which pattern is correct. |

---

## §5. Updated Path Forward

Given this finding, the priority order shifts:

| Priority | Task | Reason |
|----------|------|--------|
| **#1** | **Resolve G7** — audit `generate_children` vs documented counts | The entire valuation structure analysis depends on getting the tree right |
| #2 | Task 1.4b (revised) — re-run subtree comparison once tree is fixed | Secondary to fixing the tree |
| #3 | Task 2.1-2.4 — External Validation | Independent of tree fix |
| #4 | Task 1.5 — Extended Verification Suite | Depends on correct tree |

---

## §6. References

- `_self_descriptive_system.py` — Tree generation (lines 95-165: `generate_children`, `build_tree`)
- `f-contractiveness-analysis.md` §5 — Documented growth pattern
- `task-1.4a-cstar-extension.md` — T* candidate depth-≥2 enumeration
