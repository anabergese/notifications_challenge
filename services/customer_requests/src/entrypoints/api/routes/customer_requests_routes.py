from fastapi import APIRouter
from fastapi import HTTPException
# from src.domain.services.customer_request_service import CustomerRequestService
from services.customer_requests.src.entrypoints.api.adapters.customer_requests_adapter import CustomerRequestsAdapter

router = APIRouter()
adapter = CustomerRequestsAdapter()

@router.get("/")
def read_root():
    """Server is up and running."""
    return {"message": "This is a route path"}

@router.post("/send", response_model=dict, status_code=200)
async def customer_request_port(customer_request):
    try:
        adapter.process_request(customer_request.topic, customer_request.description)
        return {"message": "Customer request processed successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) from e
