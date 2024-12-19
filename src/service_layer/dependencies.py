from service_layer.messagebus import INITIAL_HANDLERS, MessageBus

message_bus = MessageBus(handlers=INITIAL_HANDLERS)


def get_message_bus() -> MessageBus:
    return message_bus
