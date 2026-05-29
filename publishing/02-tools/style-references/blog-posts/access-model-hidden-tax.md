# The ACCESS Model's Hidden Tax: Why CMS Just Handed Incumbents Another Moat

My colleague, the Health API Guy, called ACCESS "[the biggest tailwind since the pandemic.](https://healthapiguy.substack.com/p/cms-launches-access)" He's right about the technology. I’m not so sure about the economics.

The technical unlock is real: outcomes-based payment, a native Medicare billing lane for tech-enabled care, TEFCA integration finally becoming infrastructure. Care delivery companies already focused on improving outcomes, like Virta, Omada, and Hinge Health, now have a clear path to Medicare reimbursement without contorting themselves into telehealth billing codes.

But there's a second game being played that we should address.

CMS isn't just rewarding outcomes. They're mandating infrastructure. Through the ACCESS Model's 10-year commitment structure, the TEFCA interoperability requirements, and the ACCESS Tools Directory, they're creating a compliance regime that looks suspiciously like the last time the government tried to modernize healthcare IT.

This isn't about whether ACCESS is good policy. The shift from CPT codes to outcome-aligned payments would be wonderful and TEFCA could actually improve data liquidity.

But Transaction Cost Economics suggests a different outcome may be on the horizon. When CMS opens floodgates with government money and regulatory mandates, the water doesn't flow equally to all boats. It flows to whoever already owns the reservoir.

The pattern is consistent: government mandates don't reward the best technology. They reward whoever can absorb implementation risk on behalf of traditionally risk-averse buyers. HITECH promised digitization and competition. It delivered Epic and Cerner duopoly. ACO and MSSP programs promised innovation in population health. They delivered consolidation and exits for small independents.

---

## What ACCESS Actually Is

The [**Advancing Chronic Care with Effective, Scalable Solutions (ACCESS) Model**](https://www.cms.gov/priorities/innovation/innovation-models/access) launches July 1, 2026 as a 10-year voluntary program within Original Medicare. It targets four clinical tracks covering conditions that affect millions of beneficiaries: early Cardio-Kidney-Metabolic conditions (hypertension, high cholesterol, obesity/prediabetes), established CKM disease (diabetes, chronic kidney disease, heart disease), Musculoskeletal chronic pain, and Behavioral Health (depression and anxiety).

The core innovation is **Outcome-Aligned Payments (OAPs)**. Instead of billing for every office visit or procedure, participating organizations receive recurring payments tied explicitly to achieving measurable clinical targets—like blood pressure reduction, HbA1c control, or validated patient-reported outcome measures for pain and mood. Payment is contingent on the aggregate share of a participant's patient population meeting defined thresholds, with those thresholds escalating over the participation period to force continuous improvement rather than static maintenance.

This is fundamentally different from previous "pay-for-reporting" schemes where providers were rewarded merely for submitting data regardless of actual patient progress. ACCESS explicitly tests whether results-based care works better than activity-based care.

**Technology as a First-Class Citizen**

The model explicitly covers "tech-supported care" as a legitimate delivery mechanism. Remote monitoring, asynchronous coaching, FDA-regulated devices, behavioral support apps—all are permitted if clinically appropriate. Organizations can deliver care virtually, in person, or asynchronously, as long as they hit outcome benchmarks.

To support participants, CMS will publish an **ACCESS Tools Directory** listing approved vendors for remote patient monitoring devices, clinical software platforms, identity verification systems, and HIPAA-compliant tools. While CMS states that listing is voluntary and they won't independently verify clinical performance, vendors must self-certify compliance with HIPAA, state licensure laws, and FDA regulations.

**Integration with Primary Care**

ACCESS attempts to avoid the fragmentation that plagued earlier specialty models. Participating organizations must maintain health information exchange connectivity and share structured care updates. Meanwhile, primary care physicians can bill a new Co-Management Payment (approximately $30 per service, plus a one-time $10 onboarding fee) for reviewing updates and making clinical decisions like medication changes or problem list adjustments—all without patient cost-sharing.

**What's Genuinely Promising**

The optimist's case is real. For the first time, Medicare is creating explicit reimbursement pathways for the kind of longitudinal, tech-enabled chronic care management that has historically been impossible to bill under fee-for-service. Companies that have built condition-specific platforms finally have economics that match their clinical model. The interoperability requirements could accelerate TEFCA adoption. The outcomes focus is theoretically superior to volume-based incentives.

Worth being hopeful for.

---

## Why Government Money Creates Consolidation

To understand what ACCESS may actually do to the market, we need a framework for understanding how government mandates reshape competitive dynamics. Transaction Cost Economics, developed by Nobel laureates Ronald Coase and Oliver Williamson, explains why.

### The Asset Specificity Problem

TCE posits that transactions organize themselves to minimize the costs of exchange—the friction of search, negotiation, and enforcement. A key determinant of market structure is **asset specificity**: the degree to which an investment is locked to a specific relationship and loses value if redeployed elsewhere.

When asset specificity is high, buyers face a "hold-up problem." Once they've made relationship-specific investments—training staff on particular workflows, integrating systems, customizing processes—switching costs become prohibitive. The vendor gains leverage and can extract rents. This fear of hold-up makes buyers extremely risk-averse in vendor selection.

Government mandates create high asset specificity by forcing long commitment horizons and specific compliance requirements. Buyers can't easily pilot, can't cheaply switch, and face massive opportunity costs if they choose wrong. Under these conditions, they don't choose the most innovative vendor. They choose the "safe" vendor who can credibly commit to de-risking a high-stakes, long-term bet.

### The HITECH Pattern: How Mandates Drive Consolidation

The Health Information Technology for Economic and Clinical Health Act of 2009 is the definitive case study. Congress allocated $35 billion to subsidize EHR adoption, provided systems met "Meaningful Use" criteria. The promise was digitization and a competitive market for health IT.

The reality was market consolidation.

Between 2009 and 2015, [Epic and Cerner's combined market share grew from 23% to 72%](https://www.fiercehealthcare.com/tech/epic-cerner-growing-ehr-market-share-increased-hospital-consolidation-klas) of hospital beds. The vendor landscape collapsed from over 1,000 EHR companies to roughly 400 survivors. Small vendors with potentially superior technology were acquired, exited, or simply died.

**Why Epic Won**

Epic Systems didn't win because it had the most modern user interface or cutting-edge cloud architecture. It won because it understood the game wasn't about technology—it was about implementation.

HITECH created artificial urgency. Hospitals needed systems that could meet complex regulatory reporting requirements immediately to capture incentives and avoid penalties. This fundamentally altered purchasing criteria. Innovation and usability became secondary to regulatory compliance capability.

Epic's response was a military-grade implementation methodology: 100+ person implementation teams deploying on-site for months, co-developing custom workflows with each health system. At Mayo Clinic, this created thousands of custom workflows encoding decades of institutional knowledge directly into the system. This produced profound human and procedural asset specificity—training that was non-transferable, processes that were deeply embedded, integration that was immobile.

This is legitimate lock-in through value creation. The dependency emerged from genuine implementation excellence, not artificial barriers. Epic earned the switching costs by building something genuinely specific to each customer's needs.

But here's what mattered for the market: this capability required massive upfront resources. Smaller vendors, even those with better products, couldn't match this implementation capacity. They burned capital on regulatory compliance and had nothing left for the human-intensive work of de-risking enterprise deployments.

Meanwhile, tech giants like Microsoft and Google attempted market entry and failed—not because of technical limitations, but because they underestimated the complexity of regulatory requirements and the implementation services layer necessary to sell into risk-averse health systems.

**The Economic Lesson**

Government mandates created a market where the transaction cost of vetting, integrating, and trusting a startup became higher than the cost of the software itself. Health systems preferred vertical integration—buying an inferior module from their primary EHR vendor rather than a superior solution from a startup—because the marginal transaction cost of the former was near zero.

This is "economizing" on transaction costs, even if it sacrifices product quality. It's economically rational behavior in a market structured by regulatory compliance requirements. The result is predictable: incumbents with scale win by default.

---

## The ACCESS Model's Structural Dangers

ACCESS creates three forces that will drive the same consolidation pattern.

### 1\. The Voluntary Exit Problem

Unlike some CMMI models, ACCESS participation is voluntary for both providers and patients. Organizations apply on a rolling basis and can exit if the model doesn't work for them. This sounds like a feature—no one is forced into something that doesn't serve them.

But it creates **asymmetric risk** for technology vendors.

Primary care practices can quit ACCESS anytime if ROI doesn't materialize. They haven't promised CMS a 10-year commitment with penalties for withdrawal. But tech vendors must make substantial upfront infrastructure investments—TEFCA integration, certification costs, implementation resources—to support these practices.

If a practice quits the program, the vendor's investment is stranded. The practice could theoretically change vendors instead of quitting, but the switching cost is so high (new integration, staff retraining, data migration, workflow redesign) that they'll quit ACCESS entirely before switching. We've seen this pattern repeatedly: when the model doesn't deliver immediate ROI, practices exit rather than troubleshoot with a new vendor.

**What this means for vendor selection:**

Primary care practices making this bet will be extremely conservative. They'll choose proven, "safe" partners who guarantee they won't disappear in Year 3\. They'll demand evidence of financial stability, existing customer base, regulatory expertise, and—critically—the implementation capacity to ensure success.

Startups face a chicken-egg problem: can't get customers without proof of success, can't build proof without customers willing to take risk on an unproven vendor. In high-stakes, high-asset-specificity markets, this chicken-egg problem is nearly insurmountable without significant capital to subsidize early implementations.

### 2\. The TEFCA Infrastructure Tax and Regulatory Lock-Out

ACCESS requires participants to maintain "health information exchange connectivity." In practice, this means integration with the Trusted Exchange Framework and Common Agreement (TEFCA) ecosystem—the network of Qualified Health Information Networks (QHINs) designed to enable nationwide data exchange.

**The Compliance Floor: What It Actually Costs**

For a remote patient monitoring device startup attempting to participate in ACCESS, here's their hypothetical first-year compliance burden:

**Interoperability & Network Access:**

- Carequality implementer fees: $8,100-$11,220 annually for companies under $5M revenue  
- QHIN participation: $100,000-$500,000 in upfront engineering and legal (IHE profiles, FHIR implementation, certificate exchanges, patient matching logic)  
- Middleware alternatives: $50,000-$150,000 annually plus transaction fees  
- Annual recurring costs: $20,000-$50,000 minimum (audits, directory updates, security certifications)

**Regulatory Certifications:**

- FDA 510(k) Clearance: $30,000-$150,000 (preparation, consulting, testing—excludes clinical validation studies which can reach $250,000-$2.5M)  
- HITRUST Certification: $60,000-$120,000 initial ($15,000-$30,000 annual maintenance, excludes internal engineering remediation consuming 30-50% of dev team time for months)  
- ONC Health IT Certification: $15,000-$40,000 (testing fees, ongoing surveillance)

**Legal & Compliance:**

- HIPAA agreements, TEFCA flow-downs, data use agreements: $20,000-$50,000

This new startup's compliance outlay could easily hit $500,000. This is capital spent *before selling a single enterprise license*.

**The Regressive Tax on Innovation**

For a Series A startup with $2M raised and $500k first-year ARR, this represents **25% of total capital** or **30-100% of revenue**. For Epic, with tens of billions in annual revenue, these same costs represent **less than 0.001% of operating expenses**—and they've already sunk most of them building "Care Everywhere" over the past decade. Better yet, Epic actually *earns* fees as a QHIN operator.

This is a regressive tax structure that favors scale over innovation.

**The Manner Exception Trap**

The HTI-2 final rule introduced a provision that could significantly amplify this cost disparity: the "[TEFCA Manner Exception](https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-D/part-171/subpart-D/section-171.403)" to information blocking rules.

Normally, if a data requestor asks for information via a specific method (like a direct FHIR API), the data holder must provide it in that manner if technically feasible. The Manner Exception states it is *not* information blocking for an entity to fulfill requests only via TEFCA, provided both parties are capable of TEFCA exchange.

In theory, a startup could execute a lightweight, direct API connection to pull patient data for their ACCESS-qualified application. The hospital's EHR vendor says "we'll provide that data via our QHIN instead." The startup must now join a QHIN, pay the associated fees, and use document-based exchange that may be slower or less granular than a direct API would provide. The incumbent can legally refuse the more efficient connection and force the startup onto expensive infrastructure rails.

**The Regulatory Lock-Out**

This isn't theoretical. It's a mechanism that allows incumbents to deprecate their direct APIs in favor of TEFCA rails, effectively closing the side doors that startups have historically relied on. With explicit regulatory protection via the Manner Exception, what was once a risky anti-competitive move becomes a legally sanctioned strategy. The point-to-point integrations that allowed scrappy competitors to bypass expensive network fees can now be shut down with a reference to compliance with federal interoperability policy.

**The Consolidation Prediction**

Instead of "a thousand flowers bloom" on TEFCA, we'll see **consolidation of on-ramps**. Dominant players will cluster around the tools that are safest and most proven. Primary care practices won't evaluate all TEFCA-capable vendors—they'll choose from the short list of vendors that other practices are already using, that have proven implementation methodologies, and that their EHR vendor recommends or integrates with preferentially.

The little guys face not just a technical barrier, but a trust barrier. And trust, in high-asset-specificity markets, flows to incumbents by default.

### 3\. The 10-Year Commitment Horizon

ACCESS is explicitly designed to improve long-term outcomes. The payment structure escalates performance requirements over time. This means the partnership between vendor and deliverer ratchets up asset specificity—as the program matures, organizations can't pilot cheaply, can't easily iterate, and would need to commit substantial resources to change.

For primary care practices making this bet, the risk is existential. Choose the wrong technology partner and your choices are: stay locked in years of poor outcomes data, strained workflows, and potential financial penalties, or quit the program. Those that don't participate or drop out risk lower margins than their competitors.

This decision calculus doesn't favor innovation. It favors **governance structures** over contracts. Practices will demand:

- Proven track record with similar organizations  
- Financial stability (proof the vendor won't disappear in Year 3\)  
- Implementation methodology that's been validated at scale  
- Contractual guarantees about long-term support and evolution  
- Integration with existing EHR and care management infrastructure

Startups, almost by definition, cannot credibly make these commitments. Even if the founders genuinely intend to, buyers operating under bounded rationality cannot trust those intentions against the statistical reality that most startups fail or get acquired.

---

## The Certification Paradox: Why Compliance ≠ Success

The ACCESS Tools Directory functions as a government-sanctioned "white list" for approved vendors. While CMS explicitly states that listing is voluntary and they won't independently verify clinical performance, the entry requirements are substantial: self-certification of HIPAA compliance, state licensure adherence, and—critically—FDA regulatory compliance if the tool performs "active patient monitoring" or "clinical decision support."

For risk-averse hospital CIOs and compliance officers navigating high-stakes, long-term commitments, this directory will almost certainly function as a mandatory procurement list. "If it's not in the directory, we can't buy it" becomes the safe default position.

This recreates the dynamic from HITECH's "Certified EHR Technology" program.

### The Certification Valley of Death

A digital health startup aiming to be listed in the ACCESS Tools Directory faces a gauntlet of regulatory requirements, each with significant associated costs: FDA 510k, HITRUST, Interoperability, ONC Certification, Legal.

As laid out above, this could easily come to a half million dollars. This is capital spent *before selling a single enterprise license*. For a seed-stage startup that raised $2 million, allocating 25% of runway to compliance before finding product-market fit is often lethal.

### The HITECH Lesson: Certification Gives Permission to Play, Not Customers

After HITECH mandated Meaningful Use certification, over 1,000 vendors achieved ONC certification and were listed as approved EHR technology. The market consolidated to roughly 400 survivors by 2019\.

Why didn't certification save the other 600+ vendors?

Certification was a necessary condition but nowhere near sufficient. Small vendors burned precious capital on compliance, then discovered they had nothing left for the expensive, human-intensive work of actually selling into and implementing within large health systems. They were certified, compliant, and dead.

### The ACCESS Double Bind

ACCESS creates the same trap:

1. **To sell to practices**, you need to be in the Tools Directory (certification required)  
2. **To win deals once certified**, you need implementation capacity that dwarfs product development costs  
3. **Most startups optimize for step 1** (getting certified and listed) and run out of capital before mastering step 2 (selling into high-friction, risk-averse markets)

The vendors who survive won't be the ones with the best technology. They'll be the ones who either:

- Were already large enough to absorb compliance as a rounding error (Teladoc, Omada, Epic)  
- Sold white-label to health systems who participate under their own TIN (avoiding direct market competition)  
- Became infrastructure plays helping others navigate compliance (Zus, Metriport, Flexpa)

The "thousand flowers bloom" narrative will give way to oligopoly, not because the technology failed, but because the economics of high-friction enterprise sales killed the business models before product-market fit materialized.

---

## What Actually Wins in Biased Markets

If consolidation is structurally inevitable, and certification is necessary but insufficient, what's the viable path for tech platforms trying to participate in ACCESS?

The answer comes from understanding what Epic actually did during HITECH. They didn't just build better software or get certified faster. They fundamentally understood that in high-asset-specificity markets, buyers aren't purchasing technology—they're purchasing **risk mitigation**.

For startups and emerging players, this means abandoning the traditional SaaS playbook entirely. You're not competing on features or demos. You're competing on your ability to de-risk a 10-year bet for a practice operating under bounded rationality and facing existential consequences if they choose wrong.

### Stop Selling Features. Start Selling Risk Mitigation.

When a primary care practice considers a 10-year commitment to ACCESS with a particular technology vendor, they're not primarily asking "Does this platform have better UI than competitors?" They're asking:

- "Will this actually work in OUR practice with OUR EHR and OUR patient population?"  
- "What if we commit and this blows up in Year 2?"  
- "How do we know they'll still be around in Year 5?"  
- "Can we trust them to evolve with regulatory changes we can't predict?"

These are Transaction Cost Economics questions at their core. They're about bounded rationality (inability to predict the future) and opportunism (fear of vendor hold-up once committed). Your sales motion must directly address these fears, or you lose to whoever does.

### Close the Knowledge Gap Through Deep Diagnostics

**What buyers fear:** "Will this work in my specific context?"

Information asymmetry—the gap between what you know about your product and what the buyer knows—creates a "fear premium." The less the buyer understands about how you'll actually integrate into their workflows, EHR constraints, patient population characteristics, and political dynamics, the more they discount your value.

**How to address it:**

Conduct deep diagnostics of their specific context *before* proposing your solution. Don't lead with a demo. Lead with discovery that proves you understand their world better than they do.

Map their existing workflows in granular detail. Understand their EHR setup (Epic? Cerner? On-prem or cloud? Which version? What customizations?). Profile their patient population (demographics, acuity, health literacy, technology access). Identify political resistance ("Who loses power or convenience if this succeeds? Which physician champion previously tried something like this and got burned?").

This isn't "needs assessment." This is ethnographic research that demonstrates competence and builds trust.

**Why it works:**

Closing the information gap removes the fear premium. When buyers see that you've diagnosed risks they hadn't even articulated, you've just de-risked the purchase in their mental model. You're no longer a vendor trying to sell them something—you're a partner who understands the actual implementation challenge.

### Surface Failure Modes Before They Kill the Deal

**What buyers fear:** "What if we commit and this fails?"

Buyers are trapped in what behavioral economists call the "Buyer's Paradox": they're paralyzed by the fear of choosing wrong (Loss Aversion—losses weigh 2.25x heavier than equivalent gains), yet irrationally optimistic about execution (the Planning Fallacy—systematically underestimating how long tasks will take and how many things will go wrong).

Your sales motion must solve both sides of this paradox.

**How to address it:**

Run "Pre-Mortem" workshops during the sales process. The frame is simple: "Imagine it's 18 months from now and this implementation has completely failed. What happened?"

Force the buying committee to work backward from failure. What would cause the integration to break? Where would staff resistance be strongest? Which patient populations wouldn't engage? What regulatory changes could undermine the model? What happens if key personnel leave?

This exercise surfaces real objections that would otherwise remain hidden until they kill the deal post-signature. More importantly, it differentiates two types of resistance:

- **Rational skeptics**: Stakeholders raising legitimate technical or workflow concerns. These people can be co-opted through validation—show them you've thought about their concern and have mitigation strategies.  
- **Political adversaries**: Stakeholders whose resistance is about power, turf, or past grievances rather than legitimate concerns. These people can't be won over with logic; they need to be contained through political mapping and champion strategy.

Frame the Pre-Mortem as "protecting the champion." You're helping your internal sponsor see around corners so they can defend the decision to their peers and leadership.

**Why it works:**

Prospective hindsight is dramatically more effective than prospective planning for identifying risks. By forcing buyers to imagine failure, you activate different cognitive pathways that surface concerns they'd otherwise suppress. When you then show mitigation strategies for each failure mode, you've demonstrated that the scary unknowns are actually knowable and manageable.

### Build Implementation Roadmaps Before Contract Signature

**What buyers fear:** "We sign the contract, then discover integration is a nightmare, and now we're stuck."

In high-asset-specificity purchases, the real fear isn't the software—it's the post-contract friction. Buyers have been burned by vendors who glossed over implementation complexity during sales, then disappeared or proved incompetent once the contract was signed.

**How to address it:**

Build a detailed 90-day implementation roadmap *before* the contract signature. This isn't a proposal written by your team. This is a co-authored project plan developed with their IT leadership, clinical champions, and front-line staff.

Include everything: technical integration milestones (EHR connection, data validation, user provisioning), workflow changes (process maps for each care team role), training schedules (by user type and competency level), and success metrics (leading indicators you'll track to validate the implementation is on track before outcome data materializes).

Most critically, make this plan contractually binding. Don't just attach it as an exhibit—reference it as a governance structure that defines obligations for both parties. Build in checkpoints where either party can pause and remediate before proceeding.

**Why it works:**

High asset specificity requires governance, not contracts. A standard SaaS agreement is an incomplete contract—it can't possibly specify all contingencies over a 10-year relationship. When buyers are making this kind of bet, they need structural assurance you'll deliver, not just legal assurance you'll try.

The Mutual Implementation Plan converts fear ("what if this goes wrong?") into process ("here's exactly how we'll handle what goes wrong"). You're not eliminating risk—you're making it manageable and shared.

### Reframe Pre-Purchase Friction as Risk Reduction

Some buyers might resist this approach. "This seems like a lot of work before we even start. Can't we just do a pilot?"

The reframe is economic:

"Every hour we spend diagnosing risks now saves ten hours of firefighting later. We're de-risking your ACCESS commitment, your board presentation, and frankly, your career. The practices that fail in ACCESS will be the ones who piloted fast and fixed nothing. The ones that succeed will be the ones who implemented deliberately with clear-eyed understanding of what could go wrong."

This is the economic truth buyers already know intuitively: you're converting post-purchase friction (high, unpredictable, relationship-threatening) into pre-purchase friction (high, but structured and contained).

In Transaction Cost Economics terms, you're reducing ex-post opportunism by increasing ex-ante contracting completeness. Buyers who understand this intuitively prefer this trade, even if they can't articulate why.

---

## Conclusion: The Implementation Imperative

Outcome-aligned payments are genuinely superior to CPT fee-for-service. TEFCA represents real progress on interoperability infrastructure. Tech-enabled care deserves a native Medicare billing lane.

But participation is not success.

The ACCESS Model creates the same structural dynamics that drove consolidation after HITECH:

- **Voluntary exit option** creates asymmetric risk, forcing conservative vendor selection  
- **Infrastructure tax** favors incumbents who already sunk these costs  
- **10-year commitment horizon** creates maximum asset specificity, demanding governance over contracts  
- **Certification requirements** are necessary but insufficient—the real barrier is implementation capacity

The result is predictable: consolidation around players who were already large enough to absorb the infrastructure tax and prove long-term viability.

### For Tech Platform Founders: There Is a Path

But it requires abandoning the SaaS playbook entirely.

You're not competing on "better technology." You're competing on "can de-risk the buy for a practice making a 10-year bet under conditions of extreme uncertainty."

**The capabilities you need:**

- Deep contextual diagnostics that prove you understand their specific implementation challenges  
- Pre-mortem risk surfacing that addresses fear of failure directly  
- Co-developed implementation plans that convert post-purchase friction into pre-purchase process  
- Credible long-term commitment signals (financial stability, proven track record, governance structures)

If you can master this—if you can sell risk mitigation instead of features, governance instead of contracts, proven methodology instead of innovative technology—you can win deals despite the structural bias toward incumbents.

If you can't, you're building in the wrong market. The certification will get you listed in the Tools Directory. But the implementation capacity determines whether you'll still be around in Year 3\.

### The Hard Truth

The revolution in outcomes-based care — the shift from volume to value is necessary and long overdue. The technical infrastructure is genuinely improving.

But it's being built on a foundation that structurally favors those who can absorb compliance costs and deliver implementation excellence at scale. The ACCESS Tools Directory will likely attract hundreds of certified vendors. Within 3-5 years, most will exit through acquisition, pivot, or shutdown.

The survivors will be the ones who understood that in high-asset-specificity markets, you don't win by building better features. You win by de-risking transformation.

That's the game. Eyes open. No illusions.

Let the games begin. 