# Use the official Python image as the base image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /code

# Copy the requirements file into the container
COPY rrequirements.txt requirements.txt

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the app runs on (if this service exposes a port)
EXPOSE 80

# Copy the application code into the container
COPY . .

# Define the command to run the service
CMD ["uvicorn", "services.customer_requests.src.entrypoints:main", "--host", "0.0.0.0", "--port", "80"]