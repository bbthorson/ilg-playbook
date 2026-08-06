# Module 0: Triage Protocol

**Learning Time:** 2 hours  
**Prerequisites:** None (start here)

---

## Learning Objectives

By the end of this module, you will be able to:

1. **Classify deals** as "Bridge" (high friction) or "Toaster" (low friction) using the diagnostic rubric
2. **Score deals** accurately on tech specificity, org specificity, political complexity, and retention horizon
3. **Apply the decision matrix** to determine the appropriate sales motion (ILG vs. SLG/PLG)
4. **Explain the rationale** for why asset specificity drives transaction costs

---

## Key Concepts

### The Bridge vs. Toaster Framework

**The Core Insight:** Not all enterprise deals are created equal. The sales motion must match the deal's friction profile.

- **The Toaster (Low Friction):**
  - Easy to adopt, easy to remove
  - Single team or department
  - Simple decision-making
  - **Strategy:** Optimize for velocity (SLG/PLG)
  
- **The Bridge (High Friction):**
  - Deep integration, hard to rip out
  - Cross-functional impact
  - Complex stakeholder dynamics
  - **Strategy:** Optimize for safety and certainty (ILG)

### Pre-Qualification: The Workflow Maturity Gate

Before scoring, answer one binary question: **Does a documented SOP exist for this problem today?**

- **YES** → Proceed to scoring.
- **NO** → **STOP.** This is the **Chaos Trap** (High Specificity + Undefined Workflow). Redirect to Consulting first.

### The Diagnostic Rubric

Score each deal on four dimensions (1-5 scale):

1. **Tech Specificity:** How hard is it to rip out?
   - 1 = Standalone tool, no integration
   - 3 = Standard API integration
   - 5 = Deep ERP/core infrastructure rewrite

2. **Org Specificity:** How many habits must change?
   - 1 = Single team (<5 users), no process change
   - 3 = Single department, minor process tweak
   - 5 = Cross-functional, total workflow overhaul

3. **Political Complexity:** Who can say no?
   - 1 = Single decision maker
   - 3 = Committee (3-4 stakeholders)
   - 5 = Board approval/procurement/security audit required

4. **Retention Horizon:** One-shot or repeat game?
   - 1 = One-time project, no renewal expected
   - 3 = Annual contract, moderate switching cost
   - 5 = Multi-year platform, deep dependency, high switching cost

### The Decision Matrix

- **Score 4-9:** Lane 1 (Toaster) → Use SLG/PLG motion
- **Score 10-20:** Lane 2 (Bridge) → Deploy ILG motion

**Override Rule:** If prospect asks for a "Pilot" or "POC," immediately upgrade to Bridge (score 20).

---

## Why This Matters

**From the ILG Constitution (Axiom I — Law of Economic Boundaries):**

> "Sales is the management of transaction costs. Never apply a Bridge motion to a Toaster, and never sell a Bridge without a Blueprint."

**The Economic Logic:**

When asset specificity is high (Bridge), transaction costs explode due to:
- Implementation effort (the work)
- Information asymmetry (the fear multiplier)
- Consensus costs (political complexity)

Misclassifying a Bridge as a Toaster leads to:
- Stalled deals ("no decision")
- Failed implementations
- Early churn

---

## Knowledge Base References

- [ILG Constitution — Axiom I (Law of Economic Boundaries) and the Boundary Condition derivation](../../../theory/01-foundation/00-ilg-constitution.md)
- [Deal Triage Calculator](../../01-field-assets/process-calculator.md) (Practical scoring tool)
- [Transaction Cost Economics](../../../theory/02-research/transaction-cost-economics.md) (Academic foundation)

---

## Exercises

### Exercise 1: Score Sample Deals

**Instructions:** For each deal below, score it on the four dimensions and classify as Bridge or Toaster.

#### Deal A: Marketing Automation Platform
- **Context:** Mid-market SaaS company wants to replace their email tool
- **Users:** Marketing team (12 people)
- **Integration:** Connects to Salesforce via standard API
- **Decision:** Marketing Director has budget authority
- **Implementation:** 2-week setup, templates provided

**Your Scores:**
- Tech Specificity: ___
- Org Specificity: ___
- Political Complexity: ___
- Retention Horizon: ___
- **Total Score:** ___
- **Classification:** [ ] Toaster [ ] Bridge
- **Reasoning:**

---

#### Deal B: Revenue Operations Platform
- **Context:** Enterprise company consolidating sales tools
- **Users:** Sales (50), Marketing (30), CS (20), Finance (5)
- **Integration:** Replaces 4 existing systems, custom data warehouse integration
- **Decision:** Requires CFO approval, IT security review, procurement process
- **Implementation:** 6-month rollout, requires workflow redesign across departments

**Your Scores:**
- Tech Specificity: ___
- Org Specificity: ___
- Political Complexity: ___
- Retention Horizon: ___
- **Total Score:** ___
- **Classification:** [ ] Toaster [ ] Bridge
- **Reasoning:**

---

#### Deal C: Analytics Dashboard
- **Context:** Startup wants better reporting
- **Users:** CEO + 3 executives
- **Integration:** Read-only API to existing database
- **Decision:** CEO can sign immediately
- **Implementation:** Self-service setup, 1 day

**Your Scores:**
- Tech Specificity: ___
- Org Specificity: ___
- Political Complexity: ___
- Retention Horizon: ___
- **Total Score:** ___
- **Classification:** [ ] Toaster [ ] Bridge
- **Reasoning:**

---

#### Deal D: Customer Success Platform (with a twist)
- **Context:** Mid-market company wants CS tool
- **Users:** CS team (8 people)
- **Integration:** Standard API to CRM
- **Decision:** VP Customer Success has budget
- **Implementation:** Standard 3-week onboarding
- **TWIST:** Prospect says "We'd like to run a 90-day pilot first to prove ROI"

**Your Scores:**
- Tech Specificity: ___
- Org Specificity: ___
- Political Complexity: ___
- Retention Horizon: ___
- **Total Score:** ___
- **Classification:** [ ] Toaster [ ] Bridge
- **Reasoning (include override rule consideration):**

---

#### Deal E: Core Infrastructure Platform
- **Context:** Enterprise replacing legacy ERP module
- **Users:** Operations (100+), Finance (20), IT (15)
- **Integration:** Deep integration with SAP, custom code required
- **Decision:** Board approval needed, 9-month procurement cycle
- **Implementation:** 18-month rollout, requires business process reengineering

**Your Scores:**
- Tech Specificity: ___
- Org Specificity: ___
- Political Complexity: ___
- Retention Horizon: ___
- **Total Score:** ___
- **Classification:** [ ] Toaster [ ] Bridge
- **Reasoning:**

---

### Exercise 2: The Autopsy

**Instructions:** Review a recent closed-lost deal from your pipeline. Answer these questions:

1. **What was the stated reason for the loss?** (e.g., price, timing, chose competitor)

2. **How did you classify the deal at the time?** (Bridge or Toaster)

3. **Knowing what you know now, was the classification correct?**

4. **If you misclassified it, what was the consequence?**
   - Toaster treated as Bridge: Wasted time on unnecessary complexity
   - Bridge treated as Toaster: Deal stalled due to unaddressed friction

5. **What would you do differently?**

---

## Assessment Criteria

### Knowledge Check (LLM will evaluate)

**Foundational Understanding:**
- Can you explain the difference between Bridge and Toaster in your own words?
- Can you define "asset specificity" and why it matters?

**Applied Understanding:**
- Can you correctly score deals using the diagnostic rubric?
- Can you identify when the override rule applies?

**Mastery:**
- Can you explain the economic rationale for why misclassification leads to deal failure?
- Can you diagnose past deals and identify classification errors?

### Progression Gate

To advance to Module 1, you must:
- Score all 5 sample deals with reasoning aligned to ILG principles
- Complete the autopsy exercise with specific, evidence-based insights
- Demonstrate understanding of when to apply the override rule

---

## LLM Tutor Prompts

**For the LLM facilitating this module:**

When a rep submits their deal scores:

1. **Check for accuracy** - Compare their scores to the answer key (below)
2. **Probe their reasoning** - Ask "Why did you score Tech Specificity as X?" 
3. **Challenge assumptions** - If they miss the override rule in Deal D, ask "What did the prospect say that should change your classification?"
4. **Use Socratic method** - Don't give answers, guide them to discover the right reasoning
5. **Maintain forensic tone** - Clinical analysis, not cheerleading

### Answer Key (For LLM Tutor Only)

- **Deal A:** Tech=3, Org=2, Political=1, Retention=3, Total=9 → **Toaster**
- **Deal B:** Tech=5, Org=5, Political=5, Retention=5, Total=20 → **Bridge**
- **Deal C:** Tech=1, Org=1, Political=1, Retention=2, Total=5 → **Toaster**
- **Deal D:** Tech=3, Org=2, Political=2, Retention=3, Total=10 → **Bridge** (borderline), BUT override rule also applies (pilot request) → **Bridge (20)**
- **Deal E:** Tech=5, Org=5, Political=5, Retention=5, Total=20 → **Bridge**

---

## Next Steps

Once you've completed this module:
- Move to [Module 1 - Economics of Fear](./module-1-economics-of-fear.md)
- Apply triage protocol to your current pipeline
- Use the [Deal Triage Calculator](../../01-field-assets/process-calculator.md) as a quick reference tool
