#!/usr/bin/python3
"""
This module connects to a MySQL database and safely retrieves states
that match a given name from the states table, protected from SQL injection.
"""

import MySQLdb
import sys


def safe_filter_states():
    """
    Connects to MySQL database and displays all values in the states table
    where name matches the provided argument, sorted by states.id in
    ascending order. Uses parameterized queries to prevent SQL injection.
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

    # Create safe SQL query using parameterized query
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"

    # Execute the query with parameter (safe from SQL injection)
    cursor.execute(query, (state_name,))

    # Fetch all results
    results = cursor.fetchall()

    # Display results
    for row in results:
        print(row)

    # Close cursor and database connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    safe_filter_states()
