# Competing on Value, Not Control: How Information Blocking Rewards Value Creation

The crackdown on Information Blocking has arrived, but I’m not sure it's what most people think.

The Office of Inspector General is levying million-dollar fines. CMS is building disincentives into reimbursement. But the real story isn't happening in regulatory notices—it's unfolding in federal court. [*Real Time Medical Systems v. PointClickCare*](https://healthapiguy.substack.com/p/the-real-time-medical-systems-v-pointclickcare) has quietly established something far more consequential than another compliance checkbox: a viable pathway for private litigation against information blocking, using state unfair competition laws as the vehicle.

The Fourth Circuit's affirmation of the preliminary injunction did three things that should make every health IT executive pay attention. First, it validated robotic process automation and screen scraping as lawful access methods when standardized APIs fall short. Second, it shifted the burden of proof squarely onto vendors to demonstrate that their blocking practices qualify for a legitimate exception. And third—most critically—it proved that Cures Act violations can serve as the predicate wrongful act for tortious interference and unfair competition claims, even though the Act itself contains no private right of action.

[My colleague](https://www.linkedin.com/posts/brendan-keeler_henry-schein-ones-counterpunches-motion-activity-7386392844334358528-0_64?utm_source=share&utm_medium=member_desktop&rcm=ACoAAAKprf0BD3M7irXIXYO4-jaVuSDSA869-70) has written extensively about both the opposing forces of [systems of record](https://open.substack.com/pub/healthapiguy/p/there-will-be-bundling) and [information blocking](https://open.substack.com/pub/healthapiguy/p/the-real-time-medical-systems-v-pointclickcare), and the court cases are proving the stakes are real. To understand which companies face genuine compliance risk and which don't, I took a look at this through the lens of Transaction Cost Economics.

## A Brief Primer: Asset Specificity, Opportunism, and Hold-Up

Transaction Cost Economics, developed by Nobel laureates Ronald Coase and Oliver Williamson, provides a framework for understanding why certain economic relationships create dependency and how parties can exploit that dependency.

The key concept is **asset specificity**—investments that are valuable within a specific relationship but lose most of their value outside it. When a hospital implements an EHR, they're not just buying software; they're making relationship-specific investments: staff training on particular workflows, custom integrations, years of historical data formatted in proprietary ways. The more specific these investments, the more locked-in the customer becomes.

This creates the conditions for **opportunism**—self-interested behavior that exploits the dependency. Williamson defined this as "self-interest seeking with guile." Once a customer has made significant specific investments, a vendor can engage in **hold-up**: extracting more value than originally bargained for by threatening to withhold something the customer now depends on. In health IT, this often takes the form of data blocking—making it expensive, difficult, or impossible for customers to access their own data, thereby artificially inflating switching costs.

TCE distinguishes between legitimate and illegitimate sources of lock-in. When switching costs arise naturally from deep integration and co-developed workflows, that's productive asset specificity—the vendor earned the relationship through value creation. When switching costs are artificially manufactured through information asymmetry or contractual restrictions, that's opportunistic hold-up—the vendor is exploiting the relationship through coercion.

The Cures Act essentially outlaws opportunistic hold-up while preserving legitimate asset specificity. Understanding this distinction explains why compliance risk is dramatically higher for some vendors than others.

## The Negative Data Moats: Pure Opportunism

Let's start with the companies facing the highest compliance risk: the low-specificity, "plug-and-play" EHRs whose primary moat has always been making it expensive and painful to leave.

You know the archetype. The sales pitch emphasizes low upfront costs and quick deployment. The product itself is relatively generic—minimal customization, cookie-cutter workflows that sort of work for everyone but aren't really optimized for anyone. There's no deep implementation investment, no co-development of idiosyncratic processes. The value proposition is convenience and price, not transformation.

In TCE terms, these vendors create minimal legitimate asset specificity. There's little procedural or human capital investment that's truly relationship-specific. A practice could, in theory, switch to a comparable product with relatively low retraining costs. The business model only works if switching costs are artificially inflated through a different mechanism: controlling access to the customer's own data.

This is textbook opportunistic hold-up. The vendor waits until the customer has accumulated years of patient records in the system, then exploits that dependency by making data extraction prohibitively expensive or technically infeasible. The switching cost isn't a natural byproduct of value creation—it's a coercive mechanism designed to trap customers in a relationship they might otherwise exit.

Many EHRs have faced punishment for making data extraction difficult: eClinicalWorks settled DOJ charges for $155 million, Practice Fusion settled for $145 million, and NextGen and Greenway settled for $31 million and $57 million respectively.

The Cures Act has now made that entire retention strategy explicitly illegal and subject to $1 million per violation fines. More importantly, [*Real Time v. PointClickCare*](https://healthapiguy.substack.com/p/the-real-time-medical-systems-v-pointclickcare) has opened the door to private litigation that doesn't require waiting for federal enforcement. For companies in this category, compliance risk isn't theoretical—it's existential. To retain and grow customers, evidence suggests they'll need to invest in a different type of asset specificity.

## The Positive Workflow Moats: Legitimate Asset Specificity

Now consider Epic. When a health system like Mayo Clinic implements Epic, they're not just installing software—they're co-developing 1,400+ custom workflows that encode decades of institutional knowledge into the system. This creates profound human and procedural asset specificity, but it's the legitimate kind. The dependency emerges from genuine value creation, not artificial barriers.

You could give a competitor a complete data export from Mayo's Epic instance, and it would be functionally useless. The value isn't in the structured records—it's in the idiosyncratic order sets, the custom decision support rules, the specialty-specific documentation templates, the integrated care pathways that took years of clinical and IT collaboration to refine. That knowledge is deeply embedded in the system and in the people who use it daily.

This is the kind of lock-in TCE would predict and validate. The switching costs are real and substantial, but they're a natural byproduct of relationship-specific investments that created genuine value. Epic earned this moat through deep implementation, not through opportunistic hold-up. From a compliance perspective, vendors with this kind of workflow moat don't need to block data access to retain customers—their actual competitive advantage lies elsewhere.

The same principle applies to PointClickCare in the long-term post-acute care market, or Oracle Health (Cerner) in large health systems. These vendors have built what Williamson would call "credible commitments"—they've invested heavily in understanding their customers' specific needs and encoding solutions into the system. The resulting asset specificity is mutual: the customer is dependent on the vendor, but the vendor has also made specific investments in that relationship.

But here's the critical boundary: [*Real Time v. PointClickCare*](https://healthapiguy.substack.com/p/the-real-time-medical-systems-v-pointclickcare) demonstrates that even vendors with genuine workflow moats face compliance risk if they engage in opportunistic behavior at the margins. Real Time's allegation is that PointClickCare engaged in opportunistic bundling—allowing third-party RPA access for years, then blocking it only after releasing a competing analytics product. If proven, that's a classic hold-up problem: using legitimate asset specificity as cover for opportunistic conduct.

The court's rejection of PointClickCare's "manner," "security," and "performance" defenses is significant. Even vendors with genuine workflow moats can't weaponize them to block competition. Having legitimate asset specificity doesn't provide cover for information blocking when you're trying to preference your own ancillary products over third-party alternatives.

Epic's Payer Platform (EPP) will be an interesting test of this principle. As [my colleague Pryce Ancona pointed out](https://www.linkedin.com/posts/pryce-ancona-74a8b6a9_hot-goss-thursday-epics-payer-platform-activity-7387184909687324674-6f2y?utm_source=share&utm_medium=member_desktop&rcm=ACoAAAKprf0BD3M7irXIXYO4-jaVuSDSA869-70), because EPP is Certified Health IT, the Cures Act will force it to remain open—Epic can't turn it into a closed, proprietary network even if they wanted to. But that misses the real competitive question. Epic's EHR dominance never came from closed data; it came from implementation excellence. They built deep, idiosyncratic relationships with health systems through years of customization and workflow optimization—creating the kind of procedural and human asset specificity that makes switching prohibitively expensive regardless of data portability.

The question isn't whether EPP will be open (it will be). The question is whether Epic can execute the same implementation-led growth strategy with payers that made them dominant with providers. Can they replicate the playbook—the deep integration, the co-developed workflows, the relationship-specific investments that create genuine lock-in? Given their track record, betting against them would be unwise. But it's also a call to action for other players: there's a window to build comparable value with payers before Epic establishes the same kind of asset specificity they've achieved in the provider market.

## Beyond Workflow: Other Paths to Legitimate Lock-In

Workflow specificity isn't the only way to build legitimate competitive advantages. The critical distinction is whether vendors understand what actually creates their value and resist the temptation to fall back on opportunistic data control. As long as moats are built on genuine value creation—whether through workflow depth, network intelligence, or ecosystem enablement—rather than information asymmetry, compliance risk remains low. The question is what form that value creation takes.

## The Network Moats: When Asset Specificity is Collective

Network effects create a different kind of asset specificity entirely—one that's distributed across the entire user base rather than concentrated in a single relationship. And compliance risk depends entirely on whether that network creates value through learning or through exclusion.

Athenahealth's RCM network exemplifies productive network asset specificity. The value of athenaCollector increases as more practices join because each claim teaches the system something new about payer behavior. This is what economists would call "positive externalities"—each new user makes the service more valuable for everyone else. More data liquidity means more training data, which means better denial prevention. The company's business model reinforces this alignment: Athenahealth charges providers a percentage of their monthly collections (typically 4-8%), meaning the company only profits when its clients successfully collect revenue. This pricing structure creates incentives directly opposed to opportunistic hold-up—their success depends on their customers' success. The Cures Act actually strengthens this model because it feeds the learning flywheel. Compliance risk here is minimal because the moat depends on what you *do* with data, not on blocking access to it.

Tempus operates on the same principle in oncology. Their competitive moat is a proprietary dataset linking molecular profiles to clinical outcomes. As the network grows, the dataset becomes more statistically powerful and clinically useful. This is legitimate asset specificity at the network level—they've invested in building infrastructure to collect, curate, and analyze data in ways that create genuine insights. Importantly, their value isn't in blocking access to the underlying data; it's in the analytical layer they've built on top of it. They've created a knowledge moat, not a data moat. Again, low compliance risk because the value is in what you do with data, not in preventing others from accessing it.

But then there's Surescripts. The e-prescribing network's moat isn't that it learns from more transactions—it's that it controls access to the network itself. In TCE terms, this is closer to a tollbooth than a learning system. The asset specificity is structural rather than productive: every pharmacy and prescriber already on Surescripts creates a coordination problem for any competitor trying to build an alternative network.

That's why the FTC sued them for anticompetitive practices. When network effects are used primarily to exclude competition rather than generate learning, they start to look like opportunistic hold-up at scale. The government's answer to this tollbooth model is the Trusted Exchange Framework and Common Agreement (TEFCA) and Qualified Health Information Networks (QHINs)—a regulatory framework designed to transform these critical networks into open, transparent, and non-discriminatory infrastructure that operates more like a regulated utility than a proprietary platform.

The pattern is clear: network moats built on collective learning and intelligence face minimal compliance risk. Network moats built purely on coordination lock-in face both regulatory pressure and elevated information blocking risk.

## The Strategic Commoditizers: Inverting the Hold-Up Problem

The most interesting category might be the companies that have built entire business models around *preventing* opportunistic hold-up by eliminating information asymmetry.

Medplum open-sourced their "headless EHR" backend. The code is free. Anyone can inspect it, fork it, modify it. This is the opposite of data blocking—it's radical transparency. But they're not a charity; they're a business. Their model is selling managed hosting, support, and implementation expertise. They've intentionally commoditized one layer of the stack (the data storage and API layer) to enable customers to build their own workflow moats on top.

In TCE terms, Medplum has strategically eliminated one source of opportunism (vendor lock-in at the data layer) to compete on a different dimension (implementation quality and operational reliability). They're betting that by removing the hold-up risk, they can win on legitimate asset specificity—the relationship-specific knowledge they build by helping customers implement and operate the system. Compliance risk? Zero. Their entire business model is predicated on data liquidity.

Metriport operates on the same principle. They open-sourced their HIE and API connection infrastructure. The value isn't in the code—it's in operating a reliable, managed "network of networks" that handles all the complexity of connecting to disparate data sources. They've commoditized the connection layer to compete on execution quality.

These companies represent a fascinating strategic move in TCE terms. By voluntarily giving up the ability to engage in opportunistic hold-up, they've repositioned themselves to win on dimensions where the Cures Act is actually an advantage. More data liquidity means more integration complexity, which means more demand for their services. They've aligned their business model with the regulatory direction rather than fighting against it. Whether this open-source strategy ultimately wins in healthcare remains to be seen—none of these players have yet captured their markets—but it's a model worth watching as the competitive landscape continues to evolve.

## Compliance Risk Follows Business Model

The Cures Act doesn't threaten all vendor lock-in equally. It creates dramatically different compliance risk profiles based on what kind of moat you've built.

Transaction Cost Economics gives us the language to see this clearly. Asset specificity that emerges from deep implementation, co-developed workflows, and relationship-specific investments creates minimal compliance risk. Asset specificity that's manufactured through data control and artificial switching costs creates existential compliance risk.

The companies that should be worried are the ones that confused data control with sustainable competitive advantage. The ones that invested deeply in implementation—that built genuine procedural and human asset specificity into their products—can sleep soundly.

The battle has shifted from who hoards data to who enables its use most effectively. And from a compliance perspective, that's exactly where regulators want it.  