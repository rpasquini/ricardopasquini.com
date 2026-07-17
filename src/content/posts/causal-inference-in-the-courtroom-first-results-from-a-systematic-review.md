---
title: "Causal Inference in the Courtroom: First Results from a Systematic Review"
date: "2026-07-11"
slug: "causal-inference-in-the-courtroom-first-results-from-a-systematic-review"
lang: "es"
categories: ["Uncategorized"]
tags: []
excerpt: ""
draft: false
---

The "credibility revolution" in applied economics produced a set of methods — difference-in-differences, synthetic control, regression discontinuity, instrumental variables — that are now standard in program evaluation and academic research. The same methods have migrated into litigation: expert economists rely on them to establish causation and quantify damages in antitrust, securities, and tort cases.



Yet we know surprisingly little about how this plays out in court at scale. Which methods appear most often? Which assumptions do opposing experts challenge? Do courts engage substantively with the methodology, and on what grounds? While the academic literature has discussed the role of economic experts, and offers useful case studies, there seems to be no systematic picture on the use of causal inference methods. This post shares some early results on this research line, including the uses of the different methods and noteworthy examples, using a systematic review of US federal court filings.




---




#### Data and Methodology



We first decided to focus on US federal courts, in order to take advantage of data available through **CourtListener**, the public repository maintained by the non-profit [Free Law Project](https://free.law). CourtListener covers federal opinions as well as PACER/RECAP filings — expert reports, Daubert motions, briefs, and appendices — the documents where economists actually present and defend their methodology, not just the opinions where judges occasionally summarize it. Documents were identified through searches on method-related terms, then screened to confirm genuine use of a causal inference method. Here are preliminary numbers of the current coverage.



**Current coverage (as of July 2026):**




| Stage | Count |
| --- | --- |
| Dockets searched | 857 |
| Documents downloaded and screened | 1,158 |
| Confirmed: uses causal inference | 522 |
| Unique cases | 410 |





---




#### Which Methods Appear, and How Often



The chart below shows method mentions in confirmed documents, by filing year. We restrict the analysis to the period from 2020 to 2026 since this is where the data source provides exhaustive coverage.


![](/media/2026/07/2026-07-08_methods-by-year-2020-2026.png)



*Note: 2026 covers January–June only.*



A few observations:



**Event studies are the most common method.** Across the full dataset, event studies are the single most common method, appearing in 150 documents — ahead of DiD (108) and IV (106) individually. This is not surprising once you account for composition: a large share of US federal litigation involving causal methodology is securities class action work, where event studies are the standard tool for establishing price impact and loss causation. The "credibility revolution" literature — which emphasizes DiD and synthetic control — describes a particular slice of applied economics; it does not represent the full range of methods that forensic economists actually rely on in court.



**Instrumental variables are as common as DiD.** IV appears in 106 documents versus 108 for DiD. This probably reflects IV's long history in antitrust economics, where it is the conventional tool for handling endogeneity in price-setting and merger analysis. Its near-equal presence alongside DiD suggests that the two methods address different litigation contexts rather than competing for the same cases.



**The synthetic control spike in 2023 is the most surprising result so far.** Synthetic control appears in 89 documents overall, but the distribution across years is uneven: 34 mentions in 2023 alone, sharply higher than any other year and followed by a noticeable decline. One plausible account is a publication and diffusion lag. Abadie's 2021 *Journal of Economic Literature* survey of the synthetic control method received substantial attention in the applied economics community; adoption in expert reports may have followed with a delay, concentrating in 2022–2023 filings. Whether this pattern reflects durable uptake or a period of heightened interest that has since moderated is something the data will clarify as coverage extends.



**Regression discontinuity (RD)** appears in 77 documents — more than propensity score matching (53). RD's presence in litigation is less discussed in the existing literature; the cases driving this number span gun regulations, electoral law challenges, and healthcare policy disputes. This is a domain worth examining more closely. It is worth noting that some of these cases might include not only the use of the method by the experts, but also citations to social science research that uses RD.




---




#### Cases in the Database



The database covers a variety of cases, including several high-profile ones. Here are a few examples to illustrate the range of litigation covered and the role these methods play in each:



* **United States v. Google LLC (E.D. Virginia, 2023)** — the DOJ's antitrust case alleging Google monopolized the open web display advertising market through its AdX exchange. Plaintiffs' expert used a comparables approach — benchmarking AdX's take rate against those of competing exchanges — alongside an event study comparing AdX and rival exchanges before and after Google's implementation of its Unified Pricing Rules, with exchange fixed effects controlling for quality differences. Both approaches were designed to estimate the but-for take rate in the absence of Google's exclusionary conduct.
* **The State of Texas v. Google LLC (E.D. Texas, 2020)** — a state AG antitrust action targeting Google's ad auction manipulation, specifically the undisclosed Reserve Price Optimization (RPO) mechanism. A regression discontinuity design was applied around the date of Google's May 2016 RPO disclosure to estimate its causal effect on advertising clearing prices in AdX.
* **United States v. American Airlines Group Inc. (D. Massachusetts, 2021)** — the DOJ challenge to the Northeast Alliance between American Airlines and JetBlue. The government's experts relied on a merger simulation model to predict post-transaction fare increases, with instrumental variables used to address endogeneity in the demand-side estimation. Both were challenged in cross-examination at trial by the defendants' experts.
* **In re Apple iPhone Antitrust Litigation (N.D. California, No. 11-cv-06714)** — a consumer class action alleging Apple monopolized app distribution through the App Store's 30% commission. Plaintiffs' experts, modeled the but-for commission rate using an instrumental-variables approach; Apple's Daubert motion to exclude both experts argued the instruments were weak. In a mirror-image dispute, Apple's own expert, ran difference-in-differences "natural experiment" analyses — using inverse propensity score weighting to address selection into the treatment group — to rebut the damages case, and it was the plaintiffs who challenged his DiD, arguing he never ran or disclosed a parallel-trends test to validate his control groups. The dueling motions, each side defending its own method while attacking the other's, make this case particularly interesting in terms of their methodologically discussion.



The breadth of case types illustrates how widely these methods now appear outside their academic origins.




---




#### Where the Cases Are Filed



The geographic distribution is heavily concentrated.



*[FIGURE: cases-by-court-top15.png]*



![](/media/2026/07/2026-07-08_cases-by-court-top15-1024x677.png)



The Southern District of New York and the Northern District of California account for roughly a quarter of confirmed cases between them — which seems to reflect their roles as dominant venues for securities class actions and tech antitrust matters respectively. The D.C. Circuit and Northern District of Illinois seems to be notable in terms of regulatory and antitrust work.




---




#### What Comes Next



While this analysis covers method mentions in filings — expert reports, briefs, and appendices — it does not yet systematically capture how courts engage with the methodology: whether experts were admitted, which assumptions were challenged at Daubert, and what grounds courts used when ruling on the evidence. That is the next layer.



If you work in litigation economics and have questions or ideas on this research line, please leave your comments.




---




*Ricardo Pasquini is an Associate Professor at the Facultad de Ciencias Empresariales, Universidad Austral, and a professor at the School of Government, Universidad Torcuato Di Tella. His research covers causal inference, digital markets, and quantitative methods in economics.*
