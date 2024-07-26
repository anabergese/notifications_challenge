from pydantic import BaseModel, Field
from domain.enums import Topic

class TopicValidator(BaseModel):
    topic: Topic = Field(..., description="Topic of the message")
    description: str = Field(..., description="Description of the message")

class ResponseModel(BaseModel):
    status: int
    message: str
