#!/usr/bin/python3
from models.base_model import BaseModel, Base
from sqlalchemy import create_engine, text, Column, String, Integer
from sqlalchemy.orm import sessionmaker

class City(BaseModel, Base):
    __tablename__ = 'cities'
    state_id = Column(String(60))
    name = Column(String(128))

                  