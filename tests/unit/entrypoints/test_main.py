import pytest

from src.entrypoints.main import app


def test_app_initialization():
    assert app.title == "Notification System"
    assert app.version == "1.0.0"
    assert len(app.routes) > 0


def test_app_error_handlers():
    assert len(app.exception_handlers) > 0


def test_app_openapi_schema():
    assert app.openapi_schema is None  # Schema is generated on first access
    openapi = app.openapi()
    assert openapi["info"]["title"] == "Notification System"
    assert openapi["info"]["version"] == "1.0.0"
    assert "paths" in openapi
