# Seller Surplus and the Implementation Investment

**Version:** 1.0
**Purpose:** To specify the seller's side of the transaction, so that "should we invest engineering in this deal, and how much" becomes a question the framework can express.

The [Constitution](./00-ilg-constitution.md) models one party. Its Surplus equation describes what the *buyer* gains and what the *buyer* pays. The seller appears throughout as the agent who reduces the buyer's friction, and nowhere as a party with costs of its own.

That omission is invisible while the motion is advisory. It becomes binding the moment the seller deploys engineers into a buyer's environment before signature, because the seller is then sinking capital that no term of the buyer's equation accounts for.

This document adds the second equation. It does not revise Axiom I, which will need revising once this side is settled. See [Open questions](#open-questions).

---

## 1. Why the Surplus equation cannot answer the question

Part III of the Constitution gives:

$$S = \left(V_{effective}(t) - V_{next\_best}\right) - F_{effective}$$

Every term describes the buyer. $F_{effective}$ is the friction the buyer bears. $\Delta_A$ inflates the buyer's perceived cost. $c$ is the price the buyer pays, which is the seller's revenue rather than the seller's cost.

A seller reading this equation learns whether the deal *can* close. It cannot tell them whether the deal is *worth closing*, because nothing in it moves when the seller spends more or less to close it. Asking "should I invest in implementation" of the Surplus equation is asking a question in a language that has no word for it.

---

## 2. The seller's surplus

$$S_{seller} = p_{close} \cdot \left(V_{contract} - C_{deliver}\right) - C_{invest}$$

| Term | Meaning |
|---|---|
| $p_{close}$ | Probability the deal closes, given the investment made |
| $V_{contract}$ | Contract value the seller receives |
| $C_{deliver}$ | Post-signature cost to deliver what was sold |
| $C_{invest}$ | Pre-signature, deal-specific engineering. Spent whether or not the deal closes |

The structure of the asymmetry sits in the last two rows. $C_{deliver}$ is contingent: it is incurred only against revenue. $C_{invest}$ is not. It leaves the building before anyone signs, and it leaves whether $p_{close}$ resolves to one or to zero.

**Both parties are subject to a boundary, and both must clear it.** The Constitution's condition $S > 0$ governs whether the buyer will transact. $S_{seller} > 0$ governs whether the seller should want them to. A deal sitting comfortably inside the buyer's potential well can sit outside the seller's, and the seller who closes it has done accretive work for the customer and dilutive work for their own firm.

---

## 3. What is actually at risk

$C_{invest}$ overstates the exposure. The correct measure is the appropriable quasi-rent:

$$Q = C_{invest} - R_{redeploy}$$

Where $R_{redeploy}$ is the value of that work redeployed elsewhere: reusable connectors, a reference architecture, domain knowledge that transfers to the next deal in the segment. Research backing is in [klein-crawford-alchian.md](../02-research/klein-crawford-alchian.md).

$Q$ is the amount a buyer can extract by threatening to walk after the engineering is spent, and it is the number that belongs in a risk review. Two engagements consuming identical hours carry different exposure when one produces a connector the seller ships to every subsequent customer and the other produces a mapping to a schema that exists in exactly one hospital.

**This inverts the axiom's usual direction.** Axiom I treats asset specificity as the buyer's problem, solved by governance the seller supplies. In a forward-deployed motion the seller sinks the specific investment first, so the seller holds the exposure and needs the governance. The Mutual Implementation Plan already provides it. Its stated rationale covers only one direction.

---

## 4. The investment decision

Differentiating $S_{seller}$ with respect to $C_{invest}$ gives the marginal rule:

$$\frac{\partial p_{close}}{\partial C_{invest}} \cdot \left(V_{contract} - C_{deliver}\right) > 1$$

Spend the next increment while a unit of pre-signature engineering raises the close probability enough that the expected gross margin gain exceeds the unit spent. Stop when it does not.

**Why the left side is ever large enough to justify the spend.** $C_{invest}$ enters the buyer's equation by two routes at once. It reduces $\Delta_A$, because deployed engineering is a demonstration a weak competitor cannot afford to imitate, which is the Single Crossing Property from Axiom II. It also reduces the buyer's $F_{implementation}$ directly, because work the seller performs is work the buyer does not. Both raise $S_{buyer}$, and $p_{close}$ rises with $S_{buyer}$.

This is the only lever that appears on both sides of the transaction, which is what makes it worth modeling separately from price. Discounting moves $c$ and leaves $\Delta_A$ untouched.

**The exposure constraint runs alongside the marginal rule.** Unprotected quasi-rent at any moment must stay inside what a failed deal can cost the firm. A deal can satisfy the marginal rule at every increment and still be wrong to pursue, when the accumulated $Q$ before the buyer commits anything exceeds what the seller can absorb. Sequencing is what reconciles the two, which is section 5.

---

## 5. Staged investment: the mirror of the milestone model

The [Milestone Valuation Model](../../practice/01-field-assets/milestone-valuation-model.md) stages the buyer's payments so the buyer never carries more committed cost than the stage has de-risked. The seller's engineering spend needs the same treatment in the other direction: each tranche of $C_{invest}$ gates on a buyer commitment that reduces the seller's unprotected $Q$.

The buyer-side rule "payment follows proof, not calendar" has a seller-side twin: **engineering follows commitment, not optimism.** A tranche released against a date, a verbal assurance, or a forecast category converts a staged investment back into an unconditional one, which removes the protection the staging existed to provide.

Rule 3 of the milestone model already requires symmetric consequence when a stage fails on seller execution. The symmetric obligation is unwritten: what the buyer forfeits when a stage fails on buyer execution, whether that is data access never granted, stakeholders never convened, or an environment never provisioned.

---

## 6. Calibration status

> [!IMPORTANT]
> **Nothing here is fitted.** $p_{close}$ is not directly observable, and $\partial p_{close} / \partial C_{invest}$ cannot be estimated without a record of deals carrying both the investment made and the outcome. No such record exists in this repository. Treat these forms as a way to structure the decision and to name what a reviewer should ask for, not as a way to forecast a number. The same caution governs [03-mathematical-models.md](./03-mathematical-models.md) and applies here with more force, because this model has no parameter anchored in published literature at all.

The practical consequence: a manager can use section 4 to ask "what would have to be true about $\partial p_{close} / \partial C_{invest}$ for this spend to make sense," and can compare that answer against experience. That is a real use. Producing a number and calling it a probability is not.

---

## Open questions

- **Axiom I attributes specificity to the deal without naming the party who bears it.** Section 3 shows the bearer determines who needs governance. Revising the axiom is a breaking change to Part I and waits until this document has been reviewed.
- **Axiom I selects the motion on the combined level of the three costs.** Composition selects the motion; the sum sets the Turnkey and Structural boundary. The two claims are currently fused in one sentence.
- **$p_{close}$ needs an estimator.** The nearest available approach is retrospective scoring of closed deals, which carries hindsight bias and would be recorded with that status rather than presented as clean.
- **$R_{redeploy}$ needs a scoring method.** Redeployability is the term that separates a good forward-deployed engagement from an expensive one, and nothing in the repository measures it yet.

---

## Related

- **Research:** [klein-crawford-alchian.md](../02-research/klein-crawford-alchian.md) for quasi-rents and supplier exposure, [real-options.md](../02-research/real-options.md) for staging under irreversibility, [process-misfit.md](../02-research/process-misfit.md) for what drives $C_{deliver}$.
- **Buyer-side model:** [00-ilg-constitution.md](./00-ilg-constitution.md) Part III.
- **Functional forms:** [03-mathematical-models.md](./03-mathematical-models.md).
- **Staging in practice:** [milestone-valuation-model.md](../../practice/01-field-assets/milestone-valuation-model.md).
