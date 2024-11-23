FROM python:alpine

# Set the working directory to /code
WORKDIR /app

# Install gcc and other dependencies
RUN apk add --no-cache gcc musl-dev linux-headers

# Copy requirements.txt and install dependencies
COPY ./infra/app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy only the application_service directory to /app
COPY src/application_service .

# # Set PYTHONPATH
ENV PYTHONPATH=/app
# Expose the ports for the FastAPI applications
EXPOSE 80

# Default command
CMD ["uvicorn", "application_service.entrypoints.main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]