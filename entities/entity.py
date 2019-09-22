# coding=utf-8

import datetime
from sqlalchemy import create_engine, Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import credentials

db_url = credentials.db_url
db_name = credentials.db_name
db_user = credentials.db_user
db_password = credentials.db_password

engine = create_engine('sqlite:///iotHome.db')
Session = sessionmaker(bind=engine)
Base = declarative_base()


class Entity:
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    last_updated_by = Column(String)

    def __init__(self, created_by):
        self.created_at = datetime.datetime.now(datetime.timezone.utc)
        self.updated_at = datetime.datetime.now(datetime.timezone.utc)
        self.last_updated_by = created_by
