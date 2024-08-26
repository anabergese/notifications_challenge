from domain.events import NotificationFailed
from domain.system_events import Event


def send_service_status_notification(event: Event):
    print(f"Event {event} sent to external system for monitoring")


def send_notification_failed_to_slack(event: NotificationFailed):
    print(f"Slack Notification: A notification failed due to: {event.reason}")


# # Configuración del bus y suscripciones
# bus = MessageBus()

# # Suscribimos el handler de monitoreo para todos los eventos de servicios
# bus.subscribe(ServiceConnectionEstablished, send_service_status_notification)
# bus.subscribe(ServiceStopped, send_service_status_notification)
# bus.subscribe(ServiceConnectionFailed, send_service_status_notification)

# # Ejemplo de publicación de eventos
# eventos = ServiceConnectionEstablished(
#     timestamp=datetime.now(), service_name="DatabaseService"
# )
# bus.publish(eventos)

# eventos = ServiceStopped(timestamp=datetime.now(), service_name="DatabaseService")
# bus.publish(eventos)

# eventos = ServiceConnectionFailed(timestamp=datetime.now(), service_name="CacheService")
# bus.publish(eventos)


# # Suscribimos el handler al evento NotificationFailed
# bus.subscribe(NotificationFailed, send_notification_failed_to_slack)
# evento = NotificationFailed(timestamp=datetime.now(), reason="Slack API timeout")
# bus.publish(evento)
