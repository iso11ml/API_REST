import json
from fastapi import APIRouter, HTTPException
from bson import ObjectId, json_util
from data_base.mongoDB import MongoDBConnection
from schemas.article import articlesEntity, articlesEntity
from models.article import Articles

articlesRouter  = APIRouter()
connection = MongoDBConnection.getInstance()
db = connection.get_database()

# Crea un nuevo artículo
@articlesRouter.post("/newArticle")
async def createArticle(article: Articles):
    new_article = dict(article)
    result = db.Articulos.insert_one(new_article)
    return str(result.inserted_id)

# Filtra los datos para mostrar solo los artículos del que los publico
@articlesRouter.get("/myArticles/{user_id}")
async def getMyArticles(user_id: str):
    try:
          articles = db.Articulos.find({"user_id": user_id})
          return articlesEntity(articles)
    except Exception as e:
        return {"message": "Error al obtener los artículos del usuario."}

# Filtra los datos para mostrar solo los artículos de los demás menos los del creador
@articlesRouter.get("/otherArticles/{user_id}")
async def getOtherArticles(user_id: str):
    try:
          articles = db.Articulos.find({"user_id": {"$ne": user_id}})
          return articlesEntity(articles)
    except Exception as e:
        return {"message": "Error al obtener los artículos del usuario."}
