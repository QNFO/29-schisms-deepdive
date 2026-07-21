# WBS: Cancellation Rule + S10 Observer — Integrated Research Program
## "The Measurement Boundary: From Distinction Calculus to Observer Ontology"

**Parent project:** 29-schisms-deepdive (Zenodo v2.3, DOI 10.5281/zenodo.21469000)
**Spin-off handoffs:** `HANDOFF-cancellation-rule-research-project.md` + `HANDOFF-s10-observer-inside-outside-research-project.md`
**Date:** 2026-07-21
**Target executor:** LLM agent (DeepChat / Claude), one phase per session
**Status:** DESIGN PHASE — WBS generated, awaiting Phase 0 execution

---

## §0. Program Architecture

```
                    ┌─────────────────────────────┐
                    │  Phase 0: Infrastructure     │
                    │  Repos, handoff ingestion,   │
                    │  Zenodo pre-reservation      │
                    └──────────────┬──────────────┘
                                   │
              ┌────────────────────┼────────────────────┐
              ▼                    ▼                    ▼
     ┌────────────────┐  ┌────────────────┐  ┌────────────────┐
     │ Phase 1        │  │ Phase 2        │  │ Phase 3        │
     │ Cancellation   │  │ S10 Observer   │  │ M-Property     │
     │ Rule Deep-Dive │  │ Deep-Dive      │  │ Bridge         │
     └───────┬────────┘  └───────┬────────┘  └───────┬────────┘
             │                   │                   │
             └───────────────────┼───────────────────┘
                                 ▼
                        ┌────────────────┐
                        │ Phase 4        │
                        │ Synthesis      │
                        │ Unified Paper  │
                        └───────┬────────┘
                                ▼
                        ┌────────────────┐
                        │ Phase 5        │
                        │ Publication &  │
                        │ Dissemination  │
                        └────────────────┘

Dependencies:
  Phase 1 ═╦═ Phase 3 (M-property relies on Cancellation formalization)
           ║
  Phase 2 ═╝  (Observer analysis must reference M-property)
  Phase 4 ←── Phases 1+2+3 (synthesis of all three)
  Phase 5 ←── Phase 4 (publish after synthesis complete)
```

---

## §1. Phase 0: Repository & Infrastructure Setup

| Task ID | Task | Input | Output | Effort | Verification |
|---------|------|-------|--------|--------|-------------|
| **0.1** | Create GitHub repo `cancellation-rule-research` | Handoff doc | Public repo on feature branch | 15 min | `gh repo view` succeeds |
| **0.2** | Create GitHub repo `s10-observer-research` | Handoff doc | Public repo on feature branch | 15 min | `gh repo view` succeeds |
| **0.3** | Copy handoff docs into respective repos as `PROJECT-PLAN.md` | Existing handoff files | PROJECT-PLAN.md in each repo | 10 min | `Test-Path` confirms |
| **0.4** | Write `README.md` for each repo with thesis, RQs, Zenodo DOI placeholder | Handoff content | Two README.md files | 20 min | Read-back verified |
| **0.5** | Create `.gitignore` (from research skill template) in each repo | Research skill template | `.gitignore` in each repo | 5 min | File present |
| **0.6** | Pre-reserve Zenodo concept DOIs for both projects | ZENODO_TOKEN | Two concept DOIs recorded in `.zenodo_versions.json` | 15 min | `curl -sI https://doi.org/...` → 200 |
| **0.7** | R2 archive: upload all Phase 0 files to `qnfo-projects/<repo>/` | Local files | R2 objects verified | 10 min | Round-trip download check |
| **0.8** | Commit, push, tag both repos as `v0.1-phase0` | Clean working trees | Tags on GitHub | 10 min | `git ls-remote --tags origin` |

**Phase 0 close-out tag:** `v0.1-phase0` on each repo.

### Social Media — Phase 0 Announcement

| Platform | Post |
|----------|------|
| **Twitter/X** | "New: 'The Measurement Boundary' — a two-pronged research program investigating (1) Spencer-Brown's Cancellation Rule and the ontology of boundary-crossing, and (2) the Observer Inside vs. Outside schism in physics. Both spin off from the 29-Schisms Deep-Dive (DOI: 10.5281/zenodo.21469000). Repos live, handoffs ingested. #QNFO #FoundationsOfPhysics #LawsOfForm" |
| **LinkedIn** | Same + professional framing: research program launch, methodology description, call for peer review |
| **Bluesky** | Same as Twitter/X |

---

## §2. Phase 1: Cancellation Rule Deep-Dive

**Repo:** `cancellation-rule-research`
**Handoff:** `HANDOFF-cancellation-rule-research-project.md` (6 RQs, bibliography)
**Duration:** 3-4 sessions (estimate: 6-8 LLM-hours)
**Deliverable:** `paper-cancellation-rule.md` + `paper-cancellation-rule.pdf`

### §2.1 Literature Review (Session 1)

| Task ID | Task | Source | Output | Effort |
|---------|------|--------|--------|--------|
| **1.1** | Read Spencer-Brown (1969) *Laws of Form*, Chapters 1-4 (distinction, calling, crossing, primary algebra) | External: Bantam edition / available online | Annotated notes in `artifacts/literature-sb-primary.md` | 2 hr |
| **1.2** | Survey secondary literature: Kauffman (1995, 2012), Bricken (1986, 2019), Varela (1975) on autopoiesis and LOF | arXiv, Semantic Scholar, web | `artifacts/literature-lof-secondary.md` — classified core/supporting/background | 2 hr |
| **1.3** | Cross-reference with QNFO: "Quantum Laws of Form" (DOI: 10.5281/zenodo.19578015), STC Research Plan, PBO v1.0 | QNFO Vectorize + D1 | `artifacts/literature-qnfo-crossref.md` | 1 hr |
| **1.4** | Search arXiv + Semantic Scholar for: "cancellation rule" + "boundary crossing" + "distinction" + "measurement" + "Laws of Form" | External APIs | Annotated bibliography, 10-20 papers | 1.5 hr |
| **1.5** | Classify all found papers per research skill protocol (core/supporting/background) | Output from 1.1-1.4 | Classification matrix table | 0.5 hr |

**Phase 1.1 close-out tag:** `v0.2-phase1-lit`

### §2.2 Formal Analysis (Session 2)

| Task ID | Task | Input | Output | Effort |
|---------|------|-------|--------|--------|
| **1.6** | **RQ1:** Formalize "crossing" — write rigorous definition of what the mark ● encodes ontologically. Is it an instruction, a state, or both? | Literature from 1.1-1.2 | `artifacts/analysis-crossing-definition.md` | 2 hr |
| **1.7** | **RQ2:** Characterize the void (∅) — "staying put" vs. "nothingness." Trace Spencer-Brown's own development from 1969 through secondary readings. | 1.1 + Kauffman/Bricken | `artifacts/analysis-void-ontology.md` | 1.5 hr |
| **1.8** | **RQ3:** Does cancellation imply boundaries don't exist? Formal treatment: when does a boundary persist vs. cancel? Prove: boundary + single crossing → void; boundary + more-than-single-crossing → no cancellation. | Formal proof from §2.2 analysis | `artifacts/analysis-cancellation-boundary-persistence.md` | 1.5 hr |
| **1.9** | **RQX (bonus):** Is [●] → ∅ the ONLY possible reduction rule for a single crossing? Explore alternative reduction systems (linear logic, combinatory logic, process calculi) | External lit from 1.4 | `artifacts/analysis-alternative-reduction-systems.md` | 1.5 hr |
| **1.10** | Write formalized section of paper: "The Cancellation Rule — Formal Definition and Ontological Consequences" (§2-3 of paper) | 1.6-1.9 | `paper-cancellation-rule.md` §2-3 drafted | 2 hr |

**Phase 1.2 close-out tag:** `v0.3-phase1-formal`

### §2.3 The M-Property Boundary (Session 3)

| Task ID | Task | Input | Output | Effort |
|---------|------|-------|--------|--------|
| **1.11** | **RQ4:** Is "boundary = measurement" (the M-property) justified? Trace the origin of this claim in the QNFO corpus. Does it follow from Spencer-Brown or is it an added interpretation? | "Quantum Laws of Form" + PBO v1.0 + 29-schisms synthesis | `artifacts/analysis-m-property-justification.md` | 2 hr |
| **1.12** | **RQ5:** Confluence proof audit. Verify Spencer-Brown's Church-Rosser proof. Are there edge cases the proof misses? Does the proof hold for infinite expressions? | Spencer-Brown Ch. 2-3 + secondary verification | `artifacts/analysis-confluence-verification.md` | 1 hr |
| **1.13** | **RQ6:** Consistency of (C, X, D) under interpretation-switching. If boundaries encode measurement, do the rules remain confluent when measurement outcomes are non-deterministic? | 1.11 + 1.12 | `artifacts/analysis-consistency-measurement-interpretation.md` | 1.5 hr |
| **1.14** | Write remaining paper sections: M-property justification (§4), consistency proof (§5), limitations and alternatives (§6) | 1.11-1.13 | `paper-cancellation-rule.md` §4-6 drafted | 2 hr |

**Phase 1.3 close-out tag:** `v0.4-phase1-m-property`

### §2.4 Paper Finalization (Session 4)

| Task ID | Task | Output | Effort |
|---------|------|--------|--------|
| **1.15** | Write abstract, introduction (§1), conclusion (§7) | `paper-cancellation-rule.md` complete | 1 hr |
| **1.16** | Red-team audit of paper: 5 adversary roles, edge case testing | `artifacts/red-team-cancellation-paper.md` | 1 hr |
| **1.17** | Address red-team findings; iterate paper | Paper v2.0 | 1 hr |
| **1.18** | Build paper.md -> paper.pdf (tectonic or XeLaTeX, whichever is available) | `paper-cancellation-rule.pdf` | 0.5 hr |
| **1.19** | Verify PDF: zero `\ufffd` replacement chars, zero empty pages | Preflight check passed | 0.25 hr |

**Phase 1 close-out tag:** `v1.0-cancellation-paper`

### §2.5 Publication

| Task ID | Task | Effort |
|---------|------|--------|
| **1.20** | Zenodo deposit: upload paper.md + paper.pdf + PROVENANCE-BUNDLE.zip | 0.5 hr |
| **1.21** | Set metadata: title, author, abstract, license (CC-BY-4.0), related_identifiers | 0.25 hr |
| **1.22** | Publish; verify DOI resolves (curl -sI https://doi.org/...) | 0.25 hr |
| **1.23** | R2 archive sync + GitHub push + tag `v1.0-published` | 0.25 hr |

**Phase 1 publication DOI:** `10.5281/zenodo.<TBD>`

---

## §3. Phase 2: S10 Observer Deep-Dive

**Repo:** `s10-observer-research`
**Handoff:** `HANDOFF-s10-observer-inside-outside-research-project.md` (5 RQs, bibliography)
**Duration:** 3-4 sessions (estimate: 6-8 LLM-hours)
**Deliverable:** `paper-s10-observer.md` + `paper-s10-observer.pdf`

### §3.1 Literature Review (Session 1)

| Task ID | Task | Source | Output | Effort |
|---------|------|--------|--------|--------|
| **2.1** | Deep-read Rovelli's Relational QM: foundational papers (1996, 2004, 2018) + "Helgoland" (2020) | arXiv + published works | `artifacts/literature-rqm-deep.md` | 2 hr |
| **2.2** | Deep-read QBism: Fuchs (2010, 2014, 2023), Mermin (2012), von Baeyer (2016) | arXiv + Semantic Scholar | `artifacts/literature-qbism-deep.md` | 2 hr |
| **2.3** | Read Ismael: "The Situated Self" (2007), "How Physics Makes Us Free" (2016), "Time: A Very Short Introduction" (2021) | Published books + reviews | `artifacts/literature-ismael-deep.md` | 1.5 hr |
| **2.4** | Read Deutsch/Marletto: Constructor Theory papers (2014, 2016, 2021, 2025) — competing resolution of S19 | arXiv | `artifacts/literature-ct-deep.md` | 1.5 hr |
| **2.5** | Survey: "observer problem in physics" — broader lit scan (Semantic Scholar + web) | Semantic Scholar API + web | `artifacts/literature-observer-broad.md` — 15-30 papers classified | 1.5 hr |
| **2.6** | Cross-reference QNFO: 29-schisms synthesis §2.5 (S10), calibration map C definition, trajectory-local Bootstrap paper | QNFO repo + D1 | `artifacts/literature-qnfo-observer-crossref.md` | 0.5 hr |

**Phase 2.1 close-out tag:** `v0.2-phase2-lit`

### §3.2 Critical Analysis (Session 2)

| Task ID | Task | Input | Output | Effort |
|---------|------|-------|--------|--------|
| **2.7** | **RQ1 (CRITICAL):** Does "observer = node in TREE" eliminate external vantage point or relocate it? Formal analysis of the DIST function circularity: who computes ANCESTOR(A,B)? Does that computation require global tree knowledge? | 2.6 + calibration map C definition | `artifacts/analysis-dist-circularity.md` — the core deliverable of this phase | 2.5 hr |
| **2.8** | **RQ2:** Comparison to RQM's observer treatment. Does Rovelli's framework have the same circularity? Map RQM's "relational state" to TREE's "DIST computation." | 2.1 + 2.7 | `artifacts/analysis-rqm-comparison.md` | 1.5 hr |
| **2.9** | **RQ3:** Comparison to QBism. Does Fuchs's "participatory realism" resolve the observer position without formal mechanisms? Is the 29-schisms framework over-engineered relative to QBism? | 2.2 + 2.7 | `artifacts/analysis-qbism-comparison.md` | 1.5 hr |
| **2.10** | **RQ4:** Comparison to situated cognition (Ismael). The "situated self" vs. the "node in TREE" — what does each framework gain/lose? | 2.3 + 2.7 | `artifacts/analysis-ismael-comparison.md` | 1 hr |
| **2.11** | **RQ5:** Comparison to Constructor Theory (Deutsch/Marletto). Counterfactual vs. ultrametric — competing resolutions of S19. Is CT lighter but sufficient? | 2.4 | `artifacts/analysis-ct-comparison.md` | 1 hr |

**Phase 2.2 close-out tag:** `v0.3-phase2-critical`

### §3.3 Integration (Session 3)

| Task ID | Task | Output | Effort |
|---------|------|--------|--------|
| **2.12** | Build comparison matrix: RQM vs. QBism vs. Ismael vs. CT vs. 29-schisms — schism-by-schism coverage, assumption count, mechanism weight | `artifacts/comparison-matrix-observer-frameworks.md` | 1 hr |
| **2.13** | Draft paper §2-5: the observer problem in physics, competing frameworks, DIST circularity analysis, comparison matrix | `paper-s10-observer.md` §2-5 drafted | 2.5 hr |
| **2.14** | Red-team the DIST circularity argument: try to rescue it. Is there a reformulation where ANCESTOR is locally computable (node-local traversal rather than global tree query)? | `artifacts/red-team-dist-circularity.md` | 1.5 hr |
| **2.15** | Draft paper §6-7: if circularity is unresolved, what does this mean for the 29-schisms framework? Honest limitations section. | `paper-s10-observer.md` §6-7 drafted | 1.5 hr |

**Phase 2.3 close-out tag:** `v0.4-phase2-integration`

### §3.4 Finalization + Publication

| Task ID | Task | Effort |
|---------|------|--------|
| **2.16** | Write abstract, intro, conclusion | 1 hr |
| **2.17** | Red-team audit of full paper | 1 hr |
| **2.18** | Build PDF (tectonic/XeLaTeX) + verify | 0.5 hr |
| **2.19** | Zenodo deposit + publish | 0.5 hr |
| **2.20** | R2 archive + GitHub push + tag `v1.0-published` | 0.25 hr |

**Phase 2 publication DOI:** `10.5281/zenodo.<TBD>`

---

## §4. Phase 3: The M-Property Bridge

**Repo:** Either `cancellation-rule-research` or a new `m-property-bridge` repo
**Duration:** 2 sessions (estimate: 3-4 LLM-hours)
**Deliverable:** `paper-m-property-bridge.md` + `paper-m-property-bridge.pdf`

**Purpose:** The M-property ("boundary encodes measurement") is the central interpretive move connecting the Cancellation Rule to the S10 Observer claim. This phase subjects it to independent, rigorous evaluation.

### §4.1 Formal Analysis (Session 1)

| Task ID | Task | Input | Output | Effort |
|---------|------|-------|--------|--------|
| **3.1** | Formalize the M-property precisely: given a container [S₁...Sₖ M], what EXACTLY does it mean for M to be "measurement outcome" and S₁...Sₖ to be "system state"? | Calibration map C v2.1 definition | `artifacts/m-property-formal-definition.md` | 1.5 hr |
| **3.2** | Trace the M-property's origin in the QNFO corpus: where was it first stated? What justification was given? Has it been questioned? | QNFO papers (QLoF, STC, PBO, 29-schisms) | `artifacts/m-property-corpus-trace.md` | 1 hr |
| **3.3** | Does Spencer-Brown's calculus FORCE the M-property? Or is it neutral — just as compatible with "boundary = logical grouping" or "boundary = syntactic namespace"? | Spencer-Brown Ch. 1-2 + formal analysis | `artifacts/m-property-spencer-brown-neutrality.md` | 1.5 hr |
| **3.4** | T1 resolution: The M-property is an INTERPRETIVE LAYER. Determine under what conditions it's justified and under what conditions it's an arbitrary convention. | 3.1-3.3 | `artifacts/m-property-justification-conditions.md` | 1 hr |

**Phase 3.1 close-out tag:** `v0.2-phase3-formal`

### §4.2 Synthesis Paper (Session 2)

| Task ID | Task | Output | Effort |
|---------|------|--------|--------|
| **3.5** | Draft paper: §1 Introduction, §2 Formal definition, §3 Corpus trace, §4 Spencer-Brown neutrality, §5 Justification conditions, §6 Implications for Cancellation Rule and S10 Observer papers | `paper-m-property-bridge.md` | 2 hr |
| **3.6** | Red-team + iterate | Paper v2.0 | 0.5 hr |
| **3.7** | Build PDF + Zenodo publish + R2 + GitHub | Published | 0.5 hr |

**Phase 3 publication DOI:** `10.5281/zenodo.<TBD>`

---

## §5. Phase 4: Synthesis — Unified Paper

**Repo:** `measurement-boundary-synthesis` (new) or `29-schisms-deepdive` (append)
**Duration:** 2 sessions (estimate: 3-4 LLM-hours)
**Deliverable:** `paper-measurement-boundary-synthesis.md` + PDF

**Purpose:** Unify the three prior papers into a single comprehensive account.

| Task ID | Task | Input | Output | Effort |
|---------|------|-------|--------|--------|
| **4.1** | Extract key findings from Phase 1-3 papers into a comparison matrix: what each paper proved, what remained open, how they connect | Published Phase 1-3 DOIs | `artifacts/synthesis-cross-matrix.md` | 1 hr |
| **4.2** | Address T1-T3 (the three unresolved tensions from the DESIGN RESEARCH gap analysis) | 4.1 + prior papers | T1-T3 resolved or honestly acknowledged as open | 1.5 hr |
| **4.3** | Write unified paper: §1 Introduction, §2 Cancellation Rule, §3 S10 Observer, §4 M-Property Bridge, §5 Synthesis — How They Connect, §6 Unresolved Questions, §7 Conclusion | All prior papers | `paper-measurement-boundary-synthesis.md` | 3 hr |
| **4.4** | Red-team + iterate | | | 1 hr |
| **4.5** | Build PDF + Zenodo publish + R2 + GitHub | | | 0.5 hr |

**Phase 4 publication DOI:** `10.5281/zenodo.<TBD>`

---

## §6. Phase 5: Dissemination & Social Media Campaign

### §6.1 Publication Stack

| Task ID | Task | Effort |
|---------|------|--------|
| **5.1** | Update all 4 Zenodo deposits with cross-references (`isSupplementedBy`, `cites`) to each other | 0.5 hr |
| **5.2** | Update the 29-schisms-deepdive synthesis paper Appendix to cite all 4 papers | 0.5 hr |
| **5.3** | D1 living-paper insert for all 4 papers (or update `search_papers` index) | 0.5 hr |
| **5.4** | arXiv cross-posting (if applicable — verify account/permissions) | 0.5 hr |

### §6.2 Social Media Dissemination Schedule

**Campaign: "The Measurement Boundary" — 4-week rollout across Twitter/X, LinkedIn, Bluesky**

#### Week 1: Phase 1 Paper Release — "The Ontology of Boundary-Crossing"

| Platform | Post |
|----------|------|
| **Twitter/X** | "What does it MEAN to 'cross a boundary'? Spencer-Brown's Cancellation Rule [●]→∅ is one of the most elegant — and least understood — primitive operations in formal systems. Our new paper defends its ontology: boundary + single crossing = void. But boundaries with more structure PERSIST. DOI: [TBD] #LawsOfForm #Ontology #QNFO" |
| **LinkedIn** | Professional summary: 200-word abstract, methodology, key findings, link to Zenodo DOI |
| **Bluesky** | Same as Twitter/X |

#### Week 2: Phase 2 Paper Release — "Inside or Relocated? The Observer-as-Node Claim Under Scrutiny"

| Platform | Post |
|----------|------|
| **Twitter/X** | "Can you eliminate the 'View from Nowhere' by making the observer a node in a tree? Our new paper says: maybe not. The DIST function that encodes 'observation' requires ANCESTOR(A,B) — a global tree operation. Who performs that computation? If it's an external agent, the vantage point just got relocated. DOI: [TBD] #FoundationsOfPhysics #RQM #QBism #QNFO" |
| **LinkedIn** | Professional summary: 200-word abstract, comparison to Rovelli's RQM and Fuchs's QBism, honest limitations |
| **Bluesky** | Same as Twitter/X |

#### Week 3: Phase 3 Paper Release — "Boundary as Measurement: Justifying the M-Property"

| Platform | Post |
|----------|------|
| **Twitter/X** | "The 29-schisms framework's central interpretative move: 'a boundary encodes measurement.' But was this justified? Our new paper traces the M-property's origin through the QNFO corpus — and finds it was ASSERTED, not PROVED. Spencer-Brown's calculus is neutral: a boundary can encode measurement, logical grouping, or syntactic namespace equally well. DOI: [TBD] #FoundationsOfFormalSystems #QNFO" |
| **LinkedIn** | Professional summary with implication for framework validity |
| **Bluesky** | Same as Twitter/X |

#### Week 4: Synthesis Paper + Campaign Close

| Platform | Post |
|----------|------|
| **Twitter/X** | "Threading the Needle, Part II: Four papers. One question. Does putting the observer inside the formal system actually work — or does it just relocate the problem? Spoiler: the Cancellation Rule, the M-Property, and the Observer-As-Node move are all creative interpretations — none are FORCED by the calculus. Full synthesis: DOI: [TBD] #QNFO #ResearchSummary" |
| **LinkedIn** | Long-form synthesis post: program overview, 4 papers linked, open questions, call for peer review |
| **Bluesky** | Thread: 4 tweets summarizing each paper, followed by synthesis |

### §6.3 Buffer API Configuration

| Platform | channelId | Profile |
|----------|-----------|---------|
| Twitter/X | `674ca9af22f5c1c91afb6c5c` | @QNFOResearch |
| LinkedIn | `674ca8c822f5c1c91afb6c58` | QNFO Research |
| Bluesky | `674ca9d022f5c1c91afb6c5e` | @qnfo.bsky.social |

Token: `%USERPROFILE%\buffer\token` (standard location).

All posts use `status: SCHEDULED`, `now: false`, `utc: false`. Schedule: Mondays at 14:00 UTC for optimal engagement.

---

## §7. LLM Execution Protocol

### §7.1 Session Format

Each phase is designed for one LLM session. At session start:

```
TASK: Execute Phase N of WBS-CANCELLATION-S10-RESEARCH-PROGRAM.md
STATE: [repo], branch [feature/phaseN], prior phase tag [vX.Y-phaseZ-slug]
CONTEXT: Read PROJECT-PLAN.md (handoff doc) + prior phase artifacts
R2: qnfo-projects/<repo>/ — all files synced
WBS: WBS-CANCELLATION-S10-RESEARCH-PROGRAM.md, Phase N tasks
```

### §7.2 Per-Task Verification

Every task in this WBS has a concrete verification step:
- **File creation:** `Test-Path` confirms existence
- **DOIs:** `curl -sI https://doi.org/...` → HTTP 200
- **R2:** Round-trip download + size/hash comparison
- **Git:** `git log -1 --oneline` + `git ls-remote origin`
- **PDF:** `scripts/check-pdf.py` — zero `\ufffd`, zero empty pages
- **Social media:** Buffer GraphQL response `status: SCHEDULED`

### §7.3 Anti-Phantom Gate (MANDATORY)

Per the core skill mandate (2026-07-21), NO claim of "published," "uploaded," "verified," or "done" without an INDEPENDENT re-query of live state in the SAME turn. The API's `201 Created` response is the FIRST signal, not the LAST.

---

## §8. Summary — Complete Task Register

| Phase | Tasks | Papers | Repo | DOI |
|-------|-------|--------|------|-----|
| 0 | 8 tasks | — | 2 repos created | 2 concept DOIs |
| 1 | 23 tasks | Cancellation Rule | `cancellation-rule-research` | `<TBD>` |
| 2 | 20 tasks | S10 Observer | `s10-observer-research` | `<TBD>` |
| 3 | 7 tasks | M-Property Bridge | `m-property-bridge` or Phase 1 repo | `<TBD>` |
| 4 | 5 tasks | Synthesis | `measurement-boundary-synthesis` or 29-schisms-deepdive | `<TBD>` |
| 5 | 4 tasks | Dissemination | — | — |
| **Total** | **67 tasks** | **4 papers** | **2-4 repos** | **4-6 DOIs** |

### Critical Path

```
Phase 0 (repos) → Phase 1 (Cancellation) → Phase 3 (M-Property) → Phase 4 (Synthesis) → Phase 5 (Dissemination)
                                            ↑
Phase 0 (repos) → Phase 2 (S10 Observer) ──┘
```

Phases 1 and 2 can run in PARALLEL (different repos, independent research). Phase 3 requires Phase 1 (it references the Cancellation formalization). Phase 4 requires all three. Phase 5 requires Phase 4.

---

## §9. Next-Session Immediate Tasks

| Priority | Task | Session | Blocker |
|----------|------|---------|---------|
| **1** | Phase 0 Task 0.1: Create `cancellation-rule-research` GitHub repo | New session | None |
| **2** | Phase 0 Task 0.2: Create `s10-observer-research` GitHub repo | New session | None |
| **3** | Phase 0 Task 0.3-0.8: Complete infrastructure setup for both repos | New session | 0.1-0.2 |
| **4** | Phase 1 Task 1.1: Begin Spencer-Brown primary exegesis | New session (after Phase 0) | Phase 0 complete |
| **5** | Phase 2 Task 2.1: Begin RQM deep-read | New session (can run in parallel with Phase 1) | Phase 0 complete |

**Continuation prompt for Phase 0:**
```
TASK: Execute Phase 0 of WBS-CANCELLATION-S10-RESEARCH-PROGRAM.md
      — create both GitHub repos, ingest handoff documents as
      PROJECT-PLAN.md, pre-reserve Zenodo concept DOIs,
      R2 archive, tag v0.1-phase0 on each repo.

STATE: 29-schisms-deepdive v2.3 (DOI 10.5281/zenodo.21469000).
       Two handoff docs exist at qnfo-projects/29-schisms-deepdive/.

CONTEXT: Read WBS-CANCELLATION-S10-RESEARCH-PROGRAM.md §1 (Phase 0 tasks)
         Read HANDOFF-cancellation-rule-research-project.md
         Read HANDOFF-s10-observer-inside-outside-research-project.md

R2 path for new repos: qnfo-projects/cancellation-rule-research/
                         qnfo-projects/s10-observer-research/

WBS: 8 tasks, all executable, no blockers.
```
