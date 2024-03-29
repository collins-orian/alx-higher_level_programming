#!/usr/bin/python3

# Lists all states from the database hbtn_0e_0_usa.
# Usage: ./0-select_states.py <mysql username> <mysql password> <database name>

import MySQLdb as msdb
from sys import argv

if __name__ == '__main__':
    username = argv[1]
    password = argv[2]
    dbname = argv[3]

    try:
        con = msdb.connect(host='localhost', port=3306,
                           user=username, passwd=password, db=dbname)
    except Exception:
        print("Failed to connect to the database")
        exit(0)
    cursor = con.cursor()

    cursor.execute('SELECT * FROM states ORDER BY id ASC;')
    results = cursor.fetchall()

    for row in results:
        print(row)

    cursor.close()
    con.close()
