# Implementation Veto Authority

**Purpose:** To grant Solutions Engineering and Implementation formal authority to halt a Bridge deal before signature when pre-sale validation surfaces unmitigated operational risk, and to attach consequences to that authority so it cannot drift.

**Use when:** A Bridge deal is moving toward order form submission. The veto is exercised before commercial execution, never after.

**Operationalizes:** Axiom III. Residual control rights (Grossman-Hart-Moore) are what governance allocates, and this document allocates one specific right: who decides when the contract is silent on whether the environment is ready.

---

## Why the authority has to be real

The Manager's Oath in the [Deal Review Checklist](./02-governance-review-checklist.md) commits sales management to running the Red Team. It does not give the people who run that workshop any power over the outcome. When the party with the best information about implementation risk can only advise, three things follow from the framework directly.

An advisory veto allocates no residual control right. Grossman-Hart-Moore's result is that contracts covering complex transactions cannot specify every future state, so what governs those states is the pre-agreed allocation of authority. If Solutions Engineering holds no authority, the allocation defaults to whoever owns the number, and that is the party with the strongest incentive to discount the risk.

An advisory veto is also cheap talk. Under Axiom II, a signal carries information only when producing it costs something. A warning that a deal will fail, issued by someone who bears no consequence either way and can be overruled without a record, is exactly the babbling equilibrium the framework describes. Reps learn to route around it within a quarter.

The correction is not simply to make the veto binding. An unaccountable hard stop recreates the problem one level up, because Friction Allocation Principle 4 requires that adjudicators bear the consequences of their validation. A veto holder who blocks deals at no cost to themselves will over-block, and the structure drifts from adjudication toward obstruction. The authority below binds, and it carries cost in both directions.

---

## Who holds it

The named Solutions Engineering or Implementation lead assigned to the deal. Not the function in general, and not a committee. A single named person per deal, recorded in the CRM at the point the deal is classified as a Bridge.

The veto covers one question: **can this environment absorb this implementation on the terms being proposed?** It does not extend to pricing, competitive strategy, contract language, or account selection. A veto exercised on any of those grounds is void, and Sales should escalate it as such.

---

## Trigger conditions

The veto is available at any time before order form submission. It becomes **mandatory** when any of the following holds, meaning the veto holder must either exercise it or record in writing why the condition does not apply:

| Condition | Instrument | Threshold |
|---|---|---|
| Workflow cannot be mapped | [Process Calculator](../01-field-assets/process-calculator.md) Step 0 | Level 1, Undefined |
| Bilateral asymmetry unresolved | [Asymmetry Scorecard](./04-incentives-asymmetry-scorecard.md) | $\Delta_A$ at or above 7.0 |
| Showstopper unmitigated | [Red Team Protocol](../01-field-assets/ilg-motion/02-validation-red-team-protocol.md) | Any finding classified Showstopper without a written mitigation and a named owner |
| Buyer resources absent | [MIP](../01-field-assets/ilg-motion/03-closing-mutual-implementation-plan.md) | No named customer project manager, or committed hours below the floor set during calibration |
| Red Team not run | Deal record | Bridge deal reaching order form without a completed workshop |

Discretionary vetoes outside these conditions are permitted and follow the same procedure. The mandatory list exists so that silence on a known condition is itself a recorded decision.

---

## Procedure

1. **Exercise.** The veto holder records the veto in the deal record: the condition triggered, the evidence, and the specific change that would clear it. A veto that does not name a clearing condition is incomplete and does not take effect.
2. **Effect.** The order form cannot be submitted. This is a hard stop, and it holds while escalation runs.
3. **Remedy.** The default path is that the deal team clears the named condition and the veto holder confirms. Most vetoes should resolve here, and a veto function whose outputs are mostly escalations rather than remediations is being used wrongly by someone.
4. **Escalation.** Sales may escalate to a named executive, in practice the CRO with the delivery organization's lead present. Escalation is time-boxed to five business days. Silence at expiry sustains the veto rather than clearing it, because the default under uncertainty is the status quo.
5. **Override.** The executive may override. The override is recorded with its rationale and carries the compensation consequences below. An unrecorded override does not exist, and the veto stands.

---

## Skin in the game

The authority binds in both directions. Each party to the decision holds exposure to the outcome, which is what keeps the adjudicator from drifting.

**The veto holder who clears a deal shares its launch risk.** Where the [vested commission](./03-incentives-vested-commission.md) exposes the rep to clawback on a failure to launch, the clearing veto holder carries a proportional stake in the same outcome, set during calibration. Clearing a deal is an act of validation, and validation without exposure is the governance-drift failure mode named in Axiom III.

**The veto holder who blocks wrongly accrues a recorded false positive.** A veto is judged wrong when the deal is overridden and launches successfully within the standard window, or when the buyer implements comparably with a competitor. False-positive rate is reviewed quarterly alongside launch success. Neither number is meaningful alone; a veto function with a zero false-positive rate is almost certainly under-blocking.

**The rep who honors a veto and loses the deal carries no penalty.** This has to be stated explicitly or the compensation structure will punish compliance and the veto will be routed around regardless of what this document says. A lost deal following a sustained veto is a qualification outcome, not a performance event, and it does not count against quota attainment relief.

**The rep who proceeds under override carries full exposure.** Where an override was granted and the implementation subsequently fails to launch, the standard clawback applies and the Safe Harbor provisions are void. The override is the moment the risk was accepted knowingly, and the Safe Harbor exists for risks nobody could see.

---

## What this does not fix

The veto is a gate, not a diagnosis. It stops a deal that should not proceed, and it does nothing to make that deal viable. A team that finds itself exercising the authority frequently has a qualification problem upstream in the Process Calculator, and adding gate strength will not repair it.

The veto also cannot substitute for delivery capability. Boundary condition 6 in [01-sales-motion-comparison.md](../../theory/01-foundation/01-sales-motion-comparison.md) applies here: an organization that lacks the depth to run a genuine Red Team will produce veto holders who clear everything, and the structure will be formally correct and practically empty.

---

## Calibration parameters

Set these during the [setup workshop](./00-setup-implementation-guide.md). Every value is organization-specific and none is supplied here as a default.

| Parameter | Set to |
|---|---|
| Veto holder's share of clawback exposure | ____ percent of the rep's exposure |
| Committed customer PM hours floor | ____ hours per week |
| Escalation window | 5 business days (recommended) |
| Escalation authority | Named role, not a committee |
| False-positive review cadence | Quarterly (recommended) |

---

## Related

- [00-ilg-constitution.md](../../theory/01-foundation/00-ilg-constitution.md) — Axiom III, and the incomplete-contracts mechanism this document allocates.
- [incomplete-contracts.md](../../theory/02-research/incomplete-contracts.md) — Grossman-Hart-Moore. Why authority allocation, rather than better drafting, governs unspecified states.
- [03-incentives-vested-commission.md](./03-incentives-vested-commission.md) — The rep-side exposure this document extends to the delivery organization.
- [02-governance-review-checklist.md](./02-governance-review-checklist.md) — Where the trigger conditions are checked in the normal review cycle.
- [05-diagnostics-friction-efficiency-index.md](./05-diagnostics-friction-efficiency-index.md) — A falling cohort index predicts rising veto frequency.
- [Red Team Protocol](../01-field-assets/ilg-motion/02-validation-red-team-protocol.md) — Source of the Showstopper classification that triggers a mandatory veto.
