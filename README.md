#  <h1 align="center">**Proyecto Individual N°1** 
***
![imagen](.\img\logo.jpeg)


### <h2 align="center"> *¡Bienvenidos a mi primer proyecto individual de la etapa de labs!* 
En esta ocasión, les mostraré un trabajo realizado situandome en el rol de una Data engineering y Data science.
En primer lugar, realice transformaciones específicas en los datos (ETL) para disponibilizarlos a través de endpoints accesibles mediante la API que fue desplegada en Deta Space.
En segundo lugar, realice un proceso de EDA a los datos para armar un sistema de recomendacion de peliculas con machine learning, usando un filto basado en contenido. 

***
## <h2 align="center"> **Evaluación del cumplimiento de los objetivos**

Se ha completado los siguientes objetivos:

 >Transformaciones en las bases de datos: Archivo ETL.ipynb

 >Desarrollo de la API Deployada: [link](https://pi_tn-4-f1122587.deta.app/docs ) 

 >Proceso de EDA y machine learning: Archivo EDA.ipynb

 >Sistema de recomendacion: [link](http://127.0.0.1:7860/)  (se accede de manera local)

 >Video:[link](https://youtu.be/CPh-ybqDMWI) 


***
## <h2 align="center"> **Endpoints de la API**

### *La API cuenta con los siguientes endpoints:*


**Funcion get_max_duration** : Busca la película con mayor duración con filtros de año, plataforma y tipo de duración. 

Para utilizarla deben indicar: 

*Año*: solo acepta numeros enteros.

*Plataforma*: Cuatro opciones se escriben todo en minúscula (amazon, disney, hulu, netflix)

*Tipo de duración*: Dos opciones se escriben en minúscula (min, season)




**Función get_score_count**: Busca y cuenta la cantidad de películas por plataforma con un puntaje mayor a XX en determinado año.

Para utilizarla deben indicar: 

*Año*: Solo acepta numeros enteros.

*Plataforma*: Cuatro opciones se escriben todo en minúscula (amazon, disney, hulu, netflix)

*Puntaje*: Acepta numeros enteros y con coma.




**Función get_count_platform**: Busca y cuenta la cantidad de películas por plataforma. 

Para utilizarla deben indicar: 

*Plataforma*: Cuatro opciones se escriben todo en minúscula (amazon, disney, hulu, netflix)




**Función get_actor**: Busca al actor que más se repite según plataforma y año. 

Para utilizarla deben indicar: 

*Año*: Solo acepta numeros enteros.

*Plataforma*: Cuatro opciones se escriben todo en minúscula (amazon, disney, hulu, netflix)

***
##  <h2 align="center"> **Deployment**

Para realizar el deploy de esta aplicación se utilizó Deta Space.
 
 Nombre de la aplicación: PI_TN
 
 Nombre de usuario:nataliatr1250

### *Requisitos previos:*

Servidor con sistema operativo Windows que tenga instalado PowerShell y/o Git Bash

Tener instalado Python (version mayor a 3.9) y pip 22.3.1



### *Instrucciones detalladas para ingresar en la API:*

1-Registrarse en Deta Space en este [link](https://deta.space/signup) 

2- Confirmar la cuenta con el email que envian. 

3-Ingresar a su cuenta de Deta Space con su usuario y contraseña.

4- Ingresar al siguiente link [link]( https://pi_tn-4-f1122587.deta.app/__deta_auth?token=eyJraWQiOiJzTjVnTk43cWFGVmpPYVwvc3oyVTJvdnNIMTZyNThQb2RQVFpRZWlBQUhNZz0iLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiI4ODQyODdmYy0wMDBiLTRlMzQtYTg0Yy00MzcxMzIzZGM2YzQiLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAuZXUtY2VudHJhbC0xLmFtYXpvbmF3cy5jb21cL2V1LWNlbnRyYWwtMV9WYUhoMEVvWDUiLCJjbGllbnRfaWQiOiIzMGpnaTM0MzlsbWRnN3V0dGUyN2dkbDlnYSIsIm9yaWdpbl9qdGkiOiJkMGU0ZWU5MC02OWM5LTQyMmMtYTg4Ni05NTE4NmE3MWM4NmQiLCJldmVudF9pZCI6ImY0ODhkYTZjLTU0OGUtNGNhMC04ODhhLTY0MTZkMjRhMjY3ZSIsInRva2VuX3VzZSI6ImFjY2VzcyIsInNjb3BlIjoiYXdzLmNvZ25pdG8uc2lnbmluLnVzZXIuYWRtaW4iLCJhdXRoX3RpbWUiOjE2NzY5MDQxMTcsImV4cCI6MTY3Njk5MDUxNywiaWF0IjoxNjc2OTA0MTE3LCJqdGkiOiIwYjkwNmZhMi1jMDhmLTRlMjktOTQwZi0xMjRiMzc5YmM5NzMiLCJ1c2VybmFtZSI6Im5hdGFsaWF0cjEyNTAifQ.YpgKj9Xnn3GLMtvouhFaEqJtTXjtRTeDEP-P9OzQ1LkAqJPa-qrvnsVODi0LU8ry8GZevYiWB7cO3nt7MANTs4JeuRJqSpp4Ih9Wj1ezRQPuyG7iJXl9UICn9LsOn-g_kY3TiHeikiit13GTycZiq5OvVEAeJTQ8yOOISsJX_VEJ07fzPd5p1ue9aK4KieQZLt569irUEdd0qVQRKJw3CUwSQEzxg364_h_fV29C1GOOmFD4-S1vZ__AHKIZcB3VO6o6vSaJjDX5UcIWCvvRLbI4Ogdt3LHq75lnCzFtiKTej9Md_1eMJZ1wIRi_uHW_XqnI4k0W9JdMoNwTZvzpHw&redirect_uri=https%3A%2F%2Fpi_tn-4-f1122587.deta.app%2F)

5- Les va a aparecer una pantalla negra sin informacion y el link de la pagina va a ser https://pi_tn-4-f1122587.deta.app/ 

6- Deben escribir al final del link **docs**
Te quedará asi: https://pi_tn-4-f1122587.deta.app/docs 

7- Ya pudes realizar las consultas a la API.

***
## <h2 align="center"> **Modelo de Machine Learning**

En este proyecto se realizó un sistema de recomendacion con filtro basado en condenido, teniendo en cuenta la puntuacion de millones de usuarios y el género de las peliculas/series. Ingresando el nombre de una pelicula te recomienda 2 peliculas/series con tematica parecida que podrían gustarte. 

Con respecto a la parte técnica, se realizo la exploracion de los datos y su transformación correspondiente, como la codificacion de las columnas categoricas para un mejor procesamiento del modelo. Se utilizo un algoritmo de k-means de aprendizaje no supervizado, el cual agrupa las peliculas teniendo en cuenta sus caracteristicas comunes y realiza recomendaciones en base a eso. 

### *Instrucciones detalladas para ingresar en la API:*

Se pude acceder de forma local con los siguientes pasos:

1- Descargar este repositorio

2- Abre el archivo *app.py* que se encuentra en la carpeta **EDA-ML**

3- Correlo

4 -En tu consola aparecerá un link como este :http://127.0.0.1:7860/ 

5- Ingresa al link   

6- Allí puedes ingresar el nombre de una pelicula *(todo en minúsculas y en inglés)*
El modelo te recomendará dos peliculas con la misma temática. 


***
##  <h2 align="center"> **Contacto**

Si tiene alguna pregunta o comentario sobre este proyecto, no dude en ponerse en contacto a través de un mensaje directo a mi Linkedin Natalia Trobiano o abriendo un issue en este repositorio.


