#!/usr/bin/python3
"""
This module connects to a MySQL database and lists all cities
from the database with their corresponding state names.
"""

import MySQLdb
import sys


def list_cities_by_state():
    """
    Connects to MySQL database and displays all cities with their
    corresponding state names, sorted by cities.id in ascending order.
    """
    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Create cursor object
    cursor = db.cursor()

    # Create SQL query to join cities and states tables
    query = """SELECT cities.id, cities.name, states.name
               FROM cities
               JOIN states ON cities.state_id = states.id
               ORDER BY cities.id ASC"""

    # Execute the query
    cursor.execute(query)

    # Fetch all results
    results = cursor.fetchall()

    # Display results
    for row in results:
        print(row)

    # Close cursor and database connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    list_cities_by_state()
