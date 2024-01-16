from fastapi import FastAPI
from dotenv import load_dotenv
from controllers import create_payment_card, get_payment_link, list_credentials, login


load_dotenv()
app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


app.include_router(login.router)
app.include_router(create_payment_card.router)
app.include_router(list_credentials.router)
app.include_router(get_payment_link.router)
