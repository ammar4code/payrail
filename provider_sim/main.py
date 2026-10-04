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

@app.post("/adriatica/pricing")
async def adriatica_pricing():
    return {
    "esito": "ok",
    "importo": "3250.00",
    "divisa": "PKR",
    "spese": [
        {"tipo": "base", "importo": "2.00"},
        {"tipo": "cambio", "importo": "1.75"}
    ],
    "divisa_spese": "EUR",
    "consegna": {"da": "2026-10-06", "a": "2026-10-08"}
}

@app.post("/adriatica/pricing-error")
async def adriatica_pricing_error():
    return{
    "esito": "errore",
    "codice": "VALUTA_NON_SUPPORTATA",
    "messaggio": "Currency pair not supported"
}