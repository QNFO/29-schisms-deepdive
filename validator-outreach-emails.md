# Validator Outreach Emails — 29-Schism Taxonomy

**Date:** Drafted 2026-07-20 — to be sent after final publication
**Delivery:** Outlook (COM automation) or Cloudflare Email Service Worker
**From:** research@qnfo.net (or equivalent QUniverse domain)
**Reply-To:** [user's email — to be configured]

---

## §0. Sending Infrastructure

### Option A: Outlook COM (Windows — available now)

```powershell
# PowerShell COM script to send a single email via Outlook
$outlook = New-Object -ComObject Outlook.Application
$mail = $outlook.CreateItem(0)  # 0 = olMailItem
$mail.To = "recipient@university.edu"
$mail.From = "research@qnfo.net"  # must be configured in Outlook
$mail.Subject = "Request for expert review — 29-schism taxonomy classification"
$mail.HTMLBody = "<html><body>...</body></html>"
$mail.BodyFormat = 2  # olFormatHTML
$mail.Importance = 1   # olImportanceNormal
$mail.Send()
```

**Limitations:** Requires Outlook configured with the sending account. Must comply with institutional email policies. Rate-limited by Exchange/Outlook throttling (~30 emails/min).

### Option B: Cloudflare Email Service (via Worker)

```typescript
// src/index.ts — Email Sending Worker
export default {
  async fetch(request: Request, env: Env): Promise<Response> {
    const { to, subject, html, text } = await request.json() as EmailRequest;
    const response = await env.EMAIL.send({
      to,
      from: `research@qnfo.net`,
      subject,
      html,
      text,
    });
    return Response.json({ messageId: response.messageId });
  }
}
```

**Requirements:**
1. Domain (e.g., qnfo.net) onboarded to Cloudflare Email Service
2. SPF/DKIM DNS records configured
3. `send_email` binding in wrangler config
4. Workers Paid plan

### Option C: Hybrid (recommended)

Draft in this file → verify with user → send via Outlook for initial batch → deploy Worker for scalable follow-ups.

---

## §1. Email Templates

### General Notes

- **Personalization fields:** `[Name]`, `[Specific Work]`, `[Schism Area]`
- **Timing:** Send only after final publication (v2.0+ taxonomy paper published)
- **Package attachment:** Link to validated taxonomy package (Task 2.2)
- **Ethics:** No human subjects data collected. Professional research review only.

---

### Email 1: Tim Maudlin (NYU)

```
To: [maudlin@nyu.edu — verify institutional page]
From: research@qnfo.net
Subject: Expert review request — validating a taxonomy of 29 schisms in physics foundations

Dear Professor Maudlin,

I am writing to invite your independent expert review of a taxonomy that
classifies 29 unresolved conceptual tensions in the foundations of physics,
published as part of a research program on self-descriptive formal systems.

Your work on the measurement problem and the tension between Schrödinger
dynamics and collapse — articulated with precision in Quantum Theory
(2019) — engages directly with what the taxonomy identifies as the
"nomological dualism" schism (S19): the apparent separation of dynamical
laws from initial/boundary conditions. This is the entry-point schism for
the taxonomy, and your perspective would provide an invaluable calibration.

The review involves:
- Classifying up to 29 schisms as "physics," "philosophy," "resolved," or
  "ill-posed" (12 within your documented expertise)
- Suggesting any missing schisms
- Evaluating whether the taxonomy's proposed resolutions are substantively
  different from existing frameworks

Expected time commitment: 2–4 hours. No prior knowledge of our specific
framework is expected or required — we explicitly seek your independent
classification, not an endorsement.

The taxonomy package and classification form are attached. We would be
grateful for your response within eight weeks.

Thank you for considering this request.

Best regards,
[User Name]
QNFO Research
research@qnfo.net

---

Reference: Maudlin, T. (2019). Philosophy of Physics: Quantum Theory.
Princeton University Press.
```

---

### Email 2: David Wallace (Pittsburgh)

```
To: [david.wallace@pitt.edu — verify institutional page]
From: research@qnfo.net
Subject: Expert review — 29-schism taxonomy in foundations of physics

Dear Professor Wallace,

I am writing to invite your independent expert review of a taxonomy that
classifies 29 unresolved conceptual tensions in the foundations of physics.
Your expertise in the Everett interpretation and the philosophical
foundations of quantum mechanics makes your perspective uniquely valuable.

The taxonomy claims that several schisms — including S26 (single outcome
vs. all outcomes) — remain unresolved and require a structural
reformulation of how physics describes itself. As the author of The
Emergent Multiverse (2012), which argues that decoherence + Everett
already resolves the measurement problem, your classification would
provide a critical stress test: does the taxonomy's treatment of these
schisms survive scrutiny from an Everettian perspective, or does it
misclassify as "unresolved" what is in fact resolved?

The review involves:
- Classifying up to 29 schisms (11 within your direct expertise, spanning
  emergence, probability, and the ontology of quantum states)
- Identifying any schisms you believe are already resolved
- Evaluating the taxonomy's structural resolution claims

Expected time commitment: 2–4 hours. We seek your independent classification,
not adoption of any particular framework.

The taxonomy package and classification form are attached. We would be
grateful for your response within eight weeks.

Thank you for considering this request.

Best regards,
[User Name]
QNFO Research
research@qnfo.net

---

Reference: Wallace, D. (2012). The Emergent Multiverse: Quantum Theory
According to the Everett Interpretation. Oxford University Press.
```

---

### Email 3: Carlo Rovelli (Aix-Marseille / Perimeter)

```
To: [rovelli@cpt.univ-mrs.fr — verify institutional page; cc Perimeter]
From: research@qnfo.net
Subject: Review request — 29-schism taxonomy (relational perspective sought)

Dear Professor Rovelli,

I am writing to invite your independent expert review of a taxonomy that
classifies 29 unresolved conceptual tensions in the foundations of physics.

Your relational interpretation of quantum mechanics engages the central
tension the taxonomy addresses: the "View from Nowhere" versus the "View
from Within." The taxonomy formalizes this as a self-descriptive system
where the observer is structurally embedded — a node in a generation tree
with no external vantage point. This resonates with the perspectival
approach you have developed, while differing in its mathematical
formulation (ultrametric geometry rather than relational constraints).

Additionally, your work on loop quantum gravity engages the structural
assumptions layer of the taxonomy — specifically the discrete/continuous
schism (S1), the background/foreground schism (S3), and the dimensionality
question (S23).

The review involves:
- Classifying up to 29 schisms (12 within your documented expertise)
- Evaluating whether the taxonomy's resolution of the observer/observed
  schism (S10) captures what relational QM captures, or misses something
- Identifying any missing schisms from a quantum gravity perspective

I recognize your time is exceptionally limited. The expected commitment is
2–3 hours. If you are unavailable, a recommendation of a colleague would
be greatly appreciated.

The taxonomy package and classification form are attached.

With gratitude for your consideration,
[User Name]
QNFO Research
research@qnfo.net

---

Reference: Rovelli, C. (1996). "Relational Quantum Mechanics."
International Journal of Theoretical Physics, 35, 1637–1678.
```

---

### Email 4: Jenann Ismael (Columbia)

```
To: [ji2085@columbia.edu — verify institutional page]
From: research@qnfo.net
Subject: Expert review — 29-schism taxonomy and the situated perspective

Dear Professor Ismael,

I am writing to invite your independent expert review of a taxonomy that
classifies 29 unresolved conceptual tensions in the foundations of physics.

Your work on the situated, embedded perspective in physics — articulated in
The Situated Self (2007) and How Physics Makes Us Free (2016) — provides a
direct parallel to the taxonomy's central claim: that physics must be
formulated from within the system it describes, with the observer as a
node in the description space rather than an external vantage point.

The taxonomy intersects with your work on time (S11: time as parameter vs.
structure), laws (S16: do laws exist? and S19: law/initial-condition
dualism), and the observer's position (S10: inside vs. outside the system).
Your evaluation of whether the formal resolution of these schisms captures
the conceptual richness of the situated perspective would be deeply valuable.

The review involves:
- Classifying up to 29 schisms (12 within your expertise)
- Evaluating whether formal structural resolution addresses the conceptual
  concerns you have raised about the "view from nowhere"
- Identifying any schisms that a situated perspective reveals as
  differently framed than the taxonomy presents them

Expected time commitment: 2–4 hours.

The taxonomy package and classification form are attached. We would be
grateful for your response within eight weeks.

Thank you for considering this request.

Best regards,
[User Name]
QNFO Research
research@qnfo.net

---

Reference: Ismael, J. (2007). The Situated Self. Oxford University Press.
```

---

### Email 5: Chiara Marletto (Oxford)

```
To: [chiara.marletto@wolfson.ox.ac.uk — verify institutional page]
From: research@qnfo.net
Subject: Review request — 29-schism taxonomy and constructor theory comparison

Dear Dr. Marletto,

I am writing to invite your independent expert review of a taxonomy that
classifies 29 unresolved conceptual tensions in the foundations of physics.

Constructor theory, developed by you and David Deutsch, directly targets
the schism the taxonomy identifies as "nomological dualism" (S19) — the
separation between dynamical laws and initial/boundary conditions —
through a counterfactual framework of possible and impossible
transformations. The taxonomy proposes an alternative resolution using
ultrametric fixed-point geometry and self-referential calibration.

Your classification would provide the most direct competitive evaluation
of the taxonomy's claims: does the counterfactual approach resolve S19
more parsimoniously than the self-descriptive approach, or are there
schisms constructor theory does not address that the taxonomy captures?

The review involves:
- Classifying up to 29 schisms (8 within your direct expertise, focused on
  the laws/state ontology layer)
- Evaluating whether S19 is, in your view, resolved by constructor theory —
  and if so, whether the taxonomy's alternative resolution is unnecessary
- Identifying any schisms constructor theory could address but hasn't yet

Expected time commitment: 2–3 hours.

The taxonomy package and classification form are attached. We would be
grateful for your response within eight weeks.

Thank you for considering this request.

Best regards,
[User Name]
QNFO Research
research@qnfo.net

---

Reference: Deutsch, D. & Marletto, C. (2015). "Constructor theory of
information." Proceedings of the Royal Society A, 471, 20140540.
```

---

## §2. Batch Sending Script (Outlook COM)

```powershell
# Save as: send-validator-emails.ps1
# Run: powershell -ExecutionPolicy Bypass -File send-validator-emails.ps1

$emails = @(
    @{
        To = "maudlin@nyu.edu"
        Name = "Professor Maudlin"
        Subject = "Expert review request — validating a taxonomy of 29 schisms in physics foundations"
        BodyFile = "email-maudlin.html"
    },
    @{
        To = "david.wallace@pitt.edu"
        Name = "Professor Wallace"
        Subject = "Expert review — 29-schism taxonomy in foundations of physics"
        BodyFile = "email-wallace.html"
    },
    @{
        To = "rovelli@cpt.univ-mrs.fr"
        Name = "Professor Rovelli"
        Subject = "Review request — 29-schism taxonomy (relational perspective sought)"
        BodyFile = "email-rovelli.html"
    },
    @{
        To = "ji2085@columbia.edu"
        Name = "Professor Ismael"
        Subject = "Expert review — 29-schism taxonomy and the situated perspective"
        BodyFile = "email-ismael.html"
    },
    @{
        To = "chiara.marletto@wolfson.ox.ac.uk"
        Name = "Dr. Marletto"
        Subject = "Review request — 29-schism taxonomy and constructor theory comparison"
        BodyFile = "email-marletto.html"
    }
)

$outlook = New-Object -ComObject Outlook.Application

foreach ($email in $emails) {
    $mail = $outlook.CreateItem(0)  # olMailItem
    $mail.To = $email.To
    $mail.Subject = $email.Subject
    # Read HTML body from file
    $mail.HTMLBody = Get-Content $email.BodyFile -Raw
    $mail.BodyFormat = 2  # olFormatHTML
    $mail.Importance = 1  # olImportanceNormal
    $mail.Send()
    Write-Host "Sent to: $($email.Name) <$($email.To)>"
    Start-Sleep -Seconds 2  # Rate limit
}

Write-Host "All emails sent."
```

---

## §3. Cloudflare Email Worker (for scalable sending)

### 3.1 Worker Code

```typescript
// src/index.ts
interface EmailRequest {
  to: string;
  name: string;
  template: string;  // one of: maudlin, wallace, rovelli, ismael, marletto
}

interface Env {
  EMAIL: { send: (opts: EmailOptions) => Promise<{ messageId: string }> };
  API_KEY: string;  // secret for auth
}

interface EmailOptions {
  to: string;
  from: string;
  subject: string;
  html: string;
  text: string;
}

// Email templates — stored in Worker for now, could move to KV
const TEMPLATES: Record<string, { subject: string; html: string; text: string }> = {
  maudlin: {
    subject: "Expert review request — validating a taxonomy of 29 schisms in physics foundations",
    html: "<html><body>...</body></html>",  // full HTML content
    text: "Dear Professor Maudlin,\n\n..."  // plain text fallback
  },
  // ... other templates
};

export default {
  async fetch(request: Request, env: Env): Promise<Response> {
    // Auth check
    const auth = request.headers.get("Authorization");
    if (auth !== `Bearer ${env.API_KEY}`) {
      return new Response("Unauthorized", { status: 401 });
    }

    if (request.method === "POST") {
      const { to, name, template } = await request.json() as EmailRequest;
      const tpl = TEMPLATES[template];
      if (!tpl) {
        return new Response("Unknown template", { status: 400 });
      }

      const response = await env.EMAIL.send({
        to,
        from: "research@qnfo.net",
        subject: tpl.subject,
        html: tpl.html,
        text: tpl.text,
      });

      return Response.json({ messageId: response.messageId, sent: to });
    }

    return new Response("Email sending endpoint — POST with {to, name, template}", { status: 200 });
  }
};
```

### 3.2 Wrangler Config

```jsonc
// wrangler.jsonc
{
  "name": "qnfo-email",
  "send_email": [
    {
      "name": "EMAIL",
      "remote": true,
      "allowed_destination_addresses": [
        "maudlin@nyu.edu",
        "david.wallace@pitt.edu",
        "rovelli@cpt.univ-mrs.fr",
        "ji2085@columbia.edu",
        "chiara.marletto@wolfson.ox.ac.uk"
      ]
    }
  ]
}
```

### 3.3 Deploy Command

```bash
npx wrangler deploy
```

---

## §4. Pre-Send Checklist

- [ ] Final taxonomy paper published (Zenodo DOI obtained)
- [ ] Taxonomy validation package complete (Task 2.2)
- [ ] Classification form prepared (web form or PDF)
- [ ] Sending domain verified (qnfo.net DNS: SPF, DKIM, DMARC)
- [ ] Email addresses verified on institutional websites
- [ ] User approved all email content
- [ ] HTML versions converted from markdown templates
- [ ] Plain text fallback prepared for each email
- [ ] Reply-to configured
- [ ] Bounce handling configured (cf-bounce subdomain)
- [ ] Rate limit: max 5 emails/session (Outlook) or 100/hr (Cloudflare)
- [ ] Log sent status to `email-send-log.md`

---

*End of Outreach Email Drafts*
