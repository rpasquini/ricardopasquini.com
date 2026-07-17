---
title: "Reshape of lat and lon coordinates in MongoDB, using the aggregate pipeline"
date: "2020-01-21"
slug: "reshape-of-lat-and-lon-coordinates-in-mongodb-using-the-aggregate-pipeline"
lang: "es"
categories: ["Coding Notes", "Uncategorized"]
tags: ["aggregation pipeline", "data reshape", "MongoDB", "scalability"]
excerpt: ""
draft: false
---

# Reshape of lat and lon coordinates in MongoDB, using the aggregate pipeline

## Summary

To transform a large number of documents in a MongoDB collection with spatial data, for example:

`{lat: -58.1, lon: -34.2}`

to a GeoJson format, recognizable by [MongoDB spatial analysis functions](https://docs.mongodb.com/manual/geospatial-queries/), for example:

`{type: ”Point”, location: [- 58.1, -34.2]}`

It seems advisable to use the aggregation framework:

`db.tweets.aggregate ([{$project: {location: {type: "Point", coordinates: ["$lon", "$lat"]}}}, $ out: {$out: "newcollectionname"}] );`

## The problem

An usual task in the database in MongoDB may be to prepare the data for spatial tasks.

As I described in the previous post, it is necessary to have the data in the compatible format, in this case as a [GeoJson](https://docs.mongodb.com/manual/reference/geojson/). For example, if we are working with points:

`{type: ”Point”, location: [- 58.1, -34.2]}
{type: ”Point”, location: [- 58.1, -34.2]}`

That is, specifying a "type" key that specifies that it is a point, and then a "location" key with an array of the coordinates pair: longitude and latitude (in that order!)

If working with polygons:

```
{type: "Polygon", coordinates: [[[0, 0], [3, 6], [6, 1], [0, 0]]]}
```

The problem with my data is that it was in the following format and I needed to do a reshape. It was necessary an efficient procedure because the collection contained millions of records. Here is an example of one of my documents

`{'_id': ObjectId ('5e10e1dd6e7ccd7b44ea9a57'),
'id': 416118213328388097,
'u_id': 999999999,
'lat': -34.6449231,
'lon': -58.56565656,
'created_at': 1388045287000,
'type': 'll',
'place_type': nan,
'u_created_at': 1388012017000,
'u_followers_count': 31,
'u_location': 'BBM: 7982CCD9',
'u_lang': 'is',
'u_statuses_count': 243,
'u_name': 'Hidden1',
'u_screen_name': 'Hidden2',
'u_description': 'Nothingnothing',
'urls': nan,
'text': 'Vamooo'}`

That is, in addition to the reshape of lat and lon, there is a lot of data that I want to keep.

I initially tried a straightforward approach, that **did not work**. Resulted to be very slow and with errors. I iterated over the documents in the collection calling for an **update**. Here is an example update using **pymongo**:

```
def reshapelocation (db, doc):
    
    "document reshape function"
    "" "
    : param db: passing mongodb connection
    : param doc: document
    
    "" "
    query = {'u_id': doc ['u_id']}
    newvalues = {'$set': {'location': {'type': "Point", 'coordinates': [user ['lon'], user ['lat']]}}}
    db.tweets.update (query, newvalues, upsert = True)

#calling all documents
cursor = db.tweets.find ()

#iteration
for doc in cursor:
    updatetweetlocation (db, doc)
```

## The solution

The way that **did work** was using the [mongo aggregation pipeline](https://docs.mongodb.com/manual/core/aggregation-pipeline/).

The aggregation pipeline, as the name implies, allows several operations to be included as part of pipeline, defined in the form of a list. At the moment I will only specify one task, which is $project. With this function we can specify the new structure of each document:

```
db.mycoleccion.aggregate ([$project:: {type: "Point", {location: [$lon, $lat]}}])
```

Note that $lon and $lat here refer to the variables of the document I am modifying. type and location are the names of the new keys.

What is missing in this specification is to say what to do with all the other keys, which by default will not be taken into account. To keep the rest of the keys I will specify them indicating with a value 1 that they must be copied.

```
db.mycollection.aggregate ([{$ project: {id: 1, u_id: 1, created_at: 1, type: 1, u_created_at: 1, u_followers_count: 1, u_location: 1, u_lang: 1, u_statuses_count: 1, u_name: 1, u_screen_name: 1, u_description: 1, text: 1, location: {type: "Point", coordinates: ["$ lon", "$ lat"]}}}]);
```

By default the aggregation is a reading of the base, it does not make any modification. That is, the last thing to have is to specify that the result of the aggregation must be a new collection.

I do this as part of the pipeline, (adding to the list!) Specifying the $out function: {$out: "tweets2"}

```
db.mycollection.aggregate ([{$project: {id: 1, u_id: 1, created_at: 1, type: 1, u_created_at: 1, u_followers_count: 1, u_location: 1, u_lang: 1, u_statuses_count: 1, u_name: 1, u_screen_name: 1, u_description: 1, text: 1, location: {type: "Point", coordinates: ["$lon", "$lat"]}}}, {$out: "mynewcollection" ]);
```
