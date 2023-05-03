import json
from fastapi import APIRouter
from bson import ObjectId, json_util
from data_base.mongoDB import MongoDBConnection
from schemas.article import articlesEntity, articlesEntity
from models.article import Articles

articlesRouter  = APIRouter()
connection = MongoDBConnection.getInstance()
db = connection.get_database()

# @articlesRouter.post("/newArticle")
# async def createUser(article: Articles):
#     new_article = dict(article)
#     result = db.Article.insert_one(new_article)
#     return str(result.inserted_id)

@articlesRouter.post("/newArticle", response_model=Articles)
async def createUser(article: Articles):
    new_article = dict(article)
    result = db.Article.insert_one(new_article)
    return json.loads(json_util.dumps(new_article))