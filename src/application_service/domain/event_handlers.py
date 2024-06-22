# import requests
from src.application_service.domain.models import CreateRequestEvent

class EventLogger:
    def log_event(self, event: CreateRequestEvent):
        # Código para registrar el evento (puede ser en un archivo, base de datos, etc.)
        print(f"Logging event: {event.topic} - {event.description}")

class EventForwarder:
    def forward_event(self, event: CreateRequestEvent):
        # Código para reenviar el evento al canal adecuado
        if event.topic == "sales":
            self.send_to_slack(event)
        elif event.topic == "pricing":
            self.send_to_email(event)

    def send_to_slack(self, event: CreateRequestEvent):
        # Lógica para enviar el evento al contenedor de Slack
        # slack_url = "http://notification-services-container/slack"
        # response = requests.post(slack_url, json=event.model_dump())
        # if response.status_code != 200:
        #     raise Exception("Failed to send to Slack")
        print(f"Sending event to Slack: {event.topic} - {event.description}")

    def send_to_email(self, event: CreateRequestEvent):
        # Lógica para enviar el evento al contenedor de Email
        # email_url = "http://notification-services-container/email"
        # response = requests.post(email_url, json=event.model_dump())
        # if response.status_code != 200:
        #     raise Exception("Failed to send to Email")
        print(f"Sending event to Email: {event.topic} - {event.description}")
