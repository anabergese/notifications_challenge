from pydantic import BaseModel

class Request(BaseModel):
    topic: str
    description: str

class Response(BaseModel):
    status: int
    message: str
