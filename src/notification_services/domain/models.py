from pydantic import BaseModel, Field

class CreateRequestEvent(BaseModel):
    id: int = Field(default=None)
    topic: str
    description: str
    source: str
    status: str