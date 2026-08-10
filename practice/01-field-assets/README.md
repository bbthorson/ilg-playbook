# Field Assets

**Customer-facing tools and playbooks for executing the ILG, PLG, and SLG sales motions.**

---

## Overview

This directory contains the practical artifacts you deploy with customers during the sales process. These tools operationalize the ILG Constitution's theoretical framework into actionable customer engagements.

## Cross-Motion Diagnostics

These artifacts apply across all motions, not just ILG:

- **[Process Calculator](./process-calculator.md)** — Classifies a deal into SLG / PLG / ILG via a three-step rubric (Workflow Maturity → Market Stage → Transaction Cost).
- **[Friction Allocation Diagnostic](./friction-allocation-diagnostic.md)** — Checks whether any signal mechanism (artifact, channel, validator) satisfies the four Friction Allocation Principles derived from Axiom II. Use when designing new artifacts, diagnosing failing signal mechanisms, or evaluating channels.
- **[Costly Signal Discovery Scripts](./costly-signal-discovery-scripts.md)** — The escalating ladder of asks that converts stated interest into evidenced commitment, with the wording for each rung and how to read the response. Run during Blueprint discovery.
- **[ILG Deal Calibration Checklist](./ilg-deal-calibration-checklist.md)** — Pre-close self-audit for the AE and SE, run before the order form goes in. Carries every mandatory-veto condition so the deal team meets it before the manager does.

## Quantitative Diagnostics

Three instruments convert deal observations into comparable numbers. Each measures one term in the Surplus equation. All three rank deals against each other reliably and none of them predicts a close date. See [03-mathematical-models.md](../../theory/01-foundation/03-mathematical-models.md) for calibration status.

| Instrument | Measures | Run it when |
|---|---|---|
| **[Bilateral Asymmetry Scorecard](../02-internal-ops/04-incentives-asymmetry-scorecard.md)** | $\Delta_A = I_{seller} + I_{buyer}$ | Weekly forecast call, from first qualification onward |
| **[Consensus Friction Calculator](./consensus-friction-calculator.md)** | $F_{consensus}$ | After the Blueprint maps the buying committee |
| **[Milestone Valuation Model](./milestone-valuation-model.md)** | Staged uncertainty decay and gate payment structure | While drafting the MIP's timeline and commercial terms |

The three map onto the Three Sales Levers from Axiom II. The scorecard tells you how much uncertainty ($x$) there is to remove. The friction calculator tells you where the base cost ($c$) is concentrated. The milestone model is how you lower risk aversion ($a$) by giving hostages.

---

## ILG Motion (Implementation-Led Growth)

**When to Use:** Bridge deals (score 10-20 on diagnostic rubric)

The ILG motion uses three sequential artifacts to drive the bilateral asymmetry gap ($\Delta_A$) to zero before signature — reducing seller ignorance ($I_{seller}$) through discovery and buyer uncertainty ($I_{buyer}$) through costly signals:

### [01. Contextual Blueprint](./ilg-motion/01-discovery-contextual-blueprint.md)

**Purpose:** Maps $F_{base}$ and reduces **Seller Ignorance** ($I_{seller}$)

**Function:** Discovery and qualification tool that maps:
- Economic event (the catalyst)
- Political capital (who gains/loses power)
- Sacred cows (protected workflows/teams)
- Stakeholder DNA (champion, sponsor, saboteur)

**Reciprocity Gate:** Customer must provide current state diagram and data sample to proceed

**Outcome:** Disqualify bad-fit deals OR advance to Red Team Workshop

---

### [02. Red Team Protocol](./ilg-motion/02-validation-red-team-protocol.md)

**Purpose:** Reduces **Buyer Uncertainty** ($I_{buyer}$) through costly signals

**Function:** Pre-mortem workshop that:
- Surfaces hidden resistance (skeptics vs. adversaries)
- Validates technical feasibility
- Identifies failure modes before they happen
- Differentiates rational concerns from political sabotage

**Mechanism:** Prospective hindsight ("It's 6 months from now, the implementation failed. What went wrong?")

**Outcome:** Build containment strategy for adversaries, co-opt skeptics with validation

---

### [03. Mutual Implementation Plan](./ilg-motion/03-closing-mutual-implementation-plan.md)

**Purpose:** Locks surplus ($S > 0$) through bilateral governance before the Decay Clock erodes the buying window

**Function:** Contractual agreement that:
- Defines success metrics (RE-AIM framework)
- Allocates resources from both sides
- Creates shared accountability
- Turns resources into "tradeable currency"

**Mechanism:** Skin in the game for both parties — mutual commitments that make it costly for either side to defect

**Outcome:** Successful implementation, reduced churn risk, foundation for renewal

---

## The ILG Workflow

```
1. Triage (Process Calculator)
   ↓
2. Contextual Blueprint (Discovery + Qualification)
   ↓ [Reciprocity Gate: Customer provides artifacts]
   ↓
3. Red Team Workshop (Validation + Resistance Mapping)
   ↓ [Identify skeptics vs. adversaries]
   ↓
4. Mutual Implementation Plan (Governance + Close)
   ↓
5. Successful Implementation → Renewal
```

---

## SLG Motion (Sales-Led Growth)

**When to Use:** Nascent markets (0-1 Yes on Step 1 of the calculator). The category is not yet legible and the buyer does not know the problem can be solved.

### [01. Education-Led Motion](./slg-motion/01-education-led-motion.md)

**Purpose:** Reduces category search cost, the cognitive half of $F_{search}$

**Function:** Deliberately thin, because education-led selling is the best documented motion in B2B and this repo does not restate it. Covers only the ILG intersection:

- Which ILG artifacts to leave switched off, and what deploying each one costs in a nascent market
- Tripwires for the most common routing error, reading a mature market as nascent
- The pivot triggers that end the motion and hand the deal to the Blueprint

**Rule:** In SLG you are selling the problem. Every ILG artifact assumes the problem is already sold.

---

## PLG Motion (Product-Led Growth)

**When to Use:** Toaster deals (score 4-9 on diagnostic rubric)

### [PLG](./plg-motion)

**Strategy:** Optimize for velocity, not safety

**Characteristics:**
- Self-service trial
- Minimal sales involvement
- Standard demo and pricing
- Fast close, low friction

**Rule:** Never apply a Bridge motion to a Toaster (wastes time on unnecessary complexity)

---

## Triage Tool

### [Process Calculator](./process-calculator.md)

**Purpose:** Classify deals into SLG, PLG, or ILG by diagnosing market stage first, then asset specificity within mature markets.

**Three-step diagnostic:**
1. **Workflow Maturity Gate** — Level 1 Undefined (Chaos Trap, consulting first), Level 2 Emergent (proceed, Blueprint reconstructs the workflow), Level 3 Codified (proceed).
2. **Market Stage** — Nascent / Transitional / Mature, by category legibility.
3. **Transaction Cost** (Mature markets only) — score Integration depth + Workflow change scope + Consensus complexity + Retention horizon (1–5 each, sum 4–20).

**Motion mapping:** Nascent → SLG · Transitional 4–14 → SLG with ILG creep · Transitional 15–20 → ILG · Mature 4–9 → PLG · Mature 10–20 → ILG.

**Override Rule:** If prospect asks for pilot/POC, auto-classify as ILG regardless of cost score.

---

## Key Principles

### From the ILG Constitution

**Axiom I (Law of Economic Boundaries):**
> "Never apply a Bridge motion to a Toaster, and never sell a Bridge without a Blueprint."

**The Strategy:**
- **Toasters:** Optimize for speed (velocity)
- **Bridges:** Optimize for certainty (safety)

**The Economic Logic (Axiom II — Law of Friction):**

$$F_{effective} = (F_{search} + F_{consensus} + F_{implementation}) \cdot (1 + \Delta_A)$$

- **$F_{base}$ components**: search cost (finding the category), consensus cost (internal alignment + bargaining), implementation cost (deployment + sustained change).
- **$\Delta_A$**: bilateral asymmetry gap (the multiplier on friction) — composed of seller ignorance ($I_{seller}$) and buyer uncertainty ($I_{buyer}$).

ILG artifacts systematically reduce friction by driving $\Delta_A \to 0$ before signature — closing whichever gap is wider first — and by targeting specific cost components (Blueprint → consensus; Red Team → implementation forecasting; MIP → implementation governance).

---

## Usage Guidelines

### For Sales Reps

1. **Start with triage** - Use Process Calculator to classify the deal
2. **If Toaster** - Use PLG motion, focus on speed
3. **If Bridge** - Deploy ILG artifacts sequentially:
   - Blueprint first (discovery + qualification)
   - Red Team second (validation + resistance)
   - MIP third (governance + close)
4. **Respect the gates** - Don't skip reciprocity requirements
5. **Identify the saboteur** - Must be invited to Red Team Workshop

### For Sales Managers

**Deal Calibration Questions:**
- "Why is this a Bridge? Show me the calculator score."
- "Did they agree to the Technical Hook in the Blueprint?"
- "Did the Red Team find a failure mode, or was it 'happy ears'?"
- "Is the resource plan attached to the contract?"

**Forecast Rule:** "I will not commit a Bridge deal that has not survived a Red Team Workshop."

---

## Related Resources

- [ILG Constitution](../../theory/01-foundation/00-ilg-constitution.md) - Theoretical framework
- [Bilateral Asymmetry Scorecard](../02-internal-ops/04-incentives-asymmetry-scorecard.md) - Measure deal symmetry
- [Deal Calibration](../02-internal-ops/01-governance-deal-calibration.md) - Manager's forecast tool
- [Learning Plan](../03-learning-plan) - Training curriculum

---

**Remember:** The goal is not to close deals faster. The goal is to close deals that **stick**.
