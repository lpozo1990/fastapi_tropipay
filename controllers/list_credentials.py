from fastapi import APIRouter, Depends, Header
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
import requests

router = APIRouter()

auth_scheme = HTTPBearer()


@router.get("/list_credentials")
async def list_credentials(
    Securitycode: str = Header(...),
    Authorization: HTTPAuthorizationCredentials = Depends(auth_scheme),
):
    token = "Bearer " + Authorization.credentials
    url = "https://tropipay-dev.herokuapp.com/api/v2/credential"
    headers = {
        "Authorization": token,
        "Accept": "application/json",
        "Securitycode": Securitycode,
    }

    response = requests.get(url, headers=headers)
    result = response.json()
    return result
