#!/usr/bin/python3
"""
list all values in the states
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

    tab = db.cursor()
    tab.execute("SELECT * FROM states \
                 WHERE name LIKE BINARY '{}' \
                 ORDER BY states.id ASC".format(argv[4]))
    rows = tab.fetchall()

    for i in rows:
        print(i)
