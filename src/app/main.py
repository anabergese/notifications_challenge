from typing import Union
from fastapi import FastAPI
from src.entrypoints.fastapi.routes import customer_request_route

app = FastAPI(
    title="Customer Request Notification System",
    description="API for handling customer requests and sending notifications to varios channels.",
    version="1.0.0",
)

app.include_router(customer_request_route.router, prefix="/api/v1/customer-requests", tags=["Customer Requests"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Customer Request Notification System"}