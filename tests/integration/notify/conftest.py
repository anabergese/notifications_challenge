import pytest


@pytest.fixture(
    params=[
        Exception("Service failure"),
        TimeoutError("Too much time passed."),
        ConnectionError("No internet connection"),
        ValueError("Invalid input"),
        RuntimeError("Runtime error occurred"),
    ]
)
def mocked_service_failures(request, mocker):
    mock_create_notification = mocker.patch(
        "service_layer.service.NotificationService.create_notification",
        side_effect=request.param,
    )
    return mock_create_notification


@pytest.fixture(
    params=[
        Exception("Service failure"),
        TimeoutError("Too much time passed."),
        ConnectionError("No internet connection"),
        ValueError("Invalid input"),
        RuntimeError("Runtime error occurred"),
    ]
)
def mocked_handle_failures(request, mocker):
    mock_handle = mocker.patch(
        "service_layer.service.handle",
        side_effect=request.param,
    )
    return mock_handle
