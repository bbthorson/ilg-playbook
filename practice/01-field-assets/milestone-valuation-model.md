# Milestone Valuation Model

**Purpose:** To design MIP phase gates so that each one resolves a defined tranche of uncertainty, and to structure payments so the buyer never carries more committed cost than the stage has de-risked.

**Use when:** The Red Team has surfaced the failure modes and you are drafting the MIP's timeline and commercial terms.

**Operationalizes:** Staged Commitment (Axioms II + III). Theory in the [Constitution](../../theory/01-foundation/00-ilg-constitution.md), research in [real-options.md](../../theory/02-research/real-options.md).

---

## The premise

A buyer who accepts the business case and still declines is usually not stalling. They are pricing the option to wait, and pricing it correctly.

When an investment is irreversible and the environment is uncertain, the ability to defer carries real economic value. Demanding full commitment at signature asks the buyer to destroy that entire option in one step, which they will often refuse to do even when expected return is positive. Staging does not reduce the work. It reduces how much of the work must be committed before the buyer knows whether it will succeed.

This model is what separates a phased *project plan* from a phased *commitment*. A project plan with four phases and one signature preserves no option value. The buyer must be able to stop.

---

## The stage equation

For each stage $m$, the expected surplus is:

$$S_m = p_m \cdot \left[ V_{gross,m} - \left(a \cdot x_m^2 + c_m\right) \right]$$

| Term | Meaning |
|---|---|
| $p_m$ | Probability of achieving stage $m$, from your own delivery history in comparable environments |
| $V_{gross,m}$ | Incremental value the buyer realizes on completing stage $m$ |
| $a$ | Risk aversion coefficient, anchored at 2.25 |
| $x_m$ | Residual uncertainty entering stage $m$, normalized to $[0, 1]$ |
| $c_m$ | Payment allocated to stage $m$ |

Uncertainty decays as gates clear, with each stage resolving a fraction of what remains:

$$x_m = x_0 \cdot \prod_{k=1}^{m}(1 - \mu_k)$$

Where $x_0$ is the normalized gap from the [Bilateral Asymmetry Scorecard](../02-internal-ops/04-incentives-asymmetry-scorecard.md) and $\mu_k$ is the fraction of remaining uncertainty that stage $k$ resolves.

---

## The three design rules

**1. Low commitment before validation.** Capital committed before technical validation is limited to baseline setup. The buyer must be able to exit the Blueprint stage having spent an amount they would not need to defend internally.

**2. Payment follows proof, not calendar.** Transfers trigger on mutual sign-off against written acceptance criteria, never on elapsed time. A date-triggered payment converts a real option back into an unconditional commitment, which defeats the entire structure.

**3. Symmetric consequence.** If a stage fails on seller execution, unused fees are credited or refunded and the seller supplies remediation engineering without additional billing. Without this, the gate is a checkpoint the buyer cannot act on, and it carries no option value at all.

Rule 3 is the one most often dropped in negotiation, and dropping it removes the mechanism. A gate the buyer cannot walk away from is a milestone, not an option.

---

## Reference stage structure

Percentages are of annual contract value. Adjust the count and the decay profile to the deal. The shape is what matters.

| Stage | Acceptance criteria | Uncertainty resolved ($\mu_m$) | Residual ($x_m$) | Payment | Risk-sharing term |
|---|---|---|---|---|---|
| **0. Blueprint** | Architecture audit and data schema mapping complete and signed. | 25% | $x_1 = 0.75\,x_0$ | Discovery fee only | Fully refundable if the audit finds the architecture unworkable. No license commitment. |
| **1. Core integration** | API throughput and security protocols verified in sandbox against written benchmarks. | 50% | $x_2 = 0.375\,x_0$ | 25% | Contingent on meeting the stated throughput and security benchmarks. |
| **2. Pilot** | A defined user group operating on live production workflows. | 80% | $x_3 = 0.075\,x_0$ | 35% | Service level guarantees on stability and latency, with credit clawback. |
| **3. Full rollout** | Enterprise deployment and system sign-off. | Remaining | approaching 0 | 40% | Standard recurring license and maintenance terms begin. |

Each $\mu_m$ applies to what remains rather than to the original gap, which is why the residual column compounds downward rather than stepping linearly.

---

## How to use it in a negotiation

**Work backwards from the buyer's exit point.** Ask which stage they would need to be able to stop at for the first signature to feel survivable. That stage is where the largest refundable component belongs.

**Quantify what the buyer gives up.** The buyer holds the option today. Naming its value, and then showing that the staged structure returns most of it, is a stronger argument than any return projection. Buyers who resist discounting will accept staging, because staging costs the seller cash flow timing rather than margin.

**Check that payment never leads proof.** Walk the table left to right. At every row, committed payment to date should sit below value realized to date. If a row breaks that rule, the buyer is financing the seller's delivery risk, and they will find it during legal review.

**Do not stage a Toaster.** Gate design carries real administrative cost on both sides. Below the ILG boundary the structure destroys more surplus than the option value it preserves. Confirm with the [Process Calculator](./process-calculator.md) first.

---

## Failure modes

- **Phases without exits.** Four stages, one signature, no ability to stop. Preserves no option value and produces the same resistance as a single commitment.
- **Calendar gates.** Payment triggered by date rather than acceptance. Reintroduces unconditional commitment.
- **Asymmetric consequence.** The buyer is bound at each gate and the seller is not. The buyer's counsel will find this, and it damages more trust than the staging built.
- **Vanity criteria.** Acceptance conditions written so loosely that no outcome fails them. A gate that cannot fail resolves no uncertainty, so $\mu_m$ is effectively zero regardless of what the plan claims.

---

## Related

- [real-options.md](../../theory/02-research/real-options.md) — Dixit-Pindyck. Why waiting has value and staging recovers it.
- [00-ilg-constitution.md](../../theory/01-foundation/00-ilg-constitution.md) — Staged Commitment bridge concept.
- [Mutual Implementation Plan](./ilg-motion/03-closing-mutual-implementation-plan.md) — The artifact these gates go into.
- [Bilateral Asymmetry Scorecard](../02-internal-ops/04-incentives-asymmetry-scorecard.md) — Supplies $x_0$.
