# Dockerfile for Worker
FROM python:3.12

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY ../requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the worker code
COPY . .

# Command to run the worker
CMD ["python", "src.notification_services.worker.py"]