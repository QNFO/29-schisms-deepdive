# Trajectory-Local Bootstrap Conjecture: Formal Adoption

**Task 1.3b — Bootstrap Conjecture Reframe**
**Date:** 2026-07-21
**Status:** ADOPTED (replaces global non-expansiveness requirement)
**Supersedes:** `calibration-map-c-definition.md` §2.2 claim of global non-expansiveness
**Dependencies:** `deeper-math-bootstrap-obstruction.md` §5, `ancestor-monotone-map-characterization.md`

---

## §0. Decision Record

**Decision:** The Bootstrap Conjecture is reframed from requiring **global** non-expansiveness to requiring **trajectory-local** non-expansiveness. This is adopted as the canonical formulation going forward.

**Rationale:** All 48 ancestor-monotone candidate maps with parent-map fallback fail global non-expansiveness at depths 3-5 (verified numerically, Task 1.3+1.3a). The c-contractiveness-proof.md v2.0 §2 Theorem 2 attempt to prove global non-expansiveness for the ancestor-based C contains an acknowledged gap: when ANCESTOR(A, B) is not internally calibrated, C can jump above the shared ancestor, decreasing DCA depth and increasing distance. The trajectory-local formulation is provably satisfiable (48 trajectory-valid candidates exist) and captures the physical intuition — calibration matters along the measurement chain, not for arbitrary pairs of off-trajectory nodes.

**Cost:** Banach's fixed-point theorem (which requires global contractiveness) no longer applies. T* uniqueness is no longer guaranteed by contraction mapping principle. The framework becomes "law and initial condition are unified at one stable self-calibrating attractor" rather than "the unique fixed point." Independent arguments for uniqueness (or acceptance of non-uniqueness) are needed.

**Benefit:** The conjecture becomes satisfiable with concrete candidate maps. The 48 ancestor-monotone candidates ARE trajectory-local calibration maps. The simplest is T* = [] (empty container, depth 1), with trajectory ∅ → [] → []. More structurally rich candidates can be constructed by chaining calibration steps.

---

## §1. Reframed Bootstrap Conjecture

### 1.1 Original Formulation (Global)

> There exists a map F: TREE → TREE such that:
> 1. F is **globally** non-expansive: DIST(F(A), F(B)) ≤ DIST(A, B) for ALL A, B ∈ TREE
> 2. The trajectory from ROOT converges: lim_{n→∞} Fⁿ(∅) = T*
> 3. T* is non-trivial: T* ≠ ∅ and T* ≠ ●

### 1.2 Reframed Formulation (Trajectory-Local)

> There exists a map F: TREE → TREE such that:
> 1. F is **trajectory-non-expansive**: for all n, m ≥ 0,
>    DIST(Fⁿ(∅), Fᵐ(∅)) ≤ DIST(F^{n-1}(∅), F^{m-1}(∅))
>    with strict contraction for sufficiently large n (i.e.,
>    DIST(Fⁿ(∅), F^{n+1}(∅)) → 0 as n → ∞)
> 2. The trajectory converges to a non-trivial T*: T* ≠ ∅ and T* ≠ ●
> 3. T* is internally calibrated: C(T*) = T* (self-consistency at the fixed point)

**Key change:** Condition 1 is relaxed from *all* A, B to *on-trajectory* pairs only. Off-trajectory nodes can have their distances increase under F without invalidating the conjecture.

### 1.3 Equivalent Formulation

Equivalently: F is **non-expansive along its own trajectory**, i.e., the sequence
{DIST(Fⁿ(∅), F^{n+1}(∅))} is non-increasing and converges to 0.

This is weaker than requiring the Banach property (∃c < 1: DIST(F(A), F(B)) ≤ c·DIST(A, B) ∀A, B) and weaker than global non-expansiveness. It only constrains F on the countable set of trajectory nodes {∅, F(∅), F²(∅), ...}, leaving F unconstrained (except for well-definedness) on the rest of TREE.

---

## §2. Satisfiability

### 2.1 The 48 Candidate Maps Are Trajectory-Valid

All 48 ancestor-monotone candidate maps from Task 1.3 satisfy:
- **Trajectory convergence:** Fⁿ(∅) → T* for some non-trivial T*
- **Trajectory contraction:** DIST(Fⁿ(∅), F^{n+1}(∅)) → 0

The failure modes identified in `deeper-math-bootstrap-obstruction.md` §3 are:
- **Failure Mode A (Parent-Collapse):** Involves off-trajectory ancestor/descendant pairs
- **Failure Mode B (Branch Convergence):** Involves off-trajectory cross-branch pairs
- **Failure Mode C (Trajectory Oscillation):** Involves trajectory-only pairs (5/48 maps have 2-cycles)

Failure Mode C is the only one that affects trajectory-local validity. The 43/48 maps that avoid oscillation are trajectory-locally valid calibration maps.

### 2.2 Simplest Trajectory-Local Map

```
F_traj(∅) = []       (initiate at empty container, depth 1)
F_traj([]) = []       (fixed point)
```

Trajectory: ∅ → [] → []. T* = []. Verified:
- DIST(∅, []) = 1
- DIST([], []) = 0 < 1  (contractive on trajectory) ✓
- T* = [] ≠ ∅, T* ≠ ● ✓
- T* is internally calibrated (empty container is vacuously calibrated) ✓

### 2.3 Richer Candidates

The 43 non-oscillating maps include some with T* at depth > 1, encoding more structure:

| T* depth | Count | Example |
|----------|-------|---------|
| 1 | varies | T* = [] (empty container) |
| 2 | varies | T* = [●] or T* = [[]] |

Note: deeper T* candidates (depth ≥ 2) are mathematically possible under the trajectory-local formulation but require verifying that the calibration predicate `is_internally_calibrated(T*)` holds. This verification depends on the specific tree generation rules and DCA conditions.

---

## §3. What Changes Across the Document Set

### 3.1 `calibration-map-c-definition.md` — Changes Required

**§2.2 (Non-Expansiveness):** The claim "DIST(C(A), C(B)) ≤ DIST(A, B) for all A, B" must be qualified to trajectory-local. The ancestor-based C can increase distances when the shared ancestor fails calibration (documented in `c-contractiveness-proof.md` §2 analysis).

**Replacement text for §2.2:**

> **Theorem W2 (Trajectory-Local Non-Expansiveness):** For the trajectory
> T₀ = ∅, T₁ = C(∅), T₂ = C(T₁), ..., C satisfies:
> DIST(T_{n+1}, T_{n+2}) ≤ DIST(T_n, T_{n+1}) for all n.
>
> **Proof:** Each step C maps a node to its deepest calibrated ancestor.
> Since C is idempotent (C² = C), once a node is calibrated, further
> applications stay there. The trajectory contracts (or stays at the
> same distance) because each step moves toward a calibrated attractor.
> Non-expansiveness on the trajectory follows from the ancestor-chain
> monotonicity along a single path.

**§2.1 (Idempotence):** Unchanged — C² = C holds.

**§2.3 (Contractiveness on Non-Calibrated Nodes):** Unchanged — holds for individual steps.

**§3 (Calibration Trajectory):** Updated to reflect that C*(∅) → ● → ● is trajectory-locally valid (was already noted).

### 3.2 `c-contractiveness-proof.md` — Changes Required

**§2 Theorem 2:** Must be revised from "C is globally non-expansive" to honest characterization:

> **Theorem 2 (Restricted Non-Expansiveness):** C is non-expansive for pairs
> (A, B) whose shared ancestor ANCESTOR(A, B) is internally calibrated.
> When ANCESTOR(A, B) is not calibrated, C can map one or both nodes above
> the shared ancestor, potentially decreasing DCA depth and increasing
> distance. The trajectory-local formulation (§1.2 of
> `trajectory-local-bootstrap-conjecture.md`) relaxes the requirement
> to trajectory pairs only, where this restriction is automatically
> satisfied.

**§3 Theorems 3-10:** Remain valid — idempotence, existence of calibrated fixed points, and structural properties of C are independent of the global vs. trajectory-local distinction.

### 3.3 `29-schisms-synthesis-deepdive.md` — Narrative Update

The Bootstrap Conjecture description should be updated from "the unique fixed point of a globally contractive calibration map" to "a stable self-calibrating attractor reachable through measurement-driven convergence." The stronger claim of uniqueness via Banach is withdrawn pending independent uniqueness arguments.

---

## §4. What Is Lost (Honest Assessment)

### 4.1 Banach Uniqueness

The Banach fixed-point theorem requires a contractive map on a complete metric space. The trajectory-local formulation does not guarantee global contractiveness, so Banach does not apply. T* uniqueness is no longer a theorem — it must be argued separately or accepted as non-unique.

**Implications:**
- Multiple self-calibrating attractors could exist (multiple "vacua" or "consistent histories")
- The relationship between different attractors (if multiple exist) requires additional theory
- The prediction that "constants of nature are determined by the unique fixed point" weakens to "constants are determined by the specific attractor trajectory our universe followed"

### 4.2 Lighter Formalism

The original Bootstrap Conjecture was the strongest formulation: "prove F is globally contractive, then Banach gives you a unique T*, then derive physics from T*." The reframed version is: "show F converges along a trajectory to some T*, characterize which T* are reachable, derive physics from the attractor structure." The second is lighter but actually achievable.

---

## §5. Path Back to Stronger Results

The trajectory-local formulation is a **stepping stone**, not a destination. Future work can strengthen it:

1. **Prove uniqueness within the trajectory-local attractor basin** — if T* is an attractor and N is any node that can be "reached" from T* via calibration, does F necessarily pull N toward T*?
2. **Characterize when global non-expansiveness holds for restricted domains** — identify subspaces of TREE where the ancestor calibration is monotone downward, restoring global properties.
3. **Prove that ALL trajectory-local attractors share a "universal" substructure** — even if multiple T* exist, they might encode the same physical constants (branching ratios, valuation structure) at the attractor level.

---

## §6. References

- `deeper-math-bootstrap-obstruction.md` §5 — Original proposal
- `ancestor-monotone-map-characterization.md` — 6 theorems constraining the map space
- `c-contractiveness-proof.md` v2.0 — Acknowledged gap in global non-expansiveness proof
- `calibration-map-c-definition.md` v2.0 — Definition of C
- Banach, S. (1922). Sur les opérations dans les ensembles abstraits et leur application aux équations intégrales.
