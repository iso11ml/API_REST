import datetime
import json
from fastapi import APIRouter, HTTPException
from bson import ObjectId, json_util
from data_base.mongoDB import MongoDBConnection
from schemas.article import articlesEntity, articlesEntity
from models.article import Articles, Comment

commentRouter  = APIRouter()
connection = MongoDBConnection.getInstance()
db = connection.get_database()

@commentRouter.post("/addComment/{article_id}")
async def add_comment(article_id: str, comment: Comment):
    article = db.Articulos.find_one({"_id": ObjectId(article_id)})
    if not article:
        raise HTTPException(status_code=404, detail="Artículo no encontrado")

    db.Articulos.update_one(
        {"_id": ObjectId(article_id)},
        {"$push": {"comments": comment.dict()}}
    )
    return {"message": "Comentario añadido"}
