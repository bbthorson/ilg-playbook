# Module 3: Infinite Game

**Learning Time:** 2 hours  
**Prerequisites:** Modules 0-2

---

## Learning Objectives

By the end of this module, you will be able to:

1. **Understand repeated game theory** and why SaaS is an "infinite game"
2. **Explain the vested commission model** and how it aligns incentives with outcomes
3. **Calculate personal risk/reward** using clawback mechanics
4. **Design governance structures** (Mutual Implementation Plans) that ensure successful starts
5. **Articulate why hiding flaws destroys NRR** in a repeated game

---

## Key Concepts

### The Infinite Game (Repeated Game Theory)

**From the ILG Constitution (Axiom III — Law of Governance):**

> "SaaS is an 'Infinite Game' governed by the Shadow of the Future."

**Single-Shot Game vs. Repeated Game:**

| | Single-Shot | Repeated Game (SaaS) |
|---|---|---|
| **Time Horizon** | One transaction | Ongoing relationship |
| **Optimal Strategy** | Maximize immediate profit | Maximize lifetime value |
| **Asymmetry Gap ($\Delta_A$)** | Leave gaps wide (hide flaws, skip discovery) | Drive $\Delta_A \to 0$ (close both seller ignorance and buyer uncertainty) |
| **Consequence of Deception** | None (no future interaction) | Retaliation (churn, bad reviews) |

**The Shadow of the Future:**

When players know they'll interact again, **cooperation becomes rational**.

- **$T_0$:** Signature (you get paid)
- **$T_1$:** Implementation (they discover the truth)
- **$T_2$:** Renewal (they decide to stay or churn)

**The ILG Principle:** We must drive $\Delta_A \to 0$ at $T_0$ — closing both seller ignorance and buyer uncertainty — to secure $T_2$.

### The Principal-Agent Problem

**The Misalignment:**

- **Principal (Buyer):** Pays for the **outcome** (successful implementation, adoption, ROI)
- **Agent (Sales Rep):** Paid for the **signature** (contract signed)

**The Consequence:**

Reps are incentivized to:
- Over-promise features
- Under-estimate implementation effort
- Hide flaws to close faster
- Move on to next deal (leaving CS to clean up the mess)

**Result:** Failed implementations, churn, destroyed NRR

### The Vested Commission Model

**The Solution:** Align rep compensation with customer success through **skin in the game**.

**The Structure:**

1. **Front-Load CAC (Liquidity):**
   - Pay 100% commission on signature
   - Solves rep cash flow needs

2. **The Clawback (Alignment):**
   - Commission subject to 100% clawback if customer "fails to launch"
   - Failure defined as: opt-out, <10% adoption by Day 90, hidden technical incompatibility

3. **Safe Harbor (Fairness):**
   - Clawback waived for factors outside rep control (M&A, sponsor fired, product bug)

4. **NRR Bonus (Upside):**
   - Rep receives % of expansion revenue or early renewal within 12 months
   - Requires attending QBR handover to CS

**The Incentive:**

Reps now have **financial motivation** to:
- Tell the truth about implementation effort
- Qualify out bad-fit deals
- Ensure successful handoff to CS
- Participate in customer success

### The Mutual Implementation Plan (MIP)

**The Governance Structure:**

A contractual agreement that:
- Defines success metrics (RE-AIM framework)
- Allocates resources from both sides
- Creates accountability for both parties
- Turns resources into "tradeable currency"

**Why It Works:**

- **For Buyer:** Reduces fear (clear plan, shared accountability)
- **For Seller:** Ensures commitment (costly signal, skin in the game)
- **For Rep:** Protects against clawback (documented plan reduces failure risk)

---

## Why This Matters

**The Economic Logic:**

In traditional sales comp:
- Rep leaves $\Delta_A$ wide (hides flaws, skips discovery)
- Customer discovers the truth at $T_1$ (implementation)
- Customer churns at $T_2$ (renewal)
- Rep has already moved on (no consequence)

**Result:** 
- NRR < 100%
- CAC never recovered
- Negative word-of-mouth

**With Vested Commission:**
- Rep drives $\Delta_A \to 0$ at $T_0$ (closes both gaps through discovery and costly signals)
- Customer has realistic expectations
- Implementation succeeds
- Customer renews and expands
- Rep earns NRR bonus

**Result:**
- NRR > 100%
- CAC recovered + expansion
- Positive word-of-mouth

---

## Knowledge Base References

- [ILG Constitution — Axiom III (Law of Governance): Recursive Cooperation + Reputation Depreciation](../../../theory/01-foundation/00-ilg-constitution.md)
- [Game Theory and NRR](../../../theory/02-research/game-theory-and-nrr.md) (Academic foundation)
- [Vested Commission Agreement](../../02-internal-ops/03-incentives-vested-commission.md) (Practical template)
- [Mutual Implementation Plan](../../01-field-assets/ilg-motion/03-closing-mutual-implementation-plan.md) (Governance tool)

---

## Exercises

### Exercise 1: The Clawback Calculation

**Instructions:** Calculate your personal risk/reward on this deal.

**Deal Details:**
- **ACV:** $200,000
- **Commission Rate:** 10% ($20,000)
- **Implementation Timeline:** 90 days
- **Clawback Trigger:** <10% adoption by Day 90
- **NRR Bonus:** 5% of expansion revenue in first 12 months

**Scenario A: You Tell the Truth**

You're honest about:
- Implementation will take 6 months (not 3)
- Requires dedicated project manager from their side
- Data migration is complex (not "plug and play")
- Change management is critical

**Outcome:**
- Deal closes (but takes 2 extra months)
- Implementation succeeds
- Adoption: 85% by Day 90
- Expansion: $50,000 in Year 1

**Your Earnings:**
- Commission: $___
- Clawback: $___
- NRR Bonus: $___
- **Total: $___**

---

**Scenario B: You Hide the Flaws**

You say:
- "Implementation is easy, 3 months max"
- "It's plug and play, minimal effort"
- "You don't need a dedicated PM"

**Outcome:**
- Deal closes quickly
- Implementation struggles (no PM, data issues)
- Adoption: 8% by Day 90 (below threshold)
- Customer exercises opt-out clause

**Your Earnings:**
- Commission: $___
- Clawback: $___
- NRR Bonus: $___
- **Total: $___**

---

**Questions:**

1. **Which scenario is more profitable for you?**

2. **What's the financial risk of hiding flaws?**

3. **How does this change your incentive to qualify deals properly?**

4. **How does this change your incentive to ensure successful handoff to CS?**

---

### Exercise 2: MIP Resource Negotiation

**Instructions:** You're designing a Mutual Implementation Plan. Allocate resources and define success metrics.

**Deal Context:**
- Revenue operations platform
- 6-month implementation
- Cross-functional (Sales, Marketing, CS)
- $500k ACV

**Your Task:**

1. **Define Success Metrics (RE-AIM Framework):**
   - **Reach:** What % of users must be active?
   - **Effectiveness:** What business outcome must improve?
   - **Adoption:** What % of workflows must migrate?
   - **Implementation:** What timeline is realistic?
   - **Maintenance:** What ongoing support is needed?

2. **Allocate Resources:**

   **From Customer:**
   - Project Manager: ___ hours/week
   - Executive Sponsor: ___ hours/month
   - Technical Resources: ___
   - Budget for Change Management: $___

   **From Vendor:**
   - Implementation Consultant: ___ hours
   - Technical Support: ___
   - Training Sessions: ___
   - Custom Development: ___ hours

3. **Define Failure Conditions (Clawback Triggers):**
   - What would constitute "failure to launch"?
   - What's outside your control (Safe Harbor)?

4. **Create Tradeable Currency:**
   - If customer wants faster timeline, what do you need in return?
   - If customer can't provide PM, what's the alternative?

---

### Exercise 3: The Infinite Game Mindset

**Instructions:** Reflect on how the infinite game mindset changes your approach.

**Traditional Sales Mindset (Single-Shot Game):**

1. **Goal:** Close the deal this quarter
2. **Objection Handling:** Overcome objections (convince them)
3. **Information Sharing:** Highlight benefits, minimize risks
4. **Post-Sale:** Hand off to CS, move to next deal
5. **Success Metric:** Quota attainment

**Infinite Game Mindset (Repeated Game):**

1. **Goal:** ___
2. **Objection Handling:** ___
3. **Information Sharing:** ___
4. **Post-Sale:** ___
5. **Success Metric:** ___

**Questions:**

1. **How does the infinite game mindset change your qualification criteria?**

2. **How does it change your willingness to walk away from bad-fit deals?**

3. **How does it change your relationship with Customer Success?**

4. **How does it change your approach to objections (fear vs. price)?**

---

## Assessment Criteria

### Knowledge Check (LLM will evaluate)

**Foundational Understanding:**
- Can you explain the difference between single-shot and repeated games?
- Can you articulate the principal-agent problem in sales?

**Applied Understanding:**
- Can you calculate clawback risk/reward?
- Can you design an MIP with appropriate resources and metrics?

**Mastery:**
- Can you explain how vested commission aligns incentives with NRR?
- Can you articulate the infinite game mindset in your own words?

### Progression Gate

To complete the curriculum, you must:
- Correctly calculate clawback scenarios
- Design a realistic MIP with resources and metrics
- Articulate the infinite game mindset shift

---

## LLM Tutor Prompts

**For the LLM facilitating this module:**

When evaluating responses:

1. **Clawback Calculation:**
   - Check math accuracy
   - Probe understanding: "Why is Scenario A more profitable long-term?"
   - Challenge: "What if you could hide flaws on 10 deals but 3 fail? Still worth it?"

2. **MIP Design:**
   - Evaluate realism: Are resource allocations reasonable?
   - Check metrics: Are they measurable and tied to business outcomes?
   - Assess failure conditions: Are they fair (not all vendor risk)?

3. **Infinite Game Mindset:**
   - Look for genuine shift in thinking (not just parroting concepts)
   - Probe: "How would you handle a deal that won't close this quarter but is right long-term?"
   - Challenge: "Your manager wants you to sandbag implementation timeline to close faster. What do you do?"

### Answer Key (For LLM Tutor Only)

**Clawback Calculation:**
- Scenario A: $20k commission + $2.5k NRR bonus = $22.5k
- Scenario B: $20k commission - $20k clawback = $0

**Key Insight:** Truth-telling is more profitable AND less risky.

---

## Congratulations!

You've completed the ILG Learning Curriculum. 

**Next Steps:**
- Practice with [Simulations](../simulations.md)
- Apply ILG methodology to your current pipeline
- Use the [Field Assets](../../01-field-assets) in real deals
- Continue learning with the [Research Papers](../../../theory/02-research)
