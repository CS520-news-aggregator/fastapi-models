from pydantic import BaseModel, Field
import uuid


class ScrapeData(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    source_id: str
    text: str
