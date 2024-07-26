from uuid import uuid4

from domain.enums import Topic
from pydantic import BaseModel, Field


class Message(BaseModel):
    id: str = Field(
        default_factory=lambda: str(uuid4()),
        description="Unique identifier for the message",
    )
    topic: Topic = Field(..., description="Topic of the message")
    description: str

    @classmethod
    def create(cls, topic: Topic, description: str):
        return cls(topic=topic.value, description=description)
