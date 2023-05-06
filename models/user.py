from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
    idObject: Optional[str]
    name: str
    email: str
    password: str
