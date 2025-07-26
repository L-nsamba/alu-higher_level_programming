#!/usr/bin/python3
"""
This module contains the class definition of a State and an instance
Base = declarative_base() for SQLAlchemy ORM.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    State class that represents the states table in MySQL database.

    Attributes:
        id: Auto-generated unique integer primary key that cannot be null
        name: String column with maximum 128 characters that cannot be null
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
