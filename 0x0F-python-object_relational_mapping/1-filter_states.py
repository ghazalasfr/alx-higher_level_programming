#!/usr/bin/python3
"""
list all starting with N from data
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Access to the database
    """
    db = MySQLdb.connect(host="localhost", user=argv[1],
                         passwd=argv[2], db=argv[3])

    tab = db.cursor()
    tab.execute("SELECT * FROM states \
                 WHERE name LIKE BINARY 'N%' \
                 ORDER BY states.id ASC")
    rows = tab.fetchall()

    for i in rows:
        print(i)
