# -*- coding:UTF-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database
from os import environ

NAME = environ['DB_NAME']
USER = environ['DB_USER']
PASSWORD = environ['DB_PASSWORD']
HOST = environ['DB_HOST']
PORT = environ['DB_PORT']

# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/db"
SQLALCHEMY_DATABASE_URL = "postgresql://" + USER + ":" + PASSWORD + "@" + HOST + ":" + PORT + "/db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

if not database_exists(engine.url):
    create_database(engine.url)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()