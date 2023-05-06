from ast import List
from typing import Optional, List
from models.comment import Comment
from bson import ObjectId
from pydantic import BaseModel, validator

class Articles(BaseModel):
    title: str
    description: str
    date: Optional[str] = None
    user_id: Optional[str]
    likesUserID: Optional[List[str]]
    comments: Optional[List[Comment]] = []