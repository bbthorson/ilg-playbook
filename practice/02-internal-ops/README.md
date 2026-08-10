# Internal Ops: Governance & Incentives

**The systems that keep ILG honest at the org level.** These are tools for leadership, RevOps, and finance — not the rep in the field.

Parent: [practice/](../) · Siblings: [01-field-assets/](../01-field-assets/), [03-learning-plan/](../03-learning-plan/)

If [`../01-field-assets/`](../01-field-assets/) is *how reps run deals*, this directory is *how leadership runs reps*.

## Files

### Setup (one-time)

- **[00-setup-implementation-guide.md](./00-setup-implementation-guide.md)** — Calibration workshop to customize the ILG framework to your product, market, and tech stack. Run this before deploying any of the other artifacts here.

### Governance (deal-level, recurring)

How managers and VPs forecast Bridges based on friction completed, not hope.

- **[01-governance-deal-calibration.md](./01-governance-deal-calibration.md)** — Manager tool to qualify a Bridge deal: classification check, friction audit, "no decision" risk, forecast verdict.
- **[02-governance-review-checklist.md](./02-governance-review-checklist.md)** — Forensic checklist for the three friction phases (Blueprint → Red Team → MIP). Includes the [asymmetry scorecard](./04-incentives-asymmetry-scorecard.md) as an embedded check.
- **[06-governance-implementation-veto.md](./06-governance-implementation-veto.md)** — Grants Solutions Engineering and Implementation a binding pre-signature halt on Bridge deals carrying unmitigated operational risk. Defines trigger conditions, the escalation path, and the exposure carried by the veto holder in both directions.

### Incentives (comp design)

How to align rep behavior with long-term customer outcomes, not just signature.

- **[03-incentives-vested-commission.md](./03-incentives-vested-commission.md)** — Comp plan addendum: front-load, clawback, NRR bonus, safe harbor. Operationalizes Axiom III (Governance) at the rep/management level — the cooperation condition's $\delta_{discount}$ requires comp tied to long-term outcomes, not signature.
- **[04-incentives-asymmetry-scorecard.md](./04-incentives-asymmetry-scorecard.md)** — Weekly diagnostic measuring Bilateral Asymmetry Gap (Δ_A) across seller ignorance and buyer uncertainty.

### Diagnostics (retrospective, cohort-level)

How leadership checks whether the motion is actually being run, after deals close.

- **[05-diagnostics-friction-efficiency-index.md](./05-diagnostics-friction-efficiency-index.md)** — Quarterly retrospective across a cohort of closed Bridge deals. Measures whether implementation effort landed before or after signature (FAR), how fast the buyer mobilized (BCV), what share of discovered risk was closed pre-signature (RMS, the Risk Mitigation Score), and scope stability (SVI), combined into a single index. All parameters are uncalibrated; read the provenance table before quoting any figure.

### Tooling

- **[linting/](./linting/)** — Automated enforcement of the repo's content conventions. A dependency-free link and LaTeX validator, plus a Vale style covering banned vocabulary, emojis, punctuation density, and retired terms. Run both before opening a PR. Read its [README](./linting/README.md) first.

## Naming convention

Files use `NN-category-slug.md` where `NN` controls reading order and `category` is either `setup`, `governance`, `incentives`, or `diagnostics`.

## What goes here vs. elsewhere

| Type of content | Where it lives |
|---|---|
| Templates reps fill out on a deal | [`../01-field-assets/`](../01-field-assets/) |
| Manager / VP / RevOps tools | **`practice/02-internal-ops/`** (this directory) |
| Training and curriculum | [`../03-learning-plan/`](../03-learning-plan/) |
