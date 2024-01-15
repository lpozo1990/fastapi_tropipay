import os
from fastapi import FastAPI, HTTPException, Header
import requests
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/login")
async def login():
    url = os.getenv("TROPIPAY_API_URL")
    email = os.getenv("TEST_EMAIL")
    password = os.getenv("TEST_PASSWORD")
    data = {"email": email, "password": password}
    headers = {"Content-Type": "application/json", "Accept": "application/json"}

    response = requests.post(url, json=data, headers=headers)
    if response.status_code != 200:
        raise HTTPException(
            status_code=response.status_code, detail="Error en la autenticación"
        )

    result = response.json()
    token = result.get("token")
    if not token:
        raise HTTPException(
            status_code=500, detail="Token no encontrado en la respuesta"
        )

    return {"token": token}


@app.get("/list_credentials")
async def list_credentials(
    Authorization: str = Header(...),
    Accept: str = Header(...),
    Securitycode: str = Header(...),
):
    url = "https://tropipay-dev.herokuapp.com/api/v2/credential"
    headers = {
        "Authorization": Authorization,
        "Accept": Accept,
        "Securitycode": Securitycode,
    }

    response = requests.get(url, headers=headers)
    result = response.json()
    return result


@app.post("/get_payment_link")
async def get_payment_link(
    Authorization: str = Header(...), Securitycode: str = Header(...)
):
    headers = {
        "Authorization": Authorization,
        "Securitycode": Securitycode,
        "Content-Type": "application/json",
        "Accept": "application/json",
    }
    url = "https://tropipay-dev.herokuapp.com/api/v2/movements/in/with_tpp_url"

    payload = {
        "reference": "SP000521",
        "concept": "Cakes and Coffee",
        "description": "Only the best products",
        "amount": 1500,
        "currency": "USD",
        "lang": "es",
        "urlSuccess": "http://e-commers.com/success",
        "urlFailed": "http://e-commers.com/failed",
        "urlNotification": "https://e-commers.com/callback_notification",
    }

    response = requests.post(url, json=payload, headers=headers)

    result = response.json()
    return result
