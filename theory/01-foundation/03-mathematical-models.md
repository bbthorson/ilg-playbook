# Mathematical Models

**Version:** 1.0
**Purpose:** To specify the functional forms behind the variables the [Constitution](./00-ilg-constitution.md) names but does not compute.

The Constitution is axioms-first. It states that effective transaction cost rises with the bilateral asymmetry gap, that consensus friction rises with committee size, and that urgency decays from a triggering event. It does not say *by how much*, or *as a function of what*. This file supplies those functional forms.

Nothing here introduces new claims. Every model traces to a term the Constitution already defines. If a model here cannot be traced to an axiom, it does not belong in this file either.

> [!IMPORTANT]
> **Calibration status.** The functional forms below are specified, not fitted. Parameter defaults are reasoned starting values, not empirical estimates from booked deal data. Section 6 marks which parameters carry literature support and which are placeholders. Use these models to structure judgment, not to forecast.

---

## 1. The Two Representations of Transaction Cost

Axiom II carries two equations for the same quantity. The Constitution presents both and asserts they are representations of one thing. This section shows why that assertion holds.

### 1.1 The structural form

$$F_{effective} = (F_{search} + F_{consensus} + F_{implementation}) \cdot (1 + \Delta_A)$$

This form decomposes cost into three components that arise from distinct conditions and respond to distinct interventions. Its value is diagnostic. When a deal stalls, this form tells you which component is binding and therefore which artifact to deploy.

### 1.2 The reduced form

$$y = a \Delta_A^2 + c$$

This form collapses the decomposition into a single convex curve. Its value is argumentative. It shows why the traditional levers fail: because cost grows faster than linearly in uncertainty, cutting the constant term $c$ through discounting cannot offset a large $\Delta_A$.

### 1.3 The derivation connecting them

The structural form leaves one assumption implicit: that base friction is independent of the asymmetry gap. It is not.

An uncertain buyer does not simply pay a surcharge on a fixed quantity of work. The uncertainty changes how much work exists. A buyer who cannot verify the seller's claims adds stakeholders to the evaluation, adds security review cycles, adds proof-of-concept stages, and widens scope to cover contingencies they cannot rule out. Each addition raises $F_{consensus}$ and $F_{implementation}$ directly, before any multiplier applies.

Write base friction as a function of the gap:

$$F_{base}(\Delta_A) = c + b \Delta_A$$

Where $c$ is the irreducible floor (license fees, direct outlays, the deployment work that happens even under perfect information) and $b$ is the rate at which base friction grows per unit of asymmetry.

Substituting into the structural form:

$$F_{effective} = (c + b\Delta_A)(1 + \Delta_A) = b\Delta_A^2 + (b + c)\Delta_A + c$$

The reduced form is this expression with the middle term dropped and $a$ identified with $b$. The two representations describe the same cost. The reduced form is the structural form after you let base friction depend on asymmetry and then discard the linear term.

### 1.4 What the reduced form gives up

Two things, and both matter in the field.

**The linear term.** Dropping $(b + c)\Delta_A$ is not justified by that term being small. Over the normalized operating range defined in Section 1.5, the linear term is comparable to the quadratic term and sometimes larger. The reduced form is a two-parameter approximation of a three-parameter expression. When $a$ and $c$ are fitted to observed deals rather than assumed, they absorb the discarded term across the operating range. What the reduced form preserves, and the reason it earns its place in the framework, is convexity. Convexity is the property the Three Sales Levers argument depends on.

**The component decomposition.** The reduced form cannot tell you whether search, consensus, or implementation is binding. It produces a number, not a diagnosis.

**Operating rule.** Use the structural form to diagnose a specific deal. Use the reduced form to explain why discounting fails and to frame the three levers. Do not use the reduced form to choose an intervention.

### 1.5 Normalizing the gap before substitution

The [Bilateral Asymmetry Scorecard](../../practice/02-internal-ops/04-incentives-asymmetry-scorecard.md) produces a raw score on $[2, 10]$. Neither equation accepts that range directly. At a raw score of 10 the structural multiplier $(1 + \Delta_A)$ would inflate base friction elevenfold, which no observed deal supports.

Normalize before substituting:

$$\hat{\Delta}_A = \frac{\Delta_A^{raw} - 2}{8}, \qquad \hat{\Delta}_A \in [0, 1]$$

This keeps the structural multiplier in $[1, 2]$ and keeps the reduced form's quadratic term bounded by $a$. Use the raw score for the field triage bands in the scorecard. Use the normalized value in either equation. Confusing the two produces cost estimates off by an order of magnitude.

The normalized gap may exceed 1 when asymmetry rebuilds past the instrument's ceiling under the Decay Clock dynamics ($\hat{\Delta}_A(t) = \hat{\Delta}_A(0) + \gamma t$). The scorecard measures a point in time and cannot observe drift beyond its own range.

### 1.6 A note on the coefficient $a$

The derivation identifies $a$ with $b$, the rate at which base friction grows per unit of asymmetry. It does not identify $a$ with the loss aversion coefficient $\lambda$.

The anchor $a \approx 2.25$ borrows $\lambda$'s magnitude as a behavioral justification for why $b$ is large. Buyers add review cycles and contingency scope because they weight potential losses roughly twice as heavily as equivalent gains, so the work a buyer generates per unit of unresolved uncertainty is substantial. That reasoning supports the order of magnitude. It is not a measurement. The Constitution's hedge on $\lambda$ (conceptual anchor, likely higher in organizational contexts) applies with equal force to $a$.

---

## 2. The Bilateral Asymmetry Gap

### 2.1 Definition

$$\Delta_A = I_{seller} + I_{buyer}$$

The gap is a **sum**, not a difference. Total informational misalignment across the buyer-seller boundary is the seller's ignorance of the buyer's environment plus the buyer's uncertainty about the seller's capability. A deal where both sides are equally blind is not symmetric in any useful sense. It is maximally uninformed on both sides, and $\Delta_A$ must reflect that.

$\Delta_A = 0$ represents complete informational symmetry.

### 2.2 Seller Ignorance

Seller Ignorance measures what the seller has not yet mapped about the buyer's architecture and operations:

$$I_{seller} = w_t \cdot U_{tech}^{\phi_t} + w_p \cdot U_{process}^{\phi_p}$$

| Symbol | Meaning | Range | Default |
|---|---|---|---|
| $U_{tech}$ | Unmapped technical complexity (legacy systems, custom APIs, security controls) | $[0, 10]$ | measured |
| $U_{process}$ | Unmapped operational variance (undocumented workflows, cross-department edge cases) | $[0, 10]$ | measured |
| $w_t, w_p$ | Weights, with $w_t + w_p = 1$ | $(0, 1)$ | 0.6, 0.4 |
| $\phi_t, \phi_p$ | Risk acceleration exponents | $\ge 1$ | 1.2, 1.1 |

**Properties.** The function increases in both inputs:

$$\frac{\partial I_{seller}}{\partial U_{tech}} = w_t \phi_t U_{tech}^{\phi_t - 1} > 0$$

Because $\phi_t, \phi_p \ge 1$, the second derivative is non-negative. Unmapped technical complexity generates accelerating discovery risk rather than proportional discovery risk. The Blueprint targets this term.

### 2.3 Buyer Uncertainty

Buyer Uncertainty measures doubt about return variance and vendor capability:

$$I_{buyer} = \mu \cdot \frac{\sigma_{ROI}}{\bar{R}} + \nu \cdot e^{-\kappa K_{vendor}}$$

| Symbol | Meaning | Range | Default |
|---|---|---|---|
| $\sigma_{ROI} / \bar{R}$ | Coefficient of variation of projected return | $\ge 0$ | measured |
| $K_{vendor}$ | Demonstrated vendor proof (blueprints, reference architectures, validated benchmarks) | $[0, 10]$ | measured |
| $\mu$ | Sensitivity to return uncertainty | $> 0$ | 1.0 |
| $\nu$ | Baseline doubt for an unvalidated vendor | $> 0$ | 2.0 |
| $\kappa$ | Decay of doubt per unit of proof | $> 0$ | 0.5 |

**Properties.** Proof reduces doubt with diminishing returns:

$$\frac{\partial I_{buyer}}{\partial K_{vendor}} = -\nu \kappa e^{-\kappa K_{vendor}} < 0$$

As proof accumulates, buyer uncertainty approaches a floor set by return variance alone:

$$\lim_{K_{vendor} \to \infty} I_{buyer} = \mu \cdot \frac{\sigma_{ROI}}{\bar{R}}$$

This floor is the model's most useful field implication. No quantity of costly signaling drives buyer uncertainty to zero while the return itself remains volatile. Past a point, the seller stops investing in proof and starts working on the variance of the projected return. The Red Team targets $K_{vendor}$. The MIP targets $\sigma_{ROI}$ by bounding downside through staged gates.

---

## 3. Consensus Friction

### 3.1 Formulation

$$F_{consensus} = \alpha \cdot N^{\beta} \cdot (1 + \text{Var}(I_i))$$

| Symbol | Meaning | Range | Default |
|---|---|---|---|
| $N$ | Stakeholders with veto power or evaluation responsibility | $\ge 1$ | measured |
| $\text{Var}(I_i)$ | Variance in stakeholder incentive alignment | $[0, 1]$ | measured |
| $\alpha$ | Baseline coordination overhead | $> 0$ | 1.0 |
| $\beta$ | Organizational complexity exponent | $[1.2, 2.0]$ | 1.35 |

Variance is bounded above by 1 because $I_i$ is bounded on $[-1, 1]$. A computed value above 1 indicates an arithmetic error, not an unusually divided committee.

The exponent $\beta > 1$ reflects that communication channels grow as $N(N-1)/2$ rather than as $N$. Adding the sixth stakeholder to a committee costs more than adding the second.

### 3.2 Incentive variance

Let $I_i \in [-1, 1]$ denote stakeholder $i$'s utility from the initiative, where $+1$ means the initiative advances their incentives, 0 means no effect, and $-1$ means it conflicts directly with their measured objectives or operational control.

$$\bar{I} = \frac{1}{N}\sum_{i=1}^{N} I_i \qquad \text{Var}(I_i) = \frac{1}{N}\sum_{i=1}^{N}(I_i - \bar{I})^2$$

When every stakeholder holds identical alignment, variance is zero and friction reduces to the structural floor $\alpha N^{\beta}$. Size alone imposes cost even under perfect agreement.

### 3.3 Sensitivity

$$\frac{\partial F_{consensus}}{\partial N} = \alpha \beta N^{\beta-1}(1 + \text{Var}(I_i)) \qquad \frac{\partial^2 F_{consensus}}{\partial N^2} > 0$$

$$\frac{\partial F_{consensus}}{\partial \text{Var}(I_i)} = \alpha N^{\beta}$$

The return on reducing misalignment scales with $N^{\beta}$. In a committee of three, aligning incentives produces modest gains. In a committee of ten, it produces the largest single reduction available to the seller. This is the quantitative case for running the Red Team workshop on large committees specifically, and it is why the [Consensus Friction Calculator](../../practice/01-field-assets/consensus-friction-calculator.md) escalates to executive sponsorship above a threshold rather than recommending more meetings.

### 3.4 Field extension: technical overlap

The field calculator carries one term this section does not:

$$F_{consensus} = \alpha N^{\beta}(1 + \text{Var}(I_i))(1 + \gamma_{TO} \cdot TO)$$

Where $TO \in [1, 5]$ scores architectural alignment among technical evaluators and $\gamma_{TO} = 0.20$.

The term exists because incentive variance under-captures a specific and common failure. Two architects can both want the project to succeed, score identically on incentive alignment, and still deadlock on hosting model or integration pattern. Technical philosophy conflict is not incentive conflict, and treating it as one causes the model to score fractured engineering organizations as low-friction.

Treat $TO$ as a field refinement rather than core theory. The two-term form above is what the axioms require. The three-term form is what practitioners need to avoid a predictable blind spot.

---

## 4. Urgency Decay

### 4.1 Value decay

$$V_{solution}(t) = V_0 \cdot e^{-\delta t}$$

Where $V_0$ is peak perceived value at the triggering event and $t$ is elapsed months. This is the Axiom I half of the Decay Clock.

### 4.2 Structural form of the decay rate

The Constitution treats $\delta$ as a parameter. It has structure:

$$\delta = \frac{\lambda_{inertia}}{1 + \gamma_r E_{external}}$$

| Symbol | Meaning | Range | Default |
|---|---|---|---|
| $\lambda_{inertia}$ | Organizational inertia (bureaucracy, competing projects, status quo preference) | $[0.1, 2.0]$ | measured |
| $E_{external}$ | Magnitude of external catalyst (regulatory mandate, competitive threat, market shift) | $[0, 10]$ | measured |
| $\gamma_r$ | Responsiveness converting external pressure into internal action | $[0.1, 1.0]$ | 0.5 |

Note that $\gamma_r$ here is the responsiveness factor and is distinct from $\gamma$ in the Constitution's asymmetry drift equation $\Delta_A(t) = \Delta_A(0) + \gamma t$. The subscript keeps them separate.

### 4.3 Boundary behavior

With no external catalyst, decay runs at the full rate of organizational inertia:

$$\lim_{E_{external} \to 0} \delta = \lambda_{inertia}$$

With an overwhelming catalyst, decay approaches zero and perceived value holds:

$$\lim_{E_{external} \to \infty} \delta = 0$$

$$\frac{\partial \delta}{\partial E_{external}} = \frac{-\gamma_r \lambda_{inertia}}{(1 + \gamma_r E_{external})^2} < 0 \qquad \frac{\partial \delta}{\partial \lambda_{inertia}} = \frac{1}{1 + \gamma_r E_{external}} > 0$$

**Field implication.** The seller cannot change the buyer's inertia. The seller can find, name, and quantify an external catalyst the buyer has not yet connected to this decision. That is the only term in $\delta$ a seller can move, which is why the Blueprint asks for the economic event by name.

---

## 5. Parameter Reference

| Parameter | Symbol | Default | Provenance status |
|---|---|---|---|
| Friction-asymmetry coupling | $a$ | 2.25 | **Anchored by analogy.** Borrows $\lambda \approx 2.25$ (Kahneman & Tversky 1979) as an order-of-magnitude justification. Not fitted to deal data. |
| Technical weight | $w_t$ | 0.6 | **Chosen.** No source. Placeholder pending calibration. |
| Tech acceleration exponent | $\phi_t$ | 1.2 | **Chosen.** Convexity is motivated by Williamson's asset specificity argument. The specific value is not. |
| Process acceleration exponent | $\phi_p$ | 1.1 | **Chosen.** No source. |
| Return uncertainty sensitivity | $\mu$ | 1.0 | **Chosen.** Normalizing convention. |
| Unvalidated vendor doubt | $\nu$ | 2.0 | **Chosen.** No source. |
| Vendor proof decay | $\kappa$ | 0.5 | **Chosen.** Diminishing returns motivated by Spence (1973). The rate is not. |
| Committee complexity exponent | $\beta$ | 1.35 | **Structurally motivated.** $\beta > 1$ follows from $N(N-1)/2$ channel growth (Cyert & March 1963; Webster & Wind 1972). The value within $[1.2, 2.0]$ is chosen. |
| Technical overlap weight | $\gamma_{TO}$ | 0.20 | **Chosen.** Field refinement, not core theory. See Section 3.4. |
| Coordination overhead | $\alpha$ | 1.0 | **Chosen.** Normalizing convention. |
| Responsiveness factor | $\gamma_r$ | 0.5 | **Chosen.** Staging logic motivated by Dixit & Pindyck (1994). The value is not. |

Read the third column before quoting any number outside this repository. Two parameters carry literature support for their *shape*. None carries literature support for its *value*.

---

## 6. What Would Make These Models Empirical

The models become predictive rather than organizing when three things happen:

1. **Scorecard scores are logged at deal open and deal close** across enough deals to fit $a$ and $c$ against realized cycle length and outcome.
2. **Committee size and stakeholder alignment are recorded in the CRM** as structured fields rather than narrative notes, which makes $\beta$ estimable.
3. **Triggering events are dated**, which makes $\delta$ observable as the decay in buyer-reported urgency between the event and close.

Until then, treat every output as a structured comparison between deals rather than a quantity. A deal scoring 7.2 is meaningfully worse than one scoring 4.1. Neither number predicts a close date.

---

## Related

- [00-ilg-constitution.md](./00-ilg-constitution.md) — The axioms these models serve. Axiom II carries both cost representations reconciled in Section 1.
- [01-sales-motion-comparison.md](./01-sales-motion-comparison.md) — Motion selection, which consumes the Process Calculator score rather than these models.
- [Bilateral Asymmetry Scorecard](../../practice/02-internal-ops/04-incentives-asymmetry-scorecard.md) — Field instrument producing $\Delta_A$.
- [Consensus Friction Calculator](../../practice/01-field-assets/consensus-friction-calculator.md) — Field instrument producing $F_{consensus}$.
- [Milestone Valuation Model](../../practice/01-field-assets/milestone-valuation-model.md) — Applies staged uncertainty decay to MIP gate design.
- [real-options.md](../02-research/real-options.md) — Source for the staging logic behind $\delta$ and milestone gating.
- [Friction Efficiency Index](../../practice/02-internal-ops/05-diagnostics-friction-efficiency-index.md) — Retrospective execution metrics (FAR, BCV, RMS, SVI). Deliberately downstream of this file: those measures score how the motion was run rather than deriving from an axiom term.
