# Treatment On-Ramp: Evaluating Metriport
### Prepared for Zus by HTD

*Working draft. Brackets mark places to red-line or develop together.*

You asked us to evaluate Metriport across product, pricing, support, market perception, complex-market access, and partnerships. We did the work. The most valuable thing we can hand back is not the comparison itself. It is a verdict on which parts of it decide whether you win, and which are noise dressed as signal.

Two findings sit above the rest, and the document is built on them:

1. **Most of what is comparable does not decide the market.** Connectivity is commoditizing. The line items that fill a vendor grid are converging toward table stakes, and answering them correctly tells you almost nothing about who wins.
2. **Where the comparison might still matter, it cannot be trusted from outside.** We ran the same public research process you would, on both companies, and it produced confident, well-cited, demonstrably wrong answers.

What does decide the market is a smaller set of questions no public source can answer, plus one strategic choice about which game you are playing. We close there. Your full question list, with a one-line verdict on each, is in Appendix A.

---

## 1. What is comparable, and why it does not decide the market

The product comparison you asked for:

| Dimension | Metriport | Zus |
| --- | --- | --- |
| Data mart | No managed mart. Open-source dbt connector into the client's own warehouse (Snowflake, BigQuery, Redshift). Client funds compute and data engineering. | Managed Snowflake reader account. FHIR rectangularized into roughly 200 relational views. |
| Normalization | ICD-10-CM, SNOMED, LOINC, plus HCC and CCSR. | Deterministic normalization and dedup layer (Lenses). |
| Medications | Pharmaceutical Intelligence: PBMs, retail and cash-pay pharmacies, HIEs, direct Surescripts. | 12-month Surescripts lookback with event-driven Intelligent Refresh. |
| AI | Gated premium summaries, in a FHIR Binary resource (Base64) or rendered text. | Generated Patient Summaries, tagged `template` or `ai`. |
| Query lookback | No fixed cap. Depth set by the responding endpoint. | 12-month medication lookback documented. |
| Care gaps | Delegated to open-source Tuva. No proprietary engine found. | Risk data marts built on the Lenses layer. |

*Sources in Appendix B.* `[Brad red-line: Zus column. GPS GA date, the refresh-trigger list, the ~200 views figure.]`

A few more of your questions are answerable from public docs, so here they are, compressed:

- **"Open source"** applies to Metriport's connectors and transform logic, not the exchange itself, which HIPAA and TEFCA make impossible to open-source. It signals modularity to developer-led teams and matters far less to clinical and enterprise buyers.
- **EMRs.** Metriport documents integrations with AthenaOne, Canvas, Healthie, and Elation at varying depth (embedded modal, embedded panel, polling, ID mapping). Direct Carequality implementer since March 2024, plus CommonWell.
- **ADT.** Metriport's docs describe weekly batch roster processing. Events fire in near real time once a patient is enrolled, but panel management is batch, which points to HIE batch feeds rather than a real-time aggregator.

Now the verdict, which is the point of the section. **Even answered correctly and completely, none of this decides a deal.** Network access is commoditizing and the baseline is converging. Willingness to pay has already moved off raw connectivity and concentrated in enrichment and actionability: reconciliation, deduplication, real-time data, managed analytics. The one item above that is a real capability difference rather than a checkbox is ADT: you draw from real-time aggregators where Metriport runs a weekly batch. That is worth knowing. The rest is table stakes, and a buyer who chooses on it is choosing on the part of the market that no longer separates vendors.

## 2. Why even the comparable parts cannot be trusted from public research

This is the second reason a feature grid is a weak foundation, and we would rather show it than assert it. We ran the same public research process on both companies. It returned confident, sourced, wrong answers. A sample:

- **It described a different company.** Asked for Metriport's pricing, the run returned "metric creation, encrypted cloud backups, biometric locks, and 35 app themes." That is a consumer self-tracking app of the same name, with a shared founder. The process pulled the wrong company's FAQ and cited it with full confidence.
- **It invented a network connection.** The run claimed Metriport "supports secondary queries across the eHealth Exchange." Its documented connections are CommonWell and Carequality only. eHealth Exchange participants are reachable through Carequality, but Metriport documents no direct link. A fabricated fact, stated as fact.
- **It quoted a price it then disowned.** A circulating "$0.20 per user per month" traces to a single aggregator listing. The run surfaced it, then flagged and denied it in the same pass.

Then read your own column. The errors you catch on the company you know intimately are the gauge for the Metriport column you cannot check. `[Brad red-line ledger: GPS GA date and refresh triggers; the 5-day contribution penalty mechanics; the Type I/II purpose-of-use vetting description; any overstated Epic integration claim. The tally is the argument — careful run, company you know cold, this many errors.]`

The lesson is not "use a better prompt." It is that this class of research is structurally unreliable, and the unreliability is invisible exactly where you most need it: on the competitor you cannot independently check.

## 3. The questions that actually decide the market

Strip out the table stakes and the fabrications, and a smaller set of your questions remains. These decide deals. They share one property: no public source answers them, by us or by a better model, because the answers live in private contracts and in the heads of buyers.

- **Price discrimination and willingness to pay.** Both vendors are sales-gated. A point estimate is noise; price is conditional on stage, feature maturity, and deal context. The only reliable read is a blind, normalized survey of many real contracts.
- **Who staffs accounts, and how technical engagements feel.** The public record is directional at best (Metriport reads founder-led and engineering-heavy, YC S22, AWS-founded). Whether everyone gets technical-leadership access or only competitive accounts comes only from the buyers who lived it.
- **Where Zus loses the Bay Area room.** This is the most important question you asked, and it is not a product question. Silicon Valley buying from Silicon Valley is not a verdict on your product. It is Akerlof's market for lemons in plain view: when buyers cannot verify quality, they substitute a signal they trust, and proximity is the cheapest one available. The Valley trades within itself because it cannot tell the field apart on merit. That is an information failure, and it is fixable.

These are not gaps in this document. Together they are the specification for a primary-research instrument that does not yet exist in this niche. Hold that thought; it is the second half of what we propose.

## 4. The market underneath all of this

A pattern is forming, and it works against strong vendors and honest buyers at once.

- Connectivity becomes table stakes, and the baseline converges.
- The weight shifts to differentiation that is hard to prove from outside.
- The cost of telling real capability from claims rises, and so does the cost of getting your own organization to agree on whom to trust.
- So buyers take the shortcut. They route decisions through personal and geographic networks, and proximity stands in for proof.
- The market sorts on relationships, not merit, which is the worst possible outcome for the vendor with the strongest actual capability and the weakest proximity.

Economists call this a lemons market, after George Akerlof: when buyers cannot tell good from bad before they buy, they stop paying for quality they cannot verify. The cure is always the same. A credible third party closes the information gap, and quality becomes visible again.

## 5. Play your own game

A durable advantage is a capability that is hard to copy and aligned with where the market is heading. For Zus, that is operational depth: the demanding, unglamorous work of acquiring and normalizing messy state-HIE data for specific care models, the kind of work behind a customer like Imagine Pediatrics. High switching costs, hard to replicate, worth more as raw connectivity commoditizes.

Two postures exist here, and both are legitimate:

- **Depth.** Operations-integrated, does the hard data work, embeds in the customer. Slow to build, hard to dislodge. This is Zus.
- **Breadth.** Developer-led, horizontal, fast, oriented to the AI trend of the quarter. Wins on developer experience and reach, and carries more exposure to commoditization. This is the posture of Metriport and HealthEx.

The trap is a depth player adopting a breadth player's game while still carrying a depth player's cost structure. Chasing the Valley's enthusiasm of the quarter cedes the advantage you already hold.

Two structural facts reinforce that the depth game is the more defensible one right now:

- **Partnerships are lock-in by design.** When two vendors build complementary features for a shared customer, they co-invest in something specific to that relationship. Williamson's fundamental transformation describes what follows: a deal that began with many possible partners becomes a small-numbers, lock-in bargain once the specific investment is made. That co-dependence is a strength when the shared customer wins and a concentrated risk when they do not. It is a depth player's bargain, and breadth players cannot easily replicate it.
- **Access is tightening, and breadth carries more of the exposure.** `[Brad red-line / develop: the Epic v. Health Gorilla and GuardDog enforcement thread. Epic and co-plaintiffs sued over records retrieved under a false treatment assertion; a federal court entered a permanent injunction against GuardDog on April 2, 2026, barring it from Carequality and TEFCA. If this holds the way it reads, a breadth posture oriented to borderline purpose-of-use cases is structurally more exposed than a depth posture anchored in documentable treatment relationships.]`

## 6. What we propose

Two pieces of work follow from the diagnosis, in sequence.

**Phase one — strategy enablement (now).** We align your product and go-to-market around the game you can win, in a market large enough to be worth winning. Output: a defensible position, the evidence behind it, and a go-to-market motion built for a depth player rather than borrowed from a breadth one.

**Phase two — anchor the signal (next).** The questions in Section 3 cannot be answered from any public source. They can be answered by an independent, normalized survey of the treatment on-ramp niche and its adjacent niches: the credible third party this market is missing. We are offering Zus the anchor seat. You get first look and you help shape the instrument, including the dimensions on which depth is measured rather than assumed.

We want to be direct about the model, because the model is the point. This survey is independent, and it will serve the niche broadly rather than speak for any one vendor. That independence is the entire source of its value. A signal we issued on your behalf would be worth no more than your own marketing. A signal we issue across the niche, that happens to register what you have built, is worth more than either, for the precise reason that it is not yours to control. As the anchor, you benefit from it first and most, because you are the vendor whose real capability is currently hardest for the market to see.

What we will not do is trade on confidential client or project information, or represent inference as fact. Trust is the only thing that makes our read worth more than a search engine's. This document does not hand you a verdict on Metriport. It shows you where the public picture runs out, sorts your own questions into the ones that decide the market and the ones that do not, and points at the work that begins where the public picture ends.

`[Confirm our call: date.]`

Brad

---

## Appendix A — Your questions, with a verdict on each

| Your question | Verdict |
| --- | --- |
| Data Mart: included, bundled, costs extra, self-hosted? | Table stakes — answered, Section 1 |
| Which Surescripts products, and how | Table stakes — answered, Section 1 |
| AI summaries and other AI features | Table stakes — answered, Section 1 |
| How far back queries go | Table stakes — answered, Section 1 |
| Care gaps priced and packaged; beyond a Tuva connector | Table stakes — answered, Section 1 |
| "Open source" as a term: meaning, and whether it matters | Table stakes — answered, Section 1 |
| EMRs (Healthie, Elation, Canvas) | Table stakes — answered, Section 1 |
| Bundled ADTs: real partnerships or batch | Capability difference worth noting — Section 1 |
| Price discrimination strategy | Decides the market; needs primary research — Section 3 |
| Go-to-market team structure | Decides the market; needs primary research — Section 3 |
| Who is on the accounts | Decides the market; needs primary research — Section 3 |
| Technical-leadership access: all or only top accounts | Decides the market; needs primary research — Section 3 |
| How those engagements look and feel | Decides the market; needs primary research — Section 3 |
| Willingness to pay vs. commodity | Decides the market; needs primary research — Section 3 |
| Where Zus loses the Bay Area crowd | Decides the market; it is a lemons-market problem — Section 3 |
| Non-HIPAA entities (Sesame); does Epic respond | Compliance read; enforcement-driven — Section 5 `[develop]` |
| Borderline AI / Individual Access (Amazon Health AI) | Governance question; develop a position before writing — `[earmark]` |
| ACOs / Delegate of Authority | Mechanics documented; reciprocity is mandatory — `[develop]` |
| Better partnership terms (HIE, EMR) | Terms are under NDA; structure is predictable — Section 5 |

## Appendix B — Sources

**Gemini-sourced, Metriport**

1. Tuva connector: https://github.com/tuva-health/metriport_connector
2. FHIR Transforms for Analytics: https://www.metriport.com/blog/introducing-fhir-transforms-for-analytics
3. Coding systems overview: https://docs.metriport.com/medical-api/fhir/coding-systems/overview
4. Pharmaceutical Intelligence: https://www.metriport.com/blog/introducing-pharmaceutical-intelligence
5. AI Summaries: https://docs.metriport.com/medical-api/handling-data/ai-summaries
6. Start Network Query: https://docs.metriport.com/medical-api/api-reference/network/start-network-query
7. Quickstart / gated procurement: https://docs.metriport.com/medical-api/getting-started/quickstart
8. Y Combinator S22 reference: https://news.ycombinator.com/item?id=40456064
9. Epic statement and GuardDog injunction: https://www.epic.com/what-you-put-up-with-is-what-you-stand-for/
10. Epic v. Health Gorilla (HIPAA Journal): https://www.hipaajournal.com/epic-sues-health-information-exchange-network-improper-record-access/
11. Epic v. Health Gorilla (Womble Bond Dickinson): https://www.womblebonddickinson.com/us/insights/blogs/interoperability-meets-litigation-what-epic-v-health-gorilla-means-mass-torts
12. Contributing Data: https://docs.metriport.com/medical-api/handling-data/contribution
13. EHR Apps overview: https://docs.metriport.com/ehr-apps/overview
14. Real-time Patient Notifications: https://docs.metriport.com/medical-api/handling-data/realtime-patient-notifications
15. Metriport Joins Carequality: https://www.metriport.com/blog/metriport-joins-carequality
16. A Network of Networks: https://www.metriport.com/blog/a-network-of-networks-the-new-internet-of-healthcare-data

**Gemini-sourced, Zus**

17. Zus data marts: https://docs.zushealth.com/docs/data-marts
18. Snowflake reader account: https://docs.zushealth.com/docs/access-via-snowflake-reader-account
19. Pharmacy network: https://docs.zushealth.com/docs/pharmacy-network
20. Clinical data contribution policy: https://docs.zushealth.com/docs/clinical-data-contribution-policy
21. TEFCA concepts: https://docs.zushealth.com/docs/tefca-concepts
22. Service Level Agreement: https://zushealth.com/zus-service-level-agreement/
23. Medical History Service terms: https://zushealth.com/medical-history-service-terms/
24. Series B financing: https://zushealth.com/zus-health-closes-financing-signs-partnership-with-elation-health-to-accelerate-growth-of-its-data-service-to-provide-connective-tissue-for-healthcare/

**Our verification (error checks and references)**

25. Metriport consumer tracker FAQ: https://metriport.ai/faq.html
26. TechCrunch on the consumer tracker app: https://techcrunch.com/2022/02/17/metriport-merrily-measures-your-me-verse/
27. HealthEx: https://www.healthex.io/
