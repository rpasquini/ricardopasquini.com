---
title: "Efectos de la ley de Alquileres CABA"
date: "2019-11-21"
slug: "efectos-de-la-ley-de-alquileres-caba-2017-2"
lang: "es"
categories: ["Causal Inference", "Economics", "Uncategorized", "Urban Economics"]
tags: ["Economía Urbana", "Ley Alquileres", "Mercado de Alquileres"]
excerpt: ""
draft: false
---

Efectos de la Ley de Alquileres Noviembre


[Aquí](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3491321) encontrarán una primera versión[1](#dfref-footnote-1) de un documento de trabajo que analiza los efectos de la ley de alquileres de CABA, promulgada en 2017. Bienvenidos los comentarios.

La ley de CABA de 2017 introdujo algunas modificaciones a la operación del mercado, incluyendo la transferencia de la obligación del pago de la comisión del inquilino al propietario, entre otras medidas que mencioné en un [post anterior](https://ricardopasquini.com/efectos-ley-de-alquileres-caba-1/).

En el documento, me propuse medir los efectos de la ley de alquileres de la Ciudad de Buenos Aires de 2017 en los valores de alquiler. La principal motivación detrás de la metodología propuesta es evitar confundir la medición del efecto con otros factores que pudieran afectar los valores de manera contemporánea, como podría ser el efecto de la inflación, las modificaciones en el valor que ocurren a raíz de las tendencias de transformación urbana, y evitar sesgos de selección en la comparación con otras ciudades. Todo el análisis está basado en datos abiertos, de ofertas de alquiler publicadas en [Properati](www.properati.com). El código completo también estará próximamente disponible.

El análisis es posible gracias a algunas particularidades de la Ciudad de Buenos Aires, más precisamente el hecho de estar rodeada, en el mismo aglomerado urbano, por otras jurisdicciones de la Provincia de Buenos Aires. Propongo una estrategia de identificación que explota las diferencias en el tiempo de las propiedades que están en el límite de la ciudad.

Los resultados encontrados hasta aquí indican que el valor de alquiler aumentó en la Ciudad, de manera atribuible a la ley, en una magnitud promedio de 5%. Esta magnitud es consistente con la idea teórica de que los propietarios transfieren el valor de la comisión a los inquilinos, distribuyendo el valor a lo largo del contrato. En otras palabras, es coherente con un efecto *financiero*, donde los propietarios se ven obligados a financiar a los inquilinos en el pago de la comisión.

Otro aspecto interesante de esta aplicación es el grado de variabilidad que se puede encontrar a lo largo del límite de la Ciudad, que abarca diferentes segmentos del mercado de alquiler, con implicancias en la validez externa de la metodología. Los resultados hasta aquí sugieren mayores aumentos en los precios de alquiler en áreas de valor de alquiler relativamente más bajo. Esto también es consistente con la hipótesis de transferencia, siempre que los propietarios de propiedades menos valiosas tengan una tasa de descuento temporal más alta.

En términos promedio, la magnitud del aumento de la renta sugiere que la ley no tuvo efectos en términos de valor presente del contrato. Sin embargo, el efecto de transferir la obligación financiera, en un mercado donde el acceso al crédito puede ser restrictivo, puede tener un efecto no trivial en la accesibilidad a la vivienda. Como la obligación de financiar la comisión se transfiere al propietario, éste también podría reaccionar buscando otros recursos, como aumentar el depósito de garantía. Si bien el depósito en principio tiene que ser devuelto al final del contrato, el mismo podría ser utilizado inmediatamente para pagar la comisión. Esto es lo que parece surgir de los datos, donde la evidencia *sugiere* que los requerimientos del depósito cambiaron. Si esto fue así, en un porcentaje significativo de casos el efecto financiamiento fue cancelado por el requerimiento adicional de algunos propietarios.

El ejercicio en el documento no tiene el objetivo de cubrir todos los efectos de la ley, y está limitado por el tipo de datos que utilizo. Un análisis más completo de los efectos de la ley debería evaluar los efectos sobre la intermediación, por ejemplo, incluyendo la posibilidad de omitir al intermediario en otros mercados de propietarios directos y otros resultados de intermediación, como los efectos teóricos mencionados anteriormente en términos de aumentos en la rotación y emparejamiento (propietarios-inquilinos) menos eficiente, como se señala en la literatura teórica, que podría ser relevante en algunos mercados de alquiler.

---

1 Este es documento de trabajo en progreso, que todavía no atravesó el proceso de revisión para publicación, y como tal, los resultados pueden sufrir modificaciones.[↩](#ref-footnote-1 "back to document")
