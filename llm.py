import uuid
from pydantic import Field
from annotator.analysis.bundle.models.base_model import BaseModel


class SummaryQuery(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    post_id: str
    text: str


class Summary(BaseModel):
    id: str
    post_id: str
    summary: str
