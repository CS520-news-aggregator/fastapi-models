from typing import List
import uuid
from pydantic import BaseModel, Field


class Post(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    source_ids: List[str]
    topics: List[str]

    summary: str = ""

    upvotes: int = 0
    downvotes: int = 0

    class Config:
        populate_by_name = True
        json_schema_extra = {
            "example": {"source_ids": ["sample"], "topics": ["sample"]}
        }


class Comment(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    content: str
    post_id: str

    upvotes: int = 0
    downvotes: int = 0

    class Config:
        populate_by_name = True
        json_schema_extra = {
            "example": {
                "content": "sample",
                "post_id": "sample",
            }
        }
