import inspect
from typing import Any, Callable, Coroutine

from seedwork.application import redis_publisher
from service_layer.handlers import INITIAL_HANDLERS
from service_layer.messagebus import MessageBus


def bootstrap(
    publish: Callable[[str, Any], Coroutine[Any, Any, None]] = redis_publisher.publish,
) -> MessageBus:
    """
    Inicializa el MessageBus con handlers y dependencias inyectadas.
    """
    # Define las dependencias
    dependencies = {
        "publish": publish,
    }

    # Inyecta dependencias en los handlers
    injected_event_handlers = {
        event_type: [
            inject_dependencies(handler, dependencies) for handler in event_handlers
        ]
        for event_type, event_handlers in INITIAL_HANDLERS.items()
    }

    # Crea el MessageBus con los handlers inyectados
    return MessageBus(handlers=injected_event_handlers)


def inject_dependencies(
    handler: Callable[..., Any], dependencies: dict[str, Any]
) -> Callable[[Any], Any]:
    """
    Crea un wrapper que inyecta las dependencias necesarias al handler.
    """
    params = inspect.signature(handler).parameters
    deps = {
        name: dependency for name, dependency in dependencies.items() if name in params
    }
    return lambda event: handler(event, **deps)
