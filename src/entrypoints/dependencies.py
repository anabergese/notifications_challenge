from application.messagebus import MessageBus
from entrypoints.bootstrap import bootstrap


async def get_message_bus() -> MessageBus:
    return await bootstrap()
