---
title: "Efectos ley de alquileres CABA #1"
date: "2019-07-17"
slug: "efectos-ley-de-alquileres-caba-1"
lang: "es"
categories: ["Causal Inference", "Economics", "Uncategorized", "Urban Economics"]
tags: ["buenos aires", "econometrics", "natural experiment", "rental market", "spatial regression discontinuity"]
excerpt: "[latexpage]In englishComparto aquí un&nbsp; análisis preliminar de los efectos de la ley de alquileres, sancionada en 2017, sobre los valores de alquiler. Esta ley, declarada inconstitucional en Mayo de este año, libró a los inquilinos del pago de la comisión inmobiliaria, al tiempo que también impu"
draft: false
---

Hay una actualización de este post [aquí](https://ricardopasquini.com/efectos-de-la-ley-de-alquileres-caba-2017-2/)

[In english](https://ricardopasquini.com/efectos-ley-de-alquileres-caba-#2)
Comparto aquí un ejercicio de análisis de los efectos de la ley de alquileres de la Ciudad de Buenos Aires, sancionada en 2017, sobre los valores de alquiler. Esta ley, declarada inconstitucional en Mayo de este año, libró a los inquilinos del pago de la comisión inmobiliaria, al tiempo que también impuso una comisión máxima a ser pagada a las inmobiliarias. En particular, una de las cuestiones que se discutió entre los que cuestionaban la ley, es que la medida no tendría efecto positivo sobre los inquilinos, ya que los propietarios, desde entonces a cargo del costo de la comisión, trasladarían ese costo al valor del alquiler. El propósito de este post es indagar en esa hipótesis, y en la forma que podría verificarse en la data. La propuesta aquí es la estimación del efecto como parte de un modelo de los valores de alquiler, siguiendo una metodología del tipo cuasi-experimental.
La metodología, los datos, y el código (Python+Stata), están abiertos en este proyecto en [github](https://github.com/rpasquini/efectos-ley-alquileres). Este es un ejercicio en progreso y en futuros posts seguramente agregaré más resultados y estimadores.

### Sobre la ley

El 8 de Septiembre de 2017 la legislatura de la Ciudad de Buenos Aires dictaminó la [ley 5859](https://boletinoficial.buenosaires.gob.ar/normativaba/norma/377206), que entró en vigencia el 16 de septiembre (más info en las noticias: [Aquí](https://www.lanacion.com.ar/buenos-aires/los-cuatro-puntos-claves-de-la-nueva-ley-de-alquileres-nid2056279), [aquí](http://www.defensoria.org.ar/noticias/alquileres-desde-hoy-la-comision-la-pagara-el-dueno/)).
Esta ley fue sancionada con el objetivo de beneficiar a los inquilinos. La ley estableció, en primer lugar, que la comisión inmobiliaria no sería pagada por los inquilinos, sino por los dueños. Esto modificó lo que era la práctica habitual, en la cual se cargaba al inquilino con el costo. Esto implicaría una reducción en el costo de entrada a un contrato de alquiler para los inquilinos, ya que estos en muchos casos solían pagar un mes, o más en términos de comisión. Además, la ley estableció un máximo para esta comisión, correspondiente a un mes extra (el equivalente a 4,15% -1 mes sobre 24- del valor total del contrato) (Nota: Era algo común ver comisiones más elevadas (1.5 o 2 meses de alquiler)). Las inmobiliarias no podrían cobrar por otros gastos, como costos de gestoría de informes (condiciones de dominio, gravámenes e inhibiciones). Por último, la ley obligó a todas las inmobiliarias a mostrar un cartel que advierta de esta nueva modalidad a los locatarios, sobre los puntos anteriormente mencionados, y designó al Instituto de Vivienda de la Ciudad (IVC) como el encargado de velar por los derechos de los inquilinos y de los propietarios, en conjunto con la Defensoría del Pueblo de la Ciudad para brindar asistencia legal gratuita.
Proyectos en alguna medida similares fueron discutidos luego en la Provincia de Buenos Aires 1 y a nivel nacional (ver más [aquí](https://tn.com.ar/economia/el-gobierno-va-por-la-revancha-con-la-ley-de-alquileres-y-prepara-un-nuevo-proyecto_954937)), pero hasta el momento no se ha concretado una sanción definitiva en estos casos.
Este año, el 10 de Mayo de 2019, la Cámara en lo Contencioso Administrativo declaró inconstitucional la ley de [alquileres](https://www.lanacion.com.ar/tema/alquileres-tid59290). (Noticias: [aqui](https://www.lanacion.com.ar/buenos-aires/la-justicia-declaro-inconstitucional-ley-alquileres-ciudad-nid2237243) y [aqui)](https://www.ambito.com/ciudad-la-justicia-declaro-inconstitucional-la-ley-alquileres-n5025618). Los medios sugieren que el Gobierno de la Ciudad continuará esta disputa legal para mantener en vigencia la ley.

### *Sobre efectos teóricos de la ley*

Consideremos en primer lugar la transferencia del pago de la comisión al propietario y el argumento que sugiere que esta medida no tendrá un efecto positivo en los inquilinos. Bajo este argumento, los propietarios reaccionaron aumentando el valor de los alquileres, de manera de neutralizar el costo extra que tienen que afrontar a causa de la ley. Es esta idea razonable?
En efecto, una argumentación de ese tipo podría surgir de un simple modelo teórico de oferta y demanda agregada. Un modelo simplificado de ese tipo, se grafica más abajo. Las cantidades de departamentos demandados y ofrecidos para alquiler se representan de acuerdo a los precios de alquileres. Si no existiesen las comisiones, y las transacciones pudieran hacerse sin necesidad de intermediarios, el equilibrio se daría en la intersección de las curvas de oferta y demanda. Sin embargo, en presencia de las comisiones, el mercado de alquileres encuentra *un equilibrio* en donde lo que desembolse el inquilino (en total), menos la comisión que se lleve la inmobiliaria (llamémosle  ), será lo que reciba el dueño. En el gráfico, el equilibrio queda definido por los precios  ,  y la cantidad de inmuebles alquilados . Es más, en un esquema clásico de este tipo, surge la observación de que, bajo condiciones normales no importará sobre *quien caiga* la *obligación de transferir el dinero* de la comisión a la inmobiliaria. La carga final de la comisión se compartirá entre ambas partes del mercado, dependiendo de qué parte tolere más la pérdida que implica el pago de la comisión (i.e., qué curva sea más inelástica).
![img](/media/2019/07/b14db0ab3a565409881b0ea4e7a5eec9.png)
En otras palabras, bajo estos supuestos clásicos, podríamos resumir la situación antes y después de transferir la obligación de pagar la comisión, de acuerdo al modelo clásico, se podría resumir así:

| Antes de la ley (Obligación del inquilino) | Después de sancionada la ley (Obligación del propietario) |
| --- | --- |
| Inquilinos ofrecen  a los dueños y pagan la comisión *C* a la inmobiliaria. El costo para los inquilinos es + | Propietarios cobran  de alquiler y pagan la comisión C. El costo para los inquilinos es  (=+) |

A los fines del análisis empírico que nos interesa aquí, es importante notar que:
i) A raiz de la transferencia del pago de inquilinos a propietarios, deberíamos observar un incremento en los precios ofrecidos por los propietarios, que se debe a la incorporación de (parte de) la comisión al precio.
ii) El *bienestar agregado* de los inquilinos (**2)** se mantiene sin cambios.
¿Cuál sería la magnitud esperada del incremento? En principio, como el alquiler es fijado durante el período de 24 meses (más los reajustes respectivos), entonces no es razonable que se traduzca en un aumento del valor del alquiler mensual completamente, sino que el incremento se distribuya durante el período. Más que pensar que la comisión se va a trasladar en 24 meses, en el contexto de nuestra economía, con su alta tasa de interés real, sería más razonable pensar que la mayor parte parte sea traslada a la primera parte del contrato.
Pasemos ahora a la limitación del monto de la comisión a un máximo del equivalente a 1 mes de alquiler. El efecto espero aquí dependerá de cuál sea la comisión que los inquilinos se encuentren pagando, y es esperable que varíe según el segmento del mercado. El gráfico más arriba sugiere que si C es menor, entonces una de las consecuencias es que el precio  será menor, (y  será mayor) con lo que la carga trasladada al valor de alquiler será menor. De este esquema simple entonces, podemos inferir que:
iii) El bienestar de los inquilinos, y también el de los propietarios aumentará si la comisión cobrada por las inmobiliarias se reduce. Es decir, si la limitación de la comisión en este caso (a un mes) implicó una reducción en lo que las inmobiliarias cobraban, parte del efecto se traducirá en un menor precio a pagar por los inquilinos.

### Idea de la Estrategia de Identificación

El propósito ahora es la identificación del efecto de la introducción de la ley sobre los valores de alquiler. Esta identificación tiene la dificultad de que afectó a todo el territorio de la Ciudad de Buenos Aires, y de observarse solo la evolución del alquiler promedio en CABA, el efecto se podría confundir con muchos otros factores que afectaron a los alquileres en su conjunto durante el periodo de interés. Por ejemplo, factores a tener en cuenta serían el nivel de inflación, (ya que los contratos están mayormente denominados en pesos), alteraciones en el tipo de cambio podrían tener un efecto en los valores de alquiler observado, etc.
Como estrategia, propongo ver a los cambios regulatorios como un experimento natural, que alteró las condiciones del mercado de alquiler en la Ciudad de Buenos Aires, relativo a la Provincia. La Ciudad y la Provincia tomadas en su conjunto, sin embargo, son difícilmente comparables. La idea principal de la identificación aquí se basa en explotar la discontinuidad que ofrece el límite de la Ciudad con la Provincia de Buenos Aires. La Ciudad se encuentra envuelta por la Provincia, y existen propiedades en alquiler en ambos lados del límite de la Ciudad, al menos en gran parte de su extensión. Más aún, el gradiente de precios de alquiler de la ciudad, sugiere que, al menos en promedio, hay un descuento que es función de la distancia al centro de negocios de la Capital. Al tomar viviendas que están cercanas en el gradiente, nos aseguramos de que su valuación será similar. Si el cambio regulatorio introdujo una modificación en los precios de CABA, entonces deberíamos observar una discontinuidad en esa relación.
Pero más aún, tendríamos también que tener en cuenta que posiblemente ya existía previamente una discontinuidad en los precios que se debe al cambio entre Capital y Provincia. Después de todo, hay múltiples diferencias, por ejemplo, atribuibles a la forma en que se gestiona el territorio en la Ciudad y en los municipios respectivos de Provincia, y que podrían generar discontinuidades en el precio. Lo que se propondrá como estrategia entonces, es que la discontinuidad haya cambiado luego de la introducción del cambio regulatorio.
En términos técnicos, propongo la estimación de un modelo de diseño por discontinuidad espacial. Para una introducción a diseño de regresión por discontinuidad ver, por ejemplo [Gertler et. a. 2011](https://elibrary.worldbank.org/doi/abs/10.1596/978-0-8213-8681-1), [Angrist and Pischke(2014)](https://books.google.com.ar/books?hl=es&lr=&id=s2eYDwAAQBAJ&oi=fnd&pg=PR11&dq=angrist+pischke+mastering&ots=gLysDOCPat&sig=OVbnd7H3vJTzaIyVQyoyMo8Nwdk). Algunos antecedentes espaciales similares son [Hidano et al (2015)](https://www.sciencedirect.com/science/article/pii/S0166046215000460), [Egger and Lassman (2015)](https://academic.oup.com/ej/article/125/584/699-745/5077888).
Una limitación de esta estrategia sería si los potenciales inquilinos, ante el aumento de los preios en Capital, buscaron alquilar en Provincia. Esto violaría una de los supuestos bajo el cual esta estrategia es válida. Sin embargo, cabe notar también que de existir este problema, el sesgo tendería a reducir el efecto de interés, por lo que si observamos un aumento en la discontinuidad será suficiente para verificar la hipótesis.

### Datos

Los datos analizados aquí surgen de la data abierta de [Properati](https://www.properati.com.ar/data/). Se refieren a anuncios de alquiler (valores ofrecidos), y colectados de la principales plataformas online de alquiler. El período de los datos cubre 2016-2018, es decir, un año y 8 meses antes del cambio y un año y 4 meses posterior.
Estas ofertas fueron mapeadas y agrupadas en cuatro grupos, de manera de poder tener resultados para distintos sectores del mercado.
**Ofertas de alquiler en un buffer de 1000 metros en el límite de la Ciudad**
![1563380990251](https://www.dropbox.com/s/bo4f4eebstf59mt/1563380990251.png?dl=1)

### *Algunas Estadísticas*

Las siguientes son algunas estadísticas descriptivas de las ofertas de alquiler de departamentos en el período. La primera variable en la tabla presenta el valor del metro cuadrado en pesos, la segunda variable price\_apro es el valor del alquiler en pesos, luego logprice es el mismo precio en logaritmos. Delta es la distancia al límite (definida negativa en la capital). Treatment es la dummy de CABA. Post indica al periodo post cambio regulatorio, y DD es una interacción que explicaremos luego.
![img](/media/2019/07/2a6c57560f43fc25729c92d57f982f76.png)
![img](/media/2019/07/62eed792d9e3747ef3dd0b446f8ba531.png)
\*Se descartaron valores extremos.

#### Estimación Econométrica

El modelo de interés puede especificarse de la siguiente forma:
Donde es el precio de la oferta,  es la distancia al límite (definida de forma negativa para las distancias dirección capital),  es la dummy del período post-cambio de ley, y  es la dummy que señala con 1 a CABA.
El parámetro de principal interés es el coeficiente de interacción Post \* CABA ya que indicará un aumento en la discontinuidad posterior a la introducción de la ley. En la regresión abajo DD es la interacción.
Comenzando por el valor del alquiler en m2, las estimación de base es :
![img](/media/2019/07/14cb8342d5c3e517a431a548681c25b8.png)
Podemos ver en el coeficiente de "delta" ( ) que se verifica la existencia de un gradiente en los precios, tal como lo habíamos hipotetizado. El gradiente es económicamente significativo, representando aproximadamente 1 desvío estándar de precios por cada 500 metros.
También podemos ver que una vez que se tiene en cuenta el gradiente, el modelo no necesita diferenciar entre CABA y Provincia (i.e., el coeficiente de treatment (CABA) no logra rechaza el test de significancia).
La variable post muestra el incremento esperado en los precios, que podría ser el reflejo de la inflación.
Finalmente, la variable de interés, DD en este caso muestra que la discontinuidad se incrementó luego de sancionada la ley. En principio, esto corroboraría la hipótesis de la transferencia al precio.
Las predicciones del modelo pueden observarse en el gráfico a continuación:
**Valores de alquiler por metro cuadrado**
![img](/media/2019/07/dc3164224b7eefe75926e87904a848b9.png)
Como alternativa a la especificación anterior, aquí también tenemos la ecuación en logaritmos:
![img](/media/2019/07/4c4439c160432173d72c7c9f79135466.png)
Lo curioso de esta especificación es que se mantiene la diferencia negativa en favor de Provincia una vez que se incorporó el gradiente de precios. La conclusión sobre el efecto de la regulación es también coincidente con lo esperado. En este caso el coeficiente sugiere un aumento un 10% adicional que podría ser atribuible al cambio de regulación.

#### Resultados por áreas

Como mencionamos anteriormente al discutir la teoría, los efectos esperados podrían presentar diferencias de acuerdo a las condiciones específicas de los mercados en cuestión. De manera de permitir diversidad entre los efectos dividimos la muestra en cuatro áreas:
![1563380838869](https://www.dropbox.com/s/ordcdyvhw3r0et3/1563380838869.png?dl=1)
Luego, generalizamos la especificación econométrica, para permitir efectos específicos por áreas. La estimación resultante del modelo en logaritmos es:
![1563377787782](https://www.dropbox.com/s/jl7htivs4g0ysj1/1563377787782.png?dl=1)
Podemos ver ahora, en primer lugar, que el efecto revierte el signo para el área 1. Creo que en este caso podríamos estar confundiendo el efecto con una renovación del área importante que ocurrió en Vicente López. Para las restantes áreas podemos ver que se mantiene el efecto, siendo cada vez mayor, en las áreas 2 (5%) , 3 (15%) y 4 (18%).

## **En resumen**

De acuerdo a estos primeros resultados, el aumento en la discontinuidad de precios observada entre Provincia y Capital es consistente con la hipótesis de que los propietarios trasladaron la comisión al contrato de alquiler. La magnitud del efecto encontrada hasta el momento, sugiere que el traslado fue importante, especialmente en las áreas sur y sureste del límite de la ciudad.
**Próximos pasos**
Una pregunta que puede surgir es cuanto aplican estos datos a la generalidad de la Ciudad. Son acaso estos datos una muestra representativa? No lo son, pero la consideración de las distintas áreas parecer ser representativa de distintos segmentos del mercado. Es algo que podemos examinar en un próximo post.
Ya que tenemos data para hacerlo podríamos modelar explícitamente las tendencias en las áreas respectivas.
Otro de los efectos que se ha mencionado en los medios, es que la medida también podría haber traído un aumento en la cantidad de ofertas a través de dueños directos. No tengo por el momento data para verlo, pero sería interesante avanzar en esa dirección.
**Notas**
1 En Provincia de Buenos Aires, el proyecto que elimina las comisiones para inquilinos obtuvo media sanción en Diciembre de 2018. Ver más [aquí](https://www.lanacion.com.ar/propiedades/alquileres-avanza-ley-provincia-buenos-aires-nid2198032)
2 Medido por el excedente del consumidor.
I share here a preliminary analysis of the effects of the City of Buenos Aires rent law, enacted in 2017, on rental values. This law, declared unconstitutional in May of this year, freed the tenants from the payment of the real estate commission, while also imposing a maximum commission to be paid to the real estate companies. In particular, one of the issues that was discussed among those who questioned the law in the media, is that the measure would not have a positive effect on the tenants, since the owners, since then in charge of the cost of the commission, would transfer that cost to the value of the rent. The purpose of this post is to investigate that hypothesis, and in the way that could be verified in the data. The proposal here is the estimation of the effect as part of a model of rental values, following a methodology of the quasi-experimental type.
The methodology, the data, and the code (Python + Stata) are open in this project on [github](https://github.com/rpasquini/efectos-ley-alquileres) . This is an exercise in progress and in future posts I will surely add more results and estimators.

### About the law

On September 8, 2017, the legislature of the City of Buenos Aires passed [Law 5859](https://translate.google.com/translate?hl=es&prev=_t&sl=es&tl=en&u=https://boletinoficial.buenosaires.gob.ar/normativaba/norma/377206) , which became effective on September 16 (more info in the news: [Here](https://translate.google.com/translate?hl=es&prev=_t&sl=es&tl=en&u=https://www.lanacion.com.ar/buenos-aires/los-cuatro-puntos-claves-de-la-nueva-ley-de-alquileres-nid2056279) , [here](https://translate.google.com/translate?hl=es&prev=_t&sl=es&tl=en&u=http://www.defensoria.org.ar/noticias/alquileres-desde-hoy-la-comision-la-pagara-el-dueno/) ).
This law was sanctioned with the objective of benefiting the tenants. The law established, first, that the real estate commission would not be paid by the tenants, but by the owners. This modified what was usual practice, in which the tenant was charged with the cost. This would imply a reduction in the cost of entry to a rental contract for the tenants, since these in many cases used to pay a month, or more in terms of commission. In addition, the law established a maximum for this commission, corresponding to an extra month (equivalent to 4.15% -1 month over 24- of the total value of the contract) (Note: It was common to see higher commissions (1.5 or 2 months of rent)). The real estate agencies could not charge for other expenses, such as the costs of managing reports (conditions of ownership, liens and inhibitions). Finally, the law obliged all real estate agents to show a sign that warns of this new modality to tenants, on the points mentioned above, and appointed the Housing Institute of the City (IVC) as the person in charge of ensuring the rights of tenants and landlords, in conjunction with the City Ombudsman to provide free legal assistance.
Projects to a similar extent were discussed later in the Province of Buenos Aires 1 and nationally (see more [here](https://translate.google.com/translate?hl=es&prev=_t&sl=es&tl=en&u=https://tn.com.ar/economia/el-gobierno-va-por-la-revancha-con-la-ley-de-alquileres-y-prepara-un-nuevo-proyecto_954937) ), but so far has not been finalized a final sanction in these cases.
This year, on May 10, 2019, the Chamber of Administrative Litigation declared the [rent](https://translate.google.com/translate?hl=es&prev=_t&sl=es&tl=en&u=https://www.lanacion.com.ar/tema/alquileres-tid59290) law unconstitutional. (News: [here](https://translate.google.com/translate?hl=es&prev=_t&sl=es&tl=en&u=https://www.lanacion.com.ar/buenos-aires/la-justicia-declaro-inconstitucional-ley-alquileres-ciudad-nid2237243) and [here)](https://translate.google.com/translate?hl=es&prev=_t&sl=es&tl=en&u=https://www.ambito.com/ciudad-la-justicia-declaro-inconstitucional-la-ley-alquileres-n5025618) . The media suggests that the City Government will continue this legal dispute to keep the law in force.

### On theoretical effects of the law

Consider first the transfer of commission payment to the owner and the argument that suggests that this measure will not have a positive effect on the tenants. Under this argument, the owners reacted by increasing the value of the rents, in order to neutralize the extra cost they have to face because of the law. Is this idea reasonable?
Indeed, such an argument could arise from a simple theoretical model of aggregate supply and demand. A simplified model of this type is shown below. The amounts of apartments demanded and offered for rent are represented according to the rental prices. If there were no commissions, and transactions could be made without intermediaries, the equilibrium would occur at the intersection of supply and demand curves. However, in the presence of the commissions, the rental market finds *a balance* in what the tenant disburses (in total), less the commission that the real estate company takes (let's call it  ), it will be what the owner receives. In the chart, the balance is defined by the prices ,  and the amount of rented property . Moreover, in a classic scheme of this kind, the observation arises that, under normal conditions, it will not matter *who falls behind* the *obligation to transfer the money* from the commission to the real estate. The final charge of the commission will be shared between both parties of the market, depending on which party tolerates more the loss implied by the payment of the commission (ie, which curve is more inelastic).
![img](/media/2019/07/b14db0ab3a565409881b0ea4e7a5eec9.png)
In other words, under these classical assumptions, we could summarize the situation before and after transferring the obligation to pay the commission, according to the classical model, it could be summarized as follows:

| Before the law (Obligation of the tenant) | After the law is passed (Obligation of the owner) |
| --- | --- |
| Tenants offer  to the owners and pay commission *C* to the real estate company. The cost for the tenants is  + C | Owners charge  rent and pay the commission C. The cost for the tenants is  (=  + C) |

For the purposes of the empirical analysis that interests us here, it is important to note that:
i) Following the transfer of the payment of tenants to owners, we should observe an increase in the prices offered by the owners, which is due to the incorporation of (part of) the commission to the price.
ii) The *added well-being* of the tenants ( **2)** remains unchanged.
What would be the expected magnitude of the increase? In principle, since the rent is fixed during the 24-month period (plus the respective readjustments), then it is not reasonable that it be translated into an increase in the value of the monthly rent completely, but rather that the increase be distributed during the period. Rather than thinking that the commission will be transferred in 24 months, in the context of our economy, with its high real interest rate, it would be more reasonable to think that most of it is transferred to the first part of the contract.
Let's now turn to the limitation of the amount of the commission to a maximum of the equivalent of 1 month's rent. The effect I expect here will depend on what commission the tenants are paying, and it is expected to vary according to the market segment. The graph above suggests that if C is lower, then one of the consequences is that the price  will be lower, (and  will be higher) with which the load transferred to the rental value It will be less. From this simple scheme then, we can infer that:
iii) The welfare of the tenants, and also that of the owners, will increase if the commission charged by the real estate companies is reduced. That is, if the limitation of the commission in this case (one month) involved a reduction in what the real estate agencies charged, part of the effect will result in a lower price to be paid by the tenants.

## Identification Strategy Idea

The purpose now is the identification of the effect of the introduction of the law on rental values. This identification has the difficulty that affected the whole territory of the City of Buenos Aires, and if only the evolution of the average rent in CABA is observed, the effect could be confused with many other factors that affected the rents as a whole during the period of interest. For example, factors to take into account would be the level of inflation, (since contracts are mostly denominated in pesos), alterations in the exchange rate could have an effect on observed rental values, etc.
As a strategy, I propose to see the regulatory changes as a natural experiment, which altered the conditions of the rental market in the City of Buenos Aires, relative to the Province. The City and the Province taken as a whole, however, are hardly comparable. The main idea of identification here is based on exploiting the discontinuity offered by the boundary of the City with the Province of Buenos Aires. The City is surrounded by the Province, and there are rental properties on both sides of the City's boundary, at least to a large extent. Moreover, the gradient of rental prices in the city suggests that, at least on average, there is a discount that is a function of the distance to the business center of the Capital. By taking housing that is close to the gradient, we make sure that your valuation will be similar. If the regular change introduced a change in the prices of CABA, then we should observe a discontinuity in that relation.
But even more, we should also bear in mind that there may have been a discontinuity in prices previously due to the change between Capital and Province. After all, there are multiple differences, for example, attributable to the way in which the territory is managed in the City and in the respective municipalities of the Province, and which could generate discontinuities in the price. What will be proposed as a strategy then, is that the discontinuity has changed after the introduction of the regulatory change.
For an introduction to regression discontinuity designs see, for example, [Gertler et. a. 2011](https://elibrary.worldbank.org/doi/abs/10.1596/978-0-8213-8681-1), [Angrist and Pischke(2014)](https://books.google.com.ar/books?hl=es&lr=&id=s2eYDwAAQBAJ&oi=fnd&pg=PR11&dq=angrist+pischke+mastering&ots=gLysDOCPat&sig=OVbnd7H3vJTzaIyVQyoyMo8Nwdk). Some spatial applications are found in [Hidano et al (2015)](https://www.sciencedirect.com/science/article/pii/S0166046215000460), [Egger and Lassman (2015)](https://academic.oup.com/ej/article/125/584/699-745/5077888).
A limitation of this strategy would be if the potential tenants, faced with the increase in prices in Capital, sought to rent in the Province. This would violate one of the assumptions under which this strategy is valid. However, it should also be noted that if this problem exists, the bias would tend to reduce the effect of interest, so if we observe an increase in the discontinuity it will be sufficient to verify the hypothesis.

#### ***Data***

The data analyzed here comes from the open data of [Properati](https://translate.google.com/translate?hl=es&prev=_t&sl=es&tl=en&u=https://www.properati.com.ar/data/) . They refer to rental ads (offered values), and collected from the main online rental platforms. The data period covers 2016-2018, that is, one year and 8 months before the change and one year and 4 months after.
These offers were mapped and grouped into four groups, in order to have results for different sectors of the market.
**Offers of rent in a buffer of 1000 meters in the limit of the City**
![1563380990251](https://www.dropbox.com/s/bo4f4eebstf59mt/1563380990251.png?dl=1)
*Some statistics*
The following are some descriptive statistics of the apartment rental offers in the period. The first variable in the table presents the value of the square meter in pesos, the second variable price\_apro is the value of the rent in pesos, then logprice is the same price in logarithms. Delta is the distance to the limit (defined negative in the capital). Treatment is the dummy of CABA. Post indicates the period after regulatory change, and DD is an interaction that we will explain later.
![img](/media/2019/07/2a6c57560f43fc25729c92d57f982f76.png)
![img](/media/2019/07/62eed792d9e3747ef3dd0b446f8ba531.png)
\* Extreme values were ruled out.
*Econometric Estimation*
The model of interest can be specified as follows:
Where  is the price of the offer,  is the distance to the limit (defined negatively for capital direction distances) , is the dummy of the post-change period of the law, and  is the dummy that points with 1 to CABA.
The parameter of main interest in this case is  since it will indicate an increase in the discontinuity after the introduction of the law.
Starting with the rental value in m2, the base estimate is:
![img](/media/2019/07/14cb8342d5c3e517a431a548681c25b8.png)
First, we can see that the existence of a gradient in prices is verified, just as we had hypothesized. The gradient is economically significant, representing 1 standard deviation for every 500 meters.
We can also see that once the gradient is taken into account, the model does not need to differentiate between CABA and Province.
The post variable shows the expected increase in prices, which could be a reflection of inflation.
Finally, the variable of interest, DD in this case shows that the discontinuity was enlarged after the law was enacted. In principle, this would corroborate the hypothesis of the transfer to the price.
The predictions of the model can be seen in the graph below:
**Rental values per square meter**
![img](/media/2019/07/dc3164224b7eefe75926e87904a848b9.png)
As an alternative to the previous specification, we also have the equation in logarithms:
![img](/media/2019/07/4c4439c160432173d72c7c9f79135466.png)
The curious thing about this specification is that the negative difference in favor of the Province is maintained once the price gradient was incorporated. The conclusion about the effect of the regulation is also coincident with what was expected. In this case, the coefficient suggests an additional 10% increase that could be attributable to the change in regulation. While superior to what I had in mind, it is not out of what we had previously raised.

#### Results by area

As we mentioned earlier when discussing the theory, the expected effects could present differences according to the specific conditions of the markets in question. In order to allow variability among the effects, we divided the sample into four areas:
![1563380838869](https://www.dropbox.com/s/ordcdyvhw3r0et3/1563380838869.png?dl=1)
Then, we generalize the econometric specifics, to allow specific effects by areas. The resulting estimate of the model in logarithms is:
![1563377787782](https://www.dropbox.com/s/jl7htivs4g0ysj1/1563377787782.png?dl=1)
We can see now, in the first place, that the effect reverses the sign for Area 1. I think that in this case we could be confusing the effect with a renewal of the important area that occurred in Vicente Lopez. For the remaining areas, we can see that the effect is maintained, increasing in Areas 2 (5%), 3 (15%) and 4 (18%).
**Preliminary conclusions**
The increase in the discontinuity of prices observed between Province and Capital seems to suggest that the owners increased their offer values, and this is consistent with the hypothesis that they transferred the commission to the rental contract. The magnitude of the effect found so far suggests that the transfer was important, especially in the south and southeast areas of the city limits.
**Next steps**
One question that may arise is how much this data applies to the generality of the City. Does this data constitute a representative sample? Clearly not, but the consideration of the different areas seems to be representative of different segments of the market. This is something that we can examine in a next post.
In terms of the modelling strategy, since we have data to do it, we could explicitly model the trends in the respective areas. We could also examine in a greater extent the implicit assumption of time constant discontinuity between the City and the Province.
Another effect that has been mentioned in the media, is that the measure could also have brought about an increase in the number of offers through direct owners. I do not have at the moment to see it, but it would be interesting to move in that direction.
**Notes**
1 In the Province of Buenos Aires, the project that eliminates commissions for tenants received a half sanction in December 2018. See more [here](https://translate.google.com/translate?hl=es&prev=_t&sl=es&tl=en&u=https://www.lanacion.com.ar/propiedades/alquileres-avanza-ley-provincia-buenos-aires-nid2198032)
2 Measured by consumer surplus.
