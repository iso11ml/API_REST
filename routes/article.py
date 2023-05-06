from ast import List
import datetime
import json
from fastapi import APIRouter, HTTPException
from bson import ObjectId, json_util
from data_base.mongoDB import MongoDBConnection
from schemas.article import articlesEntity, articlesEntity
from models.article import  Articles

articlesRouter  = APIRouter()
connection = MongoDBConnection.getInstance()
db = connection.get_database()

# Crea un nuevo artículo
@articlesRouter.post("/newArticle")
async def createArticle(article: Articles):
    new_article = dict(article)
    new_article["likesUserID"] = []
    new_article["date"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
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
    

    
# Me gusta en los articulos
from fastapi import HTTPException

@articlesRouter.post("/likeArticle/{article_id}/{user_id}")
async def likeArticle(article_id: str, user_id: str):
    article = db.Articulos.find_one({"_id": ObjectId(article_id)})
    
    if not article:
        raise HTTPException(status_code=404, detail="Artículo no encontrado")

    if user_id not in article["likesUserID"]:
        db.Articulos.update_one(
            {"_id": ObjectId(article_id)},
            {"$push": {"likesUserID": user_id}}
        )
    else:
        db.Articulos.update_one(
            {"_id": ObjectId(article_id)},
            {"$pull": {"likesUserID": user_id}}
        )

    return {"message": "Like actualizado"}

# Obtiene todos los articulos
# @articlesRouter.get("/getAllArticles")
# async def get_articles():
#     articles = []
#     for article in db.Articulos.find():
#         articles.append(Articles(**article))
#     return {"articles": articles}
@articlesRouter.get("/getAllArticles")
async def get_articles():
    articles = []
    for article in db.Articulos.find():
        article_dict = article.copy()
        article_dict['idObject'] = str(article_dict.pop('_id'))
        articles.append(Articles(**article_dict))
    return {"articles": articles}