FROM python:3.12

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia los requisitos del proyecto y los instala
COPY ./infra/db/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia el contenido del proyecto al directorio de trabajo
COPY src/db_service .
ENV PYTHONPATH="/app"

# Comando para ejecutar la aplicación
CMD ["python", "entrypoints/main.py"]