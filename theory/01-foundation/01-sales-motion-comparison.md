# Sales Motion Comparison: ILG vs. PLG vs. SLG

**A decision framework for choosing the right sales motion.**

This document is the practical companion to the [Constitution](./00-ilg-constitution.md). The Constitution explains *why* motion choice matters (Axiom I: friction must match asset specificity). This doc explains *how* to choose.

---

## What Kind of Thing ILG Is

Go-to-market methodologies get compared as though they all answer the same question. They do not. Three distinct tiers exist, and confusing them produces arguments that cannot resolve.

| Tier | What it decides | Examples |
|---|---|---|
| **Macro GTM motion** | The core driver of acquisition, retention, and expansion. Which artifacts get built, who staffs the deal, how the process is shaped. | PLG, SLG, **ILG** |
| **Qualification framework** | Deal inspection, pipeline hygiene, forecasting. What must be true before a deal is called committed. | MEDDPICC, BANT |
| **Conversational methodology** | Rep dialogue, discovery technique, how a perspective gets reframed in the room. | Challenger Sale, SPIN Selling |

**ILG is a macro GTM motion.** It is therefore not an alternative to MEDDPICC or Challenger, and adopting ILG does not mean abandoning either.

The tiers compose. A team running ILG still needs a qualification standard, and MEDDPICC works as well inside ILG as inside SLG. ILG changes what the qualification evidence *is*: the Economic Buyer is confirmed in the Blueprint, the Decision Criteria are the Red Team's surfaced failure modes, and the Champion is tested by whether they commit resources to the MIP. A rep still needs conversational technique, and Challenger's commercial teaching is well suited to the Blueprint interview.

The distinction matters most when someone says their team "already does ILG because they run MEDDPICC on complex deals." Qualification tells you whether a deal is real. It does not reduce the buyer's implementation risk, which is the only thing that closes a Bridge.

---

## Buyer State and Dominant Cost

Each motion answers a different buyer, in a different state of problem awareness, carrying a different dominant cost:

| Motion | Buyer mindset | Dominant transaction cost | Core objective |
|---|---|---|---|
| **PLG** | *"I know my problem. Give me the tool to test it."* | Vendor evaluation | **Frictionless activation.** Collapse evaluation cost by letting the buyer verify utility without a seller. |
| **SLG** | *"I'm comfortable in the status quo. Convince me I have a problem."* | Category search, plus budget consensus for a category with no line item | **Problem discovery and urgency.** Educate the buyer, quantify the cost of inaction, create the budget. |
| **ILG** | *"I know my problem. Prove you won't break my business installing a fix."* | Consensus and implementation, amplified by $\Delta_A$ | **Risk elimination.** Supply pre-sale technical proof and structured risk-sharing governance. |

### A note on splitting $F_{search}$

The Constitution defines $F_{search}$ as "locating the category and viable vendors." Those are two activities, and they peak in different markets. Keeping them fused produces an apparent contradiction, because PLG and SLG both look like they own search.

- **Category search** dominates nascent markets. The buyer cannot name what they need. SLG resolves this through education, and the cost is cognitive.
- **Vendor evaluation** dominates mature, low-specificity markets. The category is legible and the buyer can name five vendors. PLG resolves this by letting them try one, and the cost is time.

ILG deals carry little of either. The buyer knows the category and the field. What they cannot resolve is whether *this* vendor can install *this* system in *their* environment without breaking it, which is $F_{implementation}$ inflated by $\Delta_A$, and no amount of category education or free trial touches it.

---

## Quick Reference

| Dimension | **ILG** | **PLG** | **SLG** |
|---|---|---|---|
| **Market Stage** | Saturated | Mature / Efficient | Nascent |
| **Deal Archetype** | The Bridge | The Toaster | The Pitch |
| **Friction Type** | Structural (implementation) | Minimal | Educational (market-creation) |
| **Cost Score** | 10–20 (Mature) | 4–9 (Mature) | n/a (market not legible) |
| **Optimization** | Safety & certainty | Velocity & volume | Education & vision-casting |
| **Primary Metric** | NRR, adoption | User growth, activation | Win rate, category awareness |
| **Sales Cycle** | 3–9 months | Self-service (days) | 6–12 months (often) |
| **ACV Range** | $100k–$1M+ | $0–$50k | $25k–$500k |
| **Decision Makers** | 3–10+ stakeholders | 1–2 | 1–3 (often visionary) |
| **Integration** | Deep (ERP, core systems) | Lightweight (API, SSO) | Variable |
| **Rep Role** | Implementation scientist | Minimal (CS-led expansion) | Educator / market-maker |
| **Comp Structure** | [Vested commission](../../practice/02-internal-ops/03-incentives-vested-commission.md) | CS-led expansion bonuses | Traditional ACV commission |

---

## The Three Motions in Context

Each motion fits a specific *market structure* and *deal profile*. The Constitution covers the theoretical mapping; here we focus on operational fit.

### ILG (Implementation-Led Growth)

**Market:** Saturated. The category is well-known, multiple credible vendors exist, buyers are sophisticated and have implementation scars.

**Deal profile:** High asset specificity. Deep integration, cross-functional impact, multi-stakeholder consensus required. Hard to rip out once installed.

**Examples:** Revenue operations platforms, ERP modules, core infrastructure replacements, enterprise data platforms, EHR systems.

**Key activities:** [Contextual Blueprint](../../practice/01-field-assets/ilg-motion/01-discovery-contextual-blueprint.md) (discovery + qualification), [Red Team Workshop](../../practice/01-field-assets/ilg-motion/02-validation-red-team-protocol.md) (validation), [Mutual Implementation Plan](../../practice/01-field-assets/ilg-motion/03-closing-mutual-implementation-plan.md) (governance + close).

**Success criteria.** Bilateral asymmetry gap closed before signature. Resources committed by both sides. Saboteur identified and contained. Implementation succeeds; NRR > 120%.

---

### PLG (Product-Led Growth)

**Market:** Mature / efficient. Category is well-defined, standard playbooks exist, comparison is straightforward, buyers can self-evaluate.

**Deal profile:** Low asset specificity. Standalone tool, lightweight integration, single team or small department, low switching cost.

**Examples:** Collaboration tools (Slack, Notion, Linear), analytics dashboards, simple marketing automation, developer tools.

**Key activities:** Self-service signup, automated onboarding, in-product activation, usage-based expansion. Sales rep involvement is minimal; CS drives expansion through product value.

**Success criteria.** Fast time-to-value. High activation rate. Low CAC. Net-new users invite their colleagues — viral or near-viral growth dynamic.

---

### SLG (Sales-Led Growth)

**Market:** Nascent. Category name may not exist yet, few proven solutions, buyer may not yet know the problem can be solved.

**Deal profile:** Variable specificity, but the dominant friction is *educational* — the seller is teaching the buyer that the problem exists and what a solution category looks like.

**Examples:** Selling AI agents to clinical teams in 2023. Selling SaaS in 1998. Selling fractional CFOs to mid-market in 2010. Often the rep is creating the market through the act of selling.

**Key activities:** Heavy buyer education, vision-casting, reference architectures, "what does good look like" sessions. Often Challenger-style commercial teaching. Buyer-seller co-design of the solution shape.

**Success criteria.** Visionary early adopters commit. The seller builds case studies that establish the category for the next wave of buyers — which is when the market transitions toward PLG or ILG.

---

## SLG vs. ILG: The Critical Distinction

Both SLG and ILG involve high-friction deals, but the *type* of friction is different, and confusing them leads to misallocated effort.

**SLG friction is educational.** The seller is teaching the buyer that they have a problem and that a solution category exists. The friction is cognitive. Once the buyer understands the category, switching to a competitor is relatively easy — the buyer has not yet built workflows around your specific implementation.

**ILG friction is structural.** The buyer already knows they have the problem and that a solution category exists. The friction comes from the *implementation itself*: integration depth, data migration, workflow rewiring, multi-stakeholder consensus. The friction is organizational, not cognitive.

The practical consequences:

- **SLG reps are educators** — Challenger-style commercial teaching, frame-of-reference building.
- **ILG reps are implementation scientists** — CFIR-style organizational diagnosis, workflow mapping.
- **Applying ILG tactics to an SLG deal over-engineers it.** You are producing rigor for a buyer who has not yet decided they have the problem.
- **Applying SLG tactics to an ILG deal under-prepares the buyer.** You are educating someone who needs implementation governance.

This distinction is why market stage matters as much as asset specificity in motion choice — and why the [Decision Framework](#decision-framework) below leads with market stage before scoring asset specificity.

---

## Decision Framework

The motion is determined by two factors: the *market stage* (which determines whether SLG, PLG, or ILG is even the right shape) and the *asset specificity within that market* (which refines within the ILG/PLG range).

### Step 0: Workflow Maturity Gate

Does a documented SOP exist for the problem? If NO → **Chaos Trap** → Redirect to Consulting/Paid Workshop. You cannot digitize undefined workflows.

### Step 1: Market Stage Diagnostic (Workflow Legibility)

Score the *market*, not the deal:

| Signal | Y/N |
|---|---|
| Is there a recognized category name? | |
| Can the buyer name 3+ vendors that solve this problem? | |
| Are there published implementation playbooks, G2 reviews, or analyst coverage? | |

- **0–1 Yes → Nascent.** Search dominates. Motion: **SLG** (educational, market-making). Skip Step 2.
- **2 Yes → Transitional.** Judgment call; usually SLG transitioning toward ILG as the category matures. Score Step 2 and weight ILG higher.
- **3 Yes → Mature.** Category is legible. Continue to Step 2 to determine PLG vs. ILG within the mature market.

### Step 2: Transaction Cost Diagnostic (Mature markets only)

Score 1–5 each, then sum:

| Factor | Targets | Score 1 | Score 5 |
|---|---|---|---|
| **Integration depth** | $F_{implementation}$ | Standalone tool, no integration | Core ERP/EHR replacement, custom code |
| **Workflow change scope** | $F_{implementation}$ | Single team, no process change | Cross-functional, total workflow overhaul |
| **Consensus complexity** | $F_{consensus}$ | Single decision maker | Board / Procurement / Security audit |
| **Retention horizon** | $F_{implementation}$ (sustained) | One-time project | Multi-year platform, deep dependency |

Sum range: 4–20.

### Step 3: Motion Selection

| Market Stage | Cost Score | Motion |
|---|---|---|
| Nascent | (n/a) | **SLG** |
| Transitional | 4–14 | **SLG** with ILG elements creeping in |
| Transitional | 15–20 | **ILG** (deal stakes high enough to force ILG even before category maturity) |
| Mature | 4–9 | **PLG** |
| Mature | 10–20 | **ILG** |
| Any | Override: pilot/POC requested | **ILG** (auto-score 20) |

The operational tool that runs this diagnostic is the [Process Calculator](../../practice/01-field-assets/process-calculator.md).

---

## Hybrid Approaches and Transitions

Markets evolve, and individual deals can shift across motion boundaries during the sales cycle. Three common transitions:

**PLG → ILG (Land and Expand).** Start with PLG motion at the team level. When enterprise expansion triggers — cross-functional rollout, security review, organization-wide governance — trigger ILG motion. *Example:* Slack runs PLG for teams and ILG for enterprise rollout.

**SLG → ILG (Maturing Category).** A nascent market becomes mature as standards emerge, analyst coverage develops, and reference customers accumulate. SLG-era sellers must transition to ILG to defend against new entrants and to handle the now-sophisticated buyer base. *Failure mode:* sticking with SLG tactics in a mature market, missing implementation depth.

**SLG → ILG (Complexity Discovery).** A single deal that looked like SLG (sell the vision, close on the merits) turns out to involve deeper integration and political complexity than initially scoped. The rep pivots to ILG mid-cycle: deploy Blueprint, Red Team, MIP. *Failure mode:* rigidly maintaining the original motion as evidence of complexity accumulates.

The Constitution's Boundary Condition (Axiom I) explains why these transitions are necessary: friction must match specificity. When the underlying specificity changes — through market evolution or in-deal discovery — the friction structure must adjust.

### The lifecycle runs one way, and then resets

Left alone, a category ages in a single direction. Standards solidify, integration patterns homogenize, implementation playbooks get published, and asset specificity falls. The motion that fits follows it down:

```
Emerging category      → high specificity, no playbooks    → ILG
Consolidating category → standard integration patterns     → SLG
Commoditized category  → turnkey interoperability          → PLG
```

The practical warning is that a motion which fit three years ago may over-serve the same category today. A team still running full ILG on a category that has commoditized is burning margin on Blueprints the buyer no longer needs.

New technical paradigms reset the clock. Complex generative AI integration, healthcare interoperability, and any category where the integration surface is still being invented all create fresh high-specificity segments inside markets that had otherwise matured. The reset is why ILG does not have an expiration date as a discipline. It relocates rather than disappears.

---

## Common Failure Patterns

The most common motion-selection mistakes:

**Treating a Bridge like a Toaster.** PLG or SLG applied to a deal that actually needs ILG. *Symptoms:* deal stalls with no clear blocker, eventually "no decision" or churn shortly after signature. *Root cause:* Process Calculator score not honored; reps optimizing for cycle time instead of close quality.

**Treating a Toaster like a Bridge.** ILG applied to a low-specificity deal. *Symptoms:* buyer experiences over-engineering, chooses a faster competitor or self-serves. *Root cause:* reps trained on ILG playbook applying it indiscriminately.

**Treating a Nascent Market like Mature.** PLG or ILG tactics in a market where the buyer cannot yet articulate the problem. *Symptoms:* low engagement, "interesting but not now" responses. *Root cause:* mistaking absence of competition for product-market fit.

**Skipping Reciprocity in ILG.** Running ILG motion but not requiring the buyer to invest in the process — provide artifacts, attend workshops, commit resources. *Symptoms:* lopsided MIP, buyer disengagement post-signature, implementation stalls. *Root cause:* fear of losing the deal by asking for too much.

**Happy-Ears Red Team.** Running the workshop but accepting "everything looks good" without surfacing real failure modes. *Symptoms:* implementation hits unexpected blockers, scope creep, late discovery of saboteurs. *Root cause:* facilitator not pushing hard enough for prospective hindsight.

---

## Key Principle

> "Never apply a Bridge motion to a Toaster, and never sell a Bridge without a Blueprint."

The motion is not about your preference. It is about the deal's physics — derived from the market stage you are operating in and the asset specificity of the deal itself.

---

## Related

- [00-ilg-constitution.md](./00-ilg-constitution.md) — Theoretical framework. Axiom I is the foundation for motion choice.
- [02-cfir-field-mapping.md](./02-cfir-field-mapping.md) — How ILG artifacts operationalize implementation science.
- [03-mathematical-models.md](./03-mathematical-models.md) — Functional forms behind $\Delta_A$, $F_{consensus}$, and the urgency decay rate.
- [process-calculator.md](../../practice/01-field-assets/process-calculator.md) — Operational tool implementing the Decision Framework.
- [ilg-motion/](../../practice/01-field-assets/ilg-motion/) — Bridge motion artifacts (Blueprint / Red Team / MIP).
- [plg-motion/](../../practice/01-field-assets/plg-motion/) — Toaster motion artifacts.
- [03-incentives-vested-commission.md](../../practice/02-internal-ops/03-incentives-vested-commission.md) — Comp structure for ILG sellers.
