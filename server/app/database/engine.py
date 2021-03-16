from os import environ

from sqlalchemy import create_engine


uri = environ.get('DB_URI')
Engine = create_engine(uri)
