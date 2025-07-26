#!/usr/bin/python3
"""
This module contains the class definition of a City that inherits from Base
imported from model_state for SQLAlchemy ORM.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """
    City class that represents the cities table in MySQL database.

    Attributes:
        id: Auto-generated unique integer primary key that cannot be null
        name: String column with maximum 128 characters that cannot be null
        state_id: Integer foreign key that references states.id,
        cannot be null
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
