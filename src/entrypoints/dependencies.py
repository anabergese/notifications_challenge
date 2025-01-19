from entrypoints.bootstrap import bootstrap
from service_layer.messagebus import MessageBus


async def get_message_bus() -> MessageBus:
    return await bootstrap()
