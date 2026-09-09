# Module 0: Triage Protocol

**Learning Time:** 1 hour  
**Prerequisites:** None (start here)

---

## Learning Objectives

By the end of this module, you will be able to:

1. **Classify deals** as **Structural** (high friction/specificity, $k \ge 10$) or **Turnkey** (low friction, $k \le 9$) using the diagnostic rubric.
2. **Score deals** accurately on integration depth, workflow change scope, consensus complexity, and retention horizon.
3. **Apply the decision matrix** to determine the appropriate sales motion (ILG vs. SLG/PLG).
4. **Identify override conditions** (pilot/POC requests that trigger structural governance).

---

## Key Concepts

### The 2x2 Deal Archetype Matrix

The sales motion must match the deal's transaction cost and market legibility profile:

| | Low Specificity ($k \le 9$) | High Specificity ($k \ge 10$) |
|---|---|---|
| **Mature / High Competition** | **Turnkey Deal (PLG Motion)**<br>Modular tools, standard APIs, low switching cost. Optimize for velocity and frictionless purchase. | **Structural Deal (ILG Motion)**<br>Deep ERP/EHR integration, multi-stakeholder consensus. Optimize for implementation safety and certainty. |
| **Nascent / Low Competition** | **Evangelism Deal (SLG Motion)**<br>Category unformed, low awareness. Educate the market, create the line item. | **Strategic Co-Development / Chaos Trap**<br>High custom build. If process is uncodified $\to$ Chaos Trap (route to consulting). |

### Pre-Qualification: The Workflow Maturity Gate

Before scoring, answer one binary question: **Does a documented SOP exist for this problem today?**

- **YES** → Proceed to scoring.
- **NO** → **STOP.** This is the **Chaos Trap** (High Specificity + Undefined Workflow). Redirect to Consulting first.

### The Diagnostic Rubric (Score 1–5 each)

1. **Integration Depth ($F_{implementation}$):** 1 = Standalone tool $\to$ 3 = Standard API $\to$ 5 = Deep ERP/core rewrite
2. **Workflow Change Scope ($F_{implementation}$):** 1 = Single team, no process change $\to$ 3 = Single department $\to$ 5 = Cross-functional overhaul
3. **Consensus Complexity ($F_{consensus}$):** 1 = Single decision maker $\to$ 3 = Committee (3–4) $\to$ 5 = Board/InfoSec/Procurement
4. **Retention Horizon (Sustained $F_{implementation}$):** 1 = One-time project $\to$ 3 = Annual contract $\to$ 5 = Multi-year platform dependency

### The Decision Matrix

- **Score 4–9:** Lane 1 (Turnkey) → Use PLG/velocity motion
- **Score 10–20:** Lane 2 (Structural) → Deploy ILG motion
- **Override Rule:** If prospect asks for a "Pilot" or "POC," immediately upgrade to Structural (score 20).

---

## Why This Matters

**From the ILG Constitution (Axiom I — Law of Transaction Cost Composition):**

> "Never apply a Turnkey motion to a Structural deal, and never sell a Structural deal without a Blueprint."

When asset specificity is high (Structural deals), transaction costs explode due to implementation effort, consensus coordination, and information asymmetry. Misclassifying a Structural deal as Turnkey leads directly to stalled deals ("no decision"), failed rollouts, and early churn.

---

## Exercise: Score Sample Deals

Evaluate the following 5 pipeline opportunities using the rubric:

| Deal | Context & Scope | Integration & Decision Path | Rubric Scores (1–5)<br>Int / Wf / Cons / Ret | Total & Classification |
|---|---|---|---|---|
| **A: Marketing Email Tool** | Replacing email tool for 12 marketers; 2-week setup with templates. | Standard Salesforce API; Marketing Director has sole budget authority. | 3 / 2 / 1 / 3 | **9 $\to$ Turnkey Deal (PLG)** |
| **B: RevOps Consolidation** | Consolidating tools across Sales (50), Mktg (30), CS (20), Finance (5); 6-mo rollout. | Replaces 4 systems; custom data warehouse sync; requires CFO + InfoSec + Procurement. | 5 / 5 / 5 / 5 | **20 $\to$ Structural Deal (ILG)** |
| **C: Exec Analytics Dashboard** | Startup CEO + 3 execs want better reporting; 1-day self-serve onboarding. | Read-only API to existing database; CEO signs immediately. | 1 / 1 / 1 / 2 | **5 $\to$ Turnkey Deal (PLG)** |
| **D: CS Platform (+ Pilot Ask)** | CS tool for 8 users; standard 3-week onboarding; prospect asks for 90-day pilot. | Standard CRM API; VP CS has budget; *pilot requested*. | 3 / 2 / 2 / 3<br>*(Pilot override)* | **10 (Base) $\to$ 20 (Override)<br>Structural Deal (ILG)** |
| **E: Core Infrastructure** | Replacing legacy SAP ERP module across 100+ ops users; 18-month rollout. | Custom code + deep ERP integration; Board approval needed; 9-month procurement. | 5 / 5 / 5 / 5 | **20 $\to$ Structural Deal (ILG)** |

---

## The Deal Autopsy

Review a recent closed-lost deal from your pipeline:
1. What was the stated reason for the loss?
2. Did you treat it as Turnkey (velocity) or Structural (governance)?
3. If misclassified: did you over-friction a Turnkey deal (scared them off), or under-friction a Structural deal (stalled due to unaddressed risk)?

---

## Next Steps

- Move to [Module 1 - Economics of Fear](./module-1-economics-of-fear.md)
- Reference the operational [Deal Triage Calculator](../../01-field-assets/process-calculator.md) on live calls.
