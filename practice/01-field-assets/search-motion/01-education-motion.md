---
title: "The Education Motion"
layer: practice
status: active
version: 1.0
operationalizes: [axiom-1]
canonical_source: theory/01-foundation/00-tcg-constitution.md
---

# The Education Motion

Version: 1.0
Component: Search. Deals whose direction points at the buyer's inability to find and compare.
Audience: Account Executives / Founders selling into an unformed category
Goal: To sell in a market that does not yet know it is a market, and to recognize the moment that stops being true.

**Canonical Reference:** [TCG Constitution, Axiom I (Law of Transaction Cost Composition)](../../../theory/01-foundation/00-tcg-constitution.md). The search-led motion is what Axiom I prescribes when the category itself is illegible. The reasoning is in [01-motion-taxonomy.md](../../../theory/01-foundation/01-motion-taxonomy.md).

| | |
|---|---|
| **Inputs** | A deal the [Deal Triage Calculator](../deal-triage-calculator.md) reads as search-dominant at a level of 15 or above. The category is not legible to this buyer. |
| **Outputs** | A visionary buyer who can name the problem, quantify the cost of inaction, and fund a line item that did not previously exist. |
| **Next step** | Standard commercial terms. If any pivot trigger below fires, re-run the calculator and deploy the [Contextual Blueprint](../implementation-motion/01-discovery-contextual-blueprint.md). |
| **Owner** | AE or founder. No solutions engineering required at this stage. |
| **Reduces** | Category search, the cognitive half of $F_{search}$ (Axiom I). |

> [!IMPORTANT]
> **This document is deliberately thin.** Education-led selling is the best documented motion in B2B, and this repo has no ambition to restate it. What follows is only the part that intersects the implementation-led motion: how to tell you are search-dominant rather than somewhere else, what implementation machinery to keep switched off while you are, and when to switch it on.

## The Triage Check

Before using this motion, confirm you belong in it.

- **Direction:** search-dominant, meaning the search component holds at least half of effective cost. Any other reading means you are not here.
- **Step 0 workflow gate:** passed. A Level 1 undefined workflow is a [Chaos Trap](../deal-triage-calculator.md), not an search-dominant deal, no matter how new the category looks.
- **Override check:** the buyer has NOT asked for a pilot, POC, or custom security review. Any of those routes to the implementation instruments whatever the counts say, because the buyer is reporting a perceived risk the counts missed.

## Where the real playbook lives

The activities themselves are covered well elsewhere, and a rep should learn them from the source rather than from a summary here.

| Need | Go to |
|---|---|
| Commercial teaching, reframing, taking control of the conversation | [The Challenger Sale](https://www.challengerinc.com/) |
| Qualification discipline in a long, low-information cycle | [MEDDICC](https://meddicc.com/) |
| Early-adopter dynamics and the transition out of a nascent market | Geoffrey Moore, *Crossing the Chasm* |
| Buyer indecision, and why urgency tactics backfire | [The JOLT Effect](https://www.jolteffect.com/), summarized in [fear-of-failure.md](../../../theory/02-research/fear-of-failure.md) |

These are external and unaffiliated. Nothing in this framework depends on adopting any of them.

## The counter-example: implementation machinery to leave switched off

This is the section that earns the file. Every implementation artifact has a search-led analogue that costs a fraction as much, and deploying the implementation version against a search-dominant deal is the **over-frictioned failure mode** from Axiom I. The Boundary Condition requires that friction scale with asset specificity ($F_{deployed} \sim k$). Where the buyer has not committed to anything specific yet, $k$ is low and heavy friction destroys the surplus it was meant to protect.

| Activity | Implementation-led deploys | Search-led deploys instead | What running the implementation version costs you |
|---|---|---|---|
| **Discovery** | [Contextual Blueprint](../implementation-motion/01-discovery-contextual-blueprint.md). Maps architecture, political capital, sacred cows, saboteurs. | A problem-framing conversation. "What does good look like, and what is the status quo costing you." | You map an environment for a buyer who has not yet agreed the problem is worth solving. The reciprocity gate fails because you have not earned the right to ask. |
| **Validation** | [Red Team pre-mortem](../implementation-motion/02-validation-red-team-protocol.md). Surfaces failure modes for a planned implementation. | A reference architecture or vision artifact. What the world looks like after. | You run a pre-mortem on an implementation the buyer has not decided to attempt. It reads as manufactured doubt about your own product. |
| **Close** | [Mutual Implementation Plan](../implementation-motion/03-closing-mutual-implementation-plan.md). Bilateral commitments, resource expiry, gates. | Standard order form and a light statement of work. | You demand hostages from a buyer whose live alternative is doing nothing at all. Staged commitment has nothing to stage against. |
| **Stakeholders** | Identify and contain the saboteur. Map a committee of 3 to 10. | Usually 1 to 3 people, often a single visionary with discretionary budget. | You go looking for political opposition in a room that has not formed one yet. |
| **Proof** | Costly signals. Paid pilot, red team, demonstrated work. | Category credibility. Public point of view, case studies, being publicly wrong in useful ways. | Costly signals separate quality from noise (the Single Crossing Property, meaning a signal only works when it is cheaper for a genuinely good vendor to produce). In a nascent market there is no field to separate yourself from yet. |
| **Comp** | [Vested commission](../../02-internal-ops/03-incentives-vested-commission.md) tied to implementation outcomes. | Traditional ACV commission. | You penalize a rep for retention outcomes in a category whose implementation patterns nobody has established. |

The rule in one line: **search-led sells the problem, and the implementation artifacts all assume the problem is already sold.**

## Misclassification tripwires

The most common routing error here is reading a legible category as an unformed one. Absence of visible competition feels like a new category and usually is not, and an unnamed category scores the maximum search cost rather than the minimum. Run these before committing to the search-led motion.

**1. The three-vendor test.** Ask the buyer directly to name three vendors who solve this. If they can, the category is legible to them regardless of how new it feels to you, two of the four search evidence items are satisfied, and the search gap has largely closed. Re-count and read the direction again.

**2. The line-item test.** Ask where the budget would come from. A genuinely nascent deal has no line item and the buyer must create one, usually by taking it from something else. If a budget line already exists with your category's name on it, the market formed without you noticing.

**3. The "to us" test.** Distinguish "nobody sells this" from "nobody sells this to *us*." A category can be mature in one segment and illegible in another. The second case is a distribution problem, not a nascent market, and the buyer will still compare you against the mature-segment vendors once procurement engages.

**4. The visionary trap.** One excited executive is not evidence of a nascent market. Mature-market deals also produce enthusiastic champions. The distinguishing question is whether the *organization* can evaluate you, not whether your champion is keen.

**5. The Chaos Trap confusion.** A buyer with no documented workflow in a legible category is a Level 1 workflow problem, not an search-dominant deal. Selling vision into an organization that cannot describe its own process produces an unimplementable win. Route to consulting.

## The motion itself

Three moves. Each has one output that gates the next.

**Step 1. Frame the problem.** Teach the buyer what the status quo is costing them, in their numbers. Do not present product. *Output: the buyer states the problem in their own words and attaches a figure to it.* Until that happens you have an interested listener rather than a deal.

**Step 2. Build the category.** Co-design what a solution looks like. Reference architectures, "what good looks like" sessions, willingness to describe the shape of the answer even where you do not supply all of it. *Output: the buyer can articulate evaluation criteria.*

Note what Step 2 does. The moment a buyer can state evaluation criteria, they can comparison shop, which is the beginning of category legibility. Education-led selling works by making its own market mature, which is why the motion has a shelf life and why the pivot triggers below eventually fire on every successful search-dominant deal.

**Step 3. Create the budget and close.** Standard commercial terms. Traditional order form. Resist adding governance the deal does not need. *Output: signature, and a case study that establishes the category for the next wave of buyers.*

## Pivot triggers: when to stop educating

Any one of these means the deal is no longer search-dominant. Stop, re-run the [Deal Triage Calculator](../deal-triage-calculator.md), and if the score lands at 10 or above in a now-mature market, deploy the [Contextual Blueprint](../implementation-motion/01-discovery-contextual-blueprint.md).

| Trigger | What it signals | Action |
|---|---|---|
| Buyer names 3+ credible vendors | The category went legible, possibly during your own sales cycle | Re-count. The search gap has closed and the vector has rotated. |
| Buyer asks for a pilot or POC | The buyer perceives Structural-level implementation risk | **Route to the implementation instruments.** Calculator override rule, no judgment required. |
| Procurement, security review, or legal engages | Consensus cost just arrived | Re-count the veto holders. Deploy the Blueprint's stakeholder mapping. |
| Stakeholder count passes 3 | You now have a buying committee and a probable saboteur | Deploy Blueprint. Map the committee. |
| Integration scope reaches core systems | Asset specificity ($k$) rose above the threshold | Deploy Blueprint, then Red Team. |
| Analyst coverage or a category name appears | The market matured underneath you | Re-count the search evidence items. |

[01-motion-taxonomy.md](../../../theory/01-foundation/01-motion-taxonomy.md) describes the two routes here. A **maturing category** moves the whole market and every deal in it. **Complexity discovery** moves one deal that turned out deeper than scoped. The response is the same in both cases, and the second one is the one reps miss, because nothing external changes to prompt a re-score.

> [!WARNING]
> Missing a pivot trigger produces the under-frictioned Structural deal failure mode from Axiom I. You keep educating a buyer who has moved on to evaluating implementation risk, they read the absence of rigor as a reason to build internally, and the deal ends as "we decided to handle this in-house."

## Related

- **Theory:** [01-motion-taxonomy.md](../../../theory/01-foundation/01-motion-taxonomy.md) covers search-led against implementation-led in depth, including why educational friction and structural friction call for opposite behavior.
- **Triage:** [deal-triage-calculator.md](../deal-triage-calculator.md). A search-dominant direction routes here, and any rotation away from search routes out.
- **Constitution:** [Axiom I and the Boundary Condition](../../../theory/01-foundation/00-tcg-constitution.md). Over-frictioning a nascent deal and under-frictioning a matured one are the two failure modes this document exists to prevent.
- **Sibling motions:** [implementation-motion/](../implementation-motion/) for Structural deals, [turnkey-motion/](../turnkey-motion/) for Turnkey deals.
