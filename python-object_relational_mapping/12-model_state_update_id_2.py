#!/usr/bin/python3
"""
This script changes the name of a State object from the database hbtn_0e_6_usa
using SQLAlchemy ORM.
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def update_state_id_2():
    """
    Connects to MySQL database using SQLAlchemy and changes the name of the
    State object where id = 2 to 'New Mexico'.
    """
    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create engine to connect to MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        username, password, database), pool_pre_ping=True)

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the State object with id = 2
    state_to_update = session.query(State).filter(State.id == 2).first()

    # Update the name if the state exists
    if state_to_update is not None:
        state_to_update.name = "New Mexico"
        session.commit()

    # Close session
    session.close()


if __name__ == "__main__":
    update_state_id_2()
