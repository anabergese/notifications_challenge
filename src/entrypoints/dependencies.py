from entrypoints.bootstrap import bootstrap
from seedwork.application import redis_publisher
from service_layer.messagebus import MessageBus


def get_message_bus() -> MessageBus:
    return bootstrap(publish=redis_publisher.publish)
