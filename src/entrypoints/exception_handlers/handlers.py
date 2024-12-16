import logging

from fastapi import status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse


def add_error_handlers(app):
    """Registra los handlers de errores personalizados en la aplicación FastAPI."""
    app.add_exception_handler(RequestValidationError, custom_422_error_handler)


async def custom_422_error_handler(request, exc: RequestValidationError):
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


def handle_invalid_topic():
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={"detail": "Invalid topic."},
    )


def handle_missing_topic():
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={"detail": "Topic is required."},
    )


def handle_missing_description():
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={"detail": "Description is required."},
    )


def handle_invalid_description():
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={"detail": "Invalid description."},
    )


def handle_generic_error():
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
