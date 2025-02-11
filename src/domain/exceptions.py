from abc import ABC
from dataclasses import dataclass, field


# en folder de domain
@dataclass(frozen=True)
class DomainError(Exception, ABC):
    message: str


@dataclass(frozen=True)
class NotificationSendError(DomainError):
    message: str = field(
        default="Notification could not be sent, retries had been applied"
    )


# en folder de infrastructure
@dataclass(frozen=True)
class MessageBrokerError(Exception, ABC):
    message: str


@dataclass(frozen=True)
class RedisStreamsError(MessageBrokerError):
    message: str


@dataclass(frozen=True)
class GroupCreationError(RedisStreamsError):
    stream_key: str = field(default="")
    consumer_group: str = field(default="")
    message: str = field(default="Redis Streams group cannot be created")


# si lo uso en get_redis_client no funciona, porque no es una excepcion de redis?
# Al simular un error en la .env password de redis termino recibiendo este error:
# api      | redis.exceptions.AuthenticationError: invalid username-password pair
# api      |
# api      | ERROR:    Application startup failed. Exiting.
class RedisConnectionError(RedisStreamsError):
    pass
