from pydantic import BaseModel

class DescriptionRequest(BaseModel):
    name: str
    brand: str
    category: str
    price: float

class DescriptionResponse(BaseModel):
    description: str

class SpecsRequest(BaseModel):
    name: str
    brand: str
    category: str

class SpecsResponse(BaseModel):
    specs: str