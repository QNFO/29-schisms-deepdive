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
---

## Next Session Immediate Tasks (rewritten 2026-07-21 — replaces corrupted/stale table; reflects verified-done vs. actually-pending)

**Note on this rewrite:** The prior version of this table had accumulated encoding corruption (literal `?` characters replacing emoji/em-dashes from an earlier PowerShell text-replace operation) and duplicate/conflicting row numbers (two different "7" rows). This rewrite consolidates everything into one clean, accurate register as of the v2.2 publication + Task 1.3/1.3a completion.

| Priority | Task | Status |
|----------|------|--------|
| 1 | Publish current research state to Zenodo | ✅ **DONE** — v2.2 published (DOI `10.5281/zenodo.21468103`). **v2.3 published 2026-07-21** (DOI `10.5281/zenodo.21469000`) — trajectory-local Bootstrap Conjecture adopted + T6.1 partial proof. Canonical chain: v1.2 → v2.2 → v2.3 under concept DOI `10.5281/zenodo.21460735`. |
| 2 | Buffer social media posts | ⬜ **DEFERRED BY DESIGN** — per `research` skill guidance, reserve social posts for final deliverables; framework is still conjecture-stage (Bootstrap Conjecture unproven). Revisit only after Task 6c (analytic proof) or Task 6b (conjecture reframe) settles. |
| 3 | Task 0.5.1: Zenodo version-chain discipline | ✅ **DONE** — `.zenodo_versions.json` tracks the full chain (legacy + canonical) with publish instructions for next version. |
| 4 | Task 0.5.2: Constructor Theory competitor analysis | ✅ **DONE-RTC** — `competitor-analysis-multi-framework.md`: CT resolves S19 with lighter formalism but covers only ~5/29 schisms overall. Monitored as low-risk ongoing gap (G3 in `RESEARCH-PLAN-UPDATE-GAP-CLOSURE.md`) — no CT extension found in 2025-2026 literature scan. |
| 4a | Task 0.5.3: GUF schism-by-schism table | ✅ **DONE** — verified 2.5/29 (previously misestimated ~15/29, wrong by 6x). |
| 4b | Task 0.5.4: Dependency graph correction | ✅ **DONE** — Phases 3-4 confirmed independent of Phase 1 (test ultrametric geometry, not the Bootstrap Conjecture calibration mechanism). Can run in parallel. |
| 5 | Task 1.1: Define calibration map C | ✅ **DONE-RTC** — v2.0, ancestor-based, well-defined, idempotent. Passed red-team re-audit (F-H1/F-H3/F-H4 resolved). |
| 5a | Task 1.2: Prove C is contractive | ✅ **DONE-RTC** — v2.0, 10 theorems, honest limitation: NOT globally non-expansive (Theorem 7). Passed red-team re-audit (F-C1-F-C5 resolved). |
| 5b | Task 0.5.6: Recruitment fallback in Phase 2 WBS | ✅ **DONE** |
| 5c | RED TEAM: 9 CRITICAL+HIGH findings, Tasks 1.1-1.2 | ✅ **DONE** — commit `04e4f50` |
| 6 | Task 1.3: Characterize ancestor-monotone maps on TREE | ✅ **DONE** — `ancestor-monotone-map-characterization.md`: 6 theorems (DCA Preservation, Sibling Collapse, Royden Obstruction, Depth Bound, Expansion Bound, Non-Trivial FP Obstruction T6.1). Corrected an error in `f-contractiveness-analysis.md` (see Task 14 below). Numerical search at depth≤3: 48 candidate maps with non-trivial T* found, all fail full-tree non-expansiveness. |
| 6a | Task 1.3a: Nontriviality constraint — deeper numerical verification | ✅ **DONE** (2026-07-21) — `deeper-math-bootstrap-obstruction.md` §2: real executed verification of all 48 candidates at depth 4 (15 nodes) and depth 5 (31 nodes) via `_verify_depth45.py` (ephemeral, deleted post-run per JIT protocol). Result: **0/48 pass at either depth.** Violation counts GROW with tree size (7→39, 10→46, 14→58, 17→65 across 4 structural sub-families) — the obstruction compounds rather than being a small fixable edge case. This strengthens support for T6.1 but is still numerical evidence at finite depth, not a general proof. |
| 6b | Task 1.3b: Reframe Bootstrap Conjecture (Trajectory-Local formulation) | ✅ **ADOPTED** (2026-07-21) — `trajectory-local-bootstrap-conjecture.md`: formal adoption document. Global non-expansiveness relaxed to trajectory-local non-expansiveness. Cost: Banach uniqueness lost; T* uniqueness requires separate argument. Benefit: 43 candidate maps are trajectorily-valid (provably satisfiable). `calibration-map-c-definition.md` → v2.1 (global claim withdrawn, trajectory-local theorem W2-TL added). `c-contractiveness-proof.md` → v2.1 (header updated, honest gap acknowledged). The simplest valid trajectory-local map: ∅ → [] → [] (T* = [] at depth 1). |
| 6c | Task 1.3c: Analytic proof of T6.1 (parent-collapse unavoidable at any depth) | ⬜→✅ **PARTIAL PROOF DELIVERED** (2026-07-21) — `t6-1-analytic-proof.md`. T6.1 PROVEN for the constrained class (ancestor-monotone maps with parent-map fallback): parent-collapse is structurally unavoidable for off-trajectory ancestor/descendant pairs. The gap to full T6.1 is Lemma G (whether F must be ancestor-monotone for sufficiently deep nodes under global non-expansiveness). Lemma G has a plausible proof sketch (§2.3) but is not rigorously established. The trajectory-local reframe (6b, adopted) sidesteps Lemma G entirely — global non-expansiveness is not required. Recommendation: pursue Lemma G as a standalone math contribution; project physics direction proceeds with trajectory-local formulation. |
| 7 | Task 2.1: Select external validators | ✅ **DONE-RTC** — email addresses verified (Rovelli typo fixed), coverage 10/29 individually, 21/29 collective across 5 candidates. |
| 7a | Task 2.2: Prepare taxonomy validation package | ✅ **DONE-RTC** — neutral resolution definition, thematic groups + disclaimer, S4 placement note, "literature review" (not "systematic scan") language. |
| 8 | Task 2.3: Validator outreach — send emails | ⬜ **UNBLOCKED, NOT EXECUTED.** All drafting complete: 5 emails (zero framework language, identical templates), PowerShell send script with error handling, infrastructure pre-send checklist. The paper is now published (v2.2, DOI above) which was the last drafting-side blocker. Remaining before actual send: (a) Cloudflare Email Service domain onboarding for qnfo.net (~15 min — see `research` skill's email/Zenodo credential protocol sections for the pattern), (b) **explicit user confirmation before sending** — this is unsolicited outbound contact to 5 named external researchers and should not be auto-sent without a go-ahead. |
| 8a | RED TEAM Phase 2: 13 findings | ✅ **DONE** — F-P2-1 through F-P2-13 all addressed. DoD Gate PASSED. Commit `4e290cd`. |
| 9 | OSF pre-register trapped-ion protocol (Task 3.1) | ⬜ **BLOCKED ON USER APPROVAL** — protocol complete and submission-ready. OSF registrations are permanent/immutable; requires explicit go-ahead per Bona Fide Registration Requirements, not silent execution. |
| 10 | OSF pre-register CMB search protocol (Task 4.1) | ⬜ **BLOCKED ON USER APPROVAL** — same gate as #9. |
| 11 | Deploy PBO v1.0 to D1 (Task 7.4) | ⬜ **BLOCKED, STALE STATUS** — confirmed 404 on papers.qnfo.org as of 2026-07-20; **not re-verified in this session (2026-07-21)** — re-check current status before next attempt, it may have changed independently. |
| 12 | Spin-off: Cancellation Rule research project | ⬜ **HANDOFF READY** (2026-07-21) — `HANDOFF-cancellation-rule-research-project.md`. Explicitly scoped OUT of this project — requires a new repo + new LLM session. Contains full starting prompt, 6 research questions (crossing semantics, void/substrate ontology, boundary=measurement justification, rule-set consistency/alternatives), and starting bibliography (Spencer-Brown, Kauffman, Varela, Bricken, Meguire). |
| 13 | Spin-off: S10 Observer Inside/Outside research project | ⬜ **HANDOFF READY** (2026-07-21) — `HANDOFF-s10-observer-inside-outside-research-project.md`. Explicitly scoped OUT of this project — requires a new repo + new LLM session. **Central open question (RQ1):** does computing DIST(observer_node, observed_node) itself require an external, non-node vantage point — circularly reintroducing the "view from nowhere" the framework claims to eliminate? paper.md §5.5 calls S10 the framework's "defining move" but gives it only a one-paragraph treatment; this spin-off exists to rigorously test whether that move actually works. If RQ1 resolves unfavorably, report back to 29-schisms-deepdive as a HIGH-severity finding against the paper's central claim — but do the investigation in the new project. |
| 14 | Correct known-false claim in `f-contractiveness-analysis.md` | ✅ **DONE** (2026-07-21) — erratum already applied in that document's Corollary 1. Original false claim ("parent function is ALWAYS contractive") struck through, corrected statement added with explicit counterexample and propagation note. The error was discovered during Task 1.3 (2026-07-21) — a reminder that plausible one-line depth arguments are not substitutes for pairwise distance checks. |
| 15 | Verify PBO/papers.qnfo.org status is current | ⬜ Same as #11 — grouped here as a reminder that infrastructure status claims from 2026-07-20 were not re-checked this session and may be stale. |
| 16 | Task 1.4: Valuation Structure Characterization | ✅→⬜ **PRELIMINARY CHARACTERIZATION COMPLETE** (2026-07-21) — `valuation-structure-characterization.md`. Key findings: (a) branching factors are tree-intrinsic (determined by rewrite rules C/X/D), NOT map-dependent; (b) all 36 valid ancestor-monotone T* are at depth 1, split into terminal `#` (dead universe) and container `[]` (rich universe, asymptotic branching ~4.7); (c) to reach T* at depth ≥ 2, need C* extension with depth-expanding non-ancestor-monotone steps — the next computational task (Task 1.4a). Asymptotic ratio ~4.7 confirmed universal; early-level [1,2,2,3,7] sequence match still open. |
| **17** | **Task 1.4a (RECOMMENDED NEXT): C* Extension — Reach T* at Depth ≥ 2** | ⬜ **ACTIONABLE, BLOCKED BY NOTHING** — Extend the C* construction to use depth-expanding trajectory steps (non-ancestor-monotone: F(∅)=●, F(●)=[●], F([●])=[●]) and avoid the cancellation-rule trap by routing through `[]` instead of `#`. Goal: characterize which depth-≥2 T* are reachable, then compute subtree branching for each candidate. Compare against executable tree early-universe prefix [1,2,2,3,7]. **Effort: 2-3 days** (modify `_self_descriptive_system.py` to allow depth-expanding trajectories, enumerate candidates up to depth 3-4, compute T* subtree growth). |
| 18 | Task 1.4b: Deep Subtree Comparison — Match to Executable Tree | ⬜ **DEPENDS ON 1.4a** — For each C*-reachable T* at depth ≥ 2, compute the subtree growth sequence and compare to the executable tree early-universe pattern [1,2,2,3,7,28,125,588]. Determine whether any T* subtree reproduces the first 4-5 terms. If multiple candidates match, select the one with the deepest calibration (highest T* depth). |
| 19 | Task 1.5: Extended Numerical Verification Suite | ⬜ **DEPENDS ON 1.4a** — Extend `_self_descriptive_system.py` to build the tree to depth 7-8. Verify trajectory-local non-expansiveness for all C*-extended candidates. Characterize the violation count growth curve as a function of depth. If T6.1 is proven for constrained class, this becomes a robustness check rather than a search for counterexamples. Effort: 1-2 weeks compute. |
| 20 | Task 2.1-2.4: External Validation of 29-Schism Taxonomy | ⬜ **UNBLOCKED, NOT EXECUTED** — Validators selected (5 researchers), emails drafted, taxonomy package ready. Blocked only on Cloudflare Email Service domain onboarding (~15 min) + user go-ahead for unsolicited outbound contact. Effort: 1-3 months calendar (waiting for responses), <1 week active work. |
| 21 | Task 3.1-3.5: Trapped-Ion Page-Wootters Experiment | ⬜ **UNBLOCKED, REQUIRES LAB ACCESS** — Full protocol documented in `trapped-ion-ultrametricity-experiment-protocol.md`. Phase 3 WBS complete. Estimated $50K lab time, 3-6 months. Tests the Sufficient Condition Theorem experimentally. |
| 22 | Task 4.1-4.4: CMB Log-Periodic Oscillation Search | ⬜ **UNBLOCKED, COMPUTATIONAL ONLY** — Pipeline design documented, null simulation protocol ready. No lab access needed — public data (Planck, ACT, SPT). Effort: 1-3 months compute. Tests discrete scale invariance via Syntactic Token Calculus. |

### Recommended Next Tasks (Priority Order)

**#1 — Task 1.4a (C* Extension, 2-3 days, unblocked):** Extend trajectory construction to reach T* at depth ≥ 2. This is the next computational task — modify `_self_descriptive_system.py` to allow depth-expanding steps, enumerate candidates up to depth 3-4, compute T* subtree growth. This directly addresses the open question: can any calibration map produce the executable tree's early-universe prefix [1,2,2,3,7]?

**#2 — Task 1.4b (Subtree Comparison, 1 week, depends on 1.4a):** Match C*-extended T* candidates against the executable tree sequence.

**#3 — Task 2.1-2.4 (External Validation, 1-3 months calendar, unblocked):** Send validator emails once Cloudflare Email Service domain is onboarded.

**Genuinely open (longer-term):**
- **#6c (Lemma G)** — Full T6.1 for arbitrary maps. Trajectory-local reframe sidesteps; pursue as standalone math contribution.
- **#8 — Validator emails** — Drafted, needs domain setup + user go-ahead.
- **#9/#10 — OSF pre-registration** — Blocked on user approval.
- **#11 — PBO/D1 deployment** — Infrastructure status stale.
- **#12/#13 — Spin-off projects** — Handoff documents ready; require separate sessions/repos.
- **#21/#22 — Experiments (Trapped-Ion, CMB)** — Protocol-ready; requires lab access (trapped-ion) or compute time (CMB).
