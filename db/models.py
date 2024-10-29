from sqlalchemy import (Column,Integer,String,DateTime,
Boolean,BigInteger,ForeignKey)

from sqlalchemy.orm import relationship
from db import Base
from datetime import datetime

# create model user
class User(Base):
    __tablename__ = "users"

    id = Column(Integer,autoincrement=True,primary_key=True)

    username = Column(String,nullable=False)
    password = Column(String,nullable=False)
    phone_number= Column(String,nullable=False)
    email = Column(String,nullable=False)
    reg_date = Column(DateTime,default=datetime.now)
# create model game
class Game(Base):
    __tablename__ = "game"

    id = Column(Integer, autoincrement=True, primary_key=True)
    game_name = Column(String)
# create model product
class  Product(Base):
    __tablename__ = "product"

    id = Column(Integer, autoincrement=True, primary_key=True)

    product_name = Column(String)
    price = Column(String)
    game_name = Column(String,ForeignKey('game.game_name'))
    category_fk = relationship(Game,lazy="subquery")