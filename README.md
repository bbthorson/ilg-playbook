# Implementation-Led Growth (ILG) Knowledge Base

**A sales methodology for high-friction B2B software, grounded in Transaction Cost Economics, Behavioral Economics, and Game Theory.**

---

## What is ILG?

**Implementation-Led Growth (ILG)** is the GTM motion for deals where Product-Led Growth (PLG) and Sales-Led Growth (SLG) fail: deep workflow integration, multi-stakeholder consensus, and long implementation cycles.

The core insight:

> **In high-specificity deals, reducing friction creates more surplus than increasing value. But friction is amplified by information gaps, and value erodes with time — so the goal is to close the asymmetry gap faster than urgency decays.**

ILG addresses this through **discovery artifacts** (Blueprints) that reduce seller ignorance and **costly signals** (Red Teams, paid pilots) that reduce buyer uncertainty — driving the Bilateral Asymmetry Gap (Δ_A) → 0 before the Decay Clock runs out.

---

## How this repo is organized

The repo serves **three functions**, each in its own top-level directory.

| Function | Where | What it is |
|---|---|---|
| **[theory/](theory/)** | `theory/01-foundation/` + `theory/02-research/` | Develop and pressure-test the ILG framework. Academic papers, axioms, definitions. |
| **[practice/](practice/)** | `practice/01-field-assets/` + `practice/02-internal-ops/` + `practice/03-learning-plan/` | Help sellers and managers actually run ILG. Templates, governance, training. |
| **[publishing/](publishing/)** | `publishing/01-cases/` + `publishing/02-tools/` | Turn the framework into public writing. Case analyses, voice guides, content generators. |

Each group has its own README explaining what's inside and the reading order.

---

## Quick start by intent

| If you want to... | Go here |
|---|---|
| Understand the theory cold | [theory/01-foundation/](theory/01-foundation/) |
| See the academic evidence behind a claim | [theory/02-research/](theory/02-research/), starting with [the synthesis](theory/02-research/00-synthesis-the-new-sales-paradigm.md) |
| Run an actual deal | [practice/01-field-assets/](practice/01-field-assets/) |
| Set up your org for ILG | [practice/02-internal-ops/](practice/02-internal-ops/) |
| Train reps | [practice/03-learning-plan/](practice/03-learning-plan/) |
| See ILG applied to a real deal | [publishing/01-cases/](publishing/01-cases/) |
| Write about ILG publicly | [publishing/02-tools/](publishing/02-tools/) |

---

## Core concepts at a glance

### The Fundamental Equation

$$S = \left(V_{solution} \times e^{-\delta t} - V_{next\_best}\right) - F_{base} \times (1 + \Delta_A)$$

- **S** = Deal Surplus (must be > 0 for a deal to close)
- **Δ_A** = Bilateral Asymmetry Gap = Seller Ignorance + Buyer Uncertainty
- **δ** = Decay Rate of urgency after the triggering event
- Applies when **k > k_threshold** (high asset specificity) AND **n_viable ≤ n_max** (thin market)

### The Three Axioms

1. **Law of Economic Boundaries** — Asset specificity determines whether ILG applies (Bridge vs. Toaster).
2. **Law of Asymmetry Convergence** — Drive Δ_A → 0 by closing the wider gap first.
3. **Law of Bilateral Governance** — Long-term alignment requires mutual skin in the game.

### Bridge vs. Toaster

| | **Toaster** | **Bridge** |
|---|---|---|
| Score | 4–9 on the [Diagnostic Rubric](practice/01-field-assets/process-calculator.md) | 10–20 |
| Strategy | PLG / SLG — optimize for velocity | ILG — optimize for safety and certainty |
| Example | Standalone SaaS tools | Enterprise platforms, deep workflow change |

---

## Contributing

This is a living document. As you work:
- Add new applied analyses to [publishing/01-cases/](publishing/01-cases/) using the trenches protocol.
- Refine field assets in [practice/01-field-assets/](practice/01-field-assets/) based on what works.
- Update research with new evidence; the [provenance audit](theory/02-research/audits/citation-provenance-audit.md) tracks source quality.

---

**Version:** 12.0
**Last updated:** 2026-05-28
