#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel

from sqlalchemy import Column, DateTime, String
from sqlalchemy.ext.declarative import declarative_base


class State(BaseModel):
    __tablename__ = "State"
    name = Column(String(128), nullable=False)


    """ State class """
    name = ""
