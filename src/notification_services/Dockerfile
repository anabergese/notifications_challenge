# # Dockerfile for Worker
# FROM python:3.12

# # Set the working directory
# WORKDIR /app

# # Copy the requirements file
# COPY src/notification_services/requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt
# COPY src/notification_services /app

# # Set PYTHONPATH
# ENV PYTHONPATH="/app"

# # Command to run the worker
# CMD ["python", "src/notification_services/entrypoints/main.py"]
# src/notification_services/Dockerfile
FROM python:3.9-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar el archivo de requerimientos y instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto de la aplicación
COPY . .

# Comando para ejecutar la aplicación
CMD ["python", "entrypoints/main.py"]