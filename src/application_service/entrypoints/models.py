from domain.enums import Topic
from pydantic import BaseModel, Field


class TopicValidator(BaseModel):
    topic: Topic = Field(..., description="Topic of the message")
    description: str = Field(..., description="Description of the message")


class ResponseModel(BaseModel):
    status: int
    message: str
