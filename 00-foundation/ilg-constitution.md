# The Constitution of Implementation-Led Growth (ILG)

**Version:** 10.0  
**Purpose:** To define the economic and behavioral laws governing high-friction B2B sales.

> [!IMPORTANT]
> **The Offensive Paradigm:** In ILG, we treat the Buyer and Seller as a single **Offensive Unit**. The "Defense" is not the buyer; the Defense is the **Market Friction** (Transaction Costs, Asymmetry, and Inertia). To score (succeed), both parties must align on a single "Playbook" (The Blueprint).

---

## Part I: The Economics of Implementation-Led Growth

### The Core Claim

> In high-specificity deals, reducing friction creates more surplus than increasing value.
> But friction is amplified by information gaps, and value erodes with time —
> so the goal is to close the asymmetry gap faster than urgency decays.

This part introduces four interlocking concepts that explain *why* ILG works. They are designed to be taught in sequence: each concept adds a complication that the previous one can't explain on its own.

---

### Concept 1: The Surplus Equation

A deal closes when the buyer perceives enough surplus to justify the cost of change.

$$S = (V_{solution} - V_{next\_best}) - F_{total}$$

Where:

| Symbol | Definition | Plain English |
|--------|-----------|---------------|
| $S$ | **Deal Surplus** | The "room" that makes a deal possible. If S ≤ 0, no deal. |
| $V_{solution}$ | **Value of Proposed Solution** | What your solution delivers in the buyer's context. |
| $V_{next\_best}$ | **Value of Next-Best Alternative** | Could be a competitor, doing nothing, or building in-house. This is the buyer's real comparison — not your list of features. |
| $F_{total}$ | **Total Friction** | Everything that makes change expensive, risky, or painful (search costs, consensus costs, implementation costs, switching costs). |

**What this teaches:**

The old equation framed ILG as "risk minimization, not value maximization." That was directionally right but imprecise. The revised framing: **you don't need to increase V — you need to increase S.** And in high-friction deals, the fastest path to surplus is reducing F, not inflating V. This is counterintuitive to most sellers, who instinctively lead with value narratives.

**Why V_next_best matters:**

The original equation used $V_{status\_quo}$ (value of doing nothing). But buyers rarely frame their decision as "your solution vs. nothing." They're weighing your solution against the full set of alternatives — building in-house, extending a workaround, allocating the budget to a different problem entirely, or staying out of the market. And critically, in high-specificity deals, the most common alternative after a failed implementation isn't "try another vendor" — it's *market withdrawal*. The buyer retreats from the category entirely.

By naming $V_{next\_best}$ explicitly, you force the seller to understand the buyer's real decision frame: not "us vs. a competitor," but "us vs. the cost of staying out of the market or solving this problem themselves."

> **Teaching moment:** "Your value doesn't exist in a vacuum. It exists relative to what else the buyer could do with the same budget, time, and political capital. And in most Bridge deals, the real alternative isn't another vendor — it's giving up on solving the problem at all."

---

### Concept 2: The Fear Multiplier (Bilateral Asymmetry)

Friction isn't just process cost — it's amplified by what each side doesn't know about the other.

$$F_{effective} = F_{base} \times (1 + \Delta_{A})$$

Where:

| Symbol | Definition | Plain English |
|--------|-----------|---------------|
| $F_{base}$ | **Base Friction** | The "real" cost of change if both sides had perfect information: labor, time, resources, process change. |
| $\Delta_{A}$ | **Asymmetry Gap** | The distance between what the seller understands about the buyer's world and what the buyer understands about the seller's solution. Ranges from 0 (perfect mutual understanding) to 1 (total mutual ignorance). |
| $F_{effective}$ | **Effective Friction** | What the buyer *actually experiences*. Always ≥ base friction. |

**The bilateral shift:**

The v9 equation used $|I_A|$ — a single information asymmetry score. But asymmetry is never one-sided. There are two distinct gaps:

- **Seller Ignorance** ($I_{seller}$): How little the seller understands the buyer's workflows, political landscape, technical constraints, and implementation reality.
- **Buyer Uncertainty** ($I_{buyer}$): How little the buyer understands what the seller's solution actually requires, how it integrates, what changes it demands, and whether the seller can deliver.

$$\Delta_{A} = f(I_{seller}, I_{buyer})$$

These two gaps create *different* problems. Seller ignorance leads to bad scoping, misaligned demos, and proposals that miss the mark. Buyer uncertainty leads to fear, delay, committee expansion, and the "Safe No." You can't solve both with the same tactic — costly signals (workshops, audits) reduce buyer uncertainty, while discovery artifacts (Blueprint, workflow mapping) reduce seller ignorance.

> **Teaching moment:** "A deal stalls for one of two reasons: you don't understand their world well enough to be credible, or they don't understand your solution well enough to feel safe. Figure out which gap is wider and close that one first."

**Connection to Prospect Theory:**

Loss aversion ($\lambda \approx 2.25$ per Kahneman & Tversky, 1979) means that uncertainty about *losses* weighs roughly twice as heavily as equivalent uncertainty about *gains*. This is why $\Delta_A$ is a multiplier on friction rather than a subtractor from value: asymmetry doesn't reduce the upside — it inflates the perceived downside. The buyer doesn't think "this might be worth less than they claim." They think "this might cost more, take longer, and blow up in my face."

**Important boundary:** The $\lambda \approx 2.25$ finding comes from individual decision-making experiments with monetary gambles. Organizational buying decisions involve committees, longer time horizons, and career risk — which likely *amplifies* loss aversion beyond 2.25. We cite the number as a conceptual anchor, not a precise organizational coefficient. The directional claim (losses loom larger than gains) is what matters for ILG strategy.

---

### Concept 3: The Decay Clock

Value is not static. The urgency that created the buying window erodes over time.

$$V_{effective}(t) = V_{solution} \times e^{-\delta t}$$

Where:

| Symbol | Definition | Plain English |
|--------|-----------|---------------|
| $V_{effective}(t)$ | **Effective Value at time t** | What the solution is actually worth to the buyer as time passes since the triggering event. |
| $\delta$ | **Decay Rate** | How quickly the urgency fades. High δ = fast decay (regulatory deadline passed, champion left, budget cycle ended). Low δ = slow decay (structural problem that gets worse over time). |
| $t$ | **Time** | Elapsed time since the economic event that opened the buying window. |

**What this teaches:**

Most sales methodologies treat value as a fixed number you "discover" and then "present." ILG recognizes that value is *perishable*. The economic event that created the buying window (a failed audit, a regulatory deadline, a lost customer, a board mandate) has a half-life. Every week of delay means:

1. The triggering pain fades from organizational memory
2. Workarounds calcify into "good enough" solutions
3. Budget gets reallocated to newer fires
4. Champions lose political momentum or leave

This creates an asymmetric race: **you must close the asymmetry gap ($\Delta_A \to 0$) faster than the value decays ($V \times e^{-\delta t} \to 0$).** This is the fundamental time pressure in ILG.

> **Teaching moment:** "You're not racing the competition. You're racing the clock. The longer you take to make the buyer feel safe, the less the deal is worth — not because your product changed, but because their urgency did."

**Event reset:** The model assumes monotonic decay from a single triggering event, which is the most common pattern. But new economic events — a second failed audit, a competitor going live, a new CIO with a mandate — can reset $t = 0$. When a stalled deal gets a fresh trigger, the clock restarts. This is often the best moment to re-engage, because the buyer's pain is renewed but your prior discovery work ($I_{seller}$ reduction) is still intact. Teach reps to watch for reset events, not just decay.

**The Chaos Trap interaction:**

When $\delta$ is high AND the buyer doesn't have a defined SOP (the Chaos Trap from Part IV), you face the worst-case scenario: urgent need but no foundation to build on. The temptation is to rush — skip the Blueprint, compress the Red Team, jump to the MIP. But that increases $\Delta_A$ (both sides understand less), which inflates $F_{effective}$, which can push $S$ negative even when $V$ is high. The Chaos Trap pre-qualification gate exists precisely to prevent this failure mode.

---

### Concept 4: The Boundary Condition (Where ILG Applies)

ILG is not a universal sales methodology. It works in thin markets with high asset specificity.

**The boundary condition:**

$$ILG\ applies\ when: \quad k > k_{threshold} \quad \land \quad n_{viable} \leq n_{max}$$

Where:

| Symbol | Definition | Plain English |
|--------|-----------|---------------|
| $k$ | **Asset Specificity** | How customized, integrated, and context-dependent the solution is. Scored via the Diagnostic Rubric (Part IV): scores 10-20 indicate high specificity. |
| $k_{threshold}$ | **Specificity Threshold** | The minimum asset specificity where ILG creates more surplus than SLG or PLG. Below this, the overhead of Blueprints and Red Teams destroys more value than it creates. Roughly corresponds to a Diagnostic Rubric score of 10. |
| $n_{viable}$ | **Viable Vendor Count** | How many vendors can realistically serve this buyer's specific need. |
| $n_{max}$ | **Market Thickness Ceiling** | The maximum number of viable vendors where ILG still provides differentiation. In a thick market with many substitutes, ILG's investment premium gets competed away. |

**What this teaches:**

ILG is expensive. Blueprints take time. Red Teams take expertise. MIPs require bilateral commitment. This investment only pays off when:

1. **The deal is specific enough** that generic sales motions fail (the buyer needs to *see themselves* in your solution before they'll commit).
2. **The market is thin enough** that the buyer can't easily find 10 vendors who all do implementation planning. If they can, your Blueprint becomes table stakes, not a differentiator.

In thick markets with low specificity — commodity SaaS, self-serve products, standardized integrations — PLG or SLG will outperform ILG because the surplus comes from speed and price, not from friction reduction.

> **Teaching moment:** "Before you invest in ILG for a deal, ask two questions: Is this solution specific enough that a generic pitch will fail? And are there few enough vendors that our investment in understanding their world won't be matched by five competitors next week?"

**Boundary drift:** Both $k$ and $n_{viable}$ change over time. Markets that were thin become thick as standards mature and SaaS vendors enter to universalize workflows that previously required custom builds. This is especially visible in healthcare interoperability — TEFCA, FHIR, and 21st Century Cures are actively commoditizing integrations that used to demand deep custom work. The question isn't just "is $k$ high enough today?" but "is $k$ likely to stay high through the contract term?"

This connects directly to **Retention Horizon** (the 4th scoring factor in the Diagnostic Rubric). If the problem is likely to be commoditized within the retention period — because a standard is maturing, an API is opening, or a SaaS vendor is universalizing part of the workflow — then ILG's upfront investment may not pay back before the deal becomes a Toaster. Reps should assess trajectory, not just current state, when qualifying deals at the boundary.

---

### Putting It All Together

The complete ILG teaching model in one frame:

$$S = \left(V_{solution} \times e^{-\delta t} - V_{next\_best}\right) - F_{base} \times (1 + \Delta_A)$$

$$\text{subject to:} \quad k > k_{threshold} \quad \land \quad n_{viable} \leq n_{max}$$

**Read it as a story:**

*A deal has surplus (S > 0) when the decaying value of your solution, compared to the buyer's next-best alternative, exceeds the base friction of change — amplified by how much each side doesn't understand about the other. But this only works in markets where the solution is specific enough and the vendor pool is thin enough that your investment in friction reduction actually differentiates you.*

**The ILG seller's job, in four moves:**

1. **Qualify the boundary** (Part IV Triage): Is this a Bridge deal in a thin market? If not, route to PLG/SLG.
2. **Map the friction** (Blueprint): Understand $F_{base}$ and both sides of $\Delta_A$ before proposing anything.
3. **Close the gap** (Red Team): Deploy costly signals to drive $\Delta_A \to 0$ before $V$ decays.
4. **Lock the surplus** (MIP): Contractualize bilateral commitments while $S > 0$.

---

### Relationship to the Three Axioms

Each axiom from Part II maps to a specific concept:

| Axiom | Concept | Connection |
|-------|---------|------------|
| **I: Law of Economic Boundaries** | Concept 4 (Boundary Condition) | Asset specificity ($k$) determines whether ILG applies at all. |
| **II: Law of Asymmetry Convergence** | Concepts 2 + 3 (Fear Multiplier + Decay Clock) | Information asymmetry amplifies friction, and you must close the gap before value decays. |
| **III: Law of Bilateral Governance** | Concept 1 (Surplus) | Mutual skin in the game preserves surplus through the repeated game (SaaS renewals). |

---

### What This Model Does NOT Claim

1. **It does not predict close probability.** This is a teaching model, not a forecasting tool. It explains *why* deals stall and *where* to intervene.
2. **It does not assign precise numerical values.** $\delta$, $\Delta_A$, and $F_{base}$ are conceptual — they orient the seller's thinking, not their spreadsheet.
3. **It does not account for irrational actors.** If a buyer makes decisions based on personal relationships, politics, or spite rather than economic logic, the model explains less. (Though $\Delta_A$ captures some of this — irrational-seeming behavior often stems from information the seller doesn't have.)
4. **It does not replace the Diagnostic Rubric.** The rubric (Part IV) is the *operational* scoring tool. This equation is the *conceptual* foundation that explains why the rubric works.

### 4. Market Evolution Model (Layer 2) & The Potential Well Curve

| Phase | Era | Dominant Cost | Buyer's Question | GTM Motion | Viable Channels | Jevons Risk |
|:---|:---|:---|:---|:---|:---|:---|
| **Nascent** | New category | Search & Discovery | "What solutions exist?" | SLG | High-touch, consultative, relationship-based | **Low** — binding constraint is knowledge of the problem |
| **Efficient** | Defined category | Evaluation | "Does this actually work?" | PLG | Product-led trials, content marketing, outbound email | **High** — binding constraint is production cost |
| **Saturated** | Mature category | Consensus + Implementation | "Can we make this work *here*?" | ILG | Implementation proof, costly signals, earned credibility | **Low** — binding constraint is experience and track record |

**What this teaches:**

The channels collapsing under Jevons' Paradox are **Stage 2 channels** — optimized for evaluation-stage friction (awareness, comparison, feature assessment). Many B2B markets have already moved to Stage 3, where the dominant friction is consensus and implementation. The sales enablement stack is still optimized for a friction profile that no longer matches the buyer's actual decision-making process.

This explains why the collapse feels so acute: Jevons is degrading a channel that was already becoming structurally irrelevant to the buyer's primary concern. The mismatch between tool optimization (Stage 2) and market reality (Stage 3) amplifies the collapse.

> **Teaching moment:** "If your market is Stage 3 and your primary outreach channel is Jevons-vulnerable, you're fighting two problems at once: the channel is congested AND the channel doesn't address the buyer's actual friction. The ILG seller's advantage is that the channels which demonstrate implementation credibility — case studies, named references, co-developed workflow documentation, published technical depth — are inherently Jevons-resistant because their binding constraint is having done the work."

### 5. Concept 5 — Channel Health ($r(V)$): The Floor Beneath $F_{base}$

The preceding four concepts treat $F_{base}$ as a property of the deal — determined by implementation complexity, consensus costs, and switching costs. This is incomplete. In practice, $F_{base}$ has a **channel-level component** that is determined by the health of the communication channel through which the seller initiates contact.

$$F_{base} = f(r(V), k, m)$$

Where:
- $r(V)$ = the signal effectiveness of the channel, a decreasing function of aggregate sender volume $V$
- $k$ = asset specificity of the deal (from the existing Diagnostic Rubric)
- $m$ = market maturity stage (Nascent, Efficient, or Saturated)

As aggregate sender volume in a channel increases, the channel's signal-to-noise ratio degrades — and $F_{base}$ rises for **every** seller, including those producing high-quality, well-targeted outreach. This is a negative externality: each sender's volume imposes costs on all other senders, but no individual sender internalizes those costs.

The three-level friction model:

| Level | Equation | What It Captures | ILG Intervention |
|:---|:---|:---|:---|
| **Deal Level** | $F_{effective} = F_{base} \times (1 + \Delta_A)$ | Bilateral information asymmetry amplifies perceived friction | Blueprints, Red Teams, MIPs reduce $\Delta_A$ |
| **Channel Level** | $F_{base} = f(r(V))$ | Aggregate sender volume degrades channel effectiveness | Channel selection, costly signal channels, mechanism design |
| **Market Level** | Channel vulnerability varies by maturity stage | Stage 2 channels are Jevons-vulnerable; Stage 3 channels are resistant | Match channel to market maturity, not to production efficiency |

**What this teaches:**

Individual deal-level optimization ($\Delta_A \to 0$) has a ceiling imposed by channel-level degradation. A seller who executes a perfect Blueprint, runs an excellent Red Team, and produces a rigorous MIP can still face elevated $F_{base}$ because the channel itself is congested. "Just do better outbound" is insufficient when $F_{base}(r(V))$ is rising due to aggregate volume the individual seller cannot control.

This explains why identical ILG-quality outreach produces different results across time — the deal-level physics haven't changed, but the channel-level physics have.

> **Teaching moment:** "Before you invest in optimizing your message ($\Delta_A$), check whether the channel itself still functions ($r(V) \geq r_{\min}$). If the channel has collapsed, no amount of message quality will overcome the base friction floor."

---

## Part II: The Three Axioms (The System Core)

### Axiom I: The Law of Economic Boundaries (The Why)
This axiom establishes the specific sales motion required based on the **Asset Specificity** of the transaction.

*   **The Mechanism:** Grounded in Coase’s "Make vs. Buy" boundary, a firm will only purchase from a market if the **total transaction costs** (search, bargaining, and enforcement) are lower than the cost of internal production.
*   **The Trigger:** When a solution has **High Asset Specificity**—meaning it is deeply entangled with a buyer's unique data, workflows, and human training—it becomes "The Bridge". 
*   **The Mandate:** In these high-specificity deals, the price mechanism alone fails because the risk of "lock-in" is too high. To keep "buying" more efficient than "making," the vendor must provide a **"Blueprint"** (Governance Structure) to lower these transaction costs. 
*   **Operating Instruction:** **"Never apply a Bridge motion to a Toaster, and never sell a Bridge without a Blueprint"**.

**Evidence:** Coase's Theorem (1937); Transaction Cost Economics (Williamson, 1981).

### The Channel Viability Corollary

Axiom I establishes that high-specificity deals require governance structures (Blueprints) because the price mechanism alone fails when lock-in risk is too high. The same principle applies one level up: **the communication channel through which deals are initiated also requires governance when the channel's quality mechanism has failed.**

> **Channel Corollary to Axiom I:** A channel that eliminates production cost for the sender without imposing a corresponding quality constraint will be flooded by low-quality actors until the channel's signal-to-noise ratio collapses. Friction at the channel level is what separates signal from noise. Remove it, and the channel reaches a Babbling Equilibrium (Crawford & Sobel, 1982) — a state where rational receivers ignore all messages because the cost of distinguishing quality from noise exceeds the expected value of engaging.

**The Mechanism (Jevons' Paradox):** When tools reduce the cost of producing outreach, total volume increases rather than decreasing — because the demand for "sending messages to buyers" is price-elastic. The efficiency gain is reinvested in volume, not quality. This depletes the shared resource (buyer attention) faster than the efficiency gain saves it.

**The Precondition:** Jevons' Paradox applies only when production cost is the **binding constraint** on sending volume. Channels where other constraints bind first — time, relationships, demonstrated expertise, physical presence — are resistant to this degradation. This is why costly signals work: their binding constraint is having done the work, which cannot be made cheaper through tooling.

**Operating Instruction:** Before selecting a channel, assess whether the binding constraint on volume in that channel is production cost (Jevons-vulnerable) or something else (Jevons-resistant). If you are using a Jevons-vulnerable channel for a Stage 3 buyer (implementation-dominated market), you have a structural mismatch — the channel is optimized for a friction profile that doesn't match your buyer's actual decision-making process.

**Evidence:** Jevons (1865), *The Coal Question*; Pigou (1920), *The Economics of Welfare*; Hardin (1968), "The Tragedy of the Commons"; Ostrom (1990), *Governing the Commons*.

### The Non-Debaseable Currency Principle

The Channel Viability Corollary implies a design principle for channel selection:

> **Non-Debaseable Currencies:** Effective B2B communication channels must be denominated in currencies that cannot be debased through efficiency gains. A currency is non-debaseable when its binding constraint is something other than production cost — time, relationships, demonstrated expertise, implementation depth, social capital. These currencies satisfy the Single Crossing Property: the cost of producing the signal is proportionally lower for high-quality sellers, and no tool can change this ratio by making production cheaper for everyone.

| Currency Type | Binding Constraint | Debaseable? | Example |
|:---|:---|:---|:---|
| AI-personalized email | Production cost | Yes — tools reduce cost to near-zero | Clay-generated outreach |
| Referral introduction | Social capital | No — spending a relationship is inherently costly | Warm intro from a shared connection |
| Published thought leadership | Knowledge and effort | No — genuine expertise can't be manufactured at scale | Original research, framework development |
| Implementation case study | Having done the work | No — you can't fake a named customer and verified outcomes | Per-EHR integration documentation |
| In-person relationship | Time and physical presence | No — attendance is constrained regardless of cost | Face-to-face meeting, site visit |

**Connection to Costly Signals:** A non-debaseable currency is a costly signal whose cost structure survives Jevons' Paradox. The cost of producing the signal cannot be automated to zero, which means it retains its ability to separate high-quality sellers from low-quality sellers regardless of what tools exist.

**Connection to the Hostage Model:** Williamson's hostage (credible commitment) functions as a non-debaseable currency — something genuinely valuable that the seller puts at risk. Channel access gated by seller hostages (forfeited if promises aren't kept) creates a non-debaseable access currency because the cost of maintaining access is proportional to the quality of the seller's delivery.

**The Demurrage Extension:** Non-debaseable currencies resist Jevons' Paradox (they can't be cheapened into meaninglessness), but they are still vulnerable to hoarding — incumbents accumulating trust and then coasting on historical reputation without continuously re-earning it. A complete channel design applies demurrage to seller credibility: trust depreciates over time unless refreshed with current evidence of delivery quality. This ensures that access to the buyer's consideration set rewards current performance, not historical accumulation. The carrying cost of trust functions as a competitive equalizer — incumbents must continuously prove they are still the vendor their reputation claims, and new entrants with strong current evidence can compete against decaying historical credibility rather than an immovable installed base.

### Axiom II: The Law of Asymmetry Convergence (The Certainty)
This axiom explains why you must drive the **Bilateral Asymmetry Gap ($\Delta_A$)** toward zero to overcome the buyer's rational paralysis — and why that requires diagnosing *which side* of the gap is wider.

*   **The Physics:** The **$\Delta_A$ Multiplier** (see Part I, Concept 2) acts as a force multiplier on all friction. $F_{effective} = F_{base} \times (1 + \Delta_A)$. If asymmetry is high on *either* side, effective friction explodes.
*   **The Two Gaps:** Asymmetry is bilateral. **Seller Ignorance** ($I_{seller}$) — how little the seller understands the buyer's workflows, politics, and constraints — leads to bad scoping and lost credibility. **Buyer Uncertainty** ($I_{buyer}$) — how little the buyer understands the seller's solution, integration requirements, and delivery capability — leads to fear, delay, and the "Safe No."
*   **The Psychology:** Because of **Loss Aversion ($\lambda \approx 2.25$)**, the buyer's brain weights the personal risk of failure roughly twice as heavily as the business gain of success. This leads to **Omission Bias**, where the "Safe No" (inaction) feels safer than a risky "Yes." Asymmetry inflates the *perceived downside*, not the upside — which is why $\Delta_A$ multiplies friction rather than subtracting from value.
*   **The Strategy:** Drive $\Delta_A \to 0$ by closing whichever gap is wider first. To reduce **Seller Ignorance**, deploy discovery artifacts (Blueprint, workflow mapping). To reduce **Buyer Uncertainty**, deploy **"Costly Signals"** (workshops, technical audits, paid pilots) that reject **"Cheap Talk"** (marketing claims).
*   **The Outcome:** These interventions provide the individual decision-maker with an **"Alibi of Rigor"** — the evidence of due diligence required to protect their career if the project fails. Critically, seller-side discovery (reducing $I_{seller}$) also enables *better* costly signals, because you can only demonstrate credible understanding if you've done the homework first.

**Evidence:** Signaling Theory (Spence, 1973); Prospect Theory (Kahneman & Tversky, 1979); The JOLT Effect (Dixon & McKenna, 2022).

### Axiom III: The Law of Bilateral Governance (The Playbook)
This axiom ensures that both parties stay aligned as a single **Offensive Unit** through the **"Fundamental Transformation"** into a long-term **Repeated Game**.

*   **The Mechanism:** Once high-specificity investments are made, the relationship shifts from a competitive market to a **Bilateral Monopoly**. Both parties are locked in, creating the **"Holdup Problem"** where one side can exploit the other's sunk costs.
*   **The Alignment:** To ensure a stable equilibrium (NRR), you must contractualize **"Mutual Skin in the Game"**.
*   **The Tactics:** 
    *   **Bilateral Hostages:** Use a **Mutual Implementation Plan (MIP)**—the "Offensive Playbook"—where the buyer commits their best resources and budget as a credible commitment.
    *   **Vested Commissions:** Align the sales agent with the "Shadow of the Future" by splitting commissions between the signature ($T_0$), the successful "Go-Live" ($T_3$), and the first renewal ($T_{12}$).

**Evidence:** Agency Theory (Jensen & Meckling, 1976); Game Theory (The Prisoner's Dilemma).

---

## Part III: The Organizational Corollary

The teaching model (Part I) introduces five key variables: $V_{next\_best}$, $F_{base}$, $\Delta_A$ (composed of $I_{seller}$ and $I_{buyer}$), $\delta$ (decay rate), and the boundary condition ($k$, $n_{viable}$). Each creates an organizational responsibility that maps to specific departments.

### The Mapping of Variables to Departments

**1. $F_{base}$ — Base Friction (The Original Cost Mapping)**

The legacy mapping still holds for the deterministic cost components:

*   **Marketing** minimizes **Search Costs** (Opening the Running Lanes) — ensuring qualified prospects find you.
*   **Sales** minimizes **Consensus Costs** (Clearing the Defensive Line) — navigating stakeholders, procurement, and committee dynamics.
*   **Customer Success** minimizes **Enforcement Costs** (Protecting the Pocket/Ensuring Yardage) — ensuring the promised value is delivered and sustained.

**2. $V_{next\_best}$ — Decision Alternatives (Build vs. Buy vs. Do Nothing)**

In high-specificity deals, the buyer's real alternative is rarely another vendor. It's building in-house, extending a workaround, reallocating budget to a different problem, or withdrawing from the market entirely. After a failed implementation, buyers don't try vendor #2 — they retreat from the category.

*   **Primary Owner: Sales** — must map the buyer's actual decision set during Blueprint discovery. What else could they do with this budget, time, and political capital? What's the cost of staying out of the market?
*   **Supporting: Product Marketing** — arms sellers with "build vs. buy" framing and market withdrawal cost narratives.
*   **Supporting: Product** — ensures the roadmap reduces the friction of choosing "buy" over "build" (APIs, interoperability, migration tooling).
*   **Operational Rule:** If the seller cannot articulate the buyer's $V_{next\_best}$ by the end of the Blueprint phase, the deal is underqualified. The Blueprint must include a "decision alternatives" section that maps the buyer's real options — not just other vendors.

**3. $\delta$ — Decay Rate (Urgency Monitoring)**

*   **Primary Owner: Sales** — monitors the triggering event's half-life and escalates when urgency is eroding faster than the sales cycle is progressing.
*   **Supporting: RevOps** — tracks deal velocity metrics that serve as proxy indicators for decay (stage duration, engagement frequency, response latency).
*   **Operational Rule:** If a deal's stage duration exceeds the historical median by >50%, treat it as a decay signal. Either re-qualify the triggering event or identify whether a new event has reset the clock.

**4. $\Delta_A$ — Bilateral Asymmetry Gap**

This is the most organizationally complex variable because each side of the gap is owned by different teams:

*   **Seller Ignorance ($I_{seller}$) — Sales + Solutions Engineering.** Reduced through discovery: the Blueprint, workflow mapping, technical architecture reviews. The seller must understand the buyer's world deeply enough to scope credibly. This is a Sales/SE joint responsibility.
*   **Buyer Uncertainty ($I_{buyer}$) — Marketing + Sales jointly.** Marketing reduces category-level uncertainty (thought leadership, case studies, educational content). Sales reduces deal-level uncertainty through costly signals (workshops, audits, paid pilots) that demonstrate specific competence.
*   **Operational Rule:** At the end of each deal stage, diagnose which gap is wider. If $I_{seller}$ is the bottleneck, invest in more discovery before deploying costly signals — otherwise your signals miss the mark. If $I_{buyer}$ is the bottleneck, accelerate costly signal deployment.

**5. Boundary Condition ($k$, $n_{viable}$) — Deal Qualification and Capacity**

*   **Primary Owner: Sales Leadership** — enforces the Triage Protocol (Part IV) to ensure ILG resources are only deployed on deals that clear the boundary condition.
*   **Supporting: Strategy/Market Intelligence** — monitors market thickness trends ($n_{viable}$) to detect when a segment is thinning or thickening over time.
*   **Operational Rule:** The Diagnostic Rubric is non-optional. No Blueprint authorization without a completed rubric score ≥ 10.

**The Capacity Constraint:** ILG requires costly signals — Blueprints, Red Teams, paid diagnostics — to prove the seller is not a lemon. These signals are expensive precisely because they *must* be expensive to be credible (see Axiom II). But this means the team can only run a limited number of concurrent ILG pursuits at quality. If demand exceeds capacity, signal quality degrades on *every* deal, which is worse than prioritizing fewer deals and executing them well.

*   **Operational Rule:** Sales Leadership must enforce a capacity ceiling on active ILG pursuits. When qualified deals exceed the team's ability to deliver quality Blueprints and Red Teams, apply a second triage: prioritize deals with the highest surplus ($S$) and the strongest triggering events (lowest $\delta$). Deals that don't make the cut should be held, not abandoned — they can re-enter the pipeline when capacity opens or a new event resets the Decay Clock.
*   **The triage protocol does double duty:** It qualifies whether a deal is ILG-appropriate *and* protects the team's capacity to deliver credible costly signals. An overloaded team that runs mediocre Blueprints on 12 deals will lose more than a focused team that runs excellent Blueprints on 5.

### The Handoff Rule (Updated)

Revenue friction occurs at the "Handoff Points." RevOps must ensure the Blueprint — including both sides of the $\Delta_A$ assessment — travels from Sales to CS to prevent the asymmetry gap from resetting. A "Fumbled Handoff" doesn't just lose context; it resets $I_{seller}$ to near-maximum, because the CS team inherits a customer they don't yet understand. The Blueprint is the institutional memory that prevents this.

---

## Part IV: The Strategy & Triage Protocol

### Pre-Qualification Gate: Workflow Maturity

Before scoring, answer one binary question: **Does a documented standard operating procedure (SOP) exist for this problem today?**

*   **YES** → Proceed to the Diagnostic Rubric.
*   **NO** → **STOP.** This is the **Chaos Trap** (High Specificity + Undefined Workflow). You cannot digitize chaos. Redirect to **Consulting/Paid Workshop** to define the SOP first. The prospect must graduate from Consulting → ILG.

**Rationale:** Selling software to automate an undefined workflow creates churn. The Chaos Trap is not a Bridge deal with extra friction; it is a fundamentally different situation that requires process definition before technology selection.

### The Diagnostic Rubric (Score 1-5 per factor)

| Factor | Score 1 (Low) | Score 3 (Medium) | Score 5 (High) |
|--------|---------------|-------------------|-----------------|
| **1. Tech Specificity** — How hard is it to rip out? | Standalone tool, no integration | Standard API integration | Deep ERP/core infrastructure, custom code |
| **2. Org Specificity** — How many habits must change? | Single team (<5 users) | Single department, minor process change | Cross-functional, total workflow overhaul |
| **3. Political Complexity** — How many stakeholders can say no? | Single decision maker | Committee (3-4 stakeholders) | Board/Procurement/Security audit required |
| **4. Retention Horizon** — One-shot or repeat game? | One-time project, no renewal | Annual contract, moderate switching cost | Multi-year platform, deep dependency |

**Total Score Range:** 4-20

### Channel Triage

Before selecting an outreach channel, assess three factors:

**1. Is production cost the binding constraint on volume in this channel?**

If yes → the channel is Jevons-vulnerable. Efficiency tools will increase total volume faster than they improve individual quality, degrading the channel for everyone.

If no (time, relationships, expertise, or physical presence bind first) → the channel is Jevons-resistant. Making it cheaper doesn't increase volume because something else limits throughput.

**2. What market maturity stage is the buyer in?**

If Stage 2 (evaluation-dominated) → volume-oriented channels may still have residual utility, but monitor for degradation.

If Stage 3 (implementation-dominated) → evaluation-stage channels are structurally mismatched to the buyer's primary concern, regardless of congestion level. Prioritize channels that demonstrate implementation credibility.

**3. What is the current channel state?**

- **Healthy** ($\lambda = 0$): Channel functions normally. Individual message quality is the primary differentiator.
- **Binding** ($\lambda > 0$): Channel is near its viability threshold. Even well-crafted outreach faces declining returns. Message quality helps but cannot fully compensate for channel degradation.
- **Collapsed** (infeasible): Channel's transaction costs exceed its utility. No volume of sending produces positive ROI. Exit the channel and reallocate to Jevons-resistant alternatives.

**The Channel Mismatch Warning:**

Using a Jevons-vulnerable, Stage 2 channel for a Stage 3 buyer means the seller is fighting both channel-level congestion ($F_{base} \uparrow$) and structural irrelevance (the channel doesn't address the buyer's actual friction). This is the worst-case configuration and the most common one in B2B sales today.

**Operating Instruction:** Match the channel to the buyer's friction profile, not to the seller's production efficiency. The cheapest channel to operate is rarely the most effective channel for the buyer's decision-making stage.

### The Decision Matrix

*   **Lane 1 (The Toaster):** Score 4-9.
    *   **Strategy:** SLG/PLG (Velocity).
*   **Lane 2 (The Bridge):** Score 10-20.
    *   **Strategy:** ILG (Safety).
    *   **Gate:** If Blueprint requires >10 hours SE time, utilize **Paid Diagnostic** to validate intent.

**Override Rule:** If the prospect asks for a "Pilot" or "Proof of Concept," immediately upgrade the score to 20 (Bridge). Pilots are strictly governed by the Red Team Protocol.

---

## Part V: The Artifacts (The Toolset)

> Before deploying any artifact, the seller must first qualify the deal through the **Triage Protocol (Part IV)** to confirm ILG applicability. The Diagnostic Rubric score must be ≥ 10 (Bridge lane) and the Workflow Maturity Gate must be passed. Only then does the artifact sequence begin.

### 1. The Contextual Blueprint (The Filter)

- **Function:** Maps $F_{base}$ and reduces **Seller Ignorance** ($I_{seller}$). The Blueprint is the primary discovery artifact — it forces the seller to understand the buyer's workflows, political landscape, and technical constraints before proposing anything.
- **Components:**
  * **Political Capital Map:** Who *loses* power if we succeed?
  * **Decision Alternatives:** What is the buyer's $V_{next\_best}$? Build in-house, extend a workaround, reallocate the budget, or withdraw from the market? What's the cost of each?
  * **Bilateral Scorecard:** Internal Seller Check (Am I blind to the Saboteur? Is the Buyer hallucinating features?).
- **Tactic:** The **Reciprocity Gate** — the buyer's willingness to invest time in the Blueprint is itself a qualification signal.

### 2. The Red Team Workshop (The Validator)

- **Function:** Reduces **Buyer Uncertainty** ($I_{buyer}$) through costly signals. The Red Team is the primary mechanism for demonstrating credible understanding — you can only stress-test what you've first discovered in the Blueprint.
- **Mechanism:** Uses **Prospective Hindsight** (Inverted RE-AIM).
- **Tactic:** Frame as "Champion Protection." Differentiate Rational Skeptics (Co-opt) from Political Adversaries (Contain). The Red Team provides the decision-maker's **"Alibi of Rigor."**

### 3. The Mutual Implementation Plan (The Close)

- **Function:** Locks surplus ($S > 0$) through bilateral governance and incentive alignment before the Decay Clock ($V \times e^{-\delta t}$) erodes the buying window.
- **Mechanism:** Contractualizes "Skin in the Game" — mutual commitments that make it costly for either side to defect.
- **Tactic:** Use **RE-AIM** metrics translated into business KPIs. Use resources as "Tradeable Currency."
