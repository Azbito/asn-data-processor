FROM python:3.9-slim
WORKDIR /app
COPY apps/api /app/api
RUN pip install --no-cache-dir -r /app/api/requirements.txt
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
