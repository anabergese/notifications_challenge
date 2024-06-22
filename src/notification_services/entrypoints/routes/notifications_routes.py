from fastapi import APIRouter
from src.notification_services.domain.event_handlers import SlackService, EmailService
from src.notification_services.domain.models import CreateRequestEvent

router = APIRouter()
slack_service = SlackService()
email_service = EmailService()

@router.post("/slack")
async def send_to_slack(event: CreateRequestEvent):
    slack_service.send_to_slack(event)
    return {"status": "success", "message": "Sending to Slack from container"}

@router.post("/email")
async def send_to_email(event: CreateRequestEvent):
    email_service.send_to_email(event)
    return {"status": "success", "message": "Sending to Email from container"}