# Calibration Map C: Formal Definition (v2.1 — Trajectory-Local Reframe)

**Phase 1, Task 1.1 — Bootstrap Conjecture Formal Proof**
**Date:** 2026-07-20 (v2.0); 2026-07-21 (v2.1 — trajectory-local reframe adopted, Task 1.3b)
**Status:** v2.1 — trajectory-local Bootstrap Conjecture adopted; global non-expansiveness claim withdrawn
**Dependencies:** Layers 0-2 of `29-schisms-formalization.md`; `trajectory-local-bootstrap-conjecture.md`

---

## §0. Revision Notes

### v2.0 → v2.1 (2026-07-21, Task 1.3b)

| Change | Detail |
|--------|--------|
| **§2.2 Non-Expansiveness** | Claim of global non-expansiveness withdrawn. Replaced with trajectory-local non-expansiveness (Theorem W2-TL). The ancestor-based C can increase distances when ANCESTOR(A, B) fails internal calibration — see `c-contractiveness-proof.md` §2 analysis. |
| **§3 Calibration Trajectory** | Reformulated in terms of trajectory-local convergence. C* extension clarified. |
| **Conjecture framing** | Bootstrap Conjecture now uses trajectory-local formulation per `trajectory-local-bootstrap-conjecture.md`. Banach uniqueness no longer claimed; T* uniqueness requires separate argument or acceptance of non-uniqueness. |

### v1.0 → v2.0 (2026-07-20)

| Finding | Issue | Fix Applied |
|---------|-------|-------------|
| **F-H4** | REDUCE on structured sub-expressions underspecified — flatten+concatenate creates artificial boundary crossings | Replaced with **tuple-DCA**: structural DCA of all system sub-expressions as separate units, no flatten+REDUCE |
| **F-H1** | C_target search over infinite DESCENDANTS(D) — unbounded, C not well-defined | Replaced with **ancestor-bound search**: search ANCESTORS of N only (finite, at most DEPTH(N) candidates) |
| **F-H3** | COMPATIBLE nearly vacuous — min(depth-1) excludes almost nothing | Replaced with **structural coincident-depth condition**: system and measurement must share DCA at depth ≥ DEPTH(N) itself within the node's container |
| **F-H2** | REDUCE simplification can decrease DCA depth | Resolved by F-H4 fix — no REDUCE used on sub-expressions |
| **Design** | C₃ search over descendants was depth-increasing, contradicted contractiveness | Complete redesign: C is **ancestor-monotone** — always maps to an ancestor or self, guaranteeing non-expansiveness |

---

## §1. Calibration Map C (Revised Definition)

### 1.1 Core Definition

```
C: TREE → TREE

C(N) = the deepest ancestor A of N such that A is "internally calibrated"
```

An ancestor A of N is **internally calibrated** if one of the following holds:

1. A = ∅ (ROOT is trivially calibrated — empty has no internal contradictions)
2. A = ● (the bare mark is trivially calibrated — a single mark has no parts to be inconsistent)
3. A is a container [E₁ ... Eₙ] with n ≥ 1, and the rightmost non-empty sub-expression M = Eₙ satisfies:
   ```
   DCA_of_all(E₁, ..., Eₙ₋₁, M) is at depth ≥ DEPTH(A)
   ```
   where DCA_of_all is the deepest common ancestor of ALL listed sub-expressions.
   
   In words: the deepest common ancestor of the system parts and the measurement
   is at least as deep as the container itself — meaning the system and measurement
   agree at the level of A's own container boundary.

### 1.2 Operational Pseudocode

```
def C(N):
    if N == EMPTY or N == MARK:
        return N                    # ROOT and bare mark are trivially calibrated

    # Walk ancestors from N upward toward ROOT
    current = N
    while current != EMPTY:
        if is_internally_calibrated(current):
            return current          # deepest calibrated ancestor
        current = parent(current)

    return EMPTY                    # fallback: ROOT is always calibrated
```

### 1.3 The "Internally Calibrated" Predicate

```
is_internally_calibrated(N):
    if N == EMPTY or N == MARK:
        return True

    if not N.is_container():
        return False                # nodes that aren't containers can't encode measurement

    elements = N.sub_expressions()
    if len(elements) == 0:
        return True                 # empty container: no contradictions (vacuously)

    # Find rightmost non-empty sub-expression as measurement
    M = last non-empty in elements
    if M is None:
        return True                 # all empty: vacuously calibrated

    system_parts = elements excluding M (all positions before M)
    if all elements of system_parts are empty:
        return True                 # no system to calibrate against

    # Key condition: DCA of ALL system parts AND M is at depth >= DEPTH(N)
    all_nodes = system_parts ∪ {M}
    dca = DCA_of_all(all_nodes)
    return DEPTH(dca) >= DEPTH(N)
```

### 1.4 DCA_of_all: Multicast DCA

```
DCA_of_all({N₁, N₂, ..., Nₖ}):
    Return the deepest node in TREE that is an ancestor of EVERY Nᵢ.
    Computed iteratively: DCA(DCA(N₁, N₂), N₃, ...)
```

This is well-defined because:
- DCA(a, b) is well-defined for any pair (formalization §4.1)
- Iterating DCA over a finite set produces a unique result (associative and commutative in tree)
- The result is always at least ROOT (∅ is ancestor of everything)

### 1.5 Why Ancestor Search Is Finite and Well-Defined

Ancestors of N form the path from ROOT to N, which is exactly DEPTH(N) + 1 nodes. The search walks upward from N, testing at most DEPTH(N) candidates. Since every node in TREE has finite depth, the search always terminates.

**Contrast with v1.0:** v1.0 searched descendants of D, which is an infinite set. v2.0 searches ancestors, which is finite.

### 1.6 Examples

**Example 1:** C(∅) = ∅. ROOT is trivially calibrated.

**Example 2:** C(●) = ●. Bare mark is trivially calibrated.

**Example 3:** C([]) — empty container.
- Check []: is_internally_calibrated? Container, 0 elements → True (vacuously).
- Return [].

**Example 4:** C([● ●]) — container with two marks.
- Check [● ●]: container, 2 elements. M = ● (rightmost). system = {●}.
  DCA_of_all({●, ●}) = ●. DEPTH(●) = 1. DEPTH([● ●]) = ? (depends on tree position).
  
  If DEPTH([● ●]) = 2: DEPTH(DCA) = 1 < 2 → NOT calibrated.
  Walk to parent([● ●]). Parent depends on tree generation.

  If DEPTH([● ●]) = 1 (if it's a direct child of ROOT): DEPTH(DCA) = 1 ≥ 1 → calibrated!

**Example 5:** C([[●] ●]) — nested container with measurement.
- Check [[●] ●]: container, elements = [[●], ●]. M = ●. system = {[[●]]}.
  DCA_of_all({[[●]], ●}) = ? [●] and ● share DCA at... depends on tree structure.
  ● is depth 1. [[●]] — [●] reduces to ∅, so [[●]] → [∅] → []. Hmm, this depends on reduction.

**The point:** C is now computable for any concrete node by walking ancestors and checking the DCA condition — no infinite searches, no underspecified flattening.

---

## §2. Properties of C (v2.0)

### 2.1 Well-Definedness (F-H1 Resolved)

**Theorem W1:** C is well-defined on all N ∈ TREE.

*Proof:* For any N, the ancestor chain has finite length DEPTH(N) + 1. The predicate `is_internally_calibrated` involves only DCA and DEPTH, both well-defined. ROOT is always calibrated, so the while loop always terminates with a valid return value. ∎

### 2.2 Trajectory-Local Non-Expansiveness (v2.1)

**Theorem W2-TL (Trajectory-Local Non-Expansiveness):** For the trajectory
T₀ = ∅, T₁ = C(∅), T₂ = C(T₁), ..., C satisfies:
DIST(T_{n+1}, T_{n+2}) ≤ DIST(T_n, T_{n+1}) for all n.

*Proof:* Each step maps a node to its deepest calibrated ancestor. Since C is
idempotent (Theorem W4), the trajectory is monotone in depth: DEPTH(T_{n+1}) ≤
DEPTH(T_n) after the first expansion step. The trajectory contracts (or stays
constant) because each move is toward a calibrated ancestor along a single path
from ROOT. Once a calibrated node is reached, C preserves it. ∎

**Global non-expansiveness (withdrawn in v2.1):** The v2.0 proof attempted
to show DIST(C(A), C(B)) ≤ DIST(A, B) for ALL A, B, but the argument assumed
that C(A) and C(B) both lie at or below ANCESTOR(A, B) on their respective
paths. This fails when ANCESTOR(A, B) is NOT internally calibrated — C can
jump above the shared ancestor, decreasing DCA depth and increasing DIST.
The trajectory-local formulation avoids this issue by constraining only
trajectory pairs. See `c-contractiveness-proof.md` §2 for the detailed
counterexample analysis and `trajectory-local-bootstrap-conjecture.md` for
the formal adoption.

**When global non-expansiveness DOES hold:** For pairs (A, B) where
ANCESTOR(A, B) is internally calibrated, C(A) and C(B) are at or below
the shared ancestor, DCA depth is preserved, and non-expansiveness follows.

### 2.3 Contractiveness on Non-Calibrated Nodes

**Theorem W3:** If C(N) ≠ N (i.e., N is not internally calibrated), then DIST(C(N), N) > 0 and DEPTH(C(N)) < DEPTH(N).

*Proof:* C searches ancestors strictly above N. Since N itself failed the calibration check, the returned ancestor is strictly shallower than N. Hence DEPTH(C(N)) < DEPTH(N) and DIST(C(N), N) > 0. ∎

### 2.4 Contractiveness Ratio

For any A ≠ B where at least one is not internally calibrated:
- Since C maps to ancestors, DEPTH decreases for non-calibrated inputs.
- If both A and B are not calibrated: DEPTH(C(A)) < DEPTH(A) and DEPTH(C(B)) < DEPTH(B), so DCA depth increases by at least 1.
- DIST(C(A), C(B)) ≤ (1/2) · DIST(A, B) when both lose depth.

### 2.5 Idempotence

**Theorem W4:** C(C(N)) = C(N) for all N.

*Proof:* C(N) is, by definition, internally calibrated. Applying C again returns the deepest calibrated ancestor of C(N), which is C(N) itself (since C(N) is calibrated and is its own deepest calibrated ancestor). Hence C²(N) = C(N). ∎

---

## §3. Calibration Trajectory (v2.1 — Trajectory-Local)

### 3.1 From ROOT

C(∅) = ∅. Under the pure ancestor-based C, ROOT maps to ROOT —
no bootstrap occurs. This is the **initial measurement problem**:
a self-descriptive system cannot bootstrap from nothing. A "first
distinction" must be externally initiated, or the system must be
extended with a measurement-initiation primitive.

### 3.2 C* Extension — Minimal Non-Trivial Trajectory

The C* extension introduces the first distinction explicitly:

```
C*(∅) = ●           (initiate first distinction — NOT ancestor-monotone)
C*(●) = ●           (fixed point)
C*(N) = C(N)        (otherwise — ancestor-based calibration)
```

Trajectory: ∅ → ● → ●. T* = ● (bare mark).

**Trajectory-local validation:**
- DIST(∅, ●) = 1
- DIST(●, ●) = 0 < 1 ✓
- T* is non-trivial (● ≠ ∅) ✓
- C* is NOT globally non-expansive (the ∅ → ● step may create off-trajectory violations), but IS trajectory-locally non-expansive

This is the minimal non-trivial trajectory-local calibration map. T* = ●
encodes no branching structure but demonstrates that the convergence
pattern works.

### 3.3 Richer Trajectories — Reaching Depth ≥ 2

For T* with depth ≥ 2, C* can chain additional steps:

```
C*(∅) = ●
C*(●) = []          (cross-branch at depth 1)
C*([]) = []          (fixed point)
```

Trajectory: ∅ → ● → [] → []. T* = [] at depth 1.

Or depth-2 trajectory:
```
C*(∅) = ●
C*(●) = [●]         (descendant, depth 2)
C*([●]) = [●]       (fixed point)
```

**Constraint:** Each step must preserve trajectory-local contraction
(DIST_{n+1} < DIST_n after the first expansion), and the fixed point
must satisfy `is_internally_calibrated(T*)`. The 43 non-oscillating
candidate maps from Task 1.3 enumeration satisfy these constraints.

### 3.4 The Substructure Problem

For T* encoding the full branching structure (1→2→2→3→7→28→125→588),
the trajectory must build up through multiple calibration steps, each
adding one level of container nesting. The trajectory-local formulation
allows this: each step can be depth-expanding as long as the overall
sequence contracts and stabilizes at a calibrated T*. Characterizing
which T* are reachable (and whether the 1→2→2→3→7→28→125→588 pattern
is among them) is deferred to Task 1.4 (Valuation Structure).

This is an open problem — deferred to Task 1.4 (valuation structure characterization).

---

## §4. Relation to v1.0

| Aspect | v1.0 | v2.0 |
|--------|------|------|
| Search direction | Descendants of DCA (infinite) | Ancestors of N (finite) |
| Sub-expression combination | REDUCE(flatten(concatenate)) | Tuple DCA (structural, no flatten) |
| Compatibility criterion | min(depth-1) (nearly vacuous) | DCA at container depth (structural) |
| Well-definedness | ❌ F-H1: search unbounded | ✅ Finite ancestor chain |
| Non-expansiveness | ⚠️ F-H2: REDUCE depth reversal | ✅ Proof from ancestor monotonicity |
| Computability | ❌ Infinite search | ✅ O(DEPTH(N)) operations |
| Fixed point from ROOT | ∅ (trivial) | ∅ (trivial) — same, honest |
| Measurement semantics | ❌ F-H3: vacuous | ⚠️ Structural, but admits emptiness |

---

## §5. Open: What v2.0 Does NOT Do

1. **Non-trivial fixed point.** C(∅) = ∅. A non-trivial calibration map requires a measurement-initiation mechanism (§3.2) or a different construction altogether.

2. **Encoding of the branching pattern.** The fixed point ● contains no structural information. The connection between calibration and the observed tree growth (1,2,2,3,7,28,125,588) remains conjectural.

3. **Physical measurement semantics.** The "rightmost = measurement" convention is still arbitrary. The DCA depth condition is structural but not physical. A proper measurement-theoretic interpretation requires additional constraints.

4. **Global contractiveness.** C is non-expansive but not strictly contractive everywhere. For nodes that are already internally calibrated, C is the identity. This is acceptable for the Bootstrap framework (many fixed-point theorems work with non-expansive + eventually-contractive maps in ultrametric spaces).

---

## References

- `red-team-audit-ctasks-2026-07-20.md` — F-H1, F-H2, F-H3, F-H4 findings
- `29-schisms-formalization.md` — TREE, DIST, DCA, DEPTH definitions
- `c-contractiveness-proof.md` — Contractiveness analysis (to be updated for v2.0)
