# ILG Deal Calibration Checklist

**Purpose:** A pre-close self-audit for the AE and Solutions Engineer, run before an order form is submitted on a Bridge deal.

**Use when:** The deal is about to move to commercial execution. Run it together, in one sitting, before the manager review rather than after.

**Operationalizes:** The Boundary Condition from Axiom I and the trigger conditions in [Implementation Veto Authority](../02-internal-ops/06-governance-implementation-veto.md). Every mandatory-veto condition appears here so the deal team meets it first.

---

## How to use this

This is not the manager's review. The [Deal Review Checklist](../02-internal-ops/02-governance-review-checklist.md) is forensic and adversarial by design. This one is the deal team checking its own work while there is still time to fix something.

Answer every item with evidence rather than recollection. If you cannot point to a document, a recorded conversation, or a named person who confirmed it, the answer is no. Any **Stop** item that fails means the order form does not go in today.

---

## Part 1: The lane (Stop items)

- [ ] **Workflow maturity is Level 2 or Level 3.** Someone has seen the current process, and for Level 2 the Blueprint reconstructed it before the Red Team ran. *A Level 1 workflow is a mandatory veto.*
- [ ] **The Process Calculator score is on file and still current.** Re-score if integration scope or stakeholder count changed materially since the original.
- [ ] **The deal is not sitting on a boundary condition.** Walk the six in [01-sales-motion-comparison.md](../../theory/01-foundation/01-sales-motion-comparison.md). Name which one you checked and why it does not apply.

## Part 2: Asymmetry (Stop items)

- [ ] **The Asymmetry Scorecard has been run within the last 30 days.** $\Delta_A$ recorded: ______ *At or above 7.0 this is a mandatory veto.*
- [ ] **The wider half has a named next action.** Seller side wider means back to the Blueprint; buyer side wider means back to the Red Team. Record which and what was done.
- [ ] **The buyer has stated the cost of inaction in their own words.** Not the seller's number repeated back. Theirs, in a recorded call or in writing.

## Part 3: The Red Team (Stop items)

- [ ] **The workshop ran, with the likely saboteur in the room.** Date: ______ Attendees: ______
- [ ] **Edge cases identified:** ______ *Below eight on a genuine Bridge, the workshop was shallow. Re-run it.*
- [ ] **Every Showstopper has a written mitigation and a named owner.** *An open Showstopper is a mandatory veto.*
- [ ] **The buyer signed off on the gap analysis.** They have acknowledged in writing what the product will not do.

## Part 4: Costly signals

- [ ] **The buyer cleared rung 3 or higher** on the [discovery ladder](./costly-signal-discovery-scripts.md): three named departments convened, or better.
- [ ] **Each ask was paired with a seller commitment.** If you cannot name what you gave in exchange, the reciprocity gate was not really run.
- [ ] **No ask was silently substituted.** Where you accepted a summary in place of the artifact you requested, say so here and explain why it was sufficient: ______

## Part 5: Governance (Stop items)

- [ ] **A named customer project manager exists, with allocated hours.** Name: ______ Hours per week: ______ *Absent, this is a mandatory veto.*
- [ ] **The MIP has staged gates with defined acceptance criteria,** rather than one commitment at signature. This is what preserves the buyer's option value under Staged Commitment.
- [ ] **Both sides' resource commitments are in the contract,** not in a slide.
- [ ] **The Blueprint is ready to travel to Customer Success intact.** Without it, $\Delta_A$ resets to near maximum at handoff.

## Part 6: The veto holder

- [ ] **The assigned Solutions Engineering or Implementation lead is named in the CRM.** Name: ______
- [ ] **They have reviewed this checklist and either cleared the deal or exercised the veto.** Clearing carries their share of launch exposure, so this is a decision rather than a formality.
- [ ] **Where a mandatory condition applies and no veto was exercised, the written reason is recorded.** Silence on a known condition is not an option.

---

## The two questions that catch the most

Ask these last, out loud, to each other.

**"What do we still not know about their environment?"** A deal team that answers "nothing" has stopped looking rather than finished looking. Every Bridge has unmapped surface at signature. The question is whether you can name it and have bounded it in the MIP.

**"If this fails to launch, what will the post-mortem say we ignored?"** The answer is almost always already known to someone on the call. Prospective hindsight works here for the same reason it works in the Red Team, and it costs ninety seconds.

---

## Sign-off

| Role | Name | Date | Verdict |
|---|---|---|---|
| Account Executive | | | |
| Solutions Engineer / Implementation lead | | | Clear / Veto |

A veto recorded here is the cheapest one available. Every later stage costs more to stop.

---

## Related

- [06-governance-implementation-veto.md](../02-internal-ops/06-governance-implementation-veto.md) — The authority behind the Stop items, and the escalation path when the AE disagrees.
- [02-governance-review-checklist.md](../02-internal-ops/02-governance-review-checklist.md) — The manager review this checklist precedes.
- [costly-signal-discovery-scripts.md](./costly-signal-discovery-scripts.md) — The ladder referenced in Part 4.
- [process-calculator.md](./process-calculator.md) — Step 0 workflow maturity and the motion score.
- [04-incentives-asymmetry-scorecard.md](../02-internal-ops/04-incentives-asymmetry-scorecard.md) — Produces the $\Delta_A$ figure in Part 2.
