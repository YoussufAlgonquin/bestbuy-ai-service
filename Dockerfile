FROM python:3.12-slim

WORKDIR /app

# Install dependencies first (layer cache)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN addgroup --system appgroup && adduser --system --ingroup appgroup appuser
USER appuser

EXPOSE 5000

# uvicorn is the ASGI server that runs FastAPI
# --host 0.0.0.0 binds to all interfaces (required in container — not just localhost)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]