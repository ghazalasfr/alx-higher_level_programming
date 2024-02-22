#!/usr/bin/python3
"""
list all states filter states from db
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
                cities.id, cities.name
            FROM
                cities
            JOIN
                states
            ON
                cities.state_id = states.id
            WHERE
                states.name LIKE BINARY %(state_name)s
            ORDER BY
                cities.id ASC
        """, {
            'state_name': argv[4]
        })

        rows = tab.fetchall()

    if rows is not None:
        print(", ".join([i[1] for i in rows]))
