# Prospect Evaluation Form

> **Status:** DRAFT — inferred from [01-velocity-standard-order-protocol.md](./01-velocity-standard-order-protocol.md) Step 2. Review and ratify before deploying.

**Purpose:** A 2-minute "Fit Check" the rep completes *before* sending the [Standard Order Form](./order-form.md). Catches Bridges-in-disguise so they don't slip through the velocity motion.

**When to use:** After triage scores < 10 on the [process calculator](../process-calculator.md), and the prospect has not asked for a Pilot, POC, or Custom Security Review.

---

## Deal context

- **Prospect company:** _____________________
- **Primary contact (name, title):** _____________________
- **Deal value (ACV):** _____________________
- **Process Calculator score:** _____  (must be < 10)
- **Date evaluated:** _____________________
- **Rep:** _____________________

---

## 1. Technical Fit

- [ ] Prospect uses a standard tech stack (e.g., Salesforce, Slack, Google Workspace, M365)
- [ ] No requirement for on-premise agents or custom APIs
- [ ] No requirement for SSO, SCIM, or custom IAM beyond what's in the standard tier
- [ ] No PHI / regulated-data path that triggers BAA or HIPAA review

**If any box unchecked:** Technical Fit = NO. **Abort velocity motion.** Re-classify as Bridge.

---

## 2. User Proficiency

- [ ] User has admin rights on their environment, or can self-provision
- [ ] User has successfully tested the Free Tier / Trial (if applicable)
- [ ] User has read or can self-serve the onboarding documentation

---

## 3. The "Karen" Check (Behavioral Risk)

Prospect has reasonable expectations for support:

- [ ] OK with chat / email support (no dedicated CSM)
- [ ] OK with self-serve onboarding (no implementation consultant)
- [ ] No request for dedicated phone line, named TAM, or executive sponsor

> **Red flag:** If the prospect asked for a dedicated phone number, named CSM, or quarterly business review, this is **not a Toaster**. DQ from velocity motion or **upsell to Enterprise tier**.

---

## 4. Verdict

- [ ] **GREEN** — All three sections pass. Proceed to [Standard Order Form](./order-form.md).
- [ ] **YELLOW** — User Proficiency soft (will need extra hand-holding). Proceed but flag CS.
- [ ] **RED** — Technical Fit or Karen Check failed. **Abort.** Either disqualify or escalate to Bridge motion ([Contextual Blueprint](../ilg-motion/01-discovery-contextual-blueprint.md)).

**Rep signature / date:** _____________________

---

## Related

- [01-velocity-standard-order-protocol.md](./01-velocity-standard-order-protocol.md) — Parent protocol; defines when this form is used.
- [order-form.md](./order-form.md) — The external contract that follows a GREEN verdict.
- [../process-calculator.md](../process-calculator.md) — Upstream triage gate.
