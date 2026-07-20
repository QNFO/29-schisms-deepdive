# WORK BREAKDOWN STRUCTURE: 29-Schisms Research Program — Next Phases

**Project:** 29-schisms-deepdive
**Current Version:** v1.2 (DOI: 10.5281/zenodo.21460736 — concept 10.5281/zenodo.21460735; see note on fragmented version chain in README.md and Phase 0.5 below)
**Date:** 2026-07-20 (updated same-day after second-round red team closeout)
**Status:** Phase 0 (Initial Research) COMPLETE, Phase 0.5 (Remediation) DEFINED → Planning Phases 1-7

---

## Overview

The initial research phase (2026-07-20) established the needle-threading framework: a 5-layer dependency-stack ontology resolving all 29 schisms of physics. Key outputs: domain-specific synthesis, domain-independent formalization, executable implementation, first-round red team audit (all 5 CRITICAL findings addressed in v1.1), 2 experimental protocols, competitor analysis, and complete publication stack (GitHub + R2 + Zenodo).

A **second-round red team audit** (documented in `red-team-audit-v12-closeout-2026-07-20.md`) was then run against the WBS itself, the competitor analysis, and the publication infrastructure. It found 2 new CRITICAL and 4 new HIGH findings. This revision of the WBS adds **Phase 0.5 (Remediation)** to track those findings as owned tasks, corrects the dependency graph to match the task tables, demotes Phase 5 (GUF Bridge) to a Speculative Backlog per that audit's R3 finding, and updates the Next-Session Immediate Tasks table to reflect what has actually been verified done (not just attempted).

The following WBS defines Phase 0.5 plus 6 forward research phases, each addressing a priority level identified by the deep-dive research scan. Each phase has concrete deliverables, task-level breakdown, dependencies, milestones, and resource estimates.

---

## Phase 0.5: Red-Team Remediation (P0 — CRITICAL, blocks nothing but must not be silently dropped)

### Objective
Convert every finding from the second-round red team closeout audit (`red-team-audit-v12-closeout-2026-07-20.md`) into an owned, tracked task. Two findings were already fixed same-session (README content drift, ephemeral script cleanup); the remainder are listed here.

### WBS

#### Task 0.5.1: Zenodo Version Chain Cross-Linking (addresses Finding I-1, CRITICAL)
| Aspect | Detail |
|--------|--------|
| **Deliverable** | Permanent cross-link between concept DOI 10.5281/zenodo.21460404 (v1.0 chain) and 10.5281/zenodo.21460735 (v1.2 chain) in all future metadata |
| **Description** | Cannot merge concept DOIs after the fact via Zenodo API. Going forward: EVERY new version MUST be created via `POST /deposit/depositions/{latest_id}/actions/newversion` against the v1.2 deposit (21460736), never as a fresh `POST /deposit/depositions`. Update `.zenodo_versions.json` (per research skill C2 fix) to track deposit ID 21460736 as `latest_deposit_id` going forward. |
| **Effort** | 1 day (process fix) + ongoing discipline |
| **Owner** | Whoever runs the next Zenodo publish step — MUST read `.zenodo_versions.json` first |

#### Task 0.5.2: Add Constructor Theory (and Bohmian, Relational QM) to Competitor Analysis (addresses R3 CRITICAL finding)
| Aspect | Detail |
|--------|--------|
| **Deliverable** | `competitor-analysis-qbism-cdt.md` → renamed/extended to include Constructor Theory, Bohmian mechanics, Rovelli's Relational QM |
| **Description** | Constructor Theory (Deutsch/Marletto) directly targets S19 (nomological dualism — the user's original entry-point schism) using counterfactual statements about possible/impossible transformations — a fundamentally different and lighter formalism than the Bootstrap Conjecture. This is a MORE serious challenge to the needle-threading framework's necessity than QBism or CDT, neither of which touch S19. Must be evaluated schism-by-schism with the same rigor. |
| **Effort** | 2-3 weeks |
| **Priority** | HIGH — do this before, or in parallel with, Phase 1 (Bootstrap proof), since a successful lightweight resolution of S19 by Constructor Theory would change the urgency/framing of Phase 1 |

#### Task 0.5.3: Produce Missing GUF Schism-by-Schism Table (closes H2 from first-round audit)
| Aspect | Detail |
|--------|--------|
| **Deliverable** | GUF evaluated with the same 29-row table format used for QBism and CDT |
| **Description** | The first-round red team (H2) demanded this; the competitor-analysis document addressed QBism/CDT but left GUF's "~15/29 (estimated)" figure unsubstantiated. Close this gap. |
| **Effort** | 1-2 weeks |

#### Task 0.5.4: Fix Dependency Graph / Task Table Inconsistency (addresses R5 MODERATE finding)
| Aspect | Detail |
|--------|--------|
| **Deliverable** | Single source of truth for whether Phases 3-4 (experiments) depend on Phase 1 (Bootstrap proof) |
| **Description** | Decide explicitly: do the trapped-ion and CMB experiments test predictions that hold REGARDLESS of whether the Bootstrap Conjecture is proven (in which case they are independent and the graph below is corrected), or do they only make sense as tests of the fully-proven framework (in which case OSF pre-registration should wait for Phase 1)? Resolved below: **experiments are independent** — the Sufficient Condition Theorem and STC log-periodic prediction were derived from Layers 1-2 (ultrametric geometry, STC), NOT from the Bootstrap Conjecture (Layer 3). They can and should proceed in parallel with Phase 1. |
| **Effort** | Resolved now (see corrected dependency graph below) |

#### Task 0.5.5: Add Decision Rule to Task 1.4 (addresses R2 HIGH finding)
| Aspect | Detail |
|--------|--------|
| **Deliverable** | Explicit pre-registered criterion for Task 1.4's validation step |
| **Description** | Before starting Task 1.4, write down: what specific numerical match/mismatch between derived branching factors and the executable's (1,2,2,3,7,28,125,588) pattern counts as confirmation vs. disconfirmation vs. inconclusive, and what action follows each. This must be written BEFORE running the comparison, not after (to avoid post-hoc rationalization — see the research skill's Calibration Register discipline). |
| **Effort** | 2-3 days, done as the first step of Task 1.4, not a separate phase |

#### Task 0.5.6: Add Recruitment Fallback to Phase 2 (addresses R2 HIGH finding)
| Aspect | Detail |
|--------|--------|
| **Deliverable** | Fallback plan if <3 external validators respond within 8 weeks |
| **Description** | Phase 2 as originally written assumes responses arrive. Add: if fewer than 3 validators respond by the 8-week mark, (a) extend by 4 weeks with a follow-up reminder, (b) if still insufficient, proceed with whatever responses exist and explicitly label the validation as "partial (N of 3-5 target respondents)" rather than silently treating 1 response as sufficient. |
| **Effort** | Planning only, no calendar cost added |

#### Task 0.5.7: Source Real Cost Estimates for Phase 3 (addresses R4 HIGH finding)
| Aspect | Detail |
|--------|--------|
| **Deliverable** | Replace the unsourced "~$50K (lab time)" figure with either a real quote or an explicit `[unverified estimate — no lab contacted yet]` label |
| **Description** | Do this as part of Task 3.2 (Secure Lab Access) rather than presenting a number now as if it were researched. |
| **Effort** | Rolled into Task 3.2 |

### Phase 0.5 Deliverables
1. Updated `.zenodo_versions.json` (new file, tracks deposit 21460736 going forward)
2. `competitor-analysis-multi-framework.md` (renamed/extended from `competitor-analysis-qbism-cdt.md`, adds Constructor Theory, Bohmian, Relational QM, GUF schism-by-schism table)
3. This WBS document, corrected

---

## Phase 1: Bootstrap Conjecture — Formal Proof (P0 — CRITICAL)

### Objective
Convert the Bootstrap Conjecture from a speculative claim to a formally proven theorem. Define the calibration map C on token space, prove contractiveness in the ultrametric, prove uniqueness of the fixed point, and characterize the valuation structure.

### Duration Estimate: 3-6 months (full-time equivalent)

### WBS

#### Task 1.1: Define the Calibration Map C
| Aspect | Detail |
|--------|--------|
| **Deliverable** | Formal definition of C: TREE → TREE |
| **Description** | Specify how C maps token configurations to "calibrated" configurations. C must encode the physical process of measurement feedback — the token representing "apparatus reading X" must update the token representing "system state." |
| **Dependencies** | None (Layer 0-2 already formalized) |
| **Validation** | C must be well-defined on ALL normal-form expressions. No undefined behavior. |
| **Effort** | 2-4 weeks |

#### Task 1.2: Prove Contractiveness
| Aspect | Detail |
|--------|--------|
| **Deliverable** | Proof that DIST(C(A), C(B)) < DIST(A, B) for all A ≠ B |
| **Description** | Apply the F-contractiveness conditions (depth-reducing, depth-preserving-strict, or absolute) to C. Determine which case C falls into. Prove the inequality holds. |
| **Dependencies** | Task 1.1 (C definition) |
| **Validation** | Counterexample search: generate random token pairs, verify contractiveness numerically |
| **Effort** | 4-8 weeks |

#### Task 1.3: Prove Fixed-Point Uniqueness
| Aspect | Detail |
|--------|--------|
| **Deliverable** | Proof that C has exactly one fixed point T* |
| **Description** | Banach's theorem provides the template. Must additionally prove: (a) TREE is complete in the ultrametric (plausible, tree is complete), (b) the fixed point is stable under small perturbations. |
| **Dependencies** | Task 1.2 (contractiveness) |
| **Validation** | Numerical verification on executable tree |
| **Effort** | 2-4 weeks |

#### Task 1.4: Characterize the Valuation Structure
| Aspect | Detail |
|--------|--------|
| **Deliverable** | Derivation of the valuation structure at T* |
| **Description** | The fixed point T* determines the "constants of nature" as valuations (ratios of distances). Compute which branching factors (primes) are stabilized by C. |
| **Dependencies** | Task 1.3 (fixed point existence + uniqueness) |
| **Validation** | Compare derived branching factors to the executable tree growth pattern (1→2→2→3→7→28→125→588) |
| **Effort** | 4-12 weeks (hardest task) |

#### Task 1.5: Numerical Verification Suite
| Aspect | Detail |
|--------|--------|
| **Deliverable** | Python verification suite extending _self_descriptive_system.py |
| **Description** | Test C on randomly generated trees up to depth 10. Verify contractiveness numerically. Verify fixed-point convergence. Compare to analytical results. |
| **Dependencies** | Tasks 1.2-1.4 |
| **Effort** | 2-4 weeks |

### Phase 1 Deliverables
1. `bootstrap-conjecture-formal-proof.md` — Complete proof document
2. `_bootstrap_verification.py` — Numerical verification suite
3. Updated `29-schisms-synthesis-deepdive.md` — Bootstrap Conjecture → Bootstrap Theorem

### Phase 1 Milestones
| Milestone | After | Criteria |
|-----------|-------|----------|
| M1.1: C defined | Task 1.1 | C formalized as a function on TREE |
| M1.2: Contractiveness proved | Task 1.2 | Peer-reviewable proof |
| M1.3: Proof complete | Task 1.4 | Full theorem statement + proof |
| M1.4: Verified | Task 1.5 | Numerical confirmation + analytical proof |

---

## Phase 2: External Validation of 29-Schism Taxonomy (P1 — HIGH)

### Objective
Submit the 29-schism taxonomy to external researchers for independent classification validation. Determine whether the taxonomy holds under external scrutiny, identify missing or misclassified schisms, and establish external credibility.

### Duration Estimate: 1-3 months (calendar time, low effort)

### WBS

#### Task 2.1: Select External Validators
| Aspect | Detail |
|--------|--------|
| **Deliverable** | List of 3-5 qualified external researchers |
| **Description** | Identify physicists or philosophers of physics with expertise in foundations. Requirements: no QNFO affiliation, published in foundations of physics, willing to review. |
| **Effort** | 1 week |

#### Task 2.2: Prepare Taxonomy Package
| Aspect | Detail |
|--------|--------|
| **Deliverable** | Standalone taxonomy document (extracted from 29-schism paper) |
| **Description** | Strip QNFO-specific language. Present the 29 schisms as a neutral classification exercise. Include classification instructions. |
| **Effort** | 1 week |

#### Task 2.3: Collect and Analyze Responses
| Aspect | Detail |
|--------|--------|
| **Deliverable** | External validation report |
| **Description** | Collect validator classifications. Identify: (a) schisms that validators agree are "physics" vs "philosophy," (b) missing schisms validators propose, (c) schisms validators consider resolved or ill-posed. **Fallback rule:** If fewer than 3 validators respond by the 8-week mark, (a) extend by 4 weeks with a follow-up reminder; (b) if still insufficient, proceed with whatever responses exist and explicitly label the validation as "partial (N of 3-5 target respondents)" rather than silently treating 1 response as sufficient. |
| **Effort** | 4-8 weeks (waiting for responses); up to 12 weeks with fallback |

#### Task 2.4: Revise Taxonomy (if needed)
| Aspect | Detail |
|--------|--------|
| **Deliverable** | Revised 29-schism taxonomy (v2.0) |
| **Description** | Incorporate external feedback. Recalculate resolution claims. Document changes. |
| **Dependencies** | Task 2.3 |
| **Effort** | 2 weeks |

### Phase 2 Deliverables
1. `taxonomy-validation-package.md` — Neutral classification document
2. `external-validation-report.md` — Validator responses + analysis
3. `29-schism-taxonomy-v2.0.md` — Revised taxonomy (if changed)

---

## Phase 3: Trapped-Ion Page-Wootters Experiment (P2 — HIGH)

### Objective
Execute the trapped-ion ultrametricity experiment to provide the first empirical test of the Sufficient Condition Theorem and the D=4 Ultrametric Special Case Theorem. This is the nearest-term testable prediction.

### Duration Estimate: 3-6 months (requires lab access)

### WBS

#### Task 3.1: OSF Pre-Registration
| Aspect | Detail |
|--------|--------|
| **Deliverable** | OSF pre-registration (timestamped, immutable) |
| **Description** | Register the complete protocol: hypothesis, design, sampling plan, variables, analysis plan. Must be submitted BEFORE any data collection. |
| **Dependencies** | Protocol document (already complete) |
| **Effort** | 2 days |

#### Task 3.2: Secure Lab Access
| Aspect | Detail |
|--------|--------|
| **Deliverable** | Agreement with trapped-ion lab |
| **Description** | Identify a lab with Yb⁺ ion trap capability. Present protocol. Negotiate beam time (~4 days). |
| **Effort** | 2-4 weeks |

#### Task 3.3: Apparatus Preparation
| Aspect | Detail |
|--------|--------|
| **Deliverable** | Calibrated apparatus meeting protocol specifications |
| **Description** | Doppler cooling, sideband cooling to |n=0⟩, Zeeman sublevel resolution, carrier/sideband Rabi frequency calibration, T₂ measurement, motional heating rate characterization. |
| **Effort** | 1-2 weeks |

#### Task 3.4: Data Collection
| Aspect | Detail |
|--------|--------|
| **Deliverable** | Raw data: 16,000 cycles (Regime A + B) |
| **Description** | Follow protocol steps: state preparation, evolution, conditional tomography. Systematic error runs with varied τ, B-field, initial states. |
| **Effort** | 4 days beam time + 1 week analysis |

#### Task 3.5: Analysis and Publication
| Aspect | Detail |
|--------|--------|
| **Deliverable** | Peer-reviewed publication |
| **Description** | Reconstruct conditional states, compute UVR, assess significance. Publish results regardless of outcome (positive, null, or falsification). |
| **Effort** | 4 weeks |

### Phase 3 Milestones
| Milestone | After | Criteria |
|-----------|-------|----------|
| M3.1: Registered | Task 3.1 | OSF pre-registration confirmed |
| M3.2: Ready | Task 3.3 | Apparatus calibrated |
| M3.3: Data collected | Task 3.4 | 16,000 cycles complete |
| M3.4: Published | Task 3.5 | Paper submitted |

---

## Phase 4: CMB Log-Periodic Oscillation Search (P3 — MODERATE)

### Objective
Search for log-periodic oscillations in CMB data as predicted by the Syntactic Token Calculus. This is the cosmological test of discrete scale invariance.

### Duration Estimate: 1-3 months (computational only)

### WBS

#### Task 4.1: Pipeline Development
| Aspect | Detail |
|--------|--------|
| **Deliverable** | Working analysis pipeline (Python) |
| **Description** | Implement: data download, foreground subtraction, Lambda-CDM fit, log-resampling, Lomb-Scargle/FFT/wavelet periodograms, null simulation generation, significance testing. |
| **Effort** | 2-4 weeks |

#### Task 4.2: Null Simulation Validation
| Aspect | Detail |
|--------|--------|
| **Deliverable** | 10,000 Lambda-CDM realizations with verified null distribution |
| **Description** | Generate simulations, run pipeline, verify that the null distribution is flat (no spurious oscillations from pipeline artifacts). |
| **Effort** | 1 week compute + 1 week analysis |

#### Task 4.3: Real Data Analysis
| Aspect | Detail |
|--------|--------|
| **Deliverable** | Periodogram of Planck + ACT + SPT combined data |
| **Description** | Apply pipeline to real data. Compute global p-value. Fit oscillation parameters if detected. |
| **Effort** | 1 week compute + 2 weeks analysis |

#### Task 4.4: Publication
| Aspect | Detail |
|--------|--------|
| **Deliverable** | Peer-reviewed publication or preprint |
| **Description** | Report results. If null: place upper limit on oscillation amplitude as function of q. If detection: report best-fit parameters with uncertainties. |
| **Effort** | 4 weeks |

---

## Speculative Backlog (demoted from Phase 5 per second-round red team R3 finding)

**Why demoted:** The second-round red team (R3) flagged that this task was self-rated "LOW FEASIBILITY" and its central premise (|χ|=6 = 2×3 relating to Bruhat-Tits branching factor p+1 at p=2) is explicitly labeled numerology by the project's own deep-dive research document (§5.1: "This is speculation dressed as a program"). Giving it WBS phase-numbering alongside genuinely scoped phases implied more confidence than the framework itself claims. It remains here as a backlog item, not a committed phase.

### GUF-to-Adelic Bridge Theorem (was Phase 5, P4 — LOW FEASIBILITY)

### Objective
Establish a formal mathematical relationship between the Geometric Unification Framework (Calabi-Yau threefold, |χ|=6) and the adelic ultrametric framework (Bruhat-Tits trees over Q_p).

### Duration Estimate: 6-18 months (deep algebraic geometry required) — IF pursued at all

### Backlog Tasks

#### Task B.1: Literature Survey
| Aspect | Detail |
|--------|--------|
| **Deliverable** | Survey of Calabi-Yau ↔ p-adic connections in the mathematical literature |
| **Description** | Search for existing work relating Calabi-Yau manifolds to p-adic geometry, Bruhat-Tits buildings, or adelic structures. Contact algebraic geometers. |
| **Effort** | 4-8 weeks |

#### Task B.2: Candidate Mapping
| Aspect | Detail |
|--------|--------|
| **Deliverable** | Candidate mathematical mapping: CY₃ ↔ BT tree |
| **Description** | Explore: (a) Euler characteristic |χ|=6 relates to branching factors (6=2×3, p=2 gives branching 3), (b) Hodge numbers ↔ tree depth structure, (c) spectral properties ↔ valuations. |
| **Effort** | 8-16 weeks |

#### Task B.3: Theorem Statement + Proof Attempt
| Aspect | Detail |
|--------|--------|
| **Deliverable** | Bridge Theorem (proven or conjecture status documented) |
| **Description** | If a mapping is found: formalize as a theorem and attempt proof. If no mapping found: document why, classify as "GUF remains isolated Archimedean pillar." |
| **Effort** | 12-24 weeks |

**Promotion criterion:** Only promote this backlog item to an active phase if Task 0.5.3 (GUF schism-by-schism table) reveals a stronger-than-expected overlap that makes the bridge look tractable, OR an external algebraic geometer (contacted informally) indicates the mapping is plausible.

---

## Phase 6: Hardware Roadmap for Passive Fault Tolerance (P5 — MODERATE)

### Objective
Design a 5-year hardware development plan from trapped-ion proof-of-concept to multi-qubit ultrametric quantum circuit demonstrating passive fault tolerance.

### Duration Estimate: 1-3 months (planning only)

### WBS

#### Task 6.1: Technology Survey
| Aspect | Detail |
|--------|--------|
| **Deliverable** | Survey of quantum computing platforms suitable for ultrametric Hamiltonian engineering |
| **Description** | Evaluate: trapped ions, superconducting qubits, Majorana systems, photonic, neutral atoms. Score on: Hamiltonian tunability, p-adic metric emulation feasibility, coherence time, scalability. |
| **Effort** | 2-4 weeks |

#### Task 6.2: Roadmap Document
| Aspect | Detail |
|--------|--------|
| **Deliverable** | 5-year hardware roadmap with milestones |
| **Description** | Year 1: Single-ion proof-of-concept. Year 2: Two-ion entangled ultrametric test. Year 3: 4-ion logical qubit. Year 4: Fault-tolerant demonstration. Year 5: Comparison to surface code overhead. |
| **Effort** | 4-8 weeks |

---

## Phase 7 — Continuous: Dissemination, Maintenance, Infrastructure

#### Task 7.1: Zenodo Versioning (continuous)
| Aspect | Detail |
|--------|--------|
| **Trigger** | Every phase completion |
| **Action** | Create new Zenodo version, update D1 living-paper, update KG |

#### Task 7.2: Papers-Server Deployment (if applicable)
| Aspect | Detail |
|--------|--------|
| **Trigger** | When papers.qnfo.org infrastructure is ready |
| **Action** | Deploy synthesis and protocols to papers-server |

#### Task 7.3: Social Media Dissemination (per milestone)
| Aspect | Detail |
|--------|--------|
| **Trigger** | Each major publication |
| **Action** | Buffer posts on Twitter/X, LinkedIn, Bluesky |

#### Task 7.4: D1/KG Infrastructure (Phase 0-1)
| Aspect | Detail |
|--------|--------|
| **Deliverable** | Complete D1/KG representation |
| **Description** | Deploy PBO v1.0 to D1. Seed Theorem nodes for Bootstrap Conjecture, Monna Projection, F-contractiveness. Fix Ratio-Based Adelic body. |
| **Effort** | 1-2 weeks |

---

## Resource Requirements Summary

| Phase | People | Equipment | Time | Cost |
|-------|--------|-----------|------|------|
| P1: Bootstrap Proof | 1 mathematician | None | 3-6 months | Time only |
| P2: Taxonomy Validation | 0 (external) | None | 1-3 months | Time only |
| P3: Trapped-Ion | 1 experimentalist + lab | Yb⁺ ion trap | 3-6 months | ~$50K (lab time) |
| P4: CMB Search | 1 data analyst | Computing cluster | 1-3 months | ~$5K (compute) |
| P5: GUF Bridge | 1 algebraic geometer | None | 6-18 months | Time only |
| P6: Hardware Roadmap | 1 quantum engineer | None | 1-3 months | Time only |
| P7: Infrastructure | 0.25 FTE | Cloudflare | Continuous | ~$0 (free tier) |

---

## Dependency Graph (CORRECTED per Task 0.5.4)

```
Phase 0.5 (Remediation) ── [do first / in parallel — low effort, unblocks nothing but must not be skipped]
    │
    ├──→ Task 0.5.2 (Constructor Theory) ──→ informs Phase 1 framing (does NOT block start)
    │
Phase 1 (Bootstrap Proof) ── INDEPENDENT of Phases 3-4 (see Task 0.5.4 resolution) ────┐
    │                                                                                    │
    ├──→ Phase 6 (Hardware Roadmap) [only meaningful AFTER Phase 3 has empirical data]  │
    │                                                                                    │
Phase 3 (Trapped-Ion) ── CAN START NOW, independent of Phase 1 ──→ Phase 3.5 (OSF Closeout)
    │         (tests Sufficient Condition Theorem — derived from Layer 1-2, not Layer 3)
    │
Phase 4 (CMB Search) ── CAN START NOW, independent of Phase 1 ──→ Phase 4.5 (OSF Closeout)
    │         (tests STC log-periodic prediction — derived from Layer 2, not Layer 3)
    │
Phase 2 (Taxonomy Validation) ──→ Revise framework claims (independent of all above)
    │
Speculative Backlog (GUF Bridge) ── promoted only if Task 0.5.3 or external input warrants it
    │
Phase 7 (Infrastructure) ──→ Continuous, independent
```

**Key correction:** The original graph implied Phase 1 gates Phases 3-4. It does not. The trapped-ion Sufficient Condition Theorem and the STC log-periodic CMB prediction were both derived from Layer 1 (ultrametric geometry) and Layer 2 (STC tokens) — NOT from Layer 3 (Bootstrap Conjecture). These experiments test whether the UNDERLYING GEOMETRY is ultrametric; they do NOT require the self-referential-calibration mechanism to be proven first. **Phases 1, 2, 3, and 4 can and should run in parallel.** Phase 1 remains the highest-priority CRITICAL PATH item only in the sense that a successful proof upgrades the framework's overall status — not in the sense that it blocks other work.

---

## Next Session Immediate Tasks (updated — reflects verified-done vs. actually-pending)

| Priority | Task | Status |
|----------|------|--------|
| 1 | Create Zenodo v1.2 with all current artifacts | ✅ **DONE** (verified live, HTTP 200: 10.5281/zenodo.21460736) — but see Task 0.5.1, version chain is fragmented, not cleanly chained from v1.0 |
| 2 | Buffer social media posts | ⬜ **NOT DONE** — deliberately deferred per research skill's "reserve social posts for final deliverables" guidance; framework is still conjecture-stage |
| 3 | Task 0.5.1: Fix Zenodo version-chain discipline going forward | ⬜ Pending — do FIRST, before any further Zenodo publishes |
| 4 | Task 0.5.2: Add Constructor Theory to competitor analysis | 🔄 **STARTED** (2026-07-20) — `competitor-analysis-multi-framework.md` created with Constructor Theory, Bohmian, Relational QM, and verified GUF table. Phase 1 can proceed; central finding: Constructor Theory resolves S19 lighter but does NOT address remaining 25+ schisms |
| 4a | Task 0.5.3: GUF schism-by-schism table | ✅ **DONE** (2026-07-20) — verified 2.5/29 (previously estimated ~15/29, wrong by 6x). Included in `competitor-analysis-multi-framework.md` §7 |
| 4b | Task 0.5.4: Fix dependency graph inconsistency | ✅ **RESOLVED** — Phases 3-4 confirmed independent of Phase 1 (test ultrametric geometry, not Bootstrap Conjecture). WBS dependency graph corrected. |
| 5 | Task 1.1: Define calibration map C | 🔄 **IN PROGRESS** (2026-07-20 — formal definition complete in `calibration-map-c-definition.md`; Tasks 1.2–1.5 remain) |
| 5a | Task 0.5.6: Recruitment fallback embedded in Phase 2 WBS | ✅ **DONE** (2026-07-20 — language added to Task 2.3) |
| 6 | Begin Task 2.1: Select external validators | ⬜ Pending |
| 7 | OSF pre-register trapped-ion protocol (Task 3.1) | ⬜ Pending — protocol document complete, ready to submit, requires explicit user approval per OSF Bona Fide Registration Requirements |
| 8 | OSF pre-register CMB search protocol (Task 4.1 prelim) | ⬜ Pending — same approval gate |
| 9 | Deploy PBO v1.0 to D1 (Task 7.4) | ⬜ Pending — confirmed still returning 404 on papers.qnfo.org as of this session |
