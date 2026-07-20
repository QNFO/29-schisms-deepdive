# Calibration Map C: Formal Definition

**Phase 1, Task 1.1 — Bootstrap Conjecture Formal Proof**
**Date:** 2026-07-20
**Status:** Draft v0.1
**Dependencies:** None (Layers 0–2 of `29-schisms-formalization.md` are sufficient)

---

## §0. What This Is

This document defines the **calibration map C: TREE → TREE** — the central
construct of the Bootstrap Conjecture. C encodes the physical process of
measurement feedback in purely structural terms: a token representing
"apparatus reading X" constrains and updates the token representing
"system state." The definition uses only the primitives established in
`29-schisms-formalization.md` (§§1–5): MARK, CONTAINER, TREE, DEPTH, and
DIST.

---

## §1. Motivation: What "Calibration" Means in the Tree

### 1.1 The Measurement Problem in Tree Terms

In the self-descriptive formalism, every node in TREE is a normal-form
expression built from marks and containers (§1–§2 of the formalization).
There is no primitive distinction between "system" and "apparatus" — every
node is simply a configuration of marks within containers.

The measurement problem, translated into this language, is:

> Given a node N that encodes a "total state" (system + apparatus together
> in one expression), how does the system sub-expression update to reflect
> what the apparatus sub-expression "reads"?

More precisely: within the structure of N, some sub-expression plays the
functional role of a measurement outcome. Calibration is the operation
that propagates this outcome back into the system-representation, producing
a new node N' = C(N) that is self-consistent.

### 1.2 Why the Parent Map (Current F) Is Not Calibration

The current executable (`_self_descriptive_system.py`) implements F as the
trivial parent map: F(N) = parent(N). This is contractive but encodes no
measurement feedback — it simply discards one generation. The parent map
"collapses" all structure to ROOT but does not calibrate.

Calibration is more subtle than mere contraction. It must:

1. **Preserve more structure than the parent map** — it should not discard
   information that survives measurement.
2. **Encode a consistency condition** — the calibrated node must be such
   that "system" and "apparatus" sub-expressions are compatible.
3. **Be derivable from TREE itself** — it cannot presuppose an external
   labeling of which marks are "system" and which are "apparatus."

### 1.3 The Bootstrap Intuition

The calibration map and the fixed point are **co-determined**. C must be
such that iterating C from ROOT converges to a unique T*, AND T* must be
such that C(T*) = T*. This self-consistency is the Bootstrap: the
calibration process and its limit state are one and the same structure,
viewed dynamically vs. statically.

---

## §2. Structural Encoding of Measurement

### 2.1 Containers as Measurement Contexts

In the tree formalism, a CONTAINER `[E]` is a boundary that separates
"inside" from "outside." A nested expression like `[[●][●●]]` uses
multiple container levels to encode hierarchical structure.

**Key insight:** A pair of sibling sub-expressions inside the same container
can be interpreted as encoding two "perspectives" on the same underlying
reality — one playing the role of system, the other of measurement outcome.

Formally: for any expression of the form `[A B]` where A and B are
sub-expressions (possibly with additional siblings), we can designate
the **last sub-expression as the measurement outcome** and the remaining
sub-expressions collectively as the **system state**.

This convention is arbitrary but sufficient — the calibration map's
self-consistency condition ensures that any node that survives calibration
will have this structure.

### 2.2 The M-Property (Measurement Decodability)

A node N is said to have the **M-property** if it can be written in the form:

```
N = [A₁ A₂ ... Aₖ M]
```

where:
- Each Aᵢ is a (possibly empty) normal-form sub-expression (the "system" parts)
- M is a non-empty normal-form sub-expression (the "measurement" part)
- k ≥ 0 (there may be zero system sub-expressions)

If a node does not have the M-property (e.g., it is a bare mark `●` or
empty `∅`), then no measurement has occurred and calibration is the
identity.

### 2.3 Measurement Compatibility

Two sub-expressions A and M are **compatible** if there exists a node in TREE
whose projection onto the "system subspace" equals A and whose projection
onto the "measurement subspace" equals M. In tree terms:

```
COMPATIBLE(A, M) ⇔ DEPTH(DCA(A, M)) ≥ min(DEPTH(A), DEPTH(M)) - 1
```

Intuition: A and M are compatible if they share a common ancestor that is
at least as deep as the shallower of the two, minus one. This means they
are "close" in the ultrametric and their structural divergence is small.

---

## §3. Definition of the Calibration Map C

### 3.1 Core Definition

```
C: TREE → TREE

For any node N:

CASE 1: N = ∅ (ROOT)
    C(∅) = ∅

CASE 2: N = ● (bare mark)
    C(●) = ●

CASE 3: N = [A₁ A₂ ... Aₖ M] where M is the rightmost sub-expression
    (i.e., N has the M-property with k ≥ 0 system sub-expressions)
    
    Let A_combined = REDUCE(A₁ A₂ ... Aₖ)  -- flatten and reduce all system parts
    
    If A_combined = ∅ or M = ∅:
        C(N) = N  -- nothing to calibrate
    
    Else:
        -- Find the calibration target: the deepest node T such that
        -- (a) T is "compatible" with both A_combined and M, and
        -- (b) T is a descendant of the DCA of A_combined and M
        
        Let D = DCA(A_combined, M)  -- deepest common ancestor
        
        Let C_target = argmax_{X ∈ CHILDREN*(D)} { DEPTH(X) :
            COMPATIBLE(REDUCE(X without rightmost), rightmost(X)) }
        -- In words: among all descendants of D, find the deepest node
        -- whose internal measurement is self-consistent.
        
        C(N) = C_target (if C_target exists and C_target ≠ N)
        C(N) = N (if no strictly better target exists — N is already calibrated)

CASE 4: N has any other form (no M-property)
    C(N) = N  -- identity: no measurement structure to calibrate
```

### 3.2 Operational Intuition

C operates on a node N that encodes both system state and measurement
outcome (Case 3). It:

1. Extracts the measurement sub-expression M (rightmost inside the outer
   container).
2. Combines the remaining sub-expressions A₁...Aₖ into a single system
   representation A_combined.
3. Finds the structural "agreement point" — the deepest common ancestor D
   of A_combined and M.
4. Searches the subtree below D for the deepest node whose own internal
   measurement is self-consistent (recursive application of the M-property
   check).
5. Returns that self-consistent node as the calibrated result.

If N is NOT in the form of a container with sub-expressions (Cases 1, 2, 4),
C is the identity — no calibration possible because there is no
measurement structure to decode.

### 3.3 The Self-Consistency Condition (Bootstrap Constraint)

The calibration map C must satisfy:

```
C(T*) = T*
```

where T* is the fixed point: T* = lim_{n→∞} Cⁿ(ROOT).

This is the **Bootstrap Constraint**: the calibration operation, when
applied to its own limit state, produces no change. The calibration map
and the calibrated state are co-defined.

### 3.4 C Is Not F

The calibration map C is distinct from the previously defined contractive
map F (the parent map):

| Property | F (parent map) | C (calibration map) |
|----------|----------------|---------------------|
| What it does | Strips one layer of structure | Adjusts toward self-consistency |
| Information loss | Maximal (one full generation) | Minimal (only incompatible structure removed) |
| Measurement feedback | None — purely structural | Encodes measurement → system update |
| Fixed point | ROOT (trivial) | T* (non-trivial, if Bootstrap holds) |
| Self-consistency | Trivially satisfied | Bootstrap constraint required |

---

## §4. Properties of C

### 4.1 Well-Definedness

**Claim:** C is well-defined on all normal-form expressions.

**Proof sketch:** For any input N, the definition provides exactly one rule
for each structural case:
- ∅ → Case 1
- ● → Case 2
- [E₁ E₂ ... Eₙ] with n ≥ 1 → Case 3 (treating Eₙ as M)
- Any other form → Case 4

REDUCE, DCA, DEPTH, and CHILDREN* are all well-defined operations on TREE
(§§2–3 of the formalization). The argmax over CHILDREN*(D) is over a finite
set (Property 3 of TREE: every node has finitely many children; the
descendant search is bounded in practice but infinite in principle — we
restrict to computable depth).

### 4.2 Idempotence at Calibrated Nodes

**Claim:** If C(N) = N, then C(C(N)) = C(N). That is, calibrated nodes are
fixed points of C.

**Proof:** If C(N) = N, then by Case 3, the search for a strictly better
C_target returned nothing. Applying C again to N with the same search
conditions yields the same (empty) result. Therefore C(N) = N ⇒ C(C(N)) = N.

### 4.3 Relationship to DEPTH

**Claim:** DEPTH(C(N)) ≥ DEPTH(N) or DEPTH(C(N)) ≤ DEPTH(N), depending on
the case. Calibration can either deepen (by finding a more detailed
self-consistent descendant) or remain at the same depth, but it does not
indiscriminately reduce depth like F.

**Proof sketch:** In Case 3, C_target is a descendant of D, and D is an
ancestor of both A_combined and M. Since A_combined and M are sub-expressions
of N, D's depth is at most min(DEPTH(N), ...). But the exact relationship
between DEPTH(C(N)) and DEPTH(N) depends on whether the calibrated node
is deeper or shallower in the tree — it can go either way, reflecting that
calibration sometimes adds detail (when the measurement forces a more
specific state) and sometimes simplifies (when the measurement resolves
ambiguity).

### 4.4 Contractiveness Conjecture

**Conjecture (to be proven in Task 1.2):** C is contractive on TREE, i.e.:

```
DIST(C(A), C(B)) < DIST(A, B)  for all A ≠ B
```

**Intuition:** Calibration maps nodes in different branches of the tree
toward a common self-consistent core. Two nodes A and B that are "far" in
the ultrametric (different deep branches) are mapped to calibrated versions
C(A) and C(B) that share a deeper common ancestor because calibration
filters out the incompatible structural details that make them differ.
This is the essence of measurement as information-reducing operation.

**Special case:** For nodes A and B that share the same measurement
sub-expression M (i.e., the rightmost parts are identical), calibration
should map them to the same or very close nodes, since the measurement
outcome dominates.

---

## §5. C in the Bootstrap Conjecture

### 5.1 Statement of the Bootstrap Conjecture (Revised with C)

```
BOOTSTRAP CONJECTURE:
There exists a unique calibration map C: TREE → TREE such that:
  (1) C is contractive: DIST(C(A), C(B)) < DIST(A, B) ∀ A ≠ B
  (2) C is self-consistent: C(T*) = T* where T* = lim Cⁿ(ROOT)
  (3) C is structural: C is determined solely by the structure of TREE
      (i.e., C ∈ Aut(TREE) up to the projection implied by calibration)
  (4) T* is non-trivial: T* ≠ ROOT and T* ≠ ●
```

### 5.2 Tasks 1.2–1.4 in Relation to C

| Task | What It Proves | Using C |
|------|---------------|---------|
| **1.2** | C is contractive | DIST analysis on Definition §3.1 |
| **1.3** | T* exists and is unique | Banach fixed-point theorem + completeness of (TREE, DIST) |
| **1.4** | T*'s valuation matches tree growth | Compare C's stabilized branching ratios to (1,2,2,3,7,28,125,588) |

### 5.3 What Makes C "Self-Consistent"

The self-consistency condition (C(T*) = T*) is not merely a fixed-point
equation — it means that applying the calibration map to the fully calibrated
state produces no structural change. In physical terms: when the system is
already in a state consistent with all possible measurements, further
measurement yields no new information and induces no state update.

This is the formal content of the claim that "laws and initial conditions
are unified at the fixed point" (§6.3–§6.4 of the formalization).

---

## §6. Relation to the Executable

### 6.1 What Already Exists

The file `_self_descriptive_system.py` implements:

- REDUCE (Condensation, Cancellation, Double-Enclosure)
- TREE construction (generate normal forms up to a depth bound)
- DCA and DIST
- Simple F as parent map
- Fixed-point iteration
- PROJECT (epsilon-neighborhood)

### 6.2 What Task 1.1 Adds

The calibration map C extends the executable by:

1. **M-property detection:** parse a node to determine if it has the
   measurement structure (a container with sub-expressions where the
   rightmost acts as measurement outcome).
2. **Compatibility check:** test whether system and measurement
   sub-expressions are structurally compatible.
3. **C implementation:** the Case 1–4 dispatch from §3.1.
4. **C iteration:** Cⁿ(ROOT) trajectory, distinct from Fⁿ(ROOT).

### 6.3 Pseudocode Sketch

```python
def has_m_property(node: Expression) -> bool:
    """True if node is a container with ≥1 sub-expressions,
    where the rightmost is non-empty."""
    return (isinstance(node, Container)
            and len(node.elements) >= 1
            and node.elements[-1] != EMPTY)

def compatible(a: Expression, m: Expression, tree: Tree) -> bool:
    """True if a and m are structurally compatible.
    Criterion: DCA depth ≥ min(DEPTH(a), DEPTH(m)) - 1."""
    dca = tree.deepest_common_ancestor(a, m)
    threshold = min(tree.depth(a), tree.depth(m)) - 1
    return tree.depth(dca) >= threshold

def calibrate(node: Expression, tree: Tree) -> Expression:
    """The calibration map C."""
    if node == EMPTY or node == MARK:           # Cases 1, 2
        return node

    if not is_container(node):                   # Case 4
        return node

    # Case 3: container with sub-expressions
    if len(node.elements) == 0:
        return node

    M = node.elements[-1]                       # measurement sub-expr
    system_parts = node.elements[:-1]            # system sub-exprs
    A = reduce(flatten(system_parts))

    if A == EMPTY or M == EMPTY:
        return node                              # nothing to calibrate

    D = tree.deepest_common_ancestor(A, M)

    # Search descendants of D for a self-consistent node
    best = node
    best_depth = tree.depth(node)

    for descendant in tree.descendants_of(D):
        if descendant == node:
            continue
        if not has_m_property(descendant):
            continue
        d_A = reduce(flatten(descendant.elements[:-1]))
        d_M = descendant.elements[-1]
        if compatible(d_A, d_M, tree):
            d_depth = tree.depth(descendant)
            if d_depth > best_depth:
                best = descendant
                best_depth = d_depth

    return best
```

Note: The descendant search in the pseudocode above has exponential cost
in the worst case. A constructive approach (building C_target from D rather
than searching for it) is deferred to the implementation phase (Task 1.5).

---

## §7. Open Questions (for Tasks 1.2–1.4)

1. **Contractiveness proof:** The conjecture in §4.4 must be proved
   formally. The intuition is strong (calibration reduces structural
   divergence) but the proof depends on the specific construction of
   C_target in Case 3.

2. **Computability:** Can C be computed without exhaustive search of the
   subtree? The argmax over CHILDREN*(D) is well-defined but potentially
   unbounded. A constructive formulation (building the calibrated node
   from A and M directly, rather than searching for it) would be
   preferable.

3. **Uniqueness of C:** The current definition provides ONE candidate
   calibration map. The Bootstrap Conjecture asserts that exactly one
   such map satisfies all four conditions (§5.1). Proving uniqueness
   requires showing that any two calibration maps satisfying the
   constraints must agree on all nodes.

4. **Non-triviality of T*:** We need to prove that T* ≠ ROOT for C as
   defined. If C always converges to ROOT (like the trivial parent map F),
   then the Bootstrap fails and the framework collapses.

5. **Sensitivity to the M-property convention:** The choice of the
   rightmost sub-expression as "measurement outcome" is a convention.
   Does the Bootstrap Constraint force a unique structural convention,
   or are multiple conventions possible (corresponding to different
   "measurement bases")?

---

## §8. Appendix: Comparison with Known Fixed-Point Constructions

### 8.1 Banach Fixed Point (Standard)

The standard Banach construction requires only contractiveness. C as
defined in §3.1 is conjectured to be contractive (§4.4). If proven,
Banach's theorem guarantees a unique fixed point T*. The Bootstrap
adds the extra condition C(T*) = T*, which is automatically satisfied
by any fixed point.

### 8.2 Kleene Fixed Point (Domain Theory)

In domain theory, fixed points are constructed via iteration from ⊥
(bottom). ROOT = ∅ plays the role of ⊥. The sequence Cⁿ(∅) monotonically
approaches T* if C is monotonic with respect to the information order.
Whether C is monotonic in this sense depends on the resolution of the
descendant search — a constructive C that builds T* incrementally would
be monotonic.

### 8.3 Ultrametric Contraction (This Work)

The distinctive feature of this construction is the **ultrametric**
structure. In an ultrametric space, the strong triangle inequality
DIST(A, C) ≤ max(DIST(A, B), DIST(B, C)) imposes additional constraints
on C beyond ordinary contractiveness. Specifically, C must map entire
subtrees (clusters at each distance scale) to subtrees at a STRICTLY
smaller scale — it cannot merely shift individual points.

This ultrametric constraint is what makes the Bootstrap Conjecture both
restrictive and powerful: it forces C to respect the hierarchical
structure of TREE at all scales simultaneously.

---

## References

- `29-schisms-formalization.md` — Domain-independent formalization (Layers 0–3)
- `29-schisms-synthesis-deepdive.md` — Domain-specific synthesis and Bootstrap Conjecture statement
- `_self_descriptive_system.py` — Executable implementation of TREE, DIST, and parent-map F
