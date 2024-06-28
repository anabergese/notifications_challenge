import requests
from src.application_service.domain.models import RequestEvent

class EventLogger:
    def log_event(self, event: RequestEvent):
        # Código para registrar el evento (puede ser en un archivo, base de datos, etc.)
        print(f"Logging event: {event.topic} - {event.description}")

class EventForwarder:
    def forward_event(self, event: RequestEvent):
        # Código para reenviar el evento al canal adecuado
        if event.topic == "sales":
            self.send_to_slack(event)
        elif event.topic == "pricing":
            self.send_to_email(event)

    def send_to_slack(self, event: RequestEvent):
        # Lógica para enviar el evento al contenedor de Slack
        slack_url = "http://notification_services:88/notification-services/slack"
        response = requests.post(slack_url, json=event.model_dump(), timeout=10)
        if response.status_code != 200:
            raise ValueError("Failed to send to Slack")
        print(f"Sending events to Slack: {event.topic} - {event.description}")

    def send_to_email(self, event: RequestEvent):
        email_url = "http://notification_services:88/notification-services/email"
        response = requests.post(email_url, json=event.model_dump(), timeout=10)
        if response.status_code != 200:
            raise ValueError("Failed to send to Email")
        print(f"Sending event to Email: {event.topic} - {event.description}")