from fastapi import FastAPI
from app.api.v1.quotes import router

app = FastAPI()
app.include_router(router, prefix="/v1")

@app.get("/health")
async def health():
    return {"status": "ok"}
