from db.models import User
from db import get_db


def register_user_db(username, phone_number, password, email):
    with next(get_db()) as db:
        new_user = User(username=username, phone_number=phone_number,password=password, email=email)
        db.add(new_user)
        db.commit()
        return True

def get_all_users_db():
    with next(get_db()) as db:
        all_users = db.query(User).all()
        return all_users


def get_exact_user_db(user_id):
    with next(get_db()) as db:
        exact_user = db.query(User).filter_by(id=user_id).first()
        if exact_user:
            return exact_user
        return False


def delete_user_db(user_id):
    with next(get_db()) as db:
        delete = db.query(User).filter_by(id=user_id).first()
        db.delete(delete)
        db.commit()
        return True


def update_new_user_db(user_id, change_info, new_info):
    with next(get_db()) as db:
        user= db.query(User).filter_by(id=user_id).first()
        if user:
            if change_info == "username":
                user.username = new_info
            elif user == "email":
                user.email = new_info
            elif user == "password":
                user.password = new_info
            elif user == "phone_number":
                user.phone_number= new_info