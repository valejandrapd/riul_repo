#Imagen de base 
From python:3.14.7

#Variables de entorno 
ENV pythondontwritebythecode=1

#Logs
ENV pythonnunbuffered=1

#Directorio de trabajo
WORKDIR /app

#Dependecias del sistema
RUN apk-get update \
    && aptget install -y --no-install-recommends gcc \
    && rm -rf/var/lib/apt/lists/*

#Dependencias de python
COPY requirements.txt .

#Instalación de las dependencias
RUN pip install --no-cache-dir -r requirements.txt

#Código de la aplicación
COPY . .

#Puerto
EXPOSE 5000

#Gunicorn exect app en flask
CMD ["gunicorn", "--bind", "0.0.0.0:5000","--workers","3","run:app"]
