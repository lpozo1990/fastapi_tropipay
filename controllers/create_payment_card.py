from fastapi import APIRouter, Header
import requests

from models.PaymentCard import Payload


router = APIRouter()


@router.post("/create_payment_card")
async def create_payment_card(
    Authorization: str = Header(...), payload: Payload = None
):
    url = "https://tropipay-dev.herokuapp.com/api/v2/paymentcards"

    payload = payload.model_dump()
    headers = {
        "Authorization": Authorization,
        "Content-Type": "application/json",
        "Accept": "application/json",
    }

    response = requests.post(url, json=payload, headers=headers)
    result = response.json()
    short_url = result.get("shortUrl")
    return short_url
