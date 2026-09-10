---
title: "The Process Calculator"
layer: practice
status: active
version: 4.2
operationalizes: [axiom-1]
canonical_source: theory/01-foundation/00-ilg-constitution.md
---

# The Process Calculator

Version: 4.2
Audience: Internal Rep / Pre-Sales
Goal: Classify a live deal opportunity into the appropriate sales motion — SLG, PLG, or ILG — by diagnosing market stage first, then asset specificity within mature markets.

**Canonical Reference:** [ILG Constitution — Axiom I (Law of Transaction Cost Composition)](../../theory/01-foundation/00-ilg-constitution.md). The reasoning behind each step is in [01-sales-motion-comparison.md](../../theory/01-foundation/01-sales-motion-comparison.md).

| | |
|---|---|
| **Inputs** | A live deal opportunity with enough context to characterize both the market (category maturity, vendor landscape) and the deal (integration scope, stakeholders, term). |
| **Outputs** | A motion classification: SLG (nascent market), PLG (mature market + low specificity), or ILG (mature market + high specificity). |
| **Next step** | See "What to do next" below. |
| **Owner** | AE / pre-sales (with manager spot-check). |

---

## Step 0: Workflow Maturity Gate (Pre-Qualification)

**Before scoring anything, classify the buyer's workflow.** You cannot digitize a process nobody has defined.

Score the workflow for the specific problem being solved, not the buyer's operational sophistication generally. A hospital with excellent finance SOPs may have no documented process for the clinical workflow you are selling into.

| Level | Condition | Evidence required | Route |
|---|---|---|---|
| **1. Undefined** | No written process. Steps vary by person. Practitioners disagree on what the current process is. | Ask three people to describe the workflow and get three different answers. | **Stop. Chaos Trap** *if the product automates the process.* Redirect to consulting or a paid workshop to define the SOP first. If the product supplies a medium rather than automating a process, an undefined workflow is not a trap; see Step 2b Gate A. |
| **2. Emergent** | A process exists and is partly written down, but business units have diverged, exceptions are undocumented, and nobody owns the variance. | A written SOP exists that people describe as out of date. | **Conditional.** Proceed to Step 1, but the Blueprint must reconstruct the workflow before the Red Team runs. Budget additional discovery. |
| **3. Codified** | Documented, followed, and exception handling is quantified. Someone owns the process and can name its failure rates. | Current SOP, plus volumes for the exception paths. | **Proceed** to Step 1. |

**Level 2 is the level that gets misread.** A buyer at Level 2 can produce a document on request, which reads as Level 3 to a rep who does not check whether the document matches practice. The failure surfaces during implementation as unmapped exception paths, which is the single most common source of post-signature scope expansion. When in doubt, score down.

> [!IMPORTANT]
> **Workflow maturity is not market stage, and it is not asset specificity.** These are three independent axes, and collapsing them produces wrong routing. A Level 1 workflow in a mature market is a Chaos Trap, not an SLG deal — the category is perfectly legible and the buyer still has nothing to automate. A Level 3 workflow tells you the deal is *mappable*, not that it is Structural; that is what Step 2 measures. Score each axis on its own evidence.

---

## Step 1: Market Stage Diagnostic (Workflow Legibility)

**Score the *market*, not the deal.** Answer Y/N for each signal:

| Signal | Y/N |
|---|---|
| Is there a recognized category name for this solution? (e.g., "ambient AI documentation," "CDP," "QHIN") | |
| Can the buyer name 3+ vendors that solve this problem? | |
| Are there published implementation playbooks, G2 reviews, or analyst coverage (Gartner, Forrester, KLAS)? | |

**Interpret:**

- **0–1 Yes → Nascent market.** The category is not yet legible. Buyers cannot easily compare options because the standards for comparison don't exist.
  - **Motion: SLG.** The seller is creating the market through education and vision-casting. *Skip Step 2* — the cost diagnostic doesn't apply yet because the buyer's problem isn't fully framed.
- **2 Yes → Transitional market.** Category exists but is still consolidating. Some buyers can comparison-shop; others can't.
  - **Continue to Step 2** and weight the result toward ILG — the market is maturing in your favor, and structural friction is rising even as educational friction declines.
- **3 Yes → Mature market.** Category is legible. Buyers can compare alternatives, evaluate implementation, and run formal procurement.
  - **Continue to Step 2** to determine PLG vs. ILG within the mature market.

---

## Step 2: Transaction Cost Diagnostic (Mature and Transitional markets)

Score each factor 1–5, then sum. Annotations show which transaction cost component each factor targets — see [Constitution, Axiom II](../../theory/01-foundation/00-ilg-constitution.md).

### 1. Integration Depth — targets $F_{implementation}$

How tightly does the solution couple to the buyer's existing systems?

- **1:** Standalone tool. No integration needed.
- **3:** Standard API integration (Salesforce, Slack, Workday).
- **5:** Deep ERP/EHR/core-infrastructure integration. Custom code required.
- **Score:** _____

### 2. Workflow Change Scope — targets $F_{implementation}$

How many people's habits change because of the implementation?

- **1:** Single team (<5 users). No process change.
- **3:** Single department. Minor process tweak.
- **5:** Cross-functional (3+ departments). Total workflow overhaul.
- **Score:** _____

### 3. Consensus Complexity — targets $F_{consensus}$

How many stakeholders can say no?

- **1:** Single decision maker with budget authority.
- **3:** Committee (3–4 stakeholders, departmental approval).
- **5:** Board approval, procurement process, or security audit required.
- **Score:** _____

### 4. Retention Horizon — targets sustained $F_{implementation}$

One-shot transaction or long-term dependency?

- **1:** One-time project, no renewal expected.
- **3:** Annual contract, moderate switching cost.
- **5:** Multi-year platform, deep dependency, high switching cost.
- **Score:** _____

**Total Score (4–20):** _____

---

## Step 2b: Workflow Divergence (Mature and Transitional markets)

The four factors above measure how *large* the installation is. None of them measures how far the buyer's existing workflow sits from the one the product was built around. Those are different quantities, and the second one is what decides whether the installation succeeds.

Packaged software carries an assumed workflow. When the buyer's actual workflow differs, the buyer picks one of four responses: change the organization to match the product, accept the shortfall, build a workaround, or pay to customize. All four cost money and only the first two are visible before signature. Research calls this gap *misfit*; see [process-misfit.md](../../theory/02-research/process-misfit.md). It operationalizes the CFIR **Compatibility** construct in its workflow sense, where [Step 0](#step-0-workflow-maturity-gate-pre-qualification) operationalizes the same construct in its maturity sense.

Two gates decide whether divergence governs this deal at all. Run them before scoring.

**Gate A — Must the product fit a workflow the buyer has already encoded?**

Some products do not. A product that supplies a medium rather than automating an existing process has nothing to misfit against, and so does a product deliberately built as a substrate the buyer configures for themselves. In both cases divergence has no reference point to measure from, and a high score would be an artifact of the rubric rather than a property of the deal.

| Answer | Condition | Route |
|---|---|---|
| **No — greenfield** | No encoded workflow exists for this problem. The product creates the practice rather than replacing one. | Skip the divergence score. Route on magnitude and market stage alone. |
| **No — the product absorbs it** | The product ships underspecified on purpose, and the buyer encodes their own workflow inside it without vendor engineering. | Skip the divergence score. Route on magnitude and market stage alone. |
| **Yes** | The buyer runs an encoded workflow the product must fit, extend, or replace. | Continue to Gate B. |

**Gate B — Can the buyer measure the gap themselves, and reverse the decision?**

This is CFIR's **Trialability** construct. A trial does not mainly reduce the cost of evaluating vendors. It transfers the divergence measurement to the buyer, who is the only party positioned to perform it. Where that transfer works, the seller does not need to supply proof before signature, which is the entire reason the ILG artifacts exist.

All three must hold for the answer to be yes:

- The buyer can run the product against their real work, with their real data, without seller engineering.
- Discovering a bad fit costs them days rather than quarters.
- Walking away strands no committed spend and no migrated data.

| Answer | Route |
|---|---|
| **Yes** | **PLG**, whatever the divergence would have scored. The buyer will find the misfit faster than the seller can prove its absence. Track churn rather than implementation risk. |
| **No** | Divergence governs. Score it below. |

Score divergence for the specific workflow you are selling into, on the same discipline Step 0 requires. Do not score the buyer's general sophistication.

| Score | Condition | Evidence required |
|---|---|---|
| **1–2. Standard** | An external authority codified this workflow. A regulator, a statute, or an industry protocol defines the steps, and vendors build against that definition. | Name the standard. If the buyer cannot name it, this is not a 1. |
| **3. Common pattern** | The buyer follows the category's usual shape and can enumerate their local exceptions. | The exception list, in writing, with volumes attached. |
| **4–5. Bespoke** | The buyer encoded the workflow themselves. Exceptions are numerous, undocumented, or both, and no vendor built against this shape. | Ask which upstream systems feed the workflow and who maintains the rules. A shrug is a 5. |

**Divergence Score:** _____

> [!IMPORTANT]
> **Do not add this to the Step 2 total.** The cost score measures magnitude and the divergence score measures fit. Summing them would let a large aligned deal and a small misaligned deal produce the same number, which is the specific confusion this step exists to prevent. Divergence modifies the routing in Step 3 instead.

**What a demonstration can and cannot show.** Misfit runs across six domains: functionality, data, usability, role, control, and organizational culture. A product demonstration reaches the first two. The remaining four surface during implementation unless discovery goes looking for them, which is what the [Contextual Blueprint](./ilg-motion/01-discovery-contextual-blueprint.md) is for.

**Who codified it is the question that predicts the score.** A workflow codified by a regulator converges across buyers, which is how mature Turnkey categories form. A workflow codified by the buyer diverges from every other buyer, and it diverges more the longer it has been in place. Both are well-defined workflows. They route to opposite motions.

---

## Step 3: Motion Selection

| Market Stage | Cost Score | Motion |
|---|---|---|
| Nascent | (n/a — skipped Step 2) | **SLG** |
| Transitional | 4–14 | **SLG with ILG elements creeping in** |
| Transitional | 15–20 | **ILG** (deal stakes high enough to force ILG even before category maturity) |
| Mature | 4–9, Gate A or B passed | **PLG** |
| Mature | 4–9, gates failed, divergence 1–3 | **PLG** |
| Mature | 4–9, gates failed, divergence 4–5 | **ILG** (Hidden Structural — see below) |
| Mature | 10–20 | **ILG** |
| Any | Override: pilot/POC requested | **ILG** (auto-score 20) |

**Override Rule.** If the prospect asks for a "Pilot" or "Proof of Concept," immediately upgrade to ILG regardless of cost score. Pilots are strictly governed by the [Red Team Protocol](./ilg-motion/02-validation-red-team-protocol.md), not by lightweight motions.

**Hidden Structural Deal.** A deal scoring 4–9 that failed Gate B and then scored 4 or 5 on divergence is a Structural deal wearing Turnkey clothes. The installation is small, so every magnitude factor scores low, and the workflow underneath it matches nothing the product assumes. Route it to ILG. This is the under-frictioned failure mode from Axiom I, and it is the one the cost score alone cannot see: the seller ships a light motion, misfit surfaces after signature, and the buyer concludes they should have built it themselves.

**Possible Over-Frictioning.** A deal scoring 10–20 with divergence of 1 or 2 is large but aligned. Run ILG, and flag the deal at [manager review](../02-internal-ops/02-governance-review-checklist.md) to confirm the full artifact chain earns its cost. Deep integration against a standard the vendor already builds to is expensive work, not uncertain work, and the ILG machinery exists to resolve uncertainty.

---

## What to do next

| Motion | Next artifact / action |
|---|---|
| **SLG** | [01-education-led-motion.md](./slg-motion/01-education-led-motion.md). Deliberately thin, since education-led selling is well documented elsewhere. Covers what ILG machinery to leave switched off, the tripwires for misreading a mature market as nascent, and the triggers that end the motion. |
| **PLG** | [01-velocity-standard-order-protocol.md](./plg-motion/01-velocity-standard-order-protocol.md), then [prospect-evaluation.md](./plg-motion/prospect-evaluation.md), then [order-form.md](./plg-motion/order-form.md). |
| **ILG** | [01-discovery-contextual-blueprint.md](./ilg-motion/01-discovery-contextual-blueprint.md) → [02-validation-red-team-protocol.md](./ilg-motion/02-validation-red-team-protocol.md) → [03-closing-mutual-implementation-plan.md](./ilg-motion/03-closing-mutual-implementation-plan.md). |

---

## Common diagnostic mistakes

- **Skipping Step 0 (Workflow Maturity Gate).** Reps see a high cost score and jump straight to ILG without checking whether a SOP exists. Result: ILG motion on a Chaos Trap; the seller and buyer co-design something that has no operational foundation.
- **Conflating cost score with market stage.** A high cost score (10–20) in a nascent market does *not* mean ILG. The cost score is only meaningful once the market is legible enough for the buyer to compare and evaluate. In nascent markets, educational friction dominates and SLG is the right motion regardless of cost score.
- **Treating "no competitors visible" as a mature market.** Absence of competition often signals nascent, not mature — the buyer can't name 3+ vendors because the category itself doesn't exist yet. This is the most common SLG/PLG misclassification.
- **Scoring size when the question is fit.** A rep totals four magnitude factors, lands at 7, and routes to PLG without asking whether the buyer's workflow resembles the one the product assumes. Step 2b exists because those two questions have different answers, and the second one is the one that surfaces after signature.
- **Scoring divergence on a deal that has nothing to diverge from.** A team-collaboration tool entering an org with no encoded workflow cannot name an external standard, so a rep reads the rubric and lands on 4 or 5. Gate A exists to stop that. High divergence and no reference point are different findings.
- **Ignoring the pilot/POC override.** A buyer who asks for a pilot is signaling they perceive Structural-level risk regardless of how the seller scored the deal. Honor the override.

---

## Related

- **Theory:** [ILG Constitution — Axiom I (Law of Transaction Cost Composition) and the Boundary Condition primary derivation](../../theory/01-foundation/00-ilg-constitution.md).
- **Decision framework explanation:** [01-sales-motion-comparison.md](../../theory/01-foundation/01-sales-motion-comparison.md) — why each step exists, with examples of common mistakes.
- **Forecasting:** Managers re-score and audit Structural deals via [02-governance-review-checklist.md](../02-internal-ops/02-governance-review-checklist.md).
- **Manager review:** Phase 1 of [02-governance-review-checklist.md](../02-internal-ops/02-governance-review-checklist.md) validates the calculator score on every Structural deal.
