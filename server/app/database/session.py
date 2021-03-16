from sqlalchemy.orm import sessionmaker

from database.engine import Engine


def create_session():
    return sessionmaker(bind=Engine)()
