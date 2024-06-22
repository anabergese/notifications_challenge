from fastapi import FastAPI
import uvicorn
from src.notification_services.entrypoints.routes import notifications_routes

app = FastAPI(
    title="Notification Services",
    description="API for handling customer requests and sending notifications to various channels.",
    version="1.0.0",
)

app.include_router(notifications_routes.router, prefix="/notification-services")

@app.get("/")
def read_root():
    """Server is up and running."""
    return {"message": "Notifications Services"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=88)