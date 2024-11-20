########################################################################################
# Etapa de base
########################################################################################
FROM python:alpine AS base
ENV PYTHON_VERSION="3.13"
LABEL maintainer="Luciano Parruccia <parruccia@yahoo.com.ar>"
LABEL version="1.0"
LABEL description="Imagen para desplegar una aplicación en python"
# Install gcc and other dependencies
RUN apk add --no-cache gcc musl-dev linux-headers \
    && rm -rf /var/cache/apk/*

# Set the working directory to /code
WORKDIR /app
########################################################################################
# Etapa de DESARROLLO
########################################################################################
FROM base AS final

# Copy requirements.txt and install dependencies
COPY ./infra/app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt \
    && rm requirements.txt \
    && rm -rf /root/.cache/pip

# # Set PYTHONPATH
ENV PYTHONPATH=/app
# Expose the ports for the FastAPI applications
EXPOSE 80

# Default command
CMD ["uvicorn", "application_service.entrypoints.main:app", "--host", "0.0.0.0", "--port", "80"]