from datetime import datetime, timezone
from pydantic import BaseModel, Field

class CreateRequestEvent(BaseModel):
    id: int = Field(default=None)
    topic: str
    description: str
    source: str
    status: str
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))