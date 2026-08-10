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
| Look up a symbol or term | [theory/01-foundation/04-glossary-and-notation.md](theory/01-foundation/04-glossary-and-notation.md) |
| See the academic evidence behind a claim | [theory/02-research/](theory/02-research/), starting with the [reading guide](theory/02-research/00-reading-guide.md) |
| Run an actual deal | [practice/01-field-assets/](practice/01-field-assets/) |
| Set up your org for ILG | [practice/02-internal-ops/](practice/02-internal-ops/) |
| Train reps | [practice/03-learning-plan/](practice/03-learning-plan/) |
| See ILG applied to a real deal | [publishing/01-cases/](publishing/01-cases/) |
| Write about ILG publicly | [publishing/02-tools/](publishing/02-tools/) |

---

## Core concepts at a glance

### The Fundamental Equation

$$S = \left(V_{solution} \cdot e^{-\delta t} - V_{next\_best}\right) - (F_{search} + F_{consensus} + F_{implementation}) \cdot (1 + \Delta_A) = OC_{\text{switching}} - y$$

- **S** = Deal Surplus (must be > 0 for a deal to close)
- **Δ_A** = Bilateral Asymmetry Gap = Seller Ignorance + Buyer Uncertainty
- **y** = Total Perceived Transaction Cost = $ax^2 + c$ (where $a = 2.25$ is risk aversion, $x \approx \Delta_A$ is uncertainty, and $c$ is direct cost)
- **δ** = Decay Rate of urgency after the triggering event
- Applies when **k > k_threshold** (the deal is a Bridge, not a Toaster) AND **F_deployed ~ k** (the friction deployed matches the specificity)

### The Three Axioms

Names, scope, and taglines below are canonical. If this table and the [Constitution](theory/01-foundation/00-ilg-constitution.md) ever disagree, the Constitution wins.

| Axiom | Governs | Tagline | What it says |
|---|---|---|---|
| **I. Law of Transaction Cost Composition** | Whether a deal can happen | *"Costs determine the deal"* | Search, consensus, and implementation costs arise independently. Their combined level determines which motion is viable, and Bridge/Toaster classification follows from measuring them. |
| **II. Law of Uncertainty Inflation** | What the deal costs when it happens | *"Fear > Value"* | Base friction is amplified by the bilateral asymmetry gap between buyer and seller. Reducing risk moves more surplus than increasing ROI. |
| **III. Law of Governance** | Whether the deal persists | *"Structure determines behavior"* | Every party whose decisions affect outcomes needs skin in the game tied to those outcomes, including the channels and adjudicators between them. |

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

**Version:** 13.0 (tracks the [Constitution](theory/01-foundation/00-ilg-constitution.md) version; bump both together)
**Last updated:** 2026-08-10
