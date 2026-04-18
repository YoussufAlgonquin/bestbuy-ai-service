import os
from dotenv import load_dotenv
load_dotenv()
from fastapi import FastAPI, HTTPException
from models import DescriptionRequest, DescriptionResponse, SpecsRequest, SpecsResponse
from openai_client import generate_description, generate_specs

app = FastAPI(title="BestBuy AI Service", version="1.0.0")

@app.get("/health")
def health():
    return {"status": "healthy", "service": "ai-service"}

@app.post("/generate/description", response_model=DescriptionResponse)
async def create_description(request: DescriptionRequest):
    try:
        description = generate_description(
            request.name, request.brand, request.category, request.price
        )
        return DescriptionResponse(description=description)
    except Exception as e:
        # Don't expose raw OpenAI errors to the client — could leak API details
        raise HTTPException(status_code=500, detail="Failed to generate description")

@app.post("/generate/specs", response_model=SpecsResponse)
async def create_specs(request: SpecsRequest):
    try:
        specs = generate_specs(request.name, request.brand, request.category)
        return SpecsResponse(specs=specs)
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to generate specs")