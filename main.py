from fastapi import FastAPI,Request
from api.userapi.user import user_router
from api.postapi.post import test_router
import stripe
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse


app = FastAPI(docs_url="/",tags = ["oplatta"])
templates = Jinja2Templates(directory="templates")
@app.post("/",response_class=HTMLResponse)
async def main(request:Request):
    return templates.TemplateResponse(request=request,
                                      name = "index.html")

from db import Base,engine

Base.metadata.create_all(bind=engine)
# register router
app.include_router(user_router)
app.include_router(test_router)
# stripe.api_key = "your_stripe_secret_key"

# class Payment(BaseModel):
#     amount: int
#     currency: str
#     description: str
#
# @app.post("/payment")
# async def create_payment(payment: Payment):
#     try:
#         charge = stripe.Charge.create(
#             amount=payment.amount,
#             currency=payment.currency,
#             source="tok_visa",  # Используйте токен, полученный от клиента
#             description=payment.description
#         )
#         return {"message": "Payment successful"}
#     except Exception as e:
#         return {"error": f"Error processing payment: {str(e)}"}