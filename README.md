# Implementation-Led Growth (ILG) Knowledge Base

**A new paradigm for enterprise software sales based on Transaction Cost Economics and Game Theory.**

---

## What is ILG?

**Implementation-Led Growth (ILG)** is a sales methodology designed for high-friction B2B software where traditional Product-Led Growth (PLG) or Sales-Led Growth (SLG) fails. 

The core insight: **In high-specificity deals, reducing friction creates more surplus than increasing value. But friction is amplified by information gaps, and value erodes with time — so the goal is to close the asymmetry gap faster than urgency decays.**

In complex enterprise deals, buyers face:
- **High base friction** ($F_{base}$) — search costs, consensus costs, implementation costs, switching costs
- **Bilateral asymmetry** ($\Delta_A$) — seller ignorance and buyer uncertainty amplify perceived friction
- **Decaying urgency** ($\delta$) — the triggering event that opened the buying window has a half-life
- **Asset specificity** ($k$) — deep workflow integration creates high switching costs

ILG addresses these through **discovery artifacts** (Blueprints) that reduce seller ignorance and **costly signals** (Red Teams, paid pilots) that reduce buyer uncertainty — driving $\Delta_A \to 0$ before the Decay Clock runs out.

---

## Repository Structure

### [00-foundation](./00-foundation)
**The core theoretical framework**

- **[ILG Constitution](./00-foundation/ilg-constitution.md)** - The complete economic and behavioral theory
  - Part I: Core Economic Theory (Fundamental Equation, Deal Zone, Repeated Game)
  - Part II: The Three Axioms (The System Core)
  - Part III: Organizational Corollary (Mapping Costs to Departments)
  - Part IV: Strategy & Triage Protocol (Chaos Trap Gate, 4-Factor Diagnostic Rubric, Bridge vs. Toaster)
  - Part V: The Artifacts (Blueprint, Red Team Workshop, Mutual Implementation Plan)
- **[Sales Motion Comparison](./00-foundation/sales-motion-comparison.md)** - ILG vs. PLG vs. SLG decision framework
- **[CFIR Field Mapping](./00-foundation/cfir-field-mapping.md)** - How Implementation Science constructs map to ILG field assets

**Start here** to understand the theoretical foundation.

---

### [01-research](./01-research)
**Academic evidence and deep dives**

Supporting research that validates the ILG framework:
- [cfir.md](./01-research/cfir.md) - Implementation Science framework
- [costly-signals.md](./01-research/costly-signals.md) - Signaling theory in sales
- [fear-of-failure.md](./01-research/fear-of-failure.md) - The JOLT Effect and buyer inaction
- [game-theory-and-nrr.md](./01-research/game-theory-and-nrr.md) - Repeated games and retention
- [total-cost-economics.md](./01-research/total-cost-economics.md) - Transaction cost theory

---

### [02-market-data](./02-market-data)
**Empirical validation and case studies**

*Currently being populated*

---

### [03-field-assets](./03-field-assets)
**Practical tools for sales execution**

Operational playbooks and processes:
- [ilg-motion/](./03-field-assets/ilg-motion) - Implementation-Led Growth motion
- [plg-motion/](./03-field-assets/plg-motion) - Product-Led Growth motion
- [process-calculator.md](./03-field-assets/process-calculator.md) - Deal triage tool

---

### [04-internal-ops](./04-internal-ops)
**Governance and alignment mechanisms**

Internal tools for organizational alignment:
- [asymmetry-scorecard.md](./04-internal-ops/04-incentives-asymmetry-scorecard.md) - Diagnose information gaps
- [deal-calibration.md](./04-internal-ops/01-governance-deal-calibration.md) - Qualify deal fit
- [vested-commission.md](./04-internal-ops/03-incentives-vested-commission.md) - Align rep incentives with outcomes

---

### [05-learning-plan](./05-learning-plan)
**Training curriculum and onboarding**

- [curriculum.md](./05-learning-plan/curriculum.md) - Training program structure

---

### [06-tools](./06-tools)
**AI and automation resources**

- [ai-persona.md](./06-tools/ai-persona.md) - Instructions for AI-assisted deal analysis

---

## Quick Start

1. **Understand the Theory** → Read [ILG Constitution](./00-foundation/ilg-constitution.md)
2. **See the Evidence** → Browse [01-research](./01-research) for academic backing
3. **Apply in Practice** → Use [03-field-assets](./03-field-assets) for execution
4. **Align Your Team** → Implement [04-internal-ops](./04-internal-ops) governance

---

## Core Concepts at a Glance

### The Teaching Model (4 Concepts)

$$S = \left(V_{solution} \times e^{-\delta t} - V_{next\_best}\right) - F_{base} \times (1 + \Delta_A)$$

Where:
- $S$ = Deal Surplus (must be > 0 for a deal to close)
- $\Delta_A$ = Bilateral Asymmetry Gap — composed of Seller Ignorance ($I_{seller}$) and Buyer Uncertainty ($I_{buyer}$)
- $\delta$ = Decay Rate (how quickly urgency fades after the triggering event)
- Subject to: $k > k_{threshold}$ (high asset specificity) AND $n_{viable} \leq n_{max}$ (thin market)

### The Three Axioms

1. **Law of Economic Boundaries** — Asset Specificity determines whether ILG applies (Bridge vs. Toaster).
2. **Law of Asymmetry Convergence** — Drive $\Delta_A \to 0$ by closing whichever gap is wider first (seller ignorance or buyer uncertainty).
3. **Law of Bilateral Governance** — Long-term alignment requires mutual skin in the game (Principal-Agent Alignment).

### Bridge vs. Toaster

**The Toaster (Low Friction):**
- Score: 4-9 on Diagnostic Rubric (4 factors, scored 1-5 each)
- Strategy: SLG/PLG (optimize for velocity)
- Example: Simple SaaS tools, low integration

**The Bridge (High Friction):**
- Score: 10-20 on Diagnostic Rubric
- Strategy: ILG (optimize for safety and certainty)
- Example: Enterprise platforms, deep workflow changes

---

## Contributing

This knowledge base is a living document. As you apply ILG in the field:
- Document case studies in `02-market-data`
- Refine field assets based on what works
- Update research with new evidence

---

## License & Usage

This framework is designed to be a **source of truth** for organizations building their own ILG process. Adapt and customize for your specific context.

---

**Version:** 10.0
**Last Updated:** 2026-03-10
