# Red-Team Audit: Phase 2 Deliverables (Tasks 2.1, 2.2, Email Infrastructure)

**Audit Date:** 2026-07-20
**Auditor:** QNFO Agent (autonomous red team per §RED-TEAM → DoD → ITERATE → REFINE)
**Target Documents:**
- `taxonomy-validation-package.md` (Task 2.2)
- `validator-outreach-emails.md` (Task 2.2a)
- `external-validator-candidates.md` (Task 2.1)
**Methodology:** Negative verification — simulate validator perspective. Identify all sources of bias. Test QNFO-neutrality claim. Challenge every assumption.

---

## §0. Summary: DoD Gate

| Criterion | Status |
|-----------|--------|
| Red-Team Passed | ❌ **FAILED** — 2 CRITICAL, 5 HIGH, 5 MODERATE, 1 LOW |
| Priming bias eliminated | ❌ All 5 emails prime validators with taxonomy claims |
| QNFO-neutrality verified | ❌ Background section encodes framework's resolution definition |
| Email addresses verified | ❌ Not yet verified against institutional pages |

**BLOCKING. Phase 2 deliverables cannot proceed to validator outreach in current form.**

---

## FINDINGS

---

### CRITICAL

---

#### F-P2-1: Taxonomy Package QNFO-Neutrality Failure — Background Section Encodes Framework's Resolution Definition

**Severity:** CRITICAL
**Document:** `taxonomy-validation-package.md` §2

**The problem text:**
> "In this taxonomy, a schism is 'resolved' not when one side is declared
> correct, but when a theoretical framework dissolves the bifurcation —
> showing that both sides of the apparent dichotomy are aspects of a single
> underlying structure."

**Why it fails QNFO-neutrality:**

This definition of "resolution" is NOT a neutral taxonomic category. It IS the
needle-threading framework's own resolution strategy. The framework claims to
resolve all 29 schisms precisely by showing that each apparent dichotomy is an
artifact of the View from Nowhere and dissolves when the observer is embedded
as a node in the tree. The definition above encodes the framework's answer
into the classification rubric itself.

**The validator's experience:** A validator reads this definition and
immediately recognizes: "Oh, this taxonomy is built by a research program
that claims to dissolve all schisms. The classification exercise is asking me
whether I agree." This transforms the task from independent classification
into framework evaluation — exactly what the instructions say they are NOT
being asked to do.

**Evidence of the bias:** Compare with a neutral definition of "resolved":
- Standard: "The physics community has reached consensus on the answer."
- This taxonomy: "A framework shows both sides are aspects of a single
  underlying structure."

The taxonomy's definition is narrower, more specific, and encodes a particular
resolution mechanism. It's not "resolved" — it's "resolved by our framework."

**Fix:** Replace with: *"Resolved: The question has a well-supported answer
accepted by most researchers in the relevant subfield, OR the question is
no longer considered productive because it was based on a false premise
or conceptual confusion."* This is standard, framework-neutral, and doesn't
encode any specific resolution mechanism.

---

#### F-P2-2: All 5 Emails Prime Validators with Taxonomy Claims — Severe Experimental Design Failure

**Severity:** CRITICAL
**Document:** `validator-outreach-emails.md` §1, all 5 emails

**The problem:** Every email tells the validator what the taxonomy claims
BEFORE asking them to independently classify.

| Email | Priming Text | What It Reveals |
|-------|-------------|-----------------|
| **Maudlin** | "the taxonomy identifies as the 'nomological dualism' schism (S19)" | Names the taxonomy's entry-point schism, frames it as "nomological dualism" |
| **Wallace** | "The taxonomy claims that several schisms — including S26 (single outcome vs. all outcomes) — remain unresolved" | TELLS Wallace the taxonomy's position on the very schism he disputes as an Everettian |
| **Rovelli** | "the taxonomy addresses: the 'View from Nowhere' versus the 'View from Within'... formalizes this as a self-descriptive system where the observer is structurally embedded" | Reveals BOTH the central tension AND the framework's internal mechanism (tree, node, embedding) |
| **Ismael** | "the taxonomy's central claim: that physics must be formulated from within the system it describes" | States the taxonomy's thesis before classification |
| **Marletto** | "The taxonomy proposes an alternative resolution using ultrametric fixed-point geometry and self-referential calibration" | Reveals the mathematical mechanism AND frames it as competing with constructor theory |

**Why this is a CRITICAL failure:** This is a classic experimental design error
— telling subjects what the study claims and then asking them to independently
evaluate. The validator cannot "independently classify" schisms when they've
already been told the taxonomy's position on each one they're most likely to
dispute.

**Specific worst case — Wallace:** The email TELLS Wallace that S26 is
"unresolved" in the taxonomy. Wallace's entire career is built on the claim
that S26 IS resolved (by decoherence + Everett). The email doesn't ask him
to classify S26 — it tells him the taxonomy's classification and asks him
to validate it. He will either (a) reject the entire exercise as biased,
or (b) defensively classify every schism as "resolved by Everett."

**Fix:** Rewrite ALL emails to use a structurally identical template:

```
Dear Professor [Name],

I am writing to invite your independent expert review of a taxonomy
that catalogs 29 unresolved conceptual tensions in the foundations
of physics.

The taxonomy is organized into five thematic layers. Your expertise in
[field] would provide valuable independent classification. The review
involves: [classification task description — ONLY].

We do not describe the taxonomy's own positions or resolution claims
in this email. We seek your independent judgment, not an evaluation of
any specific framework.

[Logistics: time, attachment, timeline, signature]
```

No discussion of "needle-threading," "Bootstrap," "View from Nowhere,"
"ultrametric," or any other framework-internal concept. Period.

---

### HIGH

---

#### F-P2-3: Taxonomy Package Layer Structure IS the Framework's Dependency Stack — Not Neutral

**Severity:** HIGH
**Document:** `taxonomy-validation-package.md` §1

**The 5-layer organization:**
1. Mathematical Substrate
2. Ontology of States and Laws
3. Quantum-Classical Divide
4. Spacetime and Gravity
5. Epistemology and the Observer

**The problem:** This layering IS the needle-threading framework's dependency
stack (Layers 0–4 in the formalization). Presenting it as a neutral
organizational scheme — "schisms are organized into five layers, from
mathematical substrate to epistemology" — frames the framework's architecture
as an objective fact about the schisms.

**What a neutral taxonomy would do differently:**
- Group by topic area (QM foundations, spacetime, statistical mechanics,
  epistemology) without imposing a dependency hierarchy
- Allow validators to suggest alternative groupings
- Label the layers as "suggested groupings" rather than "layers"

**The §2 text compounds this:**
> "The schisms are not randomly selected — they form a dependency stack.
> Layer 1 schisms constrain Layer 2, which constrains Layer 3..."

This language ("not randomly selected," "form a dependency stack") presents
the framework's architectural claim as an established fact. A validator
reading this might reasonably ask: "Says who? What empirical evidence
establishes this dependency?"

**Fix:** Relabel as "Thematic Groups" and add a disclaimer: *"The grouping
into five thematic areas reflects the research program's organizational
hypothesis. Validators are welcome to suggest alternative groupings or to
dispute whether specific schisms belong in their assigned group."*

---

#### F-P2-4: Email Primer Is Delivered Through Personalized Flattery — Compound Bias

**Severity:** HIGH
**Document:** `validator-outreach-emails.md` §1

**The pattern in all 5 emails:**
1. Flatter the validator by engaging their specific work ("Your work on X...
   articulated with precision in Y")
2. State what the taxonomy claims about the schism related to their work
3. Ask them to classify

**The problem:** The personalized engagement is professionally appropriate
(you should show you've read their work), but when combined with the priming
effect (F-P2-2), it creates a compound bias:

Validator reads: "Your brilliant work on X is directly relevant to this
taxonomy, which claims Y." → Validator feels: "This taxonomy either validates
my work (if Y aligns with my view) or challenges it (if Y contradicts me)."
→ Validator classifies defensively, not independently.

**Example — Rovelli email:**
> "Your relational interpretation... engages the central tension the taxonomy
> addresses... This resonates with the perspectival approach you have
> developed."

This tells Rovelli: "Your work is aligned with this taxonomy." He may
then classify more favorably than he otherwise would, to avoid seeming
to reject a framework that "resonates" with his own.

**Fix:** Separate the flattery from the task description. Structure:
1. Paragraph 1: Brief professional acknowledgment (1-2 sentences)
2. Paragraph 2: Description of the validation TASK (no taxonomy claims)
3. Paragraph 3: Logistics

---

#### F-P2-5: Marletto Email Frames Validation as Framework Competition

**Severity:** HIGH
**Document:** `validator-outreach-emails.md` §1, Email 5

**The problem text:**
> "Your classification would provide the most direct competitive evaluation
> of the taxonomy's claims: does the counterfactual approach resolve S19
> more parsimoniously than the self-descriptive approach..."

This explicitly frames the validation exercise as a COMPETITION between two
frameworks (constructor theory vs. needle-threading). The validator is being
asked to act as a judge between competing theories, not as an independent
classifier of schisms.

**Why this matters:** Marletto is a developer of constructor theory. Asking
her to evaluate whether her own framework is "more parsimonious" than an
alternative is asking for a biased response. Even the most honest respondent
cannot be objective about their own work in direct comparison with a
competitor.

**Fix:** The Marletto email should be structurally identical to the others.
Her expertise in constructor theory makes her a valuable validator for S19
and related schisms, but the email should not mention constructor theory's
resolution claims at all — just ask her to classify S19 as she sees it.

---

#### F-P2-6: Email Sending Infrastructure Depends on Unverified Prerequisites

**Severity:** HIGH
**Document:** `validator-outreach-emails.md` §0, §2

**Issues identified:**

1. **research@qnfo.net doesn't exist yet.** The email infrastructure section
   lists `research@qnfo.net` as the sending address, but no steps are
   provided to CREATE this address. Cloudflare Email Service sends FROM
   any address at the onboarded domain, but there's no mailbox or routing
   setup. Replies to `research@qnfo.net` will bounce.

2. **Outlook COM script references external HTML files.** The PowerShell script
   reads `email-maudlin.html`, `email-wallace.html`, etc. — NONE of these
   files exist in the project. The script will fail with file-not-found
   errors on all 5 emails.

3. **Cloudflare Worker has no `to` field in allowed destinations.** The
   wrangler config template shows `allowed_destination_addresses` with the
   validator emails, but the Worker code uses `EMAIL.send()` without
   verifying that the `to` address is in the allowed list. If the domain
   isn't onboarded yet, the Worker can't send at all.

4. **Workers Paid plan required.** Cloudflare Email Sending requires the
   Workers Paid plan (per Cloudflare changelog: "Email Sending is available
   on the Workers paid plan"). The document doesn't verify whether the
   account is on the paid plan.

**Fix:** Add a pre-send infrastructure checklist:
- [ ] Create `research@qnfo.net` mailbox or Email Routing rule
- [ ] Verify Workers Paid plan is active
- [ ] Onboard qnfo.net to Cloudflare Email Service
- [ ] Generate HTML email files from markdown templates
- [ ] Test-send to a verified internal address before validator outreach

---

#### F-P2-7: Rovelli Email Reveals Framework's Internal Mechanism Before Classification

**Severity:** HIGH
**Document:** `validator-outreach-emails.md` §1, Email 3

**The problem text:**
> "The taxonomy formalizes this as a self-descriptive system where the
> observer is structurally embedded — a node in a generation tree with
> no external vantage point. This resonates with the perspectival
> approach you have developed, while differing in its mathematical
> formulation (ultrametric geometry rather than relational constraints)."

This paragraph reveals THREE framework-internal details:
1. "self-descriptive system" — the framework's name for itself
2. "node in a generation tree" — the specific mathematical structure
3. "ultrametric geometry rather than relational constraints" — the
   mathematical distinction from Rovelli's own approach

A validator who reads this before classifying the taxonomy has been given
a preview of the framework's entire architecture. This is like telling a
peer reviewer "here's our theory, now please independently classify the
problems it claims to solve."

**Fix:** Remove ALL framework-internal language from ALL emails. The validator
should learn about the taxonomy ONLY from the taxonomy package itself.

---

### MODERATE

---

#### F-P2-8: Email Addresses Not Verified Against Current Institutional Pages

**Severity:** MODERATE
**Document:** `validator-outreach-emails.md` §2 (PowerShell script)

**Unverified addresses in script:**
| Candidate | Address in Script | Risk |
|-----------|------------------|------|
| Maudlin | maudlin@nyu.edu | Plausible but unverified |
| Wallace | david.wallace@pitt.edu | Wallace moved Oxford → USC → Pittsburgh; pitt.edu may be new |
| Rovelli | rovellli@cpt.univ-mrs.fr | Typo? "rovellli" (3 L's) vs expected "rovelli" (2 L's). Also cc Perimeter |
| Ismael | ji2085@columbia.edu | UNI format plausible but unverified |
| Marletto | chiara.marletto@wolfson.ox.ac.uk | Plausible but unverified |

**The Rovelli email address "rovellli@cpt.univ-mrs.fr" has a likely typo** —
three L's instead of two. This was not caught before including in the
PowerShell script. If sent, the email would bounce or go to a wrong address.

**Fix:** Before any sending, verify ALL email addresses by:
1. Visiting institutional profile pages
2. Checking recent arXiv preprints for listed corresponding author emails
3. Sending a test message to a verified internal address first

---

#### F-P2-9: S4 (Arrow of Time) Misplaced in Layer 3 — Not Primarily a Quantum-Classical Issue

**Severity:** MODERATE
**Document:** `taxonomy-validation-package.md` §1, Layer 3

**The assignment:** S4 (Arrow of Time) is in Layer 3: "Quantum-Classical
Divide."

**The problem:** The arrow of time is primarily a thermodynamic and
statistical mechanics issue — the second law, entropy increase, and the
past hypothesis. While quantum measurement introduces irreversibility
(via collapse or decoherence), the arrow of time predates quantum mechanics
and exists in purely classical statistical mechanics (Boltzmann's H-theorem,
Loschmidt's paradox).

Placing S4 in the "Quantum-Classical Divide" layer reflects the framework's
SPECIFIC claim that the arrow is tied to the tree's growth direction under
calibration, not a neutral taxonomic judgment. A statistical mechanics expert
would place S4 in a "thermodynamics" or "time" layer, not with S5 (Heisenberg
Cut) and S6 (Non-Local Correlations).

**Fix:** Either move S4 to a dedicated "Time and Irreversibility" layer,
merge it with S11 (Problem of Time) into a "Time" group, or add a note:
*"S4 is placed here because the framework's resolution mechanism treats
the arrow of time as emergent from quantum-to-classical projection. Validators
who work primarily in statistical mechanics may wish to reclassify this
assignment."*

---

#### F-P2-10: "Missing Schisms" Field Contradicts "Systematic Scan" Claim

**Severity:** MODERATE
**Document:** `taxonomy-validation-package.md` §2, §3

**The conflict:**
- §2: "A systematic scan of the foundations-of-physics literature (2025–2026)
  identified recurring bifurcations..."
- §3: "Are there unresolved foundational tensions that should be in this
  taxonomy but aren't? Please list:"

If the scan was truly systematic, the taxonomy should be complete. Asking for
missing schisms implies the scan was NOT systematic — or that the authors
expect it to be incomplete. This internal contradiction undermines the
credibility of the "systematic scan" methodology.

**Fix:** Replace "systematic scan" with a more honest description: *"A
literature review of foundations-of-physics papers (2025–2026) identified
recurring bifurcations. The following 29 represent the most frequently
occurring and structurally significant tensions. Validators are encouraged
to identify any that were missed or that they consider more fundamental
than those listed."*

---

#### F-P2-11: Outlook COM Script Has No Error Handling — Silent Failures on All 5 Emails

**Severity:** MODERATE
**Document:** `validator-outreach-emails.md` §2

**The script:**
```powershell
$mail.HTMLBody = Get-Content $email.BodyFile -Raw
...
$mail.Send()
Start-Sleep -Seconds 2
```

**Failure modes:**
1. Body file doesn't exist → `Get-Content` throws (not caught)
2. Outlook COM not available → `New-Object` throws (not caught)
3. Sending account not configured → `$mail.Send()` throws or silently fails
4. Email address invalid → bounce, but script reports "Sent"
5. Rate limiting → subsequent sends may be throttled without notice

None of these have try/catch blocks, logging, or retry logic.

**Fix:** Add error handling:
```powershell
try {
    $mail.Send()
    Write-Host "✓ Sent to: $($email.Name)" -ForegroundColor Green
} catch {
    Write-Host "✗ FAILED: $($email.Name) — $_" -ForegroundColor Red
}
```

---

#### F-P2-12: Rovelli Schism Coverage Inflated — S1/S3 Not Direct Expertise

**Severity:** MODERATE
**Document:** `external-validator-candidates.md` Candidate 3

**The claim:** Rovelli covers S1 (continuous/discrete) and S3
(background/foreground) "via LQG."

**The problem:** LQG predicts discrete spacetime and is background-independent.
But this makes LQG a THEORY that takes positions on S1/S3 — it doesn't make
Rovelli an EXPERT in the continuous/discrete debate or the
background-independence problem per se. His expertise is in LQG construction,
not in the philosophical dimensions of these schisms.

This inflates Rovelli's estimated coverage from ~10/29 (more realistic) to
~12/29. Two schisms of difference might not matter for the overall assessment,
but the methodology of assigning schism coverage should be more conservative.

**Fix:** Downgrade Rovelli's S1 and S3 coverage from "direct expertise" to
"indirectly via LQG" and reduce estimated overlap to ~10/29.

---

### LOW

---

#### F-P2-13: Sender Name "QNFO Research" May Suppress Response Rates

**Severity:** LOW
**Document:** `validator-outreach-emails.md` §1

**The signature block:**
```
[User Name]
QNFO Research
research@qnfo.net
```

**The issue:** "QNFO Research" is an unknown organization to all validators.
Academic email from unknown organizations is often filtered as spam or
ignored. A personal academic email signature (with institutional affiliation
if applicable) would likely have higher response rates.

**Fix:** Consider sending from a personal academic address (if the user has
one) and using "QNFO Research" only in the body as context. Alternatively,
if sending must be from qnfo.net, add a brief one-line institutional
description: *"QNFO Research — independent foundations-of-physics research
program."*

---

## §A. Remediation Priority

| Priority | Finding | Action Required |
|----------|---------|----------------|
| **1 (CRITICAL)** | F-P2-2: Email priming bias | Rewrite all 5 emails to remove ALL taxonomy claims, framework language, and resolution statements |
| **2 (CRITICAL)** | F-P2-1: Resolution definition bias | Replace resolution definition with standard neutral definition |
| **3 (HIGH)** | F-P2-7: Rovelli email reveals framework | Fix as part of email rewrite (Priority 1) |
| **4 (HIGH)** | F-P2-5: Marletto email as competition | Fix as part of email rewrite (Priority 1) |
| **5 (HIGH)** | F-P2-6: Infrastructure prerequisites | Create missing files, verify account plan, add pre-send checklist |
| **6 (HIGH)** | F-P2-3: Layer structure bias | Add neutrality disclaimer to taxonomy package |
| **7 (HIGH)** | F-P2-4: Flattery + priming compound | Fix as part of email rewrite (Priority 1) |
| 8 (MODERATE) | F-P2-8: Unverified email addresses | Verify all 5 addresses against institutional pages |
| 9 (MODERATE) | F-P2-9: S4 misplaced in Layer 3 | Move S4 or add explanatory note |
| 10 (MODERATE) | F-P2-10: "Systematic scan" language | Replace with honest description |
| 11 (MODERATE) | F-P2-11: No error handling in script | Add try/catch to PowerShell |
| 12 (MODERATE) | F-P2-12: Rovelli coverage inflated | Downgrade to ~10/29 |
| 13 (LOW) | F-P2-13: Sender name concern | Consider personal address or add org description |

---

## §B. DoD Gate

| Criterion | Evidence | Status |
|-----------|----------|--------|
| Red-Team Passed | 13 findings, 2 CRITICAL | ❌ **FAILED** |
| Priming bias eliminated | All 5 emails prime validators | ❌ |
| QNFO-neutrality verified | Background section encodes framework | ❌ |
| Infrastructure verified | Files missing, prerequisites unchecked | ❌ |
| Edge cases tested | Error handling missing in script | ❌ |

**DoD Gate: FAILED.** Phase 2 deliverables (Tasks 2.1, 2.2, email infrastructure)
cannot proceed to validator outreach. The taxonomy package and outreach
emails introduce systematic bias that would invalidate any classification
results obtained.

**Estimated remediation effort:** 4–6 hours (rewrite 5 emails + fix taxonomy
package definitions + verify infrastructure).

---

*End of Audit*
