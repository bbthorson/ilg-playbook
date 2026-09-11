---
title: "Foundation"
layer: theory
status: active
---

# Foundation

**Start here.** These documents form the canonical theoretical basis for everything else in the repo. Read in numerical order.

Parent: [theory/](../) · Sibling: [02-research/](../02-research/)

The three states (Market, Deal at T0, Relationship at T1+) are the framework's primary index. They are defined in [00-ilg-constitution.md](./00-ilg-constitution.md) Part I and used as the front door in the [root README](../../README.md).

## Reading order

1. **[01-sales-motion-comparison.md](./01-sales-motion-comparison.md)** — *(start here if you're new)* What each named motion contains, once a motion is a region of the friction vector's space rather than an item on a list. Gives you the lay of the land before you dive into theory.
2. **[00-ilg-constitution.md](./00-ilg-constitution.md)** — The full economic and behavioral framework, structured as a deductive system. Four parts:
   - **Part I:** The Three Axioms — Law of Transaction Cost Composition, Law of Uncertainty Inflation, Law of Governance
   - **Part II:** Derived Concepts — primary derivations from each axiom (Boundary Condition, Friction Allocation Principles, Three Sales Levers, Recursive Cooperation, Reputation Depreciation), bridge concepts (Decay Clock, Effective Cost, Staged Commitment, Surplus)
   - **Part III:** Synthesis — the full integrated Surplus equation and the failure-modes summary. Part I carries one figure per axiom, generated from [`models/`](../../models/README.md).
3. **[02-cfir-field-mapping.md](./02-cfir-field-mapping.md)** — How the academic [CFIR](../02-research/cfir.md) framework maps to the ILG artifacts. Read this if you're designing or modifying field assets.
4. **[03-mathematical-models.md](./03-mathematical-models.md)** — *(reference)* Functional forms, parameter specifications, and the derivation connecting the structural and reduced forms of transaction cost.
5. **[04-glossary-and-notation.md](./04-glossary-and-notation.md)** — *(reference, read as needed)* Every symbol and term in one place, with a pointer to where each is canonically defined. The notation index is itself canonical, since symbols had no home before it. Includes a disambiguation section for the five symbol pairs that look alike and mean different things.
6. **[05-seller-surplus-model.md](./05-seller-surplus-model.md)** — The seller's side of the transaction. The Constitution models what the buyer gains and pays; this specifies what the seller spends before signature, what portion of it is exposed, and when the spend is worth making. Read it before designing a forward-deployed or implementation-heavy engagement.

7. **[06-friction-vector.md](./06-friction-vector.md)** — Derives motion selection from the direction and length of the three-component cost vector. Adopted in Constitution v17.0, which took its per-component amplification into Axiom II and its vector notation into Axiom I. Section 9 records what adoption did not settle and section 10 records what it changed.

## What goes here vs. elsewhere

| Type of content | Where it lives |
|---|---|
| Theoretical framework, axioms, equations | **`theory/01-foundation/`** (this directory) |
| Academic papers and evidence | [`../02-research/`](../02-research/) |
| Templates reps actually use | [`../../practice/01-field-assets/`](../../practice/01-field-assets/) |
| Comp plans, calibration, governance | [`../../practice/02-internal-ops/`](../../practice/02-internal-ops/) |

If a concept is invoked in two or more directories, its canonical definition lives **here**.
