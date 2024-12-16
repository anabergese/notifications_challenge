from unittest.mock import MagicMock, patch

import pytest
from redis import ConnectionError, Redis
from redis.backoff import ExponentialBackoff
from redis.retry import Retry

REDIS_HOST = "invalid-host"
REDIS_PORT = 6379
REDIS_DB = 0


def get_redis_client_with_retry():
    retry_strategy = Retry(ExponentialBackoff(), retries=3)
    return Redis(
        host=REDIS_HOST,
        port=REDIS_PORT,
        db=REDIS_DB,
        retry=retry_strategy,
        retry_on_error=[ConnectionError],
    )


def test_redis_retry_behavior():
    # Mockear la conexión completa para forzar el uso de reintentos
    with patch(
        "redis.connection.Connection.connect",
        side_effect=ConnectionError("Simulated Connection Error"),
    ) as mock_connect:
        redis_client = get_redis_client_with_retry()
        with pytest.raises(ConnectionError):
            redis_client.get("key")

        assert (
            mock_connect.call_count == 1
        )  # deberia fallar el test por esta linea, debe ser igual a 4
