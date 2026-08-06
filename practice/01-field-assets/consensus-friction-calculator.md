# Consensus Friction Calculator

**Purpose:** To estimate how much organizational friction a buying committee will generate, and to decide whether the deal needs a stakeholder map, a joint steering committee, or executive sponsorship.

**Use when:** The Blueprint has identified the buying committee and you need to size $F_{consensus}$ before forecasting a close date.

**Operationalizes:** Axiom II's $F_{consensus}$ term. Theory in [03-mathematical-models.md](../../theory/01-foundation/03-mathematical-models.md) Section 3, research in [buying-center-dynamics.md](../../theory/02-research/buying-center-dynamics.md).

---

## The premise

A firm is not a single decision maker. It is a coalition whose members evaluate the same proposal against different objectives. Two things drive the cost of aligning them, and they compound rather than add:

- **Size.** Communication channels grow as $N(N-1)/2$, so the sixth stakeholder costs more than the second.
- **Goal conflict.** A large committee that agrees moves faster than a small one that does not.

---

## Inputs

### 1. Committee size ($N$)

Count every stakeholder holding veto power or direct evaluation responsibility, across executive, technical, legal, financial, and operational functions. Title does not matter. Veto power does.

Count the person who can stop the deal even if they never attend a meeting. Security architects and data protection officers are the ones most often missed.

### 2. Incentive variance (Var)

Score each stakeholder $i$ from $-1$ to $+1$ on how the initiative affects the objectives they are measured on:

- **+1** — advances their measured objectives directly
- **0** — no material effect
- **−1** — conflicts with their objectives or removes operational control

Then compute the variance across the committee:

$$\bar{I} = \frac{1}{N}\sum_{i=1}^{N} I_i \qquad \text{Var} = \frac{1}{N}\sum_{i=1}^{N}(I_i - \bar{I})^2$$

Variance is bounded on $[0, 1]$ because the scores are bounded on $[-1, 1]$. If you calculate a value above 1, you have made an arithmetic error.

When you lack the detail to score each person, use the rubric:

| Estimate | Condition |
|---|---|
| **0.0** | Every stakeholder benefits and knows it. |
| **0.25** | Minor divergence in priority. Security wants rigor, operations wants speed, nobody is threatened. |
| **0.50** | Two camps with genuinely opposed positions. At least one stakeholder loses something real. |
| **1.00** | Polarized. Some stakeholders gain substantially and others are actively harmed. |

### 3. Technical overlap ($TO$)

Architectural alignment among the technical evaluators, scored 1 to 5. This is tracked separately from incentive variance because technical philosophy conflicts persist even when incentives align. Two architects can both want the project to succeed and still deadlock on hosting model.

| Score | Condition |
|---|---|
| **1** | Unified standards and shared infrastructure principles. |
| **3** | Disagreement on integration patterns or hosting model. |
| **5** | Fractured philosophy. Cloud-native versus strict on-premise governance, or an unresolved build-versus-buy faction. |

---

## The calculation

$$F_{consensus} = \alpha \cdot N^{\beta} \cdot (1 + \text{Var}) \cdot (1 + \gamma \cdot TO)$$

With calibration defaults $\alpha = 1.0$, $\beta = 1.35$, $\gamma = 0.20$.

**Worked example.** A committee of 5, with two camps in genuine conflict (Var = 0.25) and disagreement on integration patterns (TO = 3):

$$F_{consensus} = 1.0 \times 5^{1.35} \times 1.25 \times 1.6 = 8.78 \times 1.25 \times 1.6 = 17.6$$

That lands in the medium band, which calls for a stakeholder alignment matrix and shared evaluation criteria before the deal is forecast.

> [!NOTE]
> These parameter values are reasoned defaults, not estimates fitted to booked deals. The output ranks deals against each other reliably. It does not predict a cycle length in weeks. See [03-mathematical-models.md](../../theory/01-foundation/03-mathematical-models.md) Section 6.

---

## Risk bands

| $F_{consensus}$ | Classification | What happens | Intervention |
|---|---|---|---|
| **Under 10** | Low | Linear decision path. Low stall risk. | Single-champion navigation. Standard approval workflow. |
| **10 to 25** | Medium | Delays from inter-departmental alignment cycles. The deal does not die, it drifts. | Deploy a stakeholder alignment matrix. Establish a joint steering committee and write down shared evaluation criteria before pricing. |
| **Above 25** | High | Evaluation deadlock or silent death. The most likely outcome is No Decision, not a competitive loss. | Executive sponsorship required. Run a joint Red Team workshop to force explicit trade-off resolution before the MIP is drafted. |

---

## Reading the output

**The single highest-leverage move is reducing variance, not reducing headcount.** The sensitivity of friction to variance scales with $N^{\beta}$:

$$\frac{\partial F_{consensus}}{\partial \text{Var}} = \alpha N^{\beta}$$

In a committee of three, aligning incentives produces a modest gain. In a committee of ten, it produces the largest single reduction available to the seller. This is the quantitative case for running the Red Team on large committees specifically.

**Do not respond to a high score by scheduling more meetings.** More meetings raise the coordination cost without touching the variance that generates it. The interventions that work force explicit trade-offs into the open, which is what the Red Team's prospective hindsight exercise does.

**A stakeholder scoring $-1$ is not irrational.** They are optimizing a scorecard the seller has not read. Name them in the Blueprint as the casualty, and build the containment plan. A committee where nobody scores below zero usually means the seller has not found the casualty yet, not that no casualty exists.

---

## Related

- [buying-center-dynamics.md](../../theory/02-research/buying-center-dynamics.md) — Cyert-March and Webster-Wind. Why the coalition behaves this way.
- [03-mathematical-models.md](../../theory/01-foundation/03-mathematical-models.md) — Derivation and sensitivity analysis.
- [Contextual Blueprint](./ilg-motion/01-discovery-contextual-blueprint.md) — Where the committee gets mapped.
- [Red Team Protocol](./ilg-motion/02-validation-red-team-protocol.md) — The variance-reduction instrument.
- [Bilateral Asymmetry Scorecard](../02-internal-ops/04-incentives-asymmetry-scorecard.md) — The companion measure for $\Delta_A$.
