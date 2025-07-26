#!/usr/bin/python3
"""
This script prints all City objects from the database hbtn_0e_14_usa
with their corresponding state names using SQLAlchemy ORM.
"""

import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def fetch_cities_by_state():
    """
    Connects to MySQL database using SQLAlchemy
    and displays all City objects
    with their corresponding state names,
    sorted by cities.id in ascending order.
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

    # Query cities with their states using JOIN
    results = session.query(City, State).join(State).order_by(City.id).all()

    # Display results in the required format
    for city, state in results:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    # Close session
    session.close()


if __name__ == "__main__":
    fetch_cities_by_state()
