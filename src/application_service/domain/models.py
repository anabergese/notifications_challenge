# from uuid import uuid4

# from domain.enums import Topic
# from pydantic import BaseModel, Field


# class Notification(BaseModel):
#     id: str = Field(
#         default_factory=lambda: str(uuid4()),
#         description="Unique identifier for the message",
#     )
#     topic: Topic = Field(..., description="Topic of the message")
#     description: str
