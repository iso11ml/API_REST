from pydantic import BaseModel
from typing import Optional
import datetime

class Comment(BaseModel):
    user_id: str
    content: str
    timestamp: Optional[str] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")