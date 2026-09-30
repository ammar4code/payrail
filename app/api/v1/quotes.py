from fastapi import APIRouter
from app.schemas.quote import QuoteRequest
router = APIRouter() 

@router.post("/quotes")
async def create_quote(payload: QuoteRequest):
    return payload