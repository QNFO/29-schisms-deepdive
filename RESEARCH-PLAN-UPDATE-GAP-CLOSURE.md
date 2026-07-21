# Research Plan Update: Gap-Closure and Next Phases

**Project:** 29-Schisms Deep-Dive v2.2
**Date:** 2026-07-21
**Status:** Strategic update following formal paper publication (DOI: 10.5281/zenodo.21468103)
**Based on:** Literature scan (arXiv, Semantic Scholar, QNFO Vectorize/KG), 4 red-team audits, competitor analysis

---

## §0. Summary: Where We Are

The formal paper (20 pages, Pandoc+XeLaTeX) establishes the framework's scope and limitations honestly. The central finding is that **the Bootstrap Conjecture remains unproven** — no known calibration map on the expression tree satisfies all three requirements simultaneously:

1. **Well-defined** (finite computation for every input)
2. **Non-expansive** (DIST(C(A), C(B)) $\le$ DIST(A, B) for all A, B)
3. **Non-trivial fixed point** (T* $\neq$ $\emptyset$, T* $\neq$ $\bullet$)

The calibration map C v2.0 satisfies (1) and idempotence but fails (2). The parent map satisfies (1) and (2) but fails (3). This is not a failure of effort — it reflects a genuine mathematical tension that the Bootstrap Conjecture claims can be resolved. Proving or disproving it is the central research task.

---

## §1. Gap Register

| Gap | Severity | Description | External Confirmation |
|-----|----------|-------------|----------------------|
| **G1** | CRITICAL | Bootstrap Conjecture unproven — no known map satisfies all three constraints | Literature scan confirms NO prior work on calibration maps on expression trees. Ultrametric fixed-point results (Banach 1922, Priess-Crampe & Ribenboim 1997) establish existence for contractive maps in general ultrametric spaces, but the TREE-specific construction problem is novel. |
| **G2** | CRITICAL | No empirical confirmation — Phases 3-4 (trapped-ion, CMB) not yet executed | No external experimental tests of ultrametric quantum structure found in literature. |
| **G3** | HIGH | Constructor Theory resolves S19 with a lighter formalism | CT latest work (arXiv:2505.08692 "Constructor Theory of Time," 2025; arXiv:2606.07352 "Tests of CT," 2026) does NOT extend coverage beyond ~5 schisms. No CT paper addresses Layer 1 (math substrate), Layer 4 (spacetime), or Layer 5 (epistemology). Gap closure by CT remains a monitoring risk, not an active competitor. |
| **G4** | HIGH | Computational tractability unknown — tree grows exponentially (base $\sim$4.7) | Depth-7 (588 nodes) computable; depth-20 ($\sim 10^{12}$) likely not. Classical-limit projections computable via $\varepsilon$-neighborhood coarse-graining. |
| **G5** | MODERATE | M-property convention arbitrary — "rightmost = measurement" has no structural justification | No external literature addressing measurement encoding in formal systems found. |
| **G6** | MODERATE | External validation not completed — Phase 2 emails drafted but not sent | Validator candidates selected, emails written, taxonomy package ready. Requires Cloudflare Email Service domain onboarding. |

---

## §2. Updated Phase Structure

### Phase 1: Bootstrap Conjecture — Mathematical Attack (P0, CRITICAL)

**Objective:** Prove or disprove the existence of a non-trivial calibration map satisfying well-definedness + non-expansiveness + non-trivial fixed point.

**Status:** Tasks 1.1-1.2 DONE. Task 1.3 remains open and is now the highest-priority task in the project.

#### Restructured Tasks

**Task 1.3: Characterize the Space of Ancestor-Monotone Maps on TREE**

| Aspect | Detail |
|--------|--------|
| **Deliverable** | Classification theorem for all maps $F: TREE \to TREE$ satisfying DEPTH(F(N)) $\le$ DEPTH(N) and non-expansiveness |
| **Approach** | Restrict to ancestor-monotone maps (maps that always return ancestors or the node itself). This is the natural class for calibration — measurement cannot create new structure, only filter existing structure. Within this class, characterize necessary and sufficient conditions for non-expansiveness. |
| **Effort** | 2-4 weeks |
| **Rationale** | C v2.0 is ancestor-monotone but fails non-expansiveness (Theorem 7). Understanding WHY it fails — and whether ANY ancestor-monotone map can succeed — bounds the solution space. |

**Task 1.3a: The Nontriviality Constraint**

| Aspect | Detail |
|--------|--------|
| **Deliverable** | Proof or counterexample: "There exists an ancestor-monotone, non-expansive map F on TREE with fixed point T* $\neq$ $\emptyset$ and T* $\neq$ $\bullet$." |
| **Approach** | Attempt constructive counterexample: design a map that preserves structure below a calibration depth while contracting above it. Test candidate maps on the executable tree (depths 0-7). If no such map exists at depth $\le$ 7, this strongly suggests none exists at any depth. |
| **Effort** | 4-8 weeks |
| **Validation** | Numerical search on executable tree, followed by analytic proof attempt |

**Task 1.3b: If Q1 Is "No" — Reframe the Conjecture**

| Aspect | Detail |
|--------|--------|
| **Deliverable** | Revised framework statement: either (a) "Bootstrap Conjecture is false for TREE as defined — here's why, and here's the minimal modification needed," or (b) "The conjecture holds under additional constraints (specify which)" |
| **Approach** | If no ancestor-monotone non-expansive map exists, document why. Consider: relaxing non-expansiveness to "non-expansive on the fixed-point trajectory only," or redefining TREE with additional structure (e.g., weighted edges, typed distinctions) |
| **Effort** | 2-4 weeks |
| **Dependencies** | Task 1.3a outcome |

**Task 1.4: Valuation Structure Characterization** (deferred until Task 1.3 settles)

| Aspect | Detail |
|--------|--------|
| **Deliverable** | Derivation of branching factors at T* (if T* exists) |
| **Dependencies** | Task 1.3 or 1.3a — needs a working calibration map first |
| **Effort** | 4-12 weeks |

---

### Phase 2: External Validation (P1, HIGH)

**Objective:** Obtain independent classification of the 29-schism taxonomy from 3-5 external researchers.

**Status:** Package ready. Emails drafted. Blocked on Cloudflare Email Service domain onboarding.

**Unblocking requirement:** Onboard qnfo.net to Cloudflare Email Service (15 minutes), then send 5 validator emails.

| Task | Status | Effort |
|------|--------|--------|
| 2.1: Select validators | ✅ Complete | — |
| 2.2: Prepare taxonomy package | ✅ Complete | — |
| 2.3: Send emails + collect responses | ⬜ Needs domain onboarding | 1 hour setup + 8-12 weeks wait |
| 2.4: Revise taxonomy | ⬜ After responses | 2 weeks |

---

### Phase 3-4: Experimental Falsification (P2, HIGH)

**Objective:** Test the ultrametric structure prediction independent of Bootstrap Conjecture status.

**Note:** Phases 3-4 test Layer 1-2 predictions (ultrametric geometry), NOT Layer 3 (calibration mechanism). They are independent of Phase 1 outcome and can proceed in parallel.

**Blocked on:** User approval for OSF pre-registration + lab access.

---

### Phase 5: Constructor Theory Monitoring (P3, MODERATE)

**Objective:** Track Constructor Theory developments for S19 gap closure.

**Action:** Set up automated arXiv keyword alert for "constructor theory" + "counterfactual" + "nomological dualism." Review quarterly.

**Current risk level:** LOW. CT has not extended beyond ~5 schisms in 11 years (2014-2025). The 2025 "Constructor Theory of Time" paper (150 pages) is still a conceptual framework, not a solved theory. No CT paper addresses mathematical substrate, spacetime emergence, or observer epistemology.

---

### Phase 6: Hardware Roadmap (P4, COMPLETE)

✅ Tasks 6.1-6.2 done. Technology survey (5 platforms) + 5-year roadmap with milestones.

---

### Phase 7: Continuous Tasks

| Task | Trigger | Status |
|------|---------|--------|
| 7.1: Zenodo versioning | Each phase completion | v2.2 published (DOI: 10.5281/zenodo.21468103) |
| 7.2: Papers-server deployment | When papers.qnfo.org ready | Blocked (404) |
| 7.3: Social media dissemination | Each major publication | Deferred per research skill guidance |
| 7.4: D1/KG infrastructure | Continuous | Blocked (PBO 404) |

---

## §3. Updated WBS: Next-Session Immediate Tasks

| Priority | Task | Status | Blocker |
|----------|------|--------|---------|
| **1** | **Task 1.3: Characterize ancestor-monotone maps on TREE** | ⬜ **NEW** — highest priority. Classify all maps F: TREE $\to$ TREE satisfying DEPTH(F(N)) $\le$ DEPTH(N) and non-expansiveness. | None — executable |
| **2** | Task 2.3: Send validator emails + Cloudflare Email domain onboarding | ⬜ Pending — emails drafted, taxonomy package ready | Domain onboarding (15 min) |
| **3** | OSF pre-register trapped-ion protocol (Task 3.1) | ⬜ Pending | User approval required |
| **4** | OSF pre-register CMB search protocol (Task 4.1) | ⬜ Pending | User approval required |
| 5 | Task 1.4: Valuation structure | ⬜ Blocked | Needs Task 1.3 outcome |
| 6 | Task 7.4: PBO deployment | ⬜ Blocked | 404 on papers.qnfo.org |

---

## §4. Literature Scan Methodology

**Sources queried:**
1. arXiv API — `ultrametric fixed-point`, `p-adic Banach`, `constructor theory extension`, `self-descriptive formal system`, `Spencer-Brown calibration`
2. Semantic Scholar — `ultrametric fixed-point calibration`, `non-Archimedean Banach`
3. Web search — "constructor theory 2025 2026 schisms"
4. QNFO Vectorize — all topics
5. QNFO Knowledge Graph — related papers

**Key finding:** No external work exists on calibration maps on expression trees. The ultrametric fixed-point literature (Banach 1922, Priess-Crampe & Ribenboim 1997) establishes general existence results for contractive maps in complete ultrametric spaces, but the specific problem of constructing a non-trivial calibration map on the Spencer-Brown expression tree is novel. This gap is genuine — it is not that the map has been found by others and we missed it, but that no one has attempted this specific construction.

**Constructor Theory monitoring:** arXiv:2505.08692 ("Constructor Theory of Time," 2025, 150 pages) is the most recent major CT work. It proposes time as the resource whose availability determines which tasks are possible. It does not extend CT coverage to additional schisms. arXiv:2606.07352 ("Tests of Constructor Theory," 2026) proposes experimental tests but does not expand the theoretical framework beyond existing scope. Risk of CT closing G3 in the next 12-24 months is LOW.

**Recent p-adic/ultrametric physics (2025-2026):** Active area focused on holography, AdS/CFT, and inflationary model-building — phenomenological applications of p-adic structures, not foundational self-descriptive systems. No work found connecting p-adic geometry to Spencer-Brown algebras or self-referential calibration.

---

## §5. The Core Mathematical Problem (Restated)

The Bootstrap Conjecture reduces to this:

> **Given the Spencer-Brown expression tree (TREE) with the ultrametric DIST, construct an ancestor-monotone map C: TREE $\to$ TREE such that:**
> 1. C is non-expansive: DIST(C(A), C(B)) $\le$ DIST(A, B) for all A, B
> 2. The fixed point T* = $\lim_{n\to\infty}$ C$^n$($\emptyset$) satisfies T* $\neq$ $\emptyset$ and T* $\neq$ $\bullet$
> 3. T* encodes the tree's structural properties — its position in TREE reflects the tree's own branching structure

The parent map satisfies (1) but fails (2). C v2.0 satisfies idempotence but fails (1). The problem is to find a map in the intersection — or prove the intersection is empty.

**If the intersection is empty:** The Bootstrap Conjecture, as currently stated, is false. The framework would need revision — either relaxing the constraints or restructuring the tree itself. The experimental predictions (Phases 3-4) would remain valid independent of this outcome.

**If the intersection is non-empty:** Characterize T* and derive the branching structure. Compare to the observed growth pattern (1, 2, 2, 3, 7, 28, 125, 588). A match would be strong evidence; a mismatch would constrain the tree's definition.

---

## §6. References

[1] Banach, S. "Sur les operations dans les ensembles abstraits." Fund. Math., 1922.
[2] Priess-Crampe, S. and Ribenboim, P. "Fixed points, combs and generalized power series." Abh. Math. Sem. Univ. Hamburg, 1997.
[3] Deutsch, D. and Marletto, C. "Constructor Theory of Time." arXiv:2505.08692, 2025.
[4] Marletto, C., Deutsch, D. and Vedral, V. "Tests of Constructor Theory." arXiv:2606.07352, 2026.
[5] Monna, A.F. "Sur une transformation simple des nombres p-adiques en nombres reels." Indag. Math., 1953.
[6] Spencer-Brown, G. *Laws of Form.* Allen & Unwin, 1969.
[7] QNFO Research. "Threading the Needle: A Self-Descriptive Ultrametric Framework for the 29 Schisms of Physics v2.2." Zenodo, DOI: 10.5281/zenodo.21468103, 2026.
