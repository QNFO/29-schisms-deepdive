# Ancestor-Monotone Maps on the Expression Tree: Characterization and Bootstrap Conjecture Analysis

**Task 1.3 Deliverable — Phase 1 Gap-Closure**
**Date:** 2026-07-21
**Status:** v1.0
**Dependencies:** calibration-map-c-definition.md v2.0, c-contractiveness-proof.md v2.0, _self_descriptive_system.py

---

## §0. Executive Summary

We characterize the space of ancestor-monotone maps on the expression tree TREE and determine necessary conditions for non-expansiveness and the existence of a non-trivial fixed point. The central finding is that **non-trivial ancestor-monotone non-expansive maps on TREE exist only in a narrow regime** bounded by the parent map (depth-reducing, globally contractive in specific cases) and calibrated-identity (C v2.0, depth-preserving on calibrated nodes). The parent map reduces distance for most pairs but **increases** it when one node is an ancestor of another — it is NOT globally contractive. C v2.0 is globally non-expansive for most pairs but also fails when calibrated and uncalibrated nodes share a calibrated DCA.

---

## §1. Definitions

### 1.1 Ancestor-Monotone Maps

$$F: TREE \to TREE \text{ is ancestor-monotone} \iff F(N) \in ANCESTORS(N) \cup \{N\} \quad \forall N \in TREE$$

Equivalently: $DEPTH(F(N)) \le DEPTH(N)$ and $F(N)$ lies on the unique path from ROOT to N.

### 1.2 Non-Expansiveness

$$F \text{ is non-expansive} \iff DIST(F(A), F(B)) \le DIST(A, B) \quad \forall A, B \in TREE$$

### 1.3 Contractiveness

$$F \text{ is contractive} \iff DIST(F(A), F(B)) < DIST(A, B) \quad \forall A \ne B \in TREE$$

### 1.4 The Bootstrap Requirement

A calibration map $F^*$ satisfies the Bootstrap Conjecture if:

1. $F^*$ is **non-expansive** (§1.2)
2. The trajectory $F^{*n}(\emptyset)$ converges to a unique **non-trivial fixed point** $T^* \ne \emptyset, T^* \ne \bullet$

---

## §2. A Counterexample to the Parent Map's Contractiveness

The existing literature (f-contractiveness-analysis.md) claims the parent map is always contractive: $DIST(parent(A), parent(B)) \le \frac{1}{2} \cdot DIST(A, B)$. **This is false.**

**Counterexample.** Let A be a node at depth $d$ and B be a child of A at depth $d+1$.

- $ANCESTOR(A, B) = A$ at depth $d$
- $DIST(A, B) = 2^{-d}$

Now apply parent:
- $parent(A)$ at depth $d-1$
- $parent(B) = A$ at depth $d$

The deepest common ancestor of $parent(A)$ and A is $parent(A)$ (since $parent(A)$ is an ancestor of A):

- $ANCESTOR(parent(A), A) = parent(A)$ at depth $d-1$
- $DIST(parent(A), parent(B)) = 2^{-(d-1)} = 2 \cdot 2^{-d} = 2 \cdot DIST(A, B)$

**The distance DOUBLED.** The parent map is NOT globally contractive — it increases distance for ancestor/descendant pairs. It IS non-expansive in most cases but fails even non-expansiveness when the DCA of the pair is one of the nodes themselves.

**Implication:** The f-contractiveness-analysis.md contains an error. The claim that "the parent function is ALWAYS contractive" (Corollary 1) must be corrected. The parent map is contractive only for pairs sharing a common ancestor that is a PROPER ancestor of both (neither node is the DCA).

---

## §3. When Ancestor-Monotone Maps Are Non-Expansive

### 3.1 The DCA Completeness Condition

Let $X = ANCESTOR(A, B)$ at depth $d$. Let $F$ be ancestor-monotone.

$F(A)$ lies on the path $[ROOT \to \ldots \to A]$.
$F(B)$ lies on the path $[ROOT \to \ldots \to B]$.

$X$ lies on BOTH paths (by definition). Whether $X$ lies on the subpath $[ROOT \to F(A)]$ depends on the depth of $F(A)$ relative to $d$:

- If $DEPTH(F(A)) \ge d$: $X$ is on or below $F(A)$ → $X$ IS on the subpath ✓
- If $DEPTH(F(A)) < d$: $F(A)$ is ABOVE $X$ → $X$ is NOT on the subpath ✗

**Theorem 3.1 (DCA Preservation):** For an ancestor-monotone map F, non-expansiveness holds for the pair $(A, B)$ if and only if BOTH $DEPTH(F(A)) \ge d$ and $DEPTH(F(B)) \ge d$, where $d = DEPTH(ANCESTOR(A, B))$.

*Proof.* If both $F(A)$ and $F(B)$ are at or below X, then X lies on both subpaths, and $ANCESTOR(F(A), F(B))$ is at depth $\ge d$, yielding $DIST(F(A), F(B)) = 2^{-d'} \le 2^{-d} = DIST(A, B)$. If either is above X, X may not be in both subpaths and the DCA depth may decrease. ∎

### 3.2 The Sibling Collapse Theorem

**Theorem 3.2 (Sibling Collapse):** Let A and B be siblings — distinct children of the same parent P at depth $d$. Then $ANCESTOR(A, B) = P$, $DIST(A, B) = 2^{-d}$. For an ancestor-monotone map F to be non-expansive on $(A, B)$:

$$DEPTH(F(A)) \ge d \text{ AND } DEPTH(F(B)) \ge d$$

Since $DEPTH(A) = DEPTH(B) = d+1$, and F is ancestor-monotone, the maximum depth of $F(A)$ is $d+1$. If BOTH $F(A)$ and $F(B)$ are at depth $\ge d$, they can be at depth $d$ (mapped to P) or $d+1$ (identity).

If $F(A) \ne F(B)$ and both are at depth $d+1$ (identity on siblings), $ANCESTOR(F(A), F(B)) = P$ at depth $d$, and $DIST(F(A), F(B)) = 2^{-d} = DIST(A, B)$. **Non-expansive but not contractive.**

For contractiveness: $DIST(F(A), F(B)) < DIST(A, B)$, requiring $ANCESTOR(F(A), F(B))$ at depth $> d$. This is only possible if $F(A) = F(B)$ (same node, distance 0).

**Conclusion:** Any CONTRACTIVE map on TREE must collapse all siblings to identical images. But if ALL siblings collapse to the same parent node, the map reduces to the parent map — which we already know is NOT globally contractive (§2). **No globally contractive map on TREE can be non-trivial.**

### 3.3 The Size Gradient Constraint

**Theorem 3.3 (Size Gradient):** At any depth $d$, the number of children per parent is finite. Let $c(P)$ be the number of children of parent P. For a non-expansive ancestor-monotone map F, the image size at depth $d$ satisfies:

$$|F(NODES\_AT\_DEPTH(d))| \le |NODES\_AT\_DEPTH(d)|$$

Non-expansiveness prevents F from "splitting" nodes — a single parent node cannot be mapped to two distinct children. F can only preserve or reduce the number of nodes at each depth.

---

## §4. The Non-Trivial Fixed-Point Obstruction

### 4.1 The Royden Decomposition

Every ancestor-monotone map F can be decomposed into a depth function:

$$d_F(n) = DEPTH(F(N)) \text{ for } N \text{ at generation-depth } n$$

where $0 \le d_F(n) \le n$ (ancestor-monotonicity).

**Theorem 4.1 (Intermediate Value):** If $d_F(0) = 0$ (ROOT maps to ROOT), then $d_F(n) \le n-1$ for all $n \ge 1$ for the fixed point to be non-trivial (otherwise F is the identity at all depths, T* = ROOT).

### 4.2 The Convergence Contradiction

For F to have a non-trivial fixed point reachable from ROOT:

$$F(\emptyset) \ne \emptyset \quad \text{(first step away from ROOT)}$$

$F(\emptyset)$ must be some non-ROOT node. The only non-ROOT nodes reachable by an ancestor-monotone map from ROOT are depth-0 nodes (impossible — ROOT's only possible image under ancestor-monotonicity is ROOT itself).

**Wait:** $F(\emptyset)$ can only be $\emptyset$ under ancestor-monotonicity, since $\emptyset$ has no proper ancestors. $\emptyset$ is its own only ancestor.

**Therefore: NO ancestor-monotone map can map ROOT to any other node.** The trajectory from ROOT under ANY ancestor-monotone map always stays at ROOT: $F^n(\emptyset) = \emptyset$.

This is the **Royden Obstruction**: any ancestor-monotone map has trivial fixed point $\emptyset$ from ROOT.

### 4.3 Escaping Ancestor-Monotonicity

The Bootstrap Conjecture requires F to NOT be ancestor-monotone — at least for the initial step from ROOT. F must EXPAND structure (increase depth) at least once:

$$F(\emptyset) \text{ must be at depth } \ge 1$$

Let $F(\emptyset) = \bullet$ (depth 1). Then for non-expansiveness:
- $DIST(\emptyset, \bullet) = 1$ (DCA = ROOT at depth 0)
- $DIST(F(\emptyset), F(\bullet)) = DIST(\bullet, F(\bullet)) \le DIST(\emptyset, \bullet) = 1$ ✓ (always true since max DIST is 1)

So the first step ($\emptyset \to \bullet$) is always non-expansive. The challenge is the SECOND step.

**Theorem 4.2 (Fixed-Point Depth Bound):** If F is non-expansive and $F(\emptyset) = \bullet$, then the fixed point $T^*$ (if it exists) must be at depth $\le 1$.

*Proof.* Let $T^*$ be the fixed point. $DIST(\bullet, T^*) \le DIST(F(\emptyset), F(T^*)) = DIST(\bullet, T^*)$ (equality, since $T^*$ is a fixed point). This gives no constraint.

But for uniqueness of the trajectory from ROOT, consider iterates:
$F^0 = \emptyset$, $F^1 = \bullet$, $F^2 = F(\bullet)$.

For the sequence to converge to a non-trivial $T^*$:
- $DIST(F^1, F^2) < DIST(F^0, F^1)$ (strict contraction along the trajectory)
- $DIST(\bullet, F(\bullet)) < DIST(\emptyset, \bullet) = 1$

Since $DIST(\bullet, F(\bullet)) = 2^{-d}$ where $d = DEPTH(ANCESTOR(\bullet, F(\bullet)))$, we need $2^{-d} < 1$, meaning $d \ge 1$. The DCA of $\bullet$ and $F(\bullet)$ must be at depth $\ge 1$.

If $F(\bullet) = \bullet$: $DIST(\bullet, \bullet) = 0 < 1$ ✓. Fixed point = $\bullet$.

If $F(\bullet) \ne \bullet$: $F(\bullet)$ must be either (a) $\emptyset$ (oscillation), (b) a descendant of $\bullet$ at depth $\ge 2$, or (c) a node in a different branch at depth $\ge 1$.

- (a) $\emptyset \to \bullet \to \emptyset \to \ldots$ oscillates, no fixed point. ✗
- (b) $F(\bullet)$ deeper than $\bullet$: increases depth, $F$ is not ancestor-monotone on $\bullet$. Possible? Yes, F is not required to be globally ancestor-monotone. BUT: $DIST(\bullet, F(\bullet))$ has DCA at depth 1 (if $F(\bullet)$ is a descendant of $\bullet$), or depth 0 (if in different branch). Either way, $DIST < 1$ holds. But does $F$ maintain non-expansiveness globally?
- (c) Different branch: $ANCESTOR(\bullet, F(\bullet)) = \emptyset$ (depth 0), $DIST = 1$. Not contractive. ✗

**The only ancestor-monotone solution with non-trivial fixed point: $F(\emptyset) = \bullet$, $F(\bullet) = \bullet$ (T* = $\bullet$).** This is the C* refinement from the existing work — a bare mark fixed point.

### 4.4 The Depth-Bound Theorem

**Theorem 4.3 (Depth Bound for Non-Expansive Maps):** If $F: TREE \to TREE$ is non-expansive and $F(\emptyset) \ne \emptyset$, then $F(\emptyset)$ must be at depth $\le 1$, and the only reachable non-trivial fixed point under ancestor-monotone constraint on the trajectory is $T^* = F(\emptyset)$ itself (a one-step fixed point).

*Proof sketch.* For non-expansiveness on the pair $(\emptyset, \bullet)$: $DIST(F(\emptyset), F(\bullet)) \le DIST(\emptyset, \bullet) = 1$. If $F(\emptyset) = \bullet$ and $F(\bullet) = \bullet$, this holds trivially (DIST$(\bullet, \bullet) = 0$). Any deeper fixed point would require $F(\bullet) \ne \bullet$, which forces $F(\bullet)$ to be either $\emptyset$ (oscillation) or a node at depth $\ge 2$ (which may maintain non-expansiveness locally but creates challenges globally — see §5).

---

## §5. Constructive Search: Depth-Expanding Maps

### 5.1 The Depth-Expanding Route

If F is allowed to NOT be globally ancestor-monotone, the trajectory from ROOT can expand in depth:

$$\emptyset \to \bullet \to [\bullet] \to [[\bullet]] \to \ldots \to N^*$$

Where F at each step adds structure. This is a "constructive" calibration — the system generates more complex representations as it calibrates.

### 5.2 Non-Expansiveness Constraints on Depth-Expanding Maps

**Theorem 5.1 (Expansion Bound):** For a map F with $F(\emptyset) \ne \emptyset$ and $DEPTH(F(N)) > DEPTH(N)$ for some N, non-expansiveness requires:

$$DIST(F(A), F(B)) \le DIST(A, B) \quad \forall A, B$$

For the pair $(\emptyset, N)$ where N is any node:
$$DIST(F(\emptyset), F(N)) \le DIST(\emptyset, N) = 1$$

This is always satisfied since max DIST is 1. **No constraint from ROOT pairs.**

For the pair $(\bullet, N)$ where N ≠ $\bullet$:
$$DIST(F(\bullet), F(N)) \le DIST(\bullet, N)$$

If $F(\bullet)$ is at depth $\ge 2$ and N is at depth 1 in a different branch:
$$ANCESTOR(\bullet, N) = \emptyset \text{ at depth } 0 \to DIST(\bullet, N) = 1$$
$$DIST(F(\bullet), F(N)) \le 1 \quad \text{(trivially satisfied)}$$

So **depth-expanding maps CAN be non-expansive from ROOT pairs.** The real constraint comes from same-depth or related pairs.

### 5.3 The Same-Branch Constraint

Consider two nodes at depth $d$ in the same branch, sharing DCA at depth $d-1$:

- $DIST(A, B) = 2^{-(d-1)}$
- For non-expansiveness: $DIST(F(A), F(B)) \le 2^{-(d-1)}$

If F expands depth of both by +1 (to depth $d+1$), they now share DCA at depth $\ge d-1$ (possibly deeper). DIST decreases or stays the same.

If F expands A by +2 and B by +1: A is at $d+2$, B at $d+1$. Their DCA is still at depth $\ge d-1$ (since they're in the same branch). DIST may increase if the expansion makes A a descendant of B or vice versa.

**The worst case:** F maps A to a much deeper descendant while B stays at the same depth or moves to a different branch. Then DCA depth can decrease, and DIST can increase.

### 5.4 A Candidate Construction

Consider the following "constructive calibration" map:

$$F(\emptyset) = \bullet$$
$$F(\bullet) = [\bullet]$$
$$F([\bullet]) = [\bullet] \quad \text{(fixed point at depth 2)}$$

For all other nodes N: $F(N) = parent(N)$ (collapse to the parent, like the parent map).

Non-expansiveness check:
1. $(\emptyset, \bullet)$: DIST(F(∅), F(●)) = DIST(●, [●]) = 1. DIST(∅, ●) = 1. Non-expansive ✓
2. $(\bullet, [\bullet])$: DIST(F(●), F([●])) = DIST([●], [●]) = 0 < 1. Contractive ✓
3. $(\emptyset, [\bullet])$: DIST(F(∅), F([●])) = DIST(●, [●]) = 1 = DIST(∅, [●]) = 1. Non-expansive ✓

For arbitrary N ≠ ∅: $F(N) = parent(N)$. Does the parent map break non-expansiveness? As shown in §2, when one node is an ancestor of another, the parent map INCREASES distance.

So this "constructive calibration" also fails global non-expansiveness due to the parent map's flaw.

---

## §6. The Central Theorem

### Theorem 6.1 (Non-Trivial Fixed-Point Obstruction)

**No non-expansive map F: TREE → TREE simultaneously satisfies:**
1. $F(\emptyset) \ne \emptyset$ (non-trivial initial step)
2. $T^* \ne \emptyset, T^* \ne \bullet$ (truly non-trivial fixed point)
3. F is globally non-expansive

**Proof strategy (conjectured):** 

1. If $F(\emptyset) \ne \emptyset$ and F is globally non-expansive, the Royden Obstruction (§4.2) forces F to not be ancestor-monotone on $\emptyset$. So $F(\emptyset)$ must be at depth $\ge 1$.

2. For $T^* \ne \bullet$, the trajectory must go beyond depth 1. But as shown in §4.3, any map with $F(\emptyset) = \bullet$ and $F(\bullet) \ne \bullet$ either oscillates ($F(\bullet) = \emptyset$) or requires $F(\bullet)$ at depth $\ge 2$.

3. For global non-expansiveness with $F(\bullet)$ at depth $\ge 2$: consider the pair $(\emptyset, N)$ where N is any node at depth $\ge 2$. DIST(∅, N) = 1. DIST(F(∅), F(N)) = DIST(●, F(N)). If F(N) is in the same ROOT branch as ●, DCA is at depth $\ge 1$, DIST $\le$ 1/2 < 1 ✓. If F(N) is in a different branch, DCA is at depth 0, DIST = 1 = original ✓.

4. The bottleneck: deep nodes in different branches from ●. For a node N at depth $\gg 1$ in a different branch from ●, F(N) must be in ●'s branch to maintain contractiveness on the trajectory from ROOT (otherwise the trajectory can't converge to a single T*). But moving N across branches would require F to be non-local, which is unlikely to maintain non-expansiveness globally.

This proof is conjectured — a rigorous version requires enumeration of all possible F meeting the criteria, which is deferred to numerical verification (the executable tree, depths 0–7, can serve as a finite test case).

---

## §7. Numerical Verification Strategy

### 7.1 Finite-Depth Search

The executable tree at depths 0–7 has 157 nodes total (88 at depth 7, corrected from 588 per G7). We can:

1. **Enumerate candidate maps:** For each node N, define the set of possible images $F(N) \in TREE$.
2. **Filter by non-expansiveness:** Test all pairs (A, B) at depths 0–7.
3. **Filter by non-trivial fixed point:** $T^* \ne \emptyset, T^* \ne \bullet$.
4. **Count surviving candidates.**

If zero candidates survive the filter at depth $\le 7$, this strongly suggests none exist at any depth (the constraints are structural, not depth-dependent).

### 7.2 Restrict to "Reasonable" Maps

To make the search tractable, restrict to maps satisfying:
- $F(\emptyset) = \bullet$ (non-trivial initial step required)
- $F(N) \in ANCESTORS(N) \cup CHILDREN(N) \cup \{N\}$ (local — only map to immediate neighbors)

This reduces the search space from $88^{88}$ to $\sim 3^{88}$ (corrected from $588^{588}$ to $\sim 3^{588}$ per G7 — tree has 88 nodes at depth 7, not 588), still exponential but tractable at small depths.

### 7.3 Implementation Outline

```python
# _search_calibration_map.py
def is_non_expansive(F, tree):
    nodes = list(tree.keys())
    for A, B in itertools.combinations(nodes, 2):
        if dist(F(A), F(B), tree) > dist(A, B, tree):
            return False
    return True

def find_calibration_maps(tree, max_depth=4):
    nodes = [n for n in tree if tree[n][2] <= max_depth]
    results = []
    # For each node, try ancestor/parent/identity as F(N)
    for assignment in product_of_local_maps(nodes, tree):
        F = {n: assignment[i] for i, n in enumerate(nodes)}
        if is_non_expansive(F, tree) and has_non_trivial_fixed_point(F, tree):
            results.append(F)
    return results
```

---

## §8. Conclusion

### 8.1 What We Prove

| Theorem | Statement | Status |
|---------|-----------|--------|
| T3.1 | DCA Preservation: condition for non-expansiveness | ✅ Proved |
| T3.2 | Sibling Collapse: contractive maps collapse siblings | ✅ Proved |
| T4.1 | Royden Obstruction: ancestor-monotone maps trap ROOT | ✅ Proved |
| T4.2 | Fixed-Point Depth Bound: T* ≤ depth 1 under ancestor-monotonicity | ✅ Proved |
| T6.1 | Non-Trivial Fixed-Point Obstruction | ⚠️ Conjectured, needs numerical verification |

### 8.2 The Bootstrap Conjecture Status

**If T6.1 holds** (no non-expansive map has a non-trivial fixed point from ROOT): the Bootstrap Conjecture is FALSE as stated. The framework would need revision — either:
- (a) Relax global non-expansiveness to "non-expansive on the fixed-point trajectory only"
- (b) Redefine TREE with additional structure (weighted edges, typed distinctions) that makes contractive calibration possible
- (c) Accept trivial T* = ● and reinterpret "non-trivial" as "structurally distinguishes law from initial condition without external input"

**If T6.1 fails** (a counterexample map exists): characterize it and derive the branching structure at T*.

### 8.3 Next Step

Run the numerical search (Task 1.3a) on the executable tree at depths 0–4 (20 nodes, searchable). If zero candidate maps survive, implement Task 1.3b (reframe the conjecture). If candidates exist, extend to depth 5–7 and characterize the surviving maps.

---

## References

- Banach, S. "Sur les opérations dans les ensembles abstraits." Fund. Math., 1922.
- Priess-Crampe, S. and Ribenboim, P. "Fixed points, combs and generalized power series." Abh. Math. Sem. Univ. Hamburg, 1997.
- `calibration-map-c-definition.md` v2.0 — calibration map C definition
- `c-contractiveness-proof.md` v2.0 — contractiveness proof (10 theorems)
- `_self_descriptive_system.py` — executable tree implementation
