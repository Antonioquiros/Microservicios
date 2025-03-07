# Usar una imagen base ligera
FROM python:3.9-alpine

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos necesarios
COPY requirements.txt .
COPY app.py .
COPY municipio.json .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto del servicio
EXPOSE 5001

# Ejecutar el servicio
CMD ["python", "app.py"]
