#!/usr/bin/python3
"""
This script prints the State object with the name passed as argument
from the database hbtn_0e_6_usa using SQLAlchemy ORM.
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def get_state_by_name():
    """
    Connects to MySQL database using SQLAlchemy and finds the State object
    with the specified name. Displays the state's ID or 'Not found' if
    no matching state exists. Safe from SQL injection.
    """
    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Create engine to connect to MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        username, password, database), pool_pre_ping=True)

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query State object with the specified name (SQL injection safe)
    state = session.query(State).filter(State.name == state_name).first()

    # Display result
    if state is not None:
        print(state.id)
    else:
        print("Not found")

    # Close session
    session.close()


if __name__ == "__main__":
    get_state_by_name()
