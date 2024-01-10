# **Presentación del proyecto**

El presente se realiza bajo el marco de Proyectos Individuales del tramo final de la carrera de Data Science de **"Henry"**.
https://www.soyhenry.com/carrera-data-science

Se proporcionó un conjunto de datos relacionados con videojuegos de la plataforma Steam, los cuales fueron procesados y analizados para, posteriormente, desarrollar funciones de consulta que se implementaron en un [servicio FastAPI-Render](https://pi-mlops-mtsspk.onrender.com/docs).

El trabajo final se puede encontrar en [mi repositorio de GitHub](https://github.com/mtsspk/PI_MLOps_mtsspk.git), donde se encontrarán los notebook con todo el detalle de los procesos.


## [**Datasets iniciales**](https://drive.google.com/drive/folders/1HqBG2-sUkz_R3h1dZU5F2uAzpRn7BSpj)

En el link provisto se puede acceder a los archivos brindados para el desarrollo del proyecto.
Se pueden encontrar archivos compromidos que contiene cada uno un archivo .json:

- **output_steam_games.json**: contiene información vinculada a los juegos. 

- **australian_user_reviews.json**: contiene información vinculada a reseñas de usuarios.  

- **australian_users_items.json**: contiene información vinculada a los juegos de cada usuario. 

Por otro lado se presenta un **diccionario de datos** con detalles sobre cada dataset y sus campos.



## Etapas del proyecto

Se desarrollaron tareas de:
- **ETL**: Extracción, Transformación y Carga de los datos.
Los archivos .json provistos contenian datos anidados, con lo cual las primeras tareas estuvieron vinculadas a desanidar campos que contenian listas y/o diccionarios, generando así campos nuevos y desplegando la información contenida en los anidados.
Se realizó una limpieza de datos (nulos, duplicados), transformaciones para poder procesar consultas y se determinaron los campos relevantes a los efectos de los objetivos propouestos para el proyecto.
De esta forma se obtuvieron datasets depurados con la información necesaria lista para ser analizada.
Por otro lado, a la par del ETL se realizó un trabajo de **análisis de sentimientos** creando un nuevo campo en el dataset de reseñas. Si bien este paso no se considera como parte de un proceso de ETL, a efectos prácticos se resolvió incluirlo en **1.2. ETL reviews**.
Con esos dataset depurados luego se realiza un nuevo proceso de ETL generando nuevos dataset orientados específicamente a responder a los objetivos del proyecto.
- **EDA**: Análisis Exploratorio de Datos.
Se obsevó la distribución de distintos valores aplicando distintos tipos de filtros y relaciones entre campos.
Por ejemplo: juegos por género o por año de lanzamiento, juegos por desarrollador, reseñas por año, horas jugadas por usuario, etc..
Se identificaron inconsistencias en ciertos datos que fueron corregidas mediante estrategias varias, como eliminación o imputación de otros valores.
- **MLOps**: Machine Learning Operations.
Se trabajó sobre modelos de recomendación de juegos (item-item) y de usuarios-item. 
A partir de la información procesada se aplicaron modelos para trazar similitudes entre usuarios y entre juegos, de forma tal de poder realizar recomendaciones acorde a las preferencias.
- **Deploy**: implementación del servicio FastAPI-Render.



Para seguir el flujo de trabajo se pueden encontrar los notebooks específicos de cada etapa:

- [1.1. ETL games](https://github.com/mtsspk/PI_MLOps_mtsspk/blob/main/1.1.%20ETL%20games.ipynb): 

- [1.2. ETL reviews](https://github.com/mtsspk/PI_MLOps_mtsspk/blob/main/1.2.%20ETL%20reviews.ipynb)
    
- [1.3. ETL items](https://github.com/mtsspk/PI_MLOps_mtsspk/blob/main/1.3.%20ETL%20items.ipynb)

- [2.1. EDA items](https://github.com/mtsspk/PI_MLOps_mtsspk/blob/main/2.1.%20EDA%20games.ipynb)

- [2.2. EDA items](https://github.com/mtsspk/PI_MLOps_mtsspk/blob/main/2.2.%20EDA%20reviews.ipynb)

- [2.3. EDA items](https://github.com/mtsspk/PI_MLOps_mtsspk/blob/main/2.3.%20EDA%20items.ipynb)

- [3. ETL merge](https://github.com/mtsspk/PI_MLOps_mtsspk/blob/main/3.%20ETL%20merge.ipynb)

- [4. Modelo Recomendacion](https://github.com/mtsspk/PI_MLOps_mtsspk/blob/main/4.%20Modelo%20Recomendacion.ipynb)

- [5. api_functions](https://github.com/mtsspk/PI_MLOps_mtsspk/blob/main/5.%20api_functions.ipynb)


El contenido vinculado al **deploy de la API** es:
- [**main.py**](https://github.com/mtsspk/PI_MLOps_mtsspk/blob/main/main.py)
- [**api_functions.py**](https://github.com/mtsspk/PI_MLOps_mtsspk/blob/main/api_functions.py)
- [**requirements.txt**](https://github.com/mtsspk/PI_MLOps_mtsspk/blob/main/requirements.txt)
- [**Carpeta Datasets**](https://github.com/mtsspk/PI_MLOps_mtsspk/tree/main/Datasets)

Por otro lado, se puede encontrar el archivo **my_functions.py** que contiene algunas funciones personalizadas que se utilizaron especialmente para el EDA.


## Objetivos del proyecto

Se mencionó que el objetivo general tiene que ver con utilizar la información provista para responder distintas consultas en una API.
Las funciones solicitadas son:

+ def **PlayTimeGenre( *`genero` : str* )**: Debe devolver `año` con mas horas jugadas para dicho género.

+ def **UserForGenre( *`genero` : str* )**: Debe devolver el usuario que acumula más horas jugadas para el género dado y una lista de la acumulación de horas jugadas por año.

+ def **UsersRecommend( *`año` : int* )**: Devuelve el top 3 de juegos MÁS recomendados por usuarios para el año dado. (reviews.recommend = True y comentarios positivos/neutrales).
  
+ def **UsersWorstDeveloper( *`año` : int* )**: Devuelve el top 3 de desarrolladoras con juegos MENOS recomendados por usuarios para el año dado. (reviews.recommend = False y comentarios negativos).
  
+ def **sentiment_analysis( *`empresa desarrolladora` : str* )**: Según la empresa desarrolladora, se devuelve un diccionario con el nombre de la desarrolladora como llave y una lista con la cantidad total de registros de reseñas de usuarios que se encuentren categorizados con un análisis de sentimiento como valor. 

+ def **recomendacion_juego( *`id de producto`* )**: Ingresando el id de producto, deberíamos recibir una lista con 5 juegos recomendados similares al ingresado.

+ def **recomendacion_usuario( *`id de usuario`* )**: Ingresando el id de un usuario, deberíamos recibir una lista con 5 juegos recomendados para dicho usuario.

Para ejecutar las últimas 3 funciones (**sentiment_analysis**, **recomendacion_juego** y **recomendacion_usuario**) se implementaron distintos procesos vinculados a `Feauture Engineering` y `Machine Learning`.

## **Análisis de sentimientos**
Para esta función se realizó en primer medida un proceso de **Feature Engineering** sobre el dataset de reseñas (*user_reviews*), creando la columna ***'sentiment_analysis'*** a partir de un análisis de sentimiento con NLP con la siguiente escala: 
- Valor '0' si es negativo.
- Valor '1' si es neutral.
- Valor '2' si es positivo. 
Para los datos donde no fue posible este análisis por estar ausente la reseña escrita se toma el valor de `1`.
Para este punto se utilizó la **biblioteca VADER** (Valence Aware Dictionary and sEntiment Reasoner), específicamente la clase **SentimentIntensityAnalyzer**.


## **Modelos de Recomendación**
Para el desarrollo de los modelos de recomendacion item-item y usuario-item se utilizó la función de similaridad del coseno, de la **biblioteca Scikit-learn**.

### IMPORTANTE: 
En este punto del trabajo se realizó una reducción muy significativa de los registros a utilizar dado que los dataset resultantes para generar las recomendaciones no tenían un peso apropiado para el deploy de la API en Render.

Es por ello que al ejecutar consultas con algunos de los datos existentes se observan devoluciones con errores.

### Criterios para la reducción de datos

Se aplicaron filtros varios para obtener una muestra representativa y adecuada en el deploy.

Además de tomar valores vinculador a las recomendaciones de juegos propiamente dichas, se utilizó el tiempo de juego como un criterio de filtro, entendiendo que los item con más horas de juego serían buenas recomendaciones. 
Habiendo filtrado juegos con más recomendaciones negativas que positivas, luego se aplicó un nuevo filtro tomando el 15% superior por tiempo de juego.