#!/usr/bin/python3
"""
This script prints the first State object from the database hbtn_0e_6_usa
using SQLAlchemy ORM.
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def fetch_first_state():
    """
    Connects to MySQL database using SQLAlchemy and prints the first State
    object sorted by states.id. If no states exist, prints 'Nothing'.
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

    # Query first State object ordered by id (limit to 1 record)
    first_state = session.query(State).order_by(State.id).first()

    # Display result
    if first_state is not None:
        print("{}: {}".format(first_state.id, first_state.name))
    else:
        print("Nothing")

    # Close session
    session.close()


if __name__ == "__main__":
    fetch_first_state()
