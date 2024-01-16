import os
from fastapi import APIRouter, Header
import requests

router = APIRouter()


@router.post("/get_payment_link")
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
