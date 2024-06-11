from fastapi import APIRouter
from fastapi import HTTPException
from services.customer_requests.src.domain.models.customer_request import CustomerRequest
from services.customer_requests.src.entrypoints.api.adapters.customer_requests_adapter import CustomerRequestsAdapter

router = APIRouter()
adapter = CustomerRequestsAdapter()
    
@router.get("/")
def read_root():
    """Server is up and running."""
    return {"message": "This is a route path 2"}

@router.post("/send", response_model=dict, status_code=200)
async def customer_request_port(customer_request: CustomerRequest):
    try:
        return adapter.process_request(customer_request.topic, customer_request.description)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) from e
