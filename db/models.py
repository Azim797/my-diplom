from sqlalchemy import (Column,Integer,String,DateTime,
Boolean,BigInteger,ForeignKey)

from sqlalchemy.orm import relationship
from db import Base
from datetime import datetime

# create model user
class User(Base):
    __tablename__ = "users"

    id = Column(Integer,autoincrement=True,primary_key=True)

    username = Column(String,nullable=False,unique=True)
    password = Column(String,nullable=False,unique=True)
    phone_number= Column(String,nullable=False)
    email = Column(String,nullable=False)
    reg_date = Column(DateTime,default=datetime.now)
# create model game
class Game(Base):
    __tablename__ = "game"

    id = Column(Integer, autoincrement=True, primary_key=True)
    game_name = Column(String)
# create model product
class Photo(Base):
    __tablename__ = "photo"

    id = Column(Integer,autoincrement=True,primary_key=True)
    photo_path = Column(String,nullable=False)

class  Product(Base):
    __tablename__ = "product"

    id = Column(Integer, autoincrement=True, primary_key=True)

    product_name = Column(String)
    price = Column(String)
    game_name = Column(String,ForeignKey('game.game_name'))
    category_fk = relationship(Game,lazy="subquery")
    product_photo = Column(String,ForeignKey('photo.id'))
    photo_fk = relationship(Photo,lazy="subquery")


class Oplata(Base):
    __tablename__ = 'oplata'

    id = Column(Integer, autoincrement=True, primary_key=True)
    number_of_cart = Column(Integer,default=16)
    srok_of_cart = Column(String)
    cvv_cvc = Column(Integer)
