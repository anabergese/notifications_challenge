from pydantic import BaseModel, Field

class CustomerRequest(BaseModel):
    id: int = Field(default=None, alias="_id")
    topic: str
    description: str

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "id": 1,
                "topic": "sales",
                "description": "Need assistance with a sales inquiry."
            }
        }