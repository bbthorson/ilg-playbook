# The Deal Triage Calculator

Version: 3.0
Audience: Internal Rep / Pre-Sales
Goal: To determine if a deal needs the "Heavy" Bridge (ILG) or the "Lite" Toaster (SLG/PLG) motion.

**Canonical Reference:** [ILG Constitution, Part IV](../00-foundation/ilg-constitution.md)

---

## Step 1: The Workflow Maturity Gate (Pre-Qualification)

**Before scoring, answer this binary question:**

### Does a documented standard operating procedure (SOP) exist for this problem today?

- [ ] **YES** — A documented workflow exists (written process, documented steps, known sequence of activities). → Proceed to Step 2.
- [ ] **NO** — The workflow is undefined, ad-hoc, or varies by person/team. → **STOP.**

**If NO:** This is the **Chaos Trap** (High Specificity + Undefined Workflow). You cannot digitize chaos. Redirect to **Consulting/Paid Workshop** to define the SOP first. The prospect must graduate from Consulting → ILG.

---

## Step 2: Score the Four Factors (1-5 each)

### 1. Technical Specificity (How deep is the hook?)

- **1:** Standalone tool. No integration needed.
- **3:** Standard API integration (Salesforce/Slack).
- **5:** Deep ERP/Core Infrastructure rewrite. Custom code required.
- **Score:** _____

### 2. Organizational Specificity (How many habits change?)

- **1:** Single team (<5 users). No process change.
- **3:** Single Department (Sales/Marketing). Minor process tweak.
- **5:** Cross-Functional (Sales + Finance + Ops). Total workflow overhaul.
- **Score:** _____

### 3. Political Complexity (Who can say no?)

- **1:** Single Decision Maker.
- **3:** Committee (3-4 stakeholders).
- **5:** Board Approval / Procurement / Security Audit required.
- **Score:** _____

### 4. Retention Horizon (One-shot or repeat game?)

- **1:** One-time project, no renewal expected.
- **3:** Annual contract, moderate switching cost.
- **5:** Multi-year platform, deep dependency, high switching cost.
- **Score:** _____

---

## Step 3: Interpret the Result

**Total Score (4-20):** _________

- **4-9 (The Toaster):**
  * **Action:** Go Fast.
  * **Asset:** Standard Demo + Order Form.
  * **Focus:** Speed & Price.
- **10-20 (The Bridge):**
  * **Action:** Slow Down.
  * **Asset:** Deploy Contextual Blueprint.
  * **Focus:** Risk Mitigation.

**Override Rule:** If the prospect asks for a "Pilot" or "Proof of Concept," immediately upgrade the score to **20** (Bridge). Pilots are strictly governed by the Red Team Protocol.
