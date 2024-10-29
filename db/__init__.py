from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base

SQLALCHEMY_DATABASE_URI ="sqlite:///shop.db"
#cozdaem dvijoc
engine = create_engine(SQLALCHEMY_DATABASE_URI)
#cozdaem sessiu
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()
