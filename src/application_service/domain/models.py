from pydantic import BaseModel, Field
from uuid import uuid4

class Message(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()), description="Unique identifier for the message")
    topic: str
    description: str

    @classmethod
    def create(cls, topic: str, description: str):
        return cls(topic=topic, description=description)

    # Añadir métodos adicionales para guardar el mensaje en la DB en el futuro
