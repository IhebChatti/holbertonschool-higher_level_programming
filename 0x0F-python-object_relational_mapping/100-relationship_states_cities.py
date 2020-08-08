#!/usr/bin/python3
"""[a script that creates the State “California”with the
    City “San Francisco” from the database hbtn_0e_100_usa]
"""

import sys
from sqlalchemy import create_engine
from relationship_state import State, Base
from relationship_city import City
from sqlalchemy.orm import Session

if __name__ == "__main__":
    args = sys.argv
    username = args[1]
    password = args[2]
    dbname = args[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, password, dbname),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    session.add(City(name="San Francisco", state=State(name="California")))
    session.commit()
    session.close()
