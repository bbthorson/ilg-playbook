---
title: "Sales Motion Comparison: ILG vs. PLG vs. SLG"
layer: theory
status: active
version: 2.0
operationalizes: [axiom-1, axiom-2]
canonical_source: theory/01-foundation/00-tcg-constitution.md
---

# Sales Motion Comparison: ILG vs. PLG vs. SLG

**What the three named motions are, once a motion is a region rather than a list entry.**

This document is the practical companion to the [Constitution](./00-tcg-constitution.md). The Constitution explains why motion choice matters. [06-friction-vector.md](./06-friction-vector.md) derives what a motion is. This file says what each named region contains, where the names mislead, and where the boundary of the ILG region sits.

> [!IMPORTANT]
> **Version 2.0 replaced the spine.** Version 1 organized around a three-item list of motions and a Nascent, Efficient and Saturated market-state taxonomy, and carried its own copy of the diagnostic steps. Constitution v17.0 retired all three. A motion is now a region of the friction vector's space, named by which component dominates and how long the vector is, and the diagnostic lives in one place, the [Deal Triage Calculator](../../practice/01-field-assets/deal-triage-calculator.md). What survives here is everything the calculator does not carry: what each region contains, why search-dominant and implementation-dominant deals get confused, and the six conditions that put a deal outside the ILG region entirely.

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

The distinction matters most when someone says their team "already does ILG because they run MEDDPICC on complex deals." Qualification tells you whether a deal is real. It does not reduce the buyer's implementation risk, which is the only thing that closes a Structural deal.

---

## Buyer State and Dominant Cost

Each name answers a different buyer, carrying a different dominant cost. The mindset column is what the direction sounds like in a room:

| Region | Buyer mindset | Direction | Core objective |
|---|---|---|---|
| **PLG** | *"I know my problem. Give me the tool to test it."* | Any, at a level below 15 | **Frictionless activation.** Collapse evaluation cost by letting the buyer verify utility without a seller. |
| **SLG** | *"I'm comfortable in the status quo. Convince me I have a problem."* | Search-dominant | **Problem discovery and urgency.** Educate the buyer, quantify the cost of inaction, create the budget. |
| **ILG** | *"I know my problem. Prove you won't break my business installing a fix."* | Implementation-dominant | **Risk elimination.** Supply pre-sale technical proof and structured risk-sharing governance. |
| *(unnamed)* | *"We cannot get our own people to agree."* | Consensus-dominant | **Alignment.** The instrument set for this region is the thinnest in the repository, and the region is deliberately unnamed until it exists. |

**The names are three points in a space that has four regions and a mixed case.** A deal is not assigned to one of them. It has a direction, and the direction may sit between two named regions or move from one to another as discovery lands.

### A note on splitting $F_{search}$

The Constitution defines $F_{search}$ as "locating the category and viable vendors." Those are two activities, and they peak in different markets. Keeping them fused produces an apparent contradiction, because PLG and SLG both look like they own search.

- **Category search** dominates nascent markets. The buyer cannot name what they need. SLG resolves this through education, and the cost is cognitive.
- **Vendor evaluation** dominates mature, low-specificity markets. The category is legible and the buyer can name five vendors. PLG resolves this by letting them try one, and the cost is time.

ILG deals carry little of either. The buyer knows the category and the field. What they cannot resolve is whether *this* vendor can install *this* system in *their* environment without breaking it, which is $F_{implementation}$ inflated by $\Delta_A$, and no amount of category education or free trial touches it.

---

### What replaced the Market States

Version 1 carried three stages a market passes through, Nascent, Efficient and Saturated, each with a characteristic friction profile, plus a Transitional and Mature shorthand the field rubric used because Efficient and Saturated look alike from outside. All five names are retired.

The taxonomy was a proxy for direction. It said what the friction profile *usually* is for a market at a given age, in place of measuring the profile of the deal in front of you. Once the instrument measures direction, the proxy adds nothing and can disagree with the measurement, which is what a proxy does when it is kept past its usefulness.

The information is not lost. The three legibility signals the stage diagnostic asked for, a recognized category name, three or more nameable vendors, and published third-party coverage, are now three of the four search evidence items in the [Deal Triage Calculator](../../practice/01-field-assets/deal-triage-calculator.md). They score the search gap directly instead of routing through a stage label.

**What the retirement gives up.** A market that is about to mature may behave differently from a mature one of identical present composition, and a present-tense vector cannot see that. Under the current model the difference belongs in $\gamma_{search}$, the rate at which the search gap rebuilds, and nothing tests it. This is recorded in [06-friction-vector.md](./06-friction-vector.md) section 9 rather than solved.

---

## Quick Reference

| Dimension | **ILG** | **PLG** | **SLG** |
|---|---|---|---|
| **Direction** | Implementation-dominant | Any | Search-dominant |
| **Level** | 15 to 30 | Below 15 | 15 to 30 |
| **Deal Archetype** | The Structural Deal | The Turnkey Deal | The Evangelism Deal |
| **Friction Type** | Structural (implementation) | Minimal | Educational (market-creation) |
| **Optimization** | Safety & certainty | Velocity & volume | Education & vision-casting |
| **Primary Metric** | NRR, adoption | User growth, activation | Win rate, category awareness |
| **Sales Cycle** | 3–9 months | Self-service (days) | 6–12 months (often) |
| **ACV Range** | $100k–$1M+ | $0–$50k | $25k–$500k |
| **Decision Makers** | 3–10+ stakeholders | 1–2 | 1–3 (often visionary) |
| **Integration** | Deep (ERP, core systems) | Lightweight (API, SSO) | Variable |
| **Rep Role** | Implementation scientist | Minimal (CS-led expansion) | Educator / market-maker |
| **Comp Structure** | [Vested commission](../../practice/02-internal-ops/03-incentives-vested-commission.md) | CS-led expansion bonuses | Traditional ACV commission |

---

### The regions, on the two axes Axiom I names

The 2x2 that stood here crossed specificity against category legibility. Legibility is not an axis. It is one of the search component's evidence items, and putting it on an axis of its own is what let a deal be scored twice on the same information. The axes are the two quantities Axiom I names.

| | Turnkey (level below 15) | Structural (level 15 to 30) |
|---|---|---|
| **Search-dominant** | Light education, then a self-serve path. The buyer needs to know the category exists and little else. | **Evangelism deal, SLG.** Problem awareness low, category unformed. Educate the market, create the line item. |
| **Consensus-dominant** | A committee attached to a small purchase. Usually a procurement artifact rather than a real alignment problem. | **Unnamed region.** The buyer cannot get their own people to agree. Instrument set absent. |
| **Implementation-dominant** | **Hidden Structural.** Small installation, workflow that matches nothing. The level cannot see it and the divergence modifier can. | **Structural deal, ILG.** Deep integration, multi-stakeholder consensus. Optimize for implementation certainty. |
| **Mixed** | **Turnkey deal, PLG.** Modular tools, standard APIs, low switching cost. Optimize for velocity. | Run the top two components in proportion. |

The **Chaos Trap** is not on this grid, because it is not a region of the space. An undefined workflow is a precondition failure, caught by Step 0 before anything is counted, and it can occur at any level and any direction.

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

**Key activities:** Heavy buyer education, vision-casting, reference architectures, "what does good look like" sessions. Often Challenger-style commercial teaching. Buyer-seller co-design of the solution shape. Field asset: [01-education-led-motion.md](../../practice/01-field-assets/slg-motion/01-education-led-motion.md), which carries the misclassification tripwires and the triggers for pivoting to ILG.

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

This is the same distinction as search-dominant against implementation-dominant, stated in the vocabulary reps already use. It is also the reason direction is read from the amplified components rather than the base ones. Two deals can carry identical educational and installation work, and the one whose buyer already understands the category is not a search deal, because its search gap is closed and there is nothing left there to spend on.

---

## Where the diagnostic lives

The diagnostic is not restated here. It is in the [Deal Triage Calculator](../../practice/01-field-assets/deal-triage-calculator.md), and version 1 of this file carried a second copy that drifted from it. What the calculator emits is a level, a direction, and three component gaps. What this file adds is what to do once you have them, which is the rest of this document.

Three points about the diagnostic that are theory rather than procedure, and so belong here:

**The workflow maturity gate is not a friction component.** It asks whether the buyer's process can be mapped at all. A Level 1 workflow with a legible category and a single decision maker is a Chaos Trap, and no reading of the vector says so, because the vector measures cost and this is a precondition. It runs before anything is counted for that reason.

**Level and direction answer different questions and are read off different quantities.** Level is the $L^1$ norm of base friction, which is asset specificity, a property of the deal. Direction is the share of effective cost each component carries after amplification, which is where the unresolved work sits today. Discovery moves the second and not the first, which is why a Blueprint changes the instrument without reclassifying the deal.

**The instrument counts rather than rates.** Version 4.2 asked for ratings of 1 to 5 and the models raised them to powers, which is not a defensible operation on an ordinal scale. The counts are auditable in a way ratings are not, since a count is a list and a list can be wrong in public. That does not make the instrument honest by itself, and the calculator says what else is needed.

---

## Hybrid Approaches and Transitions

Markets evolve, and individual deals can shift across motion boundaries during the sales cycle. Three common transitions:

**PLG → ILG (Land and Expand).** Start with PLG motion at the team level. When enterprise expansion triggers — cross-functional rollout, security review, organization-wide governance — trigger ILG motion. *Example:* Slack runs PLG for teams and ILG for enterprise rollout.

**SLG → ILG (Maturing Category).** A nascent market becomes mature as standards emerge, analyst coverage develops, and reference customers accumulate. SLG-era sellers must transition to ILG to defend against new entrants and to handle the now-sophisticated buyer base. *Failure mode:* sticking with SLG tactics in a mature market, missing implementation depth.

**SLG → ILG (Complexity Discovery).** A single deal that looked like SLG (sell the vision, close on the merits) turns out to involve deeper integration and political complexity than initially scoped. The rep pivots to ILG mid-cycle: deploy Blueprint, Red Team, MIP. *Failure mode:* rigidly maintaining the original motion as evidence of complexity accumulates.

The Constitution's Boundary Condition (Axiom I) explains why these transitions are necessary: friction must match specificity. When the underlying specificity changes — through market evolution or in-deal discovery — the friction structure must adjust.

### The lifecycle runs one way, and then resets

Left alone, a category ages in a single direction. Standards solidify, integration patterns homogenize, implementation playbooks get published, and asset specificity falls. Both quantities move, and they move differently:

```
Emerging category      → level high, no playbooks        → search and implementation both wide
Consolidating category → level high, patterns forming    → search closes, implementation stays
Commoditized category  → level falls below the boundary  → both close, apparatus stops earning
```

The practical warning is that a motion which fit three years ago may over-serve the same category today. A team still running the full implementation chain on a commoditized category is burning margin on Blueprints the buyer no longer needs. Re-scoring catches it, and a category's level falling below 15 is the signal to migrate.

New technical paradigms reset the clock. Complex generative AI integration, healthcare interoperability, and any category where the integration surface is still being invented all create fresh high-specificity segments inside markets that had otherwise matured. The reset is why ILG does not have an expiration date as a discipline. It relocates rather than disappears.

---

## Common Failure Patterns

The most common motion-selection mistakes. The first two are Axiom I's failure modes seen from the field, with the symptoms a rep observes and the root cause behind them:

**Treating a Structural deal like a Turnkey deal.** Velocity instruments applied to a deal that needs the implementation chain. *Symptoms:* the deal stalls with no clear blocker, ending in no decision, or it closes and churns shortly after signature. Both symptoms, and Axiom I now names both. *Root cause:* the level was not honored, or the counts behind it were deflated, which is the failure the calculator's Count Variance measure exists to make visible.

**Treating a Turnkey deal like a Structural deal.** ILG applied to a low-specificity deal. *Symptoms:* buyer experiences over-engineering, chooses a faster competitor or self-serves. *Root cause:* reps trained on the ILG playbook applying it indiscriminately.

**Reading an unnamed category as a short alternative list.** The buyer names no vendors, so the search count comes out low and the deal routes to velocity or implementation instruments. *Symptoms:* low engagement, "interesting but not now" responses. *Root cause:* mistaking absence of competition for a small choice set. An unnamed category is an unbounded alternative set and scores the maximum search cost, which the calculator states twice because this is the misreading that survives every rewrite.

**Picking a named motion when the vector is mixed.** No component reaches half of effective cost, and the rep chooses the region they know best. *Symptoms:* one binding cost is worked hard and another is untouched, so the deal moves and then stops. *Root cause:* treating the three names as an exhaustive list. They are three points in a space, and a deal is entitled to sit between them.

**Skipping Reciprocity in ILG.** Running ILG motion but not requiring the buyer to invest in the process — provide artifacts, attend workshops, commit resources. *Symptoms:* lopsided MIP, buyer disengagement post-signature, implementation stalls. *Root cause:* fear of losing the deal by asking for too much.

**Happy-Ears Red Team.** Running the workshop but accepting "everything looks good" without surfacing real failure modes. *Symptoms:* implementation hits unexpected blockers, scope creep, late discovery of saboteurs. *Root cause:* facilitator not pushing hard enough for prospective hindsight.

---

## Boundary Conditions: Where ILG Fails

Axiom I states that friction must match asset specificity, which means ILG is wrong wherever the surplus it unlocks is smaller than the friction it imposes. Six conditions put a deal outside the boundary. In each, the correct response is to decline the motion rather than to run a lighter version of it.

**1. No operational baseline exists.** The Blueprint maps a workflow. When there is no workflow to map, the artifact produces a document the buyer and seller invented together, and the Red Team then stress-tests a fiction. This is the Chaos Trap, and it is the reason Step 0 gates the calculator. *Route:* consulting to establish the SOP, then re-qualify.

**2. Deal value cannot carry the friction cost.** ILG consumes solutions-engineering hours before revenue. Below roughly the point where pre-sale cost exceeds the gross margin on the first year, the motion destroys surplus even when the deal closes. Transactional SMB business sits here structurally. *Route:* PLG, or decline.

    This is the affordability half of the level-and-frequency split in [07-governance-forms.md](./07-governance-forms.md) section 6. The level says what the deal needs and frequency says whether it can be paid for, so a one-shot deal above the boundary can genuinely need the full chain and still be correct to decline.

    *Under review.* First-year gross margin is a single-shot test. [05-seller-surplus-model.md §7](./05-seller-surplus-model.md) shows the pre-sale investment amortizes across the renewal stream, so this rule is correct where retention is weak and too strict where it holds. Use it as written until the replacement is agreed.

**3. The category has commoditized.** Integration patterns homogenized, playbooks are published, and switching cost fell. Specificity dropped out from under a motion that used to fit. Teams keep running Blueprints out of habit and lose on cycle time to lighter competitors. *Route:* re-score annually and migrate to velocity instruments when the level drops below 15.

**4. The specification is externally fixed.** A regulatory mandate or a procurement standard that dictates the implementation leaves no discovery surplus to capture. Both parties already know what gets built. Discovery cannot reduce $\Delta_A$ because the gap is already near zero on the dimension that matters. *Route:* compete on price and delivery credibility.

**5. The buyer has no implementation capacity at any price.** The MIP allocates resources the buyer does not have and cannot obtain. This is not a governance failure that better structure repairs; it is a capacity constraint. A signed MIP against absent resources produces a launch failure with a contract attached. *Route:* defer until capacity exists, or sell a managed-service shape instead.

**6. The seller cannot deliver what the motion promises.** ILG makes implementation credibility the product. An organization without the solutions-engineering depth to run a genuine Red Team will produce Happy-Ears workshops, which is worse than not running one, because the buyer now holds documented assurance that the risks were examined. *Route:* build the capability before selling on it.

The first three are properties of the deal. The last three are properties of the environment or the seller, and they are the ones teams skip when auditing their own boundary.

---

## Key Principle

> "Never apply a Turnkey motion to a Structural deal, and never sell a Structural deal without a Blueprint."

The motion is not about your preference. It follows from two measurements: how long the friction vector is, and where it points.

---

## Related

- [00-tcg-constitution.md](./00-tcg-constitution.md) — Axiom I supplies level and direction. Axiom II supplies the per-component amplification direction is read from.
- [06-friction-vector.md](./06-friction-vector.md) — Why a motion is a region rather than a list entry, and what the change retired.
- [02-cfir-field-mapping.md](./02-cfir-field-mapping.md) — How ILG artifacts operationalize implementation science.
- [03-mathematical-models.md](./03-mathematical-models.md) — Functional forms behind $\Delta_A$, $F_{consensus}$, and the urgency decay rate.
- [deal-triage-calculator.md](../../practice/01-field-assets/deal-triage-calculator.md) — The one place the diagnostic lives.
- [ilg-motion/](../../practice/01-field-assets/ilg-motion/) — Structural deal motion artifacts (Blueprint / Red Team / MIP).
- [plg-motion/](../../practice/01-field-assets/plg-motion/) — Turnkey deal motion artifacts.
- [03-incentives-vested-commission.md](../../practice/02-internal-ops/03-incentives-vested-commission.md) — Comp structure for ILG sellers.
