---
title: "Instalacion y consultas a Google Big Query desde Jupyter"
date: "2019-11-01"
slug: "instalacion-y-consultas-a-google-big-query-desde-jupyter"
lang: "es"
categories: ["Coding Notes", "Uncategorized"]
tags: ["Coding", "Conda Environments", "Google Big Query", "Jupyter", "Properati", "pymongo", "python"]
excerpt: ""
draft: false
---

Instalacion y consultas a Google Big Query desde Jupyter


# Instalación y consultas a Google Big Query desde Jupyter

Algunas notas para hacer un pedido a google big query. En este caso el objetivo es consultar la base de datos de **Properati**, y llevarla a un pandas. Agrego al final unos ultimos pasos para persistir la data en un mongo local.

## Instalación Google Cloud

1. Voy a crear un ambiente virtual especifico usando conda. En este caso le agrego python 3.6. Le llamo bigquery

```
```
xxxxxxxxxx
```



```
conda create -n bigquery python=3.6
```
```

2. Activar el ambiente

   ```
   ```
   xxxxxxxxxx
   ```



   ```
   C:\Users\Richard>activate bigquery
   ```
   ```

Dentro del ambiente puedo entrar a python, y voy a chequear desde donde python se esta ejecutando

```
```
xxxxxxxxxx
```



```
(bigquery) C:\Users\Richard>python
```



```
​
```



```
​
```



```
Python 3.6.7 (default, Jul  2 2019, 02:21:41) [MSC v.1900 64 bit (AMD64)] on win32Type "help", "copyright", "credits" or "license" for more information.
```



```
​
```



```
>>> import sys
```



```
\>>> sys.executable'C:\\Users\\Richard\\AppData\\Local\\conda\\conda\\envs\\bigquery\\python.exe'>>> exit()
```
```

3. El siguiente paso es instalar google-cloud en el ambiente. Lo instalo tambien desde conda. Lo siguiente no va a funcionar:

```
```
xxxxxxxxxx
```



```
   (bigquery) C:\Users\Richard>conda install google-cloud
```



```
   Solving environment: failed
```



```
   PackagesNotFoundError: The following packages are not available from current channels:
```



```
     \- google-cloud
```
```

La forma correcta es especificando conda-forge:

```
```
xxxxxxxxxx
```



```
   (bigquery) C:\Users\Richard>conda install -c conda-forge google-cloud-bigquery
```



```
   Solving environment: done
```
```

Ahora sí levanta bien google cloud en python:

```
```
xxxxxxxxxx
```



```
   Python 3.6.7 (default, Jul  2 2019, 02:21:41) [MSC v.1900 64 bit (AMD64)] on win32Type "help", "copyright", "credits" or "license" for more information.
```



```
   >>> import google.cloud
```



```
   >>> exit()  
```
```

4. Ahora voy a armar el ipykernel para poder levantar este ambiente desde jupyter. Instalo primero ipykernel en el ambiente con conda. El siguiente comando ejecuta el ipykernel llamando al python del ambiente sobre el que estamos trabajando

   (bigquery) C:\Users\Richard>conda install ipykernel

   Solving environment: done

   (bigquery) C:\Users\Richard>python -m ipykernel install --user --name bigquery --display-name "Python 36 (bigquery)"

   Installed kernelspec bigquery in C:\Users\Richard\AppData\Roaming\jupyter\kernels\bigquery
5. Levanto jupyter 
   (bigquery) C:\Users\Richard>jupyter notebook

## Configurando la conexion

Ir a la pagina de google que permite crear credenciales de autentificacion

<https://cloud.google.com/docs/authentication/getting-started?hl=es-419>

![1572618642641](C:\Users\Richard\AppData\Roaming\Typora\typora-user-images\1572618642641.png)

## Ejecutando el query

Desde jupyter

```
```
xxxxxxxxxx
```



```
import os, inspect
```



```
from google.cloud import bigquery
```



```
from google.oauth2 import service_account
```



```
​
```
```

```
```
xxxxxxxxxx
```



```
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
```



```
credentials = service_account.Credentials.from_service_account_file(
```



```
    currentdir+'\credentialsbigquery\miclave.json')
```
```

```
```
xxxxxxxxxx
```



```
project_id = 'dataproperati2019'
```



```
client = bigquery.Client(credentials= credentials,project=project_id)
```



```
​
```



```
​
```



```
# Preparando el query.
```



```
QUERY = (
```



```
'SELECT * FROM `properati-dw.public.ads` WHERE start_date >= "2016-01-01" AND start_date <= "2016-12-31" AND type = "Propiedad" AND country = "Argentina" '
```



```
'AND place.l1 = "Argentina" '
```



```
'AND property.type = "Departamento" '
```



```
'AND property.operation = "Alquiler" '
```



```
'AND property.surface_total > 0 '
```



```
'AND property.surface_covered > 0 '
```



```
'AND property.price > 0 '
```



```
'AND (place.l2="Capital Federal" or place.l2="Buenos Aires Interior" or place.l2="Bs.As. G.B.A. Zona Sur" or place.l2="Bs.As. G.B.A. Zona Norte" or place.l2="Bs.As. G.B.A. Zona Oeste") '
```



```
)
```



```
​
```



```
query_job = client.query(QUERY)  # API request
```



```
rows = query_job.result()  # Waits for query to finish
```



```
​
```



```
#for row in rows:
```



```
#    print(row.start_date, row.country)
```
```

## Hacer el pedido y llevarlo a un dataframe

```
```
xxxxxxxxxx
```



```
# voy a necesitarlo para manipular el dataframe
```



```
import pandas as pd
```
```

```
```
xxxxxxxxxx
```



```
# hago el query. Esto no va a funcionar si no tengo pandas instalado
```



```
df=client.query(QUERY).to_dataframe()
```
```

```
```
xxxxxxxxxx
```



```
#Ya está. Chequeo que las columnas en el dataframe:
```



```
df.columns
```
```

```
```
xxxxxxxxxx
```



```
Index(['type', 'type_i18n', 'country', 'id', 'start_date', 'end_date',
```



```
       'created_on', 'place', 'property', 'development'],
```



```
      dtype='object')
```
```

## Llevando la data a mongodb

```
```
x
```



```
# Voy a necesitar resolver el problema de que pymongo no entiende el formato datetime.date
```



```
df2=df.copy()
```



```
df2.start_date=pd.to_datetime(df.start_date)
```



```
df2.end_date=pd.to_datetime(df.end_date, errors = 'coerce') # convierto a nulos los que no se corresponden con fecha verdadera
```



```
df2.created_on=pd.to_datetime(df.created_on)
```



```
df2=df2[~pd.isnull(df2.end_date)] # me quedo solo con los registros no nulos )
```
```

```
```
xxxxxxxxxx
```



```
dfdictionary=df2.to_dict('records') #dataframe a json
```
```

```
```
xxxxxxxxxx
```



```
import pymongo
```



```
client = pymongo.MongoClient('localhost', 27017)
```



```
db = client["properati"]  #vivienda is the name of the db
```



```
db.raw.insert_many(dfdictionary)
```
```

Listo:

```
```
xxxxxxxxxx
```



```
<pymongo.results.InsertManyResult at 0x258dc1c3f88>
```
```
