from fastapi import APIRouter
from db.userservice import (register_user_db,get_all_users_db,get_exact_user_db,
                            delete_user_db,update_new_user_db)
from pydantic import BaseModel
user_router = APIRouter(prefix="/user",
                        tags=["polsovatelskaya chast"])

class User(BaseModel):
    username: str
    email: str
    phone_number: str
    password: str



@user_router.post("/register")
async def register_user(user: User):
    user_dict = dict(user)
    result = register_user_db(**user_dict)
    if result:
        return {"status":1,"message":"vi udachno zaregalis"}
    return {"status":0,"message":"error"}


@user_router.get("/get_all_user")
async def get_all_users_api():
    return get_all_users_db()


@user_router.get("/get_exact_user")
async def get_exact_users_api(user_id:int):
    result = get_exact_user_db(user_id)
    return result


@user_router.delete("/delete_user")
async def delete_user_api(user_id:int):
    return delete_user_db(user_id)

@user_router.put("/update_new_user")
async def update_user_api(user_id:int,change_info:str,new_info:str):
    result = update_new_user_db(user_id, change_info, new_info)
    if result:
        return "Info is save"
    return result