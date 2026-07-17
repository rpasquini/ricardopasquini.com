---
title: "Note on the Impact of Liquidation on Health Factor in Overcollateralized Loans"
date: "2025-05-08"
slug: "the-impact-of-liquidation-on-health-factor-in-overcollateralized-loans"
lang: "es"
categories: ["Uncategorized"]
tags: []
excerpt: ""
draft: false
---

The Impact of Liquidation on Health Factor in Overcollateralized Loans



# The Impact of Liquidation on Health Factor in Overcollateralized Loans

Why does the Health Factor of a position increase after a liquidation? If the liquidation mechanism provides liquidators with a collateral bonus, does this always improve the collateral-to-loan ratio?

In this note, we demonstrate that a liquidation generally improves the health factor of a position. We also examine the rare cases where the health factor might decrease, which can occur due to the bonus given to the liquidator.

Consider a loan smart contract, such as AAVE, that permits liquidations when the loan-to-collateral ratio exceeds a specific threshold.
This condition is reflected in the Health Factor of the position, \(H\), defined as:

\[H\equiv\frac{C\delta}{L}\]

where \(C\) represents the collateral, \(L\) the loan amount, and \(\delta\) the liquidation threshold.

For simplicity, we assume that both currencies have the same price. The contract allows liquidations when:

\[H<1\]

During a liquidation, a liquidator repays a percentage of the debt \(L\) in exchange for collateral. We denote this percentage as \(k\) (where \(0

Let's demonstrate how a liquidation affects the health factor of a position:

* After liquidation, since the liquidator repays \(kL\), the remaining loan is reduced to \((1-k)L\).
* The lender's collateral is reduced by the value covered plus the bonus: \(C-(1-k)L-(1-k)Lb=C-(1-k)L(1+b)\)

The health factor after liquidation becomes:

\[\begin{align}
H'&\equiv\frac{[C-(1-k)(1+b)L]\delta}{(1-k)L}\\
&=\frac{[1-(1-k)(1+b)\frac{L}{C}]}{(1-k)}\frac{C\delta}{L}\\
&=\bigg(\frac{1}{(1-k)}-(1+b)\frac{L}{C}\bigg)\frac{C\delta}{L}\\
&=\bigg(\frac{1}{(1-k)}-(1+b)\frac{L}{C}\bigg)H
\end{align}\]

Therefore, the health factor improves if:

\[\bigg(\frac{1}{(1-k)}-(1+b)\frac{L}{C}\bigg)>1\]

As an example, consider a position with a loan-to-collateral ratio of \(0.9\). Assuming a liquidation threshold of \(0.8\), this implies that the health factor is below 1 and therefore eligible for liquidation.
Let's also consider a bonus rate of \(0.05\).

![Plot showing the relationship between k and the health factor components](/media/2025/05/k.png)

Plot showing the relationship between \(k\) and the health factor components. The blue curve represents \(\frac{1}{1-k}\) and the red line represents \((1+b)\frac{L}{C}\) where \(b=0.05\) and \(\frac{L}{C}=0.9\).

As shown in the plot, in this case the equation is satisfied for any close factor (\(k<1\)).
For the equation to be violated, the close factor would need to be very small and the bonus rate very high.

## Conclusions

Intuitively, a liquidation improves the health factor because, in an overcollateralized loan, the lender's collateral can be viewed as consisting of the loan amount plus an additional margin.
When liquidation occurs, both the loan and its corresponding share of the collateral are reduced proportionally, while the additional margin remains unchanged.
Consequently, the collateral-to-loan ratio improves in relative terms.
The liquidation bonus, however, reduces the collateral more than the loan, creating an opposing effect. In blockchain settings, where liquidation bonuses are typically small, this effect is negligible compared to the loan reduction.
