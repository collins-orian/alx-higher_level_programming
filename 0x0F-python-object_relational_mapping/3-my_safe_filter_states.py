#!/usr/bin/python3

# script that lists all states from the database

import MySQLdb
from sys import argv
import re

if __name__ == "__main__":
    if (len(argv) != 5):
        print('Use: username, password, database name, state name')
        exit(1)

    searched = ' '.join(argv[4].split())

    if (re.search('^[a-zA-Z ]+$', searched) is None):
        print('Enter a valid name state (example: Arizona)')
        exit(1)
    con = MySQLdb.connect(
        host="localhost", port=3306, user=argv[1],
        password=argv[2], database=argv[3])
    cursor = con.cursor()
    cursor.execute(
        "SELECT * FROM states WHERE name = {:s} ORDER BY id ASC;".format(argv[4]))
    db = cursor.fetchall()
    for i in db:
        print(i)
    cursor.close()
    con.close()
