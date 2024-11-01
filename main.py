from fastapi import FastAPI,Request
from api.userapi.user import user_router
from api.postapi.post import test_router
from api.photospai.photos import photo_router
from db.testservice import get_all_product_db
import stripe
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse




app = FastAPI(docs_url="/swagger_azim_777_01150607_ya_sdam_diplomku",tags = ["oplatta"])
templates = Jinja2Templates(directory="templates")
@app.get("/",response_class=HTMLResponse)
async def main(request:Request):
    return templates.TemplateResponse(request=request,
                                      name = "index.html")
@app.get("/product",response_class=HTMLResponse)
async def product(request:Request):

    return templates.TemplateResponse(request=request,name="product.html", context={"products": get_all_products_db()})
@app.get("/oplata",response_class=HTMLResponse)
async def oplata(request:Request):
    return templates.TemplateResponse(request=request,name="pokupka.html")


from db import Base,engine

Base.metadata.create_all(bind=engine)


app.include_router(user_router)
app.include_router(test_router)
app.include_router(photo_router)
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
