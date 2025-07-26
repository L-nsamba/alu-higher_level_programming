#!/usr/bin/python3
"""
This script deletes all State objects with a name containing the letter 'a'
from the database hbtn_0e_6_usa using SQLAlchemy ORM.
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def delete_states_with_a():
    """
    Connects to MySQL database using SQLAlchemy and deletes all State objects
    that contain the letter 'a' in their name.
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

    # Query and delete all State objects that contain the letter 'a'
    states_to_delete = session.query(State).filter(
        State.name.contains('a')
    ).all()

    # Delete each state
    for state in states_to_delete:
        session.delete(state)

    # Commit the changes
    session.commit()

    # Close session
    session.close()


if __name__ == "__main__":
    delete_states_with_a()
