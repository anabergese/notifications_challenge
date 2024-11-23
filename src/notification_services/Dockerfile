FROM python:alpine

# Establece el directorio de trabajo en /app
WORKDIR /app
# Install gcc and other dependencies
RUN apk add --no-cache gcc musl-dev linux-headers

# Copia los requisitos del proyecto y los instala
COPY ./src/notification_services/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia el contenido del proyecto al directorio de trabajo
COPY src/notification_services .
ENV PYTHONPATH="/app"

# Comando para ejecutar la aplicación
CMD ["python", "entrypoints/main.py"]