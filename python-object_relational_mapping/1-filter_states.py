#!/usr/bin/python3
"""
This script lists all states with names starting with 'N' from the database
hbtn_0e_0_usa. It takes 3 arguments: mysql username, mysql password and
database name. The script connects to a MySQL server running on localhost
at port 3306. Results are sorted in ascending order by states.id.
"""

import MySQLdb
import sys


def filter_states(username, password, db_name):
    """
    Connects to MySQL database and lists states with
    names starting with 'N'.

    Args:
        username (str): MySQL username
        password (str): MySQL password
        db_name (str): Database name
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

        # Execute SQL query to select states starting with uppercase 'N'
        query = """SELECT * FROM states WHERE name
                 LIKE BINARY 'N%' ORDER BY id ASC"""
        cursor.execute(query)

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
    if len(sys.argv) == 4:
        filter_states(sys.argv[1], sys.argv[2], sys.argv[3])
