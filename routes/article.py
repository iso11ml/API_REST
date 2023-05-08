from ast import List
import datetime
import json
from fastapi import APIRouter, HTTPException
from bson import ObjectId, json_util
from data_base.mongoDB import MongoDBConnection
from schemas.article import articlesEntity, articlesEntity
from models.article import  Articles
from fastapi import HTTPException

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
        return {"likeStatus": 1}  # Devuelve 1 si el usuario dio like
    else:
        db.Articulos.update_one(
            {"_id": ObjectId(article_id)},
            {"$pull": {"likesUserID": user_id}}
        )
        return {"likeStatus": 0}

@articlesRouter.get("/getAllArticles")
async def get_articles():
    articles = []
    for article in db.Articulos.find():
        article_dict = article.copy()
        article_dict['idObject'] = str(article_dict.pop('_id'))
        articles.append(Articles(**article_dict))
    return {"articles": articles}


 #Elimina un artículo mediante el id
@articlesRouter.delete("/deleteArticle/{article_id}")
async def delete_article(article_id: str):
    result = db.Articulos.delete_one({"_id": ObjectId(article_id)})
    if result.deleted_count == 1:
        return {"message": f"Article with ID {article_id} deleted successfully."}
    else:
        raise HTTPException(status_code=404, detail="Article not found.")
    
# Cuenta el número de artículos personales
@articlesRouter.get("/countArticles/{user_id}")
async def count_articles(user_id: str):
    count = db.Articulos.count_documents({"user_id": user_id})
    return {"count": count}