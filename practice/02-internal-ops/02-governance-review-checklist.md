# Deal Review Checklist for Managers

**Purpose:** Forensic questions for forecast calls to calibrate Bridge deals based on friction, not hope.

| | |
|---|---|
| **Inputs** | A Bridge deal entering or already in commit forecast. Rep's filled artifacts (Blueprint / Red Team / MIP). |
| **Outputs** | Phase-by-phase pass/fail on the three friction phases; forecast verdict (Commit / Best Case / Pipeline). |
| **Cadence** | Per deal at each phase gate; aggregated weekly on forecast call. |
| **Owner** | Sales manager (with VP spot-checks). |
| **Lighter version** | [Deal Calibration Sheet](./01-governance-deal-calibration.md) for routine forecast calls. |

---

## Pre-Review: Classification Validation

**Before diving into the deal, validate the lane:**

- [ ] **"Why is this a Bridge?"** 
  - Show me the [Process Calculator](../01-field-assets/process-calculator.md) score (Mature market + cost score 10–20, or Transitional 15–20, or pilot/POC override)
  - What's the integration depth? Workflow change scope? Consensus complexity? Retention horizon?
  
- [ ] **"Did the override rule apply?"**
  - Did they ask for a pilot/POC? (Auto-upgrade to ILG)

- [ ] **"Do the artifacts being used satisfy the Friction Allocation Principles?"**
  - Spot-check the rep's signal mechanisms against the four principles via the [Friction Allocation Diagnostic](../01-field-assets/friction-allocation-diagnostic.md). Especially relevant when reviewing how the rep is qualifying the deal and what costly signals are being deployed.

**Red Flag:** Rep can't articulate why it's a Bridge → Likely misclassified

---

## Phase 1: The Blueprint (Discovery & Qualification)

### Economic Event
- [ ] **"What's the catalyst?"** 
  - Is it a crisis (audit, board deadline, revenue target) or just "nice to have"?
  - What's the cost of inaction in dollars/month?
  
- [ ] **"Why now vs. 6 months from now?"**
  - Is there a bleeding neck or just general pain?

**Red Flag:** Vague answers ("they want to improve efficiency") → No urgency, deal will slip

---

### Political Mapping
- [ ] **"Who loses power if we win?"**
  - Can the rep name the political casualty?
  - What's the containment strategy?
  
- [ ] **"Who's the saboteur?"**
  - Has the rep identified the person most likely to block?
  - Were they invited to the Red Team Workshop?

**Red Flag:** Rep says "everyone is supportive" → Flying blind, saboteur will surface later

---

### Sacred Cows
- [ ] **"What's the protected workflow/team?"**
  - What existing system/process is politically untouchable?
  - How are we navigating around it?

**Red Flag:** Rep doesn't know → Will hit unexpected resistance during implementation

---

### Reciprocity Gate
- [ ] **"Did they provide the artifacts?"**
  - Current state diagram? yes / no
  - Data sample? yes / no
  
- [ ] **"Did they agree to the Technical Hook?"**
  - What specific data access or integration did they commit to?

**Red Flag:** Rep moved forward without artifacts → Customer isn't serious, deal will stall

---

## Phase 2: The Red Team Workshop (Validation)

### Pre-Mortem Execution
- [ ] **"Did you run the pre-mortem?"**
  - "It's 6 months from now, the implementation failed. What went wrong?"
  
- [ ] **"What failure modes did you find?"**
  - Technical risks?
  - Organizational risks (adoption, change management)?
  - Political risks (sabotage)?

**Red Flag:** Workshop was "all positive" → Happy ears, not real validation

---

### Resistance Profiling
- [ ] **"Did you differentiate skeptics from adversaries?"**
  - Who asked rational questions and engaged with evidence? (Skeptics)
  - Who dismissed evidence and declined to engage? (Adversaries)
  
- [ ] **"How did you handle the adversaries?"**
  - Containment strategy (elevate to higher authority, build coalition)?
  - Or did rep try to "convince" them? (Wrong approach)

**Red Flag:** Rep tried to convince adversaries with more demos → Political blocking will continue

---

### Gap Analysis
- [ ] **"Did the buyer sign off on what we CAN'T do?"**
  - What features did they think we had that we don't?
  - What implementation effort did they underestimate?

**Red Flag:** Buyer still thinks it's "plug and play" → High buyer uncertainty ($I_{buyer}$)

---

## Phase 3: The MIP (Governance & Close)

### Resource Allocation
- [ ] **"Is the resource plan attached to the contract?"**
  - Customer PM: ___ hours/week
  - Executive sponsor: ___ hours/month
  - Technical resources: ___
  
- [ ] **"What happens if they can't provide the PM?"**
  - What's the tradeable currency? (Vendor PM, extended timeline, reduced scope?)

**Red Flag:** No resource commitment → Implementation will fail due to lack of customer engagement

---

### Success Metrics
- [ ] **"What are the RE-AIM metrics?"**
  - Reach: What % of users must be active?
  - Effectiveness: What business outcome must improve?
  - Adoption: What % of workflows must migrate?
  - Implementation: What's the realistic timeline?
  
- [ ] **"Are these tied to business KPIs?"**
  - Not just "usage" but actual business outcomes

**Red Flag:** Vague metrics ("improve efficiency") → Can't measure success, can't prove ROI

---

### Failure Conditions
- [ ] **"What triggers the clawback?"**
  - <10% adoption by Day 90?
  - Opt-out clause exercised?
  - Technical incompatibility discovered?
  
- [ ] **"What's outside our control (Safe Harbor)?"**
  - M&A, sponsor fired, product bug?

**Red Flag:** All risk on vendor → Unfair MIP, customer has no skin in the game

---

## Bilateral Asymmetry Scorecard

Run the full scorecard from **[04-incentives-asymmetry-scorecard.md](./04-incentives-asymmetry-scorecard.md)** as a sub-check inside this review.

In short: score Seller Ignorance ($I_{seller}$) across four dimensions (technical architecture, operational workflow, the economic event, the political map) and Buyer Uncertainty ($I_{buyer}$) across four more (vendor capability, adoption burden, cost predictability, price of failure). Each dimension scores 1 to 5, where **5 means high asymmetry**. Average each half, then add them.

$$\Delta_A = I_{seller} + I_{buyer} \qquad \Delta_A \in [2, 10]$$

The gap is a **sum**, not a difference. Two equally blind parties do not cancel out; they compound.

| $\Delta_A$ | Classification | Forecast treatment |
|---|---|---|
| **2.0 to 4.0** | Low | Forecastable. Lightweight MIP is sufficient. |
| **4.0 to 7.0** | Moderate | Hold final pricing until S2 and B3 are each at 2 or below. |
| **7.0 to 10.0** | High | Commercial hold. No contract terms until the audit clears. |

**Routing — which half is wider.** The sum sets the risk; the balance sets the next action.

- **$I_{seller}$ wider by 1.0 or more** → we are flying blind, go back to the [Blueprint](../01-field-assets/ilg-motion/01-discovery-contextual-blueprint.md). Do not run a Red Team on an environment we have not mapped.
- **$I_{buyer}$ wider by 1.0 or more** → they are working from an imagined product, go back to the [Red Team](../01-field-assets/ilg-motion/02-validation-red-team-protocol.md).
- **Within 1.0 and both high** → the most dangerous state on the card. Run Blueprint and Red Team in sequence before forecasting.

---

## Forecast Verdict

### Commit (all must be true)
- All artifacts green (Blueprint signed, Red Team completed, MIP agreed)
- $\Delta_A$ below 4.0
- Resources committed in writing
- Saboteur identified and contained

### Best Case
- Artifacts in progress
- $\Delta_A$ between 4.0 and 7.0, with a named plan to close the wider half

### Pipeline
- Blueprint not signed
- Reciprocity gate not passed
- $\Delta_A$ above 7.0

---

## Manager's Oath

**"I will not commit a Bridge deal that has not survived a Red Team Workshop."**

---

## Common Rep Mistakes to Watch For

1. **Misclassification:** Treating a Bridge like a Toaster (velocity motion on high-friction deal)
2. **Skipping gates:** Moving to Red Team without Blueprint artifacts
3. **Happy ears:** Red Team was "all positive" (not real validation)
4. **Convincing adversaries:** Trying to overcome political resistance with more demos
5. **Vague metrics:** No specific success criteria in MIP
6. **Hiding complexity:** Not educating buyer on implementation effort (high buyer asymmetry)
7. **Flying blind:** Can't name the saboteur or political casualty (high seller asymmetry)

---

## The "No Decision" Risk Analysis

**If the deal slips, it's one of these three:**

1. **Valuation Risk ($V_{solution}$):** ROI too fuzzy
   - **Fix:** Tighten "Cost of Inaction" in Blueprint

2. **Transaction Cost Risk ($TC_{implementation}$):** Work too scary
   - **Fix:** Deploy "Concierge Onboarding" in MIP to lower perceived effort

3. **Asymmetry Risk ($\Delta_A$):** They don't trust us (high $I_{buyer}$) or we don't understand them (high $I_{seller}$)
   - **Fix for $I_{buyer}$:** Offer Paid Pilot (costly signal) to prove intent
   - **Fix for $I_{seller}$:** Deeper discovery — revisit Blueprint, map workflows you missed

---

**Remember:** You're not forecasting when it will close. You're forecasting whether the work has been done to reduce friction.
