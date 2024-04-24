import uuid
from pydantic import Field, BaseModel


class Prompt(BaseModel):
    prompt: str


class SummaryQuery(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    post_id: str
    text: str


class Summary(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    post_id: str
    summary: str


class TitleQuery(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    post_id: str
    text: str


class Title(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    post_id: str
    title: str
