import logging

from fastapi import status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse


async def custom_422_error_handler(request, exc: RequestValidationError):
    errors = exc.errors()
    for error in errors:
        field = error["loc"][-1]
        error_type = error["type"]
        logging.error("Error en el campo '%s': %s", field, error_type)

        if field == "topic":
            if error_type == "enum":
                return JSONResponse(
                    status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                    content={"detail": "Invalid topic."},
                )
            else:
                return JSONResponse(
                    status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                    content={"detail": "Topic is required."},
                )
        elif field == "description":
            return JSONResponse(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                content={"detail": "Description is required."},
            )

    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={"detail": "Invalid request data."},
    )
