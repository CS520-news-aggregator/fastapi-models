from typing import List, Dict
import uuid
from pydantic import BaseModel, Field


class UserRecommendationQuery(BaseModel):
    user_id: str


class UserRecommendation(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), alias="_id")
    post_scores: List[str, float]
    date: str
