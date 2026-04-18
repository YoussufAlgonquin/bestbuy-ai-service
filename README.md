# BestBuy AI Service

A FastAPI service that generates product descriptions and technical specifications using Azure OpenAI (GPT-4o-mini).

## Endpoints

| Method | Path | Description |
|--------|------|-------------|
| GET | `/health` | Health check |
| POST | `/generate/description` | Generate a product marketing description |
| POST | `/generate/specs` | Generate product technical specifications |

## Request Examples

**POST /generate/description**
```json
{
  "name": "Galaxy Tab S9",
  "brand": "Samsung",
  "category": "Tablets",
  "price": 799.99
}
```

**POST /generate/specs**
```json
{
  "name": "Galaxy Tab S9",
  "brand": "Samsung",
  "category": "Tablets"
}
```

## Setup

1. Create a `.env` file:
```
AZURE_OPENAI_API_KEY=your_key
AZURE_OPENAI_ENDPOINT=your_endpoint
AZURE_OPENAI_DEPLOYMENT=your_deployment
```

2. Install dependencies and run:
```bash
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 5000
```

## Docker

```bash
docker build -t bestbuy-ai-service .
docker run -p 5000:5000 --env-file .env bestbuy-ai-service
```
