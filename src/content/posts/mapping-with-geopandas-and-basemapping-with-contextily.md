---
title: "Mapping with geopandas and basemapping with contextily"
date: "2019-04-29"
slug: "mapping-with-geopandas-and-basemapping-with-contextily"
lang: "es"
categories: ["Coding Notes", "Uncategorized"]
tags: ["contextily", "geopandas", "mapping", "python"]
excerpt: ""
draft: false
---

I find the [geopandas](http://geopandas.org/) library to be really useful for mapping with layers.
[Contextily](https://github.com/darribas/contextily) is also a nice library that allows adding a background basemap.
Using them together makes it fairly simple to visualize shapes such as polygons and points, together with contextual mapping information, such as in the following figure:
![](/media/2019/04/distrito-300x298.png)
Basemaps are drawn from OpenStreetMap under CC BY SA and map tiles are from Stamen Design, under CC BY 3.0. There are some  options for tile design.
https://gist.github.com/rpasquini/395ecc6e5fafb1b6da2395f174dbda14
If embedded notebook does not render try [here](https://nbviewer.jupyter.org/gist/rpasquini/395ecc6e5fafb1b6da2395f174dbda14)
