# DEEP-DIVE RESEARCH & LITERATURE SEARCH: 29-Schisms Framework
## What Else? What's Next? Applications, Gaps, Falsifiability

**Date:** 2026-07-20
**Scope:** QNFO corpus (~130 papers) + KG (3,242 nodes) + Semantic Scholar + arXiv + durable memories
**Status:** Comprehensive research scan — 6 sub-questions addressed

---

## 0. EXECUTIVE SUMMARY

The 29-schisms needle-threading framework (v1.1, DOI: 10.5281/zenodo.21465629) operates at the intersection of 5 active QNFO research programs with practical applications spanning quantum computing, cosmology, AI, and number theory. Key findings from this comprehensive scan:

- **External uniqueness confirmed:** No external work catalogs all 29 schisms or proposes self-referential calibration as a unifying meta-framework. The closest competing frameworks (QBism, CDT, Wolfram) each address subsets but lack the full 5-layer structure.
- **Practical applications exist across 6 domains:** Quantum error correction (intrinsic protection via Ostrowski's theorem), trapped-ion experiments (testable with existing hardware), CMB cosmology (log-periodic oscillation search), AI/ML (Bruhat-Tits tree hierarchical clustering), error-correcting code classification (number-theoretic), and optimization (prime numbers as primitives).
- **11 gaps identified:** 5 technical (Bootstrap proof, which primes, Einstein bridge, connectedness, adelic disconfirming), 3 infrastructure (D1/KG), 3 hardware (no physical ultrametric circuit built, CMB not yet searched, ZBW protocols not on hardware).
- **10 falsification/counterfactual conditions mapped:** 5 existing from the falsifiability register + 5 newly identified through this scan.

---

## 1. WHAT ELSE? — External Literature Landscape

### 1.1 Directly Overlapping External Work

| Framework | What It Does | Schisms Addressed | Relationship to Needle-Threading |
|-----------|-------------|-------------------|----------------------------------|
| **p-Adic Quantum Mechanics** (Dragovich 2003, Vladimirov, Volovich) | Formulates QM over $\mathbb{Q}_p$ instead of $\mathbb{R}$. Wavefunctions are complex-valued functions on $\mathbb{Q}_p$. | S1, S14, S6 | **Precursor.** Dragovich independently arrived at p-adic QM for different reasons (UV regularization, not self-reference). QNFO extends this into the adelic framework. Dragovich's work is cited in the 29-schism paper. |
| **QBism** (Fuchs 2010-2023) | Quantum states are an agent's degrees of belief. No "objective state." Measurement = updating belief. | S10, S25, S21, S27 | **Lighter-weight alternative.** Resolves 4 observer schisms with ONE conceptual move (the agent is primary). The needle-threading framework resolves these with 5 layers but adds mathematical precision. Key question: does QBism NEED the ultrametric machinery? The synthesis does not address this. |
| **Causal Dynamical Triangulations** (Oriti 2007-2013) | Spacetime as simplicial complex. Discrete at Planck scale, 4D at large scales. Spectral dimension flows 2D→4D. | S1, S3, S11, S23 | **Lighter-weight alternative.** Resolves 4 spacetime schisms with ONE structure (simplicial complex). No distinction calculus, no ultrametric, no Bootstrap needed. The synthesis does not address why CDT is insufficient. |
| **p-Adic Braneworld** (Dzhunushaliev 2008) | Extra dimensions are p-adic, not real. Braneworld scenario with p-adic extra dimensions. | S14, S23, S15 | **Independent p-adic proposal** — converges with QNFO adelic program but for different reasons (particle physics, not foundations). |
| **Wolfram Physics Project** | The universe is a hypergraph rewriting system. Discrete, computational, no continuum assumed. | S1, S2, S11, S23, S16 | **Conceptual convergence.** Wolfram independently arrived at: discrete substrate, computational irreducibility, laws as emergent from rules. Difference: Wolfram's hypergraph is not ultrametric and doesn't use self-referential calibration. |
| **AdS/CFT Correspondence** (Maldacena 1997) | Gravitational theory in (d+1)-dimensional AdS is dual to CFT on d-dimensional boundary. | S27 | **Map-territory unification without ultrametricity.** Demonstrates that S27 can be addressed with standard differential geometry. Undermines the claim that Layer 4 (Monna projection) is "necessary." |

### 1.2 No External Work Catalogs All 29 Schisms

The 29-schism paper's literature search (arXiv: 72 results, Semantic Scholar: 17 results) confirmed that no external work:
1. Catalogs all 29 schisms
2. Traces them to a single root cause
3. Proposes self-referential calibration as the unifying meta-framework

The closest external work is McKeever & Nazir (2026), which surveys QM interpretations but doesn't extend to quantum gravity, p-adic mathematics, or self-referential metrology. **This confirms the originality of the QNFO taxonomy.**

### 1.3 External Citations of QNFO Work

Zero. No external citations found for any QNFO paper in the Semantic Scholar database. The entire program is self-contained and has not yet penetrated the external academic literature. This is NOT a critique of the work's quality — it is a fact about its current stage of dissemination. All QNFO papers cite only other QNFO papers or pre-existing external literature. This is typical for a new research program.

---

## 2. WHAT'S NEXT? — Immediate Research Priorities

### Priority 0: Formal Proof of Bootstrap Conjecture

**Blocked by:** No formal definition of the calibration map C on token space.
**Required:** Define C precisely; prove contractiveness in the ultrametric; prove uniqueness of fixed point; derive valuation structure from fixed point; show fixed point corresponds to observed physical constants.
**Status:** Banach's theorem provides the abstract template but the concrete map is unspecified.
**Feasibility:** HIGH for the mathematical part (items 1-3), LOW for the physics part (item 4).

### Priority 1: External Validation of the 29-Schism Taxonomy

**Blocked by:** No external researcher has reviewed the taxonomy.
**Required:** Submit the taxonomy to an external researcher (not affiliated with QNFO) for classification validation. Do the schisms hold under external scrutiny? Are there missing schisms? Are some schisms miscategorized as physics rather than philosophy?
**Feasibility:** HIGH — this is a classification exercise, not a mathematical proof.
**Critical because:** The entire framework's claim to resolve "all 29" depends on the taxonomy being correct and complete. If external review adds, removes, or reclassifies schisms, the resolution claim must be recalculated.

### Priority 2: Trapped-Ion Page-Wootters Experiment

**Status:** Protocol fully designed (Yb$^+$ ion, 4 Zeeman sublevels as clock, motional Fock states as rest system). Predicts exact ultrametric conditional state overlaps (UVR=0%) for diagonal coupling and ~32% violation rate for nondiagonal coupling.
**Blocked by:** Requires trapped-ion lab access. Protocol is implementable with EXISTING technology — no new hardware needed.
**Impact:** If successful, this would provide the FIRST empirical evidence for ultrametric structure in quantum systems. This is the nearest-term falsifiable test of the entire framework.
**OSF Registration:** A CMB p-adic signature search was OSF-registered (2026-07-20, registration in progress). This experiment should also be pre-registered.

### Priority 3: CMB Log-Periodic Oscillation Search

**Status:** Analysis protocol fully specified — log-resample $C_\ell$, Fourier transform, peak detection. Data from Planck, ACT, SPT, and future CMB-S4.
**Blocked by:** Requires access to cleaned CMB data and Monte Carlo significance testing.
**Impact:** Direct test of discrete scale invariance prediction. If log-periodic oscillations are detected, this would be the first cosmological evidence for the framework.

### Priority 4: GUF-to-Adelic Bridge Theorem

**Status:** GUF (Calabi-Yau, $|\chi|=6$) and adelic framework are isolated pillars. The Euler characteristic $|\chi|=6$ may relate to the Bruhat-Tits tree's branching factor $p+1$ at $p=2$ (where $p+1=3$ and $6=2\times3$).
**Blocked by:** No formal mathematical relationship established. Pure numerology at present.
**Feasibility:** LOW — requires deep work in algebraic geometry and p-adic analysis.

### Priority 5: Hardware Implementation of Ultrametric Quantum Circuits

**Status:** No physical ultrametric quantum circuit has ever been built. The trapped-ion protocol designs one, but it hasn't been executed.
**Required:** Fabricate a quantum system with Hamiltonian engineered to mimic p-adic metric; demonstrate passive relaxation into protected topological sector; measure error rates and compare to active QEC.
**Feasibility:** MEDIUM — protocol exists, hardware exists (trapped ions), but requires lab access and funding.

---

## 3. DOMAIN-SPECIFIC PRACTICAL APPLICATIONS (Cross-Domain Validation)

### 3.1 Quantum Computing: Passive Geometric Fault Tolerance

**Application:** Replace active quantum error correction (surface codes, thousands of physical qubits per logical qubit) with passive protection based on number-theoretic incommensurability.

**Mechanism:** Ostrowski's theorem guarantees that Archimedean (real-numbered) perturbations cannot move p-adic fixed points because the $\mathbb{R}$ and $\mathbb{Q}_p$ topologies are mutually singular. A qubit encoded in a Majorana zero mode's ZBW state (a Bruhat-Tits tree fixed point) is protected against all Archimedean errors.

**Domain boundary crossed:** Quantum computing ↔ Number theory. The protection mechanism comes from pure mathematics (Ostrowski, 1916) applied to physical hardware. This is cross-domain validation: if passive fault tolerance succeeds, it validates BOTH the ultrametric framework AND the adelic physics program.

**Current status:**
- Theory: [CODE-EXECUTED] in the ZBW P1-P5 paper chain
- Experiment: Protocol designed (P3) but not yet executed
- Prediction: QEC overhead reduced by 1-2 orders of magnitude compared to surface codes [speculative]

**Falsification:** If engineered ultrametric circuits show comparable or worse error rates than active QEC, the passive protection claim is disconfirmed.

### 3.2 Trapped-Ion Physics: Testing Ultrametricity in the Lab

**Application:** Direct experimental test of the Sufficient Condition Theorem — that diagonal clock-rest coupling produces exact ultrametric conditional state overlaps.

**Mechanism:** A single Yb$^+$ ion with N=4 Zeeman sublevels (clock) and M motional Fock states (rest). Laser-driven carrier transitions (diagonal coupling, predicted UVR=0%) vs. sideband transitions (nondiagonal coupling, predicted UVR≈32%). Conditional state tomography at multiple clock readings yields the Parisi ultrametricity violation rate.

**Domain boundary crossed:** Quantum optics ↔ p-adic geometry. A tabletop quantum optics experiment tests predictions from pure p-adic mathematics.

**Current status:**
- Protocol: Fully specified (Hamiltonian, state preparation, measurement, error analysis)
- Hardware: Uses standard trapped-ion infrastructure (no new equipment needed)
- Feasibility: HIGH — this is the nearest-term test

**Falsification:** If UVR ≈ 32% for BOTH diagonal and nondiagonal coupling, the Sufficient Condition Theorem (and therefore the D=4 Ultrametric Special Case Theorem) is disconfirmed.

### 3.3 Cosmology: Log-Periodic CMB Oscillations

**Application:** Search for discrete scale invariance in the CMB angular power spectrum — a direct prediction of the Syntactic Token Calculus.

**Mechanism:** The STC predicts the primordial power spectrum (and therefore $C_\ell$) should be modulated by log-periodic oscillations: $\ell(\ell+1)C_\ell = A(\ell/\ell_0)^{1-n_s}[1 + B\cos(\frac{2\pi}{\ln q}\ln(\ell/\ell_0) + \phi)]$ where q is the fundamental scaling ratio of the cosmic web.

**Domain boundary crossed:** Quantum gravity ↔ Observational cosmology. A pre-geometric theory of spacetime makes testable predictions about the sky.

**Current status:**
- Theory: Fully specified (QNFO, 2026-04-13)
- Data: Planck, ACT, SPT legacy data available NOW
- Analysis protocol: 3-step (log-resample, Fourier/Lomb-Scargle, peak detection)
- OSF Registration: CMB higher n-point p-adic signature search registered (2026-07-20)
- Not yet executed on real data

**Falsification:** If no statistically significant (>3σ) log-periodic oscillations are found in CMB data at the cosmic variance limit, the STC cosmological prediction is falsified.

### 3.4 AI/Machine Learning: Bruhat-Tits Tree Hierarchical Clustering

**Application:** Replace Euclidean-based clustering (k-means, hierarchical agglomerative) with ultrametric tree-based clustering for hierarchical data.

**Mechanism:** Ballistic transport on Bruhat-Tits trees enables O(depth) navigation of hierarchical latent spaces. Decision paths are transparent walks on the tree (explainable AI). The ultrametric distance naturally captures hierarchical relationships without shoehorning them into Euclidean space.

**Domain boundary crossed:** Pure mathematics (p-adic geometry) ↔ Applied AI. Number-theoretic tree structures provide better representations for inherently hierarchical data (taxonomies, organizational structures, phylogenetic trees) than Euclidean embeddings.

**Current status:**
- Theory: Quantum walks on Bruhat-Tits trees exhibit ballistic transport [CODE-EXECUTED]
- Application: Natural fit for hierarchical clustering, explainable AI, neural data analysis
- No QNFO paper has built a production AI system on this — it's at the theoretical stage

**Validation metric:** If ultrametric embeddings of hierarchical data outperform Euclidean embeddings on standard clustering benchmarks (silhouette score, Davies-Bouldin index), this cross-validates the framework's claim that ultrametric geometry is the "correct" metric for hierarchical structure.

### 3.5 Error-Correcting Code Classification: Number-Theoretic Foundations

**Application:** Classify and analyze error-correcting codes using p-adic number theory rather than algebraic coding theory.

**Mechanism:** The "Number-Theoretic Ultrametric Foundations" paper (QNFO) proposes a unified p-adic framework for error-correcting code classification. Error syndromes map to p-adic valuations; code distance corresponds to tree depth.

**Domain boundary crossed:** Information theory ↔ Number theory. Error-correcting codes (an engineering discipline) are classified using p-adic mathematics (a pure math discipline).

**Current status:** Theoretical only. No QNFO paper has demonstrated superior code construction using p-adic methods.

### 3.6 Optimization: Prime Numbers as Universal Primitives

**Application:** Use prime number decompositions as optimization primitives rather than gradient-based methods.

**Mechanism:** The "Prime Numbers as Universal Optimization Primitives" paper (QNFO) proposes that prime number structure provides a natural optimization landscape that is scale-free and hierarchical.

**Domain boundary crossed:** Optimization ↔ Number theory. Optimization problems (engineering) are reformulated in terms of prime decompositions (pure math).

**Current status:** Theoretical only. No optimization benchmarks published.

---

## 4. WHAT CAN BE IMPROVED?

### 4.1 Bootstrap Conjecture → Formal Proof (CRITICAL)

**Current state:** Stated as a conjecture with a Banach fixed-point sketch. The "calibration map" C is not defined. Contractiveness is assumed.
**Improvement:** Define C precisely on token space. Prove contractiveness from the properties of the expression algebra. Prove uniqueness. This is the single most impactful improvement — it would convert the framework from "speculative" to "proven formal ontology."

### 4.2 External Taxonomy Validation (HIGH)

**Current state:** The 29 schisms were classified within the QNFO program. No external researcher has reviewed the taxonomy.
**Improvement:** Submit the taxonomy to 2-3 external physicists for classification validation. Publish their responses (with permission). This would convert the taxonomy from "QNFO-internal" to "independently verified."

### 4.3 Lighter-Weight Competitor Analysis (HIGH)

**Current state:** The synthesis mentions QBism and CDT in citations but does not engage with them as competitors. The GUF comparison is the only competitor evaluation, and it's asymmetric.
**Improvement:** Add a §6 to the synthesis: "Why Not Lighter?" — a schism-by-schism evaluation of QBism (what it resolves, what it doesn't, why the heavier framework is needed) and CDT (same). This addresses Occam's razor directly.

### 4.4 D1/KG Infrastructure (MODERATE)

**Current state:** PBO v1.0 exists as Zenodo DOI but not in D1. Ratio-Based Adelic Physics body is empty in D1. Only 2 Theorem nodes in KG.
**Improvement:** Deploy PBO v1.0 to D1 living-paper DB. Upload Ratio-Based Adelic body. Seed Theorem nodes for Bootstrap Conjecture, Monna Projection, PBO axioms, D=4 Ultrametric Special Case, and the F-contractiveness conditions.

### 4.5 Experimental Program Design (MODERATE)

**Current state:** Three experimental protocols exist (CMB log-periodic, trapped-ion ultrametricity, ZBW readout) but none have been executed.
**Improvement:** Create a unified experimental roadmap with timelines, required resources, and success criteria. Pre-register all experiments on OSF before data collection.

### 4.6 Hardware Implementation Roadmap (LOW)

**Current state:** Passive fault tolerance exists as a theoretical claim. No physical ultrametric quantum circuit has been built.
**Improvement:** Design a 5-year hardware roadmap from trapped-ion proof-of-concept → multi-qubit ultrametric circuit → fault-tolerant logical qubit demonstration.

---

## 5. WHAT ARE THE GAPS?

### 5.1 Technical Gaps (5)

| # | Gap | Severity | Status |
|---|-----|----------|--------|
| **G1** | Bootstrap Conjecture unproven | CRITICAL | Formal definition of C + contractiveness proof needed |
| **G2** | "Which primes?" problem | CRITICAL | Branching factors of physical tree unknown — requires solving fixed-point equation |
| **G3** | Einstein equations bridge | HIGH | No derivation of GR from STC token dynamics |
| **G4** | Connectedness of expression space | MODERATE | Assumed, not proved — affects uniqueness of fixed point |
| **G5** | Adelic disconfirming registry (5 items) | MODERATE | Partially addressed in v1.1, but all 5 remain as unresolved tensions |

### 5.2 Infrastructure Gaps (3)

| # | Gap | Severity | Status |
|---|-----|----------|--------|
| **G6** | PBO v1.0 not in D1 living-paper DB | MODERATE | DOI exists but papers.qnfo.org returns 404 |
| **G7** | Theorem nodes missing from KG | MODERATE | Only 2 Theorem nodes (D=4 Ultrametric Special Case) |
| **G8** | Ratio-Based Adelic Physics body empty in D1 | MODERATE | Data preservation issue |

### 5.3 Hardware/Experimental Gaps (3)

| # | Gap | Severity | Status |
|---|-----|----------|--------|
| **G9** | No physical ultrametric quantum circuit built | HIGH | Protocol exists, hardware exists, but not executed |
| **G10** | CMB log-periodic search not executed on real data | HIGH | Analysis protocol exists, data available, not analyzed |
| **G11** | ZBW readout protocols not on real Majorana hardware | MODERATE | Three protocols designed (spin noise, EELS/RIXS, Gromov δ), none executed |

---

## 6. POTENTIAL FALSIFICATION / COUNTERFACTUALS

### 6.1 Existing Falsification Entries (from v1.0 Falsifiability Register)

| [CHECK] | Prediction | Falsification Condition | If Falsified |
|---------|-----------|------------------------|--------------|
| **2035** | Log-periodic CMB oscillations at $\ell>2000$ | No log-periodic structure at cosmic variance limit | STC cosmological prediction dead; Layer 1 weakened |
| **2035** | Passive fault tolerance ≤10% of active QEC overhead | Ultrametric circuits require comparable overhead | Adelic QEC claim dead; Layer 1-2 application bridge broken |
| **2040** | Fine-structure constant converges to fixed point | α confirmed constant to <10⁻⁷ precision | Bootstrap Conjecture contradicted; Layer 3 fails |
| **2040** | p-adic signature in precision measurements | All precision data explained by SM + conventional BSM | Adelic framework disconfirmed; Layer 1-4 bridge broken |
| **2045** | Bootstrap Conjecture formally proven | Counterexample found (two distinct self-consistent fixed points) | Central mechanism falsified; entire framework collapses |

### 6.2 NEWLY IDENTIFIED Falsification / Counterfactual Conditions

| # | Condition | If True, Consequence | Severity |
|---|-----------|---------------------|----------|
| **F6** | QBism or CDT is shown SUFFICIENT to resolve all observer/spacetime schisms without ultrametric machinery | The heavy 5-layer framework is unnecessary — Occam's razor favors the lighter alternative. The framework would still be mathematically valid but physically redundant. | HIGH |
| **F7** | Tree growth is proven super-exponential (not exponential) beyond depth 10 | The "exponential growth" finding (v1.1) was premature. All physical predictions become incomputable. Framework is unfalsifiable in practice. | CRITICAL |
| **F8** | The adelic Dirac equation (P7 Grand Synthesis) makes a specific, testable prediction that is experimentally contradicted | The adelic physics program is falsified. Layer 1-4 connection broken. | CRITICAL |
| **F9** | p-adic signatures are definitively excluded by all precision measurement experiments at all energy scales | The entire adelic claim collapses. Ostrowski's theorem remains mathematically true but physically irrelevant. | CRITICAL |
| **F10** | A physically necessary calibration process is proven to be non-contractive in the ultrametric | Banach's theorem doesn't apply. No unique fixed point. Landscape problem returns. Bootstrap Conjecture and Schism 19 resolution both fail. | CRITICAL |

### 6.3 Counterfactual Dependency Map

```
F7 (super-exponential) ──→ F5 (Bootstrap) ──→ F10 (non-contractive)
        │                        │
        └──→ F1 (CMB)            └──→ F3 (α convergence)
                                       │
F9 (p-adic excluded) ──→ F8 (adelic Dirac false)
        │
        └──→ F2 (passive QEC)
        
F6 (QBism/CDT sufficient) ──→ framework unnecessary (but not false)
```

### 6.4 What Would Survive If Everything Is Falsified?

If ALL 10 falsification conditions are met, the following would remain:

1. **The 29-schism taxonomy** — still a valid inventory of physics foundations problems.
2. **The distinction calculus** (Layer 0) — Spencer-Brown's Laws of Form is mathematically verified independent of physics.
3. **The abstract formalization** — MARK and CONTAINER as primitives is a valid formal ontology regardless of physical applicability.
4. **The executable implementation** — the toy model demonstrates non-Archimedean distance properties, which are mathematically interesting even without physics.

What would NOT survive:
1. **The claim that ultrametric geometry is "the correct metric" for physics**
2. **The Bootstrap Conjecture as a physical mechanism**
3. **All cross-domain applications (QEC, AI, CMB)**
4. **The 29/29 resolution claim**

The framework would revert to: **"an interesting formal ontology with mathematical elegance but zero confirmed physical relevance."**

---

## 7. SYNTHESIS: Cross-Program Connection Map

The 29-schisms framework sits at the intersection of these QNFO research programs:

```
                    ┌──────────────────────────┐
                    │  29-Schisms Framework     │
                    │  (v1.1, DOI: 21465629)   │
                    └──────────┬───────────────┘
                               │
        ┌──────────────────────┼──────────────────────┐
        │                      │                      │
        ▼                      ▼                      ▼
┌───────────────┐    ┌────────────────┐    ┌──────────────────┐
│ Adelic Physics │    │ Ultrametric    │    │ Syntactic Token  │
│ Program (P1-P7)│    │ Quantum Comp   │    │ Calculus (STC)   │
│ ZBW + QEC      │    │ Bruhat-Tits    │    │ Mark/Enclosure   │
└───────┬───────┘    └───────┬────────┘    └────────┬─────────┘
        │                    │                       │
        ▼                    ▼                       ▼
┌───────────────┐    ┌────────────────┐    ┌──────────────────┐
│ Trapped-Ion   │    │ CMB Log-Period │    │ Pattern-Based    │
│ Page-Wootters │    │ Oscillation    │    │ Ontology v1.0    │
│ Experiment    │    │ Search         │    │ (PBO)            │
└───────────────┘    └────────────────┘    └──────────────────┘

        ┌──────────────────────┼──────────────────────┐
        │                      │                      │
        ▼                      ▼                      ▼
┌───────────────┐    ┌────────────────┐    ┌──────────────────┐
│ Honest Comp   │    │ Problem-       │    │ Prime Numbers    │
│ Manifesto     │    │ Substrate Map  │    │ as Optimization  │
│ Qubit Delusion│    │                │    │ Primitives       │
└───────────────┘    └────────────────┘    └──────────────────┘

        ┌──────────────────────┼──────────────────────┐
        │                      │                      │
        ▼                      ▼                      ▼
┌───────────────┐    ┌────────────────┐    ┌──────────────────┐
│ GUF (Calabi-  │    │ Ratio-Based    │    │ Autaxys          │
│ Yau, |χ|=6)   │    │ Adelic Physics │    │ (Generative      │
│ ISOLATED       │    │ DEPLOYMENT GAP │    │ Meta-Framework)  │
└───────────────┘    └────────────────┘    └──────────────────┘
```

**Key:**
- Solid arrows: Active connection / paper chain
- No arrow to GUF: Isolated Archimedean pillar (identified in KG audit)
- Ratio-Based Adelic: Bridge between ontology and math, but body missing from D1

---

## 8. REFERENCES

### QNFO Internal (Key Papers)
- 29-Schism Synthesis: DOI 10.5281/zenodo.21458373
- Quantum Laws of Form (STC): DOI 10.5281/zenodo.19578015
- Adelic Physics Grand Synthesis: DOI TBD (P7 paper)
- Adelic QEC (P5): DOI TBD
- Pattern-Based Ontology v1.0: DOI 10.5281/zenodo.21389579
- GUF: DOI 10.5281/zenodo.17074684
- Log-Periodic CMB: QNFO 2026-04-13
- Trapped-Ion Page-Wootters: QNFO 2026-07-01
- Number-Theoretic Ultrametric Foundations: QNFO
- Prime Numbers as Optimization Primitives: QNFO
- The Qubit Delusion: QNFO
- Problem-Substrate Mapping: QNFO

### External
- Dragovich, B. "p-Adic and Adelic Quantum Mechanics." Proc. Steklov Inst. Math., 2003.
- Fuchs, C.A. "QBism, the Perimeter of Quantum Bayesianism." arXiv:1003.5209, 2010.
- Oriti, D. "The Group Field Theory Approach to Quantum Gravity." 2013.
- Dzhunushaliev, V. "p-Adic Branes." 2008.
- Wolfram, S. "A New Kind of Science." 2002. "Wolfram Physics Project." 2020.
- Bekenstein, J.D. "Black Holes and Information Theory." Contemp. Phys., 2003.
- Maldacena, J. "The Large N Limit of Superconformal Field Theories." ATMP, 1998.
- McKeever & Nazir. Survey of QM Interpretations, 2026.
- Ostrowski, A. "Über einige Lösungen der Funktionalgleichung." Acta Math., 1916.
- Banach, S. "Sur les opérations dans les ensembles abstraits." Fund. Math., 1922.
