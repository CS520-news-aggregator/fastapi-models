from typing import List
import uuid
from pydantic import Field, BaseModel


class Prompt(BaseModel):
    prompt: str
    query: str


class Response(BaseModel):
    response: str


class PostQuery(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    post_id: str
    text: str


class PostsAnalysis(BaseModel):
    post_queries: List[PostQuery]


class PostCompletion(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    title: str = Field(description="title of the news event")
    summary: str = Field(description="summary of the news event")


class PostAnalysis(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    post_id: str
    completion: PostCompletion
