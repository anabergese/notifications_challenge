from fastapi import APIRouter
from fastapi import HTTPException
from services.customer_requests.src.domain.models.customer_request import CustomerRequest
from services.customer_requests.src.entrypoints.api.adapters.customer_requests_adapter import CustomerRequestsAdapter
from services.notifications.src.entrypoints.api.adapters.email_notifier_adapter import EmailNotifierAdapter
from services.notifications.src.entrypoints.api.adapters.slack_notifier_adapter import SlackNotifierAdapter

router = APIRouter()
slack_notifier = SlackNotifierAdapter()
email_notifier = EmailNotifierAdapter()
adapter = CustomerRequestsAdapter(slack_notifier, email_notifier)


@router.get("/")
def read_root():
    """Server is up and running."""
    return {"message": "This is a route path 2"}

@router.post("/send", response_model=dict, status_code=200)
async def customer_request_port(customer_request: CustomerRequest):
    try:
        adapter.process_request(customer_request.topic, customer_request.description)
        return {"message": "Customer request sent successfully."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) from e
