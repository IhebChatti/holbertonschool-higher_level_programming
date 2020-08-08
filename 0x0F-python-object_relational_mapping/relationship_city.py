#!/usr/bin/python3
"""[a python file that contains the class definition of a city
    and an instance Base = declarative_base()]
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base, State


class City(Base):
    """[City class]

    Args:
        Base ([object]): [declarative_base]
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"))
