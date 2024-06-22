from src.notification_services.entrypoints.domain.models import CreateRequestEvent

class SlackService:
    def send_to_slack(self, event: CreateRequestEvent):
        # Código para enviar el evento a Slack
        print(f"Sending to Slack from container: {event.description}")


class EmailService:
    def send_to_email(self, event: CreateRequestEvent):
        # Código para enviar el evento por correo electrónico
        print(f"Sending to Email from container: {event.description}")
