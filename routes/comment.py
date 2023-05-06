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
async def add_comment(article_id: str, comment: Comment, email: str):
    article = db.Articulos.find_one({"_id": ObjectId(article_id)})
    if not article:
        raise HTTPException(status_code=404, detail="Artículo no encontrado")
    user = db.Usuario.find_one({"email": email})
    print(user)
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    user_id = str(user["_id"])
    comment_data = comment.dict()
    comment_data["user_id"] = user_id

    db.Articulos.update_one(
        {"_id": ObjectId(article_id)},
        {"$push": {"comments": comment_data}}
    )
    return {"message": "Comentario añadido"}