#!/usr/bin/python3
"""connect database."""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
"""
create
class to relate with
database
"""
Base = declarative_base()


class State(Base):
    """cretaes table."""

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    name = Column(String(128), nullable=False)
