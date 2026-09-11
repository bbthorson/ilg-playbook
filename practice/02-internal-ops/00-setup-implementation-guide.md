---
title: 'TCG Implementation Guide: The "Installation Wizard"'
layer: practice
status: active
---

# TCG Implementation Guide: The "Installation Wizard"

Target Audience: Revenue Operations, Sales Enablement, VP Sales  
Goal: To calibrate the TCG framework to your specific product, market, and tech stack.

| | |
|---|---|
| **Inputs** | The generic [01-foundation/](../../theory/01-foundation) framework, plus your product's actual implementation reality. |
| **Outputs** | Calibrated triage thresholds, CRM lane fields, comp plan terms, manager review rituals — all tuned to your business. |
| **Cadence** | One-time setup; revisit annually. |
| **Owner** | RevOps + VP Sales (jointly). |
| **Prerequisite for** | Everything else in [02-internal-ops/](.) and the field assets in [01-field-assets/](../01-field-assets). |

## Phase 1: The Calibration Workshop

*You cannot use the Deal Triage Calculator out of the box. The counts are of your integration points, your veto holders, and your exception paths, and the bands converting them to component scores are chosen rather than fitted. Define what each count means for YOUR product before anyone scores a deal with it.*

Attendees: VP Sales, VP Customer Success, Lead Solutions Engineer, Product Marketing.  
Time: 90 Minutes.

### Step 1: Define the "Turnkey" vs. "Structural" Threshold

*Goal: Agree on the objective criteria that force a deal into the High-Friction lane.*

The calculator counts three things. This workshop decides what each of them means for your product, because "one integration point" is not self-evident and two reps will count it differently until someone rules.

| Count | What the workshop must settle | Worked example to replace |
|---|---|---|
| **Integration points** | What counts as one system exchanging data with yours. Does a read-only feed count? Does an identity provider? | *A browser-only product may genuinely count zero. An on-prem agent writing to an ERP counts that ERP, the agent's host, and every downstream consumer of the table it writes.* |
| **People who can say no** | The difference between an attendee and a veto. Name the titles in your market that actually hold one. | *A departmental buyer may have one. A cross-functional purchase touching finance and legal typically has four or more, plus a security review that is a body rather than a person.* |
| **Undocumented exception paths** | What evidence closes one. The rule is a written procedure with a volume attached. | *"Sales handles escalations case by case" is one open path, not zero, however confidently it is said.* |

**Action Item:** Replace the worked examples with your own product's, and write down the ruling for each edge case the room argues about. The arguments are the output. An unwritten ruling gets re-litigated on every deal.

> [!IMPORTANT]
> **Do not replace the counts with a 1-to-5 rating.** Every team that runs this workshop proposes it, because rating feels faster than counting. The models downstream raise their inputs to powers, and exponentiating an ordinal rating is not a defensible operation. More practically, a rating cannot be audited and a count can: a disputed rating is an argument about judgment, and a disputed count is an argument about whether a named system is on a list.

- *Output:* A customized version of the Deal Triage Calculator asset.

### Step 2: Define "The Hook" (The Reciprocity Gate)

*Goal: What is the ONE thing we need from a customer to prove they are serious?*

- **The Rule:** It must be hard enough to filter tire-kickers, but easy enough for a serious champion to provide.  
- **Examples:**  
  * *Data Company:* "A CSV export of your current schema."  
  * *Dev Tool:* "Read-access to a staging repo."  
  * *Marketing Tool:* "The last 3 months of campaign performance reports."  
- **Your Hook:** \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

## Phase 2: CRM Configuration (Salesforce/HubSpot)

*TCG fails if it isn't enforced in the CRM. Do not rely on spreadsheets.*

### 1\. The "Lane" Field

- **Field Name:** Deal\_Lane\_\_c  
- **Type:** Picklist  
- **Values:**  
  * Turnkey: Transactional (Auto-assign if Score \< 10\)  
  * Structural: Consultative (Auto-assign if Score \> 10\)

### 2\. The "Scorecard" Object

*Create a custom object or section on the Opportunity layout for the Bilateral Scorecard.*

- **Field:** Seller\_Clarity\_Score\_\_c (Number 0-15)  
- **Field:** Buyer\_Clarity\_Score\_\_c (Number 0-15)  
- **Field:** Asymmetry\_Gap\_\_c (Formula: Seller \+ Buyer)  
- **Validation Rule:** "Cannot move Stage to 'Negotiation' if Deal\_Archetype\_\_c \= 'Structural' AND Asymmetry\_Gap\_\_c \> 7."

> [!WARNING]
> **The formula is a sum, and an earlier version of this guide specified a difference.** `ABS(Seller - Buyer)` scores a deal where both sides are equally blind as zero, which reads as symmetric and therefore forecastable when it is the most dangerous deal on the board. The [Asymmetry Scorecard](./04-incentives-asymmetry-scorecard.md) corrected this and the CRM spec did not follow. If your org already built the field, the migration is to rebuild it as a sum and re-score the open pipeline, because every deal scored under the old formula is wrong in the same direction.

### 3\. The "Artifacts" Checkbox Group

- **Field:** TCG\_Artifacts\_\_c (Multi-Select Picklist)  
  * Blueprint Signed  
  * Red Team Completed  
  * MIP Drafted  
- **Validation Rule:** "Cannot move Stage to 'Closed Won' if Deal\_Archetype\_\_c \= 'Structural' AND MIP Drafted is NOT selected."

## Phase 3: Legal & Finance Alignment

*The "MIP" (Mutual Implementation Plan) often scares General Counsel. You must pre-clear it.*

### The "Non-Binding" Clause

- **Problem:** Legal fears the MIP creates a guaranteed outcome (warranty) that invites lawsuits.  
- **Solution:** Add this standard disclaimer to the MIP template:*"This Mutual Implementation Plan is a statement of shared intent and governance. While it outlines resource commitments, it does not supersede the Master Services Agreement (MSA) regarding liability or warranty."*

### The Vested Commission Wrapper

- **Problem:** Finance hates "Clawbacks" because they mess up ASC 606 revenue recognition and payroll processing.  
- **Solution:** Structure the comp plan as a "Retention Bonus" rather than a "Clawback."  
  * *Bad:* "We pay you $10k, then take back $10k if they churn." (Psychologically painful, accounting nightmare).  
  * *Good:* "We pay you $5k on signature. We pay you a $5k 'Quality Bonus' at Day 90 if adoption \> 10%." (Psychologically rewarding, cleaner accounting).

## Phase 4: The Rollout Script (Change Management)

*How to announce this to a skeptical sales team without causing a mutiny.*

**The Narrative:** "We are not adding process. We are removing failure."

1. **Week 1: The Audit.** (Show the Standish Group data). "We are losing 40% of deals to 'No Decision.' That is money you already earned but didn't get paid on."  
2. **Week 2: The Pilot.** Select 2 senior reps (Opinion Leaders). Have them use the Red Team Protocol on a stalled deal.  
3. **Week 3: The Win.** Broadcast the result. "Sarah used the Red Team Protocol and unstalled the Acme Corp deal. It closed in 14 days."  
4. **Week 4: The Standard.** Roll out the Deal Triage Calculator. Make it mandatory for deals \> $50k.

## Phase 5: The "Break Glass" Procedure

*When to ignore the rules.*

Scenario: A strategic logo (Fortune 500\) wants to buy now (End of Quarter) but refuses the Red Team.  
The Protocol:

1. **CEO Approval Required.** Only the CEO can waive the Red Team for a Structural deal.  
2. **The "Risk Letter":** The CEO writes a side-letter to the Customer Sponsor: *"We are skipping our standard validation process at your request to meet your timeline. This increases implementation risk. We require a dedicated Executive Sponsor meeting in Week 2 to mitigate this."*