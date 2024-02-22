#!/usr/bin/python3
"""
displays all values in the states
where `name` matches the argument

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
                *
            FROM
                states
            WHERE
                name LIKE BINARY %(name)s
            ORDER BY
                states.id ASC
        """, {
            'name': argv[4]
        })

        rows = tab.fetchall()

    if rows is not None:
        for i in rows:
            print(i)
