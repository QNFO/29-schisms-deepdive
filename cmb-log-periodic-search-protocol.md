# CMB Log-Periodic Oscillation Search: Data Analysis Protocol

**Document Type:** Experimental Protocol (Pre-Registration Draft)
**Date:** 2026-07-20
**Status:** Draft — awaiting OSF pre-registration
**Based on:** QNFO log-periodic-oscillations-in-the-cmb paper (2026-04-13)

---

## 0. Executive Summary

**Question:** Does the CMB angular power spectrum C_l exhibit log-periodic oscillations consistent with discrete scale invariance predicted by the Syntactic Token Calculus (STC)?

**Prediction:** The STC predicts that the primordial power spectrum — and therefore C_l — is modulated by log-periodic oscillations of the form:

```
l(l+1)C_l = A (l/l_0)^(1-n_s) [1 + B cos(2pi/ln(q) * ln(l/l_0) + phi)]
```

where q is the fundamental scaling ratio, B is oscillation amplitude, and phi is phase.

**Data:** Publicly available Planck 2018, ACT DR6, and SPT-3G legacy data.

**Success Criterion:** A statistically significant (>3 sigma) peak in the log-periodogram that is NOT explained by Lambda-CDM foreground residuals.

**Falsification:** No statistically significant log-periodic oscillations down to the cosmic variance limit at l > 2000.

**Required Resources:** Existing CMB data (no new observations needed). Computational analysis only.

---

## 1. Theoretical Motivation

### 1.1 Discrete Scale Invariance

Standard cosmology assumes continuous scale invariance. The STC posits that the underlying structure of spacetime is a Bruhat-Tits tree — a discrete, hierarchical structure exhibiting DISCRETE scale invariance: invariance under scaling by factors of q (the branching ratio of the tree), not arbitrary continuous factors.

### 1.2 Predicted Signature

Discrete scale invariance manifests as log-periodic modulation of power spectra:

```
P(k) = P_0(k) * [1 + A cos(omega * ln(k) + phi)]
```

where omega = 2pi/ln(q) is the log-frequency.

For the CMB, the angular power spectrum C_l maps angular scale to multipole moment. The predicted modulation in l-space is:

```
D_l = l(l+1)C_l/(2pi) = D_l^LCDM * [1 + B cos(omega * ln(l/l_0) + phi)]
```

### 1.3 Physical Origin of the Scaling Ratio q

The scaling ratio q is the branching factor of the cosmic Bruhat-Tits tree. Candidate values:
- q = e (2.718...) — from continuous limit of discrete scaling
- q = pi (3.141...) — from geometric constraints
- q = a prime p — from the adelic framework
- q free — treated as a parameter to be fit from data

**Conservative approach:** Treat q as a free parameter and search for ANY statistically significant log-periodic signal. This avoids theory-dependence.

---

## 2. Data Sources

### 2.1 Primary Datasets

| Dataset | l_max | Resolution | Status | Access |
|---------|-------|-----------|--------|--------|
| Planck 2018 (PR3) | 2500 | 5 arcmin | Published, final | PLA legacy archive |
| ACT DR6 | 4000 | 1.4 arcmin | Published | LAMBDA |
| SPT-3G | 3000 | 1 arcmin | Published | SPT website |
| Planck + ACT + SPT combined | 4000 | Combined | Requires joint likelihood | Custom pipeline |

### 2.2 Future Datasets

| Dataset | Expected l_max | Timeline |
|---------|---------------|----------|
| Simons Observatory | 5000 | 2028 |
| CMB-S4 | 5000+ | 2035 |
| LiteBIRD | 2000 (polarization) | 2032 |

**Priority:** Analyze Planck + ACT DR6 first (data available NOW). Follow up with Simons Observatory and CMB-S4 when available.

---

## 3. Analysis Pipeline

### 3.1 Data Preprocessing

**Step 1: Obtain cleaned C_l spectra**
- Download Planck 2018 plik_lite C_l (TT, TE, EE)
- Download ACT DR6 C_l
- Download SPT-3G bandpowers
- Apply best-fit foreground model (Planck 2018 cosmology)

**Step 2: Combine datasets**
- In overlapping l range: inverse-variance weighted average
- In non-overlapping range: use the dataset with highest l_max
- Ensure consistent calibration (cross-check at l=1000-1500 where all datasets overlap)

**Step 3: Subtract best-fit Lambda-CDM**
- Fit standard 6-parameter Lambda-CDM model to the combined C_l
- Compute residuals: Delta D_l = D_l^data - D_l^LCDM_bestfit
- This removes the dominant cosmological signal, isolating any oscillatory component

### 3.2 Log-Resampling (Step 1 of STC Protocol)

```
x_i = ln(l_i)
y_i = Delta D_l(l_i) / sigma_l(l_i)
```

where sigma_l is the measurement uncertainty at each l.

**Interpolation:** If C_l is not uniformly sampled in l, interpolate C_l onto a grid uniformly spaced in x = ln(l). Use cubic spline interpolation. Grid: 100 points from ln(30) to ln(4000), i.e., l from 30 to 4000.

**Weighting:** y_i is the residual in units of sigma. This ensures that the periodogram is "noise-whitened" — under the null hypothesis (no oscillations), the periodogram should be flat.

### 3.3 Periodogram Analysis (Step 2 of STC Protocol)

**Method A: Lomb-Scargle Periodogram**
- Applied to the irregularly-sampled, noise-weighted residuals y_i
- Suitable for gapped data (e.g., around l where foreground subtraction is unreliable)
- Frequency range: omega from 0.1 to 10 (covers q from exp(2pi/0.1) ~ 10^27 to exp(2pi/10) ~ 1.9)

**Method B: Standard FFT (after log-resampling)**
- Applied to the uniformly-sampled, interpolated residuals
- Faster than Lomb-Scargle
- Requires careful handling of interpolation errors

**Method C: Wavelet Analysis**
- Morlet wavelet: provides time-frequency localization
- Useful for detecting oscillations that vary in frequency with l
- Complementary to periodogram methods

**Use ALL THREE methods** and require consistency: a genuine signal should appear in all three.

### 3.4 Peak Detection and Significance (Step 3 of STC Protocol)

**Null hypothesis:** The residuals are consistent with Gaussian noise with variance given by the Lambda-CDM cosmic variance + measurement noise.

**Significance estimation:**
1. Generate N = 10,000 Lambda-CDM realizations (Gaussian C_l with Planck 2018 best-fit cosmology)
2. Apply the SAME pipeline (subtract best-fit Lambda-CDM, log-resample, compute periodogram)
3. Build the null distribution of periodogram power at each frequency
4. Compute the "local" p-value: fraction of null realizations with power >= observed power at that frequency
5. Compute the "global" p-value (accounting for the look-elsewhere effect): fraction of null realizations whose MAXIMUM periodogram power over the search range exceeds the observed maximum

**Detection criterion:** Global p-value < 0.003 (approximately 3 sigma).

### 3.5 Parameter Estimation (if detection)

If a statistically significant peak is detected:

1. **Frequency (omega):** Periodogram peak location → q = exp(2pi/omega)
2. **Amplitude (B):** Fit D_l model with MCMC, marginalize over LCDM parameters
3. **Phase (phi):** From the complex phase of the periodogram at peak frequency
4. **Best-fit l_0:** From MCMC

**Model comparison:** Compute Bayes factor between Lambda-CDM and Lambda-CDM + log-periodic modulation using nested sampling (e.g., MultiNest).

---

## 4. Statistical Challenges and Mitigations

### 4.1 Cosmic Variance at Low l

At l < 100, cosmic variance dominates (only 2l+1 independent modes). The noise-whitening procedure (y_i = residual / sigma) naturally downweights low-l points.

### 4.2 Foreground Residuals

At high l (> 2000), foreground residuals (dust, SZ, point sources) may mimic oscillations.

**Mitigation:**
- Use the Planck 2018 foreground model as baseline
- Vary foreground parameters within their uncertainties → assess sensitivity
- Cross-check with ACT DR6 (different foreground environment)
- If detected: verify the oscillation frequency is consistent across different foreground models

### 4.3 Look-Elsewhere Effect

We search for a peak at ANY frequency. The effective number of independent frequencies in the periodogram is approximately the number of data points in the log-resampled spectrum (~100). The global p-value accounts for this.

### 4.4 Pipeline-Induced Artifacts

Log-resampling and interpolation can introduce spurious oscillations.

**Mitigation:**
- Test pipeline on Lambda-CDM simulations with NO injected signal → verify null distribution is correct
- Test pipeline on Lambda-CDM + injected log-periodic signal of known omega, B → verify recovery
- Vary the number of interpolation points to assess sensitivity

---

## 5. Experimental Results Matrix

| Outcome | Lambda-CDM + Oscillation Global p-value | Bayes Factor | Interpretation |
|---------|---------------------------------------|--------------|----------------|
| Outcome A | < 0.001 | ln(B) > 5 | **STRONG DETECTION.** Log-periodic oscillations confirmed. STC prediction validated. |
| Outcome B | 0.001 — 0.01 | ln(B) 2.5 — 5 | **MODERATE EVIDENCE.** Interesting but not conclusive. Follow up with Simons Observatory. |
| Outcome C | 0.01 — 0.05 | ln(B) 1 — 2.5 | **WEAK EVIDENCE.** Consistent with null. More data needed. |
| Outcome D | > 0.05 | ln(B) < 1 | **NULL RESULT.** Lambda-CDM preferred. |
| Outcome E | > 0.1 at all frequencies up to l_max=4000 | ln(B) < -2 favoring LCDM | **STRONG NULL.** Oscillations excluded at current sensitivity. |
| Outcome F | Significant oscillation found but at wrong frequency | — | **UNEXPECTED SIGNAL.** Not predicted by STC. Would require theory revision. |

---

## 6. Required Computational Resources

| Component | Time | Hardware |
|-----------|------|----------|
| Data download | 1 hour | Standard internet |
| Lambda-CDM fit | 1 hour | Laptop (4 cores) |
| Pipeline development | 2 days | Laptop |
| 10,000 null simulations | 24 hours | 64-core cluster (or 1 week on laptop) |
| MCMC parameter estimation | 48 hours | 64-core cluster |
| **Total** | **~1 week** | **Standard computing cluster** |

---

## 7. Pre-Registration Checklist

### Analysis Plan (to be registered before accessing data)

- [ ] Data sources specified (Planck 2018, ACT DR6, SPT-3G)
- [ ] Foreground model specified (Planck 2018 baseline, with variation tests)
- [ ] log-resampling method specified (100 points, ln(30) to ln(4000))
- [ ] Periodogram methods specified (Lomb-Scargle, FFT, wavelet — all three)
- [ ] Significance threshold specified (global p < 0.003)
- [ ] Pipeline validated on null simulations
- [ ] Pipeline validated on injected-signal simulations
- [ ] Systematic error tests enumerated (foreground variation, l_max cutoff, interpolation grid)
- [ ] Success/failure criteria defined (Outcome A-F matrix above)

### Data Access

- [ ] Planck 2018 data: Public. No special access required.
- [ ] ACT DR6: Public via LAMBDA. 
- [ ] SPT-3G: Public via SPT website.

---

## 8. Relationship to Other Experiments

### 8.1 Complementarity with Trapped-Ion Experiment

| Aspect | CMB Search | Trapped-Ion Experiment |
|--------|-----------|----------------------|
| Scale | Cosmological (Gpc) | Tabletop (mm) |
| Physics tested | Discrete spacetime at largest scales | Ultrametric quantum dynamics at smallest scales |
| Cost | Computational only | Standard ion trap (~4 days beam time) |
| Timeline | Data available NOW | Requires lab access |
| Smoking-gun signal | Log-periodic oscillations in C_l | UVR < 5% for diagonal coupling |
| If both positive | Strong cross-scale confirmation of ultrametric framework |
| If CMB only positive | Suggests ultrametric structure at cosmic scales, not quantum |
| If trapped-ion only positive | Suggests ultrametric structure at quantum scales, not cosmic |

### 8.2 Existing OSF Registration

A CMB higher n-point p-adic signature search is already OSF-registered (2026-07-20, registration in progress). This protocol should be cross-linked with that registration.

---

## 9. References

1. QNFO Research. "Log-Periodic Oscillations in the CMB." QNFO, 2026-04-13.
2. Planck Collaboration. "Planck 2018 results. VI. Cosmological parameters." A&A, 2020.
3. ACT Collaboration. "The Atacama Cosmology Telescope: DR6." 2024.
4. SPT-3G Collaboration. "SPT-3G CMB power spectrum results." 2023.
5. Lomb, N.R. "Least-squares frequency analysis of unequally spaced data." Ap&SS, 1976.
6. Scargle, J.D. "Studies in astronomical time series analysis. II." ApJ, 1982.
7. Sornette, D. "Discrete-scale invariance and complex dimensions." Physics Reports, 1998.
