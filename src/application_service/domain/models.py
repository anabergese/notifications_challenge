from pydantic import BaseModel, Field
class RequestEvent(BaseModel):
    id: int = Field(default=None)
    topic: str
    description: str
    source: str
    status: str