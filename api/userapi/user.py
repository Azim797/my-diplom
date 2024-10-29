from fastapi import APIRouter
from db.userservice import *
user_router = APIRouter(prefix="/user",
                        tags=["polsovatelskaya chast"])

@user_router.post("/register")
async def register_user(user_name:str,phone_number:str,
                        password:str):
    result = add_user_db(username = user_name,
                         phonenumber=phone_number,
                         password=password)
    if result:
        return {"status":1,"message":"vi udachno zaregalis"}
    return {"status":0,"message":"error"}