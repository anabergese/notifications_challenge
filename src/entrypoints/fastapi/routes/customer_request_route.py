from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from src.domain.services.customer_request_service import CustomerRequestService

router = APIRouter()

# Pydantic model for request validation
class CustomerRequest(BaseModel):
    topic: str
    description: str

# Endpoint to handle customer requests
@router.post("/", response_model=dict, status_code=status.HTTP_201_CREATED)
def handle_customer_request(request: CustomerRequest):
    try:
        service = CustomerRequestService()
        service.process_request(request.topic, request.description)
        return {"message": "Customer request processed successfully"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
