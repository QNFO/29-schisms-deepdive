# Red Team Audit + Task Verification + Session Closeout
## 29-Schisms Deep-Dive — v1.2 Phase Closeout

**Date:** 2026-07-20
**Scope:** WBS-NEXT-PHASES.md, competitor-analysis-qbism-cdt.md, publication infrastructure (Zenodo/GitHub/R2)
**Method:** 5 adversary roles + infrastructure verification + task execution audit

---

## PART 1: RED TEAM — WBS-NEXT-PHASES.md

### R1: Null-Hypothesis Defender

**Attack on Phase 1 (Bootstrap Proof) effort estimates:** The WBS estimates 3-6 months for a formal proof, broken into tasks of 2-4, 4-8, 2-4, and 4-12 weeks. This is **pure guesswork disguised as planning.** No prior art exists for defining a "calibration map" on this specific expression algebra. The effort estimate has no basis — it could take 2 weeks or 2 years or turn out to be impossible (undecidable). Presenting a range (3-6 months) implies confidence that isn't earned.

**Verdict: MODERATE.** Effort estimates for genuinely novel mathematical work are inherently unfalsifiable-in-advance. Should be labeled `[speculative estimate, no comparable precedent]`.

### R2: Methodology Skeptic

**Attack on Task 1.4 (Characterize Valuation Structure):** The task description says "compare derived branching factors to the executable tree growth pattern (1→2→2→3→7→28→125→588)." This is **backwards reasoning disguised as validation.** The tree growth pattern was produced by ONE arbitrary choice of expression algebra (marks + containers with 3 specific reduction rules). If the "derived branching factors" from the Bootstrap proof don't match, the WBS gives no criterion for whether that means (a) the proof is wrong, (b) the toy algebra was the wrong model, or (c) both are valid but describe different things. This validation step is underspecified to the point of being unfalsifiable.

**Verdict: HIGH.** Task 1.4 needs an explicit pre-registered decision rule: what specifically would count as a match vs. mismatch, and what action follows each outcome.

**Attack on Phase 2 (Taxonomy Validation):** The WBS calls for "3-5 qualified external researchers" but provides no recruitment strategy, no compensation plan, and no fallback if validators decline (which is likely — foundations-of-physics researchers reviewing an unpublished, non-peer-reviewed 29-schism taxonomy from an unfamiliar research program is a significant time ask with no professional incentive).

**Verdict: HIGH.** Phase 2 as written has a near-certain risk of stalling indefinitely (Task 2.3 estimates "4-8 weeks waiting for responses" — this assumes responses arrive at all).

### R3: Better-Alternative Proposer

**Attack on Phase 5 (GUF-to-Adelic Bridge):** The WBS itself rates this "LOW FEASIBILITY" and estimates 6-18 months for what might be pure numerology (|χ|=6 = 2×3 is explicitly flagged as numerology in the deep-dive research doc, §5.1: "This is speculation dressed as a program"). Why is a LOW-feasibility, self-acknowledged-numerology task still in the WBS as Phase 5 rather than deprioritized to a backlog?

**Verdict: MODERATE.** Recommend moving Phase 5 out of the primary WBS into a "Speculative/Backlog" section, since committing WBS phase numbering to it implies more confidence than the framework itself claims.

### R4: Scaling Pessimist

**Attack on Phase 3 (Trapped-Ion) resource estimate:** "~$50K (lab time)" is stated with no sourcing. Beam time costs vary enormously by institution (university core facility vs. national lab vs. industry). No lab has been contacted (Task 3.2 is "Secure Lab Access" — still TODO). The $50K figure appears to be invented rather than researched.

**Verdict: HIGH.** All cost estimates in the "Resource Requirements Summary" table are unsourced guesses presented in a table format that implies rigor they don't have.

### R5: Resource Realist

**Attack on the Dependency Graph:** The graph shows Phase 1 (Bootstrap Proof) as blocking/informing Phases 3, 4, 5 via arrows, but the WBS body text for Phases 3 and 4 does NOT list Phase 1 as a dependency — Tasks 3.1 (OSF pre-registration) and 4.1 (pipeline development) are described as startable immediately ("Ready? ✅ Now" in the Next Session table). This is an **internal inconsistency**: the dependency graph and the task tables disagree about whether Phase 1 gates Phases 3-4.

**Verdict: MODERATE.** Either the experiments genuinely don't depend on the Bootstrap proof (in which case the graph is wrong and should show them as independent), or they do depend on it (in which case starting OSF pre-registration "now" is premature). This needs to be resolved, not left ambiguous.

---

## PART 2: RED TEAM — competitor-analysis-qbism-cdt.md

### R1: Null-Hypothesis Defender

**Attack on the "combined coverage" arithmetic:** §3 claims "If we COMBINE QBism + CDT... Total: maybe 15/29 schisms" but the scorecards given are QBism 6.5/29 and CDT 6.5/29, with only S26 (many-worlds) and possibly S7 (Born rule) as overlapping partial credits between them. 6.5 + 6.5 = 13, not 15, even before removing double-counted overlaps. The "maybe 15" figure appears to include an unstated "+ standard QM covers quantum dynamics (Layer 2-3, partially)" bonus that is not scored anywhere else in the document with a number.

**Verdict: MODERATE.** Arithmetic inconsistency. Either show the standard-QM contribution as an explicit scored line item, or correct "15" to "~13."

### R2: Methodology Skeptic

**Attack on scoring consistency between this document and the original red-team-audit:** The original red-team-audit-29-schisms-2026-07-20.md (H2 finding) explicitly criticized the synthesis for evaluating GUF as "≤15/29 schisms" WITHOUT a schism-by-schism table, calling this "asymmetric" and "self-serving." This competitor-analysis document DOES provide schism-by-schism tables for QBism and CDT — good, this addresses H3/H4 as intended. But it does NOT go back and produce the missing GUF schism-by-schism table that H2 demanded. The GUF "~15/29 (estimated)" figure is repeated in §3's Comparative Scorecard with the same unsubstantiated "estimated" qualifier that was flagged as a problem in the original audit.

**Verdict: HIGH.** H2 from the original red team audit is only half-closed. QBism and CDT got rigorous treatment; GUF did not, in the same document that compares all three.

### R3: Better-Alternative Proposer

**Attack on missing competitors:** This document only evaluates QBism and CDT. It does not evaluate: Bohmian mechanics (resolves S7, S17, S26 via a hidden-variable ontology with a single pilot wave — arguably the OLDEST "lighter alternative" to standard QM), Everettian many-worlds without QBism's belief-based gloss (directly addresses S17, S26, S21), objective collapse models (GRW/CSL — directly addresses S5, S7, S20), Rovelli's Relational QM (addresses S10, S21, S25 — arguably closer competition to Layer 5 than QBism, and the 29-schism paper's own §2.5 references "Relational QM" without crediting Rovelli by name), or Constructor Theory (Deutsch/Marletto — directly targets S16, S19, the exact schisms the needle-threading framework calls its "central layer").

**Verdict: CRITICAL.** Constructor Theory is the single most concerning omission: it was purpose-built to address S19 (the user's original entry-point schism — separating "possible/impossible" statements from dynamical laws) using a completely different, comparatively lightweight formalism (counterfactual statements about physical transformations). A competitor analysis that evaluates QBism (Layer 5) and CDT (Layer 4) but skips Constructor Theory (Layer 2, exactly where Schism 19 lives) has evaluated the two EASIEST comparisons and skipped the hardest, most relevant one.

### R4: Scaling Pessimist

**Attack on the "synthesis opportunity" claims:** §1.5 and §2.5 each propose injecting QBism/CDT insights into the needle-threading framework "without adding mathematical weight." No mechanism is given for how a Hilbert-space-based interpretation (QBism) integrates into a Bruhat-Tits-tree-based ontology, or how a simplicial-complex path integral (CDT) integrates into a static-tree self-referential-calibration framework. These are stated as aspirations, not plans.

**Verdict: MODERATE.** Consistent with the broader pattern (also flagged in the original red-team's L2 finding about the GUF-adelic bridge) of proposing cross-framework bridges as one-sentence "opportunities" without any worked mathematics.

### R5: Resource Realist

**Attack on §5 falsification conditions:** The three falsification conditions in §5 are all "X is shown to..." with no actor, timeline, or evidentiary standard specified — contrast this with the rigor of the main synthesis's falsifiability register (§6 of deepdive-research doc), which has dated `[CHECK: YYYY]` entries. This document's falsification section reads as an afterthought.

**Verdict: LOW.** Cosmetic/structural inconsistency with the project's own established calibration-register convention.

---

## PART 3: INFRASTRUCTURE AUDIT (Task Execution Verification)

### Finding I-1: Zenodo Version Chain Is Fragmented — CRITICAL

**Evidence (this session, verified live):**
```
Concept 21460404 -> v1.0 (21460405)  STATE: done, resolves HTTP 200
                     v1.1 (21465629)  STATE: 404 NOT FOUND
Concept 21460735 -> v1.2 (21460736)  STATE: done, resolves HTTP 200
```

**Diagnosis:** v1.2's metadata declares `"isNewVersionOf": "10.5281/zenodo.21465629"` (v1.1), but v1.1 no longer resolves. Worse, v1.2 was NOT created via Zenodo's `actions/newversion` API against the v1.0/v1.1 concept (21460404) — it was created as a **brand-new, disconnected deposit** with its own concept DOI (21460735). This means:

- There are now **two separate concept-DOI chains** for what is supposed to be ONE project's version history.
- Anyone citing "the concept DOI" for this project will get either v1.0-only (21460404) or v1.2-only (21460735) depending on which they find, with no automatic link between them.
- v1.1's content (which included the C1-C5 red-team fixes) exists only in git history and R2, not at a resolvable Zenodo DOI.

**Root cause:** The v1.2 publish script (`_zenodo_publish_v12.py`, since deleted per JIT ephemeral-script rules) called `POST /deposit/depositions` (create new) rather than `POST /deposit/depositions/{v1.1_id}/actions/newversion` (chain from existing). This is exactly the anti-pattern the `research` skill's Zenodo Versioning protocol (§ "Zenodo Versioning for Phase/Session Conclusions") was written to prevent — using `related_identifiers: isNewVersionOf` as a citation-only pointer instead of the actual API-level version chain.

**Impact:** MODERATE-HIGH. Not data loss (all content is safe in git + R2 + the two live Zenodo records), but a citation/discoverability fragmentation that will need manual remediation and will confuse future readers trying to find "the latest version."

**Remediation (deferred to next session, documented in updated WBS below):** Cannot merge concept DOIs after the fact via API. Options: (a) accept the fragmentation and clearly cross-link both concept DOIs in all future metadata/READMEs (cheapest, recommended), or (b) contact Zenodo support to request a manual merge (uncertain, slow). Recommend (a).

### Finding I-2: README.md Content Drift — HIGH

**Evidence:** Current `README.md` (verified this session) still states:
- DOI: 10.5281/zenodo.21460405 (v1.0 — should be v1.2: 21460736)
- "The Bootstrap 'Theorem' is a conjecture — the single largest gap (CRITICAL C1)" — this is v1.0 pre-fix language; the actual fix (C1 resolved: Bootstrap Conjecture, explicitly labeled) is not reflected
- "Tree growth is super-exponential" — this was the ORIGINAL (incorrect) red-team claim that v1.1 explicitly REVERSED (growth is exponential ~4.7x, not super-exponential) — the README states the disproven claim as current fact
- "DoD Gate: NOT PASSED" — should read "CONDITIONALLY PASSED" per all v1.1/v1.2 commit messages
- Artifact table lists only 7 of 14 files

**Root cause:** A PowerShell `-NoNewline` flag bug (documented twice already in this session's history) corrupted README.md during v1.2 editing at commit `d37be41`; the recovery in `b9b23bf` restored file INTEGRITY (readable content) but recovered from a STALE git blob (`7619df6`'s README, itself only partially updated) rather than re-applying the full set of intended v1.2 edits. The file has been "fixed" twice now for corruption but never fully brought current.

**Impact:** HIGH. This is the single first file any visitor to the GitHub repo or R2 bucket reads. It currently misrepresents the project's own resolved findings as unresolved, and points to the oldest of three DOIs.

**Remediation:** Executed in Part 4 below (same session).

### Finding I-3: Ephemeral Script Hygiene — LOW (self-correcting)

**Evidence:** At audit time, 4 files matched the `_*` ephemeral pattern in the project directory: `_self_descriptive_system.py` (git-tracked, correctly exempted per `.gitignore`'s `!_self_descriptive_system.py` rule), `_tree_growth.py`, `_fix_dois.py`, `_check_zenodo_chain.py` (none git-tracked, correctly excluded, but not yet deleted from local disk at audit time).

**Impact:** LOW. No durability risk (none of these are the sole copy of anything — `_tree_growth.py`'s output was already captured in `f-contractiveness-analysis.md` and `29-schisms-synthesis-deepdive.md` §Tree Growth Asymptotics). Straightforward cleanup item.

**Remediation:** Executed in Part 4 below.

### Finding I-4: No OSF Pre-Registrations Actually Submitted — MODERATE

**Evidence:** `tape_search` for "OSF registration draft_registrations preregistration submit" within this session returns zero hits. Both experimental protocols (trapped-ion, CMB) contain complete "OSF Pre-Registration Template" sections with explicit language "awaiting OSF pre-registration" / "Submit before first data collection." Neither has actually been submitted via the OSF API this session.

**Impact:** MODERATE. Not a defect — the WBS correctly lists "OSF pre-register trapped-ion protocol" and "OSF pre-register CMB search protocol" as pending Next Session Immediate Tasks (items 5-6), so this was never claimed as done. Flagging here only to confirm the audit trail: no phantom claim exists. Templates are ready; actual submission requires the `deepchat_question` user-approval gate per the research skill's OSF protocol (permanent, immutable — cannot be auto-submitted without explicit consent) and is correctly deferred.

### Finding I-5: No Buffer/Social Media Posts Actually Sent — LOW

**Evidence:** `tape_search` for "Buffer GraphQL createDraft social media post publish" returns zero hits this session. The prior session's final summary mentioned a "Buffer Social Media Distribution Plan" with drafted post copy, but no `createDraft` mutation was executed.

**Impact:** LOW. Consistent with the research skill's "Social-promoting every internal WBS phase transition" anti-pattern warning — Buffer/social posts are reserved for FINAL public deliverables, and this project is still mid-stream (DoD Gate conditionally passed, Bootstrap Conjecture unproven). Deferring social dissemination until Phase 1 (Bootstrap proof) concludes is the correct call, not an omission.

---

## PART 4: REMEDIATION EXECUTED THIS SESSION

1. README.md rewritten to reflect true current state (v1.2, all 14 artifacts, C1-C5 resolution status, DoD Gate: CONDITIONALLY PASSED, both Zenodo concept DOIs cross-linked).
2. Zenodo fragmentation documented transparently in README and WBS (Finding I-1) rather than silently ignored.
3. Ephemeral scripts (`_tree_growth.py`, `_fix_dois.py`, `_check_zenodo_chain.py`) deleted post-verification.
4. WBS-NEXT-PHASES.md updated with a new "Phase 0.5: Red-Team Remediation" section (below, in the updated WBS) capturing every finding above as an actionable task with owner/effort, and Phase 5 demoted to a "Speculative Backlog" section per R3 finding.
5. Constructor Theory, Bohmian mechanics, and Relational QM (Rovelli) flagged as required additions to the competitor analysis (new Task 2.5 in updated WBS).

---

## Consolidated Findings Summary

| Grade | Count | Source |
|-------|-------|--------|
| CRITICAL | 2 | Zenodo chain fragmentation (I-1); Constructor Theory omission from competitor analysis (R3) |
| HIGH | 4 | Task 1.4 unfalsifiable validation; Phase 2 recruitment risk; GUF still lacks schism table (H2 unclosed); README content drift (I-2) |
| MODERATE | 6 | Effort-estimate rigor theater; Phase 5 numerology in main WBS; cost-estimate sourcing; dependency-graph/task-table inconsistency; combined-coverage arithmetic; OSF templates unsubmitted (tracked, not a defect) |
| LOW | 2 | Ephemeral script cleanup; falsification-section rigor gap; Buffer posts deferred (tracked, not a defect) |

**DoD Gate for THIS closeout audit: PASSED WITH REMEDIATION.** All CRITICAL and HIGH findings either fixed same-session (I-2, I-3) or converted into explicit, owned WBS tasks (everything else) rather than left as silent gaps.
