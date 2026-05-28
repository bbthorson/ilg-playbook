# Field Assets

**Customer-facing tools and playbooks for executing ILG and PLG sales motions.**

---

## Overview

This directory contains the practical artifacts you deploy with customers during the sales process. These tools operationalize the ILG Constitution's theoretical framework into actionable customer engagements.

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

**Purpose:** Classify deals as Bridge or Toaster

**Diagnostic Rubric (4 factors, scored 1-5 each):**
1. Tech Specificity: How hard to rip out?
2. Org Specificity: How many habits change?
3. Political Complexity: Who can say no?
4. Retention Horizon: One-shot or repeat game?

**Decision Matrix (Score Range: 4-20):**
- Score 4-9 → Toaster (use PLG/SLG motion)
- Score 10-20 → Bridge (use ILG motion)

**Override Rule:** If prospect asks for pilot/POC, automatically classify as Bridge (score 20)

---

## Key Principles

### From the ILG Constitution

**Axiom I (Law of Commercial Friction):**
> "Never apply a Bridge motion to a Toaster, and never sell a Bridge without a Blueprint."

**The Strategy:**
- **Toasters:** Optimize for speed (velocity)
- **Bridges:** Optimize for certainty (safety)

**The Economic Logic:**

High asset specificity (Bridge) creates high effective friction:
- $F_{base}$: Implementation effort, consensus costs, switching costs (the work)
- $\Delta_A$: Bilateral asymmetry gap (the fear multiplier) — composed of seller ignorance ($I_{seller}$) and buyer uncertainty ($I_{buyer}$)

ILG artifacts systematically reduce these costs by driving $\Delta_A \to 0$ before signature — closing whichever gap is wider first.

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

- [ILG Constitution](../00-foundation/ilg-constitution.md) - Theoretical framework
- [Bilateral Asymmetry Scorecard](../04-internal-ops/04-incentives-asymmetry-scorecard.md) - Measure deal symmetry
- [Deal Calibration](../04-internal-ops/01-governance-deal-calibration.md) - Manager's forecast tool
- [Learning Plan](../05-learning-plan) - Training curriculum

---

**Remember:** The goal is not to close deals faster. The goal is to close deals that **stick**.
