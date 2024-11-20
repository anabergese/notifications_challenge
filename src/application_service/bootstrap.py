from typing import Callable

from domain.system_events import (
    NotificationFailed,
    ServiceConnectionEstablished,
    ServiceConnectionFailed,
    ServiceStopped,
)
from redis_publisher import publish
from service_layer.event_handlers import (
    send_notification_failed_to_slack,
    send_service_status_notification,
)
from service_layer.message_bus import MessageBus


def bootstrap(
    publish: Callable = publish,
) -> MessageBus:

    # Dependencias
    dependencies = {
        "publish": publish,
    }

    # Handlers con inyección de dependencias
    event_handlers = {
        ServiceConnectionEstablished: [
            inject_dependencies(send_service_status_notification, dependencies)
        ],
        ServiceStopped: [
            inject_dependencies(send_service_status_notification, dependencies)
        ],
        ServiceConnectionFailed: [
            inject_dependencies(send_service_status_notification, dependencies)
        ],
        NotificationFailed: [
            inject_dependencies(send_notification_failed_to_slack, dependencies)
        ],
    }

    # Crear y retornar el MessageBus
    bus = MessageBus()

    # Suscribir handlers al MessageBus
    for event_type, handlers in event_handlers.items():
        for handler in handlers:
            bus.subscribe(event_type, handler)

    return bus


def inject_dependencies(handler: Callable, dependencies: dict) -> Callable:
    """
    Inyecta las dependencias requeridas en el handler. Utiliza la reflexión para determinar
    qué dependencias son necesarias según los parámetros del handler.
    """
    import inspect

    params = inspect.signature(handler).parameters
    deps = {
        name: dependency for name, dependency in dependencies.items() if name in params
    }
    return lambda event: handler(event, **deps)
