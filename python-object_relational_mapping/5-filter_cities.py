#!/usr/bin/python3
"""
This module connects to a MySQL database and lists all cities
of a specific state, protected from SQL injection.
"""

import MySQLdb
import sys


def filter_cities_by_state():
    """
    Connects to MySQL database and displays all cities of a specific state,
    sorted by cities.id in ascending order, safe from SQL injection.
    """
    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

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

    # Create safe SQL query using parameterized query with JOIN
    query = """SELECT cities.name
               FROM cities
               JOIN states ON cities.state_id = states.id
               WHERE states.name = %s
               ORDER BY cities.id ASC"""

    # Execute the query with parameter (safe from SQL injection)
    cursor.execute(query, (state_name,))

    # Fetch all results
    results = cursor.fetchall()

    # Extract city names and join with commas
    city_names = [row[0] for row in results]
    if city_names:
        print(", ".join(city_names))
    else:
        print()

    # Close cursor and database connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    filter_cities_by_state()
