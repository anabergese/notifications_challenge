from pydantic import BaseModel, Field, field_validator

class RequestModel(BaseModel):
    topic: str = Field(..., description="Topic of the task")
    description: str = Field(..., description="Description of the task")
    
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

class Error(BaseModel):
    code: str = Field(title="Error Details", description="Indicates the reason code to deny the operation", example="invalid_request")
    message: str = Field(title="Description", description="A short result description of the error", example="One or more inputs are invalid")
