# **ILG Implementation Guide: The "Installation Wizard"**

Target Audience: Revenue Operations, Sales Enablement, VP Sales  
Goal: To calibrate the ILG framework to your specific product, market, and tech stack.

## **Phase 1: The Calibration Workshop**

*You cannot use the "Risk Calculator" out of the box. A generic score of "5" means nothing. You must define what "High Friction" looks like for YOUR product.*

Attendees: VP Sales, VP Customer Success, Lead Solutions Engineer, Product Marketing.  
Time: 90 Minutes.

### **Step 1: Define the "Toaster" vs. "Bridge" Threshold**

*Goal: Agree on the objective criteria that force a deal into the High-Friction lane.*

| Factor | Score 1 (Toaster / PLG) | Score 3 (Standard / SLG) | Score 5 (Bridge / ILG) |
| :---- | :---- | :---- | :---- |
| **Tech Specificity** | *Example: No code, browser-based only.* | *Example: Standard API (Salesforce, Slack).* | *Example: Requires on-prem agent, custom SQL, or ERP write-access.* |
| **Org Specificity** | *Example: Single user or single team.* | *Example: Departmental (Sales Only).* | *Example: Cross-functional (Sales \+ Finance \+ Legal).* |
| **Political Complexity** | *Example: Credit card swipe.* | *Example: Manager approval.* | *Example: InfoSec Review \+ CFO Sign-off.* |

**Action Item:** Replace the generic examples above with your specific product features/integrations.

* *Output:* A customized version of the Process Calculator asset.

### **Step 2: Define "The Hook" (The Reciprocity Gate)**

*Goal: What is the ONE thing we need from a customer to prove they are serious?*

* **The Rule:** It must be hard enough to filter tire-kickers, but easy enough for a serious champion to provide.  
* **Examples:**  
  * *Data Company:* "A CSV export of your current schema."  
  * *Dev Tool:* "Read-access to a staging repo."  
  * *Marketing Tool:* "The last 3 months of campaign performance reports."  
* **Your Hook:** \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

## **Phase 2: CRM Configuration (Salesforce/HubSpot)**

*ILG fails if it isn't enforced in the CRM. Do not rely on spreadsheets.*

### **1\. The "Lane" Field**

* **Field Name:** Deal\_Lane\_\_c  
* **Type:** Picklist  
* **Values:**  
  * Lane 1: Transactional (Auto-assign if Score \< 10\)  
  * Lane 2: Consultative (Auto-assign if Score \> 10\)

### **2\. The "Scorecard" Object**

*Create a custom object or section on the Opportunity layout for the Bilateral Scorecard.*

* **Field:** Seller\_Clarity\_Score\_\_c (Number 0-15)  
* **Field:** Buyer\_Clarity\_Score\_\_c (Number 0-15)  
* **Field:** Asymmetry\_Delta\_\_c (Formula: ABS(Seller \- Buyer))  
* **Validation Rule:** "Cannot move Stage to 'Negotiation' if Deal\_Lane\_\_c \= 'Lane 2' AND Asymmetry\_Delta\_\_c \> 3."

### **3\. The "Artifacts" Checkbox Group**

* **Field:** ILG\_Artifacts\_\_c (Multi-Select Picklist)  
  * Blueprint Signed  
  * Red Team Completed  
  * MIP Drafted  
* **Validation Rule:** "Cannot move Stage to 'Closed Won' if Deal\_Lane\_\_c \= 'Lane 2' AND MIP Drafted is NOT selected."

## **Phase 3: Legal & Finance Alignment**

*The "MIP" (Mutual Implementation Plan) often scares General Counsel. You must pre-clear it.*

### **The "Non-Binding" Clause**

* **Problem:** Legal fears the MIP creates a guaranteed outcome (warranty) that invites lawsuits.  
* **Solution:** Add this standard disclaimer to the MIP template:*"This Mutual Implementation Plan is a statement of shared intent and governance. While it outlines resource commitments, it does not supersede the Master Services Agreement (MSA) regarding liability or warranty."*

### **The Vested Commission Wrapper**

* **Problem:** Finance hates "Clawbacks" because they mess up ASC 606 revenue recognition and payroll processing.  
* **Solution:** Structure the comp plan as a "Retention Bonus" rather than a "Clawback."  
  * *Bad:* "We pay you $10k, then take back $10k if they churn." (Psychologically painful, accounting nightmare).  
  * *Good:* "We pay you $5k on signature. We pay you a $5k 'Quality Bonus' at Day 90 if adoption \> 10%." (Psychologically rewarding, cleaner accounting).

## **Phase 4: The Rollout Script (Change Management)**

*How to announce this to a skeptical sales team without causing a mutiny.*

**The Narrative:** "We are not adding process. We are removing failure."

1. **Week 1: The Audit.** (Show the Standish Group data). "We are losing 40% of deals to 'No Decision.' That is money you already earned but didn't get paid on."  
2. **Week 2: The Pilot.** Select 2 senior reps (Opinion Leaders). Have them use the Red Team Protocol on a stalled deal.  
3. **Week 3: The Win.** Broadcast the result. "Sarah used the Red Team Protocol and unstalled the Acme Corp deal. It closed in 14 days."  
4. **Week 4: The Standard.** Roll out the Process Calculator. Make it mandatory for deals \> $50k.

## **Phase 5: The "Break Glass" Procedure**

*When to ignore the rules.*

Scenario: A strategic logo (Fortune 500\) wants to buy now (End of Quarter) but refuses the Red Team.  
The Protocol:

1. **CEO Approval Required.** Only the CEO can waive the Red Team for a Lane 2 deal.  
2. **The "Risk Letter":** The CEO writes a side-letter to the Customer Sponsor: *"We are skipping our standard validation process at your request to meet your timeline. This increases implementation risk. We require a dedicated Executive Sponsor meeting in Week 2 to mitigate this."*