from typing import Union
from fastapi import FastAPI
from src.entrypoints.fastapi.routes import customer_request_route
import uvicorn

app = FastAPI(
    title="Customer Request Notification System",
    description="API for handling customer requests and sending notifications to various channels.",
    version="1.0.0",
)

app.include_router(customer_request_route.router, prefix="/api/v1/customer-requests", tags=["Customer Requests"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Customer Request Notification System"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)