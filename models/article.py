from typing import Optional
from bson import ObjectId
from pydantic import BaseModel, validator

# class Article(BaseModel):
#     title: str
#     description: str
#     date: str
#     user_id: ObjectId

class Articles(BaseModel):
    title: str
    description: str
    date: str
    user_id: str