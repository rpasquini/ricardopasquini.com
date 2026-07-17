---
title: "Bienes públicos, Gitcoin, y  financiamiento cuadrático"
date: "2020-10-01"
slug: "bienes-publicos-gitcoin-y-financiamiento-cuadratico"
lang: "es"
categories: ["Economics", "Uncategorized", "Urban Economics"]
tags: ["bienes publicos", "criptomonedas", "cryptocurrencies", "Ethereum", "financiamiento cuadrático", "Gitcoin", "public goods", "quadratic funding"]
excerpt: ""
draft: false
---

[english](#english)






Gitcoin - blog post


# Bienes públicos, Gitcoin, y financiamiento cuadrático[1](#dfref-footnote-1)

Hay algo que tienen en común las inversiones que se realizan en las ciudades, en la actividad de ciertas startups, y el software *open source* gratuito. La inversión en la generación de un espacio verde, un museo, un espacio de arte, reporta un beneficio no solo para los beneficiarios inmediatos, sino que también vuelven más atractivo el barrio, la ciudad en cuestión, etc. Típicamente, este fenómeno puede verificarse en el incremento del valor de las propiedades cercanas. En el caso de las startups, si la inversión en una de ellas, por ejemplo, hace que ésta pueda innovar exitosamente en un *modelo de negocio*, este será luego copiado por muchas empresas, cuyos valores también se incrementarán en consecuencia. El último ejemplo es la inversión en código abierto (gratuito). Se estima que el 99% de las aplicaciones desarrolladas por las compañías actualmente contienen software open source, alcanzando hasta un 70% del código de esas aplicaciones (Synopsis, 2020). Esto implica un ahorro muy importante por parte de las compañías gracias a la utilización de este tipo de código, que fue posibilitado gracias a la inversión de compañías o grupos de desarrolladores pioneros[2](#dfref-footnote-2).

En breve, lo común a estas inversiones y muchos otros ejemplos de este tipo, es que redundan en la generación de valor que va más allá de sus beneficiarios inmediatos. Tradicionalmente la disciplina de la economía ha reconocido que estas inversiones, si son llevadas adelante por un privado, al no tener en cuenta a sus beneficiarios indirectos, típicamente serán *menores* que su nivel (socialmente) eficiente, o no se llevarán a cabo en absoluto. En los casos de las inversiones realizadas, también existe el problema de que el financiamiento no permita que estos bienes se mantengan en el tiempo. Aquí también el software open source (gratuito) provee un buen ejemplo. Muchos proyectos, sobre todo pequeños, al ser abandonados por parte de sus desarrolladores, y depender sólo de un puñado de ellos, sufren de problemas de mantenimiento, como por ejemplo, problemas críticos de seguridadOwocki . De hecho, las vulnerabilidades críticas alcanzan hasta a un 50% de las aplicaciones que se desarrollan actualmente (Synopsis, 2020). En las inversiones que se desarrollan en las ciudades encontramos problemas de mantenimiento similares.

De ahí que hay un interés de la disciplina económica en aquellos mecanismos de financiación que aseguren la provisión de bienes públicos de este tipo, acerquen estas inversiones a sus niveles eficientes, y aseguren su mantenimiento. A su vez podríamos pensar que la cuestión del financiamiento conlleva dos problemas específicos. Por una parte está el problema de cómo conseguir fondos para permitir el financiamiento de este tipo de inversiones, pero también está el problema de qué proyectos financiar. Típicamente en una ciudad encontraremos una variedad de proyectos y posibles amenidades para financiar, existirán un número de startups que competirán por inversiones, etc.

En relación al primer problema, en el caso de las ciudades, la literatura económica urbana ha propuesto desarrollar instrumentos específicos que permitan conseguir los fondos para desarrollar las inversiones en primer lugar [3](#dfref-footnote-3). El racional de estos instrumentos, también llamados de captación de plusvalías, es poder captar los beneficios indirectos que generan las inversiones, por ejemplo, a través de un impuesto que capture el incremento en el valor de la propiedad[4](#dfref-footnote-4). En otros contextos, como el de las startups o el software, donde es más complejo definir quienes son los beneficiarios, las soluciones de este tipo serían mucho más difíciles de implementar.

## Gitcoin

Pero todavía queda la pregunta de qué proyectos financiar y cómo lograr que se realicen las inversiones eficientes en primer lugar. Un proyecto que hoy está experimentando con un esquema que busca generar eficiencia en este sentido es [Gitcoin](https://gitcoin.co/), una comunidad generada alrededor del desarrollo de software open source basado en blockchain. Una de las principales funcionalidades de esta plataforma, pero quizás menos relevante en esta nota, es que Gitcoin facilita un mercado de resolución de problemas de *bugs* o para la implementación de pequeñas mejoras en el código, denominadas *bounties* en la jerga de los desarrolladores. Los proyectos ofrecen estos *bounties* a cambio de pagos que se realizan en criptomonedas. Es decir, Gitcoin funciona como una plataforma que conecta las dos partes de un mercado, o un *two sided market* en la jerga de los economistas.

Pero el proyecto que me interesa aquí el de [Gitcoin Grants](https://gitcoin.co/grants/). El *grant*, también llamado aporte no reembolsable, es una figura estándar de financiamiento, mediante el cual un proyecto puede recibir dinero para un proyecto específico. El dinero, en el caso de Gitcoin, proviene de un fondo que es aportado por participantes de la comunidad e instituciones patrocinantes. Los grants suelen ser una respuesta de las instituciones para apoyar inversiones que de otra manera se realizarían en niveles sub-eficientes. Pero lo novedoso en este caso no es el grant en sí. La innovación de gitcoin grants está relacionada a la forma en la que se asignan estos fondos, entre los proyectos de las comunidad.

En primer lugar, para recibir dinero del fondo, el proyecto en cuestión debe recibir aportes privados individuales, que funcionan, a modo de votación, para que los miembros de la comunidad *señalicen* su interés en un proyecto. Lo que hará el fondo es *matchear* el aporte individual, es decir, apoyar el aporte individual aportando dinero del fondo para el proyecto en cuestión.

Que un fondo *matchee* un aporte individual tampoco es algo nuevo. Este también es un mecanismo bien difundido en los ecosistemas emprendedores, por ejemplo, cuando los gobiernos *matchean* fondos invertidos por inversores privados a una startup[5](#dfref-footnote-5). Lo novedoso es la forma en la que el grant de Gitcoin lo hace. El *matching* no es 1 x 1, es decir, el fondo no iguala su inversión en criptomonedas a las invertidas por el privado, sino que la cantidad de *dinero* que un proyecto recibe depende de un mecanismo denominado *financiamiento cuadrático*.

Voy a explicar el detalle del mecanismo en un segundo, pero quisiera mencionar primero que la característica más saliente es que el mecanismo del financiamiento al cuadrado responde a una regla que evalúa no solo el monto recibido por un proyecto sino la cantidad de aportantes que un proyecto tiene[6](#dfref-footnote-6). De esta manera, el mecanismo propone una regla que responde no solo a la capacidad económica de determinados aportantes, sino también a cada persona por su valor individual, de una forma más, si se permite el abuso del término, *democrática*.

¿Por qué no una votación tradicional por mayoría (como el que emplean los sistemas democráticos) para determinar el proyecto que será financiado (y el monto? )? Una regla puramente de 1 voto por persona hace que la decisión de financiación del bien público dependa de la valoración del *votante mediano*, y esta es una característica que podría ser no deseable si hay grupos minoritarios con una gran valoración por el bien.

Por otra parte, ¿Cuál sería la ventaja de este método, sobre la alternativa de realizar aportes voluntarios como en una campaña de recaudación de fondos?. Porque, en primer lugar, si el aporte es puramente voluntario y depende del interés privado, sabemos, como ya dijimos, que la inversión será sub-eficiente. Este sistema además reflejaría la preferencia de los donantes con mayor valoración (y capacidad para aportar). Eso llevaría a que el fondo acompañe al interés de los que más capacidad de inversión tienen.

Por eso, en cierto sentido se podría pensar a este mecanismo, como una solución intermedia entre las dos soluciones. Pero estas características son sólo una propiedad del método. Lo más interesante del financiamiento cuadrático quizás sea que, al menos en teoría, logra generar una cantidad *socialmente eficiente* de financiamiento, aún cuando cada persona tiene la libertad de decidir a qué proyecto apoyar y en cuánto (Buterin, Hitzig, and Weyl. 2018). Es decir, bajo algunas condiciones, alcanzaría ese nivel eficiente al que nos referimos más arriba. En otras palabras, el sistema de manera descentralizada alcanza un nivel de inversión equivalente al que que se conseguiría de manera centralizada si se consideran los beneficios que generará la inversión en todos los miembros de la comunidad.

# ¿Cómo es que puede este mecanismo replicar, desde la iniciativa individual, lo que se haría con una consideración por el conjunto de la comunidad?

Para entender mejor este punto vale la pena entender más en detalle el financiamiento cuadrático.

El mecanismo toma ese nombre porque para que el fondo *matchee* $x invertidos por un inversor, al inversor le costará $x *al cuadrado*. O dicho al revés, cuando el fondo haga la cuenta de cuánto va a poner para matchear el aporte de una persona determinada, solo tendrá en cuenta el monto aportado por esa persona *tomado en raiz*. Tomemos un ejemplo: El *Inversor 1* invierte 1 *DAI* al *proyecto A* (el [DAI](https://golden.com/wiki/Dai_(cryptocurrency)) es la criptomoneda que iguala en valor al dólar, por eso es útil para el ejemplo). El Inversor 2 invierte *4 DAI* al proyecto A. Hasta aquí, el proyecto A recibió 5 DAI. El fondo, por su parte va a asegurarse de que el proyecto reciba en total 9 DAI, de manera de que pondrá 4 DAI más para cubrir la diferencia. ¿Cómo surge el objetivo de los 9 DAI? Para su cuenta, el fondo tomará la raíz cuadrada de la inversión de cada inversor (1 DAI y =2 DAI respectivamente). Sumará estas cantidades (3) y la elevará al cuadrado, resultando en 9 DAI en total.

Ahora podemos ver por qué se alcanzará una inversión eficiente. Este resultado surge gracias a la intervención del fondo, ya que el fondo promete a cambio una inversión más grande mientras más grande sea el interés del resto de los participantes del proyecto. Es decir, un peso invertido por un inversor individual tiene un mayor retorno si el proyecto es más apoyado por el resto de las personas[7](#dfref-footnote-7).

Lo veamos en un ejemplo. Si nuestro Inversor 1 estaba indeciso entre invertir 1 DAI al proyecto, sabiendo que 2 va a invertir, entonces la cuenta para él debería ser, como vimos, que el retorno de invertir 1 DAI va a redundar en 9 de inversión total. Ahora comparemos el caso con la situación en la que los 4 DAI que son invertidos por el Inversor 2 en realidad están siendo aportados por 4 inversores distintos que aportan 1 DAI cada uno. La cuenta del fondo se traduciría en asegurar un objetivo de 25 DAI total, y debería cubrir la diferencia de 20. El retorno del DAI invertido por el inversor 1 redunda en 25 DAI. Podemos ver entonces que a mayor cantidad de donantes, mayores incentivos a la inversión individual.

# Desafíos y preguntas abiertas

Actualmente está ocurriendo la 8va ronda de financiamiento de Gitcoin Grants. Las distintas rondas fueron experimentando distintos elementos en su diseño, como por ejemplo, la incorporación de facilidades para volver a financiar proyectos de rondas anteriores (con el objetivo de dar sostenibilidad al financiamiento), y mejoras en el sitio que permiten invertir en varios proyectos simultáneamente.

Hasta aquí, los montos que se han financiado no son tan grandes como para garantizar la sostenibilidad de un desarrollo (en pocos casos algunos desarrolladores lograron un monto de financiamiento similar al que tendrían en un trabajo full time).

También han aparecido problemas, como los problemas de *falsificación de la identidad* (a.k.a.[sybil attack][https://es.wikipedia.org/wiki/Ataque\_Sybil]) y *colusión*. Podríamos decir que ambos problemas son estimulados por el hecho de que un mismo monto de dinero contribuido por múltiples personas sume más que si fueran contribuidas por una una sola[8](#dfref-footnote-8).

Otros temas importantes desde mi punto de vista tienen que ver, por una parte, con el hecho de que la eficiencia está al findal del día atada a la percepción de suficientes fondos por parte del matching fund (algo que propongo examinar en este [documento aparte](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3702318) ). Este es un tema que puede ser particularmente importante para el diseño del mecanismo, considerando especialmente que los fondos (en exceso) que son requeridos al matching fund ascienden rápidamente (de acuerdo al cuadrádo del número de contribuyentes). Cabe la pregunta entonces de en qué medida un mecanismo de este tipo puede resistir las necesidades de financiamiento filantrópico.

Más allá de estos problemas, las propiedades de este mecanismo a las que me referí más arriba, de balancear el sistema a uno que hace mayor representación de las mayorías hacen que el mismo sea especialmente interesante. De hecho el primo cercano de este mecanismo, la votación cuadrática, ha alcanzado mucha difusión y ya ha sido probado en varios contextos[9](#dfref-footnote-9).

Volviendo a las ciudades, estas propiedades podrían ser especialmente atractivas. Según explican Buterin, Hitzig, y Weyl, es precisamente su capacidad de potenciar las demandas de los pequeños grupos, como podrían ser, las de los vecinos que tienen problemas muy locales y que no se ven bien representados por el votante mediano en los comités o legislaturas de las ciudades.

Explorar otras extensiones como permitir votación o el financiamiento negativo, también podría servir para pensar en proyectos que pueden implicar externalidades negativas. Una aplicación para el contexto de las ciudades pueden ser los proyectos que estimulan la gentrificación y el desplazamiento urbano, de manera de reestablecer un equilibrio entre poder económico y capacidad local.

# Referencias

Buterin, Vitalik, Zoë Hitzig, and Eric Glen Weyl. 2018. “Liberal Radicalism: A Flexible Design For Philanthropic Matching Funds.” *SSRN Electronic Journal*. <https://doi.org/10.2139/ssrn.3243656>.

Lalley, S. P., & Weyl, E. G. (2018, May). Quadratic voting: How mechanism design can radicalize democracy. In *AEA Papers and Proceedings* (Vol. 108, pp. 33-37).

Pasquini, Ricardo, A Note on Quadratic Funding under Constrained Matching Funds (September 30, 2020). Available at SSRN: <https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3702318>

Smolka, M. O. (2012). A new look at value capture in Latin America. *Land Lines*, *24*(3), 10-15.

Stiglitz, J. E. (1977). The theory of local public goods. In *The economics of public services* (pp. 274-333). Palgrave Macmillan, London.

Synopsis (2020), Open source security and risk analysis report.

---

1 Expongo aquí algunas ideas sobre financiamiento cuadrático, cuya principal referencia es Buterin, Hitzig, and Weyl (2018). La página de [Radical X Change Foundation](radicalxchange.org) provee mucha información relacionada al sistema de votación cuadrático y material relacionado.[↩](#ref-footnote-1 "back to document")

2 Ver por ejemplo <https://es.slideshare.net/SFScon/04-carlo-daffarasfscon>[↩](#ref-footnote-2 "back to document")

3 Para una discusión de instrumentos de captación de plusvalías en el contexto de América Latina ver Smolka (2012) disponible [aquí][https://www.lincolninst.edu/sites/default/files/pubfiles/2099\_1420\_New\_Look\_at\_Value\_Capture\_Latin\_America\_0712LL.pdf]. [↩](#ref-footnote-3 "back to document")

4 Una referencia teórica clásica sobre la optimalidad de estos instrumentos es Stiglitz (1977). La literatura también se refiere a la optimalidad de estos instrumentos como el Teorema de Henry George<https://es.wikipedia.org/wiki/Henry_George>. [↩](#ref-footnote-4 "back to document")

5 A modo de ejemplo, en Argentina hubo mecanismos de matching funds para inversiones en startups a nivel nacional y a nivel de la Ciudad de Buenos Aires, mediante las cuales el gobierno igualaba el monto invertido por parte aceleradoras y otros fondos de capital de riesgo.[↩](#ref-footnote-5 "back to document")

6 Más precisamente la regla busca que la cantidad total de financiamiento recibido por el proyecto se iguale al cuadrado de la suma de las contribuciones tomadas en raíz.  De esa manera las contribuciones grandes se penalizan y se potencian las contribuciones pequeñas.[↩](#ref-footnote-6 "back to document")

7 Más precisamente el mi contribución de un DAI extra tiene mayor valor para mi de manera inversamente proporcional al tamaño relativo de mi contribución con respecto a la de los demás. [↩](#ref-footnote-7 "back to document")

8 Vitalik Buterin, el creador de Ethereum, los explica muy bien en esta [nota][https://vitalik.ca/general/2019/12/07/quadratic.html].[↩](#ref-footnote-8 "back to document")

9 Ver Lalley, S. P., & Weyl, E. G. (2018, May), y más info en la página de la Fundación [Radical X Change](radicalxchange.org).[↩](#ref-footnote-9 "back to document")







Gitcoin - blog post - english


# Public goods, Gitcoin, and quadratic financing [1](#dfref-footnote-1)

There is something that investments made in cities, in the activity of certain startups, and in free *open source* software have in common. Investing in green areas, a museum, an art space, provides a benefit not only for the immediate beneficiaries, but also makes the neighborhood, the city in question, etc., more attractive. Typically, this phenomenon can be verified as nearby properties increase in value. In the case of startups, if the investment in one of them, for example, makes it possible for it to successfully innovate in a new *business model*, this concept will then be copied by many other companies, whose values will also increase accordingly. The last example is investing in open source (free) software. It is estimated that 99% of the applications developed by companies currently contain open source software, reaching up to 70% of the code of those applications (Synopsis, 2020). This implies a very important saving for companies thanks to the use of this type of code, which was made possible thanks to the investment of pioneering companies or groups of developers[2](#dfref-footnote-2).

In short, what is common to these investments and many other examples of this type is that they result in the generation of value that goes beyond its immediate beneficiaries. Traditionally, the discipline of economics has recognized that these investments, if carried out by a private party, by not taking into account their indirect beneficiaries, will typically be *less* than their (socially) efficient level, or they will not be carried out at all. There is also the problem of financing which does not allow these assets to be maintained over time. Here too open source software (free) provides a good example. Many projects, especially small ones, being abandoned by their developers, and depending on only a handful of them, suffer from maintenance problems, such as critical security problems[3](#dfref-footnote-3). In fact, critical vulnerabilities reach up to 50% of applications currently being developed (Synopsis, 2020). In the investments that are developed in the cities we find similar maintenance problems.

Hence, there is an interest of economic discipline in those financing mechanisms that ensure the provision of public goods of this type, bring these investments closer to their efficient levels, and ensure their maintenance. At the same time, we could think that the question of financing involves two specific problems. On the one hand, there is the problem of how to obtain funds to allow the financing of this type of investment, but there is also the problem of which projects to finance. Typically in a city we will find a variety of projects and possible amenities to finance, there will be a number of startups that will compete for investments, etc.

In relation to the first problem, in the case of cities, the urban economic literature has proposed developing specific instruments that allow obtaining funds to develop investments in the first place [4](#dfref-footnote-4). The rationale behind these instruments, also called capital gains capture, is to be able to capture the indirect benefits generated by investments, for example, through a tax that captures the increase in the value of the property [5](#dfref-footnote-5). In other contexts, such as startups or software, where it is more complex to define who the beneficiaries are, solutions of this type would be much more difficult to implement.

## Gitcoin

But the question still remains of which projects to finance and how to get the efficient investments made in the first place. A project that today is experimenting with a scheme that seeks to generate efficiency in this sense is [Gitcoin] (<https://gitcoin.co/>), a community generated around the development of open source software based on blockchain. One of the main functionalities of this platform, but perhaps less relevant in this note, is that Gitcoin facilitates a market for solving *bugs* problems or for the implementation of small improvements in the code, called *bounties* in the jargon of developers. The projects offer these *bounties* in exchange for payments that are made in cryptocurrencies. That is, Gitcoin works as a platform that connects the two parts of a market, or a *two sided market* in the jargon of economists.

But the project that interests me here is [Gitcoin Grants](https://gitcoin.co/grants/). The *grant*, also called a non-refundable contribution, is a standard financing figure, through which a project can receive money for a specific project. The money, in the case of Gitcoin, comes from a fund that is contributed by community participants and sponsoring institutions. Grants are usually a response from institutions to support investments that would otherwise be made at sub-efficient levels. But what is new in this case is not the grant itself. The innovation of Gitcoin grants is related to the way in which these funds are allocated, among community projects.

First, to receive money from the fund, the project in question must receive individual private contributions, which function, by way of voting, for community members *to signal* their interest in a project. What the fund will do is to *match* the individual contribution, that is, support the individual contribution by contributing money from the fund for the project in question.

A fund *matching* an individual contributor is not new either. This is also well-known mechanism in entrepreneurial ecosystems, for example, when governments *match* funds invested by private investors in a startups Argentine. What's new is the way Gitcoin Grant does it. The *matching* is not 1 x 1, that is, the fund does not match its investment in cryptocurrencies to those invested by the private party, but the amount of *money* that a project receives depends on a mechanism called *quadratic financing*.

I will explain the details of the mechanism in a second, but I would like to mention first that the most salient feature is that the financing squared mechanism responds to a rule that evaluates not only the amount received by a project but the number of contributors that a project has[6](#dfref-footnote-6). In this way, the mechanism proposes a rule that responds not only to the economic capacity of certain contributors, but also to each person by their individual value, in a *democratic* way, if the abuse of the term is allowed.

Why not let a traditional majority rule (as it is used by democratic systems) to determine the project to be financed (and its amount)? A purely 1 vote per person rule makes the decision to finance the public good dependent on the valuation of the *median voter*, and this is a characteristic that might be undesirable if there are minority groups with high valuation for a given public good.

On the other hand, what would be the advantage of this method, over the alternative of making voluntary contributions as in a fundraising campaign? Because, first of all, if the contribution is purely voluntary and depends on the private interest, we know, as we have already said, that the investment will be sub-efficient. This system would also reflect the preference of donors with the highest ability to contribute (wealth). That would lead the fund to accompany the interests of those with the greatest investment capacity.

Therefore, in a certain sense, this mechanism could be thought of as an intermediate solution between the two solutions. But these characteristics are only one property of the method. Perhaps the most interesting thing about quadratic financing is that, at least in theory, it manages to generate a *socially efficient* amount of financing, even though each person has the freedom to decide which project to support and by how much (Buterin, Hitzig, and Weyl. 2018). That is to say, under some conditions, it would reach that efficient level referred to above. In other words, the decentralized system achieves a level of investment equivalent to what would be achieved by a centralized mechanism that takes into account all potential beneficiaries.

# How is it that this mechanism can replicate, from the individual initiative, what would be done with a consideration for the whole community?

To better understand this point, it is worth understanding quadratic financing in more detail.

The mechanism takes that name because for the fund to *match* $x invested by an investor, it will cost the investor $x *squared*. Or said the other way around, when the fund computes how much it is going to put to match the contribution of a certain contributor, it will only take into account the amount contributed by that person *taken in root*. Let's take an example: *Investor 1* invests 1 *DAI* to *project A* (the [DAI](https://golden.com/wiki/Dai_ (cryptocurrency)) is the cryptocurrency that equals the dollar in value, that's why it's useful for the example). Investor 2 invests *4 DAI* to project A. So far, project A received 5 DAI. The fund, for its part, will ensure that the project receives a total of 9 DAIs, so that it will put 4 more DAIs to cover the difference. How did the goal of the 9 DAIs is reached? The fund will take the square root of each investor's investment ( 1 DAI and  = 2 DAI respectively). It will add these amounts (3) and square that number, resulting in 9 DAI in total.

Now we can see why a social efficient investment level will be achieved. This result arises thanks to the intervention of the fund, since the fund promises in return a larger investment the greater the interest of the rest of the project participants. In other words, a *DAI* invested by an individual investor has a higher *return* if the project is more supported by the rest of the people[7](#dfref-footnote-7).

Let's see it in an example. If our Investor 1 was undecided between investing 1 DAI to the project, knowing that 2 is going to invest, then the account for him should be, as we saw, that the return of investing 1 DAI will result in 9 of total investment. Now let's compare the case with the situation where the 4 DAIs that are invested by Investor 2 are actually being contributed by 4 different investors that each contribute 1 DAI. The fund account would translate into securing a target of 25 DAI total, and should cover the difference of 20. The return on DAI invested by Investor 1 results in 25 DAI. We can see then that the greater the number of donors, the greater the incentives for individual investment.

# Challenges and open questions

The 8th round of Gitcoin Grants funding is currently happening. The different rounds experienced different elements in their design, such as the possibility to re-finance projects from previous rounds (with the aim of making financing sustainable for projects), and improvements to the site that allow investing in several projects simultaneously.

So far, the amounts that have been financed are not so large as to guarantee the sustainability of a large software development project. In few cases some developers achieved a financing amount similar to what they would have in a full-time job.

Problems have also appeared, such as *identity* (a.k.a. [sybil attack](https://es.wikipedia.org/wiki/Ataque_Sybil)) and *collusion* fraud. We could say that both problems are stimulated by the fact that the same amount of money contributed by multiple people adds up to more than if they were contributed by a single one[8](#dfref-footnote-8).

Other important issues from my point of view have to do, on the one hand, with the fact that social efficiency, at the end of the day is tied to the perception of sufficient funds by the matching fund (A point I propose analyzing in detail in this [separate document](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3702318)). This is an issue that may be particularly important for the design of the mechanism, especially considering that the funds (in excess) that are required for the matching fund rise rapidly (according to the square of the number of contributors). The question, then, is to what extent a mechanism of this type can withstand the needs of philanthropic financing.

Beyond these problems, the properties of this mechanism that I referred to above, of balancing the system to one that makes a greater representation of the majorities, make it especially interesting. In fact, the close cousin of this mechanism, *quadratic voting*, has become very popular and has already been tested in various contexts[9](#dfref-footnote-9).

Going back to the cities, these properties could be especially attractive. As Buterin, Hitzig, and Weyl explain, it is precisely their ability to promote the demands of small groups, such as those of neighbors who have very local problems and who are not well represented by the median voter in committees or city legislatures.

Exploring other extensions, such as allowing voting or negative financing, could also help to think about projects that may involve negative externalities. An application to think about in the context of cities can be projects that stimulate gentrification and urban displacement, in order to reestablish a balance between economic power and local capacity.

# References

Buterin, Vitalik, Zoë Hitzig, and Eric Glen Weyl. 2018. "Liberal Radicalism: A Flexible Design For Philanthropic Matching Funds." *SSRN Electronic Journal*. <https://doi.org/10.2139/ssrn.3243656>.

Lalley, S. P., & Weyl, E. G. (2018, May). Quadratic voting: How mechanism design can radicalize democracy. In *AEA Papers and Proceedings* (Vol. 108, pp. 33-37).

Pasquini, Ricardo, A Note on Quadratic Funding under Constrained Matching Funds (September 30, 2020). Available at SSRN: <https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3702318>

Smolka, M. O. (2012). A new look at value capture in Latin America. *Land Lines*, *24* (3), 10-15.

Stiglitz, J. E. (1977). The theory of local public goods. In *The economics of public services* (pp. 274-333). Palgrave Macmillan, London.

Synopsis (2020), Open source security and risk analysis report.

---

1 I present here some ideas on quadratic financing, whose main reference is Buterin, Hitzig, and Weyl (2018). The [Radical X Change Foundation page](radicalxchange.org) provides a lot of information related to the quadratic voting system and related material.[↩](#ref-footnote-1 "back to document")

2 See for example <https://es.slideshare.net/SFScon/04-carlo-daffarasfscon>[↩](#ref-footnote-2 "back to document")

3 Kevin Owocki, the founder of Gitcoin, gives a very interesting presentation on this topic [here](https://www.youtube.com/watch?v=F2yeOFlRE0E&list=LLJU2HybiPCRueodu9fxO8nA).[↩](#ref-footnote-3 "back to document")

4 For a discussion of capital gains capture instruments in the context of Latin America see Smolka (2012) available [here] [<https://www.lincolninst.edu/sites/default/files/pubfiles/2099_1420_New_Look_at_Value_Capture_Latin_America_0712LL>. pdf].[↩](#ref-footnote-4 "back to document")

5 A classic theoretical reference on the optimality of these instruments is Stiglitz (1977). The literature also refers to the optimality of these instruments as the [Henry George Theorem](https://es.wikipedia.org/wiki/Henry_George).[↩](#ref-footnote-5 "back to document")

6 More precisely, the rule seeks that the total amount of financing received by the project is equal to the square of the sum of the contributions taken at root.  In this way, large contributions are penalized and small contributions are enhanced.[↩](#ref-footnote-6 "back to document")

7 More precisely, my contribution from an extra DAI has greater value for me inversely proportional to the relative size of my contribution with respect to that of others.[↩](#ref-footnote-7 "back to document")

8 Vitalik Buterin, the creator of Ethereum, explains them very well in this [note] [<https://vitalik.ca/general/2019/12/07/quadratic.html>].[↩](#ref-footnote-8 "back to document")

9 See Lalley, S. P., & Weyl, E. G. (2018, May), and more information in the [Radical X Change webpage](radicalxchange.org).[↩](#ref-footnote-9 "back to document")
