# Technology Survey: Quantum Platforms for Ultrametric Hamiltonian Engineering

**Phase 6, Task 6.1 Deliverable — Hardware Roadmap**
**Date:** 2026-07-20
**Status:** v1.0
**Purpose:** Identify quantum computing platforms capable of emulating ultrametric (non-Archimedean) Hamiltonian structures, enabling the trapped-ion proof-of-concept to scale toward passive fault tolerance.

---

## §0. Executive Summary

Five quantum computing platforms are evaluated for their suitability to encode **ultrametric Hamiltonians** — Hamiltonians whose energy spectrum follows a non-Archimedean (p-adic-like) distance structure rather than the standard Euclidean/Lebesgue measure. The trapped-ion platform scores highest overall (4.3/5) and is the recommended path for Phase 3 proof-of-concept. Neutral atoms emerge as the strongest candidate for scaling to multi-qubit fault-tolerant circuits (Years 3–5).

| Platform | Hamiltonian Tunability | p-adic Feasibility | Coherence | Scalability | **Score** |
|----------|----------------------|-------------------|-----------|-------------|-----------|
| **Trapped Ions** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | **4.3** |
| **Neutral Atoms** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | **4.3** |
| **Superconducting** | ⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | **3.3** |
| **Photonic** | ⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | **3.0** |
| **Majorana** | ⭐ | ⭐ | ⭐⭐ | ⭐⭐ | **1.5** |

**Recommendation:** Trapped ions for Phase 3 (proof-of-concept, 2026–2027). Neutral atoms for Phase 6 Years 3–5 (scaling, 2028–2030).

---

## §1. Evaluation Criteria

Each platform is scored 1–5 on four dimensions:

### C1: Hamiltonian Tunability
Can the platform's effective Hamiltonian be engineered to produce a spectrum with non-Archimedean distance structure? Key sub-criteria:
- Independent control of individual qubit frequencies
- Programmable long-range interactions (essential for ultrametric clustering)
- Ability to implement non-local coupling terms (e.g., `J_{ij}` falling off as `2^{-d(i,j)}`)
- Absence of nearest-neighbor-only constraints

### C2: p-Adic Metric Emulation Feasibility
Can the platform simulate a system where the distance between states follows `DIST(x, y) = 2^{-v_p(x-y)}` rather than `|x - y|`? Key sub-criteria:
- Ability to encode hierarchical clustering (states closer in ultrametric share deeper common ancestors in the interaction graph)
- Controllable interaction range that can be programmed to fall off as `p^{-k}` rather than `1/r`
- Support for fractal/self-similar coupling patterns (essential for tree-like distance structures)

### C3: Coherence Time
How long can quantum information be maintained before decoherence destroys the ultrametric structure? Key sub-criteria:
- T1 (energy relaxation) and T2 (dephasing) times relative to gate operation times
- Gate fidelity (must exceed fault-tolerance thresholds for multi-qubit circuits)
- Stability of the engineered Hamiltonian over the duration of the experiment

### C4: Scalability
How many qubits can be deployed, and with what connectivity? Key sub-criteria:
- Current maximum qubit count (2026 state-of-the-art)
- Projected 5-year trajectory (2026–2031)
- All-to-all vs. nearest-neighbor connectivity
- Gate parallelizability (can multiple gates execute simultaneously?)

---

## §2. Platform Evaluations

---

### 2.1 Trapped Ions (IonQ, Quantinuum, Innsbruck, NIST)

**How it works:** Individual atomic ions (typically Yb⁺, Ca⁺, or Ba⁺) are confined in RF Paul traps and laser-cooled to their motional ground state. Qubits are encoded in hyperfine or Zeeman sublevels. Gates are mediated by laser-induced coupling to shared motional modes.

**Representative systems (2026):**
- IonQ Forte Enterprise: 36 algorithmic qubits, 99.97% two-qubit gate fidelity
- Quantinuum H2: 56 qubits, 99.8% two-qubit fidelity, real-time error correction demonstrated
- Innsbruck (Blatt group): 24-ion fully-connected quantum simulator

| Criterion | Score | Rationale |
|-----------|-------|-----------|
| **C1: Hamiltonian Tunability** | ⭐⭐⭐⭐⭐ (5/5) | Ion traps offer the best Hamiltonian engineering of any platform. Individual ion frequencies can be shifted via AC Stark (light) shifts with sub-Hz precision. Laser addressing with acousto-optic deflectors (AODs) enables independent control of each ion. Long-range spin-spin interactions are mediated by shared motional modes — the coupling matrix `J_{ij}` can be programmed to follow any desired pattern, including ultrametric clustering. **The Phase 3 protocol's requirement of "Doppler cooling + sideband cooling to n=0 + Zeeman sublevel resolution" is standard operating procedure in trapped-ion labs.** |
| **C2: p-Adic Emulation** | ⭐⭐⭐⭐ (4/5) | The all-to-all connectivity of ion traps naturally supports hierarchical clustering. By programming `J_{ij} ∝ 2^{-d(i,j)}` where `d(i,j)` is the depth of the deepest common ancestor in a programmed tree structure, the effective Hamiltonian can encode ultrametric distances. **Limitation:** The number of programmable interaction patterns is limited by the number of motional modes (≈ N modes for N ions). For N > 20, the interaction matrix is overcomplete and arbitrary patterns may not be realizable without approximation. |
| **C3: Coherence Time** | ⭐⭐⭐⭐⭐ (5/5) | Hyperfine qubits in Yb⁺ have T1 > 1000 s and T2 > 10 s (dynamical decoupling). Zeeman qubits have shorter T2 but faster gates. Gate fidelities exceed 99.9% (single-qubit) and 99.5% (two-qubit), approaching the surface-code threshold. **The Phase 3 protocol's coherence requirements (T2 ≫ gate time, ~μs) are trivially satisfied.** Motional heating rates of ~1 quanta/s in cryogenic traps allow hundreds of gate operations before decoherence. |
| **C4: Scalability** | ⭐⭐⭐ (3/5) | **Strengths:** All-to-all connectivity within a single trap. Gate parallelization via multiple laser beams. **Limitations:** Scaling beyond ~50 ions in a single trap is difficult due to spectral crowding (motional mode density increases as N). Multi-zone architectures (QCCD — Quantum Charge-Coupled Device) shuttle ions between trap zones but add overhead and reduce speed. **5-year projection:** 100–200 logical qubits feasible via QCCD; >1000 unlikely without major architectural advances. |
| **Overall Score** | **4.3/5** | **Best choice for Phase 3 proof-of-concept (1–4 ions).** Unmatched Hamiltonian control and coherence. Scaling to Year 3–5 multi-qubit circuits requires QCCD architecture, which adds complexity. |

**Key labs with relevant capability:**
- Quantinuum (H-series, QCCD architecture, commercial access)
- Innsbruck (Blatt group, 24-ion quantum simulator, academic collaboration)
- NIST Boulder (Leibfried group, precision spectroscopy, academic collaboration)
- IonQ (commercial cloud access, smaller systems ideal for initial tests)

**Estimated access cost:** $50K–150K for dedicated beam time (4 days protocol time + 1 week setup). Quantinuum cloud access: ~$10K/month for priority queue. Academic collaboration: no direct cost if co-authored.

---

### 2.2 Neutral Atoms (QuEra, Pasqal, Harvard/MIT, Caltech)

**How it works:** Neutral atoms (typically Rb or Sr) are trapped in optical tweezer arrays and excited to Rydberg states. The Rydberg blockade mechanism provides strong, programmable interactions between atoms within a blockade radius. Rearrangement via moving tweezers enables arbitrary connectivity.

**Representative systems (2026):**
- QuEra Aquila (cloud): 256 atoms, reconfigurable geometry, Rydberg blockade
- Harvard/Lukin group: 512+ atom programmable arrays, demonstrated logical qubits (2024)
- Pasqal: 100+ atoms, 2D/3D geometries, industrial partnerships

| Criterion | Score | Rationale |
|-----------|-------|-----------|
| **C1: Hamiltonian Tunability** | ⭐⭐⭐⭐ (4/5) | Rydberg interactions enable programmable Ising-type Hamiltonians `H = Σ_i Ω_i σ_i^x + Σ_{i<j} V_{ij} n_i n_j` where `V_{ij} ∝ 1/r^6` in the van der Waals regime. Interaction strength and range are tunable via laser detuning and principal quantum number. **Limitation:** The `1/r^6` scaling is not directly p-adic (`2^{-d}`), but can be approximated on a tree-structured lattice geometry. The blockade radius creates a natural hierarchical clustering structure. |
| **C2: p-Adic Emulation** | ⭐⭐⭐⭐ (4/5) | Optical tweezer arrays can be arranged in tree-like geometries (fractal patterns, hierarchical clusters). The Rydberg blockade naturally creates an "interaction horizon" analogous to ultrametric distance — atoms within the blockade radius are "close" (same branch), atoms outside are "far" (different branch). By programming multiple blockade radii at different Rydberg levels, hierarchical distance structures can be encoded. **Key advantage:** Moving tweezers enable dynamical reconfiguration of the geometry during the experiment. |
| **C3: Coherence Time** | ⭐⭐⭐⭐ (4/5) | Ground-state hyperfine qubits have T2 > 1 s (comparable to trapped ions). Rydberg state lifetimes are shorter (~100 μs for n≈70) but gate operations are fast (~100 ns). Gate fidelities ~99.5% for two-qubit gates, approaching but not exceeding surface-code thresholds. **Limitation:** Spontaneous emission from Rydberg states is the dominant error source — mitigated by higher principal quantum numbers (longer lifetime) but increases sensitivity to stray fields. |
| **C4: Scalability** | ⭐⭐⭐⭐⭐ (5/5) | **The most scalable platform.** 256+ atoms demonstrated; 1000+ feasible with current technology. Tweezer arrays scale linearly with laser power (no spectral crowding, unlike ion traps). Rearrangement via SLMs (spatial light modulators) enables arbitrary 2D/3D geometries. Multi-zone architectures with atom transport between zones are under development (Harvard 2025). **5-year projection:** 1000–5000 physical qubits in reconfigurable arrays. Logical qubit counts limited by gate fidelity, not qubit count. |
| **Overall Score** | **4.3/5** | **Best choice for Phase 6 Years 3–5 scaling (10+ qubit ultrametric circuits).** Superior scalability compensates for slightly lower gate fidelity vs. trapped ions. The reconfigurable geometry is uniquely suited to implementing tree-structured interaction graphs. |

**Key labs with relevant capability:**
- QuEra (cloud access, 256-atom programmable arrays)
- Harvard/Lukin group (academic collaboration, 512+ atoms, world-leading)
- Pasqal (industrial/cloud access, 100+ atoms, EU-based)
- Caltech/Endres group (Rydberg dressing, academic collaboration)

**Estimated access cost:** QuEra cloud: ~$5K/month. Harvard collaboration: academic partnership, no direct cost. Pasqal: ~€50K for dedicated beam time.

---

### 2.3 Superconducting Qubits (IBM, Google, Rigetti)

**How it works:** Josephson junction-based qubits (transmons, fluxoniums) operated at ~10 mK in dilution refrigerators. Gates via microwave pulses. Fixed nearest-neighbor connectivity on 2D lattice chips.

**Representative systems (2026):**
- IBM Heron: 156 qubits, heavy-hex lattice, 99.9% two-qubit fidelity
- Google Willow: 105 qubits, square lattice, below-threshold error correction demonstrated (2024)

| Criterion | Score | Rationale |
|-----------|-------|-----------|
| **C1: Hamiltonian Tunability** | ⭐⭐⭐ (3/5) | Qubit frequencies are fixed at fabrication; tunable via flux bias within narrow ranges. Two-qubit interactions are mediated by fixed capacitive or inductive couplers with limited programmability. **Not suitable for arbitrary `J_{ij}` programming** — the Hamiltonian is determined by the chip layout. Parametric coupling schemes (tunable couplers) provide some flexibility but cannot match the all-to-all programmability of ions or atoms. |
| **C2: p-Adic Emulation** | ⭐⭐ (2/5) | The fixed 2D lattice geometry is fundamentally incompatible with tree-based ultrametric structures. While fractal lattice embeddings exist (e.g., Cayley tree on 2D grid), they introduce overhead (SWAP gates) that amplifies decoherence. The nearest-neighbor connectivity makes hierarchical clustering expensive — each level of the tree requires O(depth) SWAP chains. |
| **C3: Coherence Time** | ⭐⭐⭐ (3/5) | Typical T1 ≈ 100–300 μs, T2 ≈ 50–150 μs for transmons. Gate times ~20–50 ns. Coherence limited by dielectric loss, quasiparticle tunneling, and flux noise. **Improving rapidly** — fluxonium qubits (T1 > 1 ms) and protected qubits (e.g., 0-π qubit) are promising but not yet production-ready. |
| **C4: Scalability** | ⭐⭐⭐⭐⭐ (5/5) | **Most mature scaling roadmap.** IBM roadmap targets 2000+ qubits by 2027 (Flamingo). Google targets 1000+ by 2027. Manufacturing infrastructure exists (semiconductor fabrication). Multi-chip modules under development. **5-year projection:** 5000–10000 physical qubits. |
| **Overall Score** | **3.3/5** | **Not recommended for ultrametric Hamiltonian engineering.** Excellent for general-purpose quantum computing but the fixed 2D connectivity and limited Hamiltonian programmability make it the wrong platform for this application. Consider only if the protocol can be adapted to a lattice embedding (non-trivial theoretical work required). |

---

### 2.4 Photonic Quantum Computing (Xanadu, PsiQuantum, QuiX)

**How it works:** Qubits encoded in photons (polarization, time-bin, or continuous-variable). Gates via linear optical elements (beam splitters, phase shifters). Measurement-based (cluster state) or Gaussian boson sampling approaches.

| Criterion | Score | Rationale |
|-----------|-------|-----------|
| **C1: Hamiltonian Tunability** | ⭐⭐ (2/5) | Photonic platforms do not directly implement Hamiltonian evolution — they implement unitary transformations via linear optics. Simulating Hamiltonian dynamics requires Trotterization or variational approaches, adding circuit depth. Cluster-state measurement-based computing can simulate certain Hamiltonians but requires large resource states. |
| **C2: p-Adic Emulation** | ⭐⭐⭐ (3/5) | The tree structure of cluster states naturally encodes hierarchical entanglement — a cluster state on a tree graph has entanglement properties analogous to ultrametric distance. Continuous-variable cluster states (Xanadu) can encode qumodes with hierarchical coupling. **Interesting theoretical connection** but not yet experimentally demonstrated as an ultrametric simulator. |
| **C3: Coherence Time** | ⭐⭐⭐⭐⭐ (5/5) | Photons do not decohere (zero T1 in vacuum). Loss is the dominant error — fiber/silicon loss rates of ~0.1 dB/km at telecom wavelengths. Detection efficiency > 95% for superconducting nanowire detectors. **Theoretically unlimited coherence** — loss-limited rather than decoherence-limited. |
| **C4: Scalability** | ⭐⭐⭐ (3/5) | Photons can be multiplexed to large numbers. PsiQuantum aims for 1M+ qubits via silicon photonics. **However:** generating the required cluster states for Hamiltonian simulation requires enormous resource overhead (thousands of physical photons per logical qubit). Scalability is loss-limited by the optical network. |
| **Overall Score** | **3.0/5** | **Interesting theoretical match for tree-structured states, but not ready for experimental Hamiltonian simulation.** Photonics may become relevant if the theoretical connection between cluster-state trees and ultrametric structure is formalized — this would be a Task 6.1a (theoretical photonic-ultrametric mapping). |

---

### 2.5 Majorana / Topological Qubits (Microsoft, Delft, Copenhagen)

**How it works:** Qubits encoded in non-Abelian anyons (Majorana zero modes in semiconductor-superconductor nanowires). Topologically protected against local noise.

| Criterion | Score | Rationale |
|-----------|-------|-----------|
| **C1: Hamiltonian Tunability** | ⭐ (1/5) | Topological qubits are designed for gate operations (braiding), not Hamiltonian simulation. The topological protection that makes them noise-resistant also makes the Hamiltonian fixed and non-programmable. Braiding operations implement specific unitary gates; engineering arbitrary `J_{ij}` couplings is not currently possible. |
| **C2: p-Adic Emulation** | ⭐ (1/5) | No known mechanism for encoding ultrametric structure in topological systems. The mathematical framework (topological quantum field theory) is connected to braid groups, not tree structures or ultrametrics. A theoretical breakthrough would be required. |
| **C3: Coherence Time** | ⭐⭐ (2/5) | **Theoretically protected** — topological qubits should have exponential suppression of decoherence. **In practice:** Majorana devices have not yet demonstrated a topological qubit (Microsoft's 2025 retraction of key claims). Coherence data is extremely limited. |
| **C4: Scalability** | ⭐⭐ (2/5) | **Theoretically scalable** (topological protection improves with system size). **In practice:** No multi-qubit topological device has been demonstrated. The platform is 5–10 years behind superconducting and trapped ions. |
| **Overall Score** | **1.5/5** | **Not viable for the 5-year roadmap.** Topological qubits may become relevant in 2030+ if fundamental demonstrations succeed, but they should not factor into Phase 3–6 planning. |

---

## §3. Platform Comparison: Ultrametric-Specific Features

| Feature | Trapped Ions | Neutral Atoms | Superconducting | Photonic | Majorana |
|---------|-------------|---------------|-----------------|----------|----------|
| All-to-all connectivity | ✅ Native | ✅ Reconfigurable | ❌ Fixed lattice | ✅ In cluster | ❌ |
| Programmable `J_{ij}` | ✅ Full | ✅ Via geometry | ⚠️ Limited | ❌ Not direct | ❌ |
| Tree-structure embedding | ✅ Mode programming | ✅ Tweezer geometry | ❌ Via SWAPs | ✅ Cluster state | ❌ |
| Coherence > 100 gate ops | ✅ | ✅ | ⚠️ Marginal | ✅ | ❌ Unknown |
| Cloud access (2026) | ✅ IonQ, Quantinuum | ✅ QuEra | ✅ IBM, Google | ⚠️ Xanadu | ❌ |
| Hardware cost (Phase 3) | $$–$$$ | $–$$ | $$ | $$ | N/A |
| 5-year scaling projection | 100–200 logical | 500–1000 logical | 5000+ physical | 10⁴–10⁵ photons | 0 logical |

---

## §4. Roadmap Integration

### Phase 3 (2026–2027): Trapped-Ion Proof-of-Concept
- **Platform:** Trapped ions (Quantinuum H2 or Innsbruck academic collaboration)
- **Qubits:** 1–4
- **Key capability:** Doppler + sideband cooling, Zeeman sublevel resolution, carrier/sideband Rabi frequency calibration
- **Deliverable:** Ultrametricity test of the Sufficient Condition Theorem

### Phase 6 Year 1–2 (2027–2028): Two-Ion Entangled Ultrametric Test
- **Platform:** Trapped ions (same lab)
- **Qubits:** 2 (entangled pair)
- **Key capability:** Bell-state preparation, ultrametric distance measurement between entangled ions

### Phase 6 Year 3 (2028–2029): 4-Ion Logical Qubit
- **Platform:** Trapped ions OR neutral atoms (pivot decision based on Year 1–2 results)
- **Qubits:** 4
- **Key capability:** Encoding of a logical qubit in an ultrametric cluster

### Phase 6 Year 4 (2029–2030): Fault-Tolerant Demonstration
- **Platform:** Neutral atoms (Harvard/QuEra)
- **Qubits:** 10+ logical qubits
- **Key capability:** Comparison to surface code overhead — demonstrate passive fault tolerance advantage

### Phase 6 Year 5 (2030–2031): Benchmark Against Surface Code
- **Platform:** Neutral atoms or superconducting (IBM)
- **Qubits:** 20+ logical qubits
- **Key capability:** Quantitative comparison: ultrametric encoding vs. surface code for equivalent computational task

---

## §5. Risk Register

| Risk | Probability | Impact | Mitigation |
|------|-----------|--------|------------|
| No trapped-ion lab grants access | Medium | CRITICAL | Pursue 3+ labs simultaneously; Quantinuum cloud as backup |
| Motional heating prevents n=0 cooling | Low | HIGH | Cryogenic traps (4K) reduce heating by 100×; demonstrated at NIST |
| Ultrametric Hamiltonian cannot be engineered with available motional modes | Low | MEDIUM | Approximate with nearest-mode projection; acceptable for proof-of-concept |
| Neutral atom gate fidelity stalls below fault-tolerance threshold | Medium | HIGH | Monitor Harvard/MIT tensor-network error mitigation advances |
| Funding for dedicated beam time unavailable | Medium | HIGH | Cloud access (Quantinuum ~$10K/month, QuEra ~$5K/month) as lower-cost alternative |
| Theoretical mapping of ultrametric to photonic cluster states not found | High | LOW | Photonic platform is aspirational; not on critical path |

---

## §6. Recommendations

1. **Immediate (Phase 3, 2026):** Initiate contact with 3 trapped-ion labs (Quantinuum commercial, Innsbruck academic, NIST academic). Prepare protocol package for review. Quantinuum cloud access as fallback.

2. **Medium-term (Phase 6 Years 2–3):** Establish neutral atom collaboration (Harvard/Lukin group or QuEra). Begin theoretical work on ultrametric embedding in tweezer-array geometries.

3. **Monitoring only:** Superconducting (IBM/Google) — track error correction advances. Photonic — track cluster-state scaling. Majorana — track fundamental demonstrations only; revisit in 2030+.

4. **Not recommended for this roadmap:** Diamond NV centers (limited connectivity), NMR (cannot scale), quantum dots (coherence too short for Hamiltonian engineering).

---

## References

- Blatt, R. & Roos, C.F. "Quantum simulations with trapped ions." Nature Physics 8, 277 (2012).
- Browaeys, A. & Lahaye, T. "Many-body physics with individually controlled Rydberg atoms." Nature Physics 16, 132 (2020).
- Bluvstein, D. et al. "Logical quantum processor based on reconfigurable atom arrays." Nature 626, 58 (2024).
- Quantinuum. "H2 Quantum Computer Specifications." quantinuum.com (2026).
- QuEra Computing. "Aquila: 256-Qubit Neutral-Atom Quantum Computer." quera.com (2026).
- IBM Quantum. "Heron Processor: 156 Qubits." ibm.com/quantum (2026).
- Google Quantum AI. "Quantum error correction below the surface code threshold." Nature (2024).
- `trapped-ion-ultrametricity-experiment-protocol.md` — Phase 3 Protocol
- `WBS-NEXT-PHASES.md` — Phase 6 Hardware Roadmap

---

*End of Technology Survey*
