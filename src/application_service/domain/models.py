from pydantic import BaseModel, Field
from uuid import uuid4
from .value_objects import TopicEnum

class Message(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()), description="Unique identifier for the message")
    topic: TopicEnum = Field(..., description="Topic of the message")
    description: str

    @classmethod
    def create(cls, topic: TopicEnum, description: str):
        return cls(
            topic=topic.value,
            description=description
        )

    # Añadir métodos adicionales para guardar el mensaje en la DB en el futuro
