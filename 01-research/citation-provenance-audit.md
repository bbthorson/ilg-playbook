# Longitudinal Analysis of IT Implementation Failures and the Behavioral Economics of B2B Procurement Risk

The paradigm of Implementation-Led Growth (ILG) is predicated on the empirical reality that the acquisition of enterprise technology is increasingly decoupled from its successful deployment and utilization. This disconnect creates a pervasive environment of "purchase regret" and "no-decision" paralysis, fundamentally altering the commercial landscape for B2B vendors. The following report provides an exhaustive provenance audit of the quantitative foundations supporting the ILG framework, drawing upon three decades of project performance data, macroeconomic cost assessments, and behavioral economic research into the mechanics of human choice under uncertainty.

## The Chronic Crisis of IT Project Delivery and Resolution

The foundational premise of the Implementation-Led Growth framework is the persistent high failure rate of information technology initiatives. This phenomenon is most extensively documented by the Standish Group's CHAOS Reports, a series of longitudinal studies that have tracked software project outcomes since the mid-1990s. The data suggests that the vast majority of IT projects fail to achieve their intended baseline objectives of being on-time, on-budget, and fully featured.

### Historical Benchmarks and the Definition of Failure

In the seminal 1994 Standish Group survey, which analyzed a sample of 3,682 projects, the success rate—defined as projects completed on-time and on-budget—was a meager 16.2%.¹ The remaining 83.8% of projects were classified as either "challenged" or "failed".³ Specifically, 31.1% of projects were canceled before completion (Resolution Type 3), while 52.7% were completed but exceeded their original time and cost estimates or delivered fewer features than originally specified (Resolution Type 2).¹

The depth of these failures was particularly staggering in terms of financial overruns and utility shortfalls. Challenged projects in the 1994 sample experienced an average budget overrun of 189% of the original estimate.¹ Furthermore, even when projects reached completion, they typically delivered only a fraction of their planned utility; in large organizations, completed projects averaged only 42% of their originally proposed features and functions.¹

| Project Outcome Category (1994 Sample) | Percentage of Total Projects | Average Cost Overrun | Features Delivered |
| :---- | :---- | :---- | :---- |
| Resolution Type 1: Successful | 16.2% | 0% | 100% |
| Resolution Type 2: Challenged | 52.7% | 189% | ~42% (Large Orgs) |
| Resolution Type 3: Failed/Canceled | 31.1% | N/A (Total Loss) | 0% |

Data synthesized from.¹

### Evolution of Project Outcomes (1994–2020)

Over the subsequent decades, while the absolute success rates have shown some improvement, the overall landscape remains dominated by "challenged" initiatives. By 2012, the CHAOS data indicated that 37% of projects were successful, 42% were challenged, and 21% failed.¹ However, more recent data from 2020 suggests a regression in these metrics, with successful projects falling to 31%, while 50% remained challenged and 19% failed outright.¹

This volatility in success rates is often attributed to the increasing complexity of software environments and the shift in methodological preferences. The 2020 CHAOS Report highlighted a controversial finding regarding the role of project management: it suggested that the success rate for projects led by highly skilled managers using non-Agile methods was only 23%, whereas projects without a formal manager in certain contexts saw success rates rise to 58%.⁵ The Standish Group concluded that project managers often generate unnecessary paperwork, which increases decision-making latency and slows progress, advocating instead for continuous development and "small increments".⁵

### Organizational Size as a Determinant of Success

A critical nuance identified in the Standish research is the inverse relationship between organizational size and project success. Large companies (those with over $500 million in annual revenue) face significantly higher failure rates than their smaller counterparts.²

| Company Size (Revenue) | Successful Projects | Challenged Projects | Canceled Projects |
| :---- | :---- | :---- | :---- |
| Large (>$500M) | 9% | 61.5% | 29.5% |
| Medium ($200M-$500M) | 16.2% | 46.7% | 37.1% |
| Small ($100M-$200M) | 28% | 50.4% | 21.6% |

Data sourced from.²

The disproportionate failure rate in large organizations is driven by factors such as lack of user input (12.8%), incomplete requirements (12.3%), and shifting specifications (11.8%).² These findings underscore the "implementation gap" that the Implementation-Led Growth framework seeks to mitigate by focusing on early and continuous validation of value rather than monolithic delivery schedules.

## The Macroeconomic Cost of Implementation Risk and Software Quality

The individual failure of a single project, while problematic, represents only the micro-level manifestation of a much larger macroeconomic crisis. Research by McKinsey & Company, the University of Oxford, and the Consortium for Information & Software Quality (CISQ) provides a broader view of the systemic risks and costs associated with poor implementation and software quality.

### Large-Scale IT Projects and "Black Swan" Events

Research conducted by McKinsey in collaboration with the BT Centre for Major Programme Management at the University of Oxford examined more than 5,400 IT projects with initial budgets exceeding $15 million.⁶ This study identified that while the "average" large IT project runs 45% over budget and 7% over time while delivering 56% less value than predicted, the true danger lies in the "tail risk" or "black swan" events.⁷

Approximately 17% of large-scale IT projects go so catastrophically wrong that they threaten the very existence of the company.⁶ These "black swan" projects are characterized by budget overruns of 200% to 400%.⁷ The total cost overrun for the projects in the McKinsey sample was $66 billion, a figure exceeding the GDP of Luxembourg at the time.⁷

| Project Risk Metric (Projects >$15M) | Statistical Average |
| :---- | :---- |
| Average Budget Overrun | 45% |
| Average Schedule Overrun | 7% |
| Average Value Shortfall | -56% |
| Risk of "Black Swan" (Threatens Existence) | 17% |

Data sourced from.⁷

A key finding of this research is that project duration is a primary driver of cost overruns. For every additional year a project is scheduled to last, the expected cost overrun increases by 15%.⁷ This reinforces the core ILG principle that reducing implementation cycles and focusing on "short delivery cycles" is essential for mitigating existential risk.⁷

### The $2.41 Trillion Tax on the US Economy

The aggregate impact of these failures is quantified by CISQ in their 2022 biennial report on the Cost of Poor Software Quality (CPSQ). The report estimates that the cost of poor software quality in the U.S. has grown to at least $2.41 trillion.¹¹ This figure represents approximately 10% of the U.S. GDP.¹⁴

The primary drivers of this cost are:

1. **Software Failures:** Issues arising from poor quality and vulnerabilities.
2. **Legacy System Issues:** Costs associated with maintaining and operating antiquated infrastructure.
3. **Technical Debt (TD):** The accumulated cost of rework and "shortcut" development.¹¹

Technical debt alone reached an estimated $1.52 trillion in 2022.¹¹ This debt serves as a perpetual "silent tax" on engineering organizations, with the average developer spending approximately 23% to 33% of their time—roughly 13.5 hours of a 41-hour work week—specifically addressing technical debt rather than building new value.¹¹

| CISQ 2022 Cost Component | Estimated Impact |
| :---- | :---- |
| Total Cost of Poor Software Quality (CPSQ) | $2.41 Trillion |
| Accumulated Technical Debt (TD) | $1.52 Trillion |
| Impact of Cybercrime (Software Vulnerabilities) | 64% increase (2020-21) |
| Software Supply Chain Failure Increase | 650% increase (2020-21) |

Data sourced from.¹¹

The rising cost of poor quality is further exacerbated by the increasing reliance on Open Source Software (OSS) and third-party components. Failures due to weaknesses in open-source software supply chains increased by 650% between 2020 and 2021.¹³ These figures illustrate that "implementation" is no longer a localized event but a continuous process of managing technical debt and security vulnerabilities across a globalized supply chain.

## Behavioral Economic Foundations of B2B Decision-Making

The high failure rates and astronomical costs of IT projects create a psychological landscape for B2B buyers that is dominated by risk aversion and the fear of professional failure. Understanding the mechanics of these decisions requires an application of Prospect Theory and an analysis of the "personal value" at stake for the individual decision-maker.

### Loss Aversion and the Mathematics of λ

The behavioral economic foundation for implementation-led growth is rooted in the work of Amos Tversky and Daniel Kahneman. In their 1992 paper, "Advances in Prospect Theory: Cumulative Representation of Uncertainty," they experimentally estimated the loss-aversion parameter (λ) at approximately 2.25.¹⁵

Loss aversion refers to the psychological observation that the subjective pain of a loss is significantly greater than the subjective pleasure of an equivalent gain. Specifically, the value function v(x) in Prospect Theory is defined with the parameters α = β = 0.88 and λ = 2.25.¹⁶ This implies that a loss of $1,000 has a psychological impact more than twice as severe as the positive impact of a $1,000 gain.

In a B2B procurement context, this λ parameter explains the extreme difficulty of unseating the "status quo." A buyer perceives the potential benefits of a new software implementation (the gains) but weights the risk of project failure (the loss) twice as heavily. Since software failure can lead to "career-altering" risks—such as the loss of a job or a stalled promotion—the default rational choice for the individual is often to avoid the decision entirely.¹⁸

### The Impact of Personal Value vs. Business Value

Research conducted by the CEB (now Gartner), in partnership with Google and Motista, further clarifies this psychological dynamic. Their study, "From Promotion to Emotion: Connecting Customers to B2B Brands," found that "personal value" has twice the impact on the commercial outcome compared to "business value".¹⁸

Personal value is driven by factors such as career advancement, professional pride, and social benefits within the organization.¹⁹ Conversely, business value (e.g., product features, ROI, efficiency) is often viewed as "table stakes." The study found that while leading brands in a given industry are perceived to have similar levels of business value, the differentiation lies in the emotional connection and personal value they offer.¹⁹

| Perception Category | Key Statistic |
| :---- | :---- |
| Personal Value Impact | 2x impact of Business Value on purchase |
| Differentiation Perception | Only 14% of buyers perceive enough difference to pay a premium |
| Emotional Connection (B2B) | Lowest-scoring B2B brands achieve connections (~40%) equal to top B2C brands |
| Preference for Premium | Buyers are 8x more likely to pay a premium when Personal Value is present |

Data sourced from.¹⁸

The CEB study also highlighted a startling commoditization crisis: 86% of B2B buyers perceive little to no real difference between supplier offerings, and only 14% are willing to pay a premium for perceived differentiation.¹⁹ This high degree of perceived commoditization, combined with the extreme personal risks of project failure, leads to a "one of three" problem: customers conclude that the top three leaders in an industry all deliver acceptable business value, making the decision purely about which vendor minimizes their personal risk of "messing up".²⁰

## The JOLT Effect: Overcoming the Crisis of Indecision

The convergence of high implementation failure rates and extreme loss aversion has led to a "secular trend" of sales cycles ending in "no decision." This is the central thesis of "The JOLT Effect" by Matt Dixon and Ted McKenna, whose research analyzed 2.5 million sales conversations captured during the COVID-19 pandemic.²²

### The 40–60% "No Decision" Baseline

The JOLT research indicates that 40% to 60% of all qualified sales pipeline is lost not to a competitor, but to "no decision".²² This represents a massive "deadweight loss" and productivity sink for sales organizations. The core discovery of this research is that "no decision" is driven by two distinct psychological factors:

1. **Status Quo Bias:** The belief that the current way of doing things is "good enough."
2. **Indecision:** The "Fear of Messing Up" (FOMU), driven by the fear of making a high-stakes mistake.²²

### The Backfire of FOMO Tactics

Conventional sales training suggests that if a customer is stuck, the salesperson should "hammer the ROI" or use Fear of Missing Out (FOMO) to emphasize the "pain of the same." However, the JOLT research found that this approach backfires in 84% of cases where the buyer is experiencing indecision.²²

When a buyer is terrified of making the wrong choice (Outcome Risk), increasing the pressure by highlighting the cost of doing nothing only makes them more anxious. This triggers the "paradox of personalization" where the seller is addressing the wrong problem; they are fighting the Status Quo Bias when the actual issue is the buyer's internal fear of failure.²² To overcome this, top-performing sales reps use the JOLT method to "Take Risk off the Table" and provide a "personal seal of approval" through implementation-led validation.²²

| Sales Tactic | Success/Backfire Rate with Indecisive Buyers |
| :---- | :---- |
| FOMO/ROI Hammering | 84% Backfire Rate |
| JOLT Method (Risk Mitigation) | Higher probability of closing "indecisive" deals |
| Deals Lost to No Decision | 40% to 60% |

Data sourced from.²²

## The AI Implementation Gap: From Proof-of-Concept to Production

The most recent wave of implementation failure is occurring in the domain of Artificial Intelligence. Despite the aggressive deployment of Generative AI (GenAI) initiatives, the transition from proof-of-concept (POC) to production remains a formidable barrier.

### The 80% AI Project Failure Rate

A 2024 report by the RAND Corporation, titled "The Root Causes of Failure for Artificial Intelligence Projects and How They Can Succeed," found that approximately 80% of AI projects fail.²³ This is notably twice the failure rate of traditional IT projects that do not involve AI components.²⁵

Based on structured interviews with 65 experienced data scientists and engineers, the RAND report identified five leading causes for these failures:

1. **Misunderstanding/Miscommunicating the Problem:** Stakeholders fail to define the specific business problem being solved.²⁶
2. **Lack of Necessary Training Data:** Organizations discover their "data-driven" claims collapse when AI systems require consistent, clean information.²⁶
3. **Prioritizing Technology over Problem-Solving:** Focusing on "latest and greatest" models rather than user needs.²⁶
4. **Inadequate Infrastructure:** Lack of data governance and deployment environments.²⁶
5. **Infeasibility:** Applying AI to problems that are simply too difficult for the current state of the technology.²⁶

### The GenAI Abandonment Crisis

The implementation crisis in AI is particularly acute in GenAI. Gartner estimates that by the end of 2025, at least 30% of GenAI projects will be abandoned after the proof-of-concept stage.²³ This abandonment is driven by poor data quality, escalating costs, and the "last mile" problem—the difficulty of moving from a working prototype to a production-ready system at enterprise scale.²⁶

A second-order insight from the RAND and McKinsey data is the "10/20/70" rule for successful AI deployment: 10% of the effort is in building the algorithm, 20% is in the technology and data infrastructure, and 70% is in the people, processes, and workflow redesign.²⁶ Organizations that fail to allocate the bulk of their resources to the "human" side of implementation are almost certain to join the 80% failure statistic.

## The Future of the Buyer Journey: Regret and Rep-Free Preferences

As the B2B buyer journey becomes increasingly digitized, the risks of "purchase regret" and "information overwhelm" are intensifying. The Implementation-Led Growth framework must therefore adapt to a world where buyers prefer limited human interaction but still face high levels of anxiety.

### The 56% Purchase Regret Benchmark

A 2022 survey by Gartner found that 56% of organizations experienced a high degree of purchase regret over their largest tech-related purchase in the previous two years.²⁸ This regret is frequently caused by technology that fails to meet functional requirements (52%) or implementations that take longer and require more resources than the vendor indicated (44%).²⁸

Internal factors also contribute significantly to this regret, including insufficient resources assigned to implementation (41%) and a lack of thorough due diligence (37%).²⁸ This creates a "blind spot" in the procurement process where the focus on selecting the tool overshadows the requirements for successfully implementing it.

### The Personalization Paradox and Rep-Free Buying

Gartner research also indicates a significant shift in buyer behavior, with 61% to 75% of buyers expressing a preference for a "rep-free" experience.⁸ However, this preference for self-service is often at odds with the complexity of the decisions being made.

In an effort to guide these self-service buyers, many organizations have implemented personalization strategies. However, a 2025 Gartner survey of 1,464 B2B and B2C buyers found that "passive" personalization (e.g., "next best action" recommendations) can actually be counterproductive. Customers who experienced negative personalization were 3.2x more likely to regret a purchase and 44% less likely to purchase again.³⁰

| Personalization Metric (2025 Gartner Survey) | Impact |
| :---- | :---- |
| Risk of Regret (Passive Personalization) | 3.2x Increase |
| Probability of Paying a Premium | 1.8x Increase (but accompanied by 2x overwhelm) |
| Impact of "Active" Personalization | 2.3x more likely to confidently complete decision |

Data sourced from.³⁰

The "paradox of personalization" occurs because passive tactics often intensify negative emotions when customers are trapped in decision-making pitfalls, such as task-switching from searching to selecting. Conversely, "active" personalization—which involves interactive experiences like quizzes and guided assessments that clarify customer goals—leads to a 2.3x increase in confident decision-making and improved marketing ROI.³⁰

## Synthesis: Strategic Implications for Implementation-Led Growth

The quantitative evidence presented in this audit confirms that the primary barrier to B2B growth is not a lack of interest or product features, but a pervasive and rational fear of implementation failure. The core claims of the Implementation-Led Growth playbook are supported by a rigorous cross-disciplinary body of research.

1. **The Delivery Crisis is Real and Persistent:** The Standish Group's decades-long tracking shows that over 80% of IT projects continue to struggle with overruns and utility shortfalls.¹ This provides the foundational "pain" that the ILG framework addresses.
2. **The Risk is Asymmetric and Existential:** For large enterprises, the 17% "black swan" risk means that implementation is not just an IT concern but a board-level risk management issue.⁷
3. **Psychology Dominates Procurement:** With a loss-aversion parameter of 2.25 and "personal value" carrying twice the weight of "business value," the vendor that minimizes the personal risk of implementation failure will always outperform the one that merely promises ROI.¹⁶
4. **The "No Decision" Default is the Primary Competitor:** The 40-60% loss rate to indecision is the direct result of the FOMU (Fear of Messing Up) exceeding the FOMO (Fear of Missing Out).²²
5. **Quality is the Ultimate Multiplier:** The $2.41 trillion cost of poor software quality and the 23% "tax" of technical debt are the structural headwinds that slow every transformation.¹¹

In conclusion, the Implementation-Led Growth framework is an essential response to a market where the traditional sales model—based on promotion and feature-driven differentiation—has failed. By aligning growth strategies with the reality of implementation risk, organizations can overcome the paralysis of the modern buyer and bridge the gap between technical promise and commercial reality.

---

## Works Cited

1. CHAOS Report on IT Project Outcomes - OpenCommons, accessed February 26, 2026, [https://opencommons.org/CHAOS_Report_on_IT_Project_Outcomes](https://opencommons.org/CHAOS_Report_on_IT_Project_Outcomes)
2. (PDF) The Chaos Report - ResearchGate, accessed February 26, 2026, [https://www.researchgate.net/publication/263849222_The_Chaos_Report](https://www.researchgate.net/publication/263849222_The_Chaos_Report)
3. This is Why So Many IT Projects Fail: A Wrap-up - People First Project Management, accessed February 26, 2026, [https://peoplefirstprojectmanagement.com/this-is-why-so-many-it-projects-fail-a-wrap-up/](https://peoplefirstprojectmanagement.com/this-is-why-so-many-it-projects-fail-a-wrap-up/)
4. THE STANDISH GROUP REPORT CHAOS, accessed February 26, 2026, [https://www.utdallas.edu/~chung/SYSM6309/chaos_report.pdf](https://www.utdallas.edu/~chung/SYSM6309/chaos_report.pdf)
5. Chaos Report — why this study about IT project management is so unique, accessed February 26, 2026, [https://thestory.is/en/journal/chaos-report/](https://thestory.is/en/journal/chaos-report/)
6. Build vs. Buy Dilemma: Choosing a Digital Commerce Platform | CloudBlue, accessed February 26, 2026, [https://www.cloudblue.com/app/uploads/2021/11/White-paper-Build-vs.-Buy-Dilemma%E2%80%94Choosing-a-Digital-Commerce-Platform.pdf](https://www.cloudblue.com/app/uploads/2021/11/White-paper-Build-vs.-Buy-Dilemma%E2%80%94Choosing-a-Digital-Commerce-Platform.pdf)
7. Delivering large-scale IT projects on time, on budget ... - McKinsey, accessed February 26, 2026, [https://www.mckinsey.com/~/media/McKinsey/dotcom/client_service/Corporate%20Finance/MoF/PDF%20issues/PDFs%20Issue%2045/Final/MoF45_LargeScaleIT.ashx](https://www.mckinsey.com/~/media/McKinsey/dotcom/client_service/Corporate%20Finance/MoF/PDF%20issues/PDFs%20Issue%2045/Final/MoF45_LargeScaleIT.ashx)
8. There are multiple challenges to creating a great digital experience - Experian UK, accessed February 26, 2026, [https://www.experian.co.uk/blogs/latest-thinking/automated-credit-decisions/digital-onboarding-experience/](https://www.experian.co.uk/blogs/latest-thinking/automated-credit-decisions/digital-onboarding-experience/)
9. Delivering large-scale IT projects on time, on budget, and on value - McKinsey, accessed February 26, 2026, [https://www.mckinsey.com/~/media/McKinsey/dotcom/client_service/BTO/PDF/MOBT_27_Delivering_large-scale_IT_projects_on_time_budget_and_value.ashx](https://www.mckinsey.com/~/media/McKinsey/dotcom/client_service/BTO/PDF/MOBT_27_Delivering_large-scale_IT_projects_on_time_budget_and_value.ashx)
10. ERP Implementation: The Ultimate 7 Factors to Avoid - initOS, accessed February 26, 2026, [https://www.initos.com/en/blog/what-to-avoid-in-erp-implementation-project/](https://www.initos.com/en/blog/what-to-avoid-in-erp-implementation-project/)
11. Cost of Poor Software Quality in the U.S.: A 2022 Report - CISQ, accessed February 26, 2026, [https://www.it-cisq.org/the-cost-of-poor-quality-software-in-the-us-a-2022-report/](https://www.it-cisq.org/the-cost-of-poor-quality-software-in-the-us-a-2022-report/)
12. [Analyst Report] 2022 The Cost of Poor Quality Software | Black Duck, accessed February 26, 2026, [https://www.blackduck.com/resources/analyst-reports/cost-poor-quality-software.html](https://www.blackduck.com/resources/analyst-reports/cost-poor-quality-software.html)
13. Untitled - CISQ, accessed February 26, 2026, [https://www.it-cisq.org/wp-content/uploads/sites/6/2022/11/CPSQ-Report-Nov-22-2.pdf](https://www.it-cisq.org/wp-content/uploads/sites/6/2022/11/CPSQ-Report-Nov-22-2.pdf)
14. The $2.4 Trillion Crisis: Why Hardware/Software Integration Is Your Most Critical Technical Decision - Edge AI and Vision Alliance, accessed February 26, 2026, [https://www.edge-ai-vision.com/2025/08/the-2-4-trillion-crisis-why-hardware-software-integration-is-your-most-critical-technical-decision/](https://www.edge-ai-vision.com/2025/08/the-2-4-trillion-crisis-why-hardware-software-integration-is-your-most-critical-technical-decision/)
15. A meta-analysis of loss aversion in risky contexts - IDEAS/RePEc, accessed February 26, 2026, [https://ideas.repec.org/a/eee/joepsy/v103y2024ics0167487024000485.html](https://ideas.repec.org/a/eee/joepsy/v103y2024ics0167487024000485.html)
16. Prospect theory, constant relative risk aversion, and the investment ..., accessed February 26, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC8016345/](https://pmc.ncbi.nlm.nih.gov/articles/PMC8016345/)
17. One for the Gain, Three for the Loss - SSRN, accessed February 26, 2026, [https://papers.ssrn.com/sol3/Delivery.cfm/SSRN_ID871432_code372909.pdf?abstractid=676951](https://papers.ssrn.com/sol3/Delivery.cfm/SSRN_ID871432_code372909.pdf?abstractid=676951)
18. The Real Power of Emotion in B2B Marketing | OpenView Labs, accessed February 26, 2026, [https://openviewpartners.com/blog/emotion-in-b2b-marketing/](https://openviewpartners.com/blog/emotion-in-b2b-marketing/)
19. FROM PROMOTION TO EMOTION: - Google, accessed February 26, 2026, [https://www.thinkwithgoogle.com/_qs/documents/3988/promotion-emotion-b2b_articles_q5pm53H.pdf](https://www.thinkwithgoogle.com/_qs/documents/3988/promotion-emotion-b2b_articles_q5pm53H.pdf)
20. Promotion Emotion Whitepaper Full | PDF | Brand | Marketing - Scribd, accessed February 26, 2026, [https://www.scribd.com/document/756368697/promotion-emotion-whitepaper-full](https://www.scribd.com/document/756368697/promotion-emotion-whitepaper-full)
21. Building Brand Love in B2B Industries. | Atomicdust, accessed February 26, 2026, [http://www.atomicdust.com/wp-content/uploads/2017/10/Building-Brand-Love-in-B2B-Industries.pdf](http://www.atomicdust.com/wp-content/uploads/2017/10/Building-Brand-Love-in-B2B-Industries.pdf)
22. How to JOLT buyers out of indecision | Gong.io, accessed February 26, 2026, [https://podcast.gong.io/public/76/Reveal%3A-The-Revenue-Intelligence-Podcast-05b3e1e1/af9f3a56](https://podcast.gong.io/public/76/Reveal%3A-The-Revenue-Intelligence-Podcast-05b3e1e1/af9f3a56)
23. Your AI Initiatives May Be Dead on Arrival | Digi International, accessed February 26, 2026, [https://www.digi.com/blog/post/your-ai-initiatives-may-be-dead-on-arrival](https://www.digi.com/blog/post/your-ai-initiatives-may-be-dead-on-arrival)
24. Your AI initiatives may be dead on arrival - Strategy of Things, accessed February 26, 2026, [https://strategyofthings.io/your-ai-initiatives-may-be-dead-on-arrival](https://strategyofthings.io/your-ai-initiatives-may-be-dead-on-arrival)
25. Why 80% of AI-projects fail: they miss the bigger picture | by Helge Tennø | Everything New Is Dangerous | Medium, accessed February 26, 2026, [https://medium.com/everything-new-is-dangerous/why-80-of-ai-projects-fail-they-miss-the-bigger-picture-dda05c81e33c](https://medium.com/everything-new-is-dangerous/why-80-of-ai-projects-fail-they-miss-the-bigger-picture-dda05c81e33c)
26. The Production AI Reality Check: Why 80% of AI Projects Fail to ..., accessed February 26, 2026, [https://medium.com/@archie.kandala/the-production-ai-reality-check-why-80-of-ai-projects-fail-to-reach-production-849daa80b0f3](https://medium.com/@archie.kandala/the-production-ai-reality-check-why-80-of-ai-projects-fail-to-reach-production-849daa80b0f3)
27. Generative AI ROI: Why 80% of Companies See No Results - FullStack Labs, accessed February 26, 2026, [https://www.fullstack.com/labs/resources/blog/generative-ai-roi-why-80-of-companies-see-no-results](https://www.fullstack.com/labs/resources/blog/generative-ai-roi-why-80-of-companies-see-no-results)
28. Preventing Buyer's Remorse: Route Planning Technology Survey Report - RouteSmart, accessed February 26, 2026, [https://www.routesmart.com/preventing-buyers-remorse-survey-report/](https://www.routesmart.com/preventing-buyers-remorse-survey-report/)
29. Preventing Buyer's Remorse with Supply Chain Technology - Talking Logistics, accessed February 26, 2026, [https://talkinglogistics.com/2023/04/05/preventing-buyers-remorse-with-supply-chain-technology/](https://talkinglogistics.com/2023/04/05/preventing-buyers-remorse-with-supply-chain-technology/)
30. Gartner Survey Reveals Personalization Can Triple the Likelihood of Customer Regret at Key Journey Points, accessed February 26, 2026, [https://www.gartner.com/en/newsroom/press-releases/2025-06-03-gartner-survey-reveals-personalization-can-triple-the-likelihood-of-customer-regret-at-key-journey-points](https://www.gartner.com/en/newsroom/press-releases/2025-06-03-gartner-survey-reveals-personalization-can-triple-the-likelihood-of-customer-regret-at-key-journey-points)
