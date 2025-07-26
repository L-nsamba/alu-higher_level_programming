#!/usr/bin/python3
"""
This script searches for states matching a given name in the
hbtn_0e_0_usa database. It takes 4 arguments: MySQL username,
password, database name, and state name to search.
Results are displayed sorted by state ID in ascending order.
"""

import MySQLdb
import sys


def search_states(username, password, db_name, state_name):
    """
    Connects to MySQL database and searches for states matching the given name.
    
    Args:
        username (str): MySQL username
        password (str): MySQL password
        db_name (str): Database name
        state_name (str): State name to search for
    """
    try:
        # Establish database connection
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=db_name
        )
        
        # Create cursor object
        cursor = db.cursor()
        
        # Create and execute SQL query using format
        query = "SELECT * FROM states WHERE BINARY name = '{}' ORDER BY id ASC"
        cursor.execute(query.format(state_name))
        
        # Fetch and display results
        results = cursor.fetchall()
        for row in results:
            print(row)
            
    except MySQLdb.Error as e:
        print("MySQL Error:", e)
    finally:
        # Close database connection
        if 'db' in locals():
            db.close()


if __name__ == "__main__":
    if len(sys.argv) == 5:
        search_states(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
