# Dockerfile for Worker
FROM python:3.12

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY src/notification_services/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY src/notification_services /app

# Set PYTHONPATH
ENV PYTHONPATH="/app"

# # Command to run the worker
CMD ["python", "src/notification_services/worker.py"]