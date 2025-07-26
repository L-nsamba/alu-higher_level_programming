#!/usr/bin/python3
"""
This script lists all states matching the provided name argument from the
database hbtn_0e_0_usa. It takes 4 arguments: mysql username, password,
database name, and state name to search. Results are sorted by states.id.
"""

import MySQLdb
import sys


def filter_states_by_name(username, password, db_name, state_name):
    """
    Connects to MySQL database and lists states matching the given name.

    Args:
        username (str): MySQL username
        password (str): MySQL password
        db_name (str): Database name
        state_name (str): State name to search for
    """
    try:
        # Connect to MySQL database
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=db_name
        )

        # Create a cursor object
        cursor = db.cursor()

        # Execute SQL query with user input safely using format
        query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
        cursor.execute(query, (state_name,))

        # Fetch all rows
        rows = cursor.fetchall()

        # Display results
        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        print(f"Error connecting to MySQL: {e}")
    finally:
        # Close database connection
        if 'db' in locals():
            db.close()


if __name__ == "__main__":
    if len(sys.argv) == 5:
        filter_states_by_name(
            sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
        )
