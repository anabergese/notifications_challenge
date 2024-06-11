from pydantic import BaseModel, Field

class CustomerRequest(BaseModel):
    id: int = Field(default=None, alias="_id")
    topic: str
    description: str