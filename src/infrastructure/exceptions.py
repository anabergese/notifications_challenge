from abc import ABC
from dataclasses import dataclass, field


@dataclass(frozen=True)
class MessageBrokerError(Exception, ABC):
    message: str


@dataclass(frozen=True)
class RedisStreamsError(MessageBrokerError):
    message: str


@dataclass(frozen=True)
class CreateGroupError(RedisStreamsError):
    stream_key: str = field(default="")
    consumer_group: str = field(default="")
    message: str = field(default="Redis Streams group cannot be created")


@dataclass(frozen=True)
class ReadGroupError(RedisStreamsError):
    stream_key: str = field(default="")
    consumer_group: str = field(default="")
    message: str = field(
        default="Error reading from Redis stream '{stream_key}' with group '{group}' and consumer '{consumer}'"
    )
