#!/usr/bin/python3
"""[a script that lists all City objects
    from the database hbtn_0e_101_usa]
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
    st = session.query(State).order_by(State.id).all()
    for s in st:
        for c in s.cities:
            print("{}: {} -> {}".format(c.id, c.name, s.name))
    session.close()
