# Glossary and Notation

**Version:** 1.0
**Purpose:** To supply one place to look up any symbol or term used in this repo, and to say where its canonical definition lives.

## How to use this file

Two rules govern what is written here, and they differ by section.

**The term index is an index, not a source of truth.** Every entry carries a one-line identifier and a link to where the concept is actually defined. The identifier exists so you can confirm you found the right entry, not so you can skip reading the source. If an entry and its linked source disagree, **the source wins** and the entry is a bug. Report it or fix it.

**The notation index is canonical.** Symbols had no home before this file. Several are reused across documents with different meanings, and one collision was serious enough that [03-mathematical-models.md](./03-mathematical-models.md) had to stop mid-derivation to disambiguate it by hand. That is the gap this section closes. When a document introduces a new symbol, add it here in the same commit.

---

## Notation index

### The Surplus equation

| Symbol | Meaning | Defined in |
|---|---|---|
| $S$ | Deal Surplus. Must exceed 0 for a deal to close. | [Constitution, Part III](./00-ilg-constitution.md) |
| $OC_{switching}$ | Opportunity cost of staying with the status quo. Equals $V_{effective}(t) - V_{next\_best}$. | [Constitution, Part III](./00-ilg-constitution.md) |
| $y$ | Total perceived transaction cost, reduced form. Equals $ax^2 + c$. | [Constitution, Axiom II](./00-ilg-constitution.md) |
| $D(t)$ | A deal's trajectory through time, $TC(t) - OC(t)$. Stays below the ceiling only while Axiom III holds. | [Constitution, Axiom III](./00-ilg-constitution.md) |

### Value terms (Axiom I)

| Symbol | Meaning | Defined in |
|---|---|---|
| $V_{solution}$ | Peak perceived value at the triggering event. | [Constitution, Axiom I](./00-ilg-constitution.md) |
| $V_{effective}(t)$ | Value after decay. Equals $V_{solution} \cdot e^{-\delta t}$. | [Constitution, Axiom I](./00-ilg-constitution.md) |
| $V_{next\_best}$ | Value of the buyer's next best alternative, including building it themselves. | [Constitution, Axiom I](./00-ilg-constitution.md) |
| $k$ | Asset specificity of the deal. | [Constitution, Axiom I](./00-ilg-constitution.md) |
| $k_{threshold}$ | The Bridge / Toaster boundary. Above it, ILG applies. | [Process Calculator](../../practice/01-field-assets/process-calculator.md) |
| $F_{deployed}$ | The friction structure the seller actually deploys. Must scale with $k$. | [Constitution, Axiom I](./00-ilg-constitution.md) |

### Friction terms (Axiom II)

| Symbol | Meaning | Defined in |
|---|---|---|
| $F_{base}$ | The three cost components summed, before amplification. | [Constitution, Axiom II](./00-ilg-constitution.md) |
| $F_{effective}$ | Base friction after amplification. Equals $F_{base} \cdot (1 + \Delta_A)$. | [Constitution, Axiom II](./00-ilg-constitution.md) |
| $F_{search}$ | Cost of locating the category and viable vendors. Splits into category search and vendor evaluation. | [01-sales-motion-comparison.md](./01-sales-motion-comparison.md) |
| $F_{consensus}$ | Internal buyer alignment plus external bargaining. | [03-mathematical-models.md](./03-mathematical-models.md) |
| $F_{implementation}$ | Deployment plus sustained change. | [Constitution, Axiom II](./00-ilg-constitution.md) |

### Asymmetry terms (Axiom II)

| Symbol | Meaning | Defined in |
|---|---|---|
| $\Delta_A$ | Bilateral Asymmetry Gap. A **sum**, not a difference: $I_{seller} + I_{buyer}$. | [03-mathematical-models.md §2.1](./03-mathematical-models.md) |
| $\hat{\Delta}_A$ | The gap normalized to $[0, 1]$. **Required before substituting into either cost equation.** | [03-mathematical-models.md §1.5](./03-mathematical-models.md) |
| $\Delta_A^*$ | Akerlof Exit Threshold. Above it the buyer leaves the market entirely. | [Constitution, Clarifying Concepts](./00-ilg-constitution.md) |
| $I_{seller}$ | Seller Ignorance. What the seller has not mapped about the buyer's environment. | [03-mathematical-models.md §2.2](./03-mathematical-models.md) |
| $I_{buyer}$ | Buyer Uncertainty. Doubt about return variance and vendor capability. | [03-mathematical-models.md §2.3](./03-mathematical-models.md) |
| $x$ | Uncertainty in the reduced form. Approximately $\Delta_A$, but see the disambiguation below. | [Constitution, Axiom II](./00-ilg-constitution.md) |

### Coefficients and parameters

| Symbol | Meaning | Default | Defined in |
|---|---|---|---|
| $a$ | Friction-asymmetry coupling. Anchored at 2.25 by analogy, not measurement. | 2.25 | [03-mathematical-models.md §1.6](./03-mathematical-models.md) |
| $b$ | Rate at which base friction grows per unit of asymmetry. The derivation identifies $a$ with $b$. | measured | [03-mathematical-models.md §1.3](./03-mathematical-models.md) |
| $c$ | Direct cost. The irreducible floor of licence fees and unavoidable deployment work. | measured | [Constitution, Axiom II](./00-ilg-constitution.md) |
| $\lambda$ | Loss aversion coefficient from prospect theory. **Not the same quantity as $a$.** | 2.25 | [prospect-theory.md](../02-research/prospect-theory.md) |
| $\alpha$ | Baseline coordination overhead in the consensus model. | 1.0 | [03-mathematical-models.md §3.1](./03-mathematical-models.md) |
| $\beta$ | Organizational complexity exponent. Above 1 because channels grow as $N(N-1)/2$. | 1.35 | [03-mathematical-models.md §3.1](./03-mathematical-models.md) |
| $N$ | Stakeholders holding veto power or evaluation responsibility. | measured | [03-mathematical-models.md §3.1](./03-mathematical-models.md) |
| $I_i$ | Stakeholder $i$'s utility from the initiative, on $[-1, 1]$. | measured | [03-mathematical-models.md §3.2](./03-mathematical-models.md) |
| $\text{Var}(I_i)$ | Variance in stakeholder incentive alignment, bounded above by 1. | measured | [03-mathematical-models.md §3.2](./03-mathematical-models.md) |
| $TO$ | Technical overlap score on $[1, 5]$. Architectural alignment among technical evaluators. | measured | [03-mathematical-models.md §3.4](./03-mathematical-models.md) |
| $U_{tech}$, $U_{process}$ | Unmapped technical complexity and unmapped operational variance. | measured | [03-mathematical-models.md §2.2](./03-mathematical-models.md) |
| $w_t$, $w_p$ | Weights on the two ignorance terms, summing to 1. | 0.6, 0.4 | [03-mathematical-models.md §2.2](./03-mathematical-models.md) |
| $\phi_t$, $\phi_p$ | Risk acceleration exponents. | 1.2, 1.1 | [03-mathematical-models.md §2.2](./03-mathematical-models.md) |
| $\sigma_{ROI} / \bar{R}$ | Coefficient of variation of projected return. | measured | [03-mathematical-models.md §2.3](./03-mathematical-models.md) |
| $K_{vendor}$ | Demonstrated vendor proof. Blueprints, reference architectures, validated benchmarks. | measured | [03-mathematical-models.md §2.3](./03-mathematical-models.md) |
| $\mu$, $\nu$, $\kappa$ | Sensitivity to return uncertainty, baseline doubt for an unvalidated vendor, decay of doubt per unit of proof. | 1.0, 2.0, 0.5 | [03-mathematical-models.md §2.3](./03-mathematical-models.md) |
| $\lambda_{inertia}$ | Organizational inertia. Bureaucracy, competing projects, status quo preference. | measured | [03-mathematical-models.md §4.2](./03-mathematical-models.md) |
| $E_{external}$ | Magnitude of the external catalyst. The only term in $\delta$ a seller can move. | measured | [03-mathematical-models.md §4.2](./03-mathematical-models.md) |

### Time and governance terms

| Symbol | Meaning | Defined in |
|---|---|---|
| $\delta$ | Decay rate of urgency after the triggering event. | [03-mathematical-models.md §4](./03-mathematical-models.md) |
| $\delta_{discount}$ | A party's discount factor. The weight it places on future payoffs. | [Constitution, Axiom III](./00-ilg-constitution.md) |
| $\gamma$ | Rate at which the asymmetry gap rebuilds per unit time, absent maintenance. | [Constitution, Axiom II](./00-ilg-constitution.md) |
| $\gamma_r$ | Responsiveness converting external pressure into internal action. | [03-mathematical-models.md §4.2](./03-mathematical-models.md) |
| $\gamma_{TO}$ | Weight on the technical overlap term. | 0.20, [03-mathematical-models.md §3.4](./03-mathematical-models.md) |
| $T$, $R$, $P$ | Temptation, reward, and punishment payoffs in the cooperation condition. | [game-theory-and-nrr.md](../02-research/game-theory-and-nrr.md) |

### Retrospective measures

| Symbol | Meaning | Defined in |
|---|---|---|
| FAR | Friction Allocation Ratio. Share of implementation effort spent before signature. | [Friction Efficiency Index](../../practice/02-internal-ops/05-diagnostics-friction-efficiency-index.md) |
| BCV | Buyer Commitment Velocity. How fast the buyer mobilized. | [Friction Efficiency Index](../../practice/02-internal-ops/05-diagnostics-friction-efficiency-index.md) |
| RMS | Risk Mitigation Score. Share of discovered risk closed before signature. | [Friction Efficiency Index](../../practice/02-internal-ops/05-diagnostics-friction-efficiency-index.md) |
| SVI | Scope Variance Index. Scope stability through delivery. | [Friction Efficiency Index](../../practice/02-internal-ops/05-diagnostics-friction-efficiency-index.md) |
| $H_{pre}$, $H_{post}$ | Solutions-engineering and implementation hours before and after signature. | [Friction Efficiency Index](../../practice/02-internal-ops/05-diagnostics-friction-efficiency-index.md) |

---

## Symbol disambiguation

Five pairs look alike and mean different things. Each has produced a documented error or required an inline correction somewhere in this repo.

**1. $\gamma$ carries three unrelated meanings.** In the Constitution, $\gamma$ is the rate at which the asymmetry gap rebuilds over time. In the mathematical models it appears twice more, as $\gamma_r$ (responsiveness to an external catalyst) and $\gamma_{TO}$ (the technical overlap weight). The subscripts are load-bearing. A bare $\gamma$ always means asymmetry drift.

**2. $\delta$ and $\delta_{discount}$ are unrelated.** Bare $\delta$ is the urgency decay rate, and it belongs to Axiom I's half of the Decay Clock. $\delta_{discount}$ is a party's weight on future payoffs, and it belongs to Axiom III's cooperation condition. They share a letter and nothing else. A rising $\delta$ is bad for the deal, and a rising $\delta_{discount}$ is good for it.

**3. $\Delta_A$ and $\hat{\Delta}_A$ differ by an order of magnitude.** The [Asymmetry Scorecard](../../practice/02-internal-ops/04-incentives-asymmetry-scorecard.md) produces a raw score on $[2, 10]$. Neither cost equation accepts that range. Substituting a raw 10 would inflate base friction elevenfold, which no observed deal supports. Normalize first. Use raw scores for the scorecard's field triage bands, and normalized values in any equation.

**4. $a$, $b$, and $\lambda$ are three different quantities that all sit near 2.25.** $\lambda$ is the measured loss aversion coefficient from prospect theory. $b$ is the rate at which base friction grows per unit of asymmetry, and the derivation identifies the model's $a$ with $b$. The anchor $a \approx 2.25$ borrows $\lambda$'s magnitude as behavioural justification, and it is not a measurement of $a$. Do not cite $a$ as though prospect theory established it.

**5. $F_{base}$ and $F_{effective}$ differ by the multiplier.** $F_{base}$ is the three components summed. $F_{effective}$ is that sum after amplification by $(1 + \Delta_A)$. A third form appears inside the derivation, where base friction is written as a function of the gap, $F_{base}(\Delta_A) = c + b\Delta_A$. Quoting a friction figure without saying which form it is makes the number unusable.

---

## Term index

One line each, then the canonical source. The line identifies the term. The source defines it.

### Deal classification

| Term | Identifier | Canonical source |
|---|---|---|
| **Bridge** | A deal whose specificity requires the ILG motion. Scores 10 to 20. | [Process Calculator](../../practice/01-field-assets/process-calculator.md) |
| **Toaster** | A low-specificity deal that a velocity motion serves better. Scores 4 to 9. | [Process Calculator](../../practice/01-field-assets/process-calculator.md) |
| **Chaos Trap** | A buyer with no documented workflow, in any market. Route to consulting, not to a motion. | [Process Calculator, Step 0](../../practice/01-field-assets/process-calculator.md) |
| **Market States** | Nascent, Transitional, Mature. Each carries a characteristic friction profile. | [Constitution, Clarifying Concepts](./00-ilg-constitution.md) |
| **Boundary Condition** | The test every deal passes before ILG investment is justified. | [Constitution, Part II](./00-ilg-constitution.md) |

### Axiom II concepts

| Term | Identifier | Canonical source |
|---|---|---|
| **Friction Allocation Principles** | The four conditions a signal mechanism must satisfy to reduce $\Delta_A$. | [Constitution, Part II](./00-ilg-constitution.md) |
| **Single Crossing Property** | A signal informs only when it costs the high-quality actor proportionally less. | [costly-signals.md](../02-research/costly-signals.md) |
| **Costly Signal** | A demonstration a low-quality competitor could not afford to replicate. | [costly-signals.md](../02-research/costly-signals.md) |
| **Cheap Talk** | A signal that fails the Single Crossing Property and therefore carries no information. | [Constitution, Axiom II](./00-ilg-constitution.md) |
| **Akerlof Exit Threshold** | The asymmetry level beyond which the buyer stops participating in the market. | [Constitution, Clarifying Concepts](./00-ilg-constitution.md) |
| **Jevons Vulnerability** | A channel whose binding constraint is production cost, and which therefore collapses when that cost falls. | [channel-collapse.md](../02-research/channel-collapse.md) |
| **Buying Center** | The set of people in a purchase decision, each judging it against a different objective. | [buying-center-dynamics.md](../02-research/buying-center-dynamics.md) |
| **Decay Clock** | The two time dynamics that erode deal viability before close. | [Constitution, Bridge Concepts](./00-ilg-constitution.md) |

### Axiom III concepts

| Term | Identifier | Canonical source |
|---|---|---|
| **Recursive Cooperation** | The cooperation condition must hold at every level where signal quality is adjudicated. | [Constitution, Part II](./00-ilg-constitution.md) |
| **Reputation Depreciation** | Past signals lose value without intervening evidence of continued delivery. | [Constitution, Part II](./00-ilg-constitution.md) |
| **Demurrage on Credibility** | The prescription following from depreciation. Reputation must be re-earned to retain signal value. | [Constitution, Part II](./00-ilg-constitution.md) |
| **Williamson Hold-Up** | Once asset-specific investment is sunk, either party can extract its value. | [transaction-cost-economics.md](../02-research/transaction-cost-economics.md) |
| **Residual Control Rights** | The pre-agreed authority to decide in states no contract specified. | [incomplete-contracts.md](../02-research/incomplete-contracts.md) |
| **Staged Commitment** | Why bilateral commitments must be staged rather than merely mutual. | [Constitution, Bridge Concepts](./00-ilg-constitution.md) |
| **Real Option** | The economic value of being able to defer an irreversible decision under uncertainty. | [real-options.md](../02-research/real-options.md) |
| **Handoff Rule** | The Blueprint must reach Customer Success intact, or $\Delta_A$ resets on the receiving side. | [Constitution, Part IV](./00-ilg-constitution.md), operationalized in [04-sustaining-adoption-review.md](../../practice/01-field-assets/ilg-motion/04-sustaining-adoption-review.md) |

### Artifact vocabulary

| Term | Identifier | Canonical source |
|---|---|---|
| **Contextual Blueprint** | Discovery artifact that reduces Seller Ignorance. | [01-discovery-contextual-blueprint.md](../../practice/01-field-assets/ilg-motion/01-discovery-contextual-blueprint.md) |
| **Red Team** | Pre-mortem workshop that reduces Buyer Uncertainty. | [02-validation-red-team-protocol.md](../../practice/01-field-assets/ilg-motion/02-validation-red-team-protocol.md) |
| **Mutual Implementation Plan (MIP)** | The governance instrument that distributes decision authority and stages commitment. | [03-closing-mutual-implementation-plan.md](../../practice/01-field-assets/ilg-motion/03-closing-mutual-implementation-plan.md) |
| **Sustaining Adoption Review** | The post-signature artifact. Handoff packet, RE-AIM review, QBR protocol, and renewal evidence. | [04-sustaining-adoption-review.md](../../practice/01-field-assets/ilg-motion/04-sustaining-adoption-review.md) |
| **Education-Led Motion** | The SLG field asset. Written mainly as a counter-example showing which ILG machinery to leave switched off. | [01-education-led-motion.md](../../practice/01-field-assets/slg-motion/01-education-led-motion.md) |
| **Reciprocity Gate** | The artifacts a buyer must supply before discovery advances. | [01-discovery-contextual-blueprint.md](../../practice/01-field-assets/ilg-motion/01-discovery-contextual-blueprint.md) |
| **Sacred Cow** | A politically protected workflow, tool, or team. | [01-discovery-contextual-blueprint.md](../../practice/01-field-assets/ilg-motion/01-discovery-contextual-blueprint.md) |
| **The Casualty** | The stakeholder who loses power, budget, or status if the initiative succeeds. | [01-discovery-contextual-blueprint.md](../../practice/01-field-assets/ilg-motion/01-discovery-contextual-blueprint.md) |
| **Negative Capability Declaration** | Stating platform limitations before signature, as a costly signal. | [01-discovery-contextual-blueprint.md](../../practice/01-field-assets/ilg-motion/01-discovery-contextual-blueprint.md) |
| **Resource Expiry Clause** | The buyer-side hostage that makes buyer delay costly. | [03-closing-mutual-implementation-plan.md](../../practice/01-field-assets/ilg-motion/03-closing-mutual-implementation-plan.md) |
| **Vested Commission** | Comp structure tying rep payout to outcomes rather than signature. | [03-incentives-vested-commission.md](../../practice/02-internal-ops/03-incentives-vested-commission.md) |

### External frameworks

| Term | Identifier | Canonical source |
|---|---|---|
| **CFIR** | Implementation-science framework for reading a buyer's organization pre-sale. | [cfir.md](../02-research/cfir.md), mapped in [02-cfir-field-mapping.md](./02-cfir-field-mapping.md) |
| **RE-AIM** | Five-dimension framework for post-sale success measurement. | [re-aim-framework.md](../02-research/re-aim-framework.md) |
| **NRR** | Net Revenue Retention. The lagging indicator of the four upstream RE-AIM dimensions. | [re-aim-framework.md](../02-research/re-aim-framework.md) |
| **JOLT Effect** | Research on buyer indecision, and why urgency tactics backfire on indecisive buyers. | [fear-of-failure.md](../02-research/fear-of-failure.md) |

---

## Maintaining this file

- **New symbol introduced anywhere:** add a row to the notation index in the same commit.
- **New concept that two or more directories reference:** add a row to the term index, pointing at its canonical home. Do not define it here.
- **A term is renamed or retired:** update the row, and add the old name to the retired-terms lint rule if this repo has one, so the rename cannot drift back.
- **An entry disagrees with its source:** the source wins. Fix the entry.

## Related

- [00-ilg-constitution.md](./00-ilg-constitution.md) supplies the axioms and the clarifying concepts most term entries point to.
- [03-mathematical-models.md](./03-mathematical-models.md) supplies the functional forms and every parameter default, plus the provenance status of each.
- [01-sales-motion-comparison.md](./01-sales-motion-comparison.md) covers motion vocabulary in context.
- [ilg-concept-map.md](../../publishing/02-tools/ilg-concept-map.md) is the content architecture for public writing, which is a different purpose from this file. It plans what to write. This file says what things mean.
