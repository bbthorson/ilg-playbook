# Channel Externalities and the Economics of Channel Collapse: Jevons' Paradox, Congestion Theory, and the Viability Constraint on B2B Communication

## Executive Summary

This document extends the ILG framework to the **channel level** — analyzing how the aggregate behavior of all sellers in a communication channel degrades the channel's effectiveness for every individual seller. The existing ILG framework describes friction at the deal level ($F_{effective} = F_{base} \times (1 + \Delta_A)$). This document demonstrates that $F_{base}$ itself is not a constant — it is a function of channel health, which degrades as a negative externality of aggregate sender volume.

The central argument: **sales enablement tools that reduce the cost of outreach trigger Jevons' Paradox — efficiency gains increase total consumption of buyer attention rather than reducing it, degrading channel signal-to-noise ratios until the channel collapses.** This collapse is a well-studied class of economic problem (congestion externality) with direct parallels in environmental economics, antibiotic resistance, spectrum allocation, and traffic congestion. The formal structure involves constrained optimization under Karush-Kuhn-Tucker (KKT) conditions, where buyer attention is the scarce resource and channel viability is the binding constraint.

The document introduces a three-level friction model, a Jevons vulnerability diagnostic based on demand elasticity, a market maturity interaction that connects channel vulnerability to the existing potential well curve, and a taxonomy of corrective mechanisms drawn from Pigouvian economics, Ostrom's commons governance, and Hurwicz's mechanism design theory.

---

## 1. The Problem: Channels as Shared Resources

### 1.1 The Missing Level of Analysis

The ILG framework models friction at the **deal level**: how bilateral information asymmetry ($\Delta_A$) amplifies the base friction ($F_{base}$) of any given transaction. The framework prescribes interventions to reduce $\Delta_A$ — Blueprints to close seller ignorance, Costly Signals to close buyer uncertainty, and Mutual Implementation Plans to govern the bilateral dependency.

However, the framework has treated $F_{base}$ as an exogenous parameter — a property of the deal's complexity and the market's structure. This is incomplete. In practice, $F_{base}$ is substantially influenced by the **health of the communication channel** through which the seller initiates contact with the buyer. A cold email sent in 2015, when the channel was relatively uncongested, faced a lower $F_{base}$ than the identical email sent in 2026, when buyer attention in email has been severely depleted by aggregate volume. The deal-level physics haven't changed. The channel-level physics have.

This document formalizes the channel-level dynamics and integrates them with the existing deal-level model.

### 1.2 Buyer Attention as a Commons

Buyer attention within any communication channel — email inboxes, LinkedIn feeds, conference floors, webinar attendance — is a **common-pool resource**. It shares the two defining characteristics of a commons (Ostrom, 1990):

1. **Subtractability (rivalry):** Each message that occupies a buyer's attention subtracts from the attention available for other messages. A buyer who spends cognitive energy evaluating (and rejecting) a low-quality cold email has less attention for the next message, regardless of its quality.
2. **Non-excludability (in the current regime):** No mechanism prevents any seller from accessing the channel. The marginal cost of sending an email is near zero, and there is no quality gate, reputation requirement, or community-derived filter that restricts channel access based on seller quality.

This combination — rivalrous consumption with open access — is the textbook precondition for a Tragedy of the Commons (Hardin, 1968). Each sender consumes a small amount of the shared resource (buyer attention). The benefit accrues to the individual sender. The cost (degraded channel effectiveness) is distributed across all senders. The result is systematic overuse.

---

## 2. Jevons' Paradox: Why Efficiency Accelerates Collapse

### 2.1 The Classical Paradox

In 1865, British economist William Stanley Jevons observed that technological improvements in steam engine efficiency did not reduce Britain's coal consumption. Instead, consumption increased dramatically. More efficient engines made coal economically viable for a wider range of applications, and the resulting demand increase more than offset the per-unit savings. Jevons concluded: "It is wholly a confusion of ideas to suppose that the economical use of fuel is equivalent to a diminished consumption. The very contrary is the truth." (Jevons, 1865, *The Coal Question*)

Formally, Jevons' Paradox occurs when:

$$\frac{\partial D}{\partial p} \cdot \frac{\partial p}{\partial \eta} > \frac{\partial q}{\partial \eta}$$

Where $D$ is total demand, $p$ is effective price per unit of output, $\eta$ is efficiency, and $q$ is the quantity consumed per application. The left side captures the demand increase from lower effective price; the right side captures the per-unit savings from improved efficiency. The paradox holds when the demand effect dominates the efficiency effect.

### 2.2 Application to Sales Enablement

The direct mapping:

| Jevons (Coal) | Sales Enablement (Email) |
|:---|:---|
| **Resource:** Coal | **Resource:** Buyer attention |
| **Technology:** More efficient steam engines | **Technology:** Enrichment tools, AI personalization, sequencing platforms |
| **Efficiency gain:** Less coal per unit of work | **Efficiency gain:** Less time/cost per "personalized" email |
| **Effective price drop:** Coal becomes viable for more applications | **Effective price drop:** Outbound becomes viable for more sellers, more segments, more use cases |
| **Demand response:** Total coal consumption increases | **Demand response:** Total email volume increases (293B/day in 2019 → 376B/day in 2025, +28%) |
| **Resource outcome:** Coal reserves deplete faster | **Resource outcome:** Buyer attention depletes faster (reply rates: 8.5% in 2019 → 3.4% in 2026, -60%) |

The tools — Clay, Apollo, Instantly, Smartlead, and dozens of others — reduced the marginal cost of producing a "personalized" email from approximately 20 minutes of manual research to seconds of API calls at a cost of pennies. This efficiency gain did not cause senders to produce the same number of higher-quality emails. It caused an explosion in total volume, precisely as Jevons predicts.

### 2.3 The Elasticity Precondition

Jevons' Paradox does not apply universally. It requires that demand for the resource (or for the activity the resource enables) is **price-elastic** — that a reduction in effective price triggers a proportionally larger increase in quantity demanded.

For outbound email, elasticity is clearly high. The demand for "sending messages to potential buyers" is nearly unbounded for most sales organizations. There is always another prospect, another vertical, another persona. The only constraint was production cost. When tools reduced that cost to near zero, volume expanded dramatically because the **binding constraint** on the activity was removed.

This yields a critical diagnostic: **a channel's vulnerability to Jevons-driven collapse is determined by whether production cost is the binding constraint on sending volume.**

| Jevons Vulnerability | Binding Constraint | Examples |
|:---|:---|:---|
| **High** (elastic demand) | Production cost (time, research effort, per-unit expense) | Cold email, LinkedIn outreach, AI-generated content marketing |
| **Low** (inelastic demand) | Time and physical presence | In-person meetings, site visits, conferences (pre-COVID) |
| **Low** (inelastic demand) | Social capital | Referral introductions, warm introductions through network |
| **Low** (inelastic demand) | Demonstrated expertise | Published thought leadership, implementation case studies, speaking engagements |
| **Low** (inelastic demand) | Having done the work | Deep account-based research requiring human judgment, co-developed implementation plans |

**Channels where the binding constraint is something other than production cost are structurally resistant to Jevons' Paradox.** Making them cheaper doesn't increase volume because something else — time, relationships, expertise, experience — limits throughput regardless of cost.

This connects directly to the Costly Signals framework (see `01-research/costly-signals.md`). A signal functions as a separating mechanism only when its cost structure satisfies the Single Crossing Property — the cost of producing the signal is proportionally lower for high-quality sellers than for low-quality sellers. When production cost is the binding constraint and tools reduce it to near zero, the signal's cost structure collapses and it can no longer separate quality from noise. The channel has lost its information content.

### 2.4 The Constraint Shift Vulnerability

Even channels with non-cost binding constraints can become Jevons-vulnerable if the nature of the constraint changes. The most significant recent example: **conferences during COVID**.

Pre-COVID, conference attendance was constrained by time and travel — inherently inelastic. Virtual conferences removed those constraints, shifting the binding constraint to production cost (hosting a webinar is cheap). The channel immediately flooded with low-quality content, and engagement rates collapsed. The Jevons trigger was not "conferences got cheaper" but "the binding constraint shifted from time/travel to production cost, and production cost is elastic."

This implies that channel resistance to Jevons is not permanent. Any technological or structural change that shifts the binding constraint toward production cost opens the channel to Jevons-driven degradation.

---

## 3. The Formal Model: Constrained Optimization and KKT Conditions

### 3.1 The Individual Sender's Problem

Each sender $i$ in a channel maximizes their own pipeline generation:

$$\max_{v_i} \pi_i = R(v_i \cdot r(V)) - C(v_i)$$

Where:
- $v_i$ = individual sender's volume (messages sent)
- $V = \sum_{i=1}^{N} v_i$ = aggregate volume across all $N$ senders
- $r(V)$ = channel response rate, a **decreasing function** of aggregate volume ($r'(V) < 0$)
- $R(\cdot)$ = revenue function (pipeline generated from responses)
- $C(v_i)$ = cost of sending $v_i$ messages

The critical externality: each sender's $v_i$ contributes to $V$, which degrades $r(V)$ for all senders. But sender $i$ does not internalize the effect of their marginal message on $r$ for the other $N-1$ senders. This is the congestion externality.

Without constraints, each sender sets $v_i$ where their marginal private benefit equals their marginal private cost:

$$R'(v_i \cdot r(V)) \cdot r(V) = C'(v_i)$$

When tools reduce $C'(v_i)$ toward zero, the individually optimal $v_i$ increases for every sender. This pushes $V$ up, which pushes $r(V)$ down, which requires more $v_i$ to achieve the same pipeline target — the ouroboros feedback loop.

### 3.2 The Channel Viability Constraint

The channel has a **viability floor** — a minimum response rate below which the channel's transaction costs exceed its utility:

$$r(V) \geq r_{\min}$$

Below $r_{\min}$, the cost of generating a conversation through the channel exceeds the value of that conversation. The channel's utility is negative. Rational sellers should exit, and rational buyers already have.

This connects to Williamson's TCE framework: $r_{\min}$ is the threshold at which the transaction costs of using the channel (effort to find a trustworthy signal in a sea of noise) exceed the alternative — the buyer's cost of relying on incumbents, building in-house, or deferring the decision entirely.

### 3.3 The Lagrangian Formulation

The sender's constrained optimization problem:

$$\mathcal{L} = R(v_i \cdot r(V)) - C(v_i) + \lambda(r(V) - r_{\min})$$

Where $\lambda \geq 0$ is the **shadow price of channel health** — the marginal value of relaxing the channel viability constraint by one unit.

### 3.4 KKT Conditions and the Three Channel States

The Karush-Kuhn-Tucker conditions for this problem yield three distinct channel states:

**State 1: Healthy Channel** — $r(V) > r_{\min}$, $\lambda = 0$

The viability constraint is slack. Channel health is abundant and carries no shadow price. No sender thinks about channel health because it's not scarce. Individual optimization proceeds unconstrained. This was cold email circa 2015.

**State 2: Binding Constraint** — $r(V) = r_{\min}$, $\lambda > 0$

The viability constraint binds. Channel health is now scarce and has a positive shadow price. Each additional unit of aggregate volume directly trades off against channel viability. Sophisticated senders begin to feel the squeeze — their individually optimal volume generates declining returns. This is arguably the current state of cold email (3.4% average reply rate, with substantial variation between targeted and mass campaigns).

**State 3: Constraint Violated (Channel Collapse)** — $r(V) < r_{\min}$

The optimization problem is **infeasible**. No individual volume $v_i$ produces positive ROI. The channel's transaction costs exceed its utility for all senders. The rational move is to exit the channel entirely. This is the Babbling Equilibrium (Crawford & Sobel, 1982) — the state where rational receivers ignore all messages because the signal-to-noise ratio has collapsed below the threshold of usefulness.

### 3.5 The Social Planner's Problem

A mechanism designer (Hurwicz, 1972) would solve the **social** problem — maximizing total pipeline across all senders subject to the channel constraint:

$$\max_{\{v_i\}} \sum_{i=1}^{N} \pi_i = \sum_{i=1}^{N} [R(v_i \cdot r(V)) - C(v_i)] \quad \text{subject to} \quad r(V) \geq r_{\min}$$

The social optimum requires each sender to internalize the externality they impose on $r(V)$. The gap between the individual optimum (each sender maximizes their own pipeline) and the social optimum (total pipeline is maximized subject to channel health) is the **deadweight loss from the congestion externality**. This deadweight loss grows as the channel degrades — the further into State 2 the channel moves, the larger the gap between what senders collectively achieve and what they could achieve if they internalized the externality.

---

## 4. The Three-Level Friction Model

### 4.1 Integrating Channel Health into the ILG Equation

The existing ILG fundamental equation operates at the deal level:

$$F_{effective} = F_{base} \times (1 + \Delta_A)$$

The channel externality analysis reveals that $F_{base}$ is not exogenous. It is itself a function of channel health:

$$F_{base} = f(r(V), k, m)$$

Where:
- $r(V)$ = channel signal effectiveness (decreasing in aggregate volume)
- $k$ = asset specificity of the deal (from the existing triage framework)
- $m$ = market maturity stage (see Section 5)

The complete three-level model:

**Level 1 — Deal Level (existing ILG):** $F_{effective} = F_{base} \times (1 + \Delta_A)$

Individual deal friction is a function of base friction amplified by bilateral information asymmetry. ILG interventions (Blueprints, Red Teams, MIPs) reduce $\Delta_A$.

**Level 2 — Channel Level (new):** $F_{base} = F_{base}(r(V))$

Base friction is a function of channel health, which degrades as aggregate sender volume increases. Channel health is a common-pool resource subject to congestion externalities. As the channel degrades ($r(V) \downarrow$), base friction rises ($F_{base} \uparrow$) for **all** senders — including those producing high-quality, well-targeted outreach. This is why "just do better outbound" is insufficient as a strategy: individual quality can reduce $\Delta_A$, but it cannot fix $F_{base}$ when the channel itself is congested.

**Level 3 — Market Level (new):** The *type* of friction that dominates, and therefore the channels vulnerable to Jevons-driven collapse, shifts as the market matures. See Section 5.

### 4.2 Implications

The three-level model explains several phenomena the deal-level model alone cannot:

1. **Why well-targeted outreach still fails in congested channels.** A seller who has done excellent discovery, crafted genuinely relevant messaging, and identified the right buyer can still face a non-response — because $F_{base}$ has risen to the point where even strong signals are lost in noise. The channel-level degradation imposes a "floor" on friction that no amount of deal-level optimization can breach.

2. **Why identical sales motions produce different results across time.** The same ILG-style outreach that generated productive conversations in 2018 may fail in 2026, even with the same quality of research and targeting. The deal-level $\Delta_A$ hasn't changed. The channel-level $r(V)$ has.

3. **Why the "no decision" rate is increasing.** The 40-60% no-decision rate in enterprise sales is partly a deal-level phenomenon (fear of messing up, as documented in the Fear of Failure research). But it is also a channel-level phenomenon: the degradation of outbound channels has raised buyers' baseline skepticism, increasing $F_{base}$ even for legitimate, well-qualified opportunities.

---

## 5. Market Maturity and Channel Vulnerability

### 5.1 The Potential Well Curve Revisited

The existing ILG framework describes three market phases, each characterized by a different dominant transaction cost:

| Phase | Dominant Cost | Buyer's Question | GTM Motion |
|:---|:---|:---|:---|
| **Nascent** | Search & Discovery | "What solutions exist?" | Sales-Led Growth (SLG) |
| **Efficient** | Evaluation | "Does this actually work?" | Product-Led Growth (PLG) |
| **Saturated** | Consensus & Implementation | "Can we make this work *here*?" | Implementation-Led Growth (ILG) |

This document adds a critical dimension: **channel vulnerability varies systematically by market phase.**

### 5.2 Stage 1 — Nascent Markets (Low Jevons Risk)

In a nascent market, product-market fit is undefined. Few buyers and few sellers. The dominant transaction cost is search and discovery — the buyer may not even know they have the problem the seller is solving.

The binding constraint on outreach is **knowledge**, not production cost. A seller cannot automate what they do not yet understand. Cold email is useless in this market because neither party has the vocabulary to describe the value exchange. The channels that work — consultative sales conversations, deep discovery calls, relationship-based introductions — are inherently constrained by the seller's expertise and time.

**Jevons cannot bite because the elastic resource (production cost) is not the bottleneck.** Making it cheaper to send messages doesn't help when the binding constraint is understanding the problem well enough to describe the solution.

### 5.3 Stage 2 — Efficient Markets (High Jevons Risk)

Product-market fit is established. The problem is well-understood. The category exists. Multiple sellers can articulate the value proposition because the vocabulary has been standardized. The dominant transaction cost shifts to evaluation — the buyer needs to figure out which option is best among many.

The seller's job shifts from "help the buyer understand the problem" to "make sure the buyer finds us in a crowded field." This is an awareness and volume game. The binding constraint shifts to **production cost** — how cheaply can I get in front of qualified buyers?

This is where Jevons becomes dangerous. Demand for "sending outreach" is highly elastic because the problem is well-defined enough that any seller can articulate a pitch. Tools that reduce outreach cost are genuinely useful, for a while. But as more sellers adopt the same tools and the same playbook, the evaluation channel gets congested. Every seller sends the same AI-enriched email. The buyer's inbox fills with structurally identical messages from functionally interchangeable vendors. The channel collapses as Jevons predicts.

### 5.4 Stage 3 — Saturated Markets (Low Jevons Risk)

The category is mature. The buyer knows the problem, knows the general solution shape, and has likely experienced one or two failed implementations. The dominant transaction cost is consensus and implementation. Can this vendor deliver in my specific environment? Will my organization adopt it? What happens when things go wrong?

The channels that matter in Stage 3 are those that demonstrate **implementation credibility** — proof that the seller has done the work in comparable environments. The binding constraint is having actually done the implementations, not the cost of describing them. Implementation case studies, named customer references, per-EHR integration specifics, co-developed workflow documentation — these are all constrained by experience, not production cost.

**Jevons cannot eat Stage 3 channels because the binding constraint is expertise and track record, not efficiency.** You cannot automate your way to implementation credibility. The signal costs what it costs because the underlying work costs what it costs.

### 5.5 The Maturity Mismatch Problem

The critical insight connecting channel collapse to market maturity:

**The channels collapsing under Jevons are Stage 2 channels (evaluation-optimized), but many markets have already moved to Stage 3 (implementation-dominated).** The sales enablement stack is optimized for a friction profile that no longer matches the buyer's actual decision-making process.

Email, content marketing, and LinkedIn outreach are all evaluation-stage communication methods — useful for awareness and comparison. In a Stage 3 market, the buyer doesn't need more options. They need proof that the implementation will work. The tools are solving the wrong problem at industrial scale.

This explains why the collapse feels so acute: it's not just Jevons degrading the channel. It's Jevons degrading a channel that was already becoming structurally irrelevant to the buyer's primary concern. The mismatch between tool optimization (Stage 2) and market reality (Stage 3) amplifies the collapse.

### 5.6 Extended Potential Well Curve

| Phase | Dominant Cost | GTM Motion | Viable Channels | Jevons Risk | Binding Constraint |
|:---|:---|:---|:---|:---|:---|
| **Nascent** | Search | SLG | High-touch, consultative, relationship-based | Low | Knowledge of the problem |
| **Efficient** | Evaluation | PLG | Product-led trials, content marketing, outbound email | **High** | Production cost |
| **Saturated** | Consensus + Implementation | ILG | Implementation proof, costly signals, earned credibility | Low | Experience and track record |

---

## 6. Cross-Domain Parallels

The channel health externality described in this document is a specific instance of a general class of problems studied across multiple domains. These parallels establish that the pattern is well-understood, the formal tools exist, and the solution taxonomy is developed.

### 6.1 Traffic Congestion (Pigou, 1920; Knight, 1924; Wardrop, 1952)

Each additional car on a road slows every other car. The individual driver's cost of entering the road is lower than the social cost of their entry because they do not pay for the delay they impose on everyone else. The result: the road is overused relative to the social optimum.

Knight's insight is particularly relevant: the problem is not market failure but a **missing market**. Nobody owns the roads. Drivers treat road capacity as free because there is no property right forcing them to pay for the congestion they create. In the email channel, nobody owns buyer attention as a resource, so senders treat it as free.

The formal structure is identical to the sender optimization problem in Section 3.

### 6.2 Antibiotic Resistance

Antibiotics become cheaper and more accessible → doctors prescribe more liberally → bacteria evolve resistance → antibiotics stop working → more (or entirely new) antibiotics are needed to achieve the same effect. The individual doctor prescribing amoxicillin for a mild infection acts rationally — the cost to them is near zero. The collective cost (accelerating resistance) is catastrophic and invisible to the individual prescriber.

This parallel is particularly clean because it exhibits the same **irreversibility** as channel collapse. A depleted commons can sometimes be restored. Antibiotic resistance, once established, requires entirely new drug classes. Channel collapse may exhibit similar irreversibility — once buyer attention has been fully depleted in a channel and trust has been destroyed, "just sending better emails" may not restore the channel's effectiveness. The trust destruction is a ratchet, not a dial.

The WHO's response to antibiotic resistance is essentially mechanism design: restrict access (qualification gates for prescribing), monitor outcomes (resistance surveillance), and impose costs on overuse (antimicrobial stewardship programs). This maps directly to the seller qualification, outcome measurement, and hostage mechanisms discussed in `01-research/costly-signals.md` and the ILG Constitution.

### 6.3 Spectrum Allocation (Telecommunications)

Radio spectrum is a shared resource. If everyone broadcasts on the same frequency at maximum power, the signal-to-noise ratio collapses and nobody can communicate. The FCC manages spectrum as a commons using licensing (access qualification), power limits (volume constraints), and auctions (Pigouvian pricing).

The formal model: each broadcaster's transmission degrades the channel for every other broadcaster. Optimal allocation requires a central mechanism that limits total usage below the congestion threshold.

### 6.4 Carbon Emissions (The Global Commons)

Each firm's emissions are individually rational and collectively catastrophic. The atmosphere is the commons. The Lagrangian constraint is: total emissions ≤ the atmosphere's absorptive capacity. The shadow price ($\lambda$) is the social cost of carbon — what one additional ton of CO₂ costs society.

The carbon parallel provides the most developed policy toolkit, which maps to channel collapse solutions:

| Carbon Policy | Channel Collapse Equivalent |
|:---|:---|
| **Pigouvian tax** (carbon tax) | Charge senders for the externality they impose on the channel |
| **Cap and trade** | Set a total volume ceiling; let senders bid for access based on quality |
| **Command and control** (emissions standards) | Gmail's bulk sender requirements, spam filters |
| **Ostrom governance** (community self-management) | Buyer-community trust scoring, community-gated vendor access |
| **Coase Theorem** (define property rights) | Create property rights over buyer attention; let the market allocate access |

---

## 7. Corrective Mechanisms: From Diagnosis to Design

### 7.1 Pigouvian Correction: Internalizing the Externality

A Pigouvian tax on outbound email would charge each sender a cost proportional to the marginal degradation their message imposes on the channel. The optimal tax equals the marginal external cost at the socially optimal volume level.

In practice, this could take the form of a **sender reputation cost** — a system where each message sent deducts from a reputation score that determines future channel access. Messages that generate positive buyer responses restore the score; messages that generate spam reports, unsubscribes, or negative feedback deplete it. This is structurally equivalent to the **hostage model** from Williamson's TCE: the seller's channel access is the hostage, and poor behavior triggers its forfeit.

Gmail's sender reputation system is a crude approximation of this — bulk senders who exceed spam complaint thresholds lose deliverability. But it operates only on technical deliverability (did the email land?), not on signal quality (was the email worth reading?). A more complete Pigouvian mechanism would extend the measurement deeper into the value chain.

### 7.2 Ostrom Governance: Community Self-Regulation

Elinor Ostrom's research on commons governance (Nobel Prize, 2009) demonstrated that communities can successfully manage shared resources without either privatization or top-down regulation, provided certain institutional design principles are met:

1. **Clearly defined boundaries** — who has access to the resource
2. **Proportional equivalence between costs and benefits** — those who use more pay more
3. **Collective-choice arrangements** — the people affected by the rules help make the rules
4. **Monitoring** — behavior is visible to the community
5. **Graduated sanctions** — punishments escalate with repeated violations
6. **Conflict-resolution mechanisms** — disputes are resolved locally
7. **Recognition of rights to organize** — external authorities respect the community's self-governance

Applied to channel governance, this suggests a **buyer-community-governed access system** where:
- Buyers collectively define which vendors meet minimum qualification criteria (Principle 1)
- Vendor access costs scale with usage (Principle 2)
- Buyer feedback on vendor outreach quality is collected and visible (Principles 3-4)
- Vendors who overpromise or underdeliver face graduated access restrictions (Principle 5)
- Post-engagement outcome data feeds back into vendor qualification (Principles 4-5)

This is distinct from a Group Purchasing Organization (GPO), which optimizes for price rather than fit and strips context from the matching process. Ostrom's model preserves local adaptation — the rules are community-derived and context-specific, not imposed by a central authority optimizing a single metric.

### 7.3 Mechanism Design: Incentive-Compatible Channel Architecture

Mechanism Design Theory (Hurwicz, 1972; Maskin, 1999; Myerson, 1981; Nobel Prize, 2007) provides the formal discipline for designing institutions that produce desired outcomes even when participants act in self-interest and hold private information.

The core concept — **incentive compatibility** — requires that the mechanism's rules make truthful behavior the dominant strategy. Applied to channel design, this means: the rules must make honest, quality outreach more profitable for the sender than flooding, even when the sender's natural incentive is to maximize volume.

The mechanism design question for outbound channels:

**Given:** Senders have private information about their product quality. Buyers cannot verify quality before engaging. Each sender's volume degrades the channel for all senders. The desired outcome is: buyers receive outreach that accurately represents seller quality, and high-quality sellers are rewarded more than low-quality sellers.

**Design:** A channel architecture where:

1. **Seller access requires a credible commitment** ("hostage" in Williamson's terminology) — something valuable the seller puts at risk and forfeits if they fail to deliver on their promises. The hostage makes the cost of deception higher than the cost of honesty, satisfying incentive compatibility.

2. **Quality measurement extends deep enough to be hard to game.** Measurement at Level 1 (emails sent, open rates) is trivially gamed through volume. Level 2 (meetings booked) is gameable through misleading outreach. Level 3 (opportunity conversion, implementation success) is hard to game because it requires actually delivering value. Level 4 (NRR, retention, expansion) is the ultimate measurement — it can only be achieved through honest scoping, successful implementation, and sustained value delivery. The deeper the measurement, the more the mechanism selects for genuine quality.

3. **The shadow of the future extends across interactions.** A sender's performance in current engagements determines their access to future buyers. This transforms a single-shot game (spam the inbox, extract what you can) into a repeated game where cooperation is the dominant strategy — the same structural logic that the ILG vested commission model applies to sales compensation.

4. **Cold-start access is gated by hostages rather than proof.** New sellers who lack track records can enter the channel by putting a credible commitment at risk (financial deposit, limited-access trial period with quality monitoring) rather than presenting proof they don't yet have. The hostage substitutes for proof. This addresses the cold-start problem without requiring new sellers to already have what only market participation can produce.

### 7.4 Demurrage-Based Trust: Credibility as a Depreciating Asset

A further refinement to the mechanism design architecture draws on the concept of demurrage currency — money that loses value over time unless actively circulated (Gesell, 1916). In the Wörgl experiment (Austria, 1932), local scrip depreciated 1% per month, incentivizing rapid circulation over hoarding. The carrying cost transformed the currency's function from a store of value to a medium of exchange.

Applied to channel access, demurrage addresses a structural distortion that congestion externalities and mechanism design alone do not: incumbent trust does not depreciate. A vendor's reputation, once established, persists indefinitely as a zero-carrying-cost asset — regardless of whether current delivery quality matches historical performance. The buyer's "safe choice" calculation ("nobody gets fired for buying IBM") is systematically biased toward accumulated credibility over current performance, creating an asymmetric barrier that new entrants cannot overcome through quality alone.

A demurrage mechanism on seller credibility would impose a carrying cost on trust: the seller's channel access, trust score, and position in the buyer's consideration set decay over time unless refreshed with current evidence of delivery quality. Not evidence from 2022. Evidence from this quarter — recent implementation outcomes, current customer satisfaction, fresh third-party verification.

This extends the three-level friction model with a temporal dimension:

| Level | What Decays | Decay Mechanism | What Refreshes It |
|:---|:---|:---|:---|
| **Deal** | Buyer urgency ($\delta$) | Time since triggering event | New triggering event, or seller-created urgency through costly signals |
| **Channel** | Seller access/credibility | Time since last verified outcome | Fresh implementation data, current customer references, verified results |
| **Market** | Aggregate buyer attention | Natural budget/planning cycles | Fresh costly signals from the vendor community |

The demurrage principle interacts with the congestion externality as follows: channel collapse (Section 3) makes it harder for new entrants to build trust. The absence of trust depreciation (this section) makes it harder for new entrants to displace incumbents whose historical trust persists without renewal. These two distortions reinforce each other — the new entrant faces a congested channel where signals can't be heard AND an incumbent whose credibility never expires. A demurrage mechanism on trust attacks the second distortion, creating continuous competitive pressure on incumbents to demonstrate current quality.

The VBC parallel is instructive. Value-Based Care's original design allowed providers to game quality scores through patient selection and then coast on favorable metrics. The absence of score depreciation meant that cherry-picked historical outcomes persisted as evidence of quality long after the selection bias should have been corrected. A demurrage mechanism on VBC quality scores — requiring current evidence of delivery quality each measurement period, with historical scores decaying — would prevent the selection-then-coasting strategy. The same logic applies to vendor trust in B2B channels.

---

## 8. Implications for the ILG Framework

### 8.1 Constitutional Addition: The Channel Viability Corollary

The principle articulated in Axiom I — "Friction is a Feature" — extends from the deal level to the channel level:

> **Channel Corollary to Axiom I:** The same principle that makes friction necessary in individual deals applies to the channels through which those deals are initiated. A channel that eliminates production cost for the sender without imposing a corresponding quality constraint will be flooded by low-quality actors until the channel's signal-to-noise ratio collapses. Friction at the channel level is what separates signal from noise. Remove it, and the channel reaches a Babbling Equilibrium — a state where rational receivers ignore all messages because the cost of distinguishing quality from noise exceeds the expected value of engaging.

### 8.2 Channel Triage Diagnostic

Before selecting an outreach channel, assess:

1. **Is production cost the binding constraint on sending volume in this channel?** If yes, the channel is Jevons-vulnerable. If other constraints bind first (time, relationships, expertise, physical presence), the channel is resistant.

2. **What market maturity stage is the buyer in?** If Stage 2 (evaluation-dominated), volume-oriented channels may still have residual utility. If Stage 3 (implementation-dominated), evaluation-stage channels are structurally mismatched to the buyer's primary concern, regardless of congestion level.

3. **What is the current channel state (per KKT)?** Healthy ($\lambda = 0$), binding ($\lambda > 0$), or collapsed (infeasible)? Investing in a channel that has already crossed the viability threshold produces negative returns regardless of message quality.

A channel mismatch — using a Jevons-vulnerable, Stage 2 channel for a Stage 3 buyer — means the seller is fighting both channel-level congestion ($F_{base} \uparrow$) and structural irrelevance (the channel doesn't address the buyer's actual friction). This is the worst-case scenario and the one most common in B2B sales today.

### 8.3 The Non-Debaseable Currency Principle

The Jevons vulnerability diagnostic implies a design principle for channel selection and construction:

> **Non-Debaseable Currencies:** Effective B2B communication channels must be denominated in currencies that cannot be debased through efficiency gains. A currency is non-debaseable when its binding constraint is something other than production cost — time, relationships, demonstrated expertise, implementation depth, social capital. These currencies satisfy the Single Crossing Property: the cost of producing the signal is proportionally lower for high-quality sellers, and no tool can change this ratio by making production cheaper for everyone.

---

## 9. Open Questions and Future Development

### 9.1 Empirical Calibration

The formal model requires empirical calibration of several parameters:
- The functional form of $r(V)$ — how exactly does response rate decay with aggregate volume? Is it linear, convex, or S-shaped with a threshold?
- The value of $r_{\min}$ — at what response rate does the channel become functionally useless? This likely varies by deal size, sales cycle length, and market maturity.
- The demand elasticity of sending across different channels — how price-sensitive is volume?

### 9.2 The Energy Cost Feedback Loop

Rising energy costs affect both sides of the channel equation. AI compute costs increasing makes AI-generated outreach more expensive (potentially re-imposing Jevons constraints). But energy costs also make in-person alternatives (travel, conferences, events) more expensive. Both the cheap channels and the costly channels are getting costlier simultaneously, creating an unstable equilibrium whose resolution is genuinely uncertain.

The threshold question: at what energy cost level does demand for AI-generated outreach become inelastic? And does the simultaneous cost increase in alternative channels mean the inbox remains the "least bad" option even as it degrades?

### 9.3 Irreversibility and Hysteresis

The antibiotic resistance parallel suggests that channel collapse may exhibit **hysteresis** — the channel may not recover along the same path it degraded. Trust destruction is asymmetric: it takes years of quality interactions to build trust in a channel and a single wave of spam to destroy it. If this is the case, restoring a collapsed channel may require not just reducing volume but actively rebuilding trust through costly, sustained quality — a process far more expensive than preventing the collapse in the first place.

### 9.4 Platform Incentive Conflicts

The mechanism design solutions described in Section 7.3 face a structural tension: the platform that governs channel access profits from volume (more senders = more revenue), but channel health requires volume restraint. This creates a principal-agent problem at the platform level that mirrors the principal-agent problem at the seller level. Whether any platform can resolve this conflict — serving as both the channel and the quality governor — is an open question with implications for the business model viability of incentive-compatible outbound platforms.

---

## References

- Akerlof, G.A. (1970). "The Market for 'Lemons': Quality Uncertainty and the Market Mechanism." *Quarterly Journal of Economics*, 84(3), 488-500.
- Crawford, V.P. & Sobel, J. (1982). "Strategic Information Transmission." *Econometrica*, 50(6), 1431-1451.
- Hardin, G. (1968). "The Tragedy of the Commons." *Science*, 162(3859), 1243-1248.
- Hurwicz, L. (1972). "On informationally decentralized systems." In *Decision and Organization*, ed. R. Radner and C.B. McGuire, North-Holland.
- Jevons, W.S. (1865). *The Coal Question*. Macmillan and Co.
- Maskin, E. (1999). "Nash Equilibrium and Welfare Optimality." *Review of Economic Studies*, 66, 23-38.
- Myerson, R.B. (1981). "Optimal Auction Design." *Mathematics of Operations Research*, 6(1), 58-73.
- Olson, M. (1965). *The Logic of Collective Action: Public Goods and the Theory of Groups*. Harvard University Press.
- Ostrom, E. (1990). *Governing the Commons: The Evolution of Institutions for Collective Action*. Cambridge University Press.
- Pigou, A.C. (1920). *The Economics of Welfare*. Macmillan and Co.
- Spence, M. (1973). "Job Market Signaling." *Quarterly Journal of Economics*, 87(3), 355-374.
- Williamson, O.E. (1985). *The Economic Institutions of Capitalism*. Free Press.