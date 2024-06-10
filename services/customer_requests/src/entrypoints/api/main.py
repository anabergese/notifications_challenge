from fastapi import FastAPI
import uvicorn
from services.customer_requests.src.entrypoints.api.routes import customer_requests_routes

app = FastAPI(
    title="Customer Request Notification System",
    description="API for handling customer requests and sending notifications to various channels.",
    version="1.0.0",
)

app.include_router(customer_requests_routes.router, prefix="/api/v1/customer-requests")

@app.get("/")
def read_root():
    """Server is up and running."""
    return {"message": "Welcome to the Customer Requests Handler App"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)