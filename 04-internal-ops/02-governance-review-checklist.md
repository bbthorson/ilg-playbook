# Deal Review Checklist for Managers

**Purpose:** Forensic questions for forecast calls to calibrate Bridge deals based on friction, not hope.

---

## Pre-Review: Classification Validation

**Before diving into the deal, validate the lane:**

- [ ] **"Why is this a Bridge?"** 
  - Show me the Process Calculator score (must be 10-20)
  - What's the tech specificity? Org specificity? Political complexity?
  
- [ ] **"Did the override rule apply?"**
  - Did they ask for a pilot/POC? (Auto-upgrade to Bridge)

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
  - Current state diagram? ✓ / ✗
  - Data sample? ✓ / ✗
  
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

**Red Flag:** Buyer still thinks it's "plug and play" → High buyer asymmetry ($I_A = +1$)

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

### Seller Asymmetry (What WE Don't Know)
- [ ] **Economic Event:** Can we name the specific trigger? (0-5)
- [ ] **Political Casualty:** Do we know who loses power? (0-5)
- [ ] **Saboteur:** Have we identified the blocker? (0-5)

**Seller Clarity Score:** ___/15

---

### Buyer Asymmetry (What THEY Don't Know)
- [ ] **Lemon Check:** Do they know what we CAN'T do? (0-5)
- [ ] **The Work:** Do they know implementation effort? (0-5)
- [ ] **Price of Failure:** Have they quantified cost of inaction? (0-5)

**Buyer Clarity Score:** ___/15

---

### Asymmetry Delta
**Calculate:** |Seller Score - Buyer Score| = ___

- **Delta < 3:** ✅ Symmetric → Forecastable
- **Delta > 5:** ⚠️ Asymmetric → High risk
  - If Seller Score low: Rep is flying blind → Go back to Blueprint
  - If Buyer Score low: Buyer is hallucinating → Go back to Red Team

---

## Forecast Verdict

### Commit Criteria (All must be true)
- ✅ All artifacts Green (Blueprint signed, Red Team completed, MIP agreed)
- ✅ Asymmetry Delta < 3
- ✅ Resources committed in writing
- ✅ Saboteur identified and contained

### Best Case
- 🟡 Artifacts in progress
- 🟡 Some asymmetry remaining but addressable

### Pipeline
- 🔴 Blueprint not signed
- 🔴 Reciprocity gate not passed
- 🔴 High asymmetry delta (>5)

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

3. **Asymmetry Risk ($I_A$):** They don't trust us
   - **Fix:** Offer Paid Pilot (costly signal) to prove intent

---

**Remember:** You're not forecasting when it will close. You're forecasting whether the work has been done to reduce friction.
