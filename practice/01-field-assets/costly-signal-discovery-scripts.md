# Costly Signal Discovery Scripts

**Purpose:** To supply the specific asks that convert a buyer's stated interest into evidenced commitment, and to read what the response tells you about the deal.

**Use when:** Running Blueprint discovery on a Bridge deal, or at any point where a buyer's enthusiasm is outrunning their investment.

**Operationalizes:** Axiom II. The Single Crossing Property says a signal separates quality only when it costs more to fake than to produce honestly. These scripts produce that cost on the buyer's side.

---

## The premise

Discovery is usually treated as information gathering. On a Bridge, the request itself is the instrument.

A buyer who is genuinely committed can produce a data sample, convene three departments, and name a project manager, because those things are cheap for them relative to the value they expect. A buyer who is gathering options to satisfy a procurement requirement finds the same requests expensive, because the value they expect is close to zero. The ask separates them, and it does so before the seller has spent months on a deal that was never real.

This is why the response matters more than the answer. The buyer's words describe their intent. What they actually hand over describes their commitment.

**The reciprocity rule.** Friction Allocation Principle 2 requires the claimant to bear the cost of their own signal. A seller who demands buyer investment while offering none has misallocated the friction, and the request reads as qualification theatre. Every ask below pairs with something the seller commits in the same conversation. Pair them explicitly and out loud.

---

## The ladder

Asks escalate in cost. Run them in order, because a buyer who fails an early rung will fail the later ones more expensively.

| Rung | Ask | Buyer cost | Seller pairs with |
|---|---|---|---|
| **1** | A current-state artifact they already have | Minutes | A reference architecture for their stack |
| **2** | A production data sample under NDA | Legal and security review | A written gap analysis against that sample |
| **3** | Ninety minutes from three named departments | Coordination across silos | Senior solutions engineering time in the room |
| **4** | Access to a practitioner who does the work today | Operational disruption | A workflow map returned to them, theirs to keep |
| **5** | A named project manager with committed hours | Budgeted headcount | Named delivery resources and an escalation path |
| **6** | Paid diagnostic or pilot | Real money, internal approval | Fixed scope, fixed price, defined exit |

Rungs 1 through 3 belong in Blueprint discovery. Rungs 4 and 5 gate the Red Team and the MIP. Rung 6 applies when the buyer requests a pilot, which under the Process Calculator override already classifies the deal as a Bridge.

---

## Scripts

### Rung 1 and 2: artifacts and data

> "Before I bring our architect in, I want them working from your reality rather than a generic diagram. Can you send whatever you have that describes the current process, even if it is out of date? Out of date is useful, because the gap between the document and what people actually do is usually where the implementation risk lives."

> "I would rather find the ugly parts of the data now than in month three. If you can get us a sample under NDA, we will return a written gap analysis: what we can handle, what needs transformation, and what we cannot do at all. You keep that document either way."

**What you are testing.** Whether anyone can locate the artifact, and whether security review is a two-week path or a two-month one. The second answer is a direct read on $F_{consensus}$ that no amount of asking about the buying process will give you.

### Rung 3: cross-departmental attendance

> "The failure mode I have seen most often is that we align perfectly with the team who owns the problem, and then discover in month two that the team who owns the system has a different roadmap. I would like ninety minutes with both, plus whoever owns security. I will bring our principal engineer. If we cannot get those three in a room now, that tells us both something about what implementation will look like."

**What you are testing.** Convening power. A champion who cannot convene three departments for ninety minutes before a purchase will not convene them for a rollout after one. This is the single most predictive ask on the ladder.

### Rung 4: practitioner access

> "Can I spend an hour with someone who actually does this work today? Not to sell them anything. I want to watch the workarounds, because the workarounds are the requirements nobody writes down."

**What you are testing.** Whether the buyer's described process matches the practiced one, which is exactly the Level 2 workflow maturity trap in the [Process Calculator](./process-calculator.md).

### Rung 5: named resources

> "We can commit a named implementation lead and a defined escalation path. What I need in exchange is a named project manager on your side with hours actually allocated, not borrowed. If those hours are not available until next quarter, I would rather build the plan around that reality than around a date we both know is optimistic."

**What you are testing.** Whether the initiative has budgeted capacity or only executive enthusiasm. This ask surfaces Boundary Condition 5, the buyer who cannot implement at any price, before the MIP is drafted rather than after.

### Rung 6: paid diagnostic

> "You are asking for a pilot, which tells me you see real risk here. So do we. What we have found is that free pilots get deprioritized the moment something urgent lands, so we run a paid diagnostic instead: fixed scope, fixed price, defined exit, and the output is yours whether or not you buy anything. If it says do not proceed, that is a successful outcome."

**What you are testing.** Whether the risk the buyer describes is one they will spend against. A buyer who will not fund a bounded diagnostic against a risk they say is serious has told you the risk is not the real objection.

---

## Reading the response

The response is the data. Four patterns and what each means:

**Delivered, fast, complete.** Commitment is real. Move to the next rung and compress the cycle.

**Delivered, slow, partial.** Usually organizational rather than motivational. Something in their process is expensive. Find out what before assuming disinterest, because this pattern also describes a highly regulated buyer who will eventually be an excellent customer.

**Substituted.** They offer something cheaper than what you asked for: a summary deck instead of the data, one attendee instead of three. Name it warmly and hold the ask once. If it is substituted twice, treat it as a decline.

**Declined with a reason that does not survive a follow-up question.** The most informative outcome on this page. Update the forecast, not the ask.

A buyer who declines every rung has not failed qualification. They have completed it, at a cost of two conversations instead of two quarters.

---

## Failure modes

**Asking without pairing.** The seller requests data, attendance, and resources while committing nothing. The buyer experiences an audit. Principle 2 is violated and the signal mechanism breaks regardless of how well each individual ask is worded.

**Escalating after a failed rung.** A buyer who could not send a document will not convene three departments. Skipping up the ladder converts one cheap negative signal into an expensive one.

**Reading slow as dead.** Enterprise security review is slow for structural reasons that have nothing to do with the buyer's intent. Distinguish the buyer who cannot move from the buyer who will not.

**Accepting the substitute silently.** The seller asks for production data, receives a slide about the data, and proceeds as though the ask succeeded. The gap surfaces during implementation as the unmapped exception path that consumes the margin.

---

## Related

- [costly-signals.md](../../theory/02-research/costly-signals.md) — Spence, Akerlof, and the Single Crossing Property behind every ask here.
- [friction-allocation-diagnostic.md](./friction-allocation-diagnostic.md) — Test any new ask against the four principles before adding it to the ladder.
- [01-discovery-contextual-blueprint.md](./ilg-motion/01-discovery-contextual-blueprint.md) — Where rungs 1 through 3 run, and where the Reciprocity Gate is recorded.
- [process-calculator.md](./process-calculator.md) — Step 0 workflow maturity, which rung 4 is designed to verify independently.
- [ilg-deal-calibration-checklist.md](./ilg-deal-calibration-checklist.md) — Pre-close audit confirming the ladder was actually run.
