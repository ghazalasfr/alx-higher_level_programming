#!/usr/bin/python3
"""
 City class
"""

from model_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """City class

    Attributes:
        __tablename__ (str): ...
        id (int): ...
        name (str): ...
        state_id (int): ...

    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

