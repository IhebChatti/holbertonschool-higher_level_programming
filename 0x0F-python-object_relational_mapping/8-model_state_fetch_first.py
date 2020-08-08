#!/usr/bin/python3
"""[a script that prints the first State object
    from the database hbtn_0e_6_usa]
"""

import sys
from sqlalchemy import create_engine
from model_state import State, Base
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
    for state in session.query(State).filter(State.id == 1):
        if state is None:
            print("Nothing")
        print("{}: {}".format(state.id, state.name))
    session.close()
