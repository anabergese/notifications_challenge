import logging

from fastapi import FastAPI, Request, Response, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse


def add_error_handlers(app: FastAPI) -> None:
    """Registra los handlers de errores personalizados en la aplicación FastAPI."""
    app.add_exception_handler(RequestValidationError, custom_422_error_handler)  # type: ignore


async def custom_422_error_handler(_: Request, exc: RequestValidationError) -> Response:
    """Maneja los errores de validación personalizados."""
    errors = exc.errors()

    for error in errors:
        field = error["loc"][-1]
        error_type = error["type"]
        logging.error("Error en el campo '%s': %s", field, error_type)

        handler = error_handlers.get((field, error_type))
        if handler:
            return handler()

    return handle_generic_error()


def handle_invalid_topic() -> Response:
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={"detail": "Invalid topic."},
    )


def handle_missing_topic() -> Response:
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={"detail": "Topic is required."},
    )


def handle_missing_description() -> Response:
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={"detail": "Description is required."},
    )


def handle_invalid_description() -> Response:
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={"detail": "Invalid description."},
    )


def handle_generic_error() -> Response:
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={"detail": "Invalid request data."},
    )


# === Mapeo de errores específicos a handlers personalizados ===
error_handlers = {
    ("topic", "enum"): handle_invalid_topic,
    ("topic", "missing"): handle_missing_topic,
    ("description", "value_error.missing"): handle_missing_description,
    ("description", "missing"): handle_missing_description,
    ("description", "value_error"): handle_invalid_description,
    ("description", "string_too_short"): handle_invalid_description,
    ("description", "string_too_long"): handle_invalid_description,
    ("description", "string_type"): handle_invalid_description,
    ("description", "type_error"): handle_invalid_description,
}
