#!/usr/bin/python3
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
"""
create
class to relate with
database
"""
Base = declarative_base()


class City(Base):
    """
    cretaes
    table
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
