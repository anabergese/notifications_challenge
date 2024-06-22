from fastapi import FastAPI
import uvicorn
from application_service.entrypoints.routes import application_service_routes

app = FastAPI(
    title="Application Service",
    description="API for handling customer requests and sending notifications to various channels.",
    version="1.0.0",
)

app.include_router(application_service_routes.router, prefix="/application-service")

@app.get("/")
def read_root():
    """Server is up and running."""
    return {"message": "Application Service"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)