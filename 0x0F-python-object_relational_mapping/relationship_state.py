#!/usr/bin/python3
"""[a python file that contains the class definition of a State
    and an instance Base = declarative_base()]
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """[State class]

    Args:
        Base ([object]): [declarative_base]
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")
