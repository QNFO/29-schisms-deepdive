# WORK BREAKDOWN STRUCTURE: 29-Schisms Research Program — Next Phases

**Project:** 29-schisms-deepdive
**Current Version:** v1.1 (DOI: 10.5281/zenodo.21465629)
**Date:** 2026-07-20
**Status:** Phase 0 (Initial Research) COMPLETE → Planning Phases 1-5

---

## Overview

The initial research phase (2026-07-20) established the needle-threading framework: a 5-layer dependency-stack ontology resolving all 29 schisms of physics. Key outputs: domain-specific synthesis, domain-independent formalization, executable implementation, red team audit (all 5 CRITICAL findings addressed), 2 experimental protocols, competitor analysis, and complete publication stack (GitHub + R2 + Zenodo).

The following WBS defines the next 5 research phases, each addressing a priority level identified by the deep-dive research scan. Each phase has concrete deliverables, task-level breakdown, dependencies, milestones, and resource estimates.

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
| **Description** | Collect validator classifications. Identify: (a) schisms that validators agree are "physics" vs "philosophy," (b) missing schisms validators propose, (c) schisms validators consider resolved or ill-posed. |
| **Effort** | 4-8 weeks (waiting for responses) |

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

## Phase 5: GUF-to-Adelic Bridge Theorem (P4 — LOW FEASIBILITY)

### Objective
Establish a formal mathematical relationship between the Geometric Unification Framework (Calabi-Yau threefold, |χ|=6) and the adelic ultrametric framework (Bruhat-Tits trees over Q_p).

### Duration Estimate: 6-18 months (deep algebraic geometry required)

### WBS

#### Task 5.1: Literature Survey
| Aspect | Detail |
|--------|--------|
| **Deliverable** | Survey of Calabi-Yau ↔ p-adic connections in the mathematical literature |
| **Description** | Search for existing work relating Calabi-Yau manifolds to p-adic geometry, Bruhat-Tits buildings, or adelic structures. Contact algebraic geometers. |
| **Effort** | 4-8 weeks |

#### Task 5.2: Candidate Mapping
| Aspect | Detail |
|--------|--------|
| **Deliverable** | Candidate mathematical mapping: CY₃ ↔ BT tree |
| **Description** | Explore: (a) Euler characteristic |χ|=6 relates to branching factors (6=2×3, p=2 gives branching 3), (b) Hodge numbers ↔ tree depth structure, (c) spectral properties ↔ valuations. |
| **Effort** | 8-16 weeks |

#### Task 5.3: Theorem Statement + Proof Attempt
| Aspect | Detail |
|--------|--------|
| **Deliverable** | Bridge Theorem (proven or conjecture status documented) |
| **Description** | If a mapping is found: formalize as a theorem and attempt proof. If no mapping found: document why, classify as "GUF remains isolated Archimedean pillar." |
| **Effort** | 12-24 weeks |

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

## Dependency Graph

```
Phase 1 (Bootstrap Proof) ─────────────────────────────────────────┐
    │                                                                │
    ├──→ Phase 3 (Trapped-Ion) ──→ Phase 6 (Hardware Roadmap)       │
    │         │                                                      │
    │         └──→ Phase 3.5 (OSF Closeout)                         │
    │                                                                │
    ├──→ Phase 4 (CMB Search) ──→ Phase 4.5 (OSF Closeout)          │
    │                                                                │
    └──→ Phase 5 (GUF Bridge) ── (optional, low priority)            │
                                                                     │
Phase 2 (Taxonomy Validation) ──→ Revise framework claims            │
                                                                     │
Phase 7 (Infrastructure) ──→ Continuous ────────────────────────────┘
```

**Key:** Phase 1 is the CRITICAL PATH because:
- If Bootstrap Conjecture is proven: entire framework upgrades from "speculative" to "proven formal ontology"
- If Bootstrap Conjecture is disproven: framework reverts to "interesting formal ontology, physical relevance unconfirmed"
- Phases 3-6 are empirical tests that gain weight if Phase 1 succeeds

---

## Next Session Immediate Tasks

| Priority | Task | Ready? |
|----------|------|--------|
| 1 | Create Zenodo v1.2 with all current artifacts | ✅ Now |
| 2 | Buffer social media posts for v1.0/v1.1 release | ✅ Now |
| 3 | Begin Task 1.1: Define calibration map C | ⬜ Pending |
| 4 | Begin Task 2.1: Select external validators | ⬜ Pending |
| 5 | OSF pre-register trapped-ion protocol (Task 3.1) | ⬜ Pending |
| 6 | OSF pre-register CMB search protocol (Task 4.1 prelim) | ⬜ Pending |
| 7 | Deploy PBO v1.0 to D1 (Task 7.4) | ⬜ Pending |
