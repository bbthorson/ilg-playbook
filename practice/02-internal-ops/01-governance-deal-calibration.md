# Deal Calibration Sheet (The Manager's View)

Type: Internal Ops / Forecast  
Owner: VP Sales / CRO  
Goal: To calibrate the "Commit" forecast based on Friction, not Hope.

| | |
|---|---|
| **Inputs** | Rep's pipeline of Bridge deals; artifact status (Blueprint / Red Team / MIP). |
| **Outputs** | Forecast verdict (Commit / Best Case / Pipeline) per deal, grounded in friction completed. |
| **Cadence** | Weekly forecast call. |
| **Owner** | Sales manager / VP Sales. |
| **Cross-ref** | Use the [Asymmetry Scorecard](./04-incentives-asymmetry-scorecard.md) as a sub-check; deeper forensic review uses the [Deal Review Checklist](./02-governance-review-checklist.md). |

## The Classification Check

*First, validate the Lane.*

- **Deal Name:** \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_  
- **Lane:** \[ \] Lane 1 (Toaster) / \[ \] Lane 2 (Bridge)  
- **Manager Challenge:** "Why is this a Bridge? Show me the Risk Calculator score." (Score: \_\_\_\_)

## The Friction Audit (For Bridge Deals Only)

*Do not ask 'When will it close?' Ask 'Have we done the work?'*

| Phase | The Artifact | The Manager's Question | Status (R/Y/G) |
| :---- | :---- | :---- | :---- |
| **Why** | **Contextual Blueprint** | "Did they agree to the Technical Hook (Data Access)?" | \[ \] |
| **What** | **Red Team Workshop** | "Did we find a failure mode, or was it a 'Happy Ears' demo?" | \[ \] |
| **How** | **MIP (Governance)** | "Is the resource plan attached to the contract?" | \[ \] |

## The "No Decision" Risk Analysis

*If the deal slips, it will be because of one of these three variables.*

1. **Valuation Risk (**$V\_{solution}$**):** Is the ROI too fuzzy? Is the buyer's $V_{next\_best}$ (build in-house, workaround, market withdrawal) more attractive?
   * *Fix:* Tighten the "Cost of Inaction" and "Decision Alternatives" sections in the Blueprint.
2. **Friction Risk (**$F\_{base}$**):** Is the work too scary?
   * *Fix:* Deploy a "Concierge Onboarding" offer in the MIP to lower perceived effort.
3. **Asymmetry Risk (**$\Delta\_A$**):** Do they not trust us ($I_{buyer}$ high), or do we not understand them ($I_{seller}$ high)?
   * *Fix for $I_{buyer}$:* Offer a "Paid Pilot" (Costly Signal) to prove intent.
   * *Fix for $I_{seller}$:* Deeper discovery — revisit Blueprint, map workflows you missed.

## The Forecast Verdict

- **Commit:** All Artifacts Green \+ $\Delta_A$ below 4.0 (sum of $I_{seller}$ and $I_{buyer}$ on the [Asymmetry Scorecard](./04-incentives-asymmetry-scorecard.md), range 2–10).  
- **Best Case:** Artifacts in progress.  
- **Pipeline:** Blueprint not signed.

**Manager's Oath:** "I will not commit a Bridge deal that has not survived a Red Team Workshop."