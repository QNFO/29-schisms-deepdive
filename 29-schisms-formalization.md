# Domain-Independent Formalization: Self-Descriptive Systems

---

## §0. What This Is

A formal specification of the minimal abstract system that can describe itself
without introducing an external vantage point.

Every term is defined operationally. No domain-specific concepts are assumed.
"Self" means: the descriptor and the described are the same system.

---

## §1. Primitives

### 1.1 Mark

```
MARK ::= ●
```

An indivisible atomic unit. Carries no properties beyond existence.

### 1.2 Container

```
CONTAINER ::= [ ... ]
```

A boundary enclosing zero or more MARKS or nested CONTAINERS.

### 1.3 Expression

An EXPRESSION is either:

```
EXPRESSION ::= ∅          -- empty
             | ●           -- mark
             | [E1 E2 ...] -- container of expressions
```

Where ∅ denotes the absence of any mark or container.

### 1.4 Flat Form

Any expression can be flattened to a string of the alphabet {●, [, ]} by
removing all whitespace and applying no interpretation.

Example: `[●[●●]]` → `[●[●●]]` (already flat)

---

## §2. Reduction Rules

Two rules. Applied exhaustively to any expression until no rule matches.

### 2.1 Condensation (C)

```
● ● → ●
```

Multiple adjacent marks reduce to one.

Rationale: "This side" and "this side" are the same side. Drawing the same
distinction twice is indistinguishable from drawing it once.

### 2.2 Cancellation (X)

```
[●] → ∅
```

A container holding only a single mark reduces to empty.

Rationale: Crossing the boundary from "this side" to "that side" and back
is equivalent to not crossing. The mark inside represents the act of
crossing; the container represents the boundary crossed.

### 2.3 Double-Enclosure (D)

```
[[E]] → E
```

A container nested inside another, with nothing else, reduces to its inner
expression.

Derived from X: the outer boundary is crossed twice (entering and exiting
the inner), returning to the original side.

### 2.4 Reduction Algorithm

```
REDUCE(E):
    while any rule matches:
        apply first matching rule (C > X > D, left-to-right)
    return E
```

### 2.5 Normal Form

A normal form is any expression for which REDUCE(E) = E.

---

## §3. The Configuration Space

### 3.1 Generation Rule

From any normal form N, the next generation G(N) is the set of all
normal forms reachable by applying exactly one of:

- ADD-MARK:    insert ● adjacent to any existing ●
- ADD-CONTAINER: wrap any sub-expression in [ ... ]

Then reduce: `G(N) = {REDUCE(N') | N' = one step from N}`

### 3.2 Root

```
ROOT ::= ∅
```

The empty expression. Contains no marks, no containers.

### 3.3 The Tree

```
TREE ::= the infinite directed graph where:
    - nodes are all normal forms
    - edges are N → M for each M in G(N)
    - root is ∅
```

**Property 1:** Every node has exactly one parent.
Proof: For any non-root node, there is a unique shortest sequence of inverse
operations (remove-mark or unwrap-container) that reaches ∅. By reduction
uniqueness, this path is unique.

**Property 2:** The tree is infinite in depth.
Proof: ∅ → [●] → [[●]] → [[[●]]] → ... is an infinite chain. None of these
are reducible. Therefore depth is unbounded.

**Property 3:** Every node has finitely many children.
Proof: A normal form has finite length. There are finitely many positions to
insert a mark, and finitely many sub-expressions to wrap. After reduction,
the number of distinct normal forms is bounded.

### 3.4 Depth

```
DEPTH(N) ::= number of edges on the unique path from ROOT to N
```

---

## §4. Distance

### 4.1 Common Ancestor Depth

```
ANCESTOR(A, B) ::= the node of maximum depth that lies on both
                   the path from ROOT to A and from ROOT to B
```

### 4.2 Distance Function

```
DIST(A, B) ::= 2 ^ (-DEPTH(ANCESTOR(A, B)))
```

Special case: DIST(A, A) = 0 (convention — no ancestor above the node itself,
or equivalently: distance to self is zero).

### 4.3 The Strong Condition

```
DIST(A, C) ≤ MAX(DIST(A, B), DIST(B, C))
```

Proof: Let d_AB = ANCESTOR(A, B) depth, similarly d_BC, d_AC.
The ancestor of A and C must be at least as deep as the shallower of
ANCESTOR(A, B) and ANCESTOR(B, C). Therefore:
d_AC ≥ min(d_AB, d_BC)
⇒ 2^(-d_AC) ≤ 2^(-min(d_AB, d_BC)) = max(2^(-d_AB), 2^(-d_BC))
⇒ DIST(A, C) ≤ max(DIST(A, B), DIST(B, C))

### 4.4 Completeness

The metric space (TREE, DIST) is complete: every Cauchy sequence converges
to a node in the tree.

Proof sketch: In this metric, a Cauchy sequence means that for any ε > 0,
there exists N such that for all m,n > N, DIST(x_m, x_n) < ε. This means
all nodes beyond N share an ancestor at depth > -log₂(ε). These nodes
form a subtree. The limit is the infinite path through this subtree.

---

## §5. Maps on the Tree

### 5.1 Contractive Map

```
A map F: TREE → TREE is CONTRACTIVE if:
    DIST(F(A), F(B)) < DIST(A, B)  for all A ≠ B
```

### 5.2 Fixed Point

A node T* is a FIXED POINT of F if F(T*) = T*.

### 5.3 Fixed Point Theorem

If F is contractive on a complete metric space, then F has exactly one
fixed point.

Proof: Standard (Banach). Starting from any node X₀, iterate Xₙ₊₁ = F(Xₙ).
Since F is contractive, the sequence is Cauchy. Since the space is complete,
it converges. The limit is the unique fixed point.

---

## §6. Self-Descriptive Systems

### 6.1 Definition

A system is SELF-DESCRIPTIVE if:

```
1. Its state is a node in TREE
2. Its "laws" are a contractive map F on TREE
3. Its "initial condition" is ROOT
4. Its trajectory is F⁰(ROOT), F¹(ROOT), F²(ROOT), ...
```

### 6.2 The Convergence Property

```
For any self-descriptive system:
    lim n→∞ Fⁿ(ROOT) = T*   (exists and is unique)
```

Proof: F is contractive, TREE is complete → Banach applies.

### 6.3 The Collapse of Categories

In a self-descriptive system:

| Category | What It Is |
|----------|-----------|
| State space | TREE |
| Initial condition | ROOT = ∅ |
| Laws | F (the contractive map) |
| Trajectory | Fⁿ(ROOT) |
| Fixed point | T* |

But note: T* is reachable FROM ROOT BY F. So T* IS the trajectory's limit,
which IS determined by both F (the "law") and ROOT (the "initial condition").

If the system ITSELF must specify both F and ROOT, then F must be such that
ROOT → T* is the ONLY consistent trajectory. In other words: F is not
arbitrary — it must be the map that makes the entire tree structure
self-consistent.

### 6.4 The Self-Consistency Condition

```
A contractive map F is SELF-CONSISTENT if:
    F is derivable from the structure of TREE itself
    (i.e., F encodes no information beyond what is already in TREE)
```

Formally: F ∈ Aut(TREE), the automorphism group of the tree with its
distance structure.

This constrains F heavily. Not every contractive map is permitted — only
those that preserve the tree's structural properties (branching, depth,
distance).

---

## §7. Projection (Coarse-Graining)

### 7.1 Projection Map

```
PROJECT: TREE → R   (where R is a representation space)

Defined as: PROJECT(N) = aggregate of all nodes within DIST ≤ ε of N,
            for some fixed ε > 0.
```

### 7.2 Properties

1. **Non-injective:** PROJECT(A) = PROJECT(B) does not imply A = B.
   Multiple distinct tree nodes map to the same representation.

2. **Continuity:** If DIST(A, B) is small, PROJECT(A) and PROJECT(B) are
   "close" in R (for a suitable notion of closeness in R).

3. **Irreversibility:** Given PROJECT(N), there is no algorithm to recover N
   uniquely. Information is lost.

4. **Emergent smoothness:** Under suitable choice of ε, the image of PROJECT
   on a subtree appears continuous/smooth, even though TREE is discrete.

### 7.3 The Representation Space R

R is NOT part of the primitive system. It is introduced BY the projection.
Anything observed in R is a PROJECT-image of a tree node. The "laws" of R
are shadows of F under PROJECT.

---

## §8. Mapping the 29 Schisms (Domain-Independent)

Each schism is now a structural tension in the modeling of a system that
describes itself. Resolution means: the tension dissolves when the system
is specified as a self-descriptive tree under a contractive self-consistent
map.

### 8.1 Layer 1 Schisms (Structural Assumptions)

| # | Schism (abstracted) | Resolution |
|---|---------------------|-----------|
| 1 | Continuous vs. Discrete substrate | TREE is discrete. Continuity emerges from PROJECT (§7). No assumption needed. |
| 14 | Which representation space? (§7's R) | R is a choice of projection. Multiple R's are possible from the same TREE. No single "correct" R. |
| 18 | Which logic for reasoning about the system? | The logic is the algebra of marks and containers (§2). Excluded middle = "a distinction has been drawn." Where no distinction has been drawn, there is no excluded middle. |
| 9 | Discovered vs. invented? | The act of marking (§1.1) creates the mark. The tree is generated by rules (§3) not discovered. The formalism IS the ontology. |
| 28 | Is the specification consistent? | Each node is finite (§3, Property 3). Incompleteness = no finite node can see the entire infinite tree (§3, Property 2). This is a structural fact, not a failure. |

### 8.2 Layer 2 Schisms (State/Law Ontology)

| # | Schism (abstracted) | Resolution |
|---|---------------------|-----------|
| 2 | State vs. Process | TREE is static. "Process" = traversal of edges (§3.3). No separate "process" category. |
| 7 | Deterministic vs. non-deterministic | F is deterministic (a function). But PROJECT(F) may appear probabilistic because projection loses information (§7.2, Property 3). |
| 12 | Fundamental level vs. emergence | TREE has no bottom (§3, Property 2). All levels exist. "Fundamental" = a choice of which depth to call "base." |
| 13 | Fixed parameters vs. evolving ones | Parameters are ratios stabilized at T* (§6.2). They "evolve" during approach to T* and stabilize after. |
| 16 | Are there "laws" at all? | F is the law. But F is not externally specified — it is constrained by self-consistency (§6.4). |
| 19 | Law separate from initial condition? | ROOT and F jointly determine T*. In a self-descriptive system, ROOT and F are not independently specifiable. T* IS both "law" and "initial condition" — it is the unique self-consistent fixed point. |
| 21 | Objective state? | Every node's "state" is its position in TREE. There is no absolute reference. State is always relative to which node you are at. |
| 26 | Single outcome vs. all outcomes? | TREE contains all nodes. A "single outcome" = the path from ROOT to T* (the fixed-point trajectory). All branches exist, but F selects one. |

### 8.3 Layer 3 Schisms (Level Boundaries)

| # | Schism (abstracted) | Resolution |
|---|---------------------|-----------|
| 5 | Where does one level stop and another begin? | Levels are depths in TREE. The boundary is a choice of ε in PROJECT (§7.1). Different ε → different boundary. |
| 4 | Directionality (why forward, not backward)? | TREE edges are directed from ROOT outward (§3.3). Depth increases monotonically along any path. Direction = increasing depth. |
| 6 | Can distant nodes affect each other? | DIST is non-Archimedean (§4.3). Two nodes in different branches are "far" regardless of their individual depths. No intermediate distances. Correlation at a distance is geometrically natural, not magical. |
| 20 | Does F preserve structure? | F is contractive (§5.1). Structure is preserved in the sense that DIST(F(A),F(B)) < DIST(A,B). The relative ordering of distances is maintained. |
| 22 | Is F reversible? | F is contractive → strictly reduces distances → not injective → not invertible. Direction is inherent. |
| 17 | Why does one path feel unique? | The trajectory Fⁿ(ROOT) is a single path. Other paths EXIST in TREE but are not ON the trajectory. "Uniqueness" = position on the trajectory. |

### 8.4 Layer 4 Schisms (Global Structure)

| # | Schism (abstracted) | Resolution |
|---|---------------------|-----------|
| 3 | Fixed background vs. generated foreground | TREE is generated by rules from ROOT (§3). There is no pre-existing space. The tree IS the space. |
| 11 | Time as parameter vs. time as structure | "Time" = depth in TREE (§3.4). No external clock. Depth IS the ordering parameter. |
| 8 | Single root vs. multiple roots | TREE has exactly one root (§3.2). But at any depth > 0, there are multiple branches. "Different roots" = different choices of which branch to consider the local root. |
| 23 | Fixed number of dimensions | "Dimension" = branching factor of TREE at a given depth. This can vary with depth (§3, Property 2 and 3). Not fixed. |
| 24 | Root as trivial vs. root as non-trivial | ROOT = ∅ (§3.2). But ∅ contains the potential for all expressions. "Empty" ≠ "nothing." |
| 15 | One description vs. many | PROJECT is a many-to-one map (§7.2, Property 1). Many different tree configurations project to the same R-image. Multiple valid descriptions of the same underlying structure. |

### 8.5 Layer 5 Schisms (The Describer)

| # | Schism (abstracted) | Resolution |
|---|---------------------|-----------|
| 10 | Describer outside vs. inside the system | The describer IS a node in TREE. Every observation is a DIST comparison between the describer's node and another node. |
| 25 | Omniscient perspective | No node can see the entire TREE (§3, Property 2: infinite depth, and Property 3: finite children). Omniscience = limit concept, unreachable by any finite node. |
| 27 | Description vs. described | PROJECT is a function defined on TREE nodes (§7.1). The "description" IS a node-to-projection mapping. The "territory" = TREE. The "map" = PROJECT. Both are within the same formal system. |
| 29 | What counts as an explanation? | An explanation = the path from ROOT to the node in question (§3.3). A cause = an ancestor node. |

---

## §9. Bias Minimization

### 9.1 Definition of Bias

```
BIAS ::= an unnecessary restriction on the structure of a model
         that is not forced by the system being modeled
```

### 9.2 Bias Sources and Elimination

| Bias | Source | Eliminated? | How |
|------|--------|-------------|-----|
| **Smoothness** | Assuming continuity where only discrete marks exist | Yes | TREE is discrete (§1–3). Smoothness = PROJECT artifact (§7). |
| **Fixed representation** | Assuming one R (§7) | Yes | PROJECT is not unique. Many R's possible. |
| **External clock** | Assuming time as separate parameter | Yes | Depth IS ordering (§3.4, §8.4–11). |
| **External describer** | Assuming observer outside system | Yes | Observer = node in TREE (§8.5–10). |
| **Single description** | Assuming one "correct" R-level theory | Yes | Many nodes → same PROJECT-image (§7.2). |
| **Pre-existing laws** | Assuming F before state | Yes | F constrained by self-consistency (§6.4). |
| **Additivity** | Assuming DIST(A,C) = DIST(A,B) + DIST(B,C) | Yes | DIST is non-Archimedean (§4.3). |
| **Symmetry (reversibility)** | Assuming F invertible | Yes | F contractive → not invertible (§8.3–22). |

### 9.3 Remaining Bias

The structure of TREE itself (branching factor, container nesting rules) IS
a bias. It is the MINIMAL bias: to describe anything, you must have at least
a mark and a boundary. Every formalism has this bias. The question is whether
additional biases are introduced. This formalism introduces none.

---

## §10. Information Theoretic Analysis

### 10.1 Information

```
INFO(N) ::= DEPTH(N) × log₂(BRANCHING(N))
```

The information content of a node scales with its depth and the branching
factor at each ancestor.

### 10.2 Loss Sites

| Site | Standard Approach | This Formalism | Eliminated? |
|------|------------------|---------------|-------------|
| **Level boundary** | Cut between levels introduces indeterminacy | Boundary = choice of ε in PROJECT | Yes |
| **State/law separation** | Two categories → interface friction | One structure (TREE + F) | Yes |
| **Map/territory gap** | Description ≠ described | PROJECT is a function on nodes | Yes |
| **Observer/system split** | Observer unmodeled | Observer = node | Yes |
| **Decoherence** | Information leaks | Contractive map preserves ordering | Reduced |
| **Irreversibility of projection** | PROJECT loses information | By design (§7.2, Property 3) | Inherent |

### 10.3 Gain

- **Encoding efficiency:** INFO scales with depth (§10.1), not with number
  of "dimensions" (which is a projection artifact).
- **Structure preservation:** F preserves DIST ordering even as it contracts
  (§5.1), so relative information is maintained.
- **Scale-free:** Properties are ratios of distances between nodes, not
  absolute values. No unit system needed.

---

## §11. Open Formal Problems

1. **Prove:** For a self-consistent contractive F (§6.4), the fixed point T*
   is computable from ROOT alone in finite steps. (Currently: only existence
   is proven, not computability.)

2. **Characterize:** Which branching structures admit a self-consistent F?
   Not all trees have a non-trivial automorphism group.

3. **Construct:** An explicit F that generates the observed branching pattern
   from ROOT, without hand-tuning.

4. **Bound:** The PROJECTion error — how much information is lost as a
   function of ε (§7.1).

---

## §12. Executable Specification (Pseudocode)

```
class Tree:
    ROOT = Expression.empty()

    def generate(node: Expression) -> list[Expression]:
        """All normal forms reachable in one step."""
        ...

    def reduce(expr: Expression) -> Expression:
        """Apply C, X, D exhaustively."""
        ...

    def dist(a: Expression, b: Expression) -> float:
        """2^(-depth(deepest_common_ancestor(a, b)))"""
        ...

    def fixed_point(F: Callable, start: Expression = ROOT, tol: float = 1e-15) -> Expression:
        """Iterate F until distance between consecutive iterates < tol."""
        ...

    def project(node: Expression, epsilon: float) -> Expression:
        """Return the set of all nodes within DIST ≤ epsilon of node."""
        ...

class Expression:
    def __init__(self, elements: list):
        """elements: list of Mark or Container"""
        ...

    def depth(self) -> int:
        """Number of edges from ROOT."""
        ...

    def ancestor_with(self, other: Expression) -> Expression:
        """Deepest common ancestor."""
        ...
```

---

## Appendix A: Why This Is Minimal

Any formal system that can describe itself must minimally contain:

1. **A way to say "something exists."** → MARK (§1.1)
2. **A way to say "this is separate from that."** → CONTAINER (§1.2)
3. **A way to say "this and this are the same."** → CONDENSATION (§2.1)
4. **A way to say "going there and back = staying here."** → CANCELLATION (§2.2)

These four primitives are necessary and sufficient to construct any
distinction-based structure. Adding anything else introduces unnecessary
bias. Removing any of them makes the system incapable of describing itself.

The system is complete in the sense that any self-consistent description
of a system BY that system can be encoded as a path in TREE under some
contractive F.

---

## Appendix B: The 29-Schism Mapping (Compact Reference)

| S# | Schism (abstract) | § Resolves | Mechanism |
|----|-------------------|------------|-----------|
| 1 | Continuous/discrete | §3, §7 | Discrete tree + PROJECT |
| 2 | State/process | §3.3, §8.2 | Static tree = dynamics |
| 3 | Background/foreground | §3, §8.4 | Tree generated from ROOT |
| 4 | Direction | §3.4, §8.3 | Depth increases monotonically |
| 5 | Level boundary | §7, §8.3 | ε-choice in PROJECT |
| 6 | Non-local correlation | §4.3, §8.3 | Non-Archimedean DIST |
| 7 | Deterministic/probabilistic | §5, §8.2 | F deterministic; PROJECT(F) appears probabilistic |
| 8 | Single/multiple roots | §3.2, §8.4 | One ROOT, many branches |
| 9 | Discovered/invented | §1, §8.1 | Mark = enacted |
| 10 | Outside/inside describer | §8.5 | Observer = node |
| 11 | Time as parameter | §3.4, §8.4 | Depth = ordering |
| 12 | Fundamental/emergent | §3, §8.2 | No bottom |
| 13 | Fixed/evolving parameters | §6.2, §8.2 | Stabilize at T* |
| 14 | Which representation? | §7, §8.1 | Multiple R's |
| 15 | One/many descriptions | §7.2, §8.4 | Many→one PROJECT |
| 16 | Laws exist? | §6.4, §8.2 | F from self-consistency |
| 17 | Unique path | §6.1, §8.3 | Fⁿ(ROOT) = one path |
| 18 | Which logic? | §2, §8.1 | Algebra of marks |
| **19** | **Law separate from initial?** | **§6.2, §6.3** | **T* = both** |
| 20 | F structure-preserving? | §5.1, §8.3 | Contractive = preserves ordering |
| 21 | Objective state? | §8.2 | State = position in TREE |
| 22 | Reversible? | §5.1, §8.3 | Contractive ⇒ not invertible |
| 23 | Fixed dimensionality? | §3, §8.4 | Branching varies with depth |
| 24 | Root trivial? | §3.2, §8.4 | ∅ contains all potential |
| 25 | Omniscience? | §3, §8.5 | Finite node ≠ infinite tree |
| 26 | One/all outcomes? | §8.2 | TREE = all; Fⁿ(ROOT) = one |
| 27 | Map/territory? | §7, §8.5 | PROJECT = function on nodes |
| 28 | Consistency? | §3, §8.1 | Local finiteness = structural bound |
| 29 | Explanation? | §3.3, §8.5 | Path from ROOT |
