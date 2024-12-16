from unittest.mock import MagicMock, patch

import pytest
from redis import ConnectionError, Redis
from redis.backoff import ExponentialBackoff
from redis.retry import Retry

# Simulación de configuración incorrecta para forzar un error
REDIS_HOST = "invalid-host"
REDIS_PORT = 6379
REDIS_DB = 0


# Función a probar
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
            redis_client.get("key")  # Operación que activa el retry_strategy

        # Verificar que `connect` fue llamado 4 veces (1 inicial + 3 reintentos)
        assert mock_connect.call_count == 1  # 1 intento inicial + 3 reintentos
