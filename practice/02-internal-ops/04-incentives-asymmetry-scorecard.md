# The Bilateral Asymmetry Scorecard

Type: Internal Ops / Deal Desk
Owner: Sales Manager and Rep
Frequency: Weekly forecast call
**Purpose:** To measure how much neither side knows, and to route the deal to whichever artifact closes the wider gap.

- **Theory:** A deal sticks when the Bilateral Asymmetry Gap ($\Delta_A$) approaches zero. Per Axiom II, $\Delta_A = I_{seller} + I_{buyer}$. The gap is a **sum**, not a difference.
- **Rule:** Above 7.0, place a commercial hold. Do not issue pricing into a gap that wide.

> [!IMPORTANT]
> **Corrected in this version.** An earlier version of this scorecard computed the gap as the absolute difference between seller and buyer scores. That contradicted the Constitution and produced a specific false negative: a deal where both sides were equally blind scored as "symmetric" and therefore forecastable, when it was in fact the most dangerous deal on the board. The sum is the headline metric. The *balance* between the two halves is still used, but for routing rather than for risk.

---

## How to score

Every dimension is scored 1 to 5, where **5 means high asymmetry**. Higher is worse. This inverts the older clarity-based scale, and it has to, because the two halves are summed rather than compared.

Score what you can evidence, not what you assume. If the rep cannot point to a document, a recorded conversation, or a named person who confirmed it, the answer is not a 1.

---

## Part 1: Seller Ignorance ($I_{seller}$)

What we still do not know about their environment. The [Contextual Blueprint](../01-field-assets/ilg-motion/01-discovery-contextual-blueprint.md) is the instrument that reduces this half.

| Dimension | Score 1 (mapped) | Score 3 (partial) | Score 5 (unmapped) |
|---|---|---|---|
| **S1. Technical architecture, data lineage, and security constraints** | Schemas, API endpoints, dependencies, and infosec requirements documented and verified. | High-level architecture known. Transformation logic, edge cases, and specific security policy unverified. | Legacy or proprietary systems present. Data lineage undocumented. Custom or sovereign data rules unmapped. |
| **S2. Operational workflow and exception handling** | Standard procedures mapped. Manual interventions and exceptions quantified. | Primary workflow mapped. Exception handling unquantified. | Undocumented workarounds. Steps vary by business unit and nobody owns the variance. |
| **S3. The economic event** | The triggering audit, board mandate, or financial target is named and confirmed by the economic buyer. | A general pressure is described but nobody has tied it to a date or a number. | No triggering event identified. The deal is running on interest. |
| **S4. The political map** | We know who loses budget, headcount, or control if we win, and a containment plan exists. | We suspect where resistance sits but have not confirmed it. | Everyone is agreeable and no casualty has been identified. Treat this as the highest-risk answer on the card. |

$$I_{seller} = \frac{1}{4}\sum_{k=1}^{4} S_k \qquad I_{seller} \in [1, 5]$$

**Seller Ignorance score:** ______

---

## Part 2: Buyer Uncertainty ($I_{buyer}$)

What they still do not know about us, the work, or their own exposure. The [Red Team Protocol](../01-field-assets/ilg-motion/02-validation-red-team-protocol.md) is the instrument that reduces this half.

| Dimension | Score 1 (resolved) | Score 3 (partial) | Score 5 (open) |
|---|---|---|---|
| **B1. Vendor capability and product limits** | Track record proven in a comparable environment. Buyer has signed off on a written gap analysis covering what the product cannot do. | Case studies shared. The buyer's environment contains architectural variations we have not proven. | Unproven in their domain, or the buyer believes the product has no limits. Sales puffery has gone unchallenged. |
| **B2. Adoption and change burden** | Minimal workflow disruption. Existing habits largely intact. | Retraining required across several teams. Workflow adjustments identified but not sequenced. | Significant behavioral change required, and the buyer still describes the rollout as plug and play. |
| **B3. Cost and resource predictability** | Timeline and internal resource commitments fixed, with named owners. | Baseline cost defined. Scope expansion and internal availability remain variable. | Wide variance in projected duration and internal cost. No named internal owner. |
| **B4. Price of failure** | The cost of inaction is quantified in currency and the buyer has stated it back to us. | The buyer agrees the status quo is imperfect but has not sized it. | The buyer believes doing nothing is safe. |

$$I_{buyer} = \frac{1}{4}\sum_{k=1}^{4} B_k \qquad I_{buyer} \in [1, 5]$$

**Buyer Uncertainty score:** ______

---

## Part 3: The gap

$$\Delta_A = I_{seller} + I_{buyer} \qquad \Delta_A \in [2, 10]$$

**Total gap:** ______

### Risk bands

| $\Delta_A$ | Classification | What it means | Required action |
|---|---|---|---|
| **2.0 to 4.0** | Low | Low technical and political risk. Standard procurement path is viable. Often a Toaster profile. | Proceed. Lightweight MIP is sufficient. Confirm against the [Process Calculator](../01-field-assets/process-calculator.md) that ILG is warranted at all. |
| **4.0 to 7.0** | Moderate | Real gaps exist that will surface during deployment rather than before it. | Run an explicit Blueprint alignment phase. Hold final pricing until S2 and B3 are each at 2 or below. |
| **7.0 to 10.0** | High | Bridge profile with severe stall and post-signature failure risk. | Commercial hold. Red Team architectural audit and workflow discovery before any contract terms are issued. |

### Routing: which half is wider

The sum sets the risk. The balance sets the next action.

- **$I_{seller}$ exceeds $I_{buyer}$ by 1.0 or more.** We are flying blind. Return to the Blueprint. Do not run a Red Team on an environment we have not mapped, because the workshop will surface our ignorance rather than their risk.
- **$I_{buyer}$ exceeds $I_{seller}$ by 1.0 or more.** They are working from an imagined version of the product. Return to the Red Team. Pricing into this imbalance produces a signature followed by a churn.
- **Within 1.0 of each other and both high.** The most dangerous state on the card, and the one the old difference-based scale scored as healthy. Both sides are guessing. Run Blueprint and Red Team in sequence before forecasting.

### Feeding the equations

The raw gap on $[2, 10]$ does not substitute directly into the Constitution's cost equations. Normalize first:

$$\hat{\Delta}_A = \frac{\Delta_A - 2}{8}, \qquad \hat{\Delta}_A \in [0, 1]$$

Use the raw score for the bands above. Use the normalized value in $F_{effective}$ or $y$. See [03-mathematical-models.md](../../theory/01-foundation/03-mathematical-models.md), Section 1.5.

---

## Manager calibration questions

- "Show me the document behind that S1 score."
- "Who is the casualty? If the answer is nobody, why is S4 not a 5?"
- "Has the buyer said the cost of inaction back to us in their own words, or did we say it to them?"
- "Which half is wider, and which artifact are we running next because of it?"

---

## Related

- [00-ilg-constitution.md](../../theory/01-foundation/00-ilg-constitution.md) — Axiom II defines $\Delta_A$.
- [03-mathematical-models.md](../../theory/01-foundation/03-mathematical-models.md) — Functional forms for $I_{seller}$ and $I_{buyer}$, and the normalization rule.
- [Contextual Blueprint](../01-field-assets/ilg-motion/01-discovery-contextual-blueprint.md) — Reduces $I_{seller}$.
- [Red Team Protocol](../01-field-assets/ilg-motion/02-validation-red-team-protocol.md) — Reduces $I_{buyer}$.
- [Deal Calibration](./01-governance-deal-calibration.md) — Where this score enters the forecast call.
