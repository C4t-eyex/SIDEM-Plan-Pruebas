# Imagen de la demo de SIDEM (solo para pruebas en clase, no para producción)
FROM python:3.14-slim

LABEL org.opencontainers.image.source="https://github.com/C4t-eyex/SIDEM-Plan-Pruebas" \
      org.opencontainers.image.description="Aplicación de la demo de SIDEM (commit 77f71b2)"

ENV PYTHONUNBUFFERED=1 \
    PYTHONIOENCODING=utf-8 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

# Dependencias primero, para aprovechar la caché de Docker
COPY sidem/API_seguimiento_docentes/requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

# Código de SIDEM en la versión fijada (ver preparar-demo.*)
COPY sidem/API_seguimiento_docentes/ ./

# Scripts propios de la demo
COPY seed_demo.py entrypoint.sh ./demo/
RUN chmod +x ./demo/entrypoint.sh

EXPOSE 5000
ENTRYPOINT ["./demo/entrypoint.sh"]
