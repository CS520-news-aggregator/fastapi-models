from typing import List
import uuid
from pydantic import BaseModel, Field


class Recommendation(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    user_id: str
    post_ids: List[str]
