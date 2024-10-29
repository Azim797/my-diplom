from fastapi import APIRouter
from db.testservice  import (add_game_db,add_product_db
                             ,get_product_db, get_all_games_db,get_all_products_db,
                             update_game_db,update_product_db,delete_game_db,delete_product_db)

test_router = APIRouter(prefix="/test",tags = ["post"])

@test_router.post("/add_game")
async def add_game_api(game_name):
    add_category = add_game_db(game_name)
    return add_category

@test_router.post("/add_product")
async def add_product_api(product_name:str,game_name:str,price:str):
    add_game = add_product_db(product_name,game_name,price)
    return add_game

@test_router.get("/get_all_games")
async def get_all_games_api():
    return get_all_games_db()

@test_router.get("/get_all_products")
async def get_all_products_api():
    return get_all_products_db

@test_router.get("/get_product")
async def get_exact_product_api(product_id):
    get_product = get_product_db(product_id)
    return get_product

@test_router.put("/update_game")
async def update_game_api(game_name:str,change_info:str,new_info:str):
    update_game = update_game_db(game_name, change_info, new_info)
    if update_game:
        return "Info is save"
    return update_game
@test_router.put("/update_product")
async def update_product_api(product_name:str,price:str,game_name:str):
    update_product = update_product_db(product_name,price,game_name)
    if update_product:
        return  "Info is save"
    return update_product
@test_router.delete("/delete_game")
async def delete_game_api(game_id):
    return delete_game_db(game_id)

@test_router.delete("/delete_product")
async def delete_product_api(game_id):
    return delete_product_db(game_id)
