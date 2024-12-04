from fastapi import status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse


async def custom_422_error_handler(request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={"detail": "Invalid topic."},
    )
