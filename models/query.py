from pydantic import BaseModel
from typing import Optional

class QueryRequest(BaseModel):
    question: str
    image_base64: Optional[str] = None
