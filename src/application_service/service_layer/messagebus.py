import asyncio
from inspect import iscoroutinefunction
from typing import Callable, Dict, List, Type

# Diccionario que mapea tipos de eventos a sus handlers
HANDLERS: Dict[Type, List[Callable]] = {}


async def handle(event):
    """Invoca los handlers registrados para un evento dado."""
    event_type = type(event)
    for handler in HANDLERS.get(event_type, []):
        # Si el handler es asíncrono, usamos await
        if iscoroutinefunction(handler):
            await handler(event)
        else:
            handler(event)


def register_handler(event_type: Type, handler: Callable):
    """Registra un handler para un evento específico."""
    if event_type not in HANDLERS:
        HANDLERS[event_type] = []
    HANDLERS[event_type].append(handler)
