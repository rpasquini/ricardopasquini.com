---
title: "Explicando Inferencia por Aleatorización a un futbolero"
date: "2022-11-14"
slug: "explicando-inferencia-por-aleatorizacion-a-un-futbolero"
lang: "es"
categories: ["Causal Inference", "Uncategorized"]
tags: []
excerpt: ""
draft: false
---

Explicando Inferencia por Aleatorización a un futbolero

# Explicando Inferencia por Aleatorización a un futbolero

[English version](#ingles)

Para celebrar una fecha importante, 5 amigos invitan a 5 jugadores de futbol profesional para jugar un partido. Los amigos no conocen a los jugadores profesionales. Los contrataron a través de un manager. Para que el encuentro sea más interesante, decidieron poner un premio importante al equipo ganador.

Los 5 amigos juegan bien, pero piensan que si ellos juegan contra los profesionales, van a perder con total seguridad. La idea entonces es armar equipos mezclados. ¿De cuántas formas se podrían armar los equipos? La respuesta es 252, que es la cantidad de formas en la que pueden seleccionarse 5 elementos de un grupo de 10 (i.e., número combinario C(10,5) )...

Bueno, resulta que minutos antes del partido, los amigos escuchan un rumor de que el manager podría ser un estafador, y los profesionales, en realidad, podrían ser solamente impostores. Los amigos todavía tiene interés en ganar, pero sobre todo quieren asegurarse de que el manager no los esté estafando!

Un primer amigo pensó lo siguiente: van a jugar los 5 amigos contra los 5 profesionales. Si pierden por mucha diferencia, entonces van a concluir que los jugadores eran efectivamente profesionales y el manager no era un estafador. Si la diferencia de goles es pequeña, o ellos ganan, entonces lo más probable es que el manager sea un chanta. Pero eso abrió una nueva pregunta: cuánta diferencia los dejaría seguros de que no los estarían estafando?

A un segundo amigo se le ocurrió una idea adicional: Durante el tiempo que tienen van a jugar varios partidos. En todos los partidos excepto en uno de ellos jugarán mezclados. Es decir, solo en un partido se enfrentarán los amigos contra los profesionales. En cada partido van a anotar el score. La mayor diferencia de goles en el score debiera darse en el partido que jueguen los 5 amigos contra los 5 profesionales. O, por lo menos, debiera darse una diferencia atípicamente grande con respecto al resto de los partidos. Si esto no se cumple, entonces podemos suponer que no eran profesionales.

![A football match with imposters with Dall-e](https://www.dropbox.com/s/1cm5wz9r5mj0csx/image-20221112101523865.png?dl=1)

*Inferencia por Aleatorización*

En un contexto de una evaluación experimental, el método de Inferencia por Aleatorización, propone identificar si un cierto Tratamiento () tiene un efecto en los resultados individuales () de un grupo que lo recibe. En nuestro ejemplo, el grupo de los Tratados son los supuestos profesionales, cuya habilidad superior es lo que queremos testear.

El método propone testear si el Tratamiento tuvo efecto comparando una cierta medida de la diferencia de los resultados entre Tratados y no-tratados contra las que surgirían de comparar grupos aleatoriamente armados:

* En primer lugar, es necesario tomar una medida de la diferencia que hay en los resultados de los grupos Tratados y no Tratados. Podríamos tomar, por ejemplo, la diferencia entre el resultado promedio que obtuvieron los tratados y los no tratados. En nuestro ejemplo futbolero, este es el resultado del partido, que es una medida de la diferencia relativa entre los grupos. Así como en el futbol, en nuestra inferencia podríamos tomar otras medidas de diferencias entre grupos, por ejemplo la diferencia entre las *medianas* de los resultados, etc.

* En segundo lugar, para concluir si hubo efecto del Tratamiento vamos a comparar la diferencia entre los grupos de Tratados y no Tratados con las diferencias que surgirían de todos los grupos artificiales que pueden surgir si mezclamos los elementos. O dicho de otra manera, comparamos contra todas las asignaciones alternativas que podrían haber surgido del mecanismo de asignación aleatoria (pero que en la práctica no ocurrieron). En nuestro ejemplo futbolero, la idea era comparar la diferencia del resultado del partido entre amigos versus (supuestos) profesionales contra los resultados de todos los posibles partidos alternativos que podrían haber surgido de una conformación de grupos aleatoria.

* Notemos que al calcular los resultados de las comparaciones de los grupos *artificialmente construidos*, vamos a obtener efectivamente una lista de diferencias, cuya distribución podríamos analizar (usando un histograma). En el futbol debiera ser que la diferencia entre profesionales y no profesionales sea máxima, o un resultado atípico si lo comparamos con los partidos mezclados. Cuando hacemos inferencia también queremos ver cuán atípica es la diferencia entre los Tratados y no Tratados con respecto a la distribución de resultados que surgen de grupos mezclados. Una forma de medir la *atipicidad* será mirar en qué lugar de la distribución de posibles resultados la diferencia real se encuentra, algo que en la práctica podemos implementar fácilmente con un p-valor (i.e., una medida de la probabilidad acumulada del resultado encontrado).

English

# Explaining Inference by Randomization to a football fan

[English version](#english)

To celebrate a special ocassion, 5 friends invite 5 professional football players to play a game. Friends don't know the professional players. They were hired through a manager. To make the match more interesting, they decided to put a big prize on the winning team.

The 5 friends play well, but they think that if they play against the professionals, they will lose for sure. Then the idea is to put together mixed teams. In how many ways could the teams be assembled? The answer is 252, which is the number of ways in which 5 elements can be selected from a group of 10 (i.e., combinatorial number C(10,5) )...

Well, it turns out that minutes before the game, the friends hear a rumor that the manager might be a con man, and the professional players might actually just be imposters. The friends still have an interest in winning, but most of all they want to make sure the manager isn't scamming them!

A first friend thought the following: the 5 friends are going to play against the 5 professionals. If they lose by a lot, then they will conclude that the players were indeed professionals and the manager was not a con man. If the goal difference is small, or they win, then the manager is most likely a con man. But that opened up a new question: how much difference would make them sure they weren't being scammed?

A second friend came up with an additional idea: During the time they have, they are going to play several games. In all the games except one of them they will play mixed. That is, only in one match will friends face off against professionals. In each game they will write down the score. The greatest goal difference in the score should be in the game played by the 5 friends against the 5 professionals. Or, at least, there should be an atypically large difference with respect to the rest of the games. If this is not true, then we can assume that they were not professionals.

![A football match with imposters with Dall-e](https://www.dropbox.com/s/1cm5wz9r5mj0csx/image-20221112101523865.png?dl=1)

*Inference by Randomization*

In the context of an experimental evaluation, the Randomization Inference method proposes to identify if a certain Treatment () has an effect in the individual outcome's () of a group that receives it. In our example, the Treatment group are the so-called professionals, whose superior ability is what we want to test.

The method proposes to test if the Treatment had an effect by comparing a certain measure of the difference in the results between Treated and non-treated against those that would arise from comparing randomly assambled groups:

* First of all, it is necessary to take a measure of the difference in the results of the Treated and non-Treated groups. We could take, for example, the difference between the *average* result obtained by the treated and the untreated. In our football example, this is the result of the match, which is a measure of the relative difference between the groups. Notice that we could take other measures of differences between groups, for example the difference between the *medians* of the results, etc.
* Secondly, to conclude whether there was an effect of the Treatment, we are going to compare the difference between the Treated and Non-Treated groups against the differences that would arise from all the artificial groups that arise if we mix their elements. Or put another way, we compare against all alternative assignments that could have arisen from the random assignment mechanism (but did not occur in practice). In our soccer example, the idea was to compare the difference in the outcome of the match between friends versus the (presumed) professionals against the outcomes of all possible alternative matches that could have arisen from a random allocation.
* Note that by calculating the results of the comparisons of the *artificially constructed* groups, we are effectively going to obtain a list of differences, whose distribution we could analyze (for example, using a histogram). In the football example we expected the difference between professionals and non-professionals to be maximum. In other words, we expected an atypical result to what would be obtained for the distribution of mixed groups matches. When making inferences we also want to see how atypical the difference is between Treatment and non-Treatment with respect to the distribution of outcomes arising from mixed groups. One way to measure the *extremeness* is to look where in the distribution of results the actual score is, something that in practice can be done simply by implementing a p-value (i.e., a cumulative probability measure).
