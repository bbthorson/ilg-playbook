# The Deal Triage Calculator

Version: 4.0
Audience: Internal Rep / Pre-Sales
Goal: Classify a live deal opportunity into the appropriate sales motion — SLG, PLG, or ILG — by diagnosing market stage first, then asset specificity within mature markets.

**Canonical Reference:** [ILG Constitution — Axiom I (Law of Economic Boundaries)](../../theory/01-foundation/00-ilg-constitution.md). The reasoning behind each step is in [01-sales-motion-comparison.md](../../theory/01-foundation/01-sales-motion-comparison.md).

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
| **1. Undefined** | No written process. Steps vary by person. Practitioners disagree on what the current process is. | Ask three people to describe the workflow and get three different answers. | **Stop. Chaos Trap.** Redirect to consulting or a paid workshop to define the SOP first. |
| **2. Emergent** | A process exists and is partly written down, but business units have diverged, exceptions are undocumented, and nobody owns the variance. | A written SOP exists that people describe as out of date. | **Conditional.** Proceed to Step 1, but the Blueprint must reconstruct the workflow before the Red Team runs. Budget additional discovery. |
| **3. Codified** | Documented, followed, and exception handling is quantified. Someone owns the process and can name its failure rates. | Current SOP, plus volumes for the exception paths. | **Proceed** to Step 1. |

**Level 2 is the level that gets misread.** A buyer at Level 2 can produce a document on request, which reads as Level 3 to a rep who does not check whether the document matches practice. The failure surfaces during implementation as unmapped exception paths, which is the single most common source of post-signature scope expansion. When in doubt, score down.

> [!IMPORTANT]
> **Workflow maturity is not market stage, and it is not asset specificity.** These are three independent axes, and collapsing them produces wrong routing. A Level 1 workflow in a mature market is a Chaos Trap, not an SLG deal — the category is perfectly legible and the buyer still has nothing to automate. A Level 3 workflow tells you the deal is *mappable*, not that it is a Bridge; that is what Step 2 measures. Score each axis on its own evidence.

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

Score each factor 1–5, then sum. Annotations show which transaction cost component each factor targets — see [Constitution, Part II: Three Transaction Costs](../../theory/01-foundation/00-ilg-constitution.md).

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

## Step 3: Motion Selection

| Market Stage | Cost Score | Motion |
|---|---|---|
| Nascent | (n/a — skipped Step 2) | **SLG** |
| Transitional | 4–14 | **SLG with ILG elements creeping in** |
| Transitional | 15–20 | **ILG** (deal stakes high enough to force ILG even before category maturity) |
| Mature | 4–9 | **PLG** |
| Mature | 10–20 | **ILG** |
| Any | Override: pilot/POC requested | **ILG** (auto-score 20) |

**Override Rule.** If the prospect asks for a "Pilot" or "Proof of Concept," immediately upgrade to ILG regardless of cost score. Pilots are strictly governed by the [Red Team Protocol](./ilg-motion/02-validation-red-team-protocol.md), not by lightweight motions.

---

## What to do next

| Motion | Next artifact / action |
|---|---|
| **SLG** | Educational selling motion. *Note: no canonical SLG artifact in this repo yet — see open work in task #19. In practice today: Challenger-style commercial teaching, vision-casting sessions, co-developed reference architectures, willingness to be wrong publicly about where the category is heading.* |
| **PLG** | [01-velocity-standard-order-protocol.md](./plg-motion/01-velocity-standard-order-protocol.md), then [prospect-evaluation.md](./plg-motion/prospect-evaluation.md), then [order-form.md](./plg-motion/order-form.md). |
| **ILG** | [01-discovery-contextual-blueprint.md](./ilg-motion/01-discovery-contextual-blueprint.md) → [02-validation-red-team-protocol.md](./ilg-motion/02-validation-red-team-protocol.md) → [03-closing-mutual-implementation-plan.md](./ilg-motion/03-closing-mutual-implementation-plan.md). |

---

## Common diagnostic mistakes

- **Skipping Step 0 (Workflow Maturity Gate).** Reps see a high cost score and jump straight to ILG without checking whether a SOP exists. Result: ILG motion on a Chaos Trap; the seller and buyer co-design something that has no operational foundation.
- **Conflating cost score with market stage.** A high cost score (10–20) in a nascent market does *not* mean ILG. The cost score is only meaningful once the market is legible enough for the buyer to compare and evaluate. In nascent markets, educational friction dominates and SLG is the right motion regardless of cost score.
- **Treating "no competitors visible" as a mature market.** Absence of competition often signals nascent, not mature — the buyer can't name 3+ vendors because the category itself doesn't exist yet. This is the most common SLG/PLG misclassification.
- **Ignoring the pilot/POC override.** A buyer who asks for a pilot is signaling they perceive Bridge-level risk regardless of how the seller scored the deal. Honor the override.

---

## Related

- **Theory:** [ILG Constitution — Axiom I (Law of Economic Boundaries) and the Boundary Condition primary derivation](../../theory/01-foundation/00-ilg-constitution.md).
- **Decision framework explanation:** [01-sales-motion-comparison.md](../../theory/01-foundation/01-sales-motion-comparison.md) — why each step exists, with examples of common mistakes.
- **Forecasting:** Managers re-score and audit Bridges via [01-governance-deal-calibration.md](../02-internal-ops/01-governance-deal-calibration.md).
- **Manager review:** Phase 1 of [02-governance-review-checklist.md](../02-internal-ops/02-governance-review-checklist.md) validates the calculator score on every Bridge deal.
