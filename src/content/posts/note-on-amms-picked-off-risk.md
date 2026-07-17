---
title: "Note on AMMs \"picked-off\" risk"
date: "2022-03-17"
slug: "note-on-amms-picked-off-risk"
lang: "es"
categories: ["Defi", "Economics"]
tags: ["AMM", "defi"]
excerpt: ""
draft: false
---

AMMs picked-off risk


# Note on AMMs "picked-off" risk

It has been popularized the term "Impermanent loss" (IL) to refer to costs incurred by liquidity providers (LPs) of an AMM pool in the case relative market prices change, and those changes are profited out by arbitrageurs. This [Twitter thread](https://twitter.com/AnthonyLeeZhang/status/1503465602979008512?s=20&t=rDpX1yaCWUXkb5v0tnimrg) by [@AnthonyLeeZhang](https://twitter.com/AnthonyLeeZhang) and [@guil\_lambert](https://twitter.com/guil_lambert) discuss that a more appropriate term for this loss is "picked-off" risk. In my understanding (thanks to discussions with Javier Garcia Sanchez), IL is not the best term and below are my notes of why. IL is also referred as an "opportunity cost", meaning that LPs would have been better staying out of the AMM in such a case. I tend to think that the term "opportunity cost" idea is neither adequate.

It is my understanding that "picked-off risk" or "picked-off loss" are right terms. As mentioned, this situation takes place when: i) the relative prices of the assets of interest (i.e., those in the pool) change *outside* the AMM (in the "market" or centralized exchange of reference), and ii) an arbitrageur takes advantage of the price differential (between the one provided by the AMM and market) to obtain a benefit. My understanding is that this is indeed a "picked-off" risk, since once prices outside the AMM have changed, the arbitrage reduces the value of the pool in the magnitude of the value gained by the arbitrageur. This is an example of how I see it:

Consider a pool of *DAI* and *ETH*.  as the *DAI* pool volume,  the *ETH* volume, and  the (*DAI* per *ETH*) "market" (or CEX) exchange rate. Lets assume fees are zero for the sake of the example. Assume initially the pool is in equilibrium (). Then, the exchange in the market increases to . The value of the pool (in ETH) is now

Assume the pairs ,  are trade terms that meet the AMM condition (i.e. ). Therefore, the market value of the pool after a complete arbitrage operation takes place is

Due to the convexity of AMM rule, terms of trade  will be such that , so the arbitrageur can sell  an obtain a profit (See graph at the bottom for an illustration). The value gained by the arbitrage (), expressed in ETH is:

Note that . In other words, as result of the arbitrage, the pool incurs in a value loss that matches the arbitrage gain obtained by the arbitrageur.

Therefore, as pointed out in the [thread](https://twitter.com/AnthonyLeeZhang/status/1503465602979008512?s=20&t=rDpX1yaCWUXkb5v0tnimrg), if someone front-runs the LPs in doing the arbitrage, they have effectively "picked off" part of the pool value. Notice that not being subject of front-running is not trivial, due to competition for transaction inclusion in blocks taking place at the [MEV level](https://ethereum.org/es/developers/docs/mev/).

I would notice that the term "picked-off" risk is used, for instance, in [Lehar and Parlour (2021)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3905316), who conveniently, I think, do not mention "IL".

Finally, as with "IL", I don't think the term "opportunity cost" is adequate either. Recall that the idea of opportunity cost is introduced in terms that LPs would have been better by staying out of the AMM (instead of investing and being picked off). I am inclined to think in the concept of "opportunity cost" as a second-best alternative that is known ex-ante (at least in expected terms). This seems not to be the case in this situation. I tend to see price changes and the "picked-off" possibility as forms of risks in this particular investment. In case it is agreed that all external price changes induce a "picking off" with certainty (e.g. agreeing bots always pick off LPs), then we could think of "IL" just as a specific form of price risk. Finally, in that line of reasoning, notice that the "impermanent" part in "IL", used to highlight that the fact that there is no loss if relative prices return to their initial level, is also somewhat misleading. Investment in assets in general might incur in losses if prices change and we do not refer to such losses as impermanent.

![AMM initial and final reference prices and price of the arbitrage trade](https://drive.google.com/uc?id=1Nkee_F2D4i66cqnSGcIkZLOgAG1J8VKM)
