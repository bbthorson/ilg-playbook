# Reading Guide

**How to navigate the research, in what order, for which audience.** This guide tells you where to start, what to read in what sequence, and what's safe to skip — given who you are and what you need.

The theoretical synthesis of these papers lives in the [Constitution](../01-foundation/00-ilg-constitution.md). This guide tells you which papers back the Constitution's claims and how to read them efficiently.

---

## The narrative in one paragraph

The traditional B2B sales playbook — built on persuasion, relationship-building, and "growth at all costs" — is fundamentally broken. It fails to account for the economic and psychological realities of the modern enterprise buyer. Implementation-Led Growth synthesizes frameworks from Implementation Science (CFIR, RE-AIM), Behavioral Economics (Prospect Theory, Costly Signaling), and Institutional Economics (Transaction Cost Economics, Game Theory) into a single coherent framework. The shift is from "Persuader" to "Diagnostic Change Agent," and from "Closing" to "De-risking."

For the formal axioms and derivations, read the [Constitution](../01-foundation/00-ilg-constitution.md). For the research that backs each axiom, use the reading order and audience guide below.

---

## How the research builds

The papers in this directory depend on each other in a specific order. Lower-level papers establish foundations the higher-level papers build on.

```
                         ┌─────────────────────────┐
                         │       NRR (Output)       │
                         │  The composite scorecard │
                         └────────────┬────────────┘
                                      │
                    ┌─────────────────┴─────────────────┐
                    │                                    │
         ┌──────────┴──────────┐             ┌──────────┴──────────┐
         │    CFIR (Pre-Sale)   │             │  RE-AIM (Post-Sale)  │
         │  Diagnose barriers   │             │  Measure outcomes    │
         │  Map Inner Setting   │             │  R-E-A-I-M KPIs      │
         └──────────┬──────────┘             └──────────┬──────────┘
                    │                                    │
                    └─────────────────┬─────────────────┘
                                      │
              ┌───────────────────────┼───────────────────────┐
              │                       │                       │
    ┌─────────┴─────────┐  ┌─────────┴─────────┐  ┌─────────┴─────────┐
    │  Prospect Theory   │  │   Game Theory      │  │  Costly Signals    │
    │  λ ≈ 2.25          │  │  Shadow of Future  │  │  Friction = Signal │
    │  Fear > Value      │  │  Nash Equilibrium  │  │  Cheap Talk Problem│
    └─────────┬─────────┘  └─────────┬─────────┘  └─────────┬─────────┘
              │                       │                       │
              └───────────────────────┼───────────────────────┘
                                      │
                        ┌─────────────┴─────────────┐
                        │  Transaction Cost Economics │
                        │  (The Foundation)           │
                        │  Asset Specificity →        │
                        │  Governance → Friction      │
                        └─────────────────────────────┘
```

**Order of dependency:**

1. **[Transaction Cost Economics](./transaction-cost-economics.md)** — Start here. Establishes why friction exists and why it's necessary.
2. **[Costly Signals](./costly-signals.md)** — Builds on TCE: how friction resolves information asymmetry.
3. **[Prospect Theory](./prospect-theory.md)** — Explains *why* buyers fear change at the neurobiological level (λ ≈ 2.25).
4. **[Game Theory and NRR](./game-theory-and-nrr.md)** — Shows how incentives must be structured to sustain cooperation across the repeated game.
5. **[Fear of Failure](./fear-of-failure.md)** — Empirical evidence: Standish CHAOS, Gartner regret data, the JOLT Effect.
6. **[CFIR](./cfir.md)** — Pre-sale diagnostic methodology.
7. **[RE-AIM](./re-aim-framework.md)** — Post-sale measurement methodology.

Plus the channel-level layer:

8. **[Channel Collapse](./channel-collapse.md)** — Jevons' Paradox applied to outbound. Governance solutions for the channel-level externality problem.

---

## Reading guide by audience

| Audience | Start with | Then read | Skip |
|---|---|---|---|
| **Executive / CRO** | This guide → [Constitution](../01-foundation/00-ilg-constitution.md) | [Sales Motion Comparison](../01-foundation/01-sales-motion-comparison.md) | Deep theory papers unless interested |
| **Sales Practitioner** | This guide → [CFIR](./cfir.md) (Saboteur Matrix) | [Costly Signals](./costly-signals.md), [Prospect Theory](./prospect-theory.md) | Mathematical proofs |
| **Sales Enablement / Ops** | [RE-AIM](./re-aim-framework.md) (KPI tables) → [Game Theory and NRR](./game-theory-and-nrr.md) (compensation) | Full [CFIR](./cfir.md), [Sales Motion Comparison](../01-foundation/01-sales-motion-comparison.md) | Nothing — read everything |
| **Academic / Researcher** | [TCE](./transaction-cost-economics.md) → [Costly Signals](./costly-signals.md) → [Prospect Theory](./prospect-theory.md) | [Game Theory](./game-theory-and-nrr.md), [CFIR](./cfir.md), [RE-AIM](./re-aim-framework.md) | [Fear of Failure](./fear-of-failure.md) unless reviewing data |
| **Marketing / Content** | This guide → [Sales Motion Comparison](../01-foundation/01-sales-motion-comparison.md) | [Costly Signals](./costly-signals.md), [Channel Collapse](./channel-collapse.md) | Detailed implementation science |

---

## What you won't find here

This is a citation index, not a theoretical synthesis. The synthesis lives elsewhere:

- **Three axioms and their derivations:** [Constitution](../01-foundation/00-ilg-constitution.md), Parts I and II.
- **Surplus equation, potential-well diagram, failure modes table:** Constitution Part III.
- **Operational tools** (rubric, artifacts): [`practice/`](../../practice/).

This guide tells you which papers back which axiom. The Constitution tells you what the axioms *are*.
