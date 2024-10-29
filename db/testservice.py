from db.models import Game,Product
from db import get_db

def add_game_db(game_name):
    with next(get_db()) as db:
        game = Game(game_name =game_name)
        db.add(game)
        db.commit()
        return True

def add_product_db(product_name,game_name,price):
    with next(get_db()) as db:
        product= Product(product_name = product_name,price=price,game_name = game_name)
        db.add(product)
        db.commit()
        return True

def get_game_by_name_db(game_name):
    with next((get_db())) as db:
        find_game = db.query(Game).filter_by(game_name = game_name).first()
        if find_game:
            return find_game
        return False


def get_product_db(product_id):
    with next((get_db())) as db:
        find_product= db.query(Product).filter_by(id= product_id).first()
        if find_product:
            return find_product
        return False
#
def get_all_games_db():
    with next(get_db()) as db:
        all_users = db.query(Game).all()
        return all_users


def get_all_products_db():
    with next(get_db()) as db:
        all_products = db.query(Product).all()
        return all_products

def update_game_db(game_name,change_info,new_info):
    with next(get_db()) as db:
        update_info= db.query(Game).filter_by(game_name = game_name).first()
        if update_info:
            if change_info == "game_name":
                update_info.game_name = new_info


def update_product_db(product_name,change_info,new_info):
    with next(get_db()) as db:
        update_info = db.query(Product).filter_by(product_name = product_name).first()
        if update_info:
            if change_info == "product_name":
                update_info.product_name = new_info
            elif change_info == "game_name":
                update_info.game_name = new_info
            elif change_info == "price":
                update_info.price = new_info

def delete_game_db(game_id):
    with next(get_db()) as db:
        delete = db.query(Game).filter_by(id=game_id).first()
        db.delete(delete)
        db.commit()
        return True

def delete_product_db(game_id):
    with next(get_db()) as db:
        delete = db.query(Product).filter_by(id=game_id).first()
        db.delete(delete)
        db.commit()
        return True

