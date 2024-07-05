# syntax=docker/dockerfile:1
FROM python:3.10-alpine

# Set the working directory to /code
WORKDIR /app

# Install gcc and other dependencies
RUN apk add --no-cache gcc musl-dev linux-headers

# Copy requirements.txt and install dependencies
COPY src/application_service/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY src/application_service /app

# Expose the ports for the FastAPI applications
EXPOSE 80

# Default command
CMD ["uvicorn", "src.application_service.entrypoints.main:app", "--host", "0.0.0.0", "--port", "80"]