import pandas as pd
import numpy as np


# Cargar el archivo CSV en un DataFrame
df_play_gnr = pd.read_csv('Datasets/df_play_gnr.csv')

# Cargar el archivo CSV en un DataFrame
df_usr_gnr_top = pd.read_csv('Datasets/df_usr_gnr_top.csv')

# Cargar el archivo CSV en un DataFrame
df_usr_gnr_top_year = pd.read_csv('Datasets/df_usr_gnr_top_year.csv')

# Cargar el archivo CSV en un DataFrame
df_games_rec_top_3 = pd.read_csv('Datasets/df_games_rec_top_3.csv')

# Cargar el archivo CSV en un DataFrame
df_dev_rec_worst_3 = pd.read_csv('Datasets/df_dev_rec_worst_3.csv')

# Cargar el archivo CSV en un DataFrame
df_dev_sent = pd.read_csv('Datasets/df_dev_sent.csv')

# Cargar el archivo Parquet en un DataFrame
df_games_similarity = pd.read_parquet('Datasets/df_games_similarity.parquet')

# Cargar el archivo CSV en un DataFrame
df_games_names = pd.read_csv('Datasets/df_games_names.csv')

# Convertir el campo 'game_id' a tipo string
df_games_names['game_id'] = df_games_names['game_id'].astype(str)

# Cargar el archivo Parquet en un DataFrame
df_user_similarity = pd.read_parquet('Datasets/df_user_similarity.parquet')

# Cargar el archivo Parquet en un DataFrame
df_usr_data = pd.read_parquet('Datasets/df_usr_data.parquet')



def PlayTimeGenre(genre: str):
    # Filtrar el DataFrame por el género proporcionado
    genre_data = df_play_gnr[df_play_gnr['genre'] == genre]

    if not genre_data.empty:
        # Encontrar el release_year con el mayor playtime
        max_playtime_row = genre_data.loc[genre_data['playtime'].idxmax()]
        max_release_year = max_playtime_row['release_year']
        max_playtime = max_playtime_row['playtime']

        return f"Para el género {genre}, el release_year con mayor playtime es {max_release_year} con un total de playtime de {max_playtime}."
    else:
        return f"No hay datos disponibles para el género {genre}."
    


def UserForGenre(genre: str):
    # Filtrar df_usr_gnr_top por el género proporcionado
    genre_data_top = df_usr_gnr_top[df_usr_gnr_top['genre'] == genre]

    if not genre_data_top.empty:
        # Encontrar el user_id con mayor playtime_forever para el género
        max_playtime_row = genre_data_top.loc[genre_data_top['playtime_forever'].idxmax()]
        max_user_id = max_playtime_row['user_id']
        max_playtime_forever = int(max_playtime_row['playtime_forever'])  # Convertir a int

        # Filtrar df_usr_gnr_top_year por el user_id y el género
        user_year_data = df_usr_gnr_top_year[(df_usr_gnr_top_year['user_id'] == max_user_id) & (df_usr_gnr_top_year['genre'] == genre)]

        # Preparar resultados
        result = {
            "genre": genre,
            "max_user_id": max_user_id,
            "max_playtime_forever": max_playtime_forever,
            "details": user_year_data[['release_year', 'playtime_forever', 'playtime_acumulated']].astype(int).to_dict(orient='records') if not user_year_data.empty else None
        }

        return result
    else:
        return {"error": f"No hay datos disponibles para el género {genre} en df_usr_gnr_top."}



def UsersRecommend(posted_year):
    # Filtrar df_games_rec_top_3 por el posted_year proporcionado
    year_data = df_games_rec_top_3[df_games_rec_top_3['posted_year'] == posted_year]

    if not year_data.empty:
        # Presentar mensaje
        message = f"Juegos más recomendados para el año {posted_year}:"

        # Mostrar game_id, app_name y total_recommend para el posted_year dado
        result = year_data[['game_id', 'app_name', 'total_recommend']].to_dict(orient='records')

        return {"message": message, "result": result}
    else:
        return {"message": f"No hay datos disponibles para el posted_year {posted_year} en df_games_rec_top_3."}



def UsersWorstDeveloper(posted_year):
    # Filtrar df_dev_rec_worst_3 por el posted_year proporcionado
    year_data = df_dev_rec_worst_3[df_dev_rec_worst_3['posted_year'] == posted_year]

    if not year_data.empty:
        # Presentar mensaje
        message = f"Desarrolladores con más reseñas negativas para el año {posted_year} son:"

        # Mostrar developer y neg_rec para el posted_year dado
        result = year_data[['developer', 'neg_rec']].to_dict(orient='records')

        return {"message": message, "result": result}
    else:
        return {"message": f"No hay datos disponibles para el posted_year {posted_year} en df_dev_rec_worst_3."}



def sentiment_analysis(developer: str):
    # Filtrar registros con al menos un análisis de sentimiento para el desarrollador proporcionado
    df_filtered = df_dev_sent[(df_dev_sent['total_sentiment'] > 0) & (df_dev_sent['developer'] == developer)]

    if not df_filtered.empty:
        # Crear el diccionario con el desarrollador como llave y una lista de sentimientos como valor
        sentiment_dict = {developer: []}

        # Insertar valores de análisis de sentimientos en la lista
        for index, row in df_filtered.iterrows():
            sentiment_values = {
                "Negative": row['negative_sentiment'],
                "Neutral": row['neutral_sentiment'],
                "Positive": row['positive_sentiment']
            }
            sentiment_dict[developer].append(sentiment_values)

        # Presentar el diccionario resultante
        result = {"developer": developer, "sentiments": sentiment_dict[developer]}
    else:
        result = {"message": f"No hay datos disponibles para el desarrollador {developer} en df_dev_sent."}

    return result

    

def recomendacion_juego(game_id:str, num_recommendations=5):

    game_name = df_games_names.loc[df_games_names['game_id'] == game_id, 'app_name'].values[0]

    # Convertir el campo 'game_id' a tipo string
    df_games_names['game_id'] = df_games_names['game_id'].astype(str)

    # Obtener la serie de juegos similares, excluir el game_id introducido 
    similar_games = df_games_similarity.drop(game_id).loc[:, game_id].sort_values(ascending=False)

    # Tomar las primeras num_recommendations recomendaciones
    recommendations = similar_games.head(num_recommendations).index.tolist()

    recommended_games = df_games_names.loc[df_games_names['game_id'].isin(recommendations), ['game_id', 'app_name']].reset_index(drop=True)

    recommended_games = recommended_games[['game_id', 'app_name']].to_dict(orient='records')

    message = f"Juegos similares a {game_name} (game_id {game_id}):"

    result = f"{message}", recommended_games
    
    return result



def recomendacion_usuario(user_id: str, num_recommendations = 5):
    # Filtrar df_usr_data por el user_id específico
    user_games = df_usr_data[df_usr_data['user_id'] == user_id]

    # Crear la lista user_games a partir de los valores de df_usr_data
    user_games = user_games['game_id'].tolist()

    # Obtener la serie de usuarios similares, excluir el game_id introducido 
    similar_users = df_user_similarity.drop(user_id).loc[:, user_id].sort_values(ascending=False).index.tolist()

    # Crear DataFrame con similar_users
    df_similar_users = pd.DataFrame({'user_id': similar_users})

    # Realizar la concatenación con df_usr_selection usando el método merge
    df_concatenado = pd.merge(df_similar_users, df_usr_data, on='user_id', how='inner')

    # Filtrar las filas donde el game_id no está en user_games
    df_concatenado = df_concatenado[~df_concatenado['game_id'].isin(user_games)]

    # Utilizar merge para concatenar basándote en la columna game_id
    df_final = pd.merge(df_concatenado, df_games_names, on='game_id', how='inner')

    # Eliminar duplicados y quedarse con el primer registro
    df_final_sin_duplicados = df_final.drop_duplicates(subset='game_id', keep='first').head(num_recommendations) 
        
    recommended_games = df_final_sin_duplicados[['game_id', 'app_name', 'user_id']].to_dict(orient='records')
 
    message = f"A usuarios similares a {user_id} les gustó:"
    
    #result = message, recommended_games
    result = f"{message}", recommended_games
    
    return result