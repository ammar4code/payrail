from fastapi import FastAPI

app = FastAPI()

@app.post("/veloce/quote")
async def veloce_quote():
    return {
    "esito": "ok",
    "commissione": "3.50",
    "valuta_commissione": "EUR",
    "importo_destinazione": "325000",
    "valuta_destinazione": "PKR",
    "giorni_consegna": 2
}

@app.post("/nordpost/rates")
async def nordpost_rates():
    return {
        "status": "SUCCESS",
        "offers": [
            {
                "feeCents": 420,
                "feeCurrency": "EUR",
                "payoutAmountCents": 32350000,
                "payoutCurrency": "PKR",
                "deliveryEstimateHours": 72
            }
        ]
    }