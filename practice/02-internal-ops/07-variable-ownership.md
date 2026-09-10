# Variable Ownership

**Purpose:** To name the department that owns each variable in the model, so that no variable drifts for want of an owner and none fragments across two.

**Operationalizes:** The Constitution's organizational corollary, which lived in the Constitution as Part IV through v14.0 and moved here in v15.0. A variable-to-department mapping is operational content, and the Constitution is axioms-first.

**Canonical model:** [00-ilg-constitution.md](../../theory/01-foundation/00-ilg-constitution.md) Part III for the Surplus equation, [05-seller-surplus-model.md](../../theory/01-foundation/05-seller-surplus-model.md) for the seller-side terms.

---

The variables in the Surplus equation each have a department owner. This corollary states the *principle* (the axioms map to organizational responsibility) and points to where the operational procedures live.

## The principle

Each variable in the model is owned by a specific function. If a variable has no owner, it drifts; if it has multiple owners without coordination, it fragments.

| Variable | Axiom | Primary owner | Supporting |
|---|---|---|---|
| $V_{solution}$ | I | Product | Product Marketing |
| $V_{next\_best}$ | I | Sales | Product Marketing |
| $V_{effective}(t)$ — urgency monitoring | I | Sales | RevOps |
| $k$ (asset specificity) | I | Sales Leadership | Product |
| $F_{search}$ | II | Marketing | Sales (via referrals) |
| $F_{consensus}$ | II | Sales | Solutions Engineering |
| $F_{implementation}$ | II | CS / Implementation | Sales (in the Blueprint) |
| $\Delta_A$ — Seller side ($I_{seller}$) | II | Sales + SE | Product Marketing |
| $\Delta_A$ — Buyer side ($I_{buyer}$) | II | Marketing (category) + Sales (deal) | CS (post-sale) |
| $\delta_{discount}$ — Rep level | III | Finance (vested comp) | Sales Leadership |
| $\delta_{discount}$ — Org level | III | Executive Leadership | All |
| Reputation refresh | III | Marketing + CS | All |

## The handoff rule

The Blueprint travels with the customer through the funnel. The asymmetry assessment that the seller produced must transfer intact to CS at handoff, or $\Delta_A$ resets to near-maximum on the receiving side. The Blueprint is the institutional memory that prevents the Fumbled Handoff failure mode.

## Where procedures live

This document states the principle. The detailed procedures live alongside it in this directory: CRM field configuration and manager rituals in [00-setup-implementation-guide.md](./00-setup-implementation-guide.md), comp plan mechanics in [03-incentives-vested-commission.md](./03-incentives-vested-commission.md), and calibration in [01-governance-deal-calibration.md](./01-governance-deal-calibration.md).

---
