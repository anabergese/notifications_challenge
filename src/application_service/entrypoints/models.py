from pydantic import BaseModel, field_validator

class RequestModel(BaseModel):
    topic: str
    description: str
    
    @field_validator('topic')
    @classmethod
    def validate_topic(cls, v):
        allowed_topics = {"sales", "pricing"}
        if v.lower() not in allowed_topics:
            raise ValueError('Invalid topic. Allowed topics are: "sales" or "pricing".')
        return v.lower()

class ResponseModel(BaseModel):
    status: int
    message: str
