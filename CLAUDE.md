# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

A knowledge base for **Implementation-Led Growth (ILG)** — a B2B sales methodology for high-friction, high-specificity software deals. No code; all content is Markdown. The repo is organized into three functional groups, each with its own README:

| Directory | Function |
|---|---|
| `theory/` | Develop and pressure-test the ILG framework. Axioms, equations, academic backing. |
| `practice/` | Operationalize theory for sellers and managers. Templates, governance, training. |
| `publishing/` | Turn the framework into public writing. Voice guide, content generators, case analyses. |

## Conceptual architecture

**The canonical source of truth is `theory/01-foundation/00-ilg-constitution.md`** — three axioms from which all other concepts derive. Everything in `practice/` and `publishing/` traces back to it.

The dependency chain runs one way: `theory/` → `practice/` → `publishing/`. Changes to theory should propagate downstream. Changes to practice or publishing never modify theory.

Key cross-file dependencies to know:
- The **Process Calculator** (`practice/01-field-assets/process-calculator.md`) operationalizes the Boundary Condition from Axiom I. It is referenced by nearly every field asset.
- The **CFIR field mapping** (`theory/01-foundation/02-cfir-field-mapping.md`) explains which research construct each artifact section operationalizes — read it before modifying any `practice/01-field-assets/` document.
- The **Friction Allocation Diagnostic** (`practice/01-field-assets/friction-allocation-diagnostic.md`) operationalizes the four Friction Allocation Principles from Axiom II.
- The **three ILG artifacts** (Blueprint → Red Team → MIP) in `practice/01-field-assets/ilg-motion/` run sequentially; each artifact gates the next.

The **research files** in `theory/02-research/` back specific axioms:
- Axiom I → `transaction-cost-economics.md`
- Axiom II → `costly-signals.md`, `prospect-theory.md`, `fear-of-failure.md`, `cfir.md`
- Axiom III → `game-theory-and-nrr.md`, `re-aim-framework.md`

Start with `theory/02-research/00-reading-guide.md` before modifying any research file.

## Content conventions

When writing or editing any document in this repo, apply the voice rules from `publishing/02-tools/voice-guide.md`:

- **Translate every technical term** immediately after first use — never drop "Asset Specificity" or "Single Crossing Property" without a plain-English follow-up.
<!-- vale ILG.AntiHype = NO -->
- **Anti-hype vocabulary**: banned words include *synergy*, *revolutionize*, *disruptive*, *cutting-edge*, *seamlessly*, *unlock potential*. See voice guide for replacements.
<!-- vale ILG.AntiHype = YES -->
- **Em dashes and semicolons**: 2–3 per document maximum. Restructure into periods when uncertain.
- **Anti-antithesis filter**: avoid "It's not X, it's Y" constructions.
- **Active voice**: name actors. "HTD will map the workflow" over "the workflow will be mapped."
- **No emojis.**
- The Constitution is **axioms-first** (v11+): if a claim cannot be traced to one of the three axioms, it does not belong in `theory/01-foundation/00-ilg-constitution.md`. Operational content belongs in `practice/`.

### Checking your work

Most of the rules above are machine-checked. Run both before finishing an edit, and see `practice/02-internal-ops/linting/README.md` for what each covers:

```bash
python3 practice/02-internal-ops/linting/check_playbook.py && vale .
```

`check_playbook.py` needs no dependencies and validates links plus LaTeX delimiters. Vale (`brew install vale`) enforces the banned-word list, the emoji ban, the punctuation limit, and retired vocabulary.

### Renaming anything canonical

The dependency chain runs `theory/` → `practice/` → `publishing/`, and nothing enforces it automatically. When you rename an axiom, retire an equation variable, or renumber a directory:

1. Grep the whole repo for the old term before assuming the rename is local. Stale names hide inside links whose hrefs are still correct, so the link checker will not catch them.
2. Add the old term to `swap:` in `practice/02-internal-ops/linting/styles/ILG/RetiredTerms.yml` in the same commit. That is what stops the rename from drifting back.
3. Bump the version in `theory/01-foundation/00-ilg-constitution.md` and the matching version footer in the root `README.md` together.
4. Check the *descriptions*, not just the names. A paragraph can use every current term and still describe a superseded version of an axiom.

## How documents relate to the Fundamental Equation

All framework claims trace to:

$$S = \left(V_{solution} \cdot e^{-\delta t} - V_{next\_best}\right) - (F_{search} + F_{consensus} + F_{implementation}) \cdot (1 + \Delta_A) = OC_{\text{switching}} - y$$

- **S** = Deal Surplus (must be > 0 to close)
- **Δ_A** = Bilateral Asymmetry Gap = Seller Ignorance ($I_{seller}$) + Buyer Uncertainty ($I_{buyer}$)
- **y** = Total Perceived Transaction Cost = $ax^2 + c$ (where $a = 2.25$ is risk aversion, $x \approx \Delta_A$ is uncertainty, and $c$ is direct cost)
- **Bridge** = deal scoring 10–20 on Process Calculator → deploy ILG motion
- **Toaster** = deal scoring 4–9 → deploy PLG/SLG motion

When diagnosing a stall or editing a prescription, identify which term in the equation it addresses.

## Publishing workflow

New content in `publishing/` follows the multi-phase workflow in the relevant generator file:

```
ilg-concept-map.md → voice-guide.md → context-request-protocol.md → {long-form | short-form}-generator.md → style-references/
```

Case analyses go in `publishing/01-cases/` following `publishing/02-tools/trenches-analysis-protocol.md`. If a case becomes a polished published piece, the final version moves to `publishing/02-tools/style-references/`.

The AI persona config for deal-analysis writing is in `publishing/02-tools/ai-persona.md`.
