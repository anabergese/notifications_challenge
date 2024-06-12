from services.notifications.src.entrypoints.api.ports.notifier_port import NotifierPort

class EmailNotifierAdapter(NotifierPort):
    def notify(self, description: str):
        # Implementación para notificar por correo electrónico
        print(f"Sending notification to Email: {description}")

    def validate_topic(self, topic: str) -> bool:
        # Lógica de validación del tema para correo electrónico
        return topic == "Pricing"