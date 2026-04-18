import os
from openai import AzureOpenAI

def get_client() -> AzureOpenAI:
    return AzureOpenAI(
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),
        azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
        api_version="2024-02-01"
    )

DEPLOYMENT = os.getenv("AZURE_OPENAI_DEPLOYMENT", "gpt-4o")

def generate_description(name: str, brand: str, category: str, price: float) -> str:
    client = get_client()
    prompt = f"""You are a product copywriter for Best Buy Canada.
Write a compelling 2-3 sentence marketing description for the following product.
Be specific, highlight key benefits, and keep it suitable for a product listing page.

Product: {name}
Brand: {brand}
Category: {category}
Price: ${price:.2f} CAD

Return only the description text, no labels or extra formatting."""

    response = client.chat.completions.create(
        model=DEPLOYMENT,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=200,
        temperature=0.7  # Some creativity, but not too random
    )
    return response.choices[0].message.content.strip()

def generate_specs(name: str, brand: str, category: str) -> str:
    client = get_client()
    prompt = f"""You are a technical writer for Best Buy Canada.
Generate a concise technical specification summary for the following product.
Format as 4-6 bullet points. Be specific with realistic specs for this type of product.

Product: {name}
Brand: {brand}
Category: {category}

Return only the bullet points, no intro text."""

    response = client.chat.completions.create(
        model=DEPLOYMENT,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=300,
        temperature=0.3  # Lower temperature = more factual, consistent
    )
    return response.choices[0].message.content.strip()