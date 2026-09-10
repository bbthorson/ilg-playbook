---
title: "The Friction Vector"
layer: theory
status: under-review
version: 0.1
operationalizes: [axiom-1, axiom-3]
canonical_source: theory/01-foundation/00-ilg-constitution.md
---

# The Friction Vector

**Version:** 0.1
**Purpose:** To derive motion selection from the two quantities Axiom I already names, so that a motion becomes a region of one space rather than an item on a list.

> [!IMPORTANT]
> **This document does not govern.** It is a proposal under review. [01-sales-motion-comparison.md](./01-sales-motion-comparison.md) and the [Process Calculator](../../practice/01-field-assets/process-calculator.md) remain in force and remain the answer to "which motion do I run." Nothing here has been adopted, no artifact has been retired, and section 10 lists what adoption would cost. The notation in section 1 stays local to this file rather than entering [04-glossary-and-notation.md](./04-glossary-and-notation.md), because that index is canonical and this document is not.

---

## 1. The two quantities

Axiom I states that transaction costs decompose into three components. Write them as one object:

$$\mathbf{F} = (F_{search},\; F_{consensus},\; F_{implementation})$$

Two properties of that object carry all the information a seller needs, and Axiom I already names both.

**Direction.** Where the vector points. Which component dominates, and by how much.

$$\hat{\mathbf{F}} = \frac{\mathbf{F}}{\lVert \mathbf{F} \rVert}$$

**Magnitude.** How long the vector is. The total cost of transacting.

$$\lVert \mathbf{F} \rVert_1 = F_{search} + F_{consensus} + F_{implementation}$$

Axiom I's own statement maps onto these directly. *Composition selects the motion* is a claim about direction. *Combined level sets the boundary between Turnkey and Structural deals* is a claim about magnitude. The two claims were separated in Constitution v16.0 and nothing downstream has yet consumed the separation.

The $L^1$ norm is used because it is what the field already produces. Step 2 of the Process Calculator sums four scores, which is a sum rather than a Euclidean length. Nothing in what follows depends on the choice.

---

## 2. Direction selects the instrument mix

A seller cannot move the buyer's willingness to pay, which is a property of the product. A seller can lower the buyer's perceived cost, and the reduced form in [03-mathematical-models.md](./03-mathematical-models.md) section 1.2 establishes that lowering the price term alone is the weakest of the available levers. What remains is friction, and friction has three components.

**A motion is therefore defined by which component the seller spends to reduce.** There are three components, so there are three families of instrument, and no more.

| Component | What the buyer cannot do | What the seller produces |
|---|---|---|
| $F_{search}$ | Find a viable solution at acceptable cost | Artifacts that travel without the seller present |
| $F_{consensus}$ | Get their own organization to agree | Artifacts that let stakeholders reconcile competing objectives |
| $F_{implementation}$ | Tell whether installing it will break them | Artifacts that resolve technical and operational uncertainty |

**Direction gives a mix, not a label.** A deal at $(0.1,\, 0.7,\, 0.2)$ runs mostly consensus instruments over a light implementation layer. A deal at $(0.1,\, 0.3,\, 0.6)$ inverts that. Both are ordinary deals and neither is a special case.

This resolves a question the current framing cannot answer. Asking whether consensus work is a separate motion or a phase of an implementation-heavy one assumes motions are exclusive. They never were. Every deal carries all three components, and what varies is the weighting.

### 2.1 The three sub-costs of search

$F_{search}$ carries three distinct blockers, and [01-sales-motion-comparison.md](./01-sales-motion-comparison.md) already separates the first and third. The middle one is new here.

| Blocker | Instrument |
|---|---|
| The buyer cannot name the category | Education, reference architectures, category definition |
| The buyer cannot reach the seller | Partnerships, channel, marketplace listing, group purchasing |
| The buyer cannot tell whether the fit holds | Trial, sandbox, self-serve evaluation |

The middle row is a cost the current framework does not name. A hospital chief information officer can know the category, name five vendors, and still be structurally unreachable without a channel. That cost falls largely on the seller, and neither education nor a trial reduces it. Research backing is in [channel-collapse.md](../02-research/channel-collapse.md), and Axiom III's requirement that any adjudicator carry a stake applies directly to the channels involved.

These are three instruments serving one component. They are not three motions.

### 2.2 Consensus has a mature instrument set the repository does not name

The consensus component is worked hard by the wider sales profession. Qualification frameworks built around economic buyer access, written decision criteria, documented decision process, and champion development are consensus instruments, and they are the incumbent practice for that component.

This repository measures the component and supplies no instruments for it. The [Consensus Friction Calculator](../../practice/01-field-assets/consensus-friction-calculator.md) produces a number and then prescribes executive sponsorship, which is a single tactic rather than a motion. Research is in [buying-center-dynamics.md](../02-research/buying-center-dynamics.md).

The gap is real and it is the largest one this document surfaces.

---

## 3. Magnitude sets the apparatus

Magnitude answers a different question: how much machinery the deal can carry before the machinery costs more than it saves.

This is the existing boundary condition and it is unchanged. $k > k_{threshold}$ with $k_{threshold} = 10$ separates Turnkey deals from Structural deals, and $F_{deployed} \sim k$ requires the friction the seller deploys to scale with the specificity it manages. Both over-frictioning and under-frictioning are failures of magnitude rather than of direction.

**Direction and magnitude are independent.** A short vector pointed at implementation is a small technical purchase. A long vector pointed at implementation is a Structural deal. Same direction, different apparatus.

---

## 4. Four regions

Named motions become regions of the space rather than members of a list.

| Region | Signature | Current name | State of the instruments |
|---|---|---|---|
| Short vector, any direction | All three components low | PLG | Present and thin |
| Long, search-dominant | $F_{search}$ dominates | SLG, education-led | Present and thin |
| Long, consensus-dominant | $F_{consensus}$ dominates | Unnamed | Absent |
| Long, implementation-dominant | $F_{implementation}$ dominates | ILG | Present and developed |

**The short-vector region is a magnitude claim, not a direction.** A light marketing funnel feeding a low-cost trial feeding buyer-run deployment is a light touch on all three components at once. Reading it as a competitor to the other three regions is the error this document is most concerned to correct, and sections 6 and 7 say what that error costs.

Naming the consensus region is deliberately left open. Any name chosen here would enter the repository ahead of the argument that justifies it.

---

## 5. Asymmetry rotates the vector, and drift rotates it back

The Constitution's effective cost equation applies one amplifier to the whole sum:

$$F_{effective} = (F_{search} + F_{consensus} + F_{implementation}) \cdot (1 + \Delta_A)$$

Scaling every component by the same factor changes the length of the vector and leaves its direction untouched. The consequence is exact rather than approximate: **under the equation as written, no amount of asymmetry and no amount of work reducing it can change which motion a deal needs.** Direction is invariant to $\Delta_A$.

That contradicts ordinary experience. A seller who maps an environment has changed the shape of the deal, not only its size.

### 5.1 Three pairs, three gaps

The single gap $\Delta_A = I_{seller} + I_{buyer}$ describes two parties, and the three components do not share one pair of parties between them.

| Component | Whose ignorance, about what |
|---|---|
| $F_{search}$ | The buyer, about the market |
| $F_{consensus}$ | The buyer's stakeholders, about each other |
| $F_{implementation}$ | The seller, about the buyer's environment |

Only the third is seller against buyer. The [Asymmetry Scorecard](../../practice/02-internal-ops/04-incentives-asymmetry-scorecard.md) measures that third pair and is currently applied as though it measured the deal.

Amplify each component by its own pair's gap:

$$F_{effective} = \sum_{k} F_k \, (1 + \Delta_k)$$

Direction now moves with the work. A deal that opens implementation-dominant rotates toward consensus as discovery closes $\Delta_{implementation}$, which is what a Blueprint is for and what the framework has had no way to state.

### 5.2 Drift is the same rotation running backwards

Axiom II carries $\Delta_A(t) = \Delta_A(0) + \gamma t$ before signature. Section 7.2 of [05-seller-surplus-model.md](./05-seller-surplus-model.md) carries the same equation after it. Per component:

$$\Delta_k(t) = \Delta_k(0) + \gamma_k t$$

**Seller investment and drift are one mechanism with opposite signs.** Discovery lowers a component's gap and rotates the vector away from that component. Absent maintenance the gap rebuilds at $\gamma_k$ and the vector rotates back. A deal is therefore a path through the composition space rather than a point in it, and the same is true of an account after signature.

Each component drifts for its own reasons and at its own rate.

| Rate | What drives it | Where it is already named |
|---|---|---|
| $\gamma_{search}$ | New entrants, category redefinition | Nowhere |
| $\gamma_{consensus}$ | Stakeholder turnover, reorganization | Nowhere |
| $\gamma_{implementation}$ | Staff turnover, workflow change, systems installed unseen | [05-seller-surplus-model.md](./05-seller-surplus-model.md) section 7.2 |

**The field consequence sits in the consensus row.** A champion leaving is $\gamma_{consensus}$ arriving all at once. The alignment that stakeholder held is gone, the deal rotates back toward consensus-dominant, and it can leave the viable zone without any change in the product, the price or the technical work. That event is the most common way an enterprise deal dies and the framework currently has no term for it.

This also generalizes Axiom III's trajectory. $D(t)$ is written as a scalar, the distance between transaction cost and opportunity cost. Under per-component drift it is a path with a direction, and the direction says which instrument would arrest it.

### 5.3 What this demotes

The reduced form $y = a\hat{\Delta}_A^2 + c$ collapses the vector to a scalar, and [03-mathematical-models.md](./03-mathematical-models.md) section 1.4 already concedes that it "produces a number, not a diagnosis." Under this model the concession is heavier, because direction is the quantity that selects the motion and the reduced form destroys it. The form keeps its one job, which is showing why cutting price cannot offset a wide gap. It stops being a representation of transaction cost.

The coefficient $\beta$, which weights one side's ignorance against the other's, is only meaningful inside a pair with two distinguishable sides. The consensus pair has the buyer on both sides. $\beta$ is therefore a parameter of the implementation component rather than a global one.

---

## 6. Addressable market is a property of the motion

A seller who runs only short-vector tactics can transact only with short-vector buyers. Buyers whose deals carry a long vector are not lost somewhere in the funnel. They were never reachable, because the motion offered no instrument for the cost that was blocking them.

**This inverts the usual reading.** Addressable market is normally treated as a property of the product, fixed by what the product does and who needs it. Under Axiom I it is a property of the motion, because the motion decides which regions of the friction space a seller can serve. Changing the motion changes the market.

The practical consequence is that a market sizing exercise conducted without naming the motion is not measuring anything stable.

---

## 7. A second symptom of under-frictioning

Axiom I names under-frictioning as the failure where asset specificity exceeds the friction deployed, and gives one symptom: the buyer declines to transact and builds internally.

There is a second symptom, and it appears after signature rather than before. A buyer whose implementation uncertainty was never resolved can still transact when the commercial path is easy enough. They buy, they fail to deploy, and they leave. The cause is identical. The symptom lands in retention rather than in win rate, which is why it is usually diagnosed as a product problem or an onboarding problem.

Both symptoms belong to the same failure. The framework currently names only the first.

---

## 8. Why sellers choose the wrong region

The seller picks the motion, and the seller has a reason to pick the short-vector one that has nothing to do with the deal in front of them. Short-vector tactics carry lower cost of sale, and lower cost of sale reads well on an income statement.

**This is an Axiom III failure inside the seller's own organization.** The party choosing the motion holds no stake in the outcome the choice produces. A representative compensated on new bookings, or a leader measured on sales efficiency, is an adjudicator of motion selection with no exposure to the churn that follows a misread vector. Axiom III predicts exactly this: an adjudicator without a stake drifts from adjudication toward extraction, and here the extraction runs against the seller's own future revenue.

The remedy already exists in [03-incentives-vested-commission.md](../../practice/02-internal-ops/03-incentives-vested-commission.md), which ties compensation to outcomes that survive past signature. That artifact is currently justified as protection against poor Structural deal execution. Under this reading it also governs motion selection, which is a wider claim than the file currently makes.

---

## 9. What this does not settle

- **The consensus region has no name and no instrument file.** Both are open.
- **Whether the three components are measurable in a form the equations can consume.** The [Asymmetry Scorecard](../../practice/02-internal-ops/04-incentives-asymmetry-scorecard.md) emits ordinal ratings, and the models in [03-mathematical-models.md](./03-mathematical-models.md) square their inputs. Squaring an ordinal rating is not a defensible operation, and no component score is trustworthy until that is fixed.
- **Whether market stage carries information the vector misses.** Market stage is a proxy for direction, and measuring direction should make the proxy unnecessary. A market that is about to mature may still behave differently from a mature one with identical present composition, and nothing here tests that.
- **Whether direction is vendor-relative.** An incumbent defending a renewal and a challenger attacking it face the same opportunity with different vectors, because the incumbent's implementation cost is already sunk. If that holds, the vector must be scored from a named seat rather than scored for the deal.
- **Where the boundary between short and long sits.** The magnitude threshold is inherited from the existing calculator and carries no more empirical support here than it does there.

---

## 10. What adopting this would cost

Recorded so that adoption is a decision rather than a drift.

**Rewritten.** [01-sales-motion-comparison.md](./01-sales-motion-comparison.md), whose organizing spine is the three-motion list and the Market States taxonomy. Both are replaced by direction and magnitude.

**Rebuilt.** The [Process Calculator](../../practice/01-field-assets/process-calculator.md). Its market stage step becomes unnecessary, its four summed factors become three component scores, and its routing table becomes a reading of direction and magnitude. The workflow divergence step survives as a modifier on the implementation component.

**Reassigned, with content intact.** The Blueprint, Red Team, Mutual Implementation Plan and Adoption Review become implementation-component instruments rather than the artifacts of a named motion. The velocity and education files become short-vector and search-component instruments.

**Retired.** The Nascent, Efficient and Saturated market states. The reading of the summed score as a motion selector.

**Untouched.** All research files, [05-seller-surplus-model.md](./05-seller-surplus-model.md), and the three axioms themselves. This document introduces no new axiom and asks for no change to any existing one.

---

## Related

- [00-ilg-constitution.md](./00-ilg-constitution.md) — Axiom I supplies both quantities. This document consumes the separation made in v16.0 and adds nothing to it.
- [01-sales-motion-comparison.md](./01-sales-motion-comparison.md) — The motion framing currently in force, and the file this proposal would replace.
- [03-mathematical-models.md](./03-mathematical-models.md) — Functional forms for the components, and the calibration status that governs every number here.
- [05-seller-surplus-model.md](./05-seller-surplus-model.md) — The seller's side of the transaction, which section 8 depends on.
- [transaction-cost-economics.md](../02-research/transaction-cost-economics.md) — Coase and Williamson, the source of the decomposition.
- [Process Calculator](../../practice/01-field-assets/process-calculator.md) — The instrument that would be rebuilt.
- [models/README.md](../../models/README.md) — Executable forms of the equations referenced here.
