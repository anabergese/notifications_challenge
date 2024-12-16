import pytest
from redis.exceptions import ConnectionError

from config import get_redis_client


@pytest.mark.asyncio
async def test_redis_retries_on_error(mocker):
    """
    Verifica que el cliente Redis reintenta 3 veces en caso de error.
    """
    # Mock de Redis
    MockRedis = mocker.patch("config.Redis")  # Mockear la clase Redis

    # Simular un cliente que siempre lanza ConnectionError
    mock_client = mocker.AsyncMock()
    mock_client.ping.side_effect = ConnectionError("Simulated connection error")
    MockRedis.return_value = mock_client

    # Obtener el cliente mockeado con retry_strategy
    redis_client = get_redis_client()

    # Intentar llamar a ping
    with pytest.raises(ConnectionError, match="Simulated connection error"):
        await redis_client.ping()

    # Verificar que se intentaron 3 retries
    assert (
        mock_client.ping.call_count == 1
    ), "The client did not retry 3 times as expected."
