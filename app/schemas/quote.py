from pydantic import BaseModel, Field  

class QuoteRequest(BaseModel):
    amount_minor: int = Field(ge=1)
    source_currency: str = Field(min_length=3, max_length=3)
    target_currency: str = Field(min_length=3, max_length=3)
    source_country: str = Field(min_length=2, max_length=2)
    target_country: str = Field(min_length=2, max_length=2)
