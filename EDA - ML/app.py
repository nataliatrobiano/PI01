import gradio as gr
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.decomposition import PCA

# cargar el archivo
df = pd.read_parquet("dfCodificado.parquet")

# Seleccionar las características para entrenar el modelo
cluster_features = ["listed_in_encoded", "rating_y"]
# Reducir la dimensionalidad del conjunto de datos
pca = PCA(n_components=2)
pandas_df_pca = pca.fit_transform(df[cluster_features])
# Escalar los datos
scaler = MinMaxScaler()
cluster_transformer = ColumnTransformer(transformers=[('num', scaler, cluster_features)])

# Entrenar el modelo K-means
kmeans = KMeans(n_clusters=3, random_state=0)
cluster_pipeline = Pipeline(steps=[('preprocessor', cluster_transformer), ('kmeans', kmeans)])
cluster_pipeline.fit(df)

# Agregar una columna 'cluster' al DataFrame original
df['cluster'] = kmeans.predict(pandas_df_pca)

def recommend_movies(movie):
    num_recommendations = 2
    # Filtrar la información de la película ingresada por el usuario
    input_movie_data = df[df['title'] == movie]
    
    # Predecir el cluster de la película ingresada por el usuario
    input_movie_cluster = cluster_pipeline.predict(input_movie_data)
    
    # Filtrar las películas que pertenecen al mismo cluster que la película ingresada por el usuario
    recommendations = df[df['cluster'] == input_movie_cluster[0]]
    
    # Ordenar las películas por puntaje descendente
    recommendations = recommendations.sort_values('rating_y', ascending=False)
    
       
    # Convertir la lista de títulos de películas en una cadena de texto separada por comas
    recommendations_str = ", ".join(recommendations["title"].tolist())
    
    # Devolver la lista de películas recomendadas, a partir del segundo elemento
    return ", ".join(recommendations["title"].iloc[1:num_recommendations+1].tolist())

iface = gr.Interface(fn=recommend_movies, inputs=gr.inputs.Textbox(label="Ingrese una película"), outputs=gr.outputs.Label(num_top_classes=2, label="Películas recomendadas"))
iface.launch()
