from fastapi import FastAPI

app = FastAPI()

@app.post("/veloce/quote")
async def create_quote():
    return {
    "esito": "ok",
    "commissione": "3.50",
    "valuta_commissione": "EUR",
    "importo_destinazione": "325000",
    "valuta_destinazione": "PKR",
    "giorni_consegna": 2
}