# Citation Provenance Audit

**Purpose:** trace every headline statistic the ILG framework cites to its primary source, and record how far each trace currently goes. The research entries quote these numbers. This file is where their provenance lives. Check a statistic's status here before quoting it outside this repository.

**Status vocabulary:**

- **Primary linked.** The repo links the original study, report, or announcement. A stable rehosted copy of the original text counts, and is noted.
- **Primary cited.** The original study is fully cited but not linked. Retrievable through any library.
- **Primary named.** The original study is identified, but every working link is secondary (press coverage, an aggregator, a vendor blog). Verify against the original before external use.
- **Unverified.** No primary source is confirmed. Do not cite externally.

**Last reviewed:** 2026-08-28.

---

## Project delivery outcomes (Standish Group CHAOS)

| Statistic | Cited in | Primary source | Status |
|---|---|---|---|
| 16.2% success, 52.7% challenged, 31.1% canceled (n = 3,682) | [fear-of-failure.md](../fear-of-failure.md) | Standish Group, *CHAOS Report* (1994) | **Primary linked.** Rehosted copy: [utdallas.edu PDF](https://www.utdallas.edu/~chung/SYSM6309/chaos_report.pdf). |
| 189% average cost overrun on challenged projects | [fear-of-failure.md](../fear-of-failure.md) | Standish Group, *CHAOS Report* (1994) | **Primary linked** (same PDF). A 1994 Standish figure. See discrepancy 3. |
| 42% of proposed features delivered (large organizations) | this audit | Standish Group, *CHAOS Report* (1994) | **Primary linked** (same PDF). |
| Later-year rates: 37/42/21 (2012), 31/50/19 (2020) | this audit | Standish Group, CHAOS research (2012, 2020) | **Primary named.** Repo links only summaries ([OpenCommons](https://opencommons.org/CHAOS_Report_on_IT_Project_Outcomes)). The recent reports are paywalled. |
| Success by company size: 9% large, 16.2% medium, 28% small | this audit | Standish Group, *CHAOS Report* (1994) | **Primary linked.** Rehosted copy: [ResearchGate](https://www.researchgate.net/publication/263849222_The_Chaos_Report). |
| 84% failure/challenged rate, attributed to 2020 | [fear-of-failure.md](../fear-of-failure.md) | see discrepancy 2 | **Unverified as stated.** 83.8% is the 1994 figure. The 2020 figures above sum to 69%. |

## Large-scale IT projects (McKinsey and University of Oxford)

| Statistic | Cited in | Primary source | Status |
|---|---|---|---|
| 45% average budget overrun, 7% schedule overrun, 56% less value than predicted (projects over $15M, n > 5,400) | [fear-of-failure.md](../fear-of-failure.md), this audit | McKinsey & Company with the BT Centre for Major Programme Management, University of Oxford, "Delivering large-scale IT projects on time, on budget, and on value" (2012) | **Primary linked** ([article](https://www.mckinsey.com/capabilities/tech-and-ai/our-insights/delivering-large-scale-it-projects-on-time-on-budget-and-on-value), [PDF](https://www.mckinsey.com/~/media/McKinsey/dotcom/client_service/BTO/PDF/MOBT_27_Delivering_large-scale_IT_projects_on_time_budget_and_value.ashx)). |
| 17% of large projects threaten the existence of the company (overruns of 200 to 400%) | [fear-of-failure.md](../fear-of-failure.md) | same study | **Primary linked.** |
| $66B total cost overrun in the sample. Expected overrun grows 15 percentage points per additional year of schedule | this audit | same study | **Primary linked.** |

## Software quality cost (CISQ)

| Statistic | Cited in | Primary source | Status |
|---|---|---|---|
| $2.41T total cost of poor software quality in the US (2022) | [fear-of-failure.md](../fear-of-failure.md) | CISQ, *The Cost of Poor Software Quality in the US: A 2022 Report* | **Primary linked** ([report page](https://www.it-cisq.org/the-cost-of-poor-quality-software-in-the-us-a-2022-report/), [PDF](https://www.it-cisq.org/wp-content/uploads/sites/6/2022/11/CPSQ-Report-Nov-22-2.pdf)). |
| $1.52T accumulated technical debt (2022) | this audit | same report | **Primary linked.** |
| 650% increase in open-source supply-chain failures (2020 to 2021) | this audit | same report | **Primary linked.** |
| Roughly 33% of developer time spent on technical debt (13.5 hours of a 41-hour week) | this audit | same report | **Primary linked.** Conflicting figures elsewhere in the repo. See discrepancy 4. |
| 100× cost multiplier for post-deployment fixes vs. design-phase fixes | [fear-of-failure.md](../fear-of-failure.md), attributed to IBM/CISQ | attributed to IBM Systems Sciences Institute | **Unverified.** The original IBM study has never surfaced publicly and the figure circulates without provenance. Treat as illustrative, and do not cite externally. |

## Behavioral economics (loss aversion and personal value)

| Statistic | Cited in | Primary source | Status |
|---|---|---|---|
| λ ≈ 2.25, α, β ≈ 0.88 | [prospect-theory.md](../prospect-theory.md), [fear-of-failure.md](../fear-of-failure.md), Constitution | Tversky & Kahneman (1992), "Advances in Prospect Theory," *Journal of Risk and Uncertainty*, 5(4) | **Primary cited.** Supported by a 2024 meta-analysis across 30+ studies ([*Journal of Economic Psychology*, indexed at RePEc](https://ideas.repec.org/a/eee/joepsy/v103y2024ics0167487024000485.html)). |
| Personal Value carries 2× the impact of Business Value on purchase outcomes | [prospect-theory.md](../prospect-theory.md) | CEB Marketing Leadership Council with Google and Motista, "From Promotion to Emotion" (2013) | **Primary linked** ([whitepaper PDF](https://www.thinkwithgoogle.com/_qs/documents/3988/promotion-emotion-b2b_articles_q5pm53H.pdf)). |
| 14% of buyers perceive enough differentiation to pay a premium. 86% perceive little or no difference between suppliers | [prospect-theory.md](../prospect-theory.md) | same whitepaper | **Primary linked.** |
| 71% purchase likelihood and 8× premium likelihood when high Personal Value is present | [prospect-theory.md](../prospect-theory.md) | same whitepaper | **Primary linked.** |

## Buyer indecision and regret (JOLT, Gartner)

| Statistic | Cited in | Primary source | Status |
|---|---|---|---|
| 40 to 60% of qualified pipeline lost to No Decision | [fear-of-failure.md](../fear-of-failure.md), [costly-signals.md](../costly-signals.md), [buying-center-dynamics.md](../buying-center-dynamics.md), [channel-collapse.md](../channel-collapse.md) | Dixon & McKenna, *The JOLT Effect* (2022), from 2.5M recorded sales conversations | **Primary cited** ([book site](https://www.jolteffect.com/)). Repo also links a [Gong interview](https://podcast.gong.io/public/76/Reveal%3A-The-Revenue-Intelligence-Podcast-05b3e1e1/af9f3a56) as a secondary summary. |
| 56% of No Decision losses driven by indecision (Fear of Messing Up) rather than status quo preference | [fear-of-failure.md](../fear-of-failure.md), [costly-signals.md](../costly-signals.md) | same book | **Primary cited.** The repo previously carried both 56% and 60%. Standardized to 56% on 2026-08-28. See discrepancy 1. |
| FOMO tactics backfire in 84% of cases with indecisive buyers | [fear-of-failure.md](../fear-of-failure.md) | same book | **Primary cited.** |
| 56% of organizations report significant regret over their largest recent tech purchase | [fear-of-failure.md](../fear-of-failure.md) | Gartner, technology buying behavior survey (2022) | **Primary named.** Repo links are secondary ([RouteSmart](https://www.routesmart.com/preventing-buyers-remorse-survey-report/), [Talking Logistics](https://talkinglogistics.com/2023/04/05/preventing-buyers-remorse-with-supply-chain-technology/)). Locate the Gartner announcement before external use. |
| Regret causes: 52% unmet functional requirements, 44% longer implementations, 41% insufficient implementation resources | this audit | same Gartner survey | **Primary named.** |
| 61 to 75% of buyers prefer a rep-free experience | this audit | Gartner buyer research | **Primary named.** The only repo link is an unrelated [Experian blog](https://www.experian.co.uk/blogs/latest-thinking/automated-credit-decisions/digital-onboarding-experience/). The weakest chain in this audit. |
| Personalization effects: 3.2× regret risk (passive), 2.3× decision confidence (active), 1.8× premium likelihood | this audit | Gartner survey of 1,464 B2B and B2C buyers (2025) | **Primary linked** ([press release](https://www.gartner.com/en/newsroom/press-releases/2025-06-03-gartner-survey-reveals-personalization-can-triple-the-likelihood-of-customer-regret-at-key-journey-points)). |

## AI implementation gap

| Statistic | Cited in | Primary source | Status |
|---|---|---|---|
| Roughly 80% of AI projects fail, twice the rate of traditional IT projects | this audit | RAND Corporation, "The Root Causes of Failure for Artificial Intelligence Projects and How They Can Succeed" (2024), 65 practitioner interviews | **Primary named.** Repo links are blog summaries. The report is freely available from RAND. Link it directly on the next pass. |
| 30% of GenAI projects abandoned after proof of concept by end of 2025 | [fear-of-failure.md](../fear-of-failure.md), this audit | Gartner press announcement (2024) | **Primary named.** |
| 10/20/70 effort split (algorithms / infrastructure / people and process) | this audit | unclear | **Unverified.** Circulates in consulting commentary. The repo's chain (a Medium post attributing it to RAND and McKinsey) does not establish it. |

---

## Discrepancies found

The point of a provenance audit is to catch drift between files. Open items, most severe first:

1. **FOMU share of No Decision: resolved.** [costly-signals.md](../costly-signals.md) said 60% and [fear-of-failure.md](../fear-of-failure.md) said 56%. The JOLT figure is 56%. costly-signals.md was corrected on 2026-08-28.
2. **"84% failure/challenged (Standish, 2020)" is a year/figure mismatch.** 83.8% is the 1994 figure. The 2020 figures put challenged plus failed at 69%. Correct the year or the number in [fear-of-failure.md](../fear-of-failure.md).
3. **"189% budget overruns on large projects (McKinsey)" is misattributed.** 189% is the Standish 1994 average overrun on challenged projects. The McKinsey large-project average is 45%. The statistics list in [fear-of-failure.md](../fear-of-failure.md) carries the misattribution, and its "zombie projects" claim (50 to 53% of projects, 189% over budget, 56% less value) welds the Standish overrun to the McKinsey value shortfall under one label. Rewrite against the primaries.
4. **Developer time on technical debt appears as three different values.** [fear-of-failure.md](../fear-of-failure.md) says 69% of dev time. [re-aim-framework.md](../re-aim-framework.md) says 44.1 hours per week, which exceeds the work week it implies. The CISQ 2022 primary supports roughly 33% (13.5 hours of a 41-hour week). Reconcile both files to the CISQ figure or cite a different primary.
5. **"45% timeline slippage" conflates two McKinsey numbers.** The primary reports 45% budget overrun and 7% schedule overrun. Fix in [fear-of-failure.md](../fear-of-failure.md).
6. **Buying group size (6 to 10 decision makers, Gartner)** is flagged unverified inline in [buying-center-dynamics.md](../buying-center-dynamics.md). Still open.

## Not yet traced

Statistics quoted in research entries with no provenance row yet. Add a row when each is verified:

- 61% of deals lost to No Decision (Genius Drive), in [prospect-theory.md](../prospect-theory.md).
- 60% renewal regret (Gartner, 2023), in [fear-of-failure.md](../fear-of-failure.md) and [game-theory-and-nrr.md](../game-theory-and-nrr.md).
- Churn, clawback, and Sales-CS alignment figures in [game-theory-and-nrr.md](../game-theory-and-nrr.md): 15% churn reduction, 36% retention improvement, 38% win-rate improvement, 46% valuation discount.
- SaaS utilization figures in [re-aim-framework.md](../re-aim-framework.md): license waste, DAU/MAU ratios, feature-use concentration. Zylo's 2025 index is linked there as primary, but the figures have not been checked against it line by line.
- 106 to 275 SaaS applications per enterprise and 47% utilization, in [fear-of-failure.md](../fear-of-failure.md).
- Email volume growth (293B to 376B per day) and reply-rate decline (8.5% to 3.4%), in [channel-collapse.md](../channel-collapse.md).
- Hershey (1999) and Nike i2 (2000) failure figures, in [transaction-cost-economics.md](../transaction-cost-economics.md).

## Maintaining this file

- A new headline statistic anywhere in `theory/` gets a row here in the same commit, with an honest status.
- A status moves up only when someone opens the primary source and checks the number against it.
- When two files disagree, record the disagreement here first, then fix the files against the primary.
