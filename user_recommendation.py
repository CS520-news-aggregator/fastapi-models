from typing import List, Tuple
import uuid
from pydantic import BaseModel, Field


class UserRecommendation(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), alias="_id")
    user_id: str
    post_scores: List[Tuple[str, float]]
    date: str
