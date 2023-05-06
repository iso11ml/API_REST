from pydantic import BaseModel
from typing import Optional
import datetime

class Comment(BaseModel):
    user_id: Optional[str]
    description: str
    timestamp: Optional[str] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")