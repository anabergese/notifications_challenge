from pydantic import BaseModel

class RequestModel(BaseModel):
    topic: str
    description: str
    

class ResponseModel(BaseModel):
    status: int
    message: str
