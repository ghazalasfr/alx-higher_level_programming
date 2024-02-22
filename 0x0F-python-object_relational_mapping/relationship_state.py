#!/usr/bin/python3
"""
This script defines a State class
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """State class
        __tablename__ (str): ...
        id (int): ...
        name (str): ...
        cities (:obj:`City`): ...
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")
