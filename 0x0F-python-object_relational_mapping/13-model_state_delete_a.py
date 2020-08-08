#!/usr/bin/python3
"""[ a script that deletes all State objects with a name
    containing the letter a from the database hbtn_0e_6_usa]
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
    for state in session.query(State).order_by(
                  State.id).filter(State.name.like('%a%')):
        session.delete(state)
    session.commit()
    session.close()
