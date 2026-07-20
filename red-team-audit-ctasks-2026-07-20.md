# Red-Team Audit: Calibration Map C (Tasks 1.1 & 1.2)

**Audit Date:** 2026-07-20
**Auditor:** QNFO Agent (autonomous red team per §RED-TEAM → DoD → ITERATE → REFINE cycle)
**Target Documents:**
- `calibration-map-c-definition.md` (Task 1.1, 2026-07-20)
- `c-contractiveness-proof.md` (Task 1.2, 2026-07-20)
**Methodology:** Negative verification — attempt to prove each claim FALSE. Test edge cases. Challenge every assumption.

---

## §0. Audit Scope

This audit evaluates the mathematical correctness, edge-case coverage, and
logical coherence of two linked deliverables:

| Document | Claims Evaluated |
|----------|-----------------|
| C- Definition | Well-definedness (§4.1), idempotence (§4.2), DEPTH relationship (§4.3), contractiveness conjecture (§4.4) |
| C- Proof | Theorem 1 (failure of global C), Theorem 2 (C on D_M), Theorem 3 (C* globally), Theorem 4 (non-expansive), Theorem 5 (C² on D_M) |

---

## FINDINGS

---

### CRITICAL

---

#### F-C1: Lemma 2 "Same Measurement" Argument Is False

**Severity:** CRITICAL
**Location:** `c-contractiveness-proof.md` §4, Lemma 2, Case (i)

**The claim:**
> If M_A = M_B, then D_A and D_B both involve the same measurement
> sub-expression. The DCA of D_A and D_B must be at least as deep as
> DCA(M_A, M_B) = DCA(M_A, M_A) which is M_A itself.

**Why it's false:**

D_A = DCA(REDUCE(S_A), M_A). D_B = DCA(REDUCE(S_B), M_B). Even if M_A = M_B, the
DCAs D_A and D_B are determined by the PAIR (system, measurement), not just the
measurement alone. The system parts S_A and S_B can be in entirely different
branches of the tree. The DCA of D_A and D_B could be as shallow as ROOT if
S_A and S_B diverge radically.

Consider this counterexample in the tree:
- A = [[● ●] ●] — system = [● ●], measurement = ●
- B = [∅ ●] — system = ∅, measurement = ●

Wait — B = [∅ ●] gives A_combined = REDUCE(∅) = ∅, so B ∉ D_M (the A=∅
branch returns identity). Let me construct a valid counterexample:

- A = [[●] ●] — system reduces to ∅, M_A = ● → A ∉ D_M
- B = [[●●] ●] — system = [●●], reduces to [●], M_B = ● → B ∈ D_M

So A and B can't BOTH be in D_M with the same measurement if one has empty
system. But they CAN both be in D_M with M_A = M_B if both systems are non-empty:

- A = [[●] ●] — system reduces to ∅ after [●]→∅... no, [●] is not a system
  part, it's the container. Let me be more careful.

Actually, the fundamental problem is simpler: **M_A is a sub-expression of A.**
If A and B share ANCESTOR(A, B) = X at depth d, then M_A is below X (it's a
sub-expression of A). But M_B is below X too (sub-expression of B). However,
the DCA of M_A and M_B is NOT necessarily M_A itself — it's the deepest node
on BOTH paths from ROOT to M_A and from ROOT to M_B. If M_A and M_B are in
different sub-branches below A and B respectively, their DCA could be
shallower than DEPTH(M_A).

More concretely: suppose A and B both have depth 3 and share ANCESTOR at
depth 2. M_A is a child of A at depth 4. M_B is a child of B also at depth 4.
If A and B are different children of the depth-2 ancestor, then M_A and M_B
are in different sub-branches. Their DCA could be the depth-2 ancestor, not
M_A itself. The claim "DCA(M_A, M_A) = M_A" is TRUE (DCA of a node with itself
is the node), but the relevant quantity is DCA(D_A, D_B), not DCA(M_A, M_A).

**The argument conflates:**
- DCA(M_A, M_A) = M_A (trivially true)
- DCA(D_A, D_B) where D_A = DCA(S_A, M_A) and D_B = DCA(S_B, M_A)

These are different quantities. D_A and D_B both involve M_A, but they also
involve S_A and S_B respectively, which can pull the DCA(D_A, D_B) shallower.

**Verdict:** The Case (i) argument for Lemma 2 is unsound. The claim that
same-measurement nodes are necessarily brought closer by calibration is not
supported by the argument given.

---

#### F-C2: Lemma 2 "Different Measurements" Argument Is Circular

**Severity:** CRITICAL
**Location:** `c-contractiveness-proof.md` §4, Lemma 2, Case (ii)

**The claim:**
> The self-consistency constraint forces both calibrated nodes toward a
> common structural core.

**Why it's circular:**

The COMPATIBLE condition (§2.3 of the C-definition) states:
```
COMPATIBLE(A, M) ⇔ DEPTH(DCA(A, M)) ≥ min(DEPTH(A), DEPTH(M)) - 1
```

This constrains the INTERNAL structure of a single node — it says nothing
about the relationship BETWEEN two different calibrated nodes C₃(A) and
C₃(B). The proof asserts without justification that internal compatibility
within each node implies external convergence between nodes.

To make this concrete: suppose C₃(A) = X where X_system and X_measurement
are compatible. Suppose C₃(B) = Y where Y_system and Y_measurement are
compatible. The proof claims WITHOUT DEMONSTRATION that X and Y are
"pulled toward a common structural core." There is no mechanism described
for this cross-node convergence.

**Verdict:** The Case (ii) argument for Lemma 2 is essentially an assertion
masquerading as a proof. It uses the word "therefore" with no logical
connection between the premise (internal compatibility) and the conclusion
(cross-node convergence).

---

#### F-C3: Lemma 3 Assumes the Bootstrap Conjecture to Prove the Bootstrap Conjecture

**Severity:** CRITICAL
**Location:** `c-contractiveness-proof.md` §4, Lemma 3

**The claim:**
> Under the self-consistency condition (Bootstrap Constraint), all nodes
> in D_M eventually converge to the same ROOT branch — the unique branch
> containing T*.

**Why it's circular:**

The Bootstrap Conjecture asserts that there exists a unique T* reachable
from ROOT under C. Lemma 3 uses "the unique branch containing T*" as a
premise to prove that C converges — but the existence and uniqueness of T*
is exactly what the Bootstrap Conjecture aims to establish. This is
circular reasoning.

Furthermore, T* has not been defined, characterized, or shown to exist at
this point in the proof. Lemma 3 references "T*" as if it were already
established, but Task 1.2 (contractiveness) precedes Task 1.3 (fixed-point
uniqueness) in the WBS. T* is not available as a premise.

**Verdict:** Lemma 3 is logically invalid — it assumes the conclusion.

---

#### F-C4: C* Refinement Is Abandoned Mid-Proof, Then Claimed as Proved

**Severity:** CRITICAL
**Location:** `c-contractiveness-proof.md` §5.4–§5.5

**The proof trajectory in the document:**

1. §5.3: C* is defined with 4 cases (∅→●, parent fallback, C₃, parent for
   identity)

2. §5.4: Case analysis begins. Case 4 (A=∅, B uses parent) is analyzed and
   found to FAIL: "DIST(C*(∅), C*(B)) = 1 = DIST(∅, B). This fails!"
   The document identifies a 2-cycle: ∅ → ● → ∅.

3. §5.4 continues: "Revised C* to eliminate the 2-cycle." Option A
   (C*(●) = ●) is adopted. A new 4-case definition is given.

4. §5.5: Re-verification of the revised C*. Case A=∅, B∈D_M is analyzed
   and AGAIN found to fail: "This still fails."

5. The document then says: **"Hmm. This is getting complicated. Let me take
   yet another approach."** — §6 pivots to Definition B.

6. **Yet §0's Executive Summary claims:** "Proposes C* — a refinement...
   and proves C* is contractive on all of TREE (Theorem 3)."

**Verdict:** This is a document-level integrity violation. The executive
summary claims a proof was completed. The body of the document shows the
proof was attempted, failed, and abandoned. A reader who reads only the
summary would be misled into believing C* is a proven result when the
author's own analysis shows it fails for at least two identified cases.

---

#### F-C5: Theorem 5 ("C² Is Contractive on D_M") Unsupported by Argument

**Severity:** CRITICAL
**Location:** `c-contractiveness-proof.md` §6.2

**The claim:**
```
DIST(C²(A), C²(B)) < DIST(C(A), C(B)) ≤ DIST(A, B)
```

**The "proof":**
> "Proof sketch. The first application of C maps each node to its calibrated
> version (or keeps it if already calibrated). The second application either
> (a) finds that the calibrated node is already at a fixed point (identity)
> or (b) applies the parent map (reduction). In either case, depth decreases
> or self-consistency deepens, and the DCA between any two nodes strictly
> deepens after at most 2 iterations."

**Why it's insufficient:**

This is a proof sketch, not a proof. It does not:

1. Define what "self-consistency deepens" means quantitatively.
2. Show that the identity case (a) doesn't just preserve distance
   (violating strict contractiveness).
3. Handle the case where C(A) = A (fixed point) and C(B) = B (fixed point)
   but A ≠ B — then C²(A) = A and C²(B) = B, so DIST(C²(A), C²(B)) =
   DIST(A, B), violating the claim.
4. Address the mixed case where C(A) is identity (already calibrated) but
   C(B) uses parent (reduction) — this CAN increase distance in the
   ultrametric.

**Verdict:** Theorem 5 is an unsupported claim labeled as a "proof sketch."
No rigorous argument connects the premises to the conclusion.

---

### HIGH

---

#### F-H1: C_Target Search Is Unbounded — C Is Not Computable

**Severity:** HIGH
**Location:** `calibration-map-c-definition.md` §3.1, §4.1

**The definition:**
```
C_target = argmax_{X ∈ DESCENDANTS(D)} { DEPTH(X) :
    X has M-property AND COMPATIBLE(X_system, X_measurement) }
```

**The problem:** DESCENDANTS(D) is the set of ALL descendants of D in TREE.
Since TREE is infinite in depth (formalization §3, Property 2), this is an
infinite set. The argmax over an infinite set may not exist — there could be
an unbounded chain of ever-deeper candidates with no maximum.

The C-definition document acknowledges this at §4.1:
> "the descendant search is bounded in practice but infinite in principle
> — we restrict to computable depth"

But "restrict to computable depth" is not defined, and no bound is
specified. If the bound is arbitrary (e.g., "stop at depth D_max"), then C
is not uniquely defined — different bounds give different calibration maps.

**Impact:** The calibration map C is not well-defined as a mathematical
function on TREE. It requires an external parameter (search depth bound)
that is not part of TREE's structure.

**Falsification test:** Run the executable with depth bound 5 vs depth bound
10 on the same input node. Do they produce different C_target? If yes, C is
not well-defined.

---

#### F-H2: Theorem 4 (Non-Expansiveness) Relies on Incorrect Depth Claim

**Severity:** HIGH
**Location:** `c-contractiveness-proof.md` §6.2

**The claim:**
> C₃ maps N to a descendant of DCA(A_combined, M), which is at depth
> ≥ DEPTH(N). So C₃(N) is in the same ultrametric ball as N.

**Why it's potentially wrong:**

D = DCA(A_combined, M). Both A_combined and M are sub-expressions of N
(at depth ≥ DEPTH(N) + 1 since they're inside N's container). The DCA of
two nodes that are both deeper than N could potentially be N itself (if
they diverged immediately below N), or could be SHALLOWER than N if the
paths diverge earlier.

Wait — A_combined and M are both sub-expressions of N = [A₁...Aₖ M]. They
are DIRECT children of N in the generation tree sense. So ANCESTOR(A_combined, N)
= N and ANCESTOR(M, N) = N. Their DCA is therefore at least N.

Actually, this claim might be correct for the structure as described. Let me
re-examine...

N = [A₁...Aₖ M]. The container [ ... ] IS N. Inside the container, A₁...Aₖ
and M are sub-expressions. The generation tree has N as the parent of these
sub-expressions. So yes, N is the parent of both A_combined (derived from
A₁...Aₖ) and M. Their DCA is at least N.

But REDUCE(A₁...Aₖ) could produce an expression that is NOT a descendant of
the original sub-expressions in the generation tree. REDUCE applies
condensation, cancellation, and double-enclosure, which can SIMPLIFY the
expression. A simplified expression might correspond to a node that is an
ANCESTOR of the original, not a descendant.

For example: if A₁ = ● and A₂ = ●, then REDUCE(A₁ A₂) = REDUCE(●●) = ●
(by condensation). The original sub-expressions [●] and [●] are at depth
DEPTH(N)+1. The reduced form ● is at depth 1. Is ● a descendant of N in the
generation tree? NO — ● is a depth-1 node, while N is at depth ≥ 2. The
reduced form could be an ancestor of N, not a descendant.

This means D = DCA(REDUCE(A₁...Aₖ), M) could be at depth LESS THAN DEPTH(N),
contradicting the claim "at depth ≥ DEPTH(N)."

**Verdict:** The proof that C₃ preserves or increases DCA depth is incorrect
because REDUCE can map a sub-expression to a SIMPLER (shallower) form, which
may change the DCA. The non-expansiveness claim needs a more careful
analysis of how REDUCE interacts with DCA.

---

#### F-H3: COMPATIBLE Is Defined But Not Shown to Be Census-Friendly

**Severity:** HIGH
**Location:** `calibration-map-c-definition.md` §2.3

**The definition:**
```
COMPATIBLE(A, M) ⇔ DEPTH(DCA(A, M)) ≥ min(DEPTH(A), DEPTH(M)) - 1
```

**Issues:**

1. This condition is almost always satisfied. min(DEPTH(A), DEPTH(M)) - 1
   is a depth threshold. DCA(A, M) is the deepest common ancestor. For any
   two nodes in the tree, their DCA depth is at most min(DEPTH(A), DEPTH(M)).
   The -1 allows a one-level gap, which is almost always the case.

   In fact, the only way this FAILS is if A and M are in different branches
   from their immediate common parent — i.e., they are in completely
   different subtrees with no shared structure. But even then, their common
   ancestor might be deep enough.

2. The condition is trivial for many practical pairs — it doesn't constrain
   much, so calibration based on it will accept nearly all candidates.

3. More fundamentally: COMPATIBLE is defined in terms of DEPTH and DCA,
   which are structural properties of TREE. But the INTUITION is about
   "measurement consistency." There's a gap between the structural
   definition and the physical meaning.

**Verdict:** The compatibility condition is nearly vacuous and doesn't
capture the intended notion of "measurement feeds back into system state."

---

#### F-H4: REDUCE Operating on Sub-Expressions Is Underspecified

**Severity:** HIGH
**Location:** `calibration-map-c-definition.md` §3.1, Case 3

**The definition:**
```
Let A_combined = REDUCE(A₁ A₂ ... Aₖ)
```

**The problem:** A₁, A₂, ..., Aₖ are structured sub-expressions (trees), not
flat strings. "REDUCE(A₁ A₂ ... Aₖ)" requires:
1. Flattening the sub-expressions to a string of {●, [, ]}
2. Concatenating them (in what order? Presumably left-to-right)
3. Applying reduction rules (C, X, D) exhaustively

Step 2 is ambiguous: if A₁ is a container [E], flattening gives things like
"[●]" etc. Concatenating [●] with another sub-expression could create
artificial boundary crossings that don't correspond to any structural
operation.

For example, if A₁ = [● and A₂ = ●], then flatten-and-concatenate gives
[●●] which reduces to [●] (by condensation of ●●). But this introduces a
cross-sub-expression boundary that wasn't in the original structure.

**Verdict:** The REDUCE operation on sub-expressions is not well-defined
without specifying the flattening and concatenation semantics. Different
flattening conventions could give different A_combined values, hence
different C(N).

---

### MODERATE

---

#### F-M1: C-Definition and C-Proof Disagree on C's Contractiveness

**Severity:** MODERATE
**Location:** Cross-document

**C-Definition §4.4 states:**
> Conjecture (to be proven in Task 1.2): C is contractive on TREE, i.e.:
> DIST(C(A), C(B)) < DIST(A, B) for all A ≠ B

**C-Proof Theorem 1 states:**
> The calibration map C as defined in Task 1.1 is NOT contractive on TREE.

The C-definition document presents contractiveness as a conjecture to be
proven. The C-proof document proves it false. This is fine in isolation, but
the C-definition document was NOT updated after the proof was completed.
A reader encountering the C-definition first would see the conjecture
presented optimistically, while the actual result is that C fails global
contractiveness.

---

#### F-M2: The Contraction Ratio (≤1/2) Has No Rigorous Basis

**Severity:** MODERATE
**Location:** `c-contractiveness-proof.md` §4.1

**The claim:**
> DIST(C(A), C(B)) ≤ (1/2) · DIST(A, B)

**The issue:** This is stated as if derived, but it appears only in the
context of nodes sharing the same measurement M (which was already shown to
have a flawed proof in F-C1). For the general case, the 1/2 factor comes
from the claim that DCA depth increases by exactly 1, but:

- The DCA depth might increase by MORE than 1 (giving a smaller factor)
- The DCA depth might not increase at all (F-C3, F-H2)
- The DCA depth might even decrease (F-H2 for REDUCE simplification)

No systematic bound is derived from first principles.

---

#### F-M3: No Edge Case Analysis for the C_Target Search

**Severity:** MODERATE
**Location:** `calibration-map-c-definition.md` §3.1

**Missing edge cases:**

1. D has NO descendants with the M-property. What does C(N) return?
   The definition says "C(N) = N" (the "else" branch), but this is implicit.

2. Multiple candidates have the same maximum DEPTH. The argmax is not unique.
   Which one is selected? The definition doesn't specify a tiebreaker.

3. D = N (the DCA of system and measurement IS the node itself). Then
   C_target searches descendants of N, which includes N's children. This
   might produce a loop if no child is self-consistent.

4. COMPATIBLE(X_system, X_measurement) is true for X = N itself. Then the
   argmax might return N (if no deeper candidate exists), making C(N) = N
   (identity).

---

#### F-M4: Idempotence Claim Is Trivially True But Incomplete

**Severity:** MODERATE
**Location:** `calibration-map-c-definition.md` §4.2

**The claim:**
> If C(N) = N, then C(C(N)) = C(N).

**The issue:** This is trivially true (if f(x) = x, then f(f(x)) = f(x) = x)
and doesn't require the proof sketch that follows. But more importantly,
the CONVERSE is not addressed: if C(C(N)) = C(N), does C(N) = N? This
matters because calibration might stabilize at a non-identity node N' where
C(N) = N' ≠ N and C(N') = N'. The idempotence claim only covers the case
where N is ALREADY a fixed point, not where it REACHES one.

---

### LOW

---

#### F-L1: C-Definition §4.3 Makes Contradictory Claims About DEPTH

**Severity:** LOW

**The text:**
> Calibration can either deepen (by finding a more detailed self-consistent
> descendant) or remain at the same depth, but it does not indiscriminately
> reduce depth like F.

This asserts C never reduces depth. But the C-proof document shows that C
can be the identity on non-M-property nodes, which preserves depth. It also
shows the parent-map fallback (in C*) reduces depth. And F-H2 shows that
REDUCE simplification could map to a shallower node. The claim "does not
indiscriminately reduce depth" is ambiguous — does it mean C never reduces
depth, or that it only reduces depth when justified?

---

#### F-L2: "Measurable Domain D_M" Contains No Actual Measurement Semantics

**Severity:** LOW

D_M is defined purely structurally (M-property + non-empty system). The name
"measurable domain" suggests physical measurement, but the membership
criterion has no measurement-theoretic content. A node like [●●● ●●●] is
in D_M simply because it's a container with sub-expressions — there's no
operational sense in which the rightmost ●●● "measures" the first ●●●.

This is a naming issue, not a mathematical error, but it creates a false
impression that the structural condition captures measurement semantics.

---

## §A. Audit Summary

### Findings by Severity

| Severity | Count | IDs |
|----------|-------|-----|
| CRITICAL | 5 | F-C1, F-C2, F-C3, F-C4, F-C5 |
| HIGH | 4 | F-H1, F-H2, F-H3, F-H4 |
| MODERATE | 4 | F-M1, F-M2, F-M3, F-M4 |
| LOW | 2 | F-L1, F-L2 |
| **TOTAL** | **15** | |

### Assessment of Claimed Theorems

| Theorem | Claimed Status | Actual Status After Audit |
|---------|---------------|--------------------------|
| T1 (C not globally contractive) | ✅ Proven | ✅ **HOLDS** — the counterexample (●, []) is valid |
| T2 (C contractive on D_M) | ✅ Proven | ❌ **UNPROVEN** — Lemma 2 has unsound arguments, Lemma 3 is circular |
| T3 (C* globally contractive) | ✅ Proven | ❌ **FALSE AS STATED** — document shows failure cases, then abandons proof |
| T4 (C non-expansive) | ✅ Proven | ⚠️ **SUSPECT** — relies on unexamined REDUCE behavior (F-H2) |
| T5 (C² contractive on D_M) | ✅ Proven | ❌ **UNPROVEN** — only a sketch, no rigorous argument |

### Net Assessment

**Tasks 1.1 and 1.2 are NOT definition-of-done complete.** The C-definition
has four HIGH-severity issues (unbounded search, underspecified REDUCE,
vacuous COMPATIBLE, arbitrary M-property convention). The C-proof has five
CRITICAL failures where claimed proofs are unsound, circular, or abandoned
mid-argument.

This audit does NOT mean the work is worthless. The identification of the
"initial measurement problem" (§5 of the proof) is genuinely insightful,
and the classification of failure modes (§2) is useful. But the core
mathematical claims — that C is contractive on D_M, that C* is globally
contractive — are NOT substantiated by the arguments provided.

### Recommended Remediation Path

1. **F-C1, F-C2:** Rebuild Lemma 2 from scratch. Do not assume that
   internal compatibility implies cross-node convergence. Consider a
   constructive approach: define C₃ to explicitly reduce the system part
   toward the measurement part (e.g., C₃([S M]) = [DCA(S, M)]), which
   would be provably contractive but possibly trivial.

2. **F-C3:** Remove Lemma 3's dependence on T* and the Bootstrap
   Conjecture. Instead, prove that C₃ ALWAYS maps nodes from different
   ROOT branches into the same branch (if this is true), or accept that
   C is only contractive within each ROOT branch and add branch-invariance
   as a separate theorem.

3. **F-C4:** Remove the claim that C* is proved. Either (a) complete the
   proof with the revised 4-case definition and handle the A=∅, B∈D_M case
   rigorously, or (b) downgrade C* to a conjecture and state it as such.

4. **F-C5:** Convert the "proof sketch" into an actual proof, or remove
   the theorem claim.

5. **F-H1:** Define a finite search bound or prove that a maximum exists
   (e.g., there can be at most finitely many self-consistent descendants
   above any depth bound due to tree finiteness).

6. **F-H2:** Analyze REDUCE's effect on DCA depth rigorously. Consider
   defining A_combined without REDUCE (just structural concatenation) to
   avoid the depth-reversal issue.

7. **F-H3:** Either strengthen COMPATIBLE to be more discriminating, or
   acknowledge that it's a placeholder and characterize what properties a
   proper compatibility condition would need.

---

## §B. DoD Gate

| Criterion | Status | Notes |
|-----------|--------|-------|
| Execution Evidence | ✅ | Both documents exist, git commit verified |
| Filesystem Verified | ✅ | Test-Path confirmed for both files |
| Git Verified | ✅ | Commit 3a20123 on feature/deepdive-synthesis |
| Red-Team Passed | ❌ | 5 CRITICAL findings, 4 HIGH — BLOCKING |
| Edge Cases Passed | ❌ | F-M3: 4 edge cases unaddressed |
| Cross-System Sync | ✅ | R2 sync verified (26827 + 27477 bytes) |

**DoD Gate: FAILED.** Red-team audit found BLOCKING issues. Tasks 1.1 and
1.2 should not be considered complete until CRITICAL and HIGH findings are
addressed.

---

*End of Audit*
