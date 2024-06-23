#!/usr/bin/python3
"""
This scripts defines a City class
to work with MySQLAlchemy ORM.
"""

from model_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """City classs

    Attributes:
        __tablename__ (str): The table name of the classes
        id (int): The id of the classes
        name (str): The name of the claesss
        state_id (int): The state the city belongs to

    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
