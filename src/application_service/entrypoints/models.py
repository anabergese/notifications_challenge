from pydantic import BaseModel, Field
from domain.value_objects import TopicEnum

class TopicValidator(BaseModel):
    topic: TopicEnum = Field(..., description="Topic of the message")
    description: str = Field(..., description="Description of the message")

class ResponseModel(BaseModel):
    status: int
    message: str
