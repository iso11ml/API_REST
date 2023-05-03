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
    user_id: ObjectId

    @validator('user_id', pre=True)
    def user_id_to_str(cls, v):
        return str(v)

    @validator('user_id')
    def user_id_is_valid(cls, v):
        if not isinstance(v, ObjectId):
            raise ValueError('user_id debe ser un ObjectId válido')
        return v