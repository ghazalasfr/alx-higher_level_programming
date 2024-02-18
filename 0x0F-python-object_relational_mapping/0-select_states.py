#!/usr/bin/python3
"""
it's for list all tables of the database 
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Access to the database and get the states.
    """
    db = MySQLdb.connect(host="localhost", user=argv[1],
                         passwd=argv[2], db=argv[3])

    tab = db.cursor()
    tab.execute("SELECT * FROM states")
    rows = tab.fetchall()

    for i in rows:
        print(i)
