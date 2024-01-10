import pandas as pd
from fastapi import FastAPI, HTTPException
import pyarrow.parquet as pq
import api_functions
import numpy as np

app = FastAPI()


@app.get("/")
def index():
    return {"Proyecto Steam"}


@app.get("/PlayTimeGenre")
def PlayTimeGenre(genre: str):
    return api_functions.PlayTimeGenre(genre)


@app.get("/UserForGenre")
def UserForGenre(genre: str):
    genre = genre.lower()
    return api_functions.UserForGenre(genre) 


@app.get("/UsersRecommend")
def UsersRecommend(posted_year: int):
    return api_functions.UsersRecommend(posted_year)


@app.get("/UsersWorstDeveloper")
def UsersWorstDeveloper(posted_year: int):
    return api_functions.UsersWorstDeveloper(posted_year) 
    

@app.get("/sentiment_analysis/{developer}")
def sentiment_analysis(developer: str):
    developer = developer.lower()
    return api_functions.sentiment_analysis(developer) 


@app.get("/recomendacion_juego/{game_id}")
def recomendacion_juego(game_id: str, num_recommendations: int = 5):
    game_id = game_id.lower()
    return api_functions.recomendacion_juego(game_id, num_recommendations) 


@app.get("/recomendacion_usuario/{user_id}")
def recomendacion_usuario(user_id: str, num_recommendations: int = 5):
    user_id = user_id.lower()
    return api_functions.recomendacion_usuario(user_id) 