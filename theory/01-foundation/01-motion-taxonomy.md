---
title: "The Motion Taxonomy"
layer: theory
status: active
version: 1.1
operationalizes: [axiom-1, axiom-2]
canonical_source: theory/01-foundation/00-tcg-constitution.md
---

# The Motion Taxonomy

**Version:** 1.1
**Purpose:** To name the motions and specify what each one deploys.

A sales motion is the instrument set deployed to reduce a buyer's transaction friction. Because a seller cannot alter intrinsic willingness to pay, transaction enablement operates entirely by reducing transaction costs across three components:

* **$F_{search}$:** Inability to discover, compare, or reach a viable solution at acceptable cost.
* **$F_{consensus}$:** Inability of internal buyer stakeholders to reconcile competing priorities and risks.
* **$F_{implementation}$:** Inability to verify that operational and technical deployment will succeed without destructive disruption.

The three are separately addressable rather than separately caused. A workflow the product must fit but does not raises $F_{implementation}$ and generates $F_{consensus}$ at the same time, because an imposition creates a stakeholder whose objectives worsen. Treat them as three bills the buyer pays, not as three independent variables.

---

## 1. Triage Architecture: Level and Direction

A deal is triaged through two sequential measurements emitted by Axiom I:

1. **Level ($\lVert \mathbf{F} \rVert_1$):** Evaluates total friction against the apparatus boundary of 15. Deals below 15 cannot repay dedicated enablement instruments.
2. **Direction:** Evaluates which friction component accounts for 50 percent or more of effective cost, on deals at or above the boundary. Where no component reaches 50 percent, the deal is **Composed**.

| Level | Component Condition | Motion Routing | Primary Mechanism |
|---|---|---|---|
| **Turnkey** (below 15) | Not evaluated. Component share ignored. | **Turnkey** | Self-service onboarding. Fit verification shifted entirely to the buyer. |
| **Structural** (15 and above) | $\hat{F}_{search} \ge 0.50$ | **Search-led** | Portable artifacts, external validation, and reachability infrastructure. |
| **Structural** | $\hat{F}_{consensus} \ge 0.50$ | **Consensus-led** | Stakeholder objective reconciliation and political risk elimination. |
| **Structural** | $\hat{F}_{implementation} \ge 0.50$ | **Implementation-led** | Technical discovery, failure mode stress-testing, and mutual governance. |
| **Structural** | None reaches 0.50 | **Composed** | Top two instrument sets deployed in direct proportion to weight. |

Level is read from base friction and direction from the amplified components, which is why discovery rotates a deal without reclassifying it. The [Deal Triage Calculator](../../practice/01-field-assets/deal-triage-calculator.md) emits both, and the routing values above are the words it returns.

---

## 2. Motion Specifications

### Turnkey

* **Deal Profile:** Negligible integration requirements, single-stakeholder sign-off, and native workflow alignment.
* **Seller Instruments:** Friction removal via self-service signup, public pricing, automated provisioning, and product trials.
* **Primary Failure Mode:** Misclassifying structural deals as turnkey. A low-seat deployment within an unstructured workflow masks severe underlying divergence.

### Search-led

* **Deal Profile:** High buyer uncertainty regarding category existence, vendor reachability, or baseline solution viability.
* **Blocker Decomposition:**
  * *Category Unnamed:* Deploys reference architectures, market education, and conceptual frameworks.
  * *Vendor Unreachable:* Deploys marketplace listings, distribution channels, and group purchasing contracts. This blocker falls largely on the seller, and neither education nor a trial reduces it. Research is in [channel-collapse.md](../02-research/channel-collapse.md).
  * *Fit Unverified:* Deploys sandbox environments and rapid self-serve proofs.
* **Primary Failure Mode:** Category legibility mid-cycle. As market education succeeds, buyer search costs collapse and commoditization accelerates.

### Consensus-led

* **Deal Profile:** Solution verification exists, but disparate internal buyer incentives prevent transaction sign-off.
* **Seller Instruments:** Objective reconciliation matrices, champion governance structures, and formal decision-criteria design.
* **Operational Rule:** The current repository intentionally identifies this motion as an active theoretical gap. Triage calculator routing here flags an uninstrumented deal boundary on forecast reviews. [consensus-motion/](../../practice/01-field-assets/consensus-motion/) records what exists and what an instrument here would have to do.

### Implementation-led

* **Deal Profile:** Category is understood, but operational disruption, cross-functional dependencies, or deep integrations threaten execution viability.
* **Seller Instruments:** Sequenced, pre-signature governance artifacts:
  1. *[Contextual Blueprint](../../practice/01-field-assets/implementation-motion/01-discovery-contextual-blueprint.md):* Exhaustive mapping of technical and operational baseline workflows.
  2. *[Red Team Protocol](../../practice/01-field-assets/implementation-motion/02-validation-red-team-protocol.md):* Structured prospective hindsight stress-testing to surface prospective operational failure points.
  3. *[Mutual Implementation Plan](../../practice/01-field-assets/implementation-motion/03-closing-mutual-implementation-plan.md):* Formal bilateral resource and governance allocation.
  4. *[Adoption Review](../../practice/01-field-assets/implementation-motion/04-sustaining-adoption-review.md):* Post-signature metric verification to confirm value realization.
* **Primary Failure Mode:** Deploying implementation rigor on search-dominant deals, generating unrequested governance for an uncommitted buyer.

---

## 3. Structural Transitions and Lifecycle Drift

Deal classification is a dynamic vector state, not a permanent static assignment:

* **Expansion Rotation (Turnkey to Implementation-led):** Initial team-level usage expands into enterprise deployment, introducing regulatory, security, and architectural friction that forces the level above 15.
* **Market Maturation (Search-led to Implementation-led):** Category education completes across the buyer's industry, standardizing vendor comparisons and shifting buyer friction entirely to integration governance.
* **Discovery Reclassification (Search-led to Implementation-led):** Mid-cycle architectural discoveries uncover environmental complexities, invalidating educational instruments in favor of the implementation chain.

The second and third transitions are the pair reps miss, and they miss the third more often, because nothing external changes to prompt a re-score.

---

## 4. Disqualification: Where the Implementation Chain Is Wrong

Axiom I requires friction to match asset specificity, so the implementation chain is wrong wherever the surplus it unlocks is smaller than the friction it imposes. Six conditions put a deal outside it. In each, the correct response is to decline rather than to run a lighter version.

**1. No operational baseline exists.** The Blueprint maps a workflow. With no workflow to map, the artifact produces a document the two parties invented together and the Red Team stress-tests a fiction. This is the Chaos Trap, and it is why the workflow gate runs before anything is counted. *Route:* consulting to establish the process, then re-qualify.

**2. Deal value cannot carry the friction cost.** The chain consumes solutions-engineering hours before revenue. Below roughly the point where pre-sale cost exceeds first-year gross margin, it destroys surplus even when the deal closes. *Route:* Turnkey, or decline.

    This is the affordability half of the level-and-frequency split in [07-governance-forms.md](./07-governance-forms.md) section 6. Level says what the deal needs and frequency says whether it can be paid for, so a one-shot deal above the boundary can genuinely need the full chain and still be correct to decline.

    *Under review.* First-year gross margin is a single-shot test. [05-seller-surplus-model.md](./05-seller-surplus-model.md) section 7 shows pre-sale investment amortizes across the renewal stream, so this rule is correct where retention is weak and too strict where it holds.

**3. The category has commoditized.** Integration patterns homogenized, playbooks published, switching cost fell. Specificity dropped out from under a motion that used to fit. *Route:* re-score annually and migrate to Turnkey instruments when the level drops below 15.

**4. The specification is externally fixed.** A regulatory mandate or procurement standard that dictates the implementation leaves no discovery surplus to capture. Both parties already know what gets built, so discovery cannot reduce the gap on the dimension that matters. *Route:* compete on price and delivery credibility.

**5. The buyer has no implementation capacity at any price.** The MIP allocates resources the buyer does not have and cannot obtain. This is a capacity constraint rather than a governance failure, and better structure does not repair it. A signed MIP against absent resources produces a launch failure with a contract attached. *Route:* defer until capacity exists, or sell a managed-service shape instead.

**6. The seller cannot deliver what the motion promises.** This motion makes implementation credibility the product. An organization without the depth to run a genuine Red Team produces workshops that surface nothing, which is worse than running none, because the buyer now holds documented assurance that the risks were examined. *Route:* build the capability before selling on it.

The first three are properties of the deal. The last three are properties of the environment or the seller, and they are the ones teams skip when auditing their own boundary.

---

## Related

- [00-tcg-constitution.md](./00-tcg-constitution.md) — Axiom I supplies level and direction. Axiom II supplies the per-component amplification direction is read from.
- [06-friction-vector.md](./06-friction-vector.md) — Why a motion is a region of one space rather than an item on a list.
- [07-governance-forms.md](./07-governance-forms.md) — Frequency, and what shape the arrangement takes after signature.
- [09-motion-vocabulary.md](./09-motion-vocabulary.md) — How these names map onto Product-Led, Sales-Led and the rest of the incumbent vocabulary.
- [Deal Triage Calculator](../../practice/01-field-assets/deal-triage-calculator.md) — The one place the diagnostic lives.
