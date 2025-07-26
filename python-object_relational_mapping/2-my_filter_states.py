#!/usr/bin/python3
""" 2-my_filter_states.py """


import MySQLdb
import sys


def select_states():
    """ lists all states that matches arvg[4]
            from the database
    """
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3]
                         )
    cur = db.cursor()

    sql = "SELECT * FROM states\
        WHERE BINARY name='{:s}' ORDER BY id"\
        .format(sys.argv[4])

    cur.execute(sql)

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    select_states()
