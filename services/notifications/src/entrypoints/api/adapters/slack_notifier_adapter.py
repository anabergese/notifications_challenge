from services.notifications.src.entrypoints.api.ports.notifier_port import NotifierPort

class SlackNotifierAdapter(NotifierPort):
    def notify(self, description: str):
        # Implementación para notificar a Slack
        print(f"Sending notification to Slack: {description}")
    
    def validate_topic(self, topic: str) -> bool:
        # Lógica de validación del tema para correo electrónico
        return topic == "Sales"