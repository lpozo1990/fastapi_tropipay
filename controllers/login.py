import os
from fastapi import APIRouter, HTTPException
import requests

router = APIRouter()


@router.post("/login")
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
