# from dataclasses import asdict

# import pytest

# from domain.enums import RedisStreams
# from domain.events import NotificationCreated
# from infrastructure.redis.redis_publisher import publish


# class MockRedisClient:
#     def __init__(self):
#         self.xadd_called_with = None
#         self.xadd_exception = None

#     async def xadd(self, stream_key, event_data):
#         if self.xadd_exception:
#             raise self.xadd_exception
#         self.xadd_called_with = (stream_key, event_data)


# @pytest.fixture
# def mock_redis_client():
#     return MockRedisClient()


# @pytest.fixture
# def mock_get_redis_client(monkeypatch, mock_redis_client):
#     async def get_mock_client():
#         return mock_redis_client

#     monkeypatch.setattr(
#         "infrastructure.redis.redis_initialization.get_redis_client",
#         get_mock_client,
#     )
#     return mock_redis_client


# # @pytest.mark.asyncio
# # async def test_publish_success(mock_get_redis_client, mock_redis_client):
# #     event = NotificationCreated(topic="pricing", description="test description")
# #     stream_key = RedisStreams.NOTIFICATIONS
# #     await publish(event, stream_key)
# #     assert mock_redis_client.xadd_called_with == (stream_key.value, asdict(event))


# # @pytest.mark.asyncio
# # async def test_publish_failure(mock_get_redis_client, mock_redis_client, monkeypatch):
# #     event = NotificationCreated(topic="pricing", description="test description")
# #     stream_key = RedisStreams.NOTIFICATIONS
# #     mock_redis_client.xadd_exception = Exception("Test exception")

# #     logged_errors = []

# #     def mock_logging_error(msg, *args):
# #         logged_errors.append(msg % args)

# #     monkeypatch.setattr("logging.error", mock_logging_error)

# #     with pytest.raises(Exception, match="Test exception"):
# #         await publish(event, stream_key)

# #     assert "Error publishing to stream: Test exception" in logged_errors
