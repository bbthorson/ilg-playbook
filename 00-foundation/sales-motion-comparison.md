# Sales Motion Comparison: ILG vs. PLG vs. SLG

**A framework for choosing the right sales motion based on deal characteristics.**

---

## Quick Reference Matrix

| Dimension | **ILG (Implementation-Led)** | **PLG (Product-Led)** | **SLG (Sales-Led)** |
|-----------|------------------------------|----------------------|---------------------|
| **Deal Type** | The Bridge | The Toaster | The Pitch |
| **Friction Profile** | High (10-20) | Low (4-9) | Medium (6-12) |
| **Optimization Goal** | Safety & Certainty | Velocity & Volume | Efficiency & Coverage |
| **Primary Metric** | NRR, Adoption | User Growth, Activation | Win Rate, Pipeline Velocity |
| **Sales Cycle** | 3-9 months | Self-service (days) | 1-3 months |
| **ACV Range** | $100k-$1M+ | $0-$50k | $25k-$250k |
| **Decision Makers** | 3-10+ stakeholders | 1-2 (end user + manager) | 2-5 stakeholders |
| **Integration Complexity** | Deep (ERP, core systems) | Lightweight (API, SSO) | Moderate (standard integrations) |
| **Change Management** | High (cross-functional) | Low (single team) | Medium (departmental) |

---

## The Bridge Taxonomy: Friction × Asset Specificity

The sales motion is determined by two axes: **Friction** (how hard is the buying/implementation process?) and **Asset Specificity** (how deeply embedded does the solution become?).

| | **Low Asset Specificity** | **High Asset Specificity** |
|---|---|---|
| **Low Friction** | **PLG** — Slack, Figma, Notion. Self-serve trial → buy. Low switching cost. The product sells itself. | **Open Infrastructure** — Kubernetes, Postgres, Terraform. Community-driven adoption, but architecture becomes deeply dependent. High switching cost hidden inside low sales friction. |
| **High Friction** | **SLG** — The seller must *create the market*. Heavy buyer education (they can't describe the problem). Complex procurement, but the buyer isn't locked in — they could switch, build in-house, or revert. **Friction is educational.** | **ILG** — "The Bridge." EHR, ERP, Security platforms. Both the sales process AND the asset create deep dependency. Cross-functional impact, multi-stakeholder consensus, deep integration. **Friction is structural.** |

**Key distinction between SLG and ILG friction:**

- **SLG friction is educational** — the sales rep is teaching the buyer *that they have a problem* and *what a solution category looks like*. The friction is cognitive. Once they understand, switching to a competitor is relatively easy because the asset specificity is low.
- **ILG friction is structural** — the buyer already knows they have a problem. The friction comes from the *implementation itself*: integration depth, data migration, workflow rewiring, multi-stakeholder consensus. The friction is organizational.

**This matters because:**
- SLG reps need to be *educators* (Challenger-style commercial teaching)
- ILG reps need to be *implementation scientists* (CFIR diagnostic model)
- Applying ILG tactics to an SLG deal over-engineers it
- Applying SLG tactics to an ILG deal under-prepares the buyer

---

## Detailed Comparison

### When to Use Each Motion

#### ILG (Implementation-Led Growth)
**Use When:**
- High asset specificity (hard to rip out)
- Cross-functional impact (multiple departments)
- Complex stakeholder dynamics (>3 decision makers)
- Deep workflow integration required
- High switching costs
- Customer asks for pilot/POC

**Examples:**
- Revenue operations platforms
- ERP modules
- Core infrastructure replacements
- Enterprise data platforms

---

#### PLG (Product-Led Growth)
**Use When:**
- Low asset specificity (easy to adopt/remove)
- Single team or department
- Simple decision-making (1-2 people)
- Standalone tool (minimal integration)
- Low switching costs
- Self-service viable

**Examples:**
- Collaboration tools (Slack, Notion)
- Analytics dashboards
- Marketing automation (simple)
- Developer tools

---

#### SLG (Sales-Led Growth)
**Use When:**
- Medium complexity
- Departmental impact (not cross-functional)
- Standard integrations
- Moderate stakeholder count (2-5)
- Value can be demonstrated in demo
- Budget authority clear

**Examples:**
- CRM systems
- Sales enablement tools
- Standard SaaS applications
- Departmental software

---

## Strategic Approach by Motion

### ILG: Optimize for Safety

**Philosophy:** "The goal is not to close deals faster. The goal is to close deals that stick."

**Key Activities:**
1. **Contextual Blueprint** - Map politics, economics, sacred cows
2. **Red Team Workshop** - Surface resistance, validate feasibility
3. **Mutual Implementation Plan** - Governance structure, shared accountability

**Success Criteria:**
- Information asymmetry ($I_A$) → 0
- Saboteur identified and contained
- Realistic expectations set
- Resources committed

**Failure Mode:**
- Treating a Bridge like a Toaster → Deal stalls due to unaddressed friction

---

### PLG: Optimize for Velocity

**Philosophy:** "Let the product sell itself. Remove all friction from trial to purchase."

**Key Activities:**
1. Self-service signup
2. Automated onboarding
3. In-product activation
4. Usage-based expansion

**Success Criteria:**
- Fast time-to-value
- High activation rate
- Low CAC
- Viral growth

**Failure Mode:**
- Treating a Toaster like a Bridge → Waste time on unnecessary complexity

---

### SLG: Optimize for Efficiency

**Philosophy:** "Demonstrate value, handle objections, close the deal."

**Key Activities:**
1. Discovery call
2. Product demo
3. Proposal/pricing
4. Negotiation
5. Close

**Success Criteria:**
- Clear ROI demonstrated
- Objections handled
- Budget secured
- Decision maker engaged

**Failure Mode:**
- Using on high-friction deals → Fails to address political/implementation complexity

---

## Economic Model Comparison

### Cost Structure

| | **ILG** | **PLG** | **SLG** |
|---|---------|---------|---------|
| **CAC** | High ($20k-$100k+) | Low ($100-$5k) | Medium ($5k-$25k) |
| **Sales Cycle** | Long (3-9 months) | Instant (self-service) | Medium (1-3 months) |
| **Rep Involvement** | High (consultative) | Low (CS-led expansion) | Medium (demo + close) |
| **Implementation Cost** | High (6-12 months) | Low (self-service) | Medium (3-6 months) |
| **Churn Risk** | Low (if done right) | Medium-High | Medium |
| **NRR Target** | 120-150%+ | 100-120% | 100-110% |

---

### Revenue Model

#### ILG
- **Upfront:** Large ACV ($100k-$1M+)
- **Expansion:** High (successful implementation → expansion)
- **Retention:** Very high (deep integration, high switching costs)
- **Payback:** 12-24 months (but very sticky)

#### PLG
- **Upfront:** Low/Free (freemium or trial)
- **Expansion:** Usage-based, land-and-expand
- **Retention:** Variable (easy to churn)
- **Payback:** 3-6 months (low CAC)

#### SLG
- **Upfront:** Medium ACV ($25k-$250k)
- **Expansion:** Moderate (seat-based, feature upgrades)
- **Retention:** Medium (moderate switching costs)
- **Payback:** 6-12 months

---

## Transaction Cost Analysis

### ILG (High Transaction Costs)

$$TC_{total} = (TC_{search} + TC_{consensus} + TC_{implementation}) \times (1 + |I_A|)$$

**Where costs are high:**
- **Search:** Complex requirements, many stakeholders
- **Consensus:** Political dynamics, competing interests
- **Implementation:** Deep integration, change management
- **$I_A$ Multiplier:** Fear of failure amplifies all costs

**ILG Strategy:** Systematically reduce each cost through artifacts
- Blueprint → Reduces search costs (clarity on fit)
- Red Team → Reduces consensus costs (surface resistance)
- MIP → Reduces implementation costs (governance + resources)
- All three → Drive $I_A \to 0$ (reduce fear multiplier)

---

### PLG (Low Transaction Costs)

**Where costs are low:**
- **Search:** Self-service, clear value prop
- **Consensus:** Single user or small team
- **Implementation:** Plug-and-play, no integration
- **$I_A$ Multiplier:** Low risk (easy to try, easy to leave)

**PLG Strategy:** Remove all friction
- Free trial (no search cost)
- Self-service (no consensus needed)
- Instant activation (no implementation effort)

---

### SLG (Medium Transaction Costs)

**Where costs are moderate:**
- **Search:** Demo-driven, clear use cases
- **Consensus:** Departmental buy-in needed
- **Implementation:** Standard onboarding
- **$I_A$ Multiplier:** Moderate (some risk, but proven category)

**SLG Strategy:** Demonstrate value, handle objections
- ROI calculator (reduce search cost)
- Reference calls (reduce fear)
- Standard implementation (predictable effort)

---

## Compensation Alignment

### ILG: Vested Commission
- **Structure:** 100% commission on signature, subject to clawback
- **Clawback Trigger:** Failed implementation (<10% adoption by Day 90)
- **NRR Bonus:** % of expansion revenue
- **Alignment:** Rep incentivized to tell truth, ensure successful start

### PLG: CS-Led Expansion
- **Structure:** Low/no commission on initial signup
- **Expansion Commission:** % of upsell/cross-sell
- **Alignment:** CS team drives expansion through product value

### SLG: Traditional Commission
- **Structure:** % of ACV on signature
- **Alignment:** Rep incentivized to close, but not necessarily to ensure success
- **Risk:** Principal-agent misalignment (rep paid for signature, customer pays for outcome)

---

## When Each Motion Fails

### ILG Fails When:
- ❌ Applied to a Toaster (wastes time on low-friction deal)
- ❌ Rep skips reciprocity gates (customer not serious)
- ❌ Red Team is "happy ears" (no real validation)
- ❌ MIP has no customer resources (all risk on vendor)

### PLG Fails When:
- ❌ Applied to a Bridge (ignores political/implementation complexity)
- ❌ Product requires expert setup (not self-service)
- ❌ Value not immediately obvious (long time-to-value)
- ❌ Enterprise security/compliance required

### SLG Fails When:
- ❌ Applied to high-friction Bridge (doesn't address implementation risk)
- ❌ Applied to simple Toaster (too much sales overhead)
- ❌ Rep focuses on features, not business outcomes
- ❌ Implementation complexity hidden (churn at renewal)

---

## Hybrid Approaches

### PLG → ILG (Land and Expand)
- Start with PLG motion (individual/team trial)
- Trigger ILG motion when enterprise expansion (cross-functional, complex)
- Example: Slack (PLG for teams, ILG for enterprise rollout)

### SLG → ILG (Complexity Discovery)
- Start with SLG motion (standard demo/proposal)
- Discover high friction during discovery
- Pivot to ILG motion (deploy Blueprint, Red Team, MIP)

---

## Decision Framework

### Step 0: Pre-Qualification (Workflow Maturity Gate)
Does a documented SOP exist? If NO → **Chaos Trap** → Redirect to Consulting.

### Step 1: Triage (Use [Deal Triage Calculator](../03-field-assets/process-calculator.md))
Score the deal on 4 factors (1-5 each):
1. Tech Specificity
2. Org Specificity
3. Political Complexity
4. Retention Horizon

### Step 2: Apply Decision Matrix
- **Score 4-9:** PLG/SLG (optimize for velocity)
- **Score 10-20:** ILG (optimize for safety)

### Step 3: Override Rules
- If prospect asks for pilot/POC → ILG (score 20)
- If self-service viable → PLG
- If standard enterprise sale → SLG

---

## Key Principle

**From ILG Constitution (Axiom I):**

> "Never apply a Bridge motion to a Toaster, and never sell a Bridge without a Blueprint."

**The Corollary:**

- Don't use ILG on PLG deals (wastes time)
- Don't use PLG on ILG deals (ignores friction)
- Don't use SLG on ILG deals (hides complexity)

**Match the motion to the friction profile.**

---

**Remember:** The motion is not about your preference. It's about the deal's physics.
