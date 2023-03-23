#!/usr/bin/python3

# Lists all states from the database hbtn_0e_0_usa.
# Usage: ./0-select_states.py <mysql username> <mysql password> <database name>

import MySQLdb
import sys

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]

    db = MySQLdb.connect(host='localhost', port=3306,
                         user=username, passwd=password, db=dbname)
    cursor = db.cursor()

    cursor.execute('SELECT * FROM states ORDER BY id ASC')
    results = cursor.fetchall()

    for row in results:
        print(row)

    cursor.close()
    db.close()
