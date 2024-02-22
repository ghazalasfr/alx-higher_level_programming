#!/usr/bin/python3
"""
display all states from db
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Access to the database
    """

    db = MySQLdb.connect(host="localhost", user=argv[1],
                         passwd=argv[2], db=argv[3])

    with db.cursor() as tab:
        tab.execute("""
            SELECT
                cities.id, cities.name, states.name
            FROM
                cities
            JOIN
                states
            ON
                cities.state_id = states.id
            ORDER BY
                cities.id ASC
        """)

        rows = tab.fetchall()

    if rows is not None:
        for i in rows:
            print(i)
