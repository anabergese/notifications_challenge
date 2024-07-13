from pydantic import BaseModel, Field

class CreateRequestEvent(BaseModel):
    id: str = Field(default=None)
    topic: str
    description: str
    source: str
    status: str