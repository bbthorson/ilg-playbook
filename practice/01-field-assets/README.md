---
title: "Field Assets"
layer: practice
status: active
---

# Field Assets

**The tools you deploy with a customer, indexed by the state the deal is in.**

Parent: [practice/](../) · Sibling: [02-internal-ops/](../02-internal-ops/)

Each document here carries its own header table stating its inputs, outputs, next step, and owner. This README points at them and does not restate them.

---

## Start here: which state are you in

The three states are defined in [Constitution Part I](../../theory/01-foundation/00-ilg-constitution.md). Name the state, then open the artifact.

| State | Your question | Asset |
|---|---|---|
| **Market** | Which motion does this deal take? | [Deal Triage Calculator](./deal-triage-calculator.md) |
| **Deal** (T0) | What do I not yet know about their environment? | [01. Contextual Blueprint](./ilg-motion/01-discovery-contextual-blueprint.md) |
| **Deal** (T0) | How does this implementation fail? | [02. Red Team Protocol](./ilg-motion/02-validation-red-team-protocol.md) |
| **Deal** (T0) | Who commits what, and what happens when a stage fails? | [03. Mutual Implementation Plan](./ilg-motion/03-closing-mutual-implementation-plan.md) |
| **Relationship** (T1+) | Did value land, and have we re-earned the renewal? | [04. Sustaining Adoption Review](./ilg-motion/04-sustaining-adoption-review.md) |

The four ILG artifacts run in order and each gates the next. The Deal Triage Calculator decides whether you run them at all.

---

## By motion

| Motion | When | Assets |
|---|---|---|
| **ILG** | Structural deals, calculator score 10 to 20 | [ilg-motion/](./ilg-motion/) — the four artifacts above |
| **PLG** | Turnkey deals, score 4 to 9 | [plg-motion/](./plg-motion/) — [order protocol](./plg-motion/01-velocity-standard-order-protocol.md), [prospect evaluation](./plg-motion/prospect-evaluation.md), [order form](./plg-motion/order-form.md) |
| **SLG** | Nascent markets, 0 to 1 Yes on calculator Step 1 | [slg-motion/01-education-led-motion.md](./slg-motion/01-education-led-motion.md) — deliberately thin, covering only the ILG intersection |

---

## Cross-motion diagnostics

These serve whichever state you are in rather than sitting at one point in the sequence.

| Asset | What it does |
|---|---|
| [Friction Allocation Diagnostic](./friction-allocation-diagnostic.md) | Tests whether a signal mechanism satisfies the four Friction Allocation Principles from Axiom II. Use when designing an artifact, diagnosing a failing signal, or evaluating a channel. |
| [Costly Signal Discovery Scripts](./costly-signal-discovery-scripts.md) | The escalating ladder of asks that converts stated interest into evidenced commitment. Run during Blueprint discovery. |
| [ILG Deal Calibration Checklist](./ilg-deal-calibration-checklist.md) | Pre-close self-audit for the AE and SE, carrying every mandatory-veto condition so the deal team meets it before the manager does. |

---

## Quantitative diagnostics

Three instruments convert deal observations into comparable numbers. Each measures one term in the Surplus equation. All three rank deals against each other and none predicts a close date. Calibration status is in [03-mathematical-models.md](../../theory/01-foundation/03-mathematical-models.md).

| Instrument | Measures | Run it when |
|---|---|---|
| [Bilateral Asymmetry Scorecard](../02-internal-ops/04-incentives-asymmetry-scorecard.md) | $\Delta_A = I_{seller} + I_{buyer}$ | Weekly forecast call, from first qualification onward |
| [Consensus Friction Calculator](./consensus-friction-calculator.md) | $F_{consensus}$ | After the Blueprint maps the buying committee |
| [Milestone Valuation Model](./milestone-valuation-model.md) | Staged uncertainty decay and gate payment structure | While drafting the MIP timeline and commercial terms |

The three map onto the Three Sales Levers from Axiom II. The scorecard says how much uncertainty ($x$) there is to remove. The friction calculator says where base cost ($c$) is concentrated. The milestone model lowers risk aversion ($a$) by giving hostages.

---

## Related

- **Theory:** [00-ilg-constitution.md](../../theory/01-foundation/00-ilg-constitution.md) for the axioms, [01-sales-motion-comparison.md](../../theory/01-foundation/01-sales-motion-comparison.md) for why each motion fits where.
- **Manager tools:** [02-governance-review-checklist.md](../02-internal-ops/02-governance-review-checklist.md) carries the forecast questions and the commit rule.
- **Before modifying any asset here:** [02-cfir-field-mapping.md](../../theory/01-foundation/02-cfir-field-mapping.md) says which research construct each section operationalizes.
