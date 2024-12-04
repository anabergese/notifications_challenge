FROM python:3.9

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Instala dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia el código fuente
COPY src/ /app/src

# Expone el puerto para FastAPI
EXPOSE 80

# Comando de inicio
CMD ["uvicorn", "src.entrypoints.main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]
