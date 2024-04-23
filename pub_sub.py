from typing import List
from pydantic import BaseModel


class Message(BaseModel):
    source_ids: List[str]
    message: str


class Subscriber(BaseModel):
    ip_address: str
    port: int

    def __eq__(self, other: BaseException):
        return self.ip_address == other.ip_address and self.port == other.port
