from fastapi import APIRouter
from src.notification_services.entrypoints.domain.event_handlers import SlackService, EmailService
from src.notification_services.entrypoints.domain.models import CreateRequestEvent

router = APIRouter()
slack_service = SlackService()
email_service = EmailService()

@router.post("/slack")
async def send_to_slack(event: CreateRequestEvent):
    slack_service.send_to_slack(event)
    return {"status": "success", "message": f"Sending to Slack from container: {event.timestamp}"}

@router.post("/email")
async def send_to_email(event: CreateRequestEvent):
    email_service.send_to_email(event)
    return {"status": "success", "message": f"Sending to Email from container: {event.timestamp}"}