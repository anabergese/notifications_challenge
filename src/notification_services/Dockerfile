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
# Usa una imagen base de Python (o cualquier otra según tu stack)
FROM python:3.9-slim

# Establece el directorio de trabajo en /app/src/notification_services
WORKDIR /app/src/notification_services

# Copia los requisitos del proyecto y los instala
COPY ./src/notification_services/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copia el contenido del proyecto al directorio de trabajo
COPY ./src/notification_services ./

# Comando para ejecutar la aplicación
CMD ["python", "entrypoints/main.py"]