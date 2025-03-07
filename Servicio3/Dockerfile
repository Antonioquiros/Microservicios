FROM python:3.9-alpine
WORKDIR /app
COPY requirements.txt .
COPY app.py .
COPY demo.json .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5002
CMD ["python", "app.py"]
