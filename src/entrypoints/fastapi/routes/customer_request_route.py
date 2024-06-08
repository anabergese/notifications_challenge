from fastapi import APIRouter, status
from pydantic import BaseModel
from src.domain.services.customer_request_service import CustomerRequestService

router = APIRouter()

class CustomerRequest(BaseModel):
    topic: str
    description: str

@router.post("/", response_model=dict, status_code=status.HTTP_201_CREATED)
def handle_customer_request(request: CustomerRequest):
    try:
        service = CustomerRequestService()
        service.process_request(request.topic, request.description)
        return {"message": "Customer request processed successfully"}
    except Exception as e:
        raise e
