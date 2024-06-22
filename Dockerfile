# syntax=docker/dockerfile:1
FROM python:3.10-alpine

# Set the working directory to /code
WORKDIR /code

# Install gcc and other dependencies
RUN apk add --no-cache gcc musl-dev linux-headers

# Copy requirements.txt and install dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /code
COPY . .

# Expose the ports for the FastAPI applications
EXPOSE 80
EXPOSE 88

# Default command
CMD ["uvicorn", "src.application_service.entrypoints.main:app", "--host", "0.0.0.0", "--port", "80"]