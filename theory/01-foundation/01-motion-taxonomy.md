---
title: "The Motion Taxonomy"
layer: theory
status: active
version: 1.0
operationalizes: [axiom-1, axiom-2]
canonical_source: theory/01-foundation/00-tcg-constitution.md
---

# The Motion Taxonomy

**Version:** 1.0
**Purpose:** To name the motions, and to say what each one contains. A motion is the set of instruments a seller deploys against the cost that is actually blocking the deal, so the taxonomy has exactly as many entries as there are costs, plus one for the case where none of them is large enough to matter.

---

## 1. A motion is named after the cost it spends to reduce

A seller cannot move the buyer's willingness to pay, which is a property of the product. A seller can lower the buyer's cost of transacting, and that cost has three components. **A motion is therefore defined by which component the seller spends against**, which gives three families of instrument and no more.

| Component | What the buyer cannot do | What the seller produces |
|---|---|---|
| $F_{search}$ | Find a viable solution at acceptable cost | Artifacts that travel without the seller present |
| $F_{consensus}$ | Get their own organization to agree | Artifacts that let stakeholders reconcile competing objectives |
| $F_{implementation}$ | Tell whether installing it will break them | Artifacts that resolve technical and operational uncertainty |

Naming each motion after its component is not a stylistic choice. It is the only naming that makes the set consistent, because it is the only property the motions actually differ on.

---

## 2. Two questions, asked in order

Axiom I emits two quantities and they answer different questions. The taxonomy has two tiers for that reason.

**Level asks whether the deal warrants apparatus at all.** Below the boundary, no component is large enough to repay the cost of instruments built to reduce it. Direction is not a useful question there, because every share of a small number is still small.

**Direction asks, of a deal that does warrant apparatus, which component to spend against.**

| Level | Direction | Motion | Instruments |
|---|---|---|---|
| Turnkey, below 15 | Not asked | **Turnkey** | [turnkey-motion/](../../practice/01-field-assets/turnkey-motion/) |
| Structural, 15 and above | Search-dominant | **Search-led** | [search-motion/](../../practice/01-field-assets/search-motion/) |
| Structural | Consensus-dominant | **Consensus-led** | [consensus-motion/](../../practice/01-field-assets/consensus-motion/) |
| Structural | Implementation-dominant | **Implementation-led** | [implementation-motion/](../../practice/01-field-assets/implementation-motion/) |
| Structural | Mixed | **Composed** | The top two in proportion, heaviest first |

A component is dominant at half of effective cost or more. Where none reaches it, the deal is Composed and the instruction is to run the top two in proportion rather than pick the nearest single name.

**The motion names and the calculator's output are the same words on purpose.** The [Deal Triage Calculator](../../practice/01-field-assets/deal-triage-calculator.md) emits a level and a direction, and the direction is the motion. Nothing has to be translated, which matters because translation layers are where field errors accumulate.

---

## 3. What each motion contains

### Turnkey

**The deal:** every component low. No integration worth the name, one or two people who can say no, a workflow the product already fits.

**What the seller does:** removes itself from the evaluation. Self-service signup, automated onboarding, published pricing, a trial the buyer runs against their own work. The instrument that carries the most weight is the trial, and what it actually does is transfer the fit measurement to the buyer, who is the only party positioned to perform it.

**Where it fails:** when the vector is longer than it looks. A small installation on a workflow the product matches nothing of is a Structural deal wearing Turnkey clothes, and every count comes out low while the misfit sits underneath. The calculator's divergence modifier exists to catch that case.

### Search-led

**The deal:** the buyer cannot find or compare. Three blockers sit inside this one component and they call for different instruments.

| Blocker | Instrument |
|---|---|
| The buyer cannot name the category | Education, reference architectures, category definition |
| The buyer cannot reach the seller | Partnerships, channel, marketplace listing, group purchasing |
| The buyer cannot tell whether the fit holds | Trial, sandbox, self-serve evaluation |

**The middle row is a cost most frameworks do not name.** A hospital chief information officer can know the category, name five vendors, and still be structurally unreachable without a channel agreement. That cost falls largely on the seller, and neither education nor a trial reduces it. Research is in [channel-collapse.md](../02-research/channel-collapse.md).

**Where it fails:** when the category goes legible during the cycle. Education-led selling works by making its own market comparable, which is why the motion has a shelf life on every deal it succeeds at.

### Consensus-led

**The deal:** the buyer's own stakeholders cannot see each other's measured objectives. The purchase is not blocked by anything the seller knows and withholds. It is blocked inside the buyer's building, and it still lands on the seller's forecast.

**What the seller does:** this repository does not have a full answer, and says so rather than substituting one. The [Consensus Friction Calculator](../../practice/01-field-assets/consensus-friction-calculator.md) sizes the cost and the Blueprint's stakeholder mapping and the Red Team workshop each do part of the work. The incumbent practice for this component lives in qualification frameworks built around economic buyer access, written decision criteria, documented decision process and champion development, and none of that is carried here.

**A deal routing here is routing to a gap.** Say so on the forecast call. [consensus-motion/](../../practice/01-field-assets/consensus-motion/) records what is known about what the instruments would have to do.

### Implementation-led

**The deal:** the buyer knows the category, can name the field, and cannot tell whether installing this will break them. Deep integration, cross-functional impact, a workflow that has to keep running during the change.

**What the seller does:** resolves the uncertainty before signature rather than arguing past it. [Blueprint](../../practice/01-field-assets/implementation-motion/01-discovery-contextual-blueprint.md) maps the environment, [Red Team](../../practice/01-field-assets/implementation-motion/02-validation-red-team-protocol.md) surfaces the failure modes, [MIP](../../practice/01-field-assets/implementation-motion/03-closing-mutual-implementation-plan.md) distributes the decision authority for whatever remains unmapped, and [Adoption Review](../../practice/01-field-assets/implementation-motion/04-sustaining-adoption-review.md) checks that value landed. Each gates the next.

**Where it fails:** section 6 lists six conditions, and they are the most-skipped part of this file.

---

## 4. Search-led and implementation-led are the pair that gets confused

Both carry high friction, and the *type* of friction is different in a way that inverts the correct behavior.

**Search friction is cognitive.** The seller is teaching the buyer that a problem exists and that a category of solution exists. Once the buyer understands the category, switching to a competitor is relatively easy, because they have not yet built anything around this particular implementation.

**Implementation friction is organizational.** The buyer already knows the problem and the category. What they cannot resolve is whether this vendor can install this system in their environment without breaking it. No amount of category education touches that.

The practical consequences:

- **Search-led reps are educators.** Commercial teaching, frame-of-reference building.
- **Implementation-led reps are implementation scientists.** Organizational diagnosis, workflow mapping.
- **Implementation instruments on a search-dominant deal over-engineer it.** You are producing rigor for a buyer who has not yet decided they have the problem.
- **Search instruments on an implementation-dominant deal under-prepare the buyer.** You are educating someone who needs governance.

This is also why direction is read from the amplified components rather than the base ones. Two deals can carry identical educational and installation work, and the one whose buyer already understands the category is not a search deal, because its search gap is closed and there is nothing left to spend there.

---

## 5. Motions are paths, not assignments

A deal is not filed under a motion at qualification and worked there until it closes. Direction moves every time an artifact closes a gap, and three transitions are common enough to name.

**Turnkey to implementation-led.** A team-level purchase expands to an enterprise rollout. Security review, cross-functional impact and organization-wide governance arrive together, and the level crosses the boundary. The deal was correctly Turnkey and is now correctly Structural.

**Search-led to implementation-led, by market.** The category goes legible. Standards emerge, analyst coverage develops, reference customers accumulate, and the search gap closes across every buyer at once. Sellers who stay search-led after that are educating buyers who have already been educated.

**Search-led to implementation-led, by discovery.** One deal turns out to carry integration and political complexity nobody scoped. The direction rotates mid-cycle and the instruments should follow. The failure is holding the original motion while evidence accumulates against it.

### The lifecycle runs one way, then resets

Left alone, a category ages in a single direction. Standards solidify, integration patterns homogenize, playbooks get published, and specificity falls. Both quantities move, and they move differently:

```
Emerging category      → level high, no playbooks       → search and implementation both wide
Consolidating category → level high, patterns forming   → search closes, implementation stays
Commoditized category  → level falls below the boundary → both close, apparatus stops earning
```

A motion that fit three years ago may over-serve the same category today. A team still running the full implementation chain on a commoditized category is burning margin on Blueprints the buyer no longer needs, and the signal to migrate is the level dropping below the boundary.

New technical paradigms reset the clock. Any category where the integration surface is still being invented creates fresh high-specificity segments inside markets that had otherwise matured, which is why the implementation-led motion relocates rather than disappearing.

---

## 6. Where the implementation-led motion is wrong

Axiom I says friction must match specificity, which means the implementation chain is wrong wherever the surplus it unlocks is smaller than the friction it imposes. Six conditions put a deal outside it. In each, the correct response is to decline rather than to run a lighter version.

**1. No operational baseline exists.** The Blueprint maps a workflow. With no workflow to map, the artifact produces a document the two parties invented together and the Red Team stress-tests a fiction. This is the Chaos Trap and it is why the workflow gate runs before anything is counted. *Route:* consulting to establish the process, then re-qualify.

**2. Deal value cannot carry the friction cost.** The chain consumes solutions-engineering hours before revenue. Below roughly the point where pre-sale cost exceeds first-year gross margin, it destroys surplus even when the deal closes. *Route:* Turnkey, or decline.

    This is the affordability half of the level-and-frequency split in [07-governance-forms.md](./07-governance-forms.md) section 6. Level says what the deal needs and frequency says whether it can be paid for, so a one-shot deal above the boundary can genuinely need the full chain and still be correct to decline.

    *Under review.* First-year gross margin is a single-shot test. [05-seller-surplus-model.md](./05-seller-surplus-model.md) section 7 shows pre-sale investment amortizes across the renewal stream, so this rule is correct where retention is weak and too strict where it holds.

**3. The category has commoditized.** Integration patterns homogenized, playbooks published, switching cost fell. Specificity dropped out from under a motion that used to fit. *Route:* re-score annually and migrate to Turnkey instruments when the level drops below 15.

**4. The specification is externally fixed.** A regulatory mandate or procurement standard that dictates the implementation leaves no discovery surplus to capture. Both parties already know what gets built, so discovery cannot reduce the gap on the dimension that matters. *Route:* compete on price and delivery credibility.

**5. The buyer has no implementation capacity at any price.** The MIP allocates resources the buyer does not have and cannot obtain. This is a capacity constraint rather than a governance failure, and better structure does not repair it. A signed MIP against absent resources produces a launch failure with a contract attached. *Route:* defer until capacity exists, or sell a managed-service shape instead.

**6. The seller cannot deliver what the motion promises.** This motion makes implementation credibility the product. An organization without the depth to run a genuine Red Team produces workshops that surface nothing, which is worse than running none, because the buyer now holds documented assurance that the risks were examined. *Route:* build the capability before selling on it.

The first three are properties of the deal. The last three are properties of the environment or the seller, and they are the ones teams skip when auditing their own boundary.

---

## 7. Why there is no market-stage taxonomy here

A framework organized around market maturity would carry stage names, and this one deliberately does not. Stage is a proxy for direction. It says what the friction profile *usually* is for a market at a given age, in place of measuring the profile of the deal in front of you, and a proxy that can disagree with a direct measurement is worse than no proxy.

The legibility signals a stage diagnostic would ask for are kept and measured directly. A recognized category name, three or more nameable vendors, and published third-party coverage are three of the four search evidence items in the calculator. They score the search gap itself rather than routing through a label.

**What this gives up.** A market about to mature may behave differently from a mature one of identical present composition, and a present-tense vector cannot see that. The difference belongs in $\gamma_{search}$, the rate at which the search gap rebuilds, and nothing tests it.

---

## 8. Common failure patterns

**Treating a Structural deal like a Turnkey deal.** Velocity instruments on a deal that needs the implementation chain. *Symptoms:* the deal stalls with no clear blocker and ends in no decision, or it closes and churns shortly after signature. Axiom I names both. *Root cause:* the level was not honored, or the counts behind it were deflated.

**Treating a Turnkey deal like a Structural deal.** The full chain on a low-specificity deal. *Symptoms:* the buyer experiences over-engineering and chooses a faster competitor. *Root cause:* reps trained on one motion applying it indiscriminately.

**Reading an unnamed category as a short alternative list.** The buyer names no vendors, so the search count comes out low and the deal routes to Turnkey or implementation instruments. *Root cause:* mistaking absence of competition for a small choice set. An unnamed category is an unbounded alternative set and scores the maximum search cost.

**Picking a named motion when the vector is Composed.** No component reaches half of effective cost and the rep chooses the region they know best. *Symptoms:* one binding cost is worked hard, another is untouched, and the deal moves and then stops.

**Skipping reciprocity.** Running the implementation chain without requiring the buyer to invest in it. *Symptoms:* a lopsided MIP, disengagement after signature, stalled implementation. *Root cause:* fear of losing the deal by asking for too much.

**A Red Team that surfaces nothing.** Running the workshop and accepting that everything looks fine. *Symptoms:* unexpected blockers during implementation, late discovery of an adversary. *Root cause:* the facilitator not pushing for prospective hindsight.

---

## Key principle

> Never run a Turnkey motion on a Structural deal, and never close a Structural deal without resolving the cost that is actually blocking it.

The motion is not a preference. It follows from two measurements: how long the friction vector is, and where it points.

---

## Related

- [00-tcg-constitution.md](./00-tcg-constitution.md) — Axiom I supplies level and direction. Axiom II supplies the per-component amplification direction is read from.
- [06-friction-vector.md](./06-friction-vector.md) — Why a motion is a region of one space rather than an item on a list.
- [07-governance-forms.md](./07-governance-forms.md) — The third quantity, frequency, and what shape the arrangement takes after signature.
- [09-motion-vocabulary.md](./09-motion-vocabulary.md) — How these names map onto Product-Led, Sales-Led and the rest of the incumbent vocabulary, and where the older terms mislead.
- [Deal Triage Calculator](../../practice/01-field-assets/deal-triage-calculator.md) — The one place the diagnostic lives.
- [03-incentives-vested-commission.md](../../practice/02-internal-ops/03-incentives-vested-commission.md) — Why the party choosing the motion needs a stake in the outcome.
