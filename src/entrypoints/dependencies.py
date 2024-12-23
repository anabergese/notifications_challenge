from entrypoints.bootstrap import bootstrap
from service_layer.messagebus import MessageBus

message_bus = bootstrap()


def get_message_bus() -> MessageBus:
    return message_bus
