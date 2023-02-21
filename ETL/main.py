from fastapi import FastAPI
import numpy as np
import pandas as pd

app = FastAPI() 

@app.get("/get_max_duration")
async def get_max_duration(year: int, platform:str, duration_type: str):
    df = pd.read_parquet("dfcompleto.parquet")
    df = df.dropna() # elimina los valores nulos en el dataframe
    # Filtro por parámetros utilizando la función query()
    if year:
        df = df.query(f"release_year == {year}")
    if platform:
        df = df.query(f"platform == '{platform}'")
    if duration_type:
        if duration_type == "min":
            max_duration = df.query("duration_type == 'min'").duration_int.max()
        elif duration_type == "season":
            max_duration = df.query("duration_type == 'season'").duration_int.max()
        else:
            return {"error": "Invalid duration type"}
    else:
        max_duration = df.duration_int.max()

    # Obtengo el título de la película con duración máxima
    title = df.query(f"duration_int == {max_duration}").title.values[0]
    
    return {"title": title}



# Función película con mayor promedio
@app.get("/get_score_count")
async def get_score_count(platform: str, scored: float, year: int):
    # Esta función cuenta la cantidad de películas que cumplen con los criterios 
    # ingresados en "platform, scored, year" y muestra el total.
    # Recibe los parámetros platform, scored, year (que no son opcionales)

    # Cargo los datos del Dataset final con la variable df
    df = pd.read_parquet("dfcompleto.parquet")

    # Selecciona las películas que cumplen con el criterio de los parámetros
    selec = df.loc[(df['platform'] == platform) & (df['scored'] >= scored) & (df['release_year'] == year)]

    # Cuenta las películas y retorna el resultado
    contar = selec['title'].nunique()

    return contar



#Funcion Cantidad de películas por plataforma con filtro de PLATAFORMA. 
@app.get("/count_platform")
async def get_count_platform(platform: str):
    
    df = pd.read_parquet("dfcompleto.parquet")
    # filtro las películas a la plataforma especificada y cuento los títulos únicos
    cantidad_peliculas = df[df["platform"] == platform]['title'].nunique()
    return cantidad_peliculas





@app.get("/actor")
async def get_actor(platform: str, year: int):
    
    dfcompleto = pd.read_parquet("dfcompleto.parquet")
    
    # Filtrar el DataFrame por plataforma y año
    filtered_df = dfcompleto[(dfcompleto['platform'] == platform) & (dfcompleto['release_year'] == year)]

    # Reemplazar los valores nulos en la columna "cast" por "Desconocido"
    filtered_df['cast'].fillna(value='Desconocido', inplace=True)

    # Obtener la lista de actores
    actors_list = [actor for actors in filtered_df['cast'].str.split(', ') for actor in actors if actor != 'Desconocido']

    # Obtener el actor con más apariciones
    top_actor = max(set(actors_list), key=actors_list.count)

    return top_actor

