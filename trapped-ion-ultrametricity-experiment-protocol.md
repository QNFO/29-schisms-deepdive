# Trapped-Ion Page-Wootters Experiment: Protocol for Testing Ultrametricity

**Document Type:** Experimental Protocol (Pre-Registration Draft)
**Date:** 2026-07-20
**Status:** Draft — awaiting OSF pre-registration
**Based on:** QNFO trapped-ions-ultrametric paper (2026-07-01) + Sufficient Condition Theorem

---

## 0. Executive Summary

**Question:** Does diagonal clock-rest coupling produce exact ultrametric conditional state overlaps (UVR = 0%), while nondiagonal coupling produces a universal ~32% violation rate?

**System:** Single trapped Yb⁺ ion with N=4 Zeeman sublevels as "clock" and M motional Fock states as "rest."

**Prediction:** The Sufficient Condition Theorem predicts that when the clock-rest Hamiltonian H_CR is strictly diagonal in the clock eigenbasis, the overlap matrix of conditional rest states is exactly ultrametric (UVR = 0%). For nondiagonal coupling, the violation rate is predicted to be approximately 32%.

**Success Criterion (positive result):** UVR < 5% for diagonal coupling with >99% confidence, and UVR > 20% for nondiagonal coupling.

**Falsification (negative result):** UVR ≈ 32% for BOTH diagonal and nondiagonal coupling. This would disconfirm the Sufficient Condition Theorem and the D=4 Ultrametric Special Case Theorem.

**Required Resources:** Standard trapped-ion apparatus (no new hardware). Estimated time: 2-4 weeks of beam time.

---

## 1. Physical System

### 1.1 Ion Choice

| Property | Yb⁺ (¹⁷¹Yb⁺) | Rationale |
|----------|--------------|-----------|
| Clock states | ²S₁/₂ |F=0, m_F⟩ hyperfine ground | Long coherence, well-characterized |
| Zeeman sublevels | N=4 (m_F = -3/2, -1/2, +1/2, +3/2) | Provides 4-level clock for Page-Wootters construction |
| Motional mode | Axial center-of-mass | ω_z/2π ≈ 1-2 MHz, well-controlled |
| Laser access | 369.5 nm cooling, 435.5 nm repump | Standard Yb⁺ infrastructure |
| Coherence time | T₂ ≈ seconds for hyperfine qubit | Sufficient for tomographic reconstruction |

### 1.2 Hamiltonian

The total Hamiltonian in the lab frame:

$$\hat{H} = \hat{H}_C \otimes \hat{I}_R + \hat{I}_C \otimes \hat{H}_R + \hat{H}_{CR}$$

where:

- **Clock:** $\hat{H}_C = \sum_{k=0}^{N-1} E_k |e_k\rangle\langle e_k|$
  - $|e_k\rangle$ are the N=4 Zeeman sublevels
  - $E_k = g_J \mu_B B m_F^{(k)}$ with B ≈ 5 G giving splitting ~1-10 MHz

- **Rest:** $\hat{H}_R = \hbar\omega_z \hat{a}^\dagger\hat{a}$
  - $\hat{a}^\dagger, \hat{a}$: motional creation/annihilation operators
  - M initial Fock states: |0⟩, |1⟩, ..., |M-1⟩ (M ≥ 4 for statistics)

- **Coupling (laser-ion interaction):**
  $$\hat{H}_{CR} = \sum_{k,l} \Omega_{kl} |e_k\rangle\langle e_l| \otimes \hat{V}_{kl} + \text{h.c.}$$

### 1.3 Two Regimes (Key Tunability)

The experiment's central advantage: switching between regimes by changing laser frequency in the SAME apparatus.

#### Regime A: Diagonal Coupling (Predicted UVR = 0%)

- **Laser configuration:** Carrier transitions only
- **Operators:** $\hat{V}_{kk} = \hat{I}_R$ (motional state unchanged)
- **Effect:** Clock state transfers without changing motional Fock state
- **Experimental verification:** Measure motional state before/after clock transfer — must be unchanged

#### Regime B: Nondiagonal Coupling (Predicted UVR ≈ 32%)

- **Laser configuration:** First-order red/blue sidebands
- **Operators:** $\hat{V}_{kl} = \eta(\hat{a} + \hat{a}^\dagger)$ (motional state changes)
- **Effect:** $|e_k\rangle|n\rangle \leftrightarrow |e_l\rangle|n\pm 1\rangle$
- **Experimental verification:** Motional state changes with clock transfer

---

## 2. State Preparation

### 2.1 Initial State

Prepare the ion in a product state:

$$|\Psi_0\rangle = |\psi_C\rangle \otimes |\psi_R\rangle$$

where:
- $|\psi_C\rangle = \frac{1}{\sqrt{N}}\sum_{k=0}^{N-1} |e_k\rangle$ — equal superposition of clock states
- $|\psi_R\rangle = |0\rangle$ — ground state of axial motion

### 2.2 Preparation Protocol (Step-by-Step)

| Step | Operation | Duration | Verification |
|------|-----------|----------|-------------|
| 1 | Doppler cooling | ~1 ms | Temperature < 1 mK |
| 2 | Sideband cooling to |n=0⟩ | ~1 ms per sideband | Fock state fidelity > 95% |
| 3 | Optical pumping to |F=0⟩ manifold | ~100 μs | Population > 99% |
| 4 | Microwave π/2 pulse | ~10 μs | Equal superposition of Zeeman sublevels |
| 5 | Verify initial state via tomography | ~1 ms per setting | Fidelity > 90% |

### 2.3 Page-Wootters Evolution

Apply $\hat{H} = \hat{H}_C + \hat{H}_R + \hat{H}_{CR}$ for a fixed evolution time τ:

$$|\Psi(\tau)\rangle = e^{-i\hat{H}\tau/\hbar} |\Psi_0\rangle$$

**Evolution time selection:** τ should be long enough to produce measurable entanglement between clock and rest, but short enough to avoid decoherence:
- Estimate: τ ≈ 10-100 μs (several Rabi periods)
- Optimal τ determined by maximizing the spread of conditional rest state overlaps

---

## 3. Measurement Protocol

### 3.1 Conditional State Tomography

**Goal:** For each clock reading k ∈ {0, 1, 2, 3}, reconstruct the conditional rest state ρ_R^{(k)}.

**Method:** Projective measurement of clock state, followed by full motional state tomography.

| Step | Operation |
|------|-----------|
| 1 | Project clock onto |e_k⟩ (microwave π-pulse + fluorescence detection) |
| 2 | If clock = k: reconstruct ρ_R^{(k)} via motional state tomography |
| 3 | Repeat steps 1-2 for each k (N=4 clock readings) |
| 4 | Repeat full cycle R times for statistics (R ≥ 1000 per clock reading) |

### 3.2 Motional State Tomography

For each post-selected clock reading k:

1. **Population measurement:** Apply displacement operator D(α), measure |n⟩ distribution
2. **Phase measurement:** Ramsey interferometry on motional states
3. **Full reconstruction:** Maximum-likelihood estimation of ρ_R^{(k)}

**Required precision:** Fidelity > 95% for each conditional state.

### 3.3 Overlap Matrix Computation

From the reconstructed conditional states, compute the overlap matrix O:

$$O_{ij} = \mathcal{F}(\rho_R^{(i)}, \rho_R^{(j)})$$

where $\mathcal{F}$ is the quantum fidelity:

$$\mathcal{F}(\rho, \sigma) = \left(\text{Tr}\sqrt{\sqrt{\rho}\sigma\sqrt{\rho}}\right)^2$$

For pure states: $\mathcal{F}(|\psi_i\rangle, |\psi_j\rangle) = |\langle\psi_i|\psi_j\rangle|^2$

### 3.4 Ultrametricity Violation Rate (UVR)

The Parisi overlap matrix (POM) method:

1. Build matrix D where $D_{ij} = -\ln(O_{ij})$ (or $1 - O_{ij}$ for pure states)
2. Compute the triple condition: For every triple (i,j,k), check whether:
   $$D_{ij} \geq \min(D_{ik}, D_{jk})$$
3. Count violations:
   $$\text{UVR} = \frac{\#\{\text{triples violating ultrametric condition}\}}{\#\{\text{all triples}\}}$$

For N=4 clock readings: $\binom{4}{3} = 4$ triples.

---

## 4. Predicted Outcomes

### 4.1 Diagonal Coupling (Regime A)

| Quantity | Predicted Value | Statistical Uncertainty |
|----------|----------------|------------------------|
| UVR | 0% | ±1.5% (limited by N=4 clock states) |
| Overlap matrix rank | 1 (all conditional states equal up to phase) | — |
| D_{ij} matrix | All entries equal | ±tomography noise |

**Physical interpretation:** When H_CR is diagonal, the evolution entangles clock and rest in a specific way: the conditional rest states are identical up to a phase. The clock simply "ticks" without distinguishing the rest system's state.

### 4.2 Nondiagonal Coupling (Regime B)

| Quantity | Predicted Value | Statistical Uncertainty |
|----------|----------------|------------------------|
| UVR | ~32% (theoretical) | ±5% |
| Overlap matrix structure | Hierarchical (some pairs more similar than others) | — |
| D_{ij} matrix | Non-uniform, ultrametric violations present | — |

**Physical interpretation:** Nondiagonal H_CR creates genuine distinctions between conditional rest states. Some clock readings correspond to "closer" rest states than others. The ~32% violation rate is a universal prediction of the Sufficient Condition Theorem for non-diagonal coupling.

### 4.3 Success/Failure Criteria

| Outcome | Interpretation |
|---------|---------------|
| UVR_diag < 5% AND UVR_nondiag > 20% (with >99% confidence) | **PREDICTION CONFIRMED.** Strong evidence for ultrametric conditional state structure. Supports D=4 Ultrametric Special Case Theorem. |
| UVR_diag < 5% AND UVR_nondiag ≈ 32% (within errors) | **PREDICTION CONFIRMED with universal constant.** This would be the strongest possible result — confirming both the qualitative prediction AND the quantitative 32% value. |
| UVR_diag > 10% | **PREDICTION PARTIALLY DISCONFIRMED.** Diagonal coupling does not produce exact ultrametricity. Sufficient Condition Theorem needs refinement. |
| UVR_diag ≈ UVR_nondiag ≈ 32% | **PREDICTION DISCONFIRMED.** No difference between diagonal and nondiagonal coupling. Sufficient Condition Theorem and D=4 Special Case Theorem are both falsified. |
| Any UVR value that is not theoretically predicted | **NEW PHYSICS.** The ultrametricity prediction was wrong, but the experiment reveals a different pattern. |

---

## 5. Error Analysis

### 5.1 Systematic Errors

| Source | Effect on UVR | Mitigation |
|--------|--------------|------------|
| Imperfect state preparation | UVR appears lower (mixed states wash out structure) | Verify preparation fidelity > 90% |
| Decoherence during evolution | UVR appears lower | Choose τ ≪ T₂ |
| Motional heating | UVR appears higher (random motional excitations) | Cryogenic trap, < 1 phonon/s heating rate |
| Magnetic field drift | Clock energy shifts → apparent nondiagonal coupling | Active B-field stabilization to < 1 μG |
| Detection inefficiency | Tomographic reconstruction bias | MLE with known detection efficiency |

### 5.2 Statistical Errors

- **UVR uncertainty:** Binomial error from triple counting. For N=4 and R=1000 per clock reading, expected statistical error ≈ ±3%.
- **Required R for >99% confidence:**
  - If true UVR = 0%: need at least 7 consecutive zero-violation runs (P = (1-e)^7 < 0.01 for e < 0.48)
  - If true UVR = 32%: need √(0.32 × 0.68 / R_triples) < 0.05 → R_triples > 87 → R ≥ 300 per clock reading

Conservative choice: R = 2000 per clock reading, giving statistical uncertainty < ±2% on UVR.

### 5.3 Total Measurement Time Estimate

| Component | Time per iteration | Iterations | Total |
|-----------|-------------------|------------|-------|
| State preparation (cooling + pumping) | 3 ms | 8000 | 24 s |
| Evolution τ | 50 μs | 8000 | 0.4 s |
| Clock readout | 500 μs | 8000 | 4 s |
| Motional tomography (per clock outcome) | 5 ms | 4 × 2000 | 40 s |
| **Total active measurement** | | | **~70 s** |
| **With overhead (cooling cycles, recalibration)** | ×5 | | **~6 minutes** |

**Beam time estimate:** 2 days for full data collection with recalibration between runs, plus 2 days for systematic error characterization. **Total: 4 days of beam time.**

---

## 6. Experimental Checklist

### Pre-Experiment

- [ ] Ion loaded and laser-cooled to Doppler limit
- [ ] Sideband cooling to |n=0⟩ with >95% fidelity
- [ ] Zeeman sublevels resolved (B-field > 2 G)
- [ ] Carrier Rabi frequency calibrated (Ω/2π ≈ 50 kHz)
- [ ] Sideband Rabi frequency calibrated (ηΩ/2π ≈ 5 kHz)
- [ ] T₂ measured for each clock transition (> 1 ms minimum)
- [ ] Motional heating rate measured (< 5 quanta/s)
- [ ] Detection efficiency calibrated (> 98% per shot)

### Data Collection

- [ ] Regime A (diagonal): 2000 cycles × 4 clock readings
- [ ] Regime B (nondiagonal): 2000 cycles × 4 clock readings
- [ ] Systematic error runs:
  - [ ] Repeated with different τ (50 μs, 100 μs, 200 μs)
  - [ ] Repeated with different initial states
  - [ ] Repeated with different B-field values (different clock splittings)
  - [ ] Repeated on different days (assess long-term stability)

### Post-Experiment Analysis

- [ ] Reconstruct ρ_R^{(k)} for all k, both regimes
- [ ] Compute overlap matrix O_{ij}
- [ ] Compute D_{ij} = -ln(O_{ij})
- [ ] Count ultrametricity violation triples
- [ ] Compute UVR with statistical uncertainty
- [ ] Compare Regime A vs Regime B UVR
- [ ] Quantify significance of difference (p-value, Bayes factor)
- [ ] Publish results regardless of outcome

---

## 7. OSF Pre-Registration Template

### Hypothesis

Diagonal clock-rest coupling in a trapped-ion Page-Wootters experiment produces exact ultrametric conditional state overlaps (UVR = 0% ± statistical bound), while nondiagonal coupling produces non-ultrametric overlaps (UVR ≈ 32%).

### Design Plan

- **Study type:** Experiment
- **Blinding:** None (single ion, no allocation concealment needed)
- **Study design:** Within-subject (same ion, two coupling regimes)
- **Randomization:** Not applicable (deterministic quantum evolution)

### Sampling Plan

- **Existing data:** None — all data collected for this experiment
- **Data collection procedure:** See §3 above
- **Sample size:** R = 2000 per clock reading per regime (total 4 × 2000 × 2 = 16,000 cycles)
- **Sample size rationale:** Statistical uncertainty < ±2% on UVR
- **Stopping rule:** Collect all planned data unless apparatus failure prevents completion

### Variables

- **Independent variable:** Coupling regime (diagonal vs. nondiagonal)
- **Dependent variable:** Ultrametricity violation rate (UVR)
- **Measured variables:** Conditional rest state density matrices ρ_R^{(k)}, overlap matrix O_{ij}
- **Control variables:** Evolution time τ, initial state |Ψ₀⟩, B-field, motional heating rate, detection efficiency

### Analysis Plan

- **Statistical model:** Binomial test on triple violation counts
- **Primary analysis:** Compare UVR_diag to UVR_nondiag; test null hypothesis UVR_diag = UVR_nondiag
- **Exploratory analysis:** Dependence of UVR on τ, initial state, B-field
- **Inference criteria:** Bayes factor > 100 for difference between regimes, or frequentist p < 0.001
- **Data exclusion:** Cycles with detection efficiency < 95% (apparatus failure)
- **Missing data:** Excluded cycles documented; if >5% excluded, report separately
- **Multiple comparisons:** Only one primary comparison; no correction needed

### Other

- **Funding:** Standard trapped-ion lab infrastructure (no additional funding required)
- **Conflicts of interest:** QNFO Research developed the theoretical prediction being tested
- **Data availability:** Raw data + analysis code to be published on Zenodo
- **Pre-registration date:** [TBD — submit before first data collection]

---

## 8. References

1. Quni-Gudzinas, R.B. "Conditional State Distances in Page-Wootters Quantum Clocks: When Does Ultrametricity Emerge?" QNFO, 2026.
2. QNFO Research. "Trapped-Ion Page-Wootters Experiment: Protocol for Testing Ultrametricity." QNFO, 2026-07-01.
3. Parisi, G. "A sequence of approximated solutions to the S-K model for spin glasses." J. Phys. A, 1980.
4. Page, D.N. and Wootters, W.K. "Evolution without evolution: Dynamics described by stationary observables." Phys. Rev. D, 1983.
5. Ostrowski, A. "Über einige Lösungen der Funktionalgleichung φ(x)·φ(y) = φ(xy)." Acta Math., 1916.

---

*Protocol designed for OSF pre-registration. Submit before first data collection to register the hypothesis, design, sampling plan, and analysis plan as a permanent, timestamped record.*
