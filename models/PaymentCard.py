from typing import List
from pydantic import BaseModel, EmailStr


class Client(BaseModel):
    name: str
    lastName: str
    address: str
    phone: str
    email: EmailStr
    countryId: int
    termsAndConditions: bool


class Payload(BaseModel):
    reference: str
    concept: str
    favorite: bool
    description: str
    amount: int
    currency: str
    singleUse: bool
    reasonId: int
    expirationDays: int
    lang: str
    urlSuccess: str
    urlFailed: str
    urlNotification: str
    serviceDate: str
    client: Client
    directPayment: bool
    paymentMethods: List[str]
